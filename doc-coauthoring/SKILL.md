---
name: doc-coauthoring
description: Workflow strutturato per co-autore documentazione, proposte o specifiche tecniche. Aiuta a trasferire contesto e raffinare i contenuti.
---

# Workflow di Co-Autore Documenti

Questa skill fornisce un workflow strutturato per guidare gli utenti attraverso la creazione collaborativa di documenti. Agisci come una guida attiva, accompagnando gli utenti attraverso tre stadi: Raccolta Contesto, Raffinamento & Struttura, e Testing Lettore.

## Quando Offrire Questo Workflow

**Condizioni di attivazione:**

- L'utente menziona scrivere documentazione: "scrivi un doc", "bozza una proposta", "crea una spec", "write up"
- L'utente menziona tipi specifici di doc: "PRD", "design doc", "decision doc", "RFC"
- L'utente sembra iniziare un task di scrittura sostanziale

**Offerta iniziale:**
Offri all'utente un workflow strutturato per co-autore il documento. Spiega i tre stadi:

1. **Raccolta Contesto**: L'utente fornisce tutto il contesto rilevante mentre Claude fa domande di chiarimento
2. **Raffinamento & Struttura**: Costruisci iterativamente ogni sezione attraverso brainstorming ed editing
3. **Testing Lettore**: Testa il doc con un Claude fresco (senza contesto) per catturare punti ciechi prima che altri lo leggano

Spiega che questo approccio aiuta ad assicurare che il doc funzioni bene quando altri lo leggono (incluso quando lo incollano in Claude). Chiedi se vogliono provare questo workflow o preferiscono lavorare a forma libera.

Se l'utente declina, lavora a forma libera. Se l'utente accetta, procedi allo Stadio 1.

## Stadio 1: Raccolta Contesto

**Obiettivo:** Chiudere il divario tra ciò che l'utente sa e ciò che Claude sa, abilitando una guida intelligente più tardi.

### Domande Iniziali

Inizia chiedendo all'utente il meta-contesto sul documento:

1. Che tipo di documento è questo? (es. specifica tecnica, decision doc, proposta)
2. Chi è l'audience primaria?
3. Qual è l'impatto desiderato quando qualcuno legge questo?
4. C'è un template o formato specifico da seguire?
5. Altri vincoli o contesto da sapere?

Informali che possono rispondere in shorthand o scaricare informazioni come preferiscono.

**Se l'utente fornisce un template o menziona un tipo di doc:**

- Chiedi se hanno un documento template da condividere
- Se forniscono un link a un documento condiviso, usa l'integrazione appropriata per recuperarlo
- Se forniscono un file, leggilo

**Se l'utente menziona di editare un documento condiviso esistente:**

- Usa l'integrazione appropriata per leggere lo stato corrente
- Controlla immagini senza alt-text
- Se esistono immagini senza alt-text, spiega che quando altri usano Claude per capire il doc, Claude non sarà in grado di vederle. Chiedi se vogliono generato alt-text. Se sì, richiedi che incollino ogni immagine nella chat per generazione alt-text descrittivo.

### Info Dumping

Una volta risposto alle domande iniziali, incoraggia l'utente a scaricare tutto il contesto che hanno. Richiedi informazioni come:

- Background sul progetto/problema
- Discussioni del team correlate o documenti condivisi
- Perché soluzioni alternative non vengono usate
- Contesto organizzativo (dinamiche team, incidenti passati, politica)
- Pressioni di timeline o vincoli
- Architettura tecnica o dipendenze
- Preoccupazioni degli stakeholder

Consiglia loro di non preoccuparsi di organizzarlo - buttalo solo fuori. Offri modi multipli per fornire contesto:

- Info dump flusso di coscienza
- Indica canali del team o thread da leggere
- Link a documenti condivisi

**Se integrazioni sono disponibili** (es. Slack, Teams, Google Drive, SharePoint, o altri server MCP), menziona che questi possono essere usati per tirare dentro contesto direttamente.

**Se nessuna integrazione è rilevata e in Claude.ai o app Claude:** Suggerisci che possono abilitare connettori nelle loro impostazioni Claude per permettere di tirare contesto da app di messaggistica e storage documenti direttamente.

Informali che domande di chiarimento verranno fatte una volta fatto il loro dump iniziale.

**Durante la raccolta contesto:**

- Se l'utente menziona canali team o documenti condivisi:
  - Se integrazioni disponibili: Informali che il contenuto verrà letto ora, poi usa l'integrazione appropriata
  - Se integrazioni non disponibili: Spiega mancanza di accesso. Suggerisci di abilitare connettori nelle impostazioni Claude, o incollare il contenuto rilevante direttamente.

