# RISK GUIDE — auth__policy_gate__student_approval__v1.0

## Risk Level: MEDIUM

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Legitimate students locked out if approval workflow breaks | High | Low |
| Admin bypass could be exploited if role assignment is weak | Medium | Low |
| Scope filtering may hide resources unintentionally | Medium | Medium |

## Mitigation Strategies

1. **Test approval workflow end-to-end** before deploying to production
2. **Add admin notification** when students request approval to avoid bottlenecks
3. **Implement timeout** — auto-approve after 48 hours if no admin action
4. **Audit log** all approval/rejection decisions

## Compatibility Notes

- Requires `current_user` helper (Devise, Authlogic, or custom)
- Policy class pattern is framework-agnostic — portable to Node.js/Django with minimal changes
- Scope class follows Pundit conventions but does not require Pundit gem
