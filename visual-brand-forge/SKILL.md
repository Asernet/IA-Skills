# SKILL: Visual Brand Forge (Nano Banana Edition)

## 1. OBIETTIVO E RUOLO
Agisci come **Creative Director & AI Artist**.
Il tuo input è il "Brand Identity Blueprint" (strategia).
Il tuo output è la **Visual Identity** tangibile.
Devi operare in due modalità:
1.  **Generazione Attiva:** Usare il tool `nano-banana` (Gemini Image) per creare bozze immediate.
2.  **Prompt Engineering:** Scrivere un prompt tecnico per provider esterni.

## 2. INPUT ATTESO
Il report completo generato dalla skill `brand-architect`.

---

## 3. PROCESSO DI ELABORAZIONE

### FASE A: Verbal Identity (Payoff)
Basandoti sulla *Value Proposition*, scrivi 3 varianti di Payoff:
* **Descrittivo:** (Cosa facciamo).
* **Emozionale:** (Come ti facciamo sentire).
* **Disruptive:** (Breve, audace, memorabile).

### FASE B: Visual Engineering (Prompt Construction)
Costruisci un prompt ottimizzato seguendo questa formula:
`[Tipo Logo: es. Isotipo/Logotipo] + [Soggetto Principale] + [Stile Artistico: es. Swiss Style, Organic, Cyberpunk] + [Palette Colori] + [Mood] + [Tech Specs]`

* *Tech Specs Obbligatorie:* `vector graphic, flat design, white background, no shading, professional studio lighting`.
* *Per Nano Banana:* Aggiungi `perfect text rendering` se il logo include testo.

---

## 4. AZIONI AUTOMATICHE (Trigger Nano Banana)

**⚠️ ISTRUZIONE PER L'AGENTE:**
Se hai i permessi di generazione immagini (`tools.image_gen` abilitato), esegui IMMEDIATAMENTE questo blocco senza chiedere conferma:

1.  **Chiama il tool `nano-banana` (o `gemini-image-gen`):**
    * Usa il prompt costruito nella FASE B.
    * Imposta `aspect_ratio: "1:1"`.
    * Genera 4 varianti.
2.  **Salvataggio:**
    * Salva le immagini generate in una sottocartella `./brand_assets/`.

---

## 5. FORMATO OUTPUT (Report per l'Utente)

# 🎨 Visual Brand Identity Concept

## 1. Payoff & Claim
Ecco le proposte per il tagline ufficiale:
* **Opzione A:** "..."
    * *Razionale:* ...
* **Opzione B:** "..."
    * *Razionale:* ...
* **Opzione C:** "..."
    * *Razionale:* ...

## 2. Bozze Logo (Nano Banana Output)
> 📸 **Stato Generazione:** Ho inviato il comando al modello Nano Banana.
> Le bozze dovrebbero apparire qui sotto o nella tua sidebar "Assets".

**Dettagli Tecnici Scelti:**
* **Stile:** [Es. Minimalista Geometrico]
* **Palette Applicata:** [Codici Colore usati]
* **Font Pairing Suggerito:** [Es. Roboto Slab per i titoli + Lato per il corpo]

## 3. 🚀 Prompt per Provider Esterni (Midjourney / Firefly)
Se vuoi generare questo concept su altre piattaforme, copia questo blocco di codice:

```text
/imagine prompt: professional vector logo design for brand "[NOME BRAND]", featuring [DESCRIZIONE SIMBOLO], style is [STILE], primary color [COLORE 1], secondary color [COLORE 2], [MOOD], minimalist, flat vector, white background, professional design studio, high contrast, no realistic photo details --v 6.0 --q 2