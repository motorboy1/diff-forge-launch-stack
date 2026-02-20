# APPLY — gov__enforce__gate_pass_rule__v1.0

## Prerequisites
- Ruby 3.0+ with JSON standard library
- Asset directories following DiffForge structure

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Run gate enforcement on an asset:**
   ```ruby
   enforcer = GateEnforcer.new("assets/auth__policy_gate__student_approval__v1.0")
   result = enforcer.enforce!
   puts result[:summary]
   ```

3. **Integrate into publish pipeline:**
   ```ruby
   Dir.glob("assets/*").each do |asset_dir|
     result = GateEnforcer.new(asset_dir).enforce!
     puts "#{File.basename(asset_dir)}: #{result[:summary]}"
   end
   ```

## Verification

1. Run against a complete asset — should return GATE PASS
2. Remove a required file — should return GATE FAIL
3. Empty the patch file — should fail patch_content check

## Rollback

Delete `lib/gate_enforcer.rb`. Remove any pipeline integration code.
