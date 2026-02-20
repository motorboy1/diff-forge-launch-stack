# APPLY — auth__rate_limit__login_protection__v1.0

## Prerequisites
- Rails 7+ with Rack middleware stack
- Cache store configured (Redis recommended, memcached or file store acceptable)

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Add middleware to application config:**
   ```ruby
   # config/application.rb
   config.middleware.insert_before Rack::Head, LoginRateLimiter,
     max_attempts: 5,
     window: 300,
     store: Rails.cache
   ```

3. **Ensure cache store is configured:**
   ```ruby
   # config/environments/production.rb
   config.cache_store = :redis_cache_store, { url: ENV["REDIS_URL"] }
   ```

4. **Restart the application**

## Verification

1. Attempt 5 failed logins rapidly — all should return normal error responses
2. Attempt 6th login — should return 429 with JSON body and `Retry-After` header
3. Wait 5 minutes or clear cache — next login attempt should work
4. Successful login should reset the counter

## Rollback

Remove middleware line from `config/application.rb` and delete `app/middleware/login_rate_limiter.rb`.
