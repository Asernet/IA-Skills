---
name: brand-guidelines
description: Applica i colori e la tipografia del brand Anthropic agli artefatti. Usa quando sono richiesti standard di design aziendali.
---

# Stile del Brand Anthropic

## Panoramica

Per calcolare l'identità ufficiale del brand Anthropic e le risorse di stile, usa questa skill.

**Parole chiave**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Linee Guida del Brand

### Colori

**Colori Principali:**

- Dark: `#141413` - Testo primario e sfondi scuri
- Light: `#faf9f5` - Sfondi chiari e testo su scuro
- Mid Gray: `#b0aea5` - Elementi secondari
- Light Gray: `#e8e6dc` - Sfondi sottili

**Colori Accento:**

- Orange: `#d97757` - Accento primario
- Blue: `#6a9bcc` - Accento secondario
- Green: `#788c5d` - Accento terziario

### Tipografia

- **Intestazioni**: Poppins (con fallback Arial)
- **Testo Corpo**: Lora (con fallback Georgia)
- **Nota**: I font dovrebbero essere pre-installati nel tuo ambiente per i migliori risultati

## Funzionalità

### Applicazione Font Intelligente

- Applica font Poppins alle intestazioni (24pt e più grandi)
- Applica font Lora al testo del corpo
- Fallback automatico a Arial/Georgia se font personalizzati non disponibili
- Preserva la leggibilità attraverso tutti i sistemi

### Styling Testo

- Intestazioni (24pt+): Font Poppins
- Testo corpo: Font Lora
- Selezione colore intelligente basata sullo sfondo
- Preserva gerarchia testo e formattazione

### Forme e Colori Accento

- Le forme non testuali usano colori accento
- Cicla attraverso accenti arancione, blu e verde
- Mantiene interesse visivo rimanendo on-brand

## Dettagli Tecnici

### Gestione Font

- Usa font Poppins e Lora installati nel sistema quando disponibili
- Fornisce fallback automatico ad Arial (intestazioni) e Georgia (corpo)
- Nessuna installazione font richiesta - funziona con font di sistema esistenti
- Per risultati migliori, pre-installa font Poppins e Lora nel tuo ambiente

### Applicazione Colore

- Usa valori colore RGB per corrispondenza brand precisa
- Applicato via classe RGBColor di python-pptx
- Mantiene fedeltà colore attraverso sistemi diversi
