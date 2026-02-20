# RISK GUIDE — auth__audit_log__role_change_tracking__v1.0

## Risk Level: LOW

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Audit table grows large over time | Low | High |
| IP address logging may have GDPR implications | Medium | Medium |
| Missing Current.user causes nil actor on background jobs | Low | Medium |

## Mitigation Strategies

1. **Add table partitioning or archival policy** for audit logs older than 1 year
2. **Anonymize IP addresses** if operating under GDPR — store hashed or truncated
3. **Set a system user** for background job role changes where Current.user is nil
4. **Add index on `changed_at`** for efficient time-range queries (included in migration)

## Compatibility Notes

- Pure ActiveRecord — no external gems required
- Portable to any ORM with callbacks (Sequelize, Django signals)
- `Current` attributes are Rails 5.2+ feature; backport via thread-local for older versions
