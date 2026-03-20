---
name: obsidian-clipper-template-creator
description: Guida per la creazione di template per Obsidian Web Clipper. Usa quando vuoi creare un nuovo template di acquisizione, capire le variabili disponibili o formattare il contenuto acquisito.
---

# Obsidian Web Clipper Template Creator

Questa skill ti aiuta a creare template JSON importabili per Obsidian Web Clipper.

## Workflow

1. **Identifica l'Intento dell'Utente:** sito specifico (YouTube), tipo specifico (Ricetta) o acquisizione generale?
2. **Controlla le Basi Esistenti:** L'utente probabilmente ha uno schema "Base" definito in `Templates/Bases/`.
   - **Azione:** Leggi `Templates/Bases/*.base` per trovare una categoria corrispondente (es. `Recipes.base`).
   - **Azione:** Usa le proprietà definite nella Base per strutturare le proprietà del template del Clipper.
   - Vedi [references/bases-workflow.md](references/bases-workflow.md) per i dettagli.
3. **Recupera e Analizza l'URL di Riferimento:** Valida le variabili rispetto a una pagina reale.
   - **Azione:** Chiedi all'utente un URL di esempio del contenuto che desidera acquisire (se non fornito).
   - **Azione (RICHIESTA):** Usa `WebFetch` o uno snapshot del DOM del browser per recuperare il contenuto della pagina prima di scegliere qualsiasi selettore.
   - **Azione:** Analizza l'HTML per JSON Schema.org, Meta tag e selettori CSS.
   - **Azione (RICHIESTA):** Verifica ogni selettore rispetto al contenuto recuperato. Non indovinare i selettori.
   - Vedi [references/analysis-workflow.md](references/analysis-workflow.md) per le tecniche di analisi.
4. **Bozza del JSON:** Crea un oggetto JSON valido seguendo lo schema.
   - Vedi [references/json-schema.md](references/json-schema.md).
5. **Verifica le Variabili:** Assicurati che le variabili scelte (Preset, Schema, Selettore) esistano nella tua analisi.
   - **Azione (RICHIESTA):** Se un selettore non può essere verificato dal contenuto recuperato, dichiaralo esplicitamente e chiedi un altro URL.
   - Vedi [references/variables.md](references/variables.md).

## Regole di Verifica dei Selettori

- **Verifica sempre i selettori** rispetto al contenuto della pagina live prima di rispondere.
- **Non indovinare mai i selettori.** Se non è possibile accedere al DOM o l'elemento manca, chiedi un altro URL o uno screenshot.
- **Preferisci selettori stabili** (attributi data, ruoli semantici, ID unici) rispetto a fragili catene di classi.
- **Documenta l'elemento di destinazione** nel tuo ragionamento (es. "Paragrafo della sidebar About") per ridurre i disallineamenti.

## Formato di Output

Rilascia **SEMPRE** il risultato finale come un blocco di codice JSON che l'utente può copiare e importare.

```json
{
  "schemaVersion": "0.1.0",
  "name": "My Template",
  ...
}
```

## Risorse

- [references/variables.md](references/variables.md) - Variabili di dati disponibili.
- [references/filters.md](references/filters.md) - Filtri di formattazione.
- [references/json-schema.md](references/json-schema.md) - Documentazione della struttura JSON.
- [references/bases-workflow.md](references/bases-workflow.md) - Come mappare le Basi ai Template.
- [references/analysis-workflow.md](references/analysis-workflow.md) - Come validare i dati della pagina.

### Documentazione Ufficiale

- [Variabili](https://help.obsidian.md/web-clipper/variables)
- [Filtri](https://help.obsidian.md/web-clipper/filters)
- [Template](https://help.obsidian.md/web-clipper/templates)

## Esempi

Vedi [assets/](assets/) per esempi JSON.
