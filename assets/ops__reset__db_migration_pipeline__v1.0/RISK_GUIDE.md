# RISK GUIDE — ops__reset__db_migration_pipeline__v1.0

## Risk Level: HIGH

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Data loss if backup fails silently | Critical | Low |
| Accidental production execution | Critical | Low |
| Schema drift if migrations are not idempotent | High | Medium |

## Mitigation Strategies

1. **Environment guard is built-in** — raises error in production
2. **Verify backup file size** before proceeding with drop
3. **Run `db:pipeline:verify`** after reset to confirm clean state
4. **Add CI check** that runs reset pipeline on test DB to catch migration issues early

## Compatibility Notes

- PostgreSQL required for `pg_dump` — adapt for MySQL (`mysqldump`) or SQLite (`.dump`)
- Seed data must be idempotent (use `find_or_create_by`)
- Not suitable for databases with large binary data — backup may be slow
