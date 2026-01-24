# Pattern di Output

Usa questi pattern quando le skill devono produrre output consistenti e di alta qualità.

## Pattern Template

Fornisci template per il formato di output. Adatta il livello di rigore alle tue esigenze.

**Per requisiti rigidi (come risposte API o formati dati):**

```markdown
## Struttura del report

Usa SEMPRE questa esatta struttura di template:

# [Titolo Analisi]

## Sommario Esecutivo

[Panoramica di un paragrafo dei risultati chiave]

## Risultati Chiave

- Risultato 1 con dati di supporto
- Risultato 2 con dati di supporto
- Risultato 3 con dati di supporto

## Raccomandazioni

1. Raccomandazione specifica e azionabile
2. Raccomandazione specifica e azionabile
```

**Per guide flessibili (quando l'adattamento è utile):**

```markdown
## Struttura del report

Ecco un formato predefinito ragionevole, ma usa il tuo buon senso:

# [Titolo Analisi]

## Sommario Esecutivo

[Panoramica]

## Risultati Chiave

[Adatta le sezioni in base a ciò che scopri]

## Raccomandazioni

[Adatta al contesto specifico]

Regola le sezioni secondo necessità per il tipo specifico di analisi.
```

## Pattern Esempi

Per le skill dove la qualità dell'output dipende dal vedere esempi, fornisci coppie input/output:

```markdown
## Formato messaggio di commit

Genera messaggi di commit seguendo questi esempi:

**Esempio 1:**
Input: Aggiunta autenticazione utente con token JWT
Output:

feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
```

**Esempio 2:**
Input: Corretto bug dove le date venivano visualizzate erroneamente nei report
Output:

fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation

```

Segui questo stile: type(scope): breve descrizione, poi spiegazione dettagliata.
```

Gli esempi aiutano il modello a comprendere lo stile desiderato e il livello di dettaglio più chiaramente delle sole descrizioni.
