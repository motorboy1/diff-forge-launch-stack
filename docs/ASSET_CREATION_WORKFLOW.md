# DiffForge Asset Creation Workflow

> Version: 1.0
> Last Updated: 2026-02-20
> Owner: DiffForge Asset Operations Team

---

## Overview

Every DiffForge asset follows a rigorous creation and validation pipeline before it reaches customers. This document defines the roles, processes, quality gates, and versioning policies that govern asset production.

Two primary agents drive the workflow:
- **OMC (Oh My Claude Code)**: Automated multi-agent orchestration for asset generation, linting, and quality checks.
- **Manus**: Human-in-the-loop agent responsible for strategic review, brand alignment, and final approval.

---

## Agent Roles & Responsibilities

### OMC (Oh My Claude Code) -- Automated Asset Engine

OMC is the multi-agent orchestration system that handles the bulk of asset generation. It operates in a parallelized pipeline with built-in quality checkpoints.

#### Core Capabilities

| Capability | Description |
|------------|-------------|
| Multi-Agent Orchestration | Coordinates multiple specialized sub-agents (patch generator, linter, metadata builder, documentation writer) working in parallel |
| Parallel Asset Builds | Can generate up to 5 assets simultaneously across independent workstreams |
| Quality Checks | Automated validation of all 12 quality checklist items (see below) |
| Patch Generation | Creates `changes.patch` files from source analysis, ensuring clean diffs with proper context lines |
| Metadata Construction | Generates `META.json` with all required fields, auto-populating where deterministic |
| Documentation Drafting | Produces initial drafts of `APPLY.md`, `SOURCE_RUN.md`, and `RISK_GUIDE.md` |
| Regression Detection | Compares new asset versions against previous versions to detect unintended changes |

#### OMC Pipeline Stages

```
[1] Source Analysis
     Analyze target codebase, identify modification points
         |
[2] Patch Generation (parallelizable)
     Generate changes.patch for each asset
         |
[3] Metadata Construction (parallelizable)
     Build META.json with all required fields
         |
[4] Documentation Drafting (parallelizable)
     Draft APPLY.md, SOURCE_RUN.md, RISK_GUIDE.md
         |
[5] Self-Validation
     Run automated quality checklist (12 items)
         |
[6] Handoff to Manus
     Package asset for human review
```

#### Parallel Build Strategy

OMC can process multiple assets in parallel when they target different codebases or non-overlapping sections of the same codebase.

```
Workstream A: [Asset 01] --> [Asset 02] --> [Asset 03]
Workstream B: [Asset 04] --> [Asset 05]    (parallel)
Workstream C: [Asset 06] --> [Asset 07]    (parallel)
```

Constraints on parallelism:
- Assets modifying the same files must be serialized.
- Maximum 5 parallel workstreams to prevent resource contention.
- Each workstream has its own isolated working directory.

---

### Manus -- Human-in-the-Loop Agent

Manus represents the human decision-maker in the pipeline. Manus does not generate assets but provides the strategic layer that automated systems cannot replicate.

#### Core Responsibilities

| Responsibility | Description |
|----------------|-------------|
| Strategic Decisions | Determines which assets to build, prioritization, and market positioning |
| Brand Voice | Ensures all documentation matches DiffForge's tone: precise, professional, developer-friendly |
| Final Approval | Signs off on every asset before it enters the frozen state |
| Quality Override | Can reject assets that pass automated checks but fail subjective quality standards |
| Risk Assessment | Reviews and adjusts risk ratings based on domain expertise |
| Pricing Decisions | Assigns pricing tier for each asset based on complexity and market value |
| Conflict Resolution | Resolves cases where OMC's automated judgment is ambiguous |

#### Manus Review Protocol

1. **Receive Handoff**: OMC delivers packaged asset with automated validation report.
2. **Documentation Review**: Read all 3 documentation files for accuracy, clarity, and brand voice.
3. **Patch Inspection**: Manually inspect `changes.patch` for correctness and elegance.
4. **Metadata Audit**: Verify META.json fields, especially risk, portability, and estimated_apply_time.
5. **Apply Test**: Perform the asset application on a clean test environment following APPLY.md.
6. **Decision**: APPROVE (proceed to freeze), REQUEST_CHANGES (return to OMC with notes), or REJECT (asset scrapped).

---

