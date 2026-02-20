# APPLY — api__replay__mock_server__minimal__v1.0

## Goal
Serve recorded API responses locally.

## Apply Steps

1) Create `mock/` folder:
- `mock/server.js`
- `mock/fixtures/`
- `mock/routes.json` (generated from capture)

```bash
mkdir -p mock/fixtures
node scripts/generate_mock_routes.js --input captures/api_calls.json --output mock/
```

2) Start server:
```bash
node mock/server.js
```

3) Point your clone to mock base URL:
- via `.env` (e.g., `API_BASE_URL=http://localhost:4010`)
- or via proxy rewrite in dev server

## Rollback
- Stop mock server and remove `mock/` folder.
