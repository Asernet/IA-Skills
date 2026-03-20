---
name: google-cloud-helper
description: "Esempio di skill per la gestione di risorse su Google Cloud Platform (GCP). Supporta Compute Engine e Cloud Storage."
version: 1.0.0
triggers: ["crea vm", "lista bucket", "gcp help"]
---

# Google Cloud Helper (ESEMPIO)

Questa skill dimostra come strutturare una skill tecnica con workflow e riferimenti esterni.

## Overview

Assiste l'utente nell'amministrazione di base di GCP tramite CLI `gcloud`.

## Workflow Operativo (Sequenziale)

1. **Analisi Progetto**: Identifica l'ID progetto attivo.
2. **Selezione Risorsa**: Determina se l'utente vuole agire su VM o Storage.
3. **Generazione Comando**: Fornisce il comando `gcloud` esatto.

## Pattern di Output

Usa il pattern della tabella per i listati di risorse.

## Risorse Correlate

- `references/gcloud-cheatsheet.md`: Comandi rapidi.
- `scripts/auth-check.sh`: Script per verificare il login.
