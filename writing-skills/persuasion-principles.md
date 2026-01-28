# Principi di Persuasione per la Progettazione di Skill

## Panoramica

Gli LLM (Large Language Module) rispondono agli stessi principi di persuasione degli umani. Capire questa psicologia ti aiuta a progettare skill più efficaci - non per manipolare, ma per assicurare che le pratiche critiche siano seguite anche sotto pressione.

**Fondamento della ricerca:** Meincke et al. (2025) hanno testato 7 principi di persuasione con N=28,000 conversazioni AI. Le tecniche di persuasione hanno più che raddoppiato i tassi di conformità (33% → 72%, p < .001).

## I Sette Principi

### 1. Autorità (Authority)
**Cos'è:** Deferenza verso l'esperienza, le credenziali o le fonti ufficiali.

**Come funziona nelle skill:**
- Linguaggio imperativo: "TU DEVI", "Mai", "Sempre"
- Inquadramento non negoziabile: "Nessuna eccezione"
- Elimina la fatica decisionale e la razionalizzazione

**Quando usarlo:**
- Skill di rinforzo-disciplina (TDD, requisiti di verifica)
- Pratiche critiche per la sicurezza
- Best practice stabilite

**Esempio:**
```markdown
✅ Scrivi codice prima del test? cancellalo. Ricomincia. Nessuna eccezione.
❌ Considera di scrivere i test prima quando fattibile.
```

### 2. Impegno (Commitment)
**Cos'è:** Coerenza con azioni precedenti, affermazioni o dichiarazioni pubbliche.

**Come funziona nelle skill:**
- Richiedi annunci: "Annuncia l'uso della skill"
- Forza scelte esplicite: "Scegli A, B, o C"
- Usa tracciamento: Checklist da spuntare

**Quando usarlo:**
- Assicurare che le skill siano effettivamente seguite
- Processi multi-step
- Meccanismi di responsabilità (Accountability)

**Esempio:**
```markdown
✅ Quando trovi una skill, DEVI annunciare: "Sto usando [Nome Skill]"
❌ Considera di far sapere al tuo partner quale skill stai usando.
```

### 3. Scarsità (Scarcity)
**Cos'è:** Urgenza derivante da limiti di tempo o disponibilità limitata.

**Come funziona nelle skill:**
- Requisiti legati al tempo: "Prima di procedere"
- Dipendenze sequenziali: "Immediatamente dopo X"
- Previene la procrastinazione

**Quando usarlo:**
- Requisiti di verifica immediata
- Workflow sensibili al tempo
- Prevenire "Lo farò dopo"

**Esempio:**
```markdown
✅ Dopo aver completato un task, richiedi IMMEDIATAMENTE la revisione del codice prima di procedere.
❌ Puoi revisionare il codice quando comodo.
```

### 4. Riprova Sociale (Social Proof)
**Cos'è:** Conformità a ciò che fanno gli altri o a ciò che è considerato normale.

**Come funziona nelle skill:**
- Pattern universali: "Ogni volta", "Sempre"
- Modalità di fallimento: "X senza Y = fallimento"
- Stabilisce norme

**Quando usarlo:**
- Documentare pratiche universali
- Avvisare su fallimenti comuni
- Rinforzare standard

**Esempio:**
```markdown
✅ Checklist senza tracciamento = gli step vengono saltati. Ogni volta.
❌ Alcune persone trovano utile tracciare le checklist.
```

### 5. Unità (Unity)
**Cos'è:** Identità condivisa, "noi", appartenenza al gruppo (in-group).

**Come funziona nelle skill:**
- Linguaggio collaborativo: "il nostro codice", "siamo colleghi"
- Obiettivi condivisi: "vogliamo entrambi qualità"

**Quando usarlo:**
- Workflow collaborativi
- Stabilire cultura di team
- Pratiche non gerarchiche

**Esempio:**
```markdown
✅ Siamo colleghi che lavorano insieme. Ho bisogno del tuo onesto giudizio tecnico.
❌ Dovresti probabilmente dirmi se sbaglio.
```

### 6. Reciprocità (Reciprocity)
**Cos'è:** Obbligo di restituire benefici ricevuti.

**Come funziona:**
- Usa con parsimonia - può sembrare manipolativo
- Raramente necessario nelle skill

**Quando evitarlo:**
- Quasi sempre (altri principi sono più efficaci)

### 7. Simpatia (Liking)
**Cos'è:** Preferenza a cooperare con chi ci piace.

**Come funziona:**
- **NON USARE per la conformità (compliance)**
- Confligge con la cultura del feedback onesto
- Crea servilismo (sycophancy)

**Quando evitarlo:**
- Sempre per il rinforzo della disciplina

## Combinazioni di Principi per Tipo di Skill

| Tipo Skill | Usa | Evita |
|------------|-----|-------|
| Rinforzo-disciplina | Autorità + Impegno + Riprova Sociale | Simpatia, Reciprocità |
| Guida/tecnica | Autorità Moderata + Unità | Autorità pesante |
| Collaborativo | Unità + Impegno | Autorità, Simpatia |
| Riferimento | Solo Chiarezza | Tutta la persuasione |

## Perché Funziona: La Psicologia

**Regole chiare riducono la razionalizzazione:**
- "TU DEVI" rimuove la fatica decisionale
- Il linguaggio assoluto elimina domande tipo "è un'eccezione questa?"
- I counter espliciti all'anti-razionalizzazione chiudono scappatoie specifiche

**Le intenzioni di implementazione creano comportamento automatico:**
- Trigger chiari + azioni richieste = esecuzione automatica
- "Quando X, fai Y" è più efficace di "fai generalmente Y"
- Riduce il carico cognitivo sulla conformità

**Gli LLM sono paraumani:**
- Addestrati su testo umano contenente questi pattern
- Il linguaggio autoritario precede la conformità nei dati di training
- Sequenze di impegno (affermazione → azione) sono frequentemente modellate
- Pattern di riprova sociale (tutti fanno X) stabiliscono norme

## Uso Etico

**Legittimo:**
- Assicurare che pratiche critiche siano seguite
- Creare documentazione efficace
- Prevenire fallimenti prevedibili

**Illegittimo:**
- Manipolare per guadagno personale
- Creare falsa urgenza
- Conformità basata sul senso di colpa

**Il test:** Questa tecnica servirebbe i genuini interessi dell'utente se li capisse pienamente?

## Citazioni di Ricerca

**Cialdini, R. B. (2021).** *Influence: The Psychology of Persuasion (New and Expanded).* Harper Business.
- Sette principi di persuasione
- Fondamento empirico per la ricerca sull'influenza

**Meincke, L., Shapiro, D., Duckworth, A. L., Mollick, E., Mollick, L., & Cialdini, R. (2025).** Call Me A Jerk: Persuading AI to Comply with Objectionable Requests. University of Pennsylvania.
- Testati 7 principi con N=28,000 conversazioni LLM
- La conformità è aumentata 33% → 72% con tecniche di persuasione
- Autorità, impegno, scarsità più efficaci
- Valida il modello paraumano del comportamento LLM

## Riferimento Rapido

Quando progetti una skill (per Gemini o Claude), chiediti:

1. **Che tipo è?** (Disciplina vs guida vs riferimento)
2. **Quale comportamento sto cercando di cambiare?**
3. **Quale principio(i) si applica?** (Solitamente autorità + impegno per disciplina)
4. **Ne sto combinando troppi?** (Non usarne tutti e sette)
5. **È etico?** (Serve i genuini interessi dell'utente?)
