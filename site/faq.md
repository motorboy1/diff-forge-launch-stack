# Frequently Asked Questions

---

### General

**1. What is a verified change asset?**
A verified change asset is a code patch (`changes.patch`) that has been produced by a documented AI Run, passed a quality Gate, and been Frozen into an immutable snapshot. Unlike raw diffs or copy-pasted code, each asset carries provenance, verification proof, and risk documentation.

**2. How is DiffForge different from just using Git?**
Git stores diffs — what changed between two commits. DiffForge stores *verified* change assets — diffs that carry metadata about how they were produced, whether they passed quality checks, and what risks they introduce. Git is the storage layer; DiffForge is the verification and distribution layer.

**3. How is DiffForge different from Entire?**
Entire captures the full context of an AI coding session — prompts, logs, model responses. DiffForge complements this by verifying the *output* of those sessions and packaging it as distributable, immutable assets with risk scoring.

**4. What does Run/Gate/Freeze mean?**
It's our three-stage governance model. **Run** = documented AI execution. **Gate** = quality/security verification. **Freeze** = immutable snapshot with checksum. Every asset goes through all three stages.

**5. What's in each asset?**
Five files: `changes.patch` (the actual code), `META.json` (machine-readable metadata), `APPLY.md` (application guide), `SOURCE_RUN.md` (run documentation), `RISK_GUIDE.md` (risk assessment).

---

### Assets & Application

**6. What tech stacks are supported?**
Our current assets target Rails 7+, Node.js 18+, and Django 4+. Each asset's `META.json` lists its compatible stacks. The patterns are designed to be portable — adaptation guides are included.

**7. Can I apply an asset to a framework not listed?**
Yes. The `APPLY.md` includes the core logic and pattern. You may need to adapt syntax and framework conventions, but the underlying approach is documented clearly enough to port.

**8. What if an asset doesn't apply cleanly?**
Patches are designed for common project structures. If `git apply` fails due to path differences, use `git apply --3way` or manually apply following the `APPLY.md` guide. The guide includes all code in readable form.

**9. Are assets tested?**
Each asset's `SOURCE_RUN.md` documents the gate checks it passed. These include syntax validation, security scanning, and behavioral verification. We document the evidence — not just the claim.

**10. How do I roll back an applied asset?**
Every `APPLY.md` includes a Rollback section with specific commands to reverse the change.

---

### Pricing & Licensing

**11. What does ₩49,000 get me?**
The Starter Pack: 4 AUTH domain assets with full documentation. One-time purchase, permanent access.

**12. What does the Pro Bundle include?**
All 15 assets across 4 domains (AUTH, GOVERNANCE, OPS, SECURITY). One-time purchase at ₩149,000.

**13. Is the Asset Club subscription worth it?**
If you're shipping AI-generated code regularly, yes. You get 2-4 new assets monthly, version upgrades, early access, and archive access for ₩29,000/month. Cancel anytime.

**14. Can I share purchased assets with my team?**
Assets are licensed per organization. One purchase covers your entire team. Redistribution outside your organization is not permitted.

**15. Do you offer enterprise pricing?**
Contact us for custom enterprise packages including priority support, custom asset development, and volume licensing.

---

### Security & Trust

**16. How do I verify an asset hasn't been tampered with?**
Frozen assets include SHA-256 checksums in their metadata. Verify the checksum against the published hash to confirm integrity.

**17. Who reviews the assets?**
Assets are produced by AI (Claude Opus) and verified through automated gate checks plus human review. The full provenance chain is documented in `SOURCE_RUN.md`.

**18. What if I find a vulnerability in an asset?**
Report it immediately. We will issue a patched version (v1.1) and notify all purchasers. Security issues are treated as P0.

**19. Is my payment information secure?**
We use industry-standard payment processing. We do not store credit card information on our servers.
