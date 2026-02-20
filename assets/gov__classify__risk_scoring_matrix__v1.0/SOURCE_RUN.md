# SOURCE RUN — gov__classify__risk_scoring_matrix__v1.0

## Run Record

| Field | Value |
|-------|-------|
| Run ID | `RUN-2026-D9A1` |
| Timestamp | 2026-02-15T16:00:00Z |
| Model | claude-opus-4-5-20251101 |
| Prompt | "Create a risk scoring matrix that classifies assets based on domain weight, patch complexity, blast radius, and reversibility. Output total score, band (low/medium/high), and breakdown." |
| Duration | 30s |
| Token Usage | 2,100 input / 1,970 output |

## Gate Check

| Check | Result |
|-------|--------|
| Patch non-empty | PASS |
| Valid Ruby syntax | PASS |
| Score calculation correct | PASS |
| Band classification accurate | PASS |
| Rollback documented | PASS |

**Gate Verdict: PASS**
