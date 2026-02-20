# APPLY — nav__runtime__hover_dropdown_megamenu__v1.0

## Goal
Restore cloned navigation behavior: hover/focus/click dropdown & mega menu, close behavior, ARIA states.

## Files to add (recommended)
- `site/runtime/nav.runtime.js`
- (optional) `site/runtime/nav.runtime.css`

## Apply Steps

1) Create runtime folder:
```bash
mkdir -p site/runtime
```

2) Add `site/runtime/nav.runtime.js` and include it at the end of `<body>`:
```html
<script src="/runtime/nav.runtime.js" defer></script>
```

3) If your nav needs state class hooks, add optional CSS:
```html
<link rel="stylesheet" href="/runtime/nav.runtime.css">
```

4) Map selectors in the runtime script to your cloned DOM:
- nav root selector (e.g., `[data-nav]` or `nav`)
- toggle elements (e.g., `[data-nav-toggle]`, `.dropdown-toggle`)
- menu panels (e.g., `[data-nav-panel]`, `.dropdown-menu`, `.mega-menu`)

## Rollback
- Remove the script include and delete `site/runtime/nav.runtime.js`
- Remove optional CSS file/include
