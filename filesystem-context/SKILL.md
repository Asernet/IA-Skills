---
name: filesystem-context
description: Usa questa skill per offloadare il contesto su file, usare il filesystem come memoria o persistenza output.
---

# Context Engineering Basato su Filesystem

Il filesystem fornisce un'interfaccia singola attraverso la quale gli agenti possono flessibilmente memorizzare, recuperare e aggiornare una quantità effettivamente illimitata di contesto. Questo pattern indirizza il vincolo fondamentale che le finestre di contesto sono limitate mentre i task richiedono spesso più informazioni di quante ne stiano in una singola finestra.

L'insight centrale è che i file abilitano la scoperta dinamica del contesto: gli agenti tirano contesto rilevante su richiesta piuttosto che portare tutto nella finestra di contesto. Questo contrasta con il contesto statico, che è sempre incluso indipendentemente dalla rilevanza.

## Quando Attivare

Attiva questa skill quando:

- Gli output dei tool stanno gonfiando la finestra di contesto
- Gli agenti devono persistere lo stato attraverso lunghe traiettorie
- I sub-agenti devono condividere informazioni senza passaggio diretto di messaggi
- I task richiedono più contesto di quanto ne stia nella finestra
- Costruisci agenti che imparano e aggiornano le proprie istruzioni
- Implementi scratch pad per risultati intermedi
- Output terminale o log necessitano di essere accessibili agli agenti

## Concetti Chiave

Il context engineering può fallire in quattro modi prevedibili. Primo, quando il contesto di cui un agente ha bisogno non è nel contesto totale disponibile. Secondo, quando il contesto recuperato fallisce nell'incapsulare il contesto necessario. Terzo, quando il contesto recuperato supera di molto il contesto necessario, sprecando token e degradando le performance. Quarto, quando gli agenti non possono scoprire informazioni di nicchia sepolte in molti file.

Il filesystem indirizza questi fallimenti fornendo un layer persistente dove gli agenti scrivono una volta e leggono selettivamente, scaricando contenuto in massa mentre preservano l'abilità di recuperare informazioni specifiche attraverso tool di ricerca.

## Argomenti Dettagliati

### Il Trade-off Contesto Statico vs Dinamico

**Contesto Statico**
Il contesto statico è sempre incluso nel prompt: istruzioni di sistema, definizioni tool e regole critiche. Il contesto statico consuma token indipendentemente dalla rilevanza del task. Man mano che gli agenti accumulano più capacità (tool, skill, istruzioni), il contesto statico cresce e affolla lo spazio per informazioni dinamiche.

**Scoperta Contesto Dinamico**
Il contesto dinamico è caricato su richiesta quando rilevante per il task corrente. L'agente riceve puntatori statici minimi (nomi, descrizioni, percorsi file) e usa tool di ricerca per caricare contenuto completo quando necessario.

La scoperta dinamica è più efficiente in termini di token perché solo i dati necessari entrano nella finestra di contesto. Può anche migliorare la qualità della risposta riducendo informazioni potenzialmente confuse o contraddittorie.

Il trade-off: la scoperta dinamica richiede che il modello identifichi correttamente quando caricare contesto addizionale. Questo funziona bene con gli attuali modelli di frontiera ma può fallire con modelli meno capaci che non riconoscono quando hanno bisogno di più informazioni.

### Pattern 1: Filesystem come Scratch Pad

**Il Problema**
Le chiamate ai tool possono ritornare output massicci. Una ricerca web può ritornare 10k token di contenuto grezzo. Una query database può ritornare centinaia di righe. Se questo contenuto entra nella cronologia messaggi, rimane per l'intera conversazione, gonfiando i costi dei token e potenzialmente degradando l'attenzione a informazioni più rilevanti.

**La Soluzione**
Scrivi grandi output tool su file invece di ritornarli direttamente al contesto. L'agente usa quindi recupero mirato (grep, line-specific reads) per estrarre solo le porzioni rilevanti.

**Implementazione**

```python
def handle_tool_output(output: str, threshold: int = 2000) -> str:
    if len(output) < threshold:
        return output

    # Write to scratch pad
    file_path = f"scratch/{tool_name}_{timestamp}.txt"
    write_file(file_path, output)

    # Return reference instead of content
    key_summary = extract_summary(output, max_tokens=200)
    return f"[Output written to {file_path}. Summary: {key_summary}]"
```

L'agente può quindi usare `grep` per cercare pattern specifici o `read_file` con range di righe per recuperare sezioni mirate.

**Benefici**

- Riduce accumulo token su lunghe conversazioni
- Preserva output completo per riferimento successivo
- Abilita recupero mirato invece di portare tutto

### Pattern 2: Persistenza Piano

