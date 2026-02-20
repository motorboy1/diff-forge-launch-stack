# APPLY — gov__define__run_manifest_schema__v1.0

## Prerequisites
- Ruby with `json_schemer` gem, or Node.js with `ajv` package
- Project directory with `schemas/` folder

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Install dependencies:**
   ```bash
   bundle add json_schemer
   ```

3. **Use the validator:**
   ```ruby
   validator = RunManifestValidator.new
   result = validator.validate(manifest_data)
   puts result[:valid] ? "Valid" : result[:errors]
   ```

## Verification

1. Validate a correct manifest — should return `valid: true`
2. Remove a required field — should return validation errors
3. Use invalid Run ID format — should fail pattern check

## Rollback

Remove `schemas/run_manifest.schema.json` and `lib/run_manifest_validator.rb`. Remove `json_schemer` from Gemfile.
