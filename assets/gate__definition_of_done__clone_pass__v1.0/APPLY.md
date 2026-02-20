# APPLY — gate__definition_of_done__clone_pass__v1.0

## Goal
Force an objective "clone is done" criterion.

## Gates (default 5)
1) **ROUTES**: internal routes exist and resolve
2) **ASSETS**: no unintended external asset URLs
3) **NAV**: dropdown/mega menu interactions pass
4) **API**: mock or live data path yields populated UI (optional gate)
5) **TESTS**: Playwright smoke + regression tests pass

## Apply Steps

1) Create a verifier script (Python recommended):
- checks file structure
- runs tests
- prints summary table
- exits non-zero on fail

```bash
python3 verify_clone.py --site-dir site/ --routes routes.json --run-tests
```

2) Standard command:
```bash
python3 verify_clone.py
```

## Rollback
- Remove `verify_clone.py` and gate configs.
