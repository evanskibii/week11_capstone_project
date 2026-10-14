ALLOWED_FIELDS = {"poster_id", "clinic_name", "language", "title", "alt_text", "source"}

def validate_poster_metadata(record: dict) -> dict:
    unknown = set(record) - ALLOWED_FIELDS
    if unknown:
        raise ValueError(f"Unknown fields: {sorted(unknown)}")
    required = {"poster_id", "clinic_name", "language", "title", "alt_text", "source"}
    missing = required - set(record)
    if missing:
        raise ValueError(f"Missing fields: {sorted(missing)}")
    if record["source"] != "synthetic":
        raise ValueError("Only synthetic poster metadata is permitted")
    return dict(record)
