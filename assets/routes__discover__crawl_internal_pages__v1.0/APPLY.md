# APPLY — routes__discover__crawl_internal_pages__v1.0

## Goal
Generate a reliable internal route list for multi-page cloning.

## Apply Steps

1) Use Playwright crawler OR simple link extractor:
- Start from `/`
- Follow only same-origin links
- Ignore logout/mailto/tel/javascript links
- Cap depth and total pages

```bash
npx playwright install
node scripts/crawl_routes.js --base-url http://localhost:3000 --max-depth 3 --max-pages 50
```

2) Output:
- `routes.json` with:
  - path
  - discovered_from
  - status
  - notes (e.g., requires auth)

## Rollback
- Delete generated `routes.json` and logs.
