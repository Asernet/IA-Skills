---
name: writing-skills
description: Usa per creare, modificare o verificare skill (Compatibile Gemini & Claude).
---

# Scrivere Skill (Gemini & Claude)

## Protocollo di Avvio

**Appena attivi questa skill, DEVI chiedere all'utente:**
> "Per quale AI stai scrivendo questa skill? (Gemini o Claude)"

Questa risposta determinerà:
1.  Quale guida alle best practices consultare (`gemini-best-practices.md` vs `anthropic-best-practices.md`).
2.  Dove salvare i file (`~/.gemini/skills` vs `~/.claude/skills`).
3.  Quali modelli suggerire per i test.

**AUTOMAZIONE DELIVERY (Solo Anthropic):**
Se il target è **Claude/Anthropic**, al termine del processo (dopo verfica/ingegnerizzazione), DEVI AUTOMATICAMENTE:
1.  Creare un archivio ZIP dell'intera cartella della skill.
2.  Spostare lo ZIP file nella cartella Downloads dell'utente (`C:\Users\M.Macelloni\Downloads` su questo sistema).
3.  Notificare l'utente che il file è pronto per l'installazione manuale su Claude Desktop.

## Panoramica

**Scrivere skill È Test-Driven Development applicato alla documentazione di processo.**

**Le skill personali vivono in directory specifiche per agente:**
- **Gemini**: `~/.gemini/skills` (o `C:\Users\Utente\.gemini\skills` su Windows)
- **Claude Code**: `~/.claude/skills`
- **Codex**: `~/.codex/skills`

Scrivi casi test (scenari pressione con subagenti), guardali fallire (comportamento baseline), scrivi la skill (documentazione), guarda i test passare (agenti si conformano), e rifattorizza (chiudi scappatoie).

**Principio core:** Se non hai guardato un agente fallire senza la skill, non sai se la skill insegna la cosa giusta.

**BACKGROUND RICHIESTO:** DEVI capire superpowers:test-driven-development prima di usare questa skill. Quella skill definisce il ciclo fondamentale RED-GREEN-REFACTOR. Questa skill adatta TDD alla documentazione.

**Guide ufficiali:**
- **Per Gemini**: vedi [gemini-best-practices.md](gemini-best-practices.md)
- **Per Anthropic**: vedi [anthropic-best-practices.md](anthropic-best-practices.md)

## Cos'è una Skill?

Una **skill** è una guida di riferimento per tecniche provate, pattern o tool. Le skill aiutano future istanze (Gemini o Claude) a trovare e applicare approcci efficaci.

**Le skill sono:** Tecniche riutilizzabili, pattern, tool, guide riferimento

**Le skill NON sono:** Narrative su come hai risolto un problema una volta

## Mappatura TDD per Skill

| Concetto TDD | Creazione Skill |
| :--- | :--- |
| **Caso Test** | Scenario pressione con subagente |
| **Codice Produzione** | Documento skill (SKILL.md) |
| **Test fallisce (RED)** | Agente viola regola senza skill (baseline) |
| **Test passa (GREEN)** | Agente si conforma con skill presente |
| **Refactor** | Chiudi scappatoie mantenendo conformità |
| **Scrivi test prima** | Esegui scenario baseline PRIMA di scrivere skill |
| **Guardalo fallire** | Documenta esatte razionalizzazioni che agente usa |
| **Codice minimo** | Scrivi skill indirizzando quelle specifiche violazioni |
| **Guardalo passare** | Verifica agente ora si conforma |
| **Ciclo Refactor** | Trova nuove razionalizzazioni → tappa → ri-verifica |

L'intero processo creazione skill segue RED-GREEN-REFACTOR.

## Quando Creare una Skill

**Crea quando:**

- La tecnica non era intuitivamente ovvia a te
- Referenzieresti questo ancora attraverso progetti
- Il pattern si applica largamente (non specifico progetto)
- Altri beneficerebbero

**Non creare per:**

- Soluzioni one-off
- Pratiche standard ben documentate altrove
- Convenzioni specifiche progetto (metti in `GEMINI.md` o `CLAUDE.md`)
- Vincoli meccanici (se è applicabile con regex/validazione, automatizzalo—salva documentazione per chiamate di giudizio)

## Struttura SKILL.md

**Frontmatter (YAML):**

- Solo due campi supportati: `name` e `description`
- Max 1024 caratteri totali
- `name`: Usa lettere, numeri e trattini solo (niente parentesi, caratteri speciali)
- `description`: Terza persona, descrive SOLO quando usare (NON cosa fa)
  - Inizia con "Use when..." per focalizzare su condizioni innesco
  - Includi sintomi specifici, situazioni e contesti
  - **MAI riassumere il processo o workflow della skill**
  - Mantieni sotto 500 caratteri se possibile

## Ottimizzazione Ricerca Skill (ASO - Agent Search Optimization)

**Critico per scoperta:** Il futuro agente (Gemini/Claude) deve TROVARE la tua skill

### 1. Campo Descrizione Ricco

**Scopo:** L'agente legge descrizione per decidere quali skill caricare per un dato task. Fai che risponda: "Dovrei leggere questa skill proprio ora?"

**Formato:** Inizia con "Use when..." per focalizzare su condizioni innesco

**CRITICO: Descrizione = Quando Usare, NON Cosa Fa la Skill**

La descrizione dovrebbe SOLO descrivere condizioni innesco. NON riassumere il processo o workflow della skill nella descrizione.

### 2. Copertura Keyword

Usa parole che l'agente cercherebbe:

