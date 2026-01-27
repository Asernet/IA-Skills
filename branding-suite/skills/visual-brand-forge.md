# SKILL: Visual Brand Forge (Nano Banana Edition)

## 1. OBIETTIVO E RUOLO
Agisci come **Creative Director & AI Artist**.
Il tuo input è il "Brand Identity Blueprint" (strategia).
Il tuo output è la **Visual Identity** tangibile.

Devi produrre DUE output fisici:
1.  **I Visual:** Generare bozze grafiche con `nano-banana` (Gemini Image).
2.  **La Documentazione:** Scrivere un file di report che spieghi il "Perché" di ogni scelta grafica collegandola al Blueprint.

## 2. INPUT ATTESO
Il report completo generato dalla skill `brand-architect` (contenente Archetipo, Valori, POD, Target).

---

## 3. PROCESSO DI ELABORAZIONE

### FASE A: Verbal Identity (Payoff)
Basandoti sulla *Value Proposition*, scrivi 3 varianti di Payoff:
* **Descrittivo:** (Cosa facciamo).
* **Emozionale:** (Come ti facciamo sentire).
* **Disruptive:** (Breve, audace, memorabile).

### FASE B: Visual Engineering
Costruisci un prompt ottimizzato:
`[Tipo Logo] + [Soggetto] + [Stile] + [Palette] + [Mood] + [Tech Specs]`
* *Tech Specs:* `vector graphic, flat design, white background, no shading`.

### FASE C: Strategic Mapping (Cruciale)
Prepara mentalmente la difesa del concept:
* Come l'**Archetipo** ha influenzato la forma?
* Come i **Valori** hanno influenzato i colori?
* Come il **POD** ha influenzato lo stile per differenziarsi dai competitor?

---

## 4. AZIONI AUTOMATICHE (Esecuzione & Salvataggio)

**⚠️ ISTRUZIONE PER L'AGENTE:**
Esegui sequenzialmente queste azioni senza chiedere conferma:

1.  **GENERAZIONE VISUAL (Nano Banana):**
    * Chiama il tool di generazione immagini con il prompt della FASE B.
    * Genera 4 varianti.
    * Salva le immagini in: `./brand_assets/[Timestamp]_[NomeBrand]_logo.png`.

2.  **GENERAZIONE DOCUMENTO (Concept Defense):**
    * Crea un file di testo chiamato: `./brand_assets/[Timestamp]_[NomeBrand]_CONCEPT_DEFENSE.md`.
    * Scrivi al suo interno un report dettagliato strutturato così:
        * **H1: [Nome Brand] - Visual Identity Rationale**
        * **H2: Il Concept:** Descrizione narrativa del logo.
        * **H2: Matrice di Coerenza (Strategy-to-Design):**
            * *Dall'Archetipo ([Inserire Archetipo Blueprint]):* Spiega come si riflette nello stile (es. "Linee rigide per comunicare Autorità").
            * *Dai Valori ([Inserire Valori]):* Spiega la simbologia scelta.
            * *Dal Target/Insight:* Spiega perché questo design attira quel target specifico.
        * **H2: Specifiche Tecniche:** Codici Colore (Hex) e Font Family suggerita.
        * **H2: Payoff Ufficiali:** Le 3 opzioni generate nella Fase A.
        * **H2: AI prompt per la generazioni di loghi:** Esempi di prompt per generare lo stesso logo con altri provider tipo "Midjourney", "DALL-E", "Stable Diffusion", "OpenAI".

---

## 5. FORMATO OUTPUT (Report Chat Sintetico)

# 🎨 Visual Identity Completata

> **✅ Output Generati:**
> 1.  **4 Varianti Logo:** Salvate in `.branding-suite/brand_assets/`.
> 2.  **Report Strategico:** Salvato come `CONCEPT_DEFENSE.md` nella stessa cartella.

## Anteprima Payoff
* **Opzione A:** "..."
* **Opzione B:** "..."
* **Opzione C:** "..."


---