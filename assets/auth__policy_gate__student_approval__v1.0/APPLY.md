# APPLY — auth__policy_gate__student_approval__v1.0

## Prerequisites
- Rails 7+ application with Devise or similar authentication
- User model with `role` and `approved` columns
- Existing controller structure with `current_user` helper

## Apply Steps

1. **Add approval column to users table:**
   ```bash
   rails generate migration AddApprovedToUsers approved:boolean pending_approval:boolean
   rails db:migrate
   ```

2. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

3. **Include concern in target controllers:**
   ```ruby
   class PremiumResourcesController < ApplicationController
     include StudentGated

     private
     def student_resource?
       true
     end
   end
   ```

4. **Add approval route:**
   ```ruby
   get '/approval-pending', to: 'static#approval_pending', as: :approval_pending
   ```

## Verification

1. Log in as unapproved student — should redirect to approval pending page
2. Log in as approved student — should access premium resources
3. Log in as admin — should bypass gate entirely
4. Check that public resources remain accessible to all users

## Rollback

```bash
git revert HEAD
rails generate migration RemoveApprovedFromUsers approved:boolean pending_approval:boolean
rails db:migrate
```
