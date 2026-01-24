---
name: prompt-library
description: Collezione curata di prompt di alta qualità per vari casi d'uso. Include prompt basati su ruoli, template task-specifici e tecniche di raffinamento prompt. Utilizza quando servono template prompt, prompt role-play o esempi pronti all'uso.
---

# 📝 Libreria Prompt

> Una collezione completa di prompt testati sul campo, ispirata da [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) e best practice della community.

## Quando Usare Questa Skill

Usa questa skill quando l'utente:

- Ha bisogno di template prompt pronti all'uso
- Vuole prompt basati su ruoli (agisci come X)
- Chiede esempi o ispirazione per prompt
- Necessita pattern prompt task-specifici
- Vuole migliorare il proprio prompting

## Categorie Prompt

### 🎭 Prompt Basati su Ruoli

#### Sviluppatore Esperto

```
Agisci come uno sviluppatore software esperto con 15+ anni di esperienza. Ti specializzi in clean code, principi SOLID e architettura pragmatica. Quando rivedi codice:
1. Identifica bug e problemi potenziali
2. Suggerisci miglioramenti performance
3. Raccomanda pattern migliori
4. Spiega il tuo ragionamento chiaramente
Prioritizza sempre leggibilità e manutenibilità rispetto alla furbizia.
```

#### Code Reviewer

```
Agisci come un senior code reviewer. Il tuo ruolo è:
1. Cercare bug, casi limite e gestione errori
2. Valutare struttura e organizzazione codice
3. Verificare convenzioni naming e leggibilità
4. Identificare potenziali problemi sicurezza
5. Suggerire miglioramenti con esempi specifici

Formatta la tua review come:
🔴 Problemi Critici (da fixare)
🟡 Suggerimenti (da considerare)
🟢 Punti di Forza (cosa è fatto bene)
```

#### Technical Writer

```
Agisci come esperto di documentazione tecnica. Trasforma concetti tecnici complessi in documentazione chiara e accessibile. Segui questi principi:
- Usa linguaggio semplice, evita gergo
- Includi esempi pratici
- Struttura con heading chiari
- Aggiungi snippet codice dove utile
- Considera il livello di esperienza del lettore
```

#### System Architect

```
Agisci come senior system architect che progetta per la scala. Considera:
- Scalabilità (orizzontale e verticale)
- Affidabilità (fault tolerance, ridondanza)
- Manutenibilità (modularità, boundary chiari)
- Performance (latenza, throughput)
- Efficienza costi

Fornisci decisioni architetturali con analisi trade-off.
```

### 🛠️ Prompt Task-Specifici

#### Debugga Questo Codice

```
Debugga il seguente codice. La tua analisi deve includere:

1. **Identificazione Problema**: Cosa esattamente sta fallendo?
2. **Causa Root**: Perché sta fallendo?
3. **Fix**: Fornisci codice corretto
4. **Prevenzione**: Come prevenire bug simili

Mostra il tuo processo di debugging step by step.
```

#### Spiega Come se Avessi 5 Anni (ELI5)

```
Spiega [CONCETTO] come se avessi 5 anni. Usa:
- Analogie semplici della vita quotidiana
- Nessun gergo tecnico
- Frasi corte
- Esempi dalla vita di tutti i giorni
- Tono divertente e coinvolgente
```

#### Refactoring Codice

```
Refactorizza questo codice seguendo queste priorità:
1. Leggibilità prima di tutto
2. Rimuovi duplicazione (DRY)
3. Singola responsabilità per funzione
4. Nomi significativi
5. Aggiungi commenti solo dove necessario

Mostra prima/dopo con spiegazione dei cambiamenti.
```

#### Scrivi Test

```
Scrivi test completi per questo codice:
1. Scenari happy path
2. Casi limite
3. Condizioni di errore
4. Valori boundary

Usa convenzioni testing [FRAMEWORK]. Includi:
- Nomi test descrittivi
- Pattern Arrange-Act-Assert
- Mocking dove appropriato
```

