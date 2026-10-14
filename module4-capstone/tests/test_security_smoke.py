import pytest
from fastapi import HTTPException
from app.security import validate_message

def test_rejects_openai_style_key():
    with pytest.raises(HTTPException) as exc:
        validate_message("token sk-abcdefghijklmnopqrstuvwxyz")  # allow-secret-test
    assert exc.value.status_code == 400

def test_rejects_excess_input():
    with pytest.raises(HTTPException) as exc:
        validate_message("x" * 2001)
    assert exc.value.status_code == 413

def test_accepts_normal_synthetic_text():
    assert validate_message("Synthetic headache example") == "Synthetic headache example"
