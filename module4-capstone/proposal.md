# Proposal

## Path choice
AfyaPlus Module 4 Capstone, the recommended official path.

## Problem
Health-operations teams need a small, auditable teaching service that classifies synthetic intake text into emergency, urgent, routine, or self-care routing, while exposing deterministic logistics and cost tools without requiring cloud credentials.

## Dataset scale
The project contains 300 synthetic triage messages and 12 synthetic clinic-poster metadata records. It uses no real patient rows and no production scraping.

## Milestones
1. Define scope and Week 1-10 reuse map.
2. Implement deterministic triage, named tools, and bounded stub agent.
3. Add security smoke, gold, integration, and marked performance tests.
4. Document architecture, deployment, cost, and user operation.
5. Complete feature-branch review and sprint evidence.

## Out of scope
Medical diagnosis, treatment prescription, EHR integration, production identity, live LLM calls, cloud deployment, OCR of real posters, and storage of patient records.

## Success criteria
Green local pytest, documented fallbacks, exact dependency pins, 200-500 synthetic teaching rows, no secrets, and honest peer-review records.
