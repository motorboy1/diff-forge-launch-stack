# APPLY — auth__middleware__approved_only_access__v1.0

## Prerequisites
- Rails 7+ with Rack middleware stack
- Warden or compatible authentication middleware
- User model with `approved?` method

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Configure protected paths** in `config/application.rb`:
   ```ruby
   config.middleware.insert_after Warden::Manager, ApprovedOnlyAccess,
     protected_paths: %w[/dashboard /api/v1 /premium],
     bypass_paths: %w[/login /signup /public]
   ```

3. **Restart the application server**

## Verification

1. `curl -I http://localhost:3000/dashboard` without auth — expect 403
2. Log in as unapproved user, access `/dashboard` — expect 403 JSON response
3. Log in as approved user, access `/dashboard` — expect 200 with `X-Approval-Status: approved` header
4. Access `/public` — expect 200 regardless of approval status

## Rollback

Remove the middleware line from `config/application.rb` and delete `app/middleware/approved_only_access.rb`.
