import re
from fastapi import HTTPException

MAX_INPUT_CHARS = 2000
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"(?i)(api[_-]?key|secret|password)\s*[:=]\s*[^\s]{8,}"),
]

def validate_message(message: str) -> str:
    cleaned = message.strip()
    if len(cleaned) > MAX_INPUT_CHARS:
        raise HTTPException(status_code=413, detail="Input exceeds teaching limit")
    if any(pattern.search(cleaned) for pattern in SECRET_PATTERNS):
        raise HTTPException(status_code=400, detail="Potential secret detected")
    return cleaned
