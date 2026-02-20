# RISK GUIDE — gov__classify__risk_scoring_matrix__v1.0

## Risk Level: LOW

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Incorrect domain weights miscategorize assets | Medium | Low |
| Binary risk input feeds back into circular scoring | Low | Low |
| Missing domains default to weight 2 | Low | Medium |

## Mitigation Strategies

1. **Calibrate weights** against manual risk assessments periodically
2. **Add domain weights** for new domains as they're introduced
3. **Log score breakdown** for transparency and audit
4. **Allow manual override** for edge cases that matrix misclassifies

## Compatibility Notes

- Pure Ruby — no external dependencies
- Score matrix is a configuration concern — easily ported to JSON config file
- For teams: consider storing weights in a database for dynamic adjustment
