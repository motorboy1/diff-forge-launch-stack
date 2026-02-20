# APPLY — data__seed__fixture_generator_from_responses__v1.0

## Goal
Turn captured responses into reusable fixtures.

## Apply Steps

1) Input files:
- `captures/api_calls.json` and/or response body dumps

2) Run generator (Node or Python) to produce:
- `mock/fixtures/<endpoint_hash>.json`
- optionally a human-friendly mapping file: `mock/routes.json`

```bash
python3 scripts/generate_fixtures.py --input captures/api_calls.json --output mock/fixtures/
```

3) Ensure deterministic output:
- stable ordering
- stable IDs
- include minimal variants (empty state, one item, many items)

## Rollback
- Delete generated `mock/fixtures/` files.
