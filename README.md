# Workshop Planner API

FastAPI service exposing workshop CRUD routes and a health check. No persistence layer exists yet.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

## Test

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Current behavior

- `GET /health` returns `{"status": "ok"}`.
- `POST /workshops`, `GET /workshops`, `GET /workshops/{id}`, `PUT /workshops/{id}`, `DELETE /workshops/{id}` are routed and validate request/response shapes via `WorkshopInput`/`Workshop`, but all return `501 Not Implemented` — no persistence backend is wired up yet.
- Malformed workshop payloads (missing required fields) return `422 Unprocessable Entity` from Pydantic validation.
