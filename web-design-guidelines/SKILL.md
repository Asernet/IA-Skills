---
name: web-design-guidelines
description: Rivedi codice UI per conformità alle Web Interface Guidelines. Utilizza quando l'utente chiede di revisionare la UI, controllare accessibilità, audit design, review UX o controllare il sito rispetto alle best practice.
---

# Linee Guida Interfacce Web

Rivedi file per conformità alle Web Interface Guidelines.

## Come Funziona

1. Recupera le ultime linee guida dall'URL sorgente sotto
2. Leggi i file specificati (o chiedi all'utente file/pattern)
3. Controlla rispetto a tutte le regole nelle linee guida recuperate
4. Output risultati nel formato conciso `file:riga`

## Sorgente Linee Guida

Recupera linee guida aggiornate prima di ogni review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Usa WebFetch per recuperare le ultime regole. Il contenuto recuperato contiene tutte le regole e istruzioni formato output.

## Utilizzo

Quando un utente fornisce un file o pattern:

1. Recupera linee guida dall'URL sorgente sopra
2. Leggi i file specificati
3. Applica tutte le regole dalle linee guida recuperate
4. Output risultati usando il formato specificato nelle linee guida

Se nessun file specificato, chiedi all'utente quali file revisionare.

## Aree di Verifica Principali

### Accessibilità

- Contrasto colori sufficiente
- Testo alternativo per immagini
- Navigazione da tastiera
- Landmark ARIA appropriati
- Focus visibile

### Performance

- Ottimizzazione immagini
- Lazy loading appropriato
- Minimizzazione CSS/JS
- Cache efficiente

### Usabilità

- Gerarchia visiva chiara
- Feedback interazioni
- Stati loading appropriati
- Gestione errori user-friendly

### Mobile

- Design responsive
- Touch target adeguati
- Viewport configurato
- No scroll orizzontale

## Formato Output

Per ogni problema trovato:

```
file.tsx:42 - [PROBLEMA] Descrizione issue
file.tsx:67 - [SUGGERIMENTO] Miglioramento consigliato
```

## Skill Correlate

- **frontend-dev-guidelines**: Per pattern sviluppo React
- **seo-fundamentals**: Per ottimizzazione SEO
