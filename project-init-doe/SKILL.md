---
name: project-init-doe
description: Inizializza un nuovo progetto seguendo l'architettura a 3 livelli (DOE) definita in GEMINI.md.
---

# Project Init DOE

Questa skill automatizza la creazione della struttura standard per i progetti VibeCoding (Directives, Orchestration, Execution).

## Quando usare questa skill

- All'inizio di un nuovo progetto.
- Quando si vuole convertire un progetto esistente alla struttura DOE.

## Come usare

1. Fornisci il percorso assoluto della cartella del progetto.
2. Analizza il file INSTRUCTIION.md che contiene le direttive indissolubili da seguire
3 Richiama lo script di inizializzazione e verifica se è conforme alle istruzioni fornite.

## Parametri

- `project_path`: Il percorso della cartella da inizializzare.

## Workflow

1. L'agente verifica l'esistenza della cartella.
2. Esegue `python C:\Users\mazin\.gemini\skills\project-init-doe\scripts\init_project.py --path <project_path>`.
3. Informa l'utente del completamento.
