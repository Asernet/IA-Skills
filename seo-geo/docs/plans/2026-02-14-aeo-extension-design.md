# Design Document: Espansione AEO per Skill SEO-GEO (2026)

## Obiettivo

Integrare le tecniche di Answer Engine Optimization (AEO) e il protocollo "Antifragile" sviluppato durante il brainstorming nel workflow tecnico della skill `seo-geo`.

## Architettura dell'Espansione

### 1. Nuovo Modulo di Riferimento: `references/aeo-optimization.md`

Conterrà le linee guida teorico-pratiche derivate dal "Manuale Master", incluse:

- Protocollo Q-A-V (Question-Answer-Value).
- Inverted Pyramid per bot LLM.
- Strategia di Zero Ambiguity via Schema Markup.

### 2. Aggiornamento Workflow in `SKILL.md`

Aggiunta di una fase specifica post-audit: "Ottimizzazione per gli Answer Engine".

- Audit semantico delle FAQ.
- Verifica della presenza di risposte dirette nei primi 150-200 caratteri.

### 3. Strumenti di Misurazione (Scripts)

Progettazione di un prototipo di script (`scripts/aeo-checker.py`) per simulare risposte di modelli comuni e verificare la "Share of Voice" del brand.

## Validazione Antifragile (Devil's Advocate & Cognitos)

- **Rischio**: Dipendenza eccessiva dai modelli attuali.
- **Mitigazione**: Il design punta sulla _chiarezza semantica universale_ (Schema.org), garantendo valore anche in caso di cambiamenti negli algoritmi dei chatbot.

## Roadmap

1. Creazione file di riferimento AEO.
2. Iniezione linee guida AEO in `SKILL.md`.
3. Creazione esempio pratico aggiornato.
