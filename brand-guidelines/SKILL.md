---
name: brand-guidelines
description: Gestisce dinamicamente l'identità del brand. Verifica l'esistenza di dati di brand (Colori, Font) e, se mancanti, interroga l'utente per crearli.
---

# Brand Guidelines Manager

## Scopo
Questa skill garantisce che ogni artefatto prodotto (siti, PDF, presentazioni) rispetti l'identità visiva del progetto corrente.

## Procedura "Man in the Middle"
Ogni volta che devi applicare uno stile o design:

### 1. Ricerca Identità
Cerca il file `concept_defense_*.md` nelle seguenti posizioni (in ordine):
1.  Cartella `Desktop\Progetti\[dominio-sito]\brand_assets\`
2.  Root del Workspace attivo.
3.  Cartella `.gemini` o `.docs`.
4.  Cartella `artefacts` o `brain`.

### 2. Logica Condizionale

#### CASO A: Il file ESISTE
1.  **Leggi** il file.
2.  **Applica** rigorosamente i valori trovati (Colori Primari, Secondari, Font).
3.  *Non chiedere nulla all'utente.*

#### CASO B: Il file NON ESISTE (Missing Data)
⚠️ **STOP**. Non inventare colori o font.
1.  Usa lo strumento `notify_user`.
2.  Chiedi esplicitamente all'utente di definire lo stile del progetto.
3.  **Prompt Suggerito**:
    *"Non trovo le linee guida del brand per questo progetto. Per procedere, indicami:*
    *   *Colore Primario (Hex)*
    *   *Colore Secondario/Accento (Hex)*
    *   *Font Intestazioni (es. Inter, Poppins)*
    *   *Font Corpo (es. Roboto, Open Sans)"*
4.  Attendi la risposta.

### 3. Persistenza (Dopo la risposta)
Con i dati forniti dall'utente:
1.  Crea un file `BRAND_IDENTITY.md` nella root del progetto **Desktop\Progetti\[dominio-sito]\brand_assets\**.
2.  Usa questo formato standard:

```markdown
# Brand Identity: [Nome Progetto]

## Palette Colori
- **Primary**: `[Hex]`
- **Secondary**: `[Hex]`
- **Background**: `[Hex]`
- **Text**: `[Hex]`

## Tipografia
- **Headers**: [Font Family]
- **Body**: [Font Family]

## Tono di Voce
[Descrizione breve se fornita]
```

3.  Riprendi il task originale usando i nuovi dati salvati.

## Esempio di Applicazione
Se l'utente chiede "Fai un sito per una pizzeria":
1.  Cerca `concept_defense_*.md` -> Non c'è.
2.  Chiama `notify_user`: *"Che colori e font usa la pizzeria?"*
3.  Utente: *"Rosso pomodoro (#FF6347) e font rustici"*
4.  Crea `concept_defense_*.md` con Primary: #FF6347.
5.  Genera il CSS usando `--primary-color: #FF6347`.
