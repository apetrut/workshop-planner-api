# Workshop Planner API

FastAPI service exposing workshop CRUD routes backed by Azure Cosmos DB and a health check.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

```powershell
$env:COSMOS_ENDPOINT = "https://your-account.documents.azure.com:443/"
$env:COSMOS_KEY = "your-account-key"
$env:COSMOS_DATABASE = "workshop-planner"
$env:COSMOS_CONTAINER = "workshops"
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

`COSMOS_ENDPOINT` and `COSMOS_KEY` are required. Database and container names default to
`workshop-planner` and `workshops`. TLS certificate verification is enabled by default;
for the Azure Cosmos DB vNext Linux Emulator's self-signed certificate, set
`COSMOS_SSL_VERIFY=false` for local development only.

## Test

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Persistence

- `GET /health` returns `{"status": "ok"}`.
- Workshop CRUD operations use the official `azure-cosmos` Python SDK through
	`CosmosWorkshopRepository`.
- The workshops container uses `/id` as its partition key. Item reads, replacements, and
	deletes use direct point operations; listing workshops is a cross-partition query.
- Malformed workshop payloads (missing required fields) return `422 Unprocessable Entity` from Pydantic validation.
