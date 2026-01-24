---
name: hosted-agents
description: Usa questa skill per creare agenti in background, ambienti sandboxed o infrastrutture multi-agente persistenti.
---

# Infrastruttura Agenti Hosted

Gli agenti hosted girano in ambienti sandboxed remoti piuttosto che su macchine locali. Quando progettati bene, forniscono concorrenza illimitata, ambienti di esecuzione consistenti e collaborazione multiplayer. L'insight critico è che la velocità della sessione dovrebbe essere limitata solo dal time-to-first-token del provider del modello, con tutto il setup dell'infrastruttura completato prima che l'utente inizi la sua sessione.

## Quando Attivare

Attiva questa skill quando:

- Costruisci agenti di coding in background che girano indipendentemente dai dispositivi utente
- Progetti ambienti di esecuzione sandboxed per carichi di lavoro agente
- Implementi sessioni agente multiplayer con stato condiviso
- Crei interfacce agente multi-client (Slack, Web, Estensioni Chrome)
- Scali infrastruttura agente oltre i vincoli della macchina locale
- Costruisci sistemi dove gli agenti spawnano sub-agenti per lavoro parallelo

## Concetti Chiave

Gli agenti hosted indirizzano la limitazione fondamentale dell'esecuzione agente locale: contesa risorse, inconsistenza ambiente e vincoli singolo-utente. Spostando l'esecuzione agente in ambienti sandboxed remoti, i team ottengono concorrenza illimitata, ambienti riproducibili e workflow collaborativi.

L'architettura consiste in tre layer: infrastruttura sandbox per esecuzione isolata, layer API per gestione stato e coordinamento client, e interfacce client per interazione utente attraverso piattaforme. Ogni layer ha requisiti di design specifici che abilitano il sistema a scalare.

## Argomenti Dettagliati

### Infrastruttura Sandbox

**La Sfida Centrale**
Far partire ambienti di sviluppo completi velocemente è la sfida tecnica primaria. Gli utenti si aspettano avvii di sessione quasi istantanei, ma gli ambienti di sviluppo richiedono cloning repository, installazione dipendenze ed esecuzione passaggi build.

**Pattern Registry Immagini**
Pre-costruisci immagini ambiente a cadenza regolare (ogni 30 minuti funziona bene). Ogni immagine contiene:

- Repository clonato a un commit noto
- Tutte le dipendenze runtime installate
- Setup iniziale e comandi build completati
- File cachati da app in esecuzione e suite test una volta

Quando inizi una sessione, fai partire una sandbox dall'immagine più recente. Il repository è al massimo vecchio di 30 minuti, rendendo la sincronizzazione con l'ultimo codice molto più veloce.

**Snapshot e Restore**
Prendi snapshot del filesystem a punti chiave:

- Dopo build immagine iniziale (base snapshot)
- Quando l'agente finisce di fare cambiamenti (session snapshot)
- Prima dell'uscita sandbox per potenziale follow-up

Questo abilita ripristino istantaneo per prompt di follow-up senza rieseguire il setup.

**Configurazione Git per Agenti Background**
Poiché le operazioni git non sono legate a un utente specifico durante le build immagine:

- Genera token installazione app GitHub per accesso repository durante clone
- Aggiorna `user.name` e `user.email` di git quando committi e pushi cambiamenti
- Usa l'identità dell'utente che fa il prompt per i commit, non l'identità dell'app

**Strategia Warm Pool**
Mantieni una pool di sandbox pre-riscaldate per repository ad alto volume:

- Le sandbox sono pronte prima che gli utenti inizino le sessioni
- Scadi e ricrea entry pool man mano che nuove build immagine completano
- Inizia a riscaldare sandbox appena l'utente inizia a digitare (predictive warm-up)

### Selezione Framework Agente

**Architettura Server-First**
Scegli un framework agente strutturato come server first, con TUI e app desktop come client. Questo abilita:

- Client custom multipli senza duplicare logica agente
- Comportamento consistente attraverso tutte le superfici di interazione
- Sistemi plugin per estendere funzionalità
- Architetture event-driven per aggiornamenti real-time

**Codice come Fonte di Verità**
Seleziona framework dove l'agente può leggere il proprio codice sorgente per capire il comportamento. Questo è sottovalutato nello sviluppo AI: avere il codice come fonte di verità previene allucinazioni sulle capacità dell'agente stesso.

