import pytest
from app.router import route_message

@pytest.mark.parametrize("text,expected", [
    ("I have chest pain", "emergency"),
    ("The high fever is worsening", "urgent"),
    ("I have a headache", "routine"),
    ("I feel slightly tired", "self_care"),
])
def test_routes(text, expected):
    assert route_message(text)["route"] == expected