- Messaggi errore: "Hook timed out", "ENOTEMPTY", "race condition"
- Sintomi: "flaky", "hanging", "zombie", "pollution"
- Sinonimi: "timeout/hang/freeze", "cleanup/teardown/afterEach"
- Tool: Comandi effettivi, nomi librerie, tipi file

### 3. Naming Descrittivo

**Usa voce attiva, verbo-prima:**

- ✅ `creating-skills` non `skill-creation`
- ✅ `condition-based-waiting` non `async-test-helpers`

### 4. Efficienza Token (Critico)

**Problema:** skill getting-started e frequentemente-referenziate caricano in OGNI conversazione. Ogni token conta.

**Target conteggio parole:**

- workflow getting-started: <150 parole ognuno
- skill frequentemente-caricate: <200 parole totale
- Altre skill: <500 parole (sii comunque conciso)

### 4. Cross-Referencing Altre Skill

**Quando scrivi documentazione che referenzia altre skill:**

Usa solo nome skill, con marker requisito espliciti:

- ✅ Buono: `**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development`
- ✅ Buono: `**REQUIRED BACKGROUND:** You MUST understand superpowers:systematic-debugging`
- ❌ Cattivo: `See skills/testing/test-driven-development` (non chiaro se richiesto)
- ❌ Cattivo: `@skills/testing/test-driven-development/SKILL.md` (forza caricamento, brucia contesto)

## Uso Flowchart

**Usa flowchart SOLO per:**

- Punti decisione non-ovvi
- Loop processo dove potresti fermarti troppo presto
- Decisioni "Quando usare A vs B"

**Mai usare flowchart per:**

- Materiale riferimento → Tabelle, liste
- Esempi codice → Blocchi Markdown
- Istruzioni lineari → Liste numerate
- Etichette senza significato semantico (step1, helper2)

## Organizzazione File

### Skill Auto-Contenuta

```
defense-in-depth/
  SKILL.md    # Tutto inline
```

Quando: Tutto contenuto ci sta, nessun riferimento pesante necessario

### Skill con Tool Riutilizzabile

```
condition-based-waiting/
  SKILL.md    # Panoramica + pattern
  example.ts  # Helper funzionanti da adattare
```

Quando: Tool è codice riutilizzabile, non solo narrativo

### Skill con Riferimento Pesante

```
pptx/
  SKILL.md       # Panoramica + workflow
  pptxgenjs.md   # 600 righe riferimento API
  ooxml.md       # 500 righe struttura XML
  scripts/       # Tool eseguibili
```

Quando: Materiale riferimento troppo grande per inline

## La Legge Ferrea (Stessa del TDD)

```
NESSUNA SKILL SENZA UN TEST FALLIMENTARE PRIMA
```

Questo si applica a NUOVE skill E MODIFICHE a skill esistenti.

Scrivi skill prima di testare? Cancellala. Ricomincia.
Edita skill senza testare? Stessa violazione.

**Nessuna eccezione:**

- Non per "aggiunte semplici"
- Non per "aggiungere solo una sezione"
- Non per "aggiornamenti documentazione"
- Non tenere cambiamenti non testati come "riferimento"
- Non "adattare" mentre esegui test
- Cancellare significa cancellare

**BACKGROUND RICHIESTO:** La skill superpowers:test-driven-development spiega perché questo importa. Stessi principi si applicano alla documentazione.

## Testare Tutti i Tipi Skill

Tipi skill diversi necessitano approcci test diversi. Testa con i modelli che intendi supportare (es. Gemini Flash, Pro, Ultra).

### Skill Rinforzo-Disciplina (regole/requisiti)

**Esempi:** TDD, verification-before-completion, designing-before-coding

**Testa con:**

- Domande accademiche: Capiscono le regole?
- Scenari pressione: Si conformano sotto stress?
- Pressioni multiple combinate: tempo + costi affondati + esaurimento
- Identifica razionalizzazioni e aggiungi counter espliciti

**Criteri successo:** Agente segue regola sotto massima pressione

### Skill Tecnica (guide how-to)

**Esempi:** condition-based-waiting, root-cause-tracing, defensive-programming

**Testa con:**

- Scenari applicazione: Possono applicare la tecnica correttamente?
- Scenari variazione: Gestiscono casi limite?
- Test informazione mancante: Le istruzioni hanno gap?

**Criteri successo:** Agente applica con successo tecnica a nuovo scenario

### Skill Pattern (modelli mentali)

**Esempi:** reducing-complexity, concetti information-hiding

**Testa con:**

- Scenari riconoscimento: Riconoscono quando il pattern si applica?
- Scenari applicazione: Possono usare il modello mentale?
- Contro-esempi: Sanno quando NON applicare?

**Criteri successo:** Agente identifica correttamente quando/come applicare pattern

### Skill Riferimento (documentazione/API)

**Esempi:** documentazione API, riferimenti comandi, guide libreria

**Testa con:**

- Scenari recupero: Possono trovare l'informazione giusta?
- Scenari applicazione: Possono usare cosa hanno trovato correttamente?
- Gap testing: Casi d'uso comuni sono coperti?

**Criteri successo:** Agente trova e applica correttamente informazione riferimento

## La Linea di Fondo

**Creare skill È TDD per documentazione di processo.**

Stessa Legge Ferrea: Nessuna skill senza test fallimentare prima.
Stesso ciclo: RED (baseline) → GREEN (scrivi skill) → REFACTOR (chiudi scappatoie).
Stessi benefici: Migliore qualità, meno sorprese, risultati a prova di proiettile.

Se segui TDD per il codice, seguilo per le skill. È la stessa disciplina applicata alla documentazione.
