# RISK GUIDE — sec__log__sensitive_access_trace__v1.0

## Risk Level: MEDIUM

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Performance overhead from logging every field access | Medium | High |
| Log volume explosion in high-traffic applications | Medium | Medium |
| Masked values still potentially re-identifiable | Low | Low |

## Mitigation Strategies

1. **Sample logging** — log only a percentage of accesses in high-traffic environments
2. **Async logging** — use background job for database persistence, keep inline logging minimal
3. **Log rotation** — configure aggressive log rotation for sensitive access logs
4. **Review masking strength** — ensure masked previews can't be reversed or correlated

## Compatibility Notes

- Requires ActiveSupport::CurrentAttributes (Rails 5.2+)
- For non-Rails: replace `Current` with thread-local storage
- For Node.js: use `cls-hooked` or AsyncLocalStorage for request context
- GDPR note: even masked logs should be treated as personal data — configure retention policy
