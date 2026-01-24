---
name: web-artifacts-builder
description: Crea artefatti HTML complessi multi-componente (React, Tailwind, shadcn/ui) per applicazioni web.
---

# Web Artifacts Builder

Per costruire artefatti frontend claude.ai potenti, segui questi passi:

1. Inizializza la repo frontend usando `scripts/init-artifact.sh`
2. Sviluppa il tuo artefatto editando il codice generato
3. Impacchetta (bundle) tutto il codice in un singolo file HTML usando `scripts/bundle-artifact.sh`
4. Mostra artefatto all'utente
5. (Opzionale) Testa l'artefatto

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Linee Guida Design & Stile

MOLTO IMPORTANTE: Per evitare ciò che è spesso riferito come "AI slop", evita di usare eccessivi layout centrati, gradienti viola, angoli arrotondati uniformi e font Inter.

## Avvio Rapido

### Passo 1: Inizializza Progetto

Esegui lo script di inizializzazione per creare un nuovo progetto React:

```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

Questo crea un progetto pienamente configurato con:

- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 con sistema theming shadcn/ui
- ✅ Path alias (`@/`) configurati
- ✅ 40+ componenti shadcn/ui pre-installati
- ✅ Tutte dipendenze Radix UI incluse
- ✅ Parcel configurato per bundling (via .parcelrc)
- ✅ Compatibilità Node 18+ (auto-rileva e pinea versione Vite)

### Passo 2: Sviluppa il Tuo Artefatto

Per costruire l'artefatto, edita i file generati.

### Passo 3: Bundle in Singolo File HTML

Per impacchettare l'app React in un singolo artefatto HTML:

```bash
bash scripts/bundle-artifact.sh
```

Questo crea `bundle.html` - un artefatto auto-contenuto con tutto JavaScript, CSS e dipendenze inlined. Questo file può essere condiviso direttamente in conversazioni Claude come artefatto.

**Requisiti**: Il tuo progetto deve avere un `index.html` nella directory root.

**Cosa fa lo script**:

- Installa dipendenze bundling (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Crea config `.parcelrc` con supporto path alias
- Costruisce con Parcel (no source maps)
- Inlinea tutti gli asset in singolo HTML usando html-inline

### Passo 4: Condividi Artefatto con Utente

Finalmente, condividi il file HTML impacchettato in conversazione con l'utente così possono vederlo come artefatto.

### Passo 5: Testare/Visualizzare l'Artefatto (Opzionale)

Nota: Questo è un passo completamente opzionale. Esegui solo se necessario o richiesto.

Per testare/visualizzare l'artefatto, usa tool disponibili (inclusi altre Skill o tool built-in come Playwright o Puppeteer). In generale, evita di testare l'artefatto upfront poiché aggiunge latenza tra la richiesta e quando l'artefatto finito può essere visto. Testa dopo, dopo aver presentato l'artefatto, se richiesto o se sorgono problemi.

## Riferimento

- **Componenti shadcn/ui**: https://ui.shadcn.com/docs/components
