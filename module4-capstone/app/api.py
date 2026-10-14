from fastapi import FastAPI, HTTPException
from app.models import TriageRequest, TriageResponse
from app.router import route_message
from app.security import validate_message

app = FastAPI(title="AfyaPlus Module 4 Capstone", version="1.0.0")

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "mode": "deterministic_stub"}

@app.post("/v1/triage", response_model=TriageResponse)
def triage(payload: TriageRequest) -> TriageResponse:
    if not payload.consent:
        raise HTTPException(status_code=400, detail="Consent is required for this teaching request")
    safe_message = validate_message(payload.message)
    return TriageResponse(**route_message(safe_message))
