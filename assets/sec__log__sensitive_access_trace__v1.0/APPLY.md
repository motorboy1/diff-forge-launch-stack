# APPLY — sec__log__sensitive_access_trace__v1.0

## Prerequisites
- Rails 7+ with ActiveRecord and ActiveSupport::CurrentAttributes
- Logger configured (stdout or file)

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Include concern in models with sensitive data:**
   ```ruby
   class User < ApplicationRecord
     include SensitiveAccessTracer
   end
   ```

3. **Set Current attributes in ApplicationController:**
   ```ruby
   before_action :set_request_context
   def set_request_context
     Current.user = current_user
     Current.ip_address = request.remote_ip
     Current.request_id = request.request_id
     Current.user_agent = request.user_agent
   end
   ```

4. **(Optional) Create SensitiveAccessLog model for persistent storage:**
   ```bash
   rails g model SensitiveAccessLog field:string record_type:string record_id:integer accessed_by:integer value_preview:string request_id:string ip_address:string user_agent:string timestamp:datetime
   rails db:migrate
   ```

## Verification

1. Access a user's email in console: `User.first.email` — check logs for JSON trace entry
2. Verify value is masked: should show `jo***@example.com`, not full email
3. Check that request context (IP, user agent) is captured
4. Access SSN field — should log with `***-**-1234` masking

## Rollback

Remove `include SensitiveAccessTracer` from models. Delete concern file. Revert Current.rb changes.
