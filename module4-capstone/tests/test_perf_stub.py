import time, pytest
from app.router import route_message

@pytest.mark.perf
def test_teaching_router_latency():
    start = time.perf_counter()
    for _ in range(1000):
        route_message("synthetic mild headache")
    elapsed_ms = (time.perf_counter() - start) * 1000
    assert elapsed_ms < 1000, "Teaching threshold on local hardware, not a production SLA"
