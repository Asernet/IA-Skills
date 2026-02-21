# Workflow di Analisi: Validazione delle Variabili

Per garantire che il tuo template funzioni correttamente, devi convalidare che la pagina di destinazione contenga effettivamente i dati che desideri estrarre.

## 1. Recupera la Pagina

Usa lo strumento `WebFetch` o uno snapshot del DOM del browser per recuperare il contenuto di un URL rappresentativo fornito dall'utente.

```text
WebFetch(url="https://example.com/recipe/chocolate-cake")
```

## 2. Analizza l'Output

### Controlla Schema.org (Consigliato)

Cerca `<script type="application/ld+json">`. Contiene dati strutturati, che rappresentano il modo più affidabile per estrarre informazioni.

**Esempio Trovato nell'HTML:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Recipe",
  "name": "Chocolate Cake",
  "author": {
    "@type": "Person",
    "name": "John Doe"
  }
}
```

**Conclusione:**

- `{{schema:Recipe:name}}` è valido.
- `{{schema:Recipe:author.name}}` è valido.
- **Suggerimento:** Puoi usare `schema:Recipe` nell'array `triggers` per selezionare automaticamente questo template per qualsiasi pagina con questo schema.

### Controlla i Meta Tag

Cerca i tag `<meta>` nella sezione `<head>`.

**Esempio Trovato nell'HTML:**

```html
<meta property="og:title" content="The Best Chocolate Cake" />
<meta name="description" content="A rich, moist chocolate cake recipe." />
```

**Conclusione:**

- `{{meta:og:title}}` è valido.
- `{{meta:description}}` è valido.

### Controlla i Selettori CSS (Verificato)

Se Schema e Meta tag mancano, cerca la struttura HTML (classi e ID) da usare con `{{selector:...}}`.
I selettori devono essere verificati rispetto all'HTML recuperato o allo snapshot del DOM. Non indovinare i selettori.

**Esempio Trovato nell'HTML:**

```html
<div class="article-body">
  <h1 id="main-title">Chocolate Cake</h1>
  <span class="author-name">By John Doe</span>
</div>
```

**Conclusione:**

- `{{selector:h1#main-title}}` o `{{selector:h1}}` può estrarre il titolo.
- `{{selector:.author-name}}` può estrarre l'autore.

## 3. Verifica rispetto alla Base

Confronta i dati disponibili dalla tua analisi con le proprietà richieste dalla Base dell'utente (vedi `references/bases-workflow.md`).

- Se la Base richiede `ingredients` ma la pagina non ha uno Schema o una chiara struttura a elenco, avvisa l'utente che questo campo potrebbe richiedere l'inserimento manuale o una variabile di prompt.
