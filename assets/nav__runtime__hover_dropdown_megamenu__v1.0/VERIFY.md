# VERIFY — nav__runtime__hover_dropdown_megamenu__v1.0

## Pass/Fail Rules
PASS if all scenarios succeed with **0 console errors** and **no broken layout** for the nav region.

## Scenarios (Desktop)
1) Hover a top-level item with submenu → submenu opens within 200ms.
2) Move mouse away from nav and submenu → submenu closes within 300ms.
3) Click top-level toggle → submenu toggles open/close.
4) Press `Esc` while submenu open → submenu closes and focus returns to toggle.
5) Click outside nav while open → closes.

## Scenarios (Keyboard)
6) Tab to toggle → `Enter` opens submenu, `Esc` closes.
7) ARIA: `aria-expanded` reflects open state (`true/false`).

## Scenarios (Mobile emulation)
8) Tap toggle → opens submenu (no hover dependency).
9) Tap outside → closes submenu.
