---
name: notebooklm-connector
description: Interagisce con il server locale NotebookLM MCP via REST API per caricare file, fare query e scaricare audio.
---

# NotebookLM Connector

Wrapper locale per il server NotebookLM MCP.

## Comandi

1.  **Avvia Server**: `powershell -File skills/notebooklm-connector/scripts/start_server.ps1`
2.  **Usa Client**:
    ```python
    from skills.notebooklm_connector.scripts.api_client import NotebookLMClient
    client = NotebookLMClient()
    client.upload("path/to/file.pdf")
    ```
