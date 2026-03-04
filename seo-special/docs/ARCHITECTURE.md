# Architettura

## Panoramica

Claude SEO segue la specifica ufficiale della skill Claude Code di Anthropic con un'architettura modulare multi-skill.

## Struttura delle Directory

```text
~/.gemini/
├── skills/
│   ├── seo-special/          # Skill multi-agente per la SEO
│   │   ├── SKILL.md          # Punto di ingresso principale della skill
│   │   ├── docs/             # Documentazione architetturale e descrittiva
│   │   ├── hooks/            # Script di hook e validazione
│   │   ├── pdf/              # Guide e reference convertiti
│   │   ├── references/       # File di riferimento e framework on-demand
│   │   │   ├── cwv-thresholds.md
│   │   │   ├── eeat-framework.md
│   │   │   ├── industry-signals.md
│   │   │   ├── quality-gates.md
│   │   │   └── schema-types.md
│   │   ├── schema/           # Template JSON per dati strutturati
│   │   ├── scripts/          # Script Python per fetch, parsing ed export
│   │   ├── subagents/        # Sottoagenti specializzati (Agenti)
│   │   │   ├── seo-content.md        # Revisore della qualità dei contenuti
│   │   │   ├── seo-performance.md    # Analizzatore delle prestazioni
│   │   │   ├── seo-schema.md         # Esperto di markup Schema
│   │   │   ├── seo-sitemap.md        # Architetto di Sitemap
│   │   │   ├── seo-technical.md      # Specialista SEO tecnico
│   │   │   └── seo-visual.md         # Analizzatore visivo
│   │   ├── tasks/            # Componenti modulari e sub-skills (Task)
│   │   │   ├── assets/               # Template specifici per settore (saas, ecommerce, ecc.)
│   │   │   ├── task-audit.md         # Esempio: Task di audit completo
│   │   │   ├── task-page.md          # Esempio: Analisi di una singola pagina
│   │   │   └── ...                   # Altri task SEO associati
│   │   └── requirements.txt  # Dipendenze Python
```

## Tipi di Componenti

### Skills

Le skill sono file markdown con frontmatter YAML che definiscono capacità e istruzioni.

**Formato SKILL.md:**
```yaml
---
name: nome-skill
description: >
  Quando usare questa skill. Includere parole chiave di attivazione
  e casi d'uso concreti.
---

# Titolo della Skill

Istruzioni e documentazione...
```

### Subagents (Sottoagenti)

I subagent sono lavoratori specializzati a cui possono essere delegati compiti. Hanno il loro contesto e i loro strumenti.

**Formato Agent:**
```yaml
---
name: nome-agente
description: Cosa fa questo agente.
tools: Read, Bash, Write, Glob, Grep
---

Istruzioni per l'agente...
```

### File di Riferimento

I file di riferimento contengono dati statici caricati su richiesta per evitare di sovraccaricare la skill principale.

## Flusso di Orchestrazione

### Audit Completo (`/seo audit`)

```
Richiesta Utente
    │
    ▼
┌─────────────────┐
│ seo-special     │  ← Orchestratore principale
│ (SKILL.md)      │
└────────┬────────┘
         │
         │  Rileva il tipo di attività
         │  Genera subagent in parallelo
         │
    ┌────┴────┬────────┬────────┬────────┬────────┐
    ▼         ▼        ▼        ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│agente │ │agente │ │agente │ │agente │ │agente │ │agente │
│tech   │ │content│ │schema │ │sitemap│ │perf   │ │visual │
└───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
    │         │        │        │        │        │
    └─────────┴────────┴────┬───┴────────┴────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Aggrega i    │
                    │  Risultati    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Genera il    │
                    │  Report       │
                    └───────────────┘
```

### Singolo Comando

```
Richiesta Utente (es., /seo page)
    │
    ▼
┌─────────────────┐
│ seo-special     │  ← Instrada al task specifico
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ task-page.md    │  ← Il task gestisce la richiesta
│ (in tasks/)     │
└─────────────────┘
```

## Principi di Progettazione

### 1. Divulgazione Progressiva

- Il file SKILL.md principale è conciso (<200 righe)
- I file di riferimento e di gestione sono caricati su richiesta
- Istruzioni dettagliate sono fornite e gestite dai singoli `tasks/task-*.md`

### 2. Elaborazione Parallela

- I subagent vengono eseguiti contemporaneamente durante gli audit
- Analisi indipendenti non si bloccano a vicenda
- I risultati vengono aggregati dopo che tutti sono stati completati

### 3. Quality Gates (Soglie di Qualità)

- Soglie integrate impediscono raccomandazioni errate
- Limiti delle pagine di località (30 avviso, 50 blocco fisso)
- Consapevolezza della deprecazione degli schema
- Sostituzione di FID → INP imposta

### 4. Consapevolezza del Settore

- Template per diversi tipi di aziende
- Rilevamento automatico tramite segnali in homepage
- Raccomandazioni su misura per settore

## Convenzioni per i Nomi dei File

| Tipo | Modello | Esempio |
|------|---------|---------|
| Skill | `seo-special/SKILL.md` | `seo-special/SKILL.md` |
| Task | `tasks/task-{argomento}.md` | `task-audit.md` |
| Agent | `subagents/seo-{nome}.md` | `seo-technical.md` |
| Riferimento | `references/{argomento}.md` | `cwv-thresholds.md` |
| Script | `scripts/{azione}_{bersaglio}.py` | `fetch_page.py` |
| Documento | `docs/{argomento}.md` | `ARCHITECTURE.md` |
| Template | `tasks/assets/{settore}.md` | `saas.md` |

## Punti di Estensione

### Aggiunta di un Nuovo Task (ex Sub-Skill)

1. Crea `tasks/task-nuovotask.md`
2. Definisci le istruzioni e il markup per il task
3. Aggiorna `SKILL.md` principale o gli altri agenti per poterlo invocare e gestire

### Aggiunta di un Nuovo Subagent

1. Crea `subagents/seo-nuovoagente.md`
2. Aggiungi il frontmatter YAML con nome, descrizione, strumenti
3. Scrivi le istruzioni dell'agente
4. Fai riferimento dalla directory `tasks/` o `SKILL.md` pertinenti

### Aggiunta di un Nuovo File di Riferimento

1. Crea il file nell'appropriata directory `references/`
2. Fai riferimento nella skill con istruzione di caricamento su richiesta
