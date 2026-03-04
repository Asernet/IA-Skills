---
name: task-mobile-parity
description: Verifica della congruenza tra versione Mobile e Desktop (Mobile-First Indexing).
---

# Mobile Content Parity Check (Standard 2026)

Google indicizza ESCLUSIVAMENTE la versione mobile dei siti web (completato Luglio 2024). Questo task verifica che non ci siano discrepanze critiche tra le due versioni.

## Workflow di Analisi

1. **Recupero Doppia Versione:** 
   - Scansione con User-Agent Desktop.
   - Scansione con User-Agent Mobile (Googlebot Mobile).
   
2. **Confronto Metadati:**
   - I tag `Title` e `Meta Description` devono essere identici.
   - I tag `Robots` (index/noindex) devono corrispondere perfettamente.

3. **Verifica Dati Strutturati:**
   - Lo Schema Markup (JSON-LD) deve essere presente e identico in entrambe le versioni.
   - Spesso le versioni mobile "snelliscono" il codice rimuovendo lo schema: questo è un errore critico.

4. **Parità di Contenuto (Content Completeness):**
   - Il corpo del testo principale deve essere lo stesso.
   - Verificare che testi critici non siano "nascosti" o rimossi su mobile per motivi di spazio.

5. **User Experience & Interattività:**
   - Verifica che gli elementi interattivi (menu, form) siano accessibili su mobile.

---

## Formato Report

### Punteggio di Parità: XX/100

| Elemento           | Stato           | Descrizione Discrepanza |
|--------------------|-----------------|-------------------------|
| Meta Tag           | ✅/❌          | ....................... |
| Schema Markup      | ✅/❌          | ....................... |
| Testo Principale   | ✅/❌          | ....................... |
| Robots Directives  | ✅/❌          | ....................... |

### Raccomandazioni
- Azioni correttive per allineare la versione mobile a quella desktop.
