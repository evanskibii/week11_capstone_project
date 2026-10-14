import json
from pathlib import Path
from app.router import route_message

def test_gold_cases():
    cases = json.loads(Path("fixtures/gold_cases.json").read_text(encoding="utf-8"))
    for case in cases:
        actual = route_message(case["message"])
        assert actual["route"] == case["expected_route"], case["id"]