## Asset Validation Process: 5-Step Pipeline

Every asset must pass through all 5 steps sequentially. No step can be skipped. A failure at any step returns the asset to the appropriate earlier stage.

### Step 1: Generate

**Owner**: OMC
**Duration**: 15-60 minutes per asset

Actions:
- Analyze the source project and identify modification targets.
- Generate `changes.patch` with clean, contextual diffs.
- Build `META.json` with all required fields.
- Draft `APPLY.md` with step-by-step application instructions.
- Draft `SOURCE_RUN.md` documenting the source analysis run.
- Draft `RISK_GUIDE.md` with risk assessment and rollback procedures.

Exit Criteria:
- All 5 files exist in the asset folder.
- `changes.patch` is non-empty and syntactically valid.
- `META.json` parses as valid JSON.

Failure Action: Re-run generation with adjusted parameters.

---

### Step 2: Lint

**Owner**: OMC (automated)
**Duration**: < 2 minutes per asset

Checks:
- `changes.patch`: Valid unified diff format, proper headers, context lines present.
- `META.json`: Valid JSON, schema-compliant, all required fields present.
- `APPLY.md`: Markdown well-formed, contains required sections (Prerequisites, Steps, Verification).
- `SOURCE_RUN.md`: Contains run ID, timestamp, source URL, extraction parameters.
- `RISK_GUIDE.md`: Contains risk level, impact assessment, rollback instructions.

Exit Criteria:
- Zero lint errors across all 5 files.

Failure Action: Auto-fix where possible (formatting, whitespace). Return to Generate for structural issues.

---

### Step 3: Gate Check

**Owner**: OMC (automated)
**Duration**: < 5 minutes per asset

This is the comprehensive automated quality gate. All 12 items from the Quality Checklist (see below) must pass.

Gate Check Execution:
```
for each item in QUALITY_CHECKLIST:
    result = evaluate(item, asset)
    if result == FAIL:
        record_failure(item, reason)

if any failures:
    return GATE_FAIL with failure report
else:
    set META.json gate_pass = true
    set META.json gate_condition = "All 12 quality checks passed"
    return GATE_PASS
```

Exit Criteria:
- `gate_pass: true` in META.json.
- All 12 quality checklist items verified.

Failure Action: Return to Generate with specific failure report. OMC attempts auto-remediation for up to 2 retries before escalating to Manus.

---

### Step 4: Peer Review

**Owner**: Manus (human)
**Duration**: 10-30 minutes per asset

This is the human review step. Even if all automated checks pass, Manus applies subjective quality standards.

Review Areas:
- **Correctness**: Does the patch actually achieve what it claims?
- **Elegance**: Is the diff minimal and clean, or does it include unnecessary changes?
- **Documentation Quality**: Are instructions clear enough for a developer to follow without confusion?
- **Risk Accuracy**: Is the stated risk level appropriate given the patch scope?
- **Market Fit**: Would a developer pay for this asset? Does it save meaningful time?
- **Brand Voice**: Does the documentation match DiffForge's professional, precise tone?

Review Outcomes:
| Outcome | Action |
|---------|--------|
| APPROVE | Proceed to Freeze |
| REQUEST_CHANGES | Return to OMC with specific change requests (max 3 rounds) |
| REJECT | Asset scrapped; document reason in rejection log |

Exit Criteria:
- Manus explicitly approves with sign-off timestamp.

---

### Step 5: Freeze

**Owner**: OMC (automated, triggered by Manus approval)
**Duration**: < 1 minute

Actions:
- Lock all 5 files to read-only state.
- Generate SHA-256 checksums for each file.
- Record freeze timestamp and approver in META.json.
- Assign final asset version number.
- Add asset to the global asset registry.
- Generate customer-facing asset listing data.

Exit Criteria:
- Asset is immutable.
- Checksums recorded.
- Asset appears in registry.

Post-Freeze Modifications:
- Any changes after freeze require a new version (see Version Upgrade Policy below).
- The frozen version is never modified; a new version folder is created instead.

---

## Validation Pipeline Diagram

