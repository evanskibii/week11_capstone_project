# Deployment

## Executed path
Local Python virtual environment, pinned dependencies, pytest, and Uvicorn.

## Local commands
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest -q
uvicorn app.api:app --host 127.0.0.1 --port 8000
```

## Optional container path
Not executed live in this project packet. A future deployment should run as a non-root user, expose a health check, inject configuration through environment variables, scan the image, and preserve exact pins.

## Optional cloud path
Not executed because no Azure or AWS credentials are required for grading. Record the service, region, identity controls, secret store, health evidence, and rollback steps if this path is later executed.
