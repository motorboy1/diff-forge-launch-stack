# RISK GUIDE — sec__inject__visible_watermark__v1.0

## Risk Level: MEDIUM

## Potential Impacts

| Impact | Severity | Likelihood |
|--------|----------|------------|
| Visual disruption on certain layouts | Low | Medium |
| CSS z-index conflicts with modals/overlays | Medium | Low |
| Performance impact from body manipulation on large pages | Low | Low |

## Mitigation Strategies

1. **Test on all page layouts** — especially modals and full-screen views
2. **Adjust z-index** if conflicts with existing UI components
3. **Use conditional rendering** — only enable on specific controllers, not globally
4. **Monitor performance** on pages with large HTML bodies

## Compatibility Notes

- Inline styles ensure watermark survives CSS minification and purging
- `pointer-events: none` ensures watermark doesn't interfere with user interaction
- For SPA frameworks: adapt as a React/Vue component instead of server-side injection
