---
name: seo-geo
description: |
  SEO e GEO (Generative Engine Optimization) e AEO (Answer Engine Optimization) per siti web.
  Analizza parole chiave, genera markup schema, ottimizza per i motori di ricerca AI
  (ChatGPT, Perplexity, Gemini, Copilot, Claude) e la ricerca tradizionale (Google, Bing).
  Usa questa skill quando l'utente desidera migliorare la visibilità sui motori di ricerca.
triggers:
  - "SEO"
  - "GEO"
  - "ottimizzazione ricerca"
  - "markup schema"
  - "JSON-LD"
  - "meta tag"
  - "ricerca parole chiave"
  - "ranking ricerca"
  - "visibilità AI"
  - "ranking ChatGPT"
  - "AEO"
  - "Answer Engine Optimization"
  - "Q-A-V protocol"
  - "Content Engineering"
  - "Perplexity"
  - "Google AI Overview"
  - "indicizzazione"
---

# Skill di Ottimizzazione SEO/GEO

Ottimizzazione completa SEO e GEO (Generative Engine Optimization) per siti web. Ottimizza sia per i motori di ricerca tradizionali (Google, Bing) che per i motori di ricerca AI (ChatGPT, Perplexity, Gemini, Copilot, Claude).

## Riferimento Rapido

**GEO = Generative Engine Optimization** - Ottimizzazione dei contenuti per essere citati dai motori di ricerca AI.

**Concetto Chiave:** I motori di ricerca AI non classificano le pagine - essi **citano le fonti**. Essere citati è il nuovo "primo posto in classifica".

## Workflow

### Step 1: Audit del Sito Web

Ottieni l'URL di destinazione e analizza l'attuale stato SEO/GEO.

**Audit SEO di Base (Gratuito):**

```bash
python3 scripts/seo_audit.py "https://example.com"
```

**Usa questo per**: Controllo tecnico SEO rapido (titolo, meta, H1, robots, sitemap, tempo di caricamento). Non è necessaria alcuna API.

---

**Controlla i Meta Tag:**

```bash
curl -sL "https://example.com" | grep -E "<title>|<meta name=\"description\"|<meta property=\"og:|application/ld\+json" | head -20
```

**Usa questo per**: Controllo rapido dei meta tag essenziali e del markup schema su qualsiasi pagina web.

---

**Controlla robots.txt:**

```bash
curl -s "https://example.com/robots.txt"
```

**Usa questo per**: Verificare quali bot sono permessi/bloccati. Critico per garantire che i motori di ricerca AI possano scansionare il tuo sito.

---

**Controlla la sitemap:**

```bash
curl -s "https://example.com/sitemap.xml" | head -50
```

**Usa questo per**: Verificare la struttura della sitemap e assicurarsi che tutte le pagine importanti siano incluse per la scoperta da parte dei motori di ricerca.

**Verifica l'Accesso dei Bot AI:**

```
# Questi bot dovrebbero essere consentiti nel robots.txt:
- Googlebot (Google)
- Bingbot (Bing/Copilot)
- PerplexityBot (Perplexity)
- ChatGPT-User (ChatGPT con navigazione)
- ClaudeBot / anthropic-ai (Claude)
- GPTBot (OpenAI)
```

### Step 2: Ricerca Parole Chiave

Usa **WebSearch** per ricercare le parole chiave target:

```
WebSearch: "{keyword} keyword difficulty site:ahrefs.com OR site:semrush.com"
WebSearch: "{keyword} search volume 2026"
WebSearch: "site:{competitor.com} {keyword}"
```

**Analizza:**

- Volume di ricerca e difficoltà
- Strategie delle parole chiave dei concorrenti
- Opportunità per parole chiave a coda lunga (long-tail)
- Conflitti internazionali delle parole chiave (es. "OPC" = automazione industriale nei mercati inglesi)

### Step 3: Ottimizzazione GEO (Motori di Ricerca AI)

Applica i **9 Metodi GEO di Princeton** (vedi [references/geo-research.md](./references/geo-research.md)):

