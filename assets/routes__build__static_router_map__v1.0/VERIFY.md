# VERIFY — routes__build__static_router_map__v1.0

PASS if:
- `route_map.json` exists and every entry points to a real file or route
- Link smoke test passes for all mapped routes
- No mapped route returns 404
