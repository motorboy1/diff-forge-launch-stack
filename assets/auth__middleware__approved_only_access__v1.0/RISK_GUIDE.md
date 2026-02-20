# RISK GUIDE — auth__middleware__approved_only_access__v1.0

## Risk Level: MEDIUM

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Legitimate users blocked if approval check has a bug | High | Low |
| API clients break if not expecting 403 JSON format | Medium | Medium |
| Performance overhead on every protected request | Low | Low |

## Mitigation Strategies

1. **Add comprehensive integration tests** before deploying
2. **Implement a kill switch** — environment variable to disable middleware in emergencies
3. **Log all 403 responses** for monitoring false rejections
4. **Gradual rollout** — start with one protected path, expand after validation

## Compatibility Notes

- Requires Warden middleware (ships with Devise)
- For non-Warden setups, modify `extract_user` to match your auth strategy
- Portable to Express.js (rewrite as middleware function) or Django (rewrite as middleware class)
