# APPLY — assets__localize__cdn_images_fonts__v1.0

## Goal
Make cloned site self-contained.

## Apply Steps (recommended)

1) Choose local asset root:
- `public/_assets/` (static hosting) or `site/_assets/`

2) Run an asset localizer script (Node or Python) to:
- scan HTML for `<img src>`, `<source srcset>`, `<link rel=preload>`, `<script src>`
- scan CSS for `url(...)` (background images, fonts)
- download assets
- rewrite URLs to `/_assets/...`

```bash
mkdir -p public/_assets
python3 scripts/localize_assets.py --input site/ --output public/_assets/
```

3) Verify render:
- load site with network offline mode and check visual integrity

## Rollback
- Restore original HTML/CSS (`git checkout`) and delete local assets folder.
