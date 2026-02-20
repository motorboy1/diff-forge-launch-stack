# RISK GUIDE — sec__render__controller_protected_html__v1.0

## Risk Level: HIGH

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Overly strict CSP blocks legitimate inline scripts/styles | High | Medium |
| CSRF enforcement breaks API endpoints that use token auth | High | Medium |
| Template guard blocks legitimate static file serving | Medium | Low |

## Mitigation Strategies

1. **Whitelist API paths** from CSRF enforcement if using token-based auth
2. **Tune CSP gradually** — start with report-only mode before enforcing
3. **Test all page types** (forms, AJAX, file uploads) before deploying
4. **Exclude static asset paths** (`.css`, `.js`, `.png`) from template guard

## Compatibility Notes

- CSRF enforcement assumes Rails `form_authenticity_token` — adapt for custom auth
- CSP may need adjustment for pages with inline scripts or external CDN resources
- Template guard is Rack middleware — works with any Rack-compatible framework