**Il Problema**
Task a lungo orizzonte richiedono che gli agenti facciano piani e li seguano. Ma man mano che le conversazioni si estendono, i piani possono cadere fuori dall'attenzione o essere persi col riassunto. L'agente perde traccia di ciò che supponeva di fare.

**La Soluzione**
Scrivi piani sul filesystem. L'agente può rileggere il suo piano in qualsiasi punto, ricordando a se stesso l'obiettivo corrente e il progresso. Questo è a volte chiamato "manipolare l'attenzione attraverso la recitazione".

**Implementazione**
Memorizza piani in formato strutturato:

```yaml
# scratch/current_plan.yaml
objective: "Refactor authentication module"
status: in_progress
steps:
  - id: 1
    description: "Audit current auth endpoints"
    status: completed
  - id: 2
    description: "Design new token validation flow"
    status: in_progress
  - id: 3
    description: "Implement and test changes"
    status: pending
```

L'agente legge questo file all'inizio di ogni turno o quando ha bisogno di ri-orientarsi.

### Pattern 3: Comunicazione Sub-Agente via Filesystem

**Il Problema**
In sistemi multi-agente, i sub-agenti tipicamente riportano scoperte a un coordinatore attraverso passaggio messaggi. Questo crea un "gioco del telefono" dove l'informazione degrada attraverso riassunto ad ogni salto.

**La Soluzione**
I sub-agenti scrivono le loro scoperte direttamente sul filesystem. Il coordinatore legge questi file direttamente, bypassando il passaggio messaggi intermedio. Questo preserva la fedeltà e riduce l'accumulo di contesto nel coordinatore.

**Implementazione**

```
workspace/
  agents/
    research_agent/
      findings.md        # Research agent writes here
      sources.jsonl      # Source tracking
    code_agent/
      changes.md         # Code agent writes here
      test_results.txt   # Test output
  coordinator/
    synthesis.md         # Coordinator reads agent outputs, writes synthesis
```

Ogni agente opera in isolamento relativo ma condivide lo stato attraverso il filesystem.

### Pattern 4: Caricamento Dinamico Skill

**Il Problema**
Gli agenti possono avere molte skill o set di istruzioni, ma la maggior parte sono irrilevanti per ogni dato task. Riempire tutte le istruzioni nel prompt di sistema spreca token e può confondere il modello con guida contraddittoria o irrilevante.

**La Soluzione**
Memorizza skill come file. Includi solo nomi skill e brevi descrizioni nel contesto statico. L'agente usa tool di ricerca per caricare contenuto skill rilevante quando il task lo richiede.

**Implementazione**
Il contesto statico include:

```
Available skills (load with read_file when relevant):
- database-optimization: Query tuning and indexing strategies
- api-design: REST/GraphQL best practices
- testing-strategies: Unit, integration, and e2e testing patterns
```

L'agente carica `skills/database-optimization/SKILL.md` solo quando lavora su task database.

### Pattern 5: Persistenza Terminale e Log

**Il Problema**
L'output terminale da processi long-running si accumula rapidamente. Copiare e incollare output nell'input agente è manuale e inefficiente.

**La Soluzione**
Sincronizza output terminale su file automaticamente. L'agente può allora fare grep per sezioni rilevanti (messaggi errore, comandi specifici) senza caricare intere cronologie terminale.

**Implementazione**
Le sessioni terminale sono persistite come file:

```
terminals/
  1.txt    # Terminal session 1 output
  2.txt    # Terminal session 2 output
```

Gli agenti interrogano con grep mirato:

```bash
grep -A 5 "error" terminals/1.txt
```

### Pattern 6: Apprendimento Attraverso Auto-Modifica

**Il Problema**
Gli agenti mancano spesso di contesto che gli utenti forniscono implicitamente o esplicitamente durante le interazioni. Tradizionalmente, questo richiede aggiornamenti manuali del prompt di sistema tra le sessioni.

**La Soluzione**
Gli agenti scrivono informazioni apprese nei propri file di istruzioni. Sessioni successive caricano questi file, incorporando contesto appreso automaticamente.

**Implementazione**
Dopo che l'utente fornisce preferenza:

```python
def remember_preference(key: str, value: str):
    preferences_file = "agent/user_preferences.yaml"
    prefs = load_yaml(preferences_file)
    prefs[key] = value
    write_yaml(preferences_file, prefs)
```

Sessioni successive includono un passaggio per caricare preferenze utente se il file esiste.

**Attenzione**
Questo pattern è ancora emergente. L'auto-modifica richiede guardrails attenti per prevenire che gli agenti accumulino istruzioni non corrette o contraddittorie nel tempo.

### Tecniche Ricerca Filesystem

