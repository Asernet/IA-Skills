---
name: task-schema
description: Rilevamento, validazione e generazione di dati strutturati Schema.org (JSON-LD prioritario).
---

# Analisi e Generazione Schema Markup (Febbraio 2026)

## Rilevamento e Validazione
- **Priorità JSON-LD:** Raccomanda sempre JSON-LD rispetto a Microdata o RDFa.
- **Checklist:** @context HTTPS, @type valido, URL assoluti, date ISO 8601.
- **JS SEO (Dic 2025):** Lo schema iniettato via JS può subire ritardi. Per Product/Offer, usa HTML server-rendered.

## Stato Tipi Schema (Aggiornamento 2026)
- **ATTIVI:** Organization, Product (con certificazione Apr 2025), Article, Review, Person, VideoObject.
- **RISTRETTI:** FAQ (Solo siti governativi/sanitari).
- **DEPRECATI (Mai usare):** HowTo, SpecialAnnouncement, CourseInfo, EstimatedSalary, LearningVideo.

## Generazione
1. Identifica il tipo di pagina.
2. Genera JSON-LD con proprietà obbligatorie e raccomandate.
3. Utilizza i template in `schema/templates.json`.

## Formato Output
- `SCHEMA-REPORT.md`: Analisi esistente e validazione.
- `generated-schema.json`: Snippet pronti all'uso.
