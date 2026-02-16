---
name: text-animations
description: Pattern di tipografia e animazione del testo per Remotion.
metadata:
  tags: typography, text, typewriter, highlighter ken
---

## Animazioni del testo

Basandoti su `useCurrentFrame()`, riduci la stringa carattere per carattere per creare un effetto macchina da scrivere (typewriter).

## Effetto Macchina da Scrivere (Typewriter)

Vedi [Typewriter](assets/text-animations-typewriter.tsx) per un esempio avanzato con un cursore lampeggiante e una pausa dopo la prima frase.

Usa sempre il ritaglio della stringa (string slicing) per gli effetti macchina da scrivere. Non usare mai l'opacità per singolo carattere.

## Evidenziazione delle parole (Word Highlighting)

Vedi [Word Highlight](assets/text-animations-word-highlight.tsx) per un esempio di come viene animata l'evidenziazione di una parola, come con un evidenziatore.
