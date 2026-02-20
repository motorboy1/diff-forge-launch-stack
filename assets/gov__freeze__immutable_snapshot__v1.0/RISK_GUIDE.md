# RISK GUIDE — gov__freeze__immutable_snapshot__v1.0

## Risk Level: MEDIUM

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| File permissions prevent legitimate updates | Medium | Medium |
| Manifest file could be deleted, breaking integrity checks | Medium | Low |
| chmod not available in all environments (containers) | Low | Medium |

## Mitigation Strategies

1. **Use an unfreeze command** for authorized updates (requires new Run and Gate)
2. **Store manifest checksums externally** (database or API) as backup
3. **For containerized environments**, use filesystem-level immutability instead of chmod
4. **Version freeze manifests** — never overwrite, create new version

## Compatibility Notes

- Uses Ruby stdlib only — no external dependencies
- File permissions approach works on Linux/macOS; Windows requires different approach
- For Node.js: use `fs.chmod` and `crypto.createHash`