- Se l'utente menziona entità/progetti che sono sconosciuti:
  - Chiedi se tool connessi dovrebbero essere cercati per saperne di più
  - Aspetta conferma utente prima di cercare

- Mentre l'utente fornisce contesto, traccia cosa viene appreso e cosa è ancora non chiaro

**Fare domande di chiarimento:**

Quando l'utente segnala di aver fatto il loro dump iniziale (o dopo sostanziale contesto fornito), fai domande di chiarimento per assicurare comprensione:

Genera 5-10 domande numerate basate su gap nel contesto.

Informali che possono usare shorthand per rispondere (es., "1: sì, 2: vedi #channel, 3: no perché retrocompatibilità"), linkare a più doc, indicare canali da leggere, o solo continuare l'info-dumping. Qualsiasi cosa sia più efficiente per loro.

**Condizione di uscita:**
Sufficiente contesto è stato raccolto quando le domande mostrano comprensione - quando casi limite e trade-off possono essere chiesti senza bisogno di spiegare le basi.

**Transizione:**
Chiedi se c'è altro contesto che vogliono fornire a questo stadio, o se è tempo di passare a bozzare il documento.

Se l'utente vuole aggiungere altro, lascialo fare. Quando pronto, procedi allo Stadio 2.

## Stadio 2: Raffinamento & Struttura

**Obiettivo:** Costruire il documento sezione per sezione attraverso brainstorming, curatela e raffinamento iterativo.

**Istruzioni all'utente:**
Spiega che il documento sarà costruito sezione per sezione. Per ogni sezione:

1. Domande di chiarimento verranno fatte su cosa includere
2. 5-20 opzioni verranno brainstormate
3. L'utente indicherà cosa tenere/rimuovere/combinare
4. La sezione verrà bozzata
5. Verrà raffinata attraverso edit chirurgici

Inizia con qualsiasi sezione abbia il maggior numero di incognite (solitamente la decisione/proposta centrale), poi lavora attraverso il resto.

**Ordinamento sezioni:**

Se la struttura del documento è chiara:
Chiedi con quale sezione vorrebbero iniziare.

Suggerisci di iniziare con qualsiasi sezione abbia il maggior numero di incognite. Per decision doc, solitamente è la proposta centrale. Per spec, è tipicamente l'approccio tecnico. Le sezioni di riassunto sono meglio lasciate per ultime.

Se l'utente non sa di quali sezioni ha bisogno:
Basandoti sul tipo di documento e template, suggerisci 3-5 sezioni appropriate per il tipo di doc.

Chiedi se questa struttura funziona, o se vogliono aggiustarla.

**Una volta che la struttura è concordata:**

Crea la struttura iniziale del documento con testo placeholder per tutte le sezioni.

**Se l'accesso agli artefatti è disponibile:**
Usa `create_file` per creare un artefatto. Questo dà sia a Claude che all'utente un'impalcatura su cui lavorare.

Informali che la struttura iniziale con placeholder per tutte le sezioni verrà creata.

Crea artefatto con tutte le intestazioni di sezione e breve testo placeholder come "[To be written]" o "[Content here]".

Fornisci il link all'impalcatura e indica che è tempo di riempire ogni sezione.

**Se nessun accesso agli artefatti:**
Crea un file markdown nella directory di lavoro. Nomina appropriatamente (es., `decision-doc.md`, `technical-spec.md`).

Informali che la struttura iniziale con placeholder per tutte le sezioni verrà creata.

Crea file con tutte le intestazioni di sezione e testo placeholder.

Conferma che il filename è stato creato e indica che è tempo di riempire ogni sezione.

**Per ogni sezione:**

### Passo 1: Domande di Chiarimento

Annuncia che il lavoro inizierà sulla sezione [NOME SEZIONE]. Fai 5-10 domande di chiarimento su cosa dovrebbe essere incluso:

Genera 5-10 domande specifiche basate sul contesto e scopo della sezione.

Informali che possono rispondere in shorthand o solo indicare cosa è importante coprire.

### Passo 2: Brainstorming

Per la sezione [NOME SEZIONE], brainstorma [5-20] cose che potrebbero essere incluse, dipendendo dalla complessità della sezione. Cerca:

- Contesto condiviso che potrebbe essere stato dimenticato
- Angoli o considerazioni non ancora menzionati

Genera 5-20 opzioni numerate basate sulla complessità della sezione. Alla fine, offri di brainstormare di più se vogliono opzioni addizionali.

### Passo 3: Curatela

