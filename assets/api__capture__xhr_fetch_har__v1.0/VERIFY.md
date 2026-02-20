# VERIFY — api__capture__xhr_fetch_har__v1.0

PASS if:
- `captures/network.har` exists and is non-empty
- Contains >= 20 XHR/fetch entries (or your threshold)
- Includes calls for:
  - home feed/list
  - detail page load
  - search/list endpoint (if site has search)
