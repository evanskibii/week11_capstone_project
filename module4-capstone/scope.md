# Scope

## In scope
- Stateless synthetic-message triage API
- Deterministic rule router with reason codes
- Stub agent with named tools and `max_steps`
- Teaching cost estimator and stock lookup
- Secret-pattern and input-size controls
- Clinic-poster metadata validation without OCR
- Unit, integration, security, gold, and marked performance tests

## Out of scope
Diagnosis, prescriptions, production clinical data, marketplace data, real cloud deployment, and autonomous action.

## Safety boundary
Outputs are routing guidance for a teaching fixture, not medical advice. Emergency indicators produce an emergency-routing response and do not attempt diagnosis.
