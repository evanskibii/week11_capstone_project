import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Rule:
    route: str
    score: int
    code: str
    patterns: tuple[str, ...]

RULES = (
    Rule("emergency", 100, "RED_FLAG_EMERGENCY", (r"chest pain", r"cannot breathe", r"unconscious", r"severe bleeding", r"stroke", r"suicid")),
    Rule("urgent", 75, "URGENT_REVIEW", (r"high fever", r"worsening", r"persistent vomiting", r"severe pain", r"pregnan.*bleed")),
    Rule("routine", 40, "ROUTINE_REVIEW", (r"rash", r"cough", r"headache", r"back pain", r"follow.?up")),
)
GUIDANCE = {
    "emergency": "Seek emergency assistance now or go to the nearest emergency facility.",
    "urgent": "Arrange clinician review as soon as possible today.",
    "routine": "Book a routine clinical review and monitor for worsening symptoms.",
    "self_care": "Use appropriate self-care and seek clinical review if symptoms persist or worsen.",
}

def route_message(message: str) -> dict:
    text = message.casefold()
    for rule in RULES:
        if any(re.search(p, text) for p in rule.patterns):
            return {"route": rule.route, "urgency_score": rule.score, "reason_codes": [rule.code], "guidance": GUIDANCE[rule.route]}
    return {"route": "self_care", "urgency_score": 15, "reason_codes": ["NO_RULE_MATCH"], "guidance": GUIDANCE["self_care"]}
