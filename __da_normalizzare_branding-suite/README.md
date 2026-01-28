# 🎨 Brand Studio AI - Antigravity Suite

Benvenuto nella **Brand Identity Suite**.
Questo progetto contiene un ecosistema di Agenti AI progettati per simulare un'agenzia di branding completa: dal Senior Strategist (Step 1) al Creative Director (Step 2).

## 📂 Struttura del Progetto & Output

Il sistema è progettato per auto-organizzarsi. I file generati (Immagini e Report) vengono salvati automaticamente nella cartella `brand_assets`.

/mio-progetto-branding/
│
├── agent.yaml                # ⚙️ Configurazione (Permessi Web, Image, Filesystem)
├── README.md                 # 📄 Questo file
│
├── skills/                   # 🧠 Le Intelligenze
│   ├── brand-architect.md    # [STEP 1] Strategia & Analisi
│   └── visual-brand-forge.md # [STEP 2] Design & Concept Defense
│
└── brand_assets/             # 📂 [OUTPUT AUTOMATICO]
    ├── 2026..._NomeBrand_logo_v1.png          # 🖼️ Bozze Visive
    ├── 2026..._NomeBrand_logo_v2.png
    └── 2026..._NomeBrand_CONCEPT_DEFENSE.md   # 📝 Report Strategico (New!)


## 🚀 Workflow Operativo (Human-in-the-Loop)
Il processo è sequenziale e richiede la tua approvazione tra le fasi.

### 1️⃣ FASE 1: Strategia & Analisi
Agente: brand-architect Obiettivo: Creare il "Brand Identity Blueprint".

Come fornire l'Input:
Hai due modalità per avviare questa fase. Scegli quella più adatta:

OPZIONE A: Brief Esistente Se il cliente ha già fornito documentazione, scrivi:

"Attiva @brand-architect. Ecco il documento di brief del cliente [Nome]..."

OPZIONE B: Intervista Strategica (Consigliata) Se devi costruire il brand da zero, raccogli le risposte a queste 4 domande chiave e passale all'agente:

1. Identità e Purpose (Visione Interna) Perché la vostra azienda esiste oltre al fare profitto? Se domani chiudeste, cosa mancherebbe al mondo? Cosa fate concretamente ogni giorno per raggiungere questo ideale (Mission)?

2. Personalità (Party Metaphor) Se il brand entrasse in una stanza per una festa, come si comporterebbe? Sarebbe al centro dell'attenzione a raccontare barzellette (Intrattenitore), in un angolo ad ascoltare (Saggio/Empatico), o organizzerebbe i drink per tutti (Leader/Curatore)?

3. Analisi Mercato & PODs Perché un cliente dovrebbe scegliere voi e NON il vostro concorrente più forte? C'è qualcosa che i vostri competitor fanno e che voi vi rifiutate categoricamente di fare?

4. Sintesi Strategica Qual è il singolo problema principale che risolvete e come si sente il cliente DOPO aver usato il vostro prodotto?

"Attiva @brand-architect per il cliente [Nome]. Ecco le info..."

Processo: L'agente analizza il web, studia i competitor e definisce Archetipo e Valori.

Output: Un report in chat. Leggilo e approvalo prima di procedere.

### 2️⃣ FASE 2: Visual & Concept Defense
Agente: visual-brand-forge Obiettivo: Tradurre la strategia in Visual Identity e giustificarla.

Input: Conferma la strategia approvata.

"La strategia è approvata. Attiva @visual-brand-forge per generare gli asset."

Processo:

Genera 3 Payoff.

Crea 4 varianti del logo con Nano Banana.

Scrive la "Matrice di Coerenza".

Output (nella cartella brand_assets/):

🖼️ I Loghi: File PNG pronti all'uso.

📝 Il File CONCEPT_DEFENSE.md: Un documento cruciale che spiega perché il logo è stato disegnato così, collegando ogni scelta (colore, forma) ai Valori e all'Archetipo del Blueprint.

### 💡 A Cosa serve il file CONCEPT_DEFENSE.md?
Non ignorare questo file. È la tua arma di vendita. Contiene argomentazioni come:

"Abbiamo scelto il colore Blu Elettrico non per caso, ma per differenziarci dal competitor X che usa il Rosso..."

"La forma spigolosa riflette l'Archetipo 'Eroe' definito a pagina 3 della strategia..."

Usa questo testo per costruire la presentazione PowerPoint per il cliente.

## Requisiti Tecnici (agent.yaml)
Verifica che il tuo file agent.yaml abbia queste impostazioni attive:

tools.image_gen → enabled: true (Per generare i PNG)

tools.file_system → write: true (Per salvare PNG e MD)

environment.allow_file_creation → true

## 🆘 Troubleshooting
Vedo le immagini in chat ma non nella cartella: Verifica i permessi di scrittura della cartella. Prova a creare manualmente la cartella brand_assets se l'agente non riesce a farlo.

Il file CONCEPT_DEFENSE è vuoto: Assicurati di aver passato il Blueprint Strategico completo alla seconda skill. L'agente non può giustificare le scelte se non conosce la strategia iniziale.