```
+----------+    +------+    +------------+    +-------------+    +--------+
| Generate |--->| Lint |--->| Gate Check |--->| Peer Review |--->| Freeze |
|  (OMC)   |    |(OMC) |    |   (OMC)    |    |  (Manus)    |    | (OMC)  |
+----------+    +------+    +------------+    +-------------+    +--------+
     ^              |             |                  |
     |              v             v                  v
     +---- FAIL ----+      FAIL (auto-fix     REQUEST_CHANGES
                           or escalate)       (max 3 rounds)
```

---

## Quality Checklist (12 Items)

Every asset must satisfy all 12 items before passing the Gate Check (Step 3). These are evaluated automatically by OMC.

| # | Check | Field / File | Criteria | Severity |
|---|-------|-------------|----------|----------|
| 1 | Non-empty patch | `changes.patch` | File exists and contains > 10 lines | CRITICAL |
| 2 | Valid JSON | `META.json` | Parses without error, conforms to schema | CRITICAL |
| 3 | Risk defined | `META.json -> risk` | Value is one of: `"low"`, `"medium"`, `"high"` | CRITICAL |
| 4 | Portability defined | `META.json -> portability` | Value is one of: `"low"`, `"medium"`, `"high"` | CRITICAL |
| 5 | Evidence present | `META.json -> source_run_id` | Array with at least one non-empty string entry | HIGH |
| 6 | Compatible stack listed | `META.json -> compatible_stack` | Non-empty array of stack identifiers (e.g., `["rails-8", "nextjs-14"]`) | HIGH |
| 7 | Apply instructions complete | `APPLY.md` | Contains sections: Prerequisites, Steps, Verification, Troubleshooting | HIGH |
| 8 | Rollback documented | `RISK_GUIDE.md` | Contains explicit rollback instructions with step-by-step commands | HIGH |
| 9 | Source run documented | `SOURCE_RUN.md` | Contains run ID, timestamp, source URL, extraction method | MEDIUM |
| 10 | Gate condition specified | `META.json -> gate_condition` | Non-empty string describing the passing condition | MEDIUM |
| 11 | Estimated time realistic | `META.json -> estimated_apply_time` | Value is a string in format `"Xm"` or `"Xh Ym"` where X,Y are positive integers; value is between 5m and 4h | MEDIUM |
| 12 | Unique asset ID | `META.json -> asset_id` | Matches the folder name exactly; unique across all assets in registry | CRITICAL |

### Severity Levels

| Severity | Meaning | On Failure |
|----------|---------|------------|
| CRITICAL | Asset cannot ship without this | Blocks Gate Check immediately |
| HIGH | Significant quality gap | Blocks Gate Check; auto-remediation attempted first |
| MEDIUM | Minor quality gap | Warning issued; Manus decides in Peer Review |

---

## Detailed META.json Schema

```json
{
  "asset_id": "string (must match folder name)",
  "version": "string (semver, e.g., '1.0.0')",
  "title": "string (human-readable asset name)",
  "description": "string (1-3 sentence summary)",
  "risk": "string (low|medium|high)",
  "portability": "string (low|medium|high)",
  "compatible_stack": ["string (stack identifiers)"],
  "estimated_apply_time": "string (e.g., '15m', '1h 30m')",
  "gate_pass": "boolean",
  "gate_condition": "string (description of passing criteria)",
  "source_run_id": ["string (run identifiers)"],
  "created_at": "string (ISO 8601 timestamp)",
  "frozen_at": "string (ISO 8601 timestamp, set at freeze)",
  "approved_by": "string (Manus sign-off identifier)",
  "checksums": {
    "changes.patch": "string (SHA-256)",
    "APPLY.md": "string (SHA-256)",
    "META.json": "string (SHA-256, self-referencing, computed last)",
    "SOURCE_RUN.md": "string (SHA-256)",
    "RISK_GUIDE.md": "string (SHA-256)"
  },
  "tags": ["string (categorization tags)"],
  "pricing_tier": "string (free|starter|pro|enterprise)",
  "changelog": ["string (version change descriptions)"]
}
```

---

## Version Upgrade Policy

DiffForge uses strict semantic versioning (semver) for all assets.

### Version Format

```
MAJOR.MINOR.PATCH
  v1.0.0  ->  Initial release
  v1.0.1  ->  Patch: typo fix, documentation correction
  v1.1.0  ->  Minor: expanded compatibility, improved patch
  v2.0.0  ->  Major: breaking change, different target structure
```

### When to Increment