I modelli sono specificamente addestrati per comprendere l'attraversamento del filesystem. La combinazione di `ls`, `glob`, `grep`, e `read_file` con range di righe fornisce potente scoperta contesto:

- `ls` / `list_dir`: Scopri struttura directory
- `glob`: Trova file che corrispondono a pattern (es., `**/*.py`)
- `grep`: Cerca contenuti file per pattern, ritorna righe corrispondenti
- `read_file` con range: Leggi specifici range di righe senza caricare interi file

Questa combinazione spesso supera la ricerca semantica per contenuto tecnico (codice, API docs) dove il significato semantico è sparso ma i pattern strutturali sono chiari.

Ricerca semantica e ricerca filesystem funzionano bene insieme: ricerca semantica per query concettuali, ricerca filesystem per query strutturali ed exact-match.

## Guida Pratica

### Quando Usare Contesto Filesystem

**Usa pattern filesystem quando:**

- Output tool superano 2000 token
- Task spaziano multipli turni conversazione
- Agenti multipli devono condividere stato
- Skill o istruzioni superano ciò che sta comodamente nel prompt di sistema
- Log o output terminale necessitano querying selettivo

**Evita pattern filesystem quando:**

- Task completano in singoli turni
- Contesto sta comodamente nella finestra
- Latenza è critica (I/O file aggiunge overhead)
- Modello semplice incapace di uso tool filesystem

### Organizzazione File

Struttura file per scopribilità:

```
project/
  scratch/           # Temporary working files
    tool_outputs/    # Large tool results
    plans/           # Active plans and checklists
  memory/            # Persistent learned information
    preferences.yaml # User preferences
    patterns.md      # Learned patterns
  skills/            # Loadable skill definitions
  agents/            # Sub-agent workspaces
```

Usa convenzioni di naming consistenti. Includi timestamp o ID in file scratch per disambiguazione.

### Contabilità Token

Traccia da dove originano i token:

- Misura rapporto contesto statico vs dinamico
- Monitora dimensioni output tool prima e dopo offloading
- Traccia quanto spesso il contesto dinamico è effettivamente caricato

Ottimizza basato su misurazioni, non assunzioni.

## Esempi

**Esempio 1: Offloading Output Tool**

```
Input: Web search returns 8000 tokens
Before: 8000 tokens added to message history
After:
  - Write to scratch/search_results_001.txt
  - Return: "[Results in scratch/search_results_001.txt. Key finding: API rate limit is 1000 req/min]"
  - Agent greps file when needing specific details
Result: ~100 tokens in context, 8000 tokens accessible on demand
```

**Esempio 2: Caricamento Dinamico Skill**

```
Input: User asks about database indexing
Static context: "database-optimization: Query tuning and indexing"
Agent action: read_file("skills/database-optimization/SKILL.md")
Result: Full skill loaded only when relevant
```

**Esempio 3: Cronologia Chat come Riferimento File**

```
Trigger: Context window limit reached, summarization required
Action:
  1. Write full history to history/session_001.txt
  2. Generate summary for new context window
  3. Include reference: "Full history in history/session_001.txt"
Result: Agent can search history file to recover details lost in summarization
```

## Linee Guida

1. Scrivi grandi output su file; ritorna riassunti e riferimenti al contesto
2. Memorizza piani e stato in file strutturati per rilettura
3. Usa workspace file sub-agente invece di catene messaggi
4. Carica skill dinamicamente piuttosto che riempire tutto nel prompt di sistema
5. Persisti output terminale e log come file ricercabili
6. Combina grep/glob con ricerca semantica per scoperta comprensiva
7. Organizza file per scopribilità agente con naming chiaro
8. Misura risparmio token per validare che i pattern filesystem siano efficaci
9. Implementa cleanup per file scratch per prevenire crescita illimitata
10. Proteggi pattern auto-modifica con validazione

## Integrazione

Questa skill si connette a:

- **context-optimization** - Offloading filesystem è una forma di mascheramento osservazioni
- **memory-systems** - Filesystem-as-memory è un semplice layer di memoria
- **multi-agent-patterns** - Workspace file sub-agente abilitano isolamento
- **context-compression** - Riferimenti file abilitano "compressione" lossless
- **tool-design** - I tool dovrebbero ritornare riferimenti file per grandi output

## Riferimenti

Riferimento interno:

- [Implementation Patterns](./references/implementation-patterns.md) - Implementazioni pattern dettagliate

Skill correlate in questa collezione:

- context-optimization - Tecniche riduzione token
- memory-systems - Pattern storage persistente
- multi-agent-patterns - Coordinamento agente

Risorse esterne:

- LangChain Deep Agents: How agents can use filesystems for context engineering
- Cursor: Dynamic context discovery patterns
- Anthropic: Agent Skills specification