**Requisiti Sistema Plugin**
Il framework dovrebbe supportare plugin che:

- Ascoltano eventi esecuzione tool (es., `tool.execute.before`)
- Bloccano o modificano chiamate tool condizionalmente
- Iniettano contesto o stato a runtime

### Ottimizzazioni Velocità

**Predictive Warm-Up**
Inizia a riscaldare la sandbox appena un utente inizia a digitare il proprio prompt:

- Clona ultimi cambiamenti in parallelo con digitazione utente
- Esegui setup iniziale prima che l'utente prema invio
- Per spin-up veloce, la sandbox può essere pronta prima che l'utente finisca di digitare

**Lettura File Parallela**
Permetti all'agente di iniziare a leggere file immediatamente, anche se la sync dall'ultimo branch base non è completa:

- In grandi repository, prompt in arrivo modificano raramente file cambiati di recente
- L'agente può ricercare immediatamente senza aspettare sync git
- Blocca edit file (non letture) finché la sincronizzazione completa

**Massimizza Lavoro Build-Time**
Sposta tutto il possibile al passaggio build immagine:

- Installazione dipendenze completa
- Setup schema database
- Esecuzioni iniziali app e suite test (popola cache)
- Durata build-time è invisibile agli utenti

### Agenti Self-Spawning

**Sessioni Spawnate da Agente**
Crea tool che permettono agli agenti di spawnare nuove sessioni:

- Task di ricerca attraverso repository diversi
- Esecuzione sottotask parallela per grandi cambiamenti
- PR più piccole multiple da un task maggiore

I modelli di frontiera sono capaci di contenere se stessi. I tool dovrebbero:

- Iniziare una nuova sessione con parametri specificati
- Leggere stato di qualsiasi sessione (capacità check-in)
- Continuare lavoro principale mentre le sub-sessioni girano in parallelo

**Prompt Engineering per Self-Spawning**
Ingegnerizza prompt per guidare quando gli agenti spawnano sub-sessioni:

- Task di ricerca che richiedono esplorazione cross-repository
- Rompere cambiamenti monolitici in PR più piccole
- Esplorazione parallela di approcci diversi

### Layer API

**Isolamento Stato Per-Sessione**
Ogni sessione richiede il proprio storage stato isolato:

- Database dedicato per sessione (SQLite per sessione funziona bene)
- Nessuna sessione può impattare la performance di un'altra
- Gestisce centinaia di sessioni concorrenti

**Streaming Real-Time**
Il lavoro dell'agente coinvolge aggiornamenti ad alta frequenza:

- Streaming token da provider modello
- Aggiornamenti stato esecuzione tool
- Notifiche cambiamenti file

Connessioni WebSocket con API di ibernazione riducono costi compute durante periodi inattivi mantenendo connessioni aperte.

**Sincronizzazione Attraverso Client**
Costruisci un singolo sistema di stato che sincronizza attraverso:

- Interfacce chat
- Slack bot
- Estensioni Chrome
- Interfacce Web
- Istanze VS Code

Tutti i cambiamenti si sincronizzano allo stato sessione, abilitando switch client senza interruzioni.

### Supporto Multiplayer

**Perché Multiplayer Conta**
Multiplayer abilita:

- Insegnare a non-ingegneri ad usare AI efficacemente
- Sessioni QA live con membri team multipli
- Revisione PR real-time con cambiamenti immediati
- Sessioni di debug collaborativo

**Requisiti Implementazione**

- Modello dati non deve legare sessioni a singoli autori
- Passa info autore a ogni prompt
- Attribuisci cambiamenti codice all'utente che fa il prompt
- Condividi link sessione per collaborazione istantanea

Con architettura di sincronizzazione appropriata, il supporto multiplayer è quasi gratis da aggiungere.

### Autenticazione e Autorizzazione

**Commit Basati su Utente**
Usa autenticazione GitHub per:

- Ottenere token utente per creazione PR
- Aprire PR per conto dell'utente (non dell'app)
- Prevenire che gli utenti approvino i propri cambiamenti

**Flusso Sandbox-to-API**

1. Sandbox pusha cambiamenti (aggiornando git user config)
2. Sandbox invia evento ad API con nome branch e session ID
3. API usa token GitHub dell'utente per creare PR
4. Webhook GitHub notificano API degli eventi PR

