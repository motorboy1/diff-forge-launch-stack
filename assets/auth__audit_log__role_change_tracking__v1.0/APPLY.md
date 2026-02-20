# APPLY — auth__audit_log__role_change_tracking__v1.0

## Prerequisites
- Rails 7+ with ActiveRecord
- User model with a `role` column
- `Current` attributes set up (optional, for actor tracking)

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Run the migration:**
   ```bash
   rails db:migrate
   ```

3. **Include the concern in User model:**
   ```ruby
   class User < ApplicationRecord
     include RoleAuditable
     attr_accessor :role_change_reason
   end
   ```

4. **Set Current attributes** (if not already):
   ```ruby
   class ApplicationController < ActionController::Base
     before_action :set_current_attributes
     def set_current_attributes
       Current.user = current_user
       Current.ip_address = request.remote_ip
     end
   end
   ```

## Verification

1. Change a user's role in console: `user.update(role: "admin", role_change_reason: "Promotion")`
2. Check audit log: `RoleAuditLog.recent` — should show the change
3. Verify all fields populated: actor, target, old_role, new_role, reason, ip_address

## Rollback

```bash
rails db:rollback
git revert HEAD
```
