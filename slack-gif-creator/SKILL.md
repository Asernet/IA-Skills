---
name: slack-gif-creator
description: Crea GIF animate ottimizzate per Slack partendo da richieste dell'utente.
---

# Creatore GIF Slack

Un toolkit che fornisce utility e conoscenze per creare GIF animate ottimizzate per Slack.

## Requisiti Slack

**Dimensioni:**

- Emoji GIF: 128x128 (raccomandato)
- Messaggio GIF: 480x480

**Parametri:**

- FPS: 10-30 (più basso è file size minore)
- Colori: 48-128 (meno = file size minore)
- Durata: Mantieni sotto 3 secondi per emoji GIF

## Workflow Core

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

# 1. Create builder
builder = GIFBuilder(width=128, height=128, fps=10)

# 2. Generate frames
for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)

    # Draw your animation using PIL primitives
    # (circles, polygons, lines, etc.)

    builder.add_frame(frame)

# 3. Save with optimization
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

## Disegnare Grafica

### Lavorare con Immagini Caricate da Utente

Se un utente carica un'immagine, considera se vuole:

- **Usarla direttamente** (es., "anima questo", "dividi questo in frame")
- **Usarla come ispirazione** (es., "fai qualcosa come questo")

Carica e lavora con immagini usando PIL:

```python
from PIL import Image

uploaded = Image.open('file.png')
# Use directly, or just as reference for colors/style
```

### Disegnare da Zero

Quando disegni grafica da zero, usa primitive PIL ImageDraw:

```python
from PIL import ImageDraw

draw = ImageDraw.Draw(frame)

# Circles/ovals
draw.ellipse([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)

# Stars, triangles, any polygon
points = [(x1, y1), (x2, y2), (x3, y3), ...]
draw.polygon(points, fill=(r, g, b), outline=(r, g, b), width=3)

# Lines
draw.line([(x1, y1), (x2, y2)], fill=(r, g, b), width=5)

# Rectangles
draw.rectangle([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)
```

**Non usare:** Font Emoji (inaffidabili attraverso piattaforme) o assumere che grafica pre-pacchettizzata esista in questa skill.

### Rendere la Grafica Bella

La grafica dovrebbe apparire rifinita e creativa, non base. Ecco come:

**Usa linee più spesse** - Imposta sempre `width=2` o maggiore per contorni e linee. Linee sottili (width=1) sembrano spezzettate e amatoriali.

**Aggiungi profondità visiva**:

- Usa gradienti per sfondi (`create_gradient_background`)
- Stratifica forme multiple per complessità (es., una stella con una stella più piccola dentro)

**Rendi forme più interessanti**:

- Non disegnare solo un cerchio semplice - aggiungi riflessi, anelli o pattern
- Le stelle possono avere bagliori (disegna versioni semi-trasparenti, più grandi dietro)
- Combina forme multiple (stelle + scintille, cerchi + anelli)

**Fai attenzione ai colori**:

- Usa colori vibranti, complementari
- Aggiungi contrasto (contorni scuri su forme chiare, contorni chiari su forme scure)
- Considera la composizione complessiva

**Per forme complesse** (cuori, fiocchi di neve, ecc.):

- Usa combinazioni di poligoni ed ellissi
- Calcola punti attentamente per simmetria
- Aggiungi dettagli (un cuore puo avere una curva riflesso, fiocchi di neve hanno rami intricati)

Sii creativo e dettagliato! Una buona GIF Slack dovrebbe apparire rifinita, non come grafica segnaposto.

## Utility Disponibili

### GIFBuilder (`core.gif_builder`)

Assembla frami e ottimizza per Slack:

```python
builder = GIFBuilder(width=128, height=128, fps=10)
builder.add_frame(frame)  # Add PIL Image
builder.add_frames(frames)  # Add list of frames
builder.save('out.gif', num_colors=48, optimize_for_emoji=True, remove_duplicates=True)
```

### Validator (`core.validators`)

Controlla se la GIF soddisfa i requisiti Slack:

```python
from core.validators import validate_gif, is_slack_ready

# Detailed validation
passes, info = validate_gif('my.gif', is_emoji=True, verbose=True)

# Quick check
if is_slack_ready('my.gif'):
    print("Ready!")
```

### Funzioni Easing (`core.easing`)

Movimento fluido invece che lineare:

