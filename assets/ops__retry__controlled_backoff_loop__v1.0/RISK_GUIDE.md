# RISK GUIDE — ops__retry__controlled_backoff_loop__v1.0

## Risk Level: LOW

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Retry storms if multiple instances retry simultaneously | Medium | Low |
| Circuit breaker too sensitive — blocks valid calls | Medium | Low |
| Sleep calls block thread in synchronous contexts | Low | Medium |

## Mitigation Strategies

1. **Jitter is included** to prevent thundering herd
2. **Tune circuit threshold** based on actual failure rates
3. **Use async/threaded execution** for non-blocking retries in high-throughput systems
4. **Add dead letter queue** for permanently failed operations

## Compatibility Notes

- Framework-agnostic Ruby — replace `Rails.logger` with any logger
- Node.js equivalent: use `p-retry` or `cockatiel` packages
- Django equivalent: use `tenacity` Python library
- Thread-safe for single-instance use; for shared state, use Redis-backed circuit breaker