### Implementazioni Client

**Integrazione Slack**
Il canale di distribuzione più efficace per adozione interna:

- Crea loop viralità mentre i membri del team vedono altri usarlo
- Nessuna sintassi richiesta, interfaccia chat naturale
- Classifica repository da messaggio, thread context e nome canale

Costruisci un classificatore per determinare in quale repository lavorare:

- Modello veloce con descrizioni dei repository disponibili
- Includi hint per repository comuni
- Permetti opzione "sconosciuto" per casi ambigui

**Interfaccia Web**
Funzionalità core:

- Funziona su desktop e mobile
- Streaming real-time lavoro agente
- Istanza VS Code hosted che gira dentro sandbox
- Vista desktop streamata per verifica visiva
- Screenshot prima/dopo per PR

Pagina statistiche che mostra:

- Sessioni risultanti in PR mergiate (metrica primaria)
- Utilizzo nel tempo
- Conteggio "umani che fanno prompt" live (prompt negli ultimi 5 minuti)

**Estensione Chrome**
Per utenti non-ingegneri:

- Interfaccia chat sidebar con tool screenshot
- Estrazione interni DOM e React invece di immagini grezze
- Riduce uso token mantenendo precisione
- Distribuisci via policy dispositivo gestito (bypassa Chrome Web Store)

## Guida Pratica

### Gestione Messaggi Follow-Up

Decidi come gestire messaggi inviati durante esecuzione:

- **Approccio Coda**: Messaggi aspettano finché il prompt corrente completa
- **Approccio Inserimento**: Messaggi sono processati immediatamente

La coda è più semplice da gestire e lascia gli utenti inviare pensieri sui prossimi passi mentre l'agente lavora. Costruisci meccanismo per fermare agente a metà esecuzione quando necessario.

### Metriche Che Contano

Traccia metriche che indicano valore reale:

- Sessioni risultanti in PR mergiate (metrica successo primaria)
- Tempo da inizio sessione a prima risposta modello
- Tasso approvazione PR e conteggio revisioni
- Percentuale codice scritto da agente attraverso repository

### Strategia Adozione

Pattern adozione interna che funzionano:

- Lavora in spazi pubblici (canali Slack) per visibilità
- Lascia che il prodotto crei loop di viralità
- Non forzare uso sopra tool esistenti
- Costruisci per bisogni delle persone, non requisiti ipotetici

## Linee Guida

1. Pre-costruisci immagini ambiente a cadenza regolare (30 minuti è un buon default)
2. Inizia a riscaldare sandbox quando gli utenti iniziano a digitare, non quando inviano
3. Permetti letture file prima che sync git completi; blocca solo scritture
4. Struttura framework agente come server-first con client come wrapper sottili
5. Isola stato per sessione per prevenire interferenza cross-sessione
6. Attribuisci commit all'utente che ha fatto il prompt, non all'app
7. Traccia PR mergiate come metrica successo primaria
8. Costruisci per multiplayer dall'inizio; è quasi gratis con architettura sync appropriata

## Integrazione

Questa skill costruisce su multi-agent-patterns per coordinamento agenti e tool-design per interfacce agente-tool. Si connette a:

- **multi-agent-patterns** - Agenti self-spawning seguono pattern supervisore
- **tool-design** - Costruire tool per spawning agente e controllo stato
- **context-optimization** - Gestire contesto attraverso sessioni distribuite
- **filesystem-context** - Usare filesystem per stato sessione e artefatti

## Riferimenti

Riferimento interno:

- [Infrastructure Patterns](./references/infrastructure-patterns.md) - Pattern implementazione dettagliati

Skill correlate in questa collezione:

- multi-agent-patterns - Pattern coordinamento per agenti self-spawning
- tool-design - Progettare tool per ambienti hosted
- context-optimization - Gestire contesto in sistemi distribuiti

Risorse esterne:

- [Ramp](https://builders.ramp.com/post/why-we-built-our-background-agent) - Perché abbiamo costruito il nostro Agente Background
- [Modal Sandboxes](https://modal.com/docs/guide/sandbox) - Infrastruttura sandbox cloud
- [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/) - Gestione stato per-sessione
- [OpenCode](https://github.com/sst/opencode) - Framework agente server-first
