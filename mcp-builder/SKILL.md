---
name: mcp-builder
description: Guida per creare server MCP (Model Context Protocol) di alta qualità per integrare servizi esterni con LLM.
---

# Guida allo Sviluppo di Server MCP

## Panoramica

Crea server MCP (Model Context Protocol) che abilitano gli LLM a interagire con servizi esterni attraverso tool ben progettati. La qualità di un server MCP è misurata da quanto bene abilita gli LLM a compiere task del mondo reale.

---

# Processo

## 🚀 Workflow Alto Livello

Creare un server MCP di alta qualità coinvolge quattro fasi principali:

### Fase 1: Ricerca Profonda e Pianificazione

#### 1.1 Comprendere il Design MCP Moderno

**Copertura API vs. Tool Workflow:**
Bilancia copertura endpoint API comprensiva con tool workflow specializzati. I tool workflow possono essere più convenienti per task specifici, mentre copertura comprensiva dà agli agenti flessibilità per comporre operazioni. La performance varia per client—alcuni beneficiano da esecuzione codice che combina tool base, mentre altri lavorano meglio con workflow di alto livello. Quando incerto, prioritizza copertura API comprensiva.

**Naming Tool e Scopribilità:**
Nomi tool chiari e descrittivi aiutano gli agenti a trovare i tool giusti velocemente. Usa prefissi consistenti (es., `github_create_issue`, `github_list_repos`) e naming orientato all'azione.

**Gestione Contesto:**
Gli agenti beneficiano da descrizioni tool concise e abilità di filtrare/paginare risultati. Progetta tool che ritornano dati focalizzati, rilevanti.

**Messaggi Errore Azionabili:**
I messaggi di errore dovrebbero guidare gli agenti verso soluzioni con suggerimenti specifici e prossimi passi.

#### 1.2 Studiare Documentazione Protocollo MCP

**Naviga la specifica MCP:**

Inizia con la sitemap per trovare pagine rilevanti: `https://modelcontextprotocol.io/sitemap.xml`

Poi recupera pagine specifiche con suffisso `.md` per formato markdown (es., `https://modelcontextprotocol.io/specification/draft.md`).

Pagine chiave da revisionare:

- Panoramica specifica e architettura
- Meccanismi trasporto (streamable HTTP, stdio)
- Definizioni tool, risorse e prompt

#### 1.3 Studiare Documentazione Framework

**Stack raccomandato:**

- **Linguaggio**: TypeScript (supporto SDK alta qualità e buona compatibilità in molti ambienti esecuzione es. MCPB. Più i modelli AI sono bravi a generare codice TypeScript, beneficiando dal suo ampio uso, tipizzazione statica e buoni tool di linting)
- **Trasporto**: Streamable HTTP per server remoti, usando JSON stateless (più semplice da scalare e mantenere, opposto a sessioni stateful e risposte streaming). stdio per server locali.

**Carica documentazione framework:**

- **Best Practices MCP**: [📋 Vedi Best Practices](./reference/mcp_best_practices.md) - Linee guida core

**Per TypeScript (raccomandato):**

- **TypeScript SDK**: Usa WebFetch per caricare `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- [⚡ Guida TypeScript](./reference/node_mcp_server.md) - Pattern ed esempi TypeScript

**Per Python:**

- **Python SDK**: Usa WebFetch per caricare `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- [🐍 Guida Python](./reference/python_mcp_server.md) - Pattern ed esempi Python

#### 1.4 Pianifica la Tua Implementazione

**Comprendi l'API:**
Revisiona la documentazione API del servizio per identificare endpoint chiave, requisiti autenticazione e modelli dati.

**Selezione Tool:**
Prioritizza copertura API comprensiva. Elenca endpoint da implementare, iniziando con le operazioni più comuni.

---

### Fase 2: Implementazione

#### 2.1 Imposta Struttura Progetto

Vedi guide specifiche per linguaggio per setup progetto:

- [⚡ Guida TypeScript](./reference/node_mcp_server.md) - Struttura progetto, package.json, tsconfig.json
- [🐍 Guida Python](./reference/python_mcp_server.md) - Organizzazione moduli, dipendenze

#### 2.2 Implementa Infrastruttura Core

Crea utility condivise:

- Client API con autenticazione
- Helper gestione errori
- Formattazione risposta (JSON/Markdown)
- Supporto paginazione

