# APPLY — routes__build__static_router_map__v1.0

## Goal
Turn discovered internal routes into working routes in your clone.

## Apply Steps

1) Input: `routes.json`

2) Generate `route_map.json`:
- path → output file
- method: static file, server route, SPA fallback

3) Static hosting approach:
```
/pricing → pricing/index.html
/terms   → terms/index.html
```

4) Framework approach:
- **Next.js**: create `app/<route>/page.tsx` that imports static HTML or renders component
- **Rails**: routes + controller actions rendering templates

```bash
node scripts/build_route_map.js --input routes.json --output route_map.json --strategy static
```

## Rollback
- Remove generated route stubs and restore prior routing.