```python
from core.easing import interpolate

# Progress from 0.0 to 1.0
t = i / (num_frames - 1)

# Apply easing
y = interpolate(start=0, end=400, t=t, easing='ease_out')

# Available: linear, ease_in, ease_out, ease_in_out,
#           bounce_out, elastic_out, back_out
```

### Helper Frame (`core.frame_composer`)

Funzioni convenienza per bisogni comuni:

```python
from core.frame_composer import (
    create_blank_frame,         # Solid color background
    create_gradient_background,  # Vertical gradient
    draw_circle,                # Helper for circles
    draw_text,                  # Simple text rendering
    draw_star                   # 5-pointed star
)
```

## Concetti Animazione

### Scuoti/Vibra (Shake)

Offset posizione oggetto con oscillazione:

- Usa `math.sin()` o `math.cos()` con indice frame
- Aggiungi piccole variazioni random per feeling naturale
- Applica a posizione x e/o y

### Pulsa/Battito (Pulse/Heartbeat)

Scala dimensione oggetto ritmicamente:

- Usa `math.sin(t * frequency * 2 * math.pi)` per pulso fluido
- Per battito: due pulsi veloci poi pausa (aggiusta onda seno)
- Scala tra 0.8 e 1.2 della dimensione base

### Rimbalzo (Bounce)

Oggetto cade e rimbalza:

- Usa `interpolate()` con `easing='bounce_out'` per atterraggio
- Usa `easing='ease_in'` per caduta (accelerando)
- Applica gravità aumentando velocità y ogni frame

### Gira/Ruota (Spin/Rotate)

Ruota oggetto attorno al centro:

- PIL: `image.rotate(angle, resample=Image.BICUBIC)`
- Per oscillazione: usa onda seno per angolo invece che lineare

### Fade In/Out

Appari o sparisci gradualmente:

- Crea immagine RGBA, aggiusta canale alpha
- O usa `Image.blend(image1, image2, alpha)`
- Fade in: alpha da 0 a 1
- Fade out: alpha da 1 a 0

### Scivola (Slide)

Muovi oggetto da fuori schermo a posizione:

- Posizione inizio: fuori dai bordi frame
- Posizione fine: location target
- Usa `interpolate()` con `easing='ease_out'` per stop fluido
- Per overshoot: usa `easing='back_out'`

### Zoom

Scala e posiziona per effetto zoom:

- Zoom in: scala da 0.1 a 2.0, ritaglia centro
- Zoom out: scala da 2.0 a 1.0
- Può aggiungere motion blur per drammaticità (filtro PIL)

### Esplodi/Scoppio Particelle (Explode)

Crea particelle che irradiano verso l'esterno:

- Genera particelle con angoli e velocità random
- Aggiorna ogni particella: `x += vx`, `y += vy`
- Aggiungi gravità: `vy += gravity_constant`
- Fade out particelle nel tempo (riduci alpha)

## Strategie Ottimizzazione

Solo quando chiesto di rendere il file size più piccolo, implementa alcuni dei seguenti metodi:

1. **Meno frame** - FPS più bassi (10 invece di 20) o durata più breve
2. **Meno colori** - `num_colors=48` invece di 128
3. **Dimensioni minori** - 128x128 invece di 480x480
4. **Rimuovi duplicati** - `remove_duplicates=True` in save()
5. **Modo Emoji** - `optimize_for_emoji=True` auto-ottimizza

```python
# Maximum optimization for emoji
builder.save(
    'emoji.gif',
    num_colors=48,
    optimize_for_emoji=True,
    remove_duplicates=True
)
```

## Filosofia

Questa skill fornisce:

- **Conoscenza**: Requisiti di Slack e concetti animazione
- **Utility**: GIFBuilder, validatori, funzioni easing
- **Flessibilità**: Crea la logica animazione usando primitive PIL

NON fornisce:

- Rigidi template animazione o funzioni pre-fatte
- Rendering font Emoji (inaffidabile attraverso piattaforme)
- Una libreria di grafiche pre-pacchettizzate costruite nella skill

**Nota su caricamenti utente**: Questa skill non include grafiche pre-costruite, ma se un utente carica un'immagine, usa PIL per caricarla e lavorarci - interpreta basato sulla loro richiesta se la vogliono usata direttamente o solo come ispirazione.

Sii creativo! Combina concetti (rimbalzare + ruotare, pulsare + scivolare, ecc.) e usa le piene capacità di PIL.

## Dipendenze

```bash
pip install pillow imageio numpy
```
