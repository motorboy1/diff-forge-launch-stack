# APPLY — ops__detect__env_mismatch_guard__v1.0

## Prerequisites
- Rails 7+ or any Ruby application
- `.ruby-version` and optionally `.node-version` files present

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Add to deploy pipeline:**
   ```ruby
   # In your deploy script or Capistrano task
   require_relative "lib/env_mismatch_guard"
   EnvMismatchGuard.new.check!
   ```

3. **Or add as initializer:**
   ```ruby
   # config/initializers/env_guard.rb
   EnvMismatchGuard.new.check! if Rails.env.production?
   ```

## Verification

1. Remove a required env var temporarily — guard should raise error
2. Change `.ruby-version` to a wrong version — guard should report mismatch
3. Restore correct values — guard should pass silently

## Rollback

Remove the initializer or deploy hook line. Delete `lib/env_mismatch_guard.rb`.
