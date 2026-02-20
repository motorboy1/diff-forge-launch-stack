# The DiffForge Manifesto

## Why the Industry Needs Verified Change Assets

---

### The Unverified Code Crisis

Every day, millions of lines of AI-generated code enter production codebases worldwide. Developers prompt, copy, paste, commit, and push. The speed is exhilarating. The risk is invisible.

No one asks: **Who verified this change?**

Not the model that generated it — it has no concept of "correctness" beyond token probability. Not the developer who applied it — they trusted the AI. Not the CI pipeline — it checks syntax, not provenance.

The result: an industry running on unverified change.

---

### What We Believe

**1. Every change should have provenance.**
A patch without a source Run ID is a patch without identity. We document exactly which model, which prompt, which context, and which timestamp produced each change.

**2. Every change should pass a gate.**
Quality is not optional. Before any DiffForge asset is published, it passes validation: syntax checks, security scans, risk scoring, and evidence capture. No gate pass, no publish.

**3. Every verified change should be immutable.**
Once an asset passes its gate and is approved, it is frozen. SHA-256 checksummed. No modifications. No tampering. What you download is what was verified.

**4. Risk should be explicit, not discovered.**
Every DiffForge asset carries a risk score: low, medium, or high. Plus a detailed risk guide documenting potential impacts, mitigation strategies, and compatibility notes. Know the blast radius before you apply.

**5. Portability matters.**
A good change pattern is not locked to one framework. Every asset documents compatible stacks and provides guidance for adaptation. A well-designed diff transcends its origin language.

---

### The Run/Gate/Freeze Model

This is not a slogan. It is an engineering protocol.

- **Run**: The documented execution that produces a change artifact. Every Run has an ID, a timestamp, a prompt, a model, and measured output.
- **Gate**: The quality barrier between production and unverified code. Gates check syntax, security, risk, and evidence. Assets that fail are rejected.
- **Freeze**: The immutability guarantee. Frozen assets cannot be modified. Their checksums are permanent. Trust is preserved.

---

### What DiffForge Is Not

We do not replace Git. Git is infrastructure. We build on it.
We do not replace Entire. Entire captures session context. We complement it.
We do not generate code. We verify, score, document, and distribute verified change assets.

---

### The Standard We Set

Every DiffForge asset ships with five artifacts:
1. `changes.patch` — The actual code change
2. `META.json` — Machine-readable metadata with risk, portability, run IDs, and gate results
3. `APPLY.md` — Human-readable application guide with rollback instructions
4. `SOURCE_RUN.md` — Full documentation of the Run that produced this asset
5. `RISK_GUIDE.md` — Detailed risk assessment with mitigation strategies

This is the minimum. Not the maximum.

---

*DiffForge. Verified change assets. Because `git diff` alone isn't enough.*
