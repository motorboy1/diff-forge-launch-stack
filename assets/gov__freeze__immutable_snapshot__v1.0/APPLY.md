# APPLY — gov__freeze__immutable_snapshot__v1.0

## Prerequisites
- Ruby 3.0+ with `digest` and `json` standard libraries

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Freeze an asset:**
   ```ruby
   freezer = AssetFreezer.new("assets/auth__policy_gate__student_approval__v1.0")
   freezer.freeze!
   ```

3. **Verify integrity later:**
   ```ruby
   result = freezer.verify_integrity
   puts result[:valid] ? "Integrity OK" : result[:error]
   ```

## Verification

1. Freeze an asset — should create `.freeze_manifest.json` and set files to read-only
2. Attempt to modify a frozen file — should fail due to file permissions
3. Verify integrity — should return `valid: true`
4. Manually alter a file (chmod first), re-verify — should return `valid: false`

## Rollback

```bash
chmod 644 assets/<asset_id>/*
rm assets/<asset_id>/.freeze_manifest.json
```
