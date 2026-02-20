# APPLY — sec__render__controller_protected_html__v1.0

## Prerequisites
- Rails 7+ with ActionController
- Existing authentication system for CSRF

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Include concern in sensitive controllers:**
   ```ruby
   class AdminController < ApplicationController
     include ProtectedRendering
   end
   ```

3. **Add middleware to application config:**
   ```ruby
   config.middleware.insert_before ActionDispatch::Static, TemplateAccessGuard
   ```

## Verification

1. Access a protected page via controller route — should render normally with security headers
2. Try accessing a `.erb` or `.html` file directly — should return 403
3. Check response headers — should include `X-Frame-Options: DENY` and `X-Rendered-By: controller`
4. Submit a form without CSRF token — should return 403

## Rollback

Remove `include ProtectedRendering` from controllers. Remove middleware line. Delete both files.
