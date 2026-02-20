# About DiffForge

## Mission

DiffForge exists to bring verification, provenance, and trust to AI-generated code changes.

We believe every patch applied to a production system should carry proof of how it was made, what it does, and what risks it introduces.

---

## Why This Matters

The AI coding revolution produces enormous volumes of code. Developers copy-paste from ChatGPT, apply Copilot suggestions, and run Claude Code sessions — all generating diffs that land in production.

But none of these diffs carry:
- **Provenance** — Which model? Which prompt? Which context?
- **Verification** — Did anyone check if this is safe?
- **Risk scoring** — How dangerous is this change?
- **Evidence** — Did it pass any quality gate?

Git records *that* something changed. Entire records *the context* of the session. DiffForge records **verified proof that the change is safe to apply**.

---

## Our Philosophy

### Run/Gate/Freeze

Every DiffForge asset follows a three-stage governance model:

1. **Run** — The AI session that produced the change is documented: prompt, model, timestamp, duration, token usage.
2. **Gate** — The output passes quality checks: syntax validation, security scanning, test coverage, risk scoring.
3. **Freeze** — The verified asset is locked. No further modifications. Immutable. Auditable.

This is not bureaucracy. This is engineering discipline applied to AI-generated code.

---

## What We Are Not

- We are **not replacing Git**. Git is the storage layer. We build on top of it.
- We are **not replacing Entire**. Entire captures session context. We complement it.
- We are **not an AI coding tool**. We are the verification and marketplace layer for AI-generated changes.

---

## Team

DiffForge is built by developers who have shipped AI-generated code to production and learned — sometimes painfully — that verification matters.
