<!-- Aggiornato: 2026-03-04 -->
# Integrazione MCP

## Panoramica

Gemini SEO Special può integrarsi con i server del Model Context Protocol (MCP) per accedere ad API esterne e potenziare le proprie capacità di analisi.

## Integrazioni Disponibili

### API PageSpeed Insights

Utilizza l'API di Google PageSpeed Insights direttamente per dati reali sui Core Web Vitals.

**Configurazione:**

1. Ottieni una chiave API dalla [Google Cloud Console](https://console.cloud.google.com/)
2. Abilita l'API PageSpeed Insights
3. Usala nelle tue analisi:

```bash
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=LA_TUA_CHIAVE_API"
```

### Google Search Console

Per i dati della ricerca organica, utilizza il server MCP `mcp-server-gsc` di [ahonn](https://github.com/ahonn/mcp-server-gsc). Fornisce dati sulle prestazioni di ricerca, ispezione URL e gestione delle sitemap.

**Configurazione:**

*(Nota per Gemini: Questo è l'output attesa se gestito in JSON per la configurazione. Le configurazioni di Gemini MCP potrebbero trovarsi in file globali).*

```json
{
  "mcpServers": {
    "google-search-console": {
      "command": "npx",
      "args": ["-y", "mcp-server-gsc"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "/percorso/per/le/credenziali.json"
      }
    }
  }
}
```

### Server MCP per PageSpeed Insights

Utilizza `mcp-server-pagespeed` di [enemyrr](https://github.com/enemyrr/mcp-server-pagespeed) per audit Lighthouse, metriche sui CWV e punteggi di performance tramite MCP.

**Configurazione:**

```json
{
  "mcpServers": {
    "pagespeed": {
      "command": "npx",
      "args": ["-y", "mcp-server-pagespeed"],
      "env": {
        "PAGESPEED_API_KEY": "la-tua-chiave-api"
      }
    }
  }
}
```

### Server MCP SEO Ufficiali (2025-2026)

L'ecosistema MCP per la SEO è maturato notevolmente. Queste sono integrazioni pronte per la produzione:

| Strumento | Pacchetto / Endpoint | Tipo | Note |
|------|-------------------|------|-------|
| **Ahrefs** | `@ahrefs/mcp` | Ufficiale | Rilasciato a luglio 2025. Supporta modalità locali e remote. Backlink, keyword, dati sull'audit del sito. |
| **Semrush** | `https://mcp.semrush.com/v1/mcp` | Ufficiale (remoto) | Accesso API completo via endpoint MCP remoto. Analisi domini, ricerca keyword, dati backlink. |
| **Google Search Console** | `mcp-server-gsc` | Community | Creato da ahonn. Prestazioni di ricerca, ispezione URL, sitemap. |
| **PageSpeed Insights** | `mcp-server-pagespeed` | Community | Creato da enemyrr. Audit Lighthouse, metriche CWV, punteggi di performance. |
| **DataForSEO** | `dataforseo-mcp-server` | Community | Creato da Skobyn (GitHub: Skobyn/dataforseo-mcp-server). Dati SERP, dati keyword, backlink. |
| **kwrds.ai** | kwrds MCP server | Community | Ricerca keyword, volume di ricerca, calcolo difficoltà. |
| **SEO Review Tools** | SEO Review Tools MCP | Community | API per audit del sito e analisi on-page. |

## Esempi di Utilizzo delle API

### PageSpeed Insights

```python
import requests

def get_pagespeed_data(url: str, api_key: str) -> dict:
    """Recupera i dati di PageSpeed Insights per un URL."""
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": url,
        "key": api_key,
        "strategy": "mobile",  # o "desktop"
        "category": ["performance", "accessibility", "best-practices", "seo"]
    }
    response = requests.get(endpoint, params=params)
    return response.json()
```

### Core Web Vitals dal CrUX

```python
def get_crux_data(url: str, api_key: str) -> dict:
    """Recupera i dati del Chrome UX Report per un URL."""
    endpoint = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"
    payload = {
        "url": url,
        "formFactor": "PHONE"  # o "DESKTOP"
    }
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    response = requests.post(endpoint, json=payload, headers=headers, params=params)
    return response.json()
```

## Metriche Disponibili

### Da PageSpeed Insights

| Metrica | Descrizione |
|--------|-------------|
| LCP | Largest Contentful Paint (dati di lab) |
| INP | Interaction to Next Paint (stimato) |
| CLS | Cumulative Layout Shift (dati di lab) |
| FCP | First Contentful Paint |
| TBT | Total Blocking Time |
| Speed Index | Velocità dell'avanzamento visivo |

### Dal CrUX (Dati sul campo / Field Data)

| Metrica | Descrizione |
|--------|-------------|
| LCP | 75° percentile, utenti reali |
| INP | 75° percentile, utenti reali |
| CLS | 75° percentile, utenti reali |
| TTFB | Time to First Byte |

## Migliori Pratiche

1. **Limiti di Velocità (Rate Limiting)**: Rispetta le quote delle API (tipicamente 25k richieste/giorno per PageSpeed)
2. **Caching**: Usa la cache dei risultati per evitare chiamate API rindondanti
3. **Field vs Lab**: Dai priorità ai dati sul campo (CrUX) riguardo i fattori utili al ranking
4. **Gestione Errori**: Gestisci gli errori delle API in modo adeguato

## Senza Chiavi API

Se non si dispone di chiavi API, Gemini SEO Special può comunque:

1. Analizzare il codice sorgente HTML del sito per potenziali problemi
2. Identificare i comuni problemi di prestazione
3. Verificare la presenza di risorse che bloccano la renderizzazione
4. Valutare opportunità di ottimizzazione delle immagini
5. Rilevare implementazioni che fanno eccessivo uso di JavaScript

L'analisi chiarirà in ogni caso che le misurazioni effettive sui Core Web Vitals richiedono l'acceso ai "Dati sul campo" registrati da utenti in carne ed ossa.
