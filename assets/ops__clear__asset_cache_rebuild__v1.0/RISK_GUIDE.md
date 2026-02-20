# RISK GUIDE — ops__clear__asset_cache_rebuild__v1.0

## Risk Level: MEDIUM

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Brief period of missing assets during rebuild | Medium | High |
| Old cached assets served if CDN not invalidated | Low | Medium |
| Slow rebuild on large asset pipelines | Low | Low |

## Mitigation Strategies

1. **Run during maintenance window** or low-traffic period
2. **Invalidate CDN cache** after rebuild if using CloudFront/Cloudflare
3. **Use blue-green deployment** to avoid serving stale assets
4. **Pre-warm cache** by hitting critical pages after rebuild

## Compatibility Notes

- Works with Sprockets and Propshaft
- For Webpack/esbuild setups, adapt to clear `public/packs` or `app/assets/builds`
- Node.js equivalent: clear `node_modules/.cache` and rebuild
