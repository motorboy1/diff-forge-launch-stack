# VERIFY — gate__definition_of_done__clone_pass__v1.0

PASS if all gates succeed:

## ROUTES
- `routes.json` or `route_map.json` exists
- each route resolves (HTTP 200/expected redirect)

## ASSETS
- external URLs in HTML/CSS are 0 (except allowlist)

## NAV
- nav runtime scenarios pass (see nav VERIFY)

## API (optional but recommended)
- mock server enabled
- home + detail pages show populated content

## TESTS
- Playwright smoke passes
- interaction regression passes

Output must include:
- PASS/FAIL table
- artifact paths (html report, screenshots on failure)