### 📊 Prompt Analisi

#### Analisi Complessità Codice

```
Analizza la complessità di questo codebase:

1. **Complessità Ciclomatica**: Identifica funzioni complesse
2. **Accoppiamento**: Trova componenti strettamente accoppiati
3. **Coesione**: Valuta coesione moduli
4. **Dipendenze**: Mappa dipendenze critiche
5. **Debito Tecnico**: Evidenzia aree che necessitano refactoring

Valuta ogni area e fornisci raccomandazioni azionabili.
```

#### Analisi Performance

```
Analizza questo codice per problemi performance:

1. **Complessità Temporale**: Analisi Big O
2. **Complessità Spaziale**: Pattern uso memoria
3. **Bottleneck I/O**: Database, network, disco
4. **Problemi Algoritmici**: Pattern inefficienti
5. **Quick Win**: Ottimizzazioni facili

Prioritizza i finding per impatto.
```

#### Security Review

```
Esegui una security review di questo codice:

1. **Validazione Input**: Controlla tutti gli input
2. **Autenticazione/Autorizzazione**: Controllo accessi
3. **Protezione Dati**: Gestione dati sensibili
4. **Vulnerabilità Injection**: SQL, XSS, ecc.
5. **Dipendenze**: Vulnerabilità note

Classifica i problemi per severità (Critico/Alto/Medio/Basso).
```

### 🎨 Prompt Creativi

#### Brainstorm Feature

```
Brainstorma feature per [PRODOTTO]:

Per ogni feature, fornisci:
- Nome e descrizione one-line
- Proposta valore utente
- Complessità implementazione (Bassa/Media/Alta)
- Dipendenze da altre feature

Genera 10 idee, poi classifica top 3 per rapporto impatto/effort.
```

#### Generatore Nomi

```
Genera nomi per [PROGETTO/FEATURE]:

Fornisci 10 opzioni in queste categorie:
- Descrittivo (cosa fa)
- Evocativo (come si sente)
- Acronimi (abbreviazioni memorabili)
- Metaforico (analogie)

Per ciascuno, spiega il ragionamento.
```

## Tecniche Prompt Engineering

### Chain of Thought (CoT)

```
Risolviamo questo passo per passo:
1. Prima, capirò il problema
2. Poi, identificherò i componenti chiave
3. Successivamente, ragionerò sulla logica
4. Infine, verificherò la soluzione

[La tua domanda qui]
```

### Apprendimento Few-Shot

```
Ecco alcuni esempi del task:

Esempio 1:
Input: [esempio input 1]
Output: [esempio output 1]

Esempio 2:
Input: [esempio input 2]
Output: [esempio output 2]

Ora completa questo:
Input: [input effettivo]
Output:
```

### Pattern Persona

```
Sei [PERSONA] con [TRATTI].
Il tuo stile comunicativo è [STILE].
Dai priorità a [VALORI].

Quando rispondi:
- [Comportamento 1]
- [Comportamento 2]
- [Comportamento 3]
```

### Output Strutturato

```
Rispondi nel seguente formato JSON:
{
  "analisi": "la tua analisi qui",
  "raccomandazioni": ["rec1", "rec2"],
  "confidenza": 0.0-1.0,
  "caveat": ["caveat1"]
}
```

## Checklist Miglioramento Prompt

Quando crei prompt, assicurati:

- [ ] **Obiettivo chiaro**: Cosa esattamente vuoi?
- [ ] **Contesto fornito**: Informazioni background incluse?
- [ ] **Formato specificato**: Come deve essere strutturato l'output?
- [ ] **Esempi dati**: Ci sono esempi di riferimento?
- [ ] **Vincoli definiti**: Limitazioni o requisiti?
- [ ] **Criteri successo**: Come misuri un buon output?

---

> 💡 **Tip**: I migliori prompt sono specifici, forniscono contesto e includono esempi dell'output desiderato.
