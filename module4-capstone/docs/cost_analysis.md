# Cost Analysis

## Teaching assumptions
The default path uses local pytest, deterministic routing, static synthetic fixtures, and no paid APIs.

| Activity | Calls | Assumed unit cost | Estimated total | Caption |
|---|---:|---:|---:|---|
| Unit tests and stubs | 0 | $0 | $0 | Executed locally |
| Optional live agent loop | 0-50 | $0-$0.01 | $0-$0.50 | Not executed |
| Optional cloud dry-run | 0 | $0 | $0 | Documentation only |

Expected submitted path: $0. Any future live usage must replace assumptions with provider pricing and measured token/call counts.