| Metodo                     | Incremento Visibilità | Come Applicarlo                                |
| -------------------------- | --------------------- | ---------------------------------------------- |
| **Cita le Fonti**          | +40%                  | Aggiungi citazioni e riferimenti autorevoli    |
| **Aggiunta Statistiche**   | +37%                  | Includi numeri specifici e punti dati          |
| **Aggiunta Citazioni**     | +30%                  | Aggiungi citazioni di esperti con attribuzione |
| **Tono Autorevole**        | +25%                  | Usa un linguaggio esperto e sicuro             |
| **Facile da Capire**       | +20%                  | Semplifica concetti complessi                  |
| **Termini Tecnici**        | +18%                  | Includi terminologia specifica del dominio     |
| **Parole Uniche**          | +15%                  | Aumenta la diversità del vocabolario           |
| **Ottimizzazione Fluenza** | +15-30%               | Migliora la leggibilità e il flusso            |
| ~~Keyword Stuffing~~       | **-10%**              | **EVITARE - danneggia la visibilità**          |

**Migliore Combinazione:** Fluenza + Statistiche = Massimo potenziamento

**Genera Schema FAQPage** (+40% di visibilità AI):

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Cos'è [argomento]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Secondo [fonte], [risposta con statistiche]."
      }
    }
  ]
}
```

**Ottimizza la Struttura del Contenuto:**

- Usa il formato "answer-first" (risposta diretta in alto)
- Gerarchia chiara H1 > H2 > H3
- Elenchi puntati e numerati
- Tabelle per i dati di confronto
- Paragrafi brevi (max 2-3 frasi)

### Step 4: Ottimizzazione Answer Engine (AEO)

Applica il protocollo **Q-A-V** (vedi [references/aeo-optimization.md](./references/aeo-optimization.md)):

1. **Question (Q)**: Identificare la domanda specifica dell'utente.
2. **Answer (A)**: Fornire la risposta tecnica e diretta nei primi 150-200 caratteri (Inverted Pyramid).
3. **Value (V)**: Approfondire con dati, esperienza reale (E-E-A-T) e differenziazione del brand.

**Ingegnazione del Contenuto:**

- Struttura il contenuto per un doppio livello di lettura: bot (risposta rapida) e umani (valore profondo).
- Usa il "Gateway Content" per spingere l'utente all'interazione dopo aver fornito la risposta.

### Step 5: Ottimizzazione SEO Tradizionale

**Template Meta Tag:**

```html
<title>{Parola Chiave Primaria} - {Brand} | {Parola Chiave Secondaria}</title>
<meta
  name="description"
  content="{Descrizione accattivante con parola chiave, 150-160 caratteri}"
/>
<meta name="keywords" content="{keyword1}, {keyword2}, {keyword3}" />

<!-- Open Graph -->
<meta property="og:title" content="{Titolo}" />
<meta property="og:description" content="{Descrizione}" />
<meta property="og:image" content="{URL Immagine 1200x630}" />
<meta property="og:url" content="{URL Canonico}" />
<meta property="og:type" content="website" />

<!-- Twitter Cards -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{Titolo}" />
<meta name="twitter:description" content="{Descrizione}" />
<meta name="twitter:image" content="{URL Immagine}" />
```

**JSON-LD Schema** (vedi [references/schema-templates.md](./references/schema-templates.md)):

- WebPage / Article per le pagine di contenuto
- FAQPage per le sezioni FAQ
- Product per le pagine prodotto
- Organization per le pagine "Chi siamo"
- SoftwareApplication per tool/app

**Controlla il Contenuto:**

- [ ] H1 contiene la parola chiave primaria
- [ ] Le immagini hanno testi alt descrittivi
- [ ] Link interni a contenuti correlati
- [ ] I link esterni hanno `rel="noopener noreferrer"`
- [ ] Il contenuto è ottimizzato per i dispositivi mobili
- [ ] La pagina si carica in < 3 secondi

### Step 5: Valida e Monitora

**Validazione Schema:**

```bash
# Apri il Test dei Risultati Multimediali di Google
open "https://search.google.com/test/rich-results?url={encoded_url}"

