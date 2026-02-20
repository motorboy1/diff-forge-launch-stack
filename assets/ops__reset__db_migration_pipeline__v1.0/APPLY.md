# APPLY — ops__reset__db_migration_pipeline__v1.0

## Prerequisites
- Rails 7+ with PostgreSQL
- `pg_dump` available on system
- Non-production environment only

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Run the reset pipeline:**
   ```bash
   rails db:pipeline:reset
   ```

3. **Verify migrations are clean:**
   ```bash
   rails db:pipeline:verify
   ```

## Verification

1. Check that all tables exist: `rails db:schema:dump`
2. Verify seed data is present: `rails runner "puts User.count"`
3. Confirm no pending migrations: `rails db:pipeline:verify`
4. Compare schema.rb before and after — should be identical

## Rollback

Restore from the backup file created during reset:
```bash
psql your_database < tmp/db_backup_TIMESTAMP.sql
```
