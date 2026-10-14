import pytest
from app.agent import run_stub_agent
from app.tools import estimate_request_cost, lookup_stock

def test_cost_is_decimal_safe():
    assert estimate_request_cost(3, "0.10")["total_usd"] == "0.30"

def test_stock_is_synthetic():
    assert lookup_stock("gloves")["source"] == "synthetic teaching table"

def test_agent_enforces_step_limit():
    plan = [{"tool":"lookup_stock","arguments":{"item":"masks"}}] * 4
    assert len(run_stub_agent(plan, max_steps=2)) == 2

def test_agent_rejects_excessive_max_steps():
    with pytest.raises(ValueError):
        run_stub_agent([], max_steps=10)
