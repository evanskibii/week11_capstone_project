from decimal import Decimal, ROUND_HALF_UP

STOCK = {"gloves": 240, "masks": 500, "saline": 80}

def estimate_request_cost(units: int, unit_cost_usd: str) -> dict:
    if units < 0:
        raise ValueError("units must be non-negative")
    cost = (Decimal(units) * Decimal(unit_cost_usd)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {"units": units, "unit_cost_usd": str(Decimal(unit_cost_usd)), "total_usd": str(cost), "caption": "Teaching estimate; not a live invoice."}

def lookup_stock(item: str) -> dict:
    key = item.strip().casefold()
    return {"item": key, "quantity": STOCK.get(key), "source": "synthetic teaching table"}
