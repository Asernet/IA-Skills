$serverPath = "$PSScriptRoot/../../mcp-servers/notebooklm-mcp"
Set-Location $serverPath
Write-Host "Starting NotebookLM API Server..."
npm run start:http
