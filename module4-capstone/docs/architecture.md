# Architecture

## Runtime flow
Client -> FastAPI validation -> security guard -> deterministic router -> typed response.

## Supporting components
- `router.py`: ordered transparent rules and retrieval-style guidance table.
- `tools.py`: synthetic stock lookup and decimal-safe teaching cost estimate.
- `agent.py`: allow-listed stub tools with a bounded `max_steps`.
- `poster.py`: validates synthetic clinic-poster metadata and rejects unknown fields.

## Data boundaries
The API is stateless and does not write intake text to disk. Triage and poster fixtures are separate. There is no marketplace fixture. This teaching design does not provide diagnosis or treatment.
