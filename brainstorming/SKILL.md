---
name: brainstorming
description: OBBLIGATORIO prima di qualsiasi lavoro creativo o implementativo. Esplora l'intento dell'utente, i requisiti e il design prima di iniziare a scrivere codice.
---

# Brainstorming da Idee a Design

## Panoramica

Aiuta a trasformare idee in design e specifiche completamente formati attraverso un dialogo collaborativo naturale.

Inizia comprendendo il contesto attuale del progetto, poi fai domande una alla volta per raffinare l'idea. Una volta capito cosa stai costruendo, presenta il design in piccole sezioni (200-300 parole), controllando dopo ogni sezione se sembra corretto finora.

## Il Processo

**Comprendere l'idea:**

- Controlla prima lo stato attuale del progetto (file, doc, commit recenti)
- Fai domande una alla volta per raffinare l'idea
- Preferisci domande a scelta multipla quando possibile, ma a risposta aperta va bene lo stesso
- Solo una domanda per messaggio - se un argomento richiede più esplorazione, spezzalo in più domande
- Concentrati sulla comprensione: scopo, vincoli, criteri di successo

**Esplorare approcci:**

- Proponi 2-3 approcci diversi con trade-off
- Presenta le opzioni in modo colloquiale con la tua raccomandazione e ragionamento
- Inizia con la tua opzione raccomandata e spiega perché

**Presentare il design:**

- Una volta che credi di capire cosa stai costruendo, presenta il design
- Spezzalo in sezioni di 200-300 parole
- Chiedi dopo ogni sezione se sembra corretto finora
- Copri: architettura, componenti, flusso dati, gestione errori, testing
- Sii pronto a tornare indietro e chiarire se qualcosa non ha senso

## Dopo il Design

**Documentazione:**

- Scrivi il design validato in `docs/plans/YYYY-MM-DD-<topic>-design.md`
- Usa la skill elements-of-style:writing-clearly-and-concisely se disponibile
- Committa il documento di design su git

**Implementazione (se prosegue):**

- Una volta accettato il design, chiedi esplicitamente: "Vuoi passare alla realizzazione del piano usando la skill `writing-plans` (ora integrata come modulo)?"
- Se confermato:
  - Leggi le istruzioni dettagliate in `assets/writing-plans-guide.md`
  - Usa superpowers:using-git-worktrees per creare un workspace isolato
  - Segui le istruzioni della guida per creare un piano di implementazione dettagliato, agendo come se fossi la skill writing-plans.

## Principi Chiave

- **Una domanda alla volta** - Non sovraccaricare con domande multiple
- **Scelta multipla preferita** - Più facile rispondere che a risposta aperta quando possibile
- **YAGNI spietato** - Rimuovi funzionalità non necessarie da tutti i design
- **Esplora alternative** - Proponi sempre 2-3 approcci prima di stabilirti
- **Validazione incrementale** - Presenta il design in sezioni, valida ognuna
- **Sii flessibile** - Torna indietro e chiarisci quando qualcosa non ha senso
