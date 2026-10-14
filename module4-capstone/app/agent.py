from app.tools import estimate_request_cost, lookup_stock

TOOLS = {"estimate_request_cost": estimate_request_cost, "lookup_stock": lookup_stock}

def run_stub_agent(plan: list[dict], max_steps: int = 3) -> list[dict]:
    if max_steps < 1 or max_steps > 5:
        raise ValueError("max_steps must be between 1 and 5")
    results = []
    for step in plan[:max_steps]:
        name = step.get("tool")
        if name not in TOOLS:
            results.append({"tool": name, "error": "tool_not_allowed"})
            continue
        results.append({"tool": name, "result": TOOLS[name](**step.get("arguments", {}))})
    return results
