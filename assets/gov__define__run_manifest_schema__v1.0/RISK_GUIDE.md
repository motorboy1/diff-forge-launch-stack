# RISK GUIDE — gov__define__run_manifest_schema__v1.0

## Risk Level: LOW

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Schema too strict rejects valid manifests | Medium | Low |
| Schema too loose allows invalid manifests | Low | Low |
| Dependency on json_schemer gem | Low | Low |

## Mitigation Strategies

1. **Test with diverse sample manifests** before enforcing in production
2. **Use schema versioning** — include `$id` with version for future upgrades
3. **Allow additional properties** for forward compatibility

## Compatibility Notes

- JSON Schema is language-agnostic — validate in any language with a JSON Schema library
- Ruby: `json_schemer` gem. Node.js: `ajv`. Python: `jsonschema`.
