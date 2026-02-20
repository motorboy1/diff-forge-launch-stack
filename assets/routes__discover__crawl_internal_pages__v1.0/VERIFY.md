# VERIFY — routes__discover__crawl_internal_pages__v1.0

PASS if:
- `routes.json` exists and is valid JSON
- Contains required minimum:
  - `/` plus >= 10 internal routes (configurable)
- No external-domain routes included
- Includes common legal pages if they exist on site:
  - `/terms`, `/privacy` (or detected equivalents)