#### 2.3 Implementa Tool

Per ogni tool:

**Schema Input:**

- Usa Zod (TypeScript) o Pydantic (Python)
- Includi vincoli e descrizioni chiare
- Aggiungi esempi nelle descrizioni campo

**Schema Output:**

- Definisci `outputSchema` dove possibile per dati strutturati
- Usa `structuredContent` nelle risposte tool (feature TypeScript SDK)
- Aiuta i client a capire e processare output tool

**Descrizione Tool:**

- Riassunto conciso funzionalità
- Descrizioni parametri
- Schema tipo ritorno

**Implementazione:**

- Async/await per operazioni I/O
- Gestione errori appropriata con messaggi azionabili
- Supporta paginazione dove applicabile
- Ritorna sia contenuto testo che dati strutturati quando usi SDK moderni

**Annotazioni:**

- `readOnlyHint`: true/false
- `destructiveHint`: true/false
- `idempotentHint`: true/false
- `openWorldHint`: true/false

---

### Fase 3: Revisione e Test

#### 3.1 Qualità Codice

Revisiona per:

- Nessun codice duplicato (principio DRY)
- Gestione errori consistente
- Copertura tipi completa
- Descrizioni tool chiare

#### 3.2 Build e Test

**TypeScript:**

- Esegui `npm run build` per verificare compilazione
- Testa con MCP Inspector: `npx @modelcontextprotocol/inspector`

**Python:**

- Verifica sintassi: `python -m py_compile your_server.py`
- Testa con MCP Inspector

Vedi guide specifiche per linguaggio per approcci di testing dettagliati e checklist qualità.

---

### Fase 4: Crea Valutazioni

Dopo aver implementato il tuo server MCP, crea valutazioni comprensive per testare la sua efficacia.

**Carica [✅ Guida Valutazione](./reference/evaluation.md) per linee guida valutazione complete.**

#### 4.1 Comprendi Scopo Valutazione

Usa valutazioni per testare se gli LLM possono usare efficacemente il tuo server MCP per rispondere a domande realistiche e complesse.

#### 4.2 Crea 10 Domande Valutazione

Per creare valutazioni efficaci, segui il processo delineato nella guida valutazione:

1. **Ispezione Tool**: Elenca tool disponibili e comprendi le loro capacità
2. **Esplorazione Contenuto**: Usa operazioni READ-ONLY per esplorare dati disponibili
3. **Generazione Domande**: Crea 10 domande complesse, realistiche
4. **Verifica Risposta**: Risolvi ogni domanda tu stesso per verificare risposte

#### 4.3 Requisiti Valutazione

Assicura che ogni domanda sia:

- **Indipendente**: Non dipendente da altre domande
- **Read-only**: Solo operazioni non distruttive richieste
- **Complessa**: Richiedendo chiamate tool multiple ed esplorazione profonda
- **Realistica**: Basata su casi d'uso reali di cui gli umani si preoccuperebbero
- **Verificabile**: Risposta singola, chiara che può essere verificata da confronto stringhe
- **Stabile**: La risposta non cambierà nel tempo

#### 4.4 Formato Output

Crea un file XML con questa struttura:

```xml
<evaluation>
  <qa_pair>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </qa_pair>
<!-- More qa_pairs... -->
</evaluation>
```

---

# File Riferimento

## 📚 Libreria Documentazione

Carica queste risorse come necessario durante lo sviluppo:

### Documentazione Core MCP (Carica Prima)

- **Protocollo MCP**: Inizia con sitemap a `https://modelcontextprotocol.io/sitemap.xml`, poi recupera pagine specifiche con suffisso `.md`
- [📋 Best Practices MCP](./reference/mcp_best_practices.md) - Linee guida MCP universali

### Documentazione SDK (Carica Durante Fase 1/2)

- **Python SDK**: Recupera da `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: Recupera da `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

### Guide Implementazione Specifiche Linguaggio (Carica Durante Fase 2)

- [🐍 Guida Implementazione Python](./reference/python_mcp_server.md) - Guida completa Python/FastMCP
- [⚡ Guida Implementazione TypeScript](./reference/node_mcp_server.md) - Guida completa TypeScript

### Guida Valutazione (Carica Durante Fase 4)

- [✅ Guida Valutazione](./reference/evaluation.md) - Guida creazione valutazione completa
