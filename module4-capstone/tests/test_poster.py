import json
from pathlib import Path
from app.poster import validate_poster_metadata

def test_all_poster_metadata_is_synthetic():
    records = json.loads(Path("fixtures/posters_sample.json").read_text(encoding="utf-8"))
    assert records
    for record in records:
        assert validate_poster_metadata(record)["source"] == "synthetic"
