# APPLY — ui__test__link_smoke__playwright__v1.0

## Goal
Automate a pass/fail check that core links work.

## Prerequisites
- Node.js 18+
- A local server running your clone (example: `http://localhost:3000`)

## Apply Steps

1) Install Playwright:
```bash
npm init -y
npm i -D @playwright/test
npx playwright install
```

2) Create `tests/link-smoke.spec.ts` (or `.js`) and set `BASE_URL` env:
```bash
export BASE_URL="http://localhost:3000"
```

3) Run:
```bash
npx playwright test --reporter=html
npx playwright show-report
```

## Rollback
- Remove `tests/` and uninstall Playwright packages.