Chiedi quali punti dovrebbero essere tenuti, rimossi o combinati. Richiedi brevi giustificazioni per aiutare a imparare le priorità per le prossime sezioni.

Fornisci esempi:

- "Tieni 1,4,7,9"
- "Rimuovi 3 (duplica 1)"
- "Rimuovi 6 (audience sa già questo)"
- "Combina 11 e 12"

**Se l'utente dà feedback a forma libera** (es., "sembra buono" o "mi piace la maggior parte ma...") invece di selezioni numerate, estrai le loro preferenze e procedi. Parla cosa vogliono tenuto/rimosso/cambiato e applicalo.

### Passo 4: Controllo Gap

Basandoti su cosa hanno selezionato, chiedi se c'è qualcosa di importante mancante per la sezione [NOME SEZIONE].

### Passo 5: Drafting (Bozza)

Usa `str_replace` per sostituire il testo placeholder per questa sezione con il contenuto bozzato attuale.

Annuncia che la sezione [NOME SEZIONE] verrà bozzata ora basandosi su cosa hanno selezionato.

**Se usi artefatti:**
Dopo aver bozzato, fornisci un link all'artefatto.

Chiedi loro di leggerlo e indicare cosa cambiare. Nota che essere specifici aiuta l'apprendimento per le prossime sezioni.

**Se usi un file (no artefatti):**
Dopo aver bozzato, conferma completamento.

Informali che la sezione [NOME SEZIONE] è stata bozzata in [filename]. Chiedi loro di leggerlo e indicare cosa cambiare. Nota che essere specifici aiuta l'apprendimento per le prossime sezioni.

**Istruzione chiave per utente (includi quando bozzi la prima sezione):**
Fornisci una nota: Invece di editare il doc direttamente, chiedi loro di indicare cosa cambiare. Questo aiuta l'apprendimento del loro stile per sezioni future. Per esempio: "Rimuovi il bullet X - già coperto da Y" o "Rendi il terzo paragrafo più conciso".

### Passo 6: Raffinamento Iterativo

Mentre l'utente fornisce feedback:

