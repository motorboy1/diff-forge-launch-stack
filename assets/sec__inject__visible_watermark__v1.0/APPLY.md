# APPLY — sec__inject__visible_watermark__v1.0

## Prerequisites
- Rails 7+ application with HTML views

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Include concern in ApplicationController:**
   ```ruby
   class ApplicationController < ActionController::Base
     include Watermarkable
   end
   ```

3. **Configure watermark (optional):**
   ```bash
   # .env
   WATERMARK_ENABLED=true
   ```

## Verification

1. Load any HTML page — subtle watermark should appear in bottom-right corner
2. Inspect element — watermark div should have `pointer-events: none`
3. Minify CSS — watermark should survive (inline styles)
4. Set `WATERMARK_ENABLED=false` — watermark should disappear

## Rollback

Remove `include Watermarkable` from ApplicationController. Delete `app/controllers/concerns/watermarkable.rb` and `config/initializers/watermark.rb`.