# Apri il Validatore di Schema.org
open "https://validator.schema.org/?url={encoded_url}"
```

**Controlla lo Stato dell'Indicizzazione:**

```bash
# Google (usa Search Console API o controllo manuale)
open "https://www.google.com/search?q=site:{domain}"

# Bing
open "https://www.bing.com/search?q=site:{domain}"
```

**Genera Report:**

```markdown
## Report di Ottimizzazione SEO/GEO

### Stato Attuale

- Meta Tag: ✅/❌
- Schema Markup: ✅/❌
- Accesso Bot AI: ✅/❌
- Ottimizzazione Mobile: ✅/❌
- Velocità Pagina: X secondi

### Raccomandazioni

1. [Azione priorità 1]
2. [Azione priorità 2]
3. [Azione priorità 3]

### Ottimizzazioni GEO Applicate

- [ ] Schema FAQPage aggiunto
- [ ] Statistiche incluse
- [ ] Citazioni aggiunte
- [ ] Struttura Answer-first
```

## Ottimizzazione Specifica per Piattaforma

Vedi [references/platform-algorithms.md](./references/platform-algorithms.md) per i fattori di ranking dettagliati.

### ChatGPT

- Focus sull'**autorità del dominio del brand** (citato l'11% in più rispetto a terze parti)
- Aggiorna i contenuti entro **30 giorni** (3.2x più citazioni)
- Costruisci **backlink** (>350K domini di riferimento = 8.4 citazioni medie)
- Adatta lo stile del contenuto al formato delle risposte di ChatGPT

### Perplexity

- Consenti **PerplexityBot** nel robots.txt
- Usa lo **Schema FAQ** (tasso di citazione più alto)
- Ospita **documenti PDF** (prioritari per la citazione)
- Focalizzati sulla **rilevanza semantica** rispetto alle parole chiave

### Google AI Overview (SGE)

- Ottimizza per **E-E-A-T** (Esperienza, Competenza, Autorevolezza, Affidabilità)
- Usa **dati strutturati** (markup Schema)
- Costruisci **autorità tematica** (cluster di argomenti + link interni)
- Includi **citazioni autorevoli** (+132% visibilità)

### Microsoft Copilot / Bing

- Assicura l'**indicizzazione su Bing** (richiesta per la citazione)
- Ottimizza per l'**ecosistema Microsoft** (le menzioni su LinkedIn, GitHub aiutano)
- Velocità della pagina **< 2 secondi**
- Definizioni di **entità** chiare

### Claude AI

- Assicura l'**indicizzazione su Brave Search** (Claude usa Brave, non Google)
- Alta **densità fattuale** (preferiti contenuti ricchi di dati)
- Chiara **chiarezza strutturale** (facile da estrarre)

## Dipendenze della Skill

Questa skill funziona meglio con:

- **twitter skill** - Cerca esperti SEO per gli ultimi consigli
- **reddit skill** - Cerca discussioni su r/SEO, r/bigseo per discussioni
- **WebSearch** - Ricerca parole chiave e analisi della concorrenza

## Riferimenti

- [references/platform-algorithms.md](./references/platform-algorithms.md) - Fattori di ranking dettagliati per ogni piattaforma
- [references/geo-research.md](./references/geo-research.md) - Ricerca GEO di Princeton (9 metodi)
- [references/schema-templates.md](./references/schema-templates.md) - Template JSON-LD
- [references/aeo-optimization.md](./references/aeo-optimization.md) - Guida Answer Engine Optimization (Protocollo Q-A-V)
- [references/seo-checklist.md](./references/seo-checklist.md) - Checklist completa per l'audit SEO
- [references/tools-and-apis.md](./references/tools-and-apis.md) - Riferimento a tool e API
- [examples/opc-skills-case-study.md](./examples/opc-skills-case-study.md) - Esempio di caso di studio di ottimizzazione reale
