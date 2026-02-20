# APPLY — ops__clear__asset_cache_rebuild__v1.0

## Prerequisites
- Rails 7+ with Sprockets or Propshaft asset pipeline
- Write access to `tmp/cache` and `public/assets`

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Run cache rebuild:**
   ```bash
   rails assets:cache:rebuild
   ```

3. **Verify cache integrity:**
   ```bash
   rails assets:cache:verify
   ```

## Verification

1. Manifest file exists in `public/assets/`
2. All asset fingerprints resolve correctly
3. Page load in browser shows no 404s for CSS/JS assets

## Rollback

Cache rebuild is non-destructive. If issues arise, simply re-run:
```bash
rails assets:clobber && rails assets:precompile
```
