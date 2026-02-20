# APPLY — ui__test__interaction_regression__v1.0

## Goal
Prevent silent breakage of UI interactions in repeated cloning cycles.

## Apply Steps

1) Reuse Playwright install (from link smoke asset) or install it:
```bash
npm i -D @playwright/test
npx playwright install
```

2) Identify 3~7 "must-work" components (tabs/accordion/modal/menu/slider).

3) Create tests that:
- click/tap toggles
- assert visible state
- capture screenshot on failure

4) Run:
```bash
npx playwright test tests/interaction-regression.spec.ts --reporter=html
```

## Rollback
- Remove regression test file(s).