| Change Type | Version Bump | Examples |
|------------|-------------|----------|
| Typo in documentation | PATCH (v1.0 -> v1.0.1) | Fix typo in APPLY.md, correct formatting in RISK_GUIDE.md |
| Patch content adjustment (non-breaking) | PATCH (v1.0 -> v1.0.1) | Add missing context lines, fix whitespace in diff |
| New compatible stack added | MINOR (v1.0 -> v1.1) | Add support for Next.js 15 alongside existing Next.js 14 |
| Expanded documentation | MINOR (v1.0 -> v1.1) | Add new troubleshooting section, additional examples |
| Improved patch (same target, better approach) | MINOR (v1.0 -> v1.1) | Refactor patch to be cleaner while achieving same result |
| Different target file structure | MAJOR (v1.0 -> v2.0) | Patch now targets `src/app/` instead of `pages/` |
| Incompatible stack change | MAJOR (v1.0 -> v2.0) | Drop Rails 7 support, require Rails 8 |
| Fundamentally different approach | MAJOR (v1.0 -> v2.0) | Complete rewrite of the patch strategy |

### Upgrade Process

1. **Create new version folder**: `asset-name-v2.0.0/` alongside existing `asset-name-v1.0.0/`.
2. **Copy and modify**: Start from the previous version's files, make changes.
3. **Run full pipeline**: New version goes through all 5 steps (Generate through Freeze).
4. **Update changelog**: Add entry to META.json changelog array.
5. **Backward compatibility notes**: Document in APPLY.md what changed and migration path.
6. **Registry update**: Both versions listed; previous version marked as `superseded_by: "v2.0.0"`.

### Changelog Requirements

Every version bump must include a changelog entry in META.json:

```json
{
  "changelog": [
    "v1.0.0: Initial release",
    "v1.0.1: Fixed typo in APPLY.md step 3",
    "v1.1.0: Added Next.js 15 compatibility, improved rollback instructions",
    "v2.0.0: BREAKING - Migrated to App Router structure, dropped Pages Router support"
  ]
}
```

### Backward Compatibility Notes

For MINOR version bumps:
- Previous version's APPLY.md instructions must still work.
- New features are additive only.
- Document new capabilities in a "What's New in vX.Y" section of APPLY.md.

For MAJOR version bumps:
- Clearly state what is incompatible in APPLY.md under "Breaking Changes."
- Provide migration guide if users are upgrading from a previous major version.
- Previous major version remains available for purchase/download for 6 months.

---

## Asset Lifecycle Summary

```
IDEA -> GENERATE -> LINT -> GATE CHECK -> PEER REVIEW -> FREEZE -> PUBLISH -> [SUPERSEDE]
                                                                                    |
                                                                          New version created
                                                                          Old version archived
```

### Lifecycle States

| State | Description | Mutable? |
|-------|-------------|----------|
| DRAFT | Asset is being generated by OMC | Yes |
| REVIEW | Asset is awaiting Manus review | Yes (by Manus request) |
| FROZEN | Asset is approved and locked | No |
| PUBLISHED | Asset is available to customers | No |
| SUPERSEDED | Newer version exists; still available | No |
| ARCHIVED | Removed from active listing (6+ months after superseded) | No |

---

## Appendix: OMC Agent Configuration

### Sub-Agent Roles

| Sub-Agent | Role | Inputs | Outputs |
|-----------|------|--------|---------|
| Analyzer | Source code analysis, modification point identification | Source repo URL, target description | Analysis report, file map |
| Patcher | Diff generation | Analysis report, target files | `changes.patch` |
| Documenter | Documentation generation | Analysis report, patch file | `APPLY.md`, `SOURCE_RUN.md`, `RISK_GUIDE.md` |
| MetaBuilder | Metadata construction | All generated files, analysis report | `META.json` |
| Validator | Quality checklist evaluation | All 5 asset files | Validation report (12-item pass/fail) |

### Retry Policy

- **Lint failures**: Auto-fix attempted, up to 3 retries.
- **Gate Check failures**: Auto-remediation attempted for HIGH/MEDIUM items, up to 2 retries. CRITICAL failures escalate to Manus immediately.
- **Peer Review REQUEST_CHANGES**: Up to 3 rounds of revision before Manus must APPROVE or REJECT.
- **Total pipeline timeout**: 4 hours per asset. If exceeded, asset is flagged for manual intervention.
