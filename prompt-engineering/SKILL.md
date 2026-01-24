---
name: prompt-engineering
description: Guida esperta su pattern prompt engineering, best practice e tecniche di ottimizzazione. Utilizza quando l'utente vuole migliorare prompt, imparare strategie di prompting o debuggare comportamento agente.
---

# Pattern Prompt Engineering

Tecniche avanzate di prompt engineering per massimizzare performance, affidabilità e controllabilità degli LLM.

## Capacità Core

### 1. Apprendimento Few-Shot

Insegna al modello mostrando esempi invece di spiegare regole. Includi 2-5 coppie input-output che dimostrano il comportamento desiderato. Usa quando hai bisogno di formattazione consistente, pattern di ragionamento specifici o gestione casi limite. Più esempi migliorano l'accuratezza ma consumano token—bilancia in base alla complessità del task.

**Esempio:**

```markdown
Estrai informazioni chiave dai ticket di supporto:

Input: "Il mio login non funziona e continuo a ricevere errore 403"
Output: {"problema": "autenticazione", "codice_errore": "403", "priorità": "alta"}

Input: "Richiesta feature: aggiungi dark mode alle impostazioni"
Output: {"problema": "richiesta_feature", "codice_errore": null, "priorità": "bassa"}

Ora processa: "Non riesco a caricare file più grandi di 10MB, ricevo timeout"
```

### 2. Prompting Chain-of-Thought

Richiedi ragionamento step-by-step prima della risposta finale. Aggiungi "Pensiamo passo per passo" (zero-shot) o includi tracce di ragionamento di esempio (few-shot). Usa per problemi complessi che richiedono logica multi-step, ragionamento matematico, o quando devi verificare il processo di pensiero del modello. Migliora l'accuratezza sui task analitici del 30-50%.

**Esempio:**

```markdown
Analizza questo bug report e determina la causa root.

Pensa passo per passo:

1. Qual è il comportamento atteso?
2. Qual è il comportamento effettivo?
3. Cosa è cambiato di recente che potrebbe causare questo?
4. Quali componenti sono coinvolti?
5. Qual è la causa root più probabile?

Bug: "Gli utenti non riescono a salvare le bozze dopo il deploy dell'update cache di ieri"
```

### 3. Ottimizzazione Prompt

Migliora sistematicamente i prompt attraverso testing e raffinamento. Parti semplice, misura performance (accuratezza, consistenza, uso token), poi itera. Testa su input diversi inclusi casi limite. Usa A/B testing per confrontare variazioni. Critico per prompt in produzione dove consistenza e costi contano.

**Esempio:**

```markdown
Versione 1 (Semplice): "Riassumi questo articolo"
→ Risultato: Lunghezza inconsistente, manca punti chiave

Versione 2 (Aggiungi vincoli): "Riassumi in 3 bullet point"
→ Risultato: Struttura migliore, ma ancora manca sfumatura

Versione 3 (Aggiungi ragionamento): "Identifica le 3 scoperte principali, poi riassumi ciascuna"
→ Risultato: Consistente, accurato, cattura informazioni chiave
```

### 4. Sistemi Template

Costruisci strutture prompt riutilizzabili con variabili, sezioni condizionali e componenti modulari. Usa per conversazioni multi-turn, interazioni role-based, o quando lo stesso pattern si applica a input diversi. Riduce duplicazione e assicura consistenza tra task simili.

**Esempio:**

```python
# Template code review riutilizzabile
template = """
Rivedi questo codice {linguaggio} per {area_focus}.

Codice:
{blocco_codice}

Fornisci feedback su:
{checklist}
"""

# Utilizzo
prompt = template.format(
    linguaggio="Python",
    area_focus="vulnerabilità sicurezza",
    blocco_codice=user_code,
    checklist="1. SQL injection\n2. Rischi XSS\n3. Autenticazione"
)
```

### 5. Design System Prompt

Imposta comportamento globale e vincoli che persistono nella conversazione. Definisci ruolo del modello, livello expertise, formato output e linee guida sicurezza. Usa system prompt per istruzioni stabili che non dovrebbero cambiare turn-to-turn, liberando token user message per contenuto variabile.

**Esempio:**

```markdown
Sistema: Sei un senior backend engineer specializzato in API design.

Regole:

- Considera sempre scalabilità e performance
- Suggerisci pattern RESTful di default
- Segnala concern sicurezza immediatamente
- Fornisci esempi codice in Python
- Usa pattern early return

Formatta risposte come:

1. Analisi
2. Raccomandazione
3. Esempio codice
4. Trade-off
```

## Pattern Chiave

### Disclosure Progressiva

Parti con prompt semplici, aggiungi complessità solo quando necessario:

1. **Livello 1**: Istruzione diretta
   - "Riassumi questo articolo"

2. **Livello 2**: Aggiungi vincoli
   - "Riassumi in 3 bullet point, focus sulle scoperte chiave"

3. **Livello 3**: Aggiungi ragionamento
   - "Leggi l'articolo, identifica le scoperte principali, poi riassumi in 3 bullet point"

4. **Livello 4**: Aggiungi esempi
   - Includi 2-3 riassunti di esempio con coppie input-output

### Gerarchia Istruzioni

```
[Contesto Sistema] → [Istruzione Task] → [Esempi] → [Dati Input] → [Formato Output]
```

### Recupero Errori

Costruisci prompt che gestiscono fallimenti con grazia:

- Includi istruzioni fallback
- Richiedi score di confidence
- Chiedi interpretazioni alternative quando incerto
- Specifica come indicare informazioni mancanti

## Best Practice

1. **Sii Specifico**: Prompt vaghi producono risultati inconsistenti
2. **Mostra, Non Dire**: Gli esempi sono più efficaci delle descrizioni
3. **Testa Estensivamente**: Valuta su input diversi e rappresentativi
4. **Itera Rapidamente**: Piccoli cambiamenti possono avere grandi impatti
5. **Monitora Performance**: Traccia metriche in produzione
6. **Versiona**: Tratta i prompt come codice con versioning appropriato
7. **Documenta l'Intento**: Spiega perché i prompt sono strutturati così

## Trappole Comuni

- **Over-engineering**: Partire con prompt complessi prima di provare quelli semplici
- **Inquinamento esempi**: Usare esempi che non corrispondono al task target
- **Overflow contesto**: Superare limiti token con troppi esempi
- **Istruzioni ambigue**: Lasciare spazio a interpretazioni multiple
- **Ignorare casi limite**: Non testare su input insoliti o boundary
