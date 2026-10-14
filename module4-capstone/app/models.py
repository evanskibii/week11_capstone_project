from typing import Literal
from pydantic import BaseModel, Field

class TriageRequest(BaseModel):
    message: str = Field(min_length=3, max_length=2000)
    consent: bool = True

class TriageResponse(BaseModel):
    route: Literal["emergency", "urgent", "routine", "self_care"]
    urgency_score: int = Field(ge=0, le=100)
    reason_codes: list[str]
    guidance: str
    mode: Literal["deterministic_stub"] = "deterministic_stub"
    disclaimer: str = "Teaching system only; not a diagnosis or substitute for a clinician."
