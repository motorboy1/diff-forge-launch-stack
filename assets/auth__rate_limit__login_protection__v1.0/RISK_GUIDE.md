# RISK GUIDE — auth__rate_limit__login_protection__v1.0

## Risk Level: LOW

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Shared IP (NAT/VPN) blocks multiple legitimate users | Medium | Medium |
| Cache store failure disables rate limiting silently | Low | Low |
| Distributed attacks bypass per-IP limiting | Medium | Low |

## Mitigation Strategies

1. **Add user-identifier-based limiting** in addition to IP for logged-in users
2. **Monitor cache store health** — add fallback to in-memory store
3. **Implement CAPTCHA** after 3 attempts as a softer alternative before hard block
4. **Whitelist known office IPs** if NAT is a concern

## Compatibility Notes

- Requires `Rails.cache` or any store responding to `read`, `increment`, `delete`
- For Node.js: use `express-rate-limit` with Redis store (same concept)
- For Django: use `django-ratelimit` with cache backend
- IP extraction relies on `Rack::Request#ip` — works behind reverse proxy with X-Forwarded-For
