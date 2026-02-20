# SOURCE RUN — gov__define__run_manifest_schema__v1.0

## Run Record

| Field | Value |
|-------|-------|
| Run ID | `RUN-2026-A1F3` |
| Timestamp | 2026-02-15T09:30:00Z |
| Model | claude-opus-4-5-20251101 |
| Prompt | "Define a JSON Schema (Draft 2020-12) for DiffForge Run manifests. Include required fields: run_id, timestamp, model, prompt, gate_result. Add a Ruby validator class." |
| Duration | 35s |
| Token Usage | 2,340 input / 1,890 output |

## Gate Check

| Check | Result |
|-------|--------|
| Patch non-empty | PASS |
| Valid JSON Schema | PASS |
| Required fields enforced | PASS |
| Pattern validation works | PASS |
| Rollback documented | PASS |

**Gate Verdict: PASS**