- Usa `str_replace` per fare edit (mai ristampare l'intero doc)
- **Se usi artefatti:** Fornisci link all'artefatto dopo ogni edit
- **Se usi file:** Conferma solo che gli edit sono completi
- Se l'utente edita il doc direttamente e chiede di leggerlo: nota mentalmente i cambiamenti che hanno fatto e tienili a mente per sezioni future (questo mostra le loro preferenze)

**Continua a iterare** finché l'utente è soddisfatto con la sezione.

### Controllo Qualità

Dopo 3 iterazioni consecutive senza cambiamenti sostanziali, chiedi se qualcosa può essere rimosso senza perdere informazioni importanti.

Quando la sezione è fatta, conferma [NOME SEZIONE] è completa. Chiedi se pronto a muovere alla prossima sezione.

**Ripeti per tutte le sezioni.**

### Quasi Completamento

Mentre ti avvicini al completamento (80%+ delle sezioni fatte), annuncia intenzione di rileggere l'intero documento e controlla per:

- Flusso e consistenza attraverso le sezioni
- Ridondanza o contraddizioni
- Qualsiasi cosa che sembra "slop" o riempitivo generico
- Se ogni frase porta peso

Leggi intero documento e fornisci feedback.

**Quando tutte le sezioni sono bozzate e raffinate:**
Annuncia che tutte le sezioni sono bozzate. Indica intenzione di revisionare il documento completo una volta in più.

Revisiona per coerenza complessiva, flusso, completezza.

Fornisci qualsiasi suggerimento finale.

Chiedi se pronto a muovere al Testing Lettore, o se vogliono raffinare altro.

## Stadio 3: Testing Lettore

**Obiettivo:** Testare il documento con un Claude fresco (nessun bleed di contesto) per verificare che funzioni per i lettori.

**Istruzioni all'utente:**
Spiega che il testing avverrà ora per vedere se il documento funziona effettivamente per i lettori. Questo cattura punti ciechi - cose che hanno senso per gli autori ma potrebbero confondere gli altri.

### Approccio di Testing

**Se l'accesso a sub-agenti è disponibile (es., in Claude Code):**

Esegui il testing direttamente senza coinvolgimento utente.

### Passo 1: Predici Domande Lettore

Annuncia intenzione di predire quali domande i lettori potrebbero chiedere quando provano a scoprire questo documento.

Genera 5-10 domande che i lettori chiederebbero realisticamente.

### Passo 2: Testa con Sub-Agente

Annuncia che queste domande verranno testate con un'istanza Claude fresca (nessun contesto da questa conversazione).

Per ogni domanda, invoca un sub-agente con solo il contenuto del documento e la domanda.

Riassumi cosa il Lettore Claude ha capito giusto/sbagliato per ogni domanda.

### Passo 3: Esegui Controlli Addizionali

Annuncia che controlli addizionali verranno eseguiti.

Invoca sub-agente per controllare ambiguità, false assunzioni, contraddizioni.

Riassumi qualsiasi problema trovato.

### Passo 4: Report e Fix

Se problemi trovati:
Riporta che il Lettore Claude ha faticato con problemi specifici.

Elenca i problemi specifici.

Indica intenzione di fixare questi gap.

Torna al raffinamento per sezioni problematiche.

---

**Se nessun accesso a sub-agenti (es., interfaccia web claude.ai):**

L'utente dovrà fare il testing manualmente.

### Passo 1: Predici Domande Lettore

Chiedi quali domande le persone potrebbero chiedere quando provano a scoprire questo documento. Cosa scriverebbero in Claude.ai?

Genera 5-10 domande che i lettori chiederebbero realisticamente.

### Passo 2: Setup Testing

Fornisci istruzioni di testing:

1. Apri una conversazione Claude fresca: https://claude.ai
2. Incolla o condividi il contenuto del documento (se usi una piattaforma doc condivisa con connettori abilitati, fornisci il link)
3. Chiedi al Lettore Claude le domande generate

Per ogni domanda, istruisci il Lettore Claude a fornire:

- La risposta
- Se qualcosa era ambiguo o non chiaro
- Quale conoscenza/contesto il doc assume sia già nota

Controlla se il Lettore Claude dà risposte corrette o malinterpreta qualcosa.

### Passo 3: Controlli Addizionali

Inoltre chiedi al Lettore Claude:

- "Cosa in questo doc potrebbe essere ambiguo o non chiaro ai lettori?"
- "Quale conoscenza o contesto questo doc assume i lettori abbiano già?"
- "Ci sono contraddizioni interne o inconsistenze?"

### Passo 4: Itera Basato sui Risultati

Chiedi cosa il Lettore Claude ha sbagliato o con cui ha faticato. Indica intenzione di fixare quei gap.

Torna indietro al raffinamento per qualsiasi sezione problematica.

---

### Condizione di Uscita (Entrambi gli Approcci)

Quando il Lettore Claude risponde consistentemente alle domande correttamente e non fa emergere nuovi gap o ambiguità, il doc è pronto.

## Revisione Finale

Quando il Testing Lettore passa:
Annuncia che il doc ha passato il testing del Lettore Claude. Prima del completamento:

1. Raccomanda che facciano una rilettura finale loro stessi - possiedono questo documento e sono responsabili per la sua qualità
2. Suggerisci di ricontrollare qualsiasi fatto, link, o dettaglio tecnico
3. Chiedi loro di verificare che raggiunga l'impatto che volevano

Chiedi se vogliono una revisione in più, o se il lavoro è fatto.

**Se l'utente vuole revisione finale, forniscila. Altrimenti:**
Annuncia completamento documento. Fornisci qualche consiglio finale:

- Considera di linkare questa conversazione in un'appendice così i lettori possono vedere come il doc è stato sviluppato
- Usa appendici per fornire profondità senza gonfiare il doc principale
- Aggiorna il doc man mano che il feedback viene ricevuto da lettori reali

## Consigli per Guida Efficace

**Tono:**

- Sii diretto e procedurale
- Spiega il razionale brevemente quando influenza il comportamento utente
- Non provare a "vendere" l'approccio - eseguilo solo

**Gestire Deviazioni:**

- Se l'utente vuole saltare uno stadio: Chiedi se vogliono saltare questo e scrivere a forma libera
- Se l'utente sembra frustrato: Riconosci che questo sta prendendo più tempo del previsto. Suggerisci modi per muovere più velocemente
- Dai sempre all'utente agenzia per aggiustare il processo

**Gestione Contesto:**

- Attraverso tutto, se il contesto manca su qualcosa menzionato, chiedi proattivamente
- Non lasciare accumulare gap - indirizzali man mano che vengono fuori

**Gestione Artefatti:**

- Usa `create_file` per bozzare sezioni intere
- Usa `str_replace` per tutti gli edit
- Fornisci link artefatto dopo ogni cambiamento
- Mai usare artefatti per liste brainstorming - quella è solo conversazione

**Qualità sopra Velocità:**

- Non correre attraverso gli stadi
- Ogni iterazione dovrebbe fare miglioramenti significativi
- L'obiettivo è un documento che funziona effettivamente per i lettori
