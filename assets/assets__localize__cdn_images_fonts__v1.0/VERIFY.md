# VERIFY — assets__localize__cdn_images_fonts__v1.0

PASS if:
- Grep/check finds **0** unintended external URLs:
  - `http://` / `https://` in HTML/CSS except allowlist
- Browser loads with "offline" mode and still renders:
  - images visible (no broken icons)
  - fonts applied (no fallback if you require)
- No 404 for `/_assets/*`
