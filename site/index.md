# DiffForge

## Verified Change Assets for Developers

> Git stores diffs. Entire stores context. **DiffForge stores verified change assets.**

---

## The Problem

AI generates code. Developers apply it. But between generation and deployment, there's no verification layer.

- Git tracks *what* changed — not *why* or *how safely*
- Entire captures context — but doesn't validate the output
- Most AI-generated patches ship without evidence of correctness

**DiffForge bridges this gap.**

---

## How It Works

```
Run → Gate → Freeze → Ship
```

1. **Run** — Every change asset is produced by a documented AI run with full prompt, model, and context metadata.
2. **Gate** — Each asset passes a quality gate: syntax validation, security checks, risk scoring, and evidence capture.
3. **Freeze** — Approved assets are frozen into immutable snapshots with SHA-256 checksums.
4. **Ship** — Verified assets are published with full provenance chain. Apply with confidence.

---

## Asset Domains

| Domain | Description | Assets |
|--------|-------------|--------|
| **AUTH** | Authentication, authorization, access control | 4 |
| **GOVERNANCE** | Run manifests, gate rules, risk scoring | 4 |
| **OPS** | Migrations, caching, environment guards, retry logic | 4 |
| **SECURITY** | Watermarking, rendering protection, access tracing | 3 |

---

## Why DiffForge?

- Every asset has a **source Run ID** — you know exactly how it was made
- Every asset passed a **Gate** — you know it meets quality standards
- Every asset is **Frozen** — you know it hasn't been tampered with
- Every asset includes **risk scoring** — you know what you're getting into

---

## Get Started

- [View Pricing](/pricing) — Starter Pack from ₩49,000
- [Browse Asset Packs](/packs) — 15 verified assets across 4 domains
- [Join Asset Club](/subscription) — ₩29,000/month for continuous delivery

---

*DiffForge — Because `git diff` alone isn't enough.*
