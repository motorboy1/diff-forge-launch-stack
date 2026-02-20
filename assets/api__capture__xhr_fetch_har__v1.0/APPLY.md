# APPLY — api__capture__xhr_fetch_har__v1.0

## Goal
Record the API layer of the original site to enable replay/mocking.

## Apply Steps

1) Use Playwright to:
- open base URL
- navigate key pages
- perform key clicks
- record HAR and response bodies where possible

```bash
npx playwright install
node scripts/capture_har.js --base-url https://target-site.com --output captures/
```

2) Save outputs:
- `captures/network.har`
- `captures/api_calls.json` (normalized list)

## Rollback
- Delete `captures/` folder.
