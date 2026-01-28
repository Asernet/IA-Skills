# Documentazione Brand Forge

Questo repository contiene la documentazione e le risorse per la skill **Brand Forge**, un sistema progettato per guidare la creazione di un'identità di marca completa, dalla strategia iniziale agli asset visivi finali.

## Panoramica del Processo

Il workflow di Brand Forge è un percorso lineare ma iterativo che trasforma un brief grezzo in una Brand Identity professionale e coerente. Il processo è diviso in quattro fasi principali:

### 1. Fase 0: Validazione Configurazione
Prima di ogni operazione, la skill verifica l'integrità dell'ambiente di lavoro:
- Presenza del file `agent.yaml`.
- Abilitazione delle procedure di ricerca (`web_search`), generazione immagini (`image_generation`) e gestione file (`file_system`).
- Creazione (se mancante) della cartella `Documents/brand_assets/` dove verranno salvati tutti gli output.

### 2. Fase 1: Brand Architecture (Strategia)
Questa è la fase analitica in cui viene definito lo "spazio mentale" del brand.
- **Analisi dell'Input**: Studio del brief cliente o del sito web esistente.
- **Market Scanning**: Ricerca attiva sui competitor per identificare Punti di Parità (POP) e Punti di Differenza (POD).
- **Creazione del Blueprint**: Generazione del file `blueprint_[NOME_BRAND].md` che include Purpose, Mission, Vision, Valori, Archetipo e Strategia Cromatica.

### 3. Fase 1.5: Approvazione Utente (Check-point)
**Fondamentale**: Il processo si ferma finché l'utente non approva esplicitamente il Blueprint. 
- La skill presenta i punti chiave della strategia.
- L'utente deve dare il via libera per procedere alla fase creativa. Se richiesto, il Blueprint viene corretto e ripresentato.

### 4. Fase 2: Visual Forge (Design)
Una volta approvata la strategia, si passa alla creazione degli elementi tangibili:
- **Verbal Identity**: Generazione di varianti di Payoff (Descrittivo, Emozionale, disruptive).
- **Visual Engineering**: Utilizzo di prompt avanzati per generare 4 varianti di logo professionali.
- **Concept Defense**: Creazione del file `concept_defense_[NOME_BRAND].md` che spiega razionalmente le scelte stilistiche in relazione alla strategia approvata.

## Risorse in questo Folder

In questa cartella (`references/`) sono presenti documenti di supporto utilizzati dalla skill durante il processo:

- **naming_strategies.md**: Linee guida sulle tipologie di nomi e tecniche per la creazione di claim/payoff efficaci.

## Standard di Consegna

Tutti i file generati vengono salvati in un'unica posizione centralizzata per facilitare la consultazione:
`[USER_HOME]/Documents/brand_assets/`

**File tipici generati:**
- `blueprint_[brand].md`
- `concept_defense_[brand].md`
- Asset dei loghi (immagini PNG/JPG)
