# User Guide

1. Create and activate `.venv`.
2. Install `requirements-dev.txt`.
3. Run `pytest -q`.
4. Run `uvicorn app.api:app --reload`.
5. Open `/docs` and submit a synthetic message with consent set to true.

## Health check
```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## Stub path
No key is required. The response always reports `deterministic_stub` mode.

## Safety
Never paste patient identifiers, credentials, or production text. Emergency output is routing guidance, not diagnosis.
