# DiffForge Launch Verification Checklist

> Version: 1.0
> Last Updated: 2026-02-20
> Owner: DiffForge QA Lead
>
> **Instructions**: Execute this checklist sequentially before every launch milestone.
> Every item must be checked off. Any unchecked item is a launch blocker.
> Record the verifier's name and timestamp next to each completed item.

---

## Section 1: STRUCTURE VERIFICATION

Verify that the DiffForge launch package has the correct directory structure, all required files exist, and nothing is missing.

### 1.1 Asset Folder Structure

All 15 asset folders must exist under `assets/`. Each folder must contain exactly 5 files.

**Asset Folders:**

- [ ] `assets/asset-01/` exists
- [ ] `assets/asset-02/` exists
- [ ] `assets/asset-03/` exists
- [ ] `assets/asset-04/` exists
- [ ] `assets/asset-05/` exists
- [ ] `assets/asset-06/` exists
- [ ] `assets/asset-07/` exists
- [ ] `assets/asset-08/` exists
- [ ] `assets/asset-09/` exists
- [ ] `assets/asset-10/` exists
- [ ] `assets/asset-11/` exists
- [ ] `assets/asset-12/` exists
- [ ] `assets/asset-13/` exists
- [ ] `assets/asset-14/` exists
- [ ] `assets/asset-15/` exists

**Per-Asset File Check (repeat for each of the 15 asset folders):**

| Asset Folder | changes.patch | APPLY.md | META.json | SOURCE_RUN.md | RISK_GUIDE.md |
|-------------|:---:|:---:|:---:|:---:|:---:|
| asset-01 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-02 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-03 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-04 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-05 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-06 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-07 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-08 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-09 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-10 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-11 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-12 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-13 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-14 | [ ] | [ ] | [ ] | [ ] | [ ] |
| asset-15 | [ ] | [ ] | [ ] | [ ] | [ ] |

**Verification command:**
```bash
# Run from project root to verify all 15 folders and 75 files exist
for i in $(seq -w 1 15); do
  dir="assets/asset-$i"
  if [ ! -d "$dir" ]; then
    echo "MISSING FOLDER: $dir"
  else
    for f in changes.patch APPLY.md META.json SOURCE_RUN.md RISK_GUIDE.md; do
      [ ! -f "$dir/$f" ] && echo "MISSING FILE: $dir/$f"
    done
  fi
done
echo "Structure check complete."
```

### 1.2 Site Pages

All 10 site pages must exist under `site/`.

- [ ] `site/index.md` exists (landing page)
- [ ] `site/pricing.md` exists (pricing tiers and bundles)
- [ ] `site/about.md` exists (about DiffForge)
- [ ] `site/faq.md` exists (frequently asked questions)
- [ ] `site/manifesto.md` exists (vision and value proposition)
- [ ] `site/subscription.md` exists (subscription model details)
- [ ] `site/terms.md` exists (terms of service)
- [ ] `site/privacy.md` exists (privacy policy)
- [ ] `site/copyright.md` exists (copyright and licensing)
- [ ] `site/contact.md` exists (contact and support)

**Verification command:**
```bash
for f in index.md pricing.md about.md faq.md manifesto.md subscription.md terms.md privacy.md copyright.md contact.md; do
  [ ! -f "site/$f" ] && echo "MISSING: site/$f"
done
echo "Site pages check complete."
```

### 1.3 Documentation Files

All 3 documentation files must exist under `docs/`.

- [ ] `docs/LAUNCH_30D_PLAN.md` exists
- [ ] `docs/ASSET_CREATION_WORKFLOW.md` exists
- [ ] `docs/LAUNCH_VERIFICATION_CHECKLIST.md` exists (this file)

**Verification command:**
```bash
for f in LAUNCH_30D_PLAN.md ASSET_CREATION_WORKFLOW.md LAUNCH_VERIFICATION_CHECKLIST.md; do
  [ ! -f "docs/$f" ] && echo "MISSING: docs/$f"
done
echo "Docs check complete."
```

---

## Section 2: ASSET QUALITY VERIFICATION

Verify that every asset meets the quality standards defined in the Asset Creation Workflow. These checks validate the content of asset files, not just their existence.

### 2.1 META.json Field Validation

For each of the 15 assets, verify the following META.json fields:

#### Risk Field
Every META.json must have a `risk` field with value `"low"`, `"medium"`, or `"high"`.

- [ ] asset-01/META.json has valid `risk` field
- [ ] asset-02/META.json has valid `risk` field
- [ ] asset-03/META.json has valid `risk` field
- [ ] asset-04/META.json has valid `risk` field
- [ ] asset-05/META.json has valid `risk` field
- [ ] asset-06/META.json has valid `risk` field
- [ ] asset-07/META.json has valid `risk` field
- [ ] asset-08/META.json has valid `risk` field
- [ ] asset-09/META.json has valid `risk` field
- [ ] asset-10/META.json has valid `risk` field
- [ ] asset-11/META.json has valid `risk` field
- [ ] asset-12/META.json has valid `risk` field
- [ ] asset-13/META.json has valid `risk` field
- [ ] asset-14/META.json has valid `risk` field
- [ ] asset-15/META.json has valid `risk` field

#### Portability Field
Every META.json must have a `portability` field with value `"low"`, `"medium"`, or `"high"`.

- [ ] asset-01/META.json has valid `portability` field
- [ ] asset-02/META.json has valid `portability` field
- [ ] asset-03/META.json has valid `portability` field
- [ ] asset-04/META.json has valid `portability` field
- [ ] asset-05/META.json has valid `portability` field
- [ ] asset-06/META.json has valid `portability` field
- [ ] asset-07/META.json has valid `portability` field
- [ ] asset-08/META.json has valid `portability` field
- [ ] asset-09/META.json has valid `portability` field
- [ ] asset-10/META.json has valid `portability` field
- [ ] asset-11/META.json has valid `portability` field
- [ ] asset-12/META.json has valid `portability` field
- [ ] asset-13/META.json has valid `portability` field
- [ ] asset-14/META.json has valid `portability` field
- [ ] asset-15/META.json has valid `portability` field

#### Patch Non-Emptiness
Every `changes.patch` must be non-empty with more than 10 lines.

- [ ] asset-01/changes.patch has > 10 lines
- [ ] asset-02/changes.patch has > 10 lines
- [ ] asset-03/changes.patch has > 10 lines
- [ ] asset-04/changes.patch has > 10 lines
- [ ] asset-05/changes.patch has > 10 lines
- [ ] asset-06/changes.patch has > 10 lines
- [ ] asset-07/changes.patch has > 10 lines
- [ ] asset-08/changes.patch has > 10 lines
- [ ] asset-09/changes.patch has > 10 lines
- [ ] asset-10/changes.patch has > 10 lines
- [ ] asset-11/changes.patch has > 10 lines
- [ ] asset-12/changes.patch has > 10 lines
- [ ] asset-13/changes.patch has > 10 lines
- [ ] asset-14/changes.patch has > 10 lines
- [ ] asset-15/changes.patch has > 10 lines

#### Gate Pass and Gate Condition
Every META.json must have `gate_pass: true` and a non-empty `gate_condition` string.

- [ ] asset-01/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-02/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-03/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-04/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-05/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-06/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-07/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-08/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-09/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-10/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-11/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-12/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-13/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-14/META.json has `gate_pass: true` and `gate_condition` defined
- [ ] asset-15/META.json has `gate_pass: true` and `gate_condition` defined

#### Source Run ID
Every META.json must have at least one `source_run_id` entry.

- [ ] asset-01/META.json has at least one `source_run_id`
- [ ] asset-02/META.json has at least one `source_run_id`
- [ ] asset-03/META.json has at least one `source_run_id`
- [ ] asset-04/META.json has at least one `source_run_id`
- [ ] asset-05/META.json has at least one `source_run_id`
- [ ] asset-06/META.json has at least one `source_run_id`
- [ ] asset-07/META.json has at least one `source_run_id`
- [ ] asset-08/META.json has at least one `source_run_id`
- [ ] asset-09/META.json has at least one `source_run_id`
- [ ] asset-10/META.json has at least one `source_run_id`
- [ ] asset-11/META.json has at least one `source_run_id`
- [ ] asset-12/META.json has at least one `source_run_id`
- [ ] asset-13/META.json has at least one `source_run_id`
- [ ] asset-14/META.json has at least one `source_run_id`
- [ ] asset-15/META.json has at least one `source_run_id`

#### Asset ID Matching
Every META.json `asset_id` must match the containing folder name exactly.

- [ ] asset-01/META.json `asset_id` == `"asset-01"`
- [ ] asset-02/META.json `asset_id` == `"asset-02"`
- [ ] asset-03/META.json `asset_id` == `"asset-03"`
- [ ] asset-04/META.json `asset_id` == `"asset-04"`
- [ ] asset-05/META.json `asset_id` == `"asset-05"`
- [ ] asset-06/META.json `asset_id` == `"asset-06"`
- [ ] asset-07/META.json `asset_id` == `"asset-07"`
- [ ] asset-08/META.json `asset_id` == `"asset-08"`
- [ ] asset-09/META.json `asset_id` == `"asset-09"`
- [ ] asset-10/META.json `asset_id` == `"asset-10"`
- [ ] asset-11/META.json `asset_id` == `"asset-11"`
- [ ] asset-12/META.json `asset_id` == `"asset-12"`
- [ ] asset-13/META.json `asset_id` == `"asset-13"`
- [ ] asset-14/META.json `asset_id` == `"asset-14"`
- [ ] asset-15/META.json `asset_id` == `"asset-15"`

#### Compatible Stack
Every META.json must have a non-empty `compatible_stack` array.

- [ ] asset-01/META.json has non-empty `compatible_stack`
- [ ] asset-02/META.json has non-empty `compatible_stack`
- [ ] asset-03/META.json has non-empty `compatible_stack`
- [ ] asset-04/META.json has non-empty `compatible_stack`
- [ ] asset-05/META.json has non-empty `compatible_stack`
- [ ] asset-06/META.json has non-empty `compatible_stack`
- [ ] asset-07/META.json has non-empty `compatible_stack`
- [ ] asset-08/META.json has non-empty `compatible_stack`
- [ ] asset-09/META.json has non-empty `compatible_stack`
- [ ] asset-10/META.json has non-empty `compatible_stack`
- [ ] asset-11/META.json has non-empty `compatible_stack`
- [ ] asset-12/META.json has non-empty `compatible_stack`
- [ ] asset-13/META.json has non-empty `compatible_stack`
- [ ] asset-14/META.json has non-empty `compatible_stack`
- [ ] asset-15/META.json has non-empty `compatible_stack`

#### Estimated Apply Time
Every META.json must have a valid `estimated_apply_time` field.

- [ ] asset-01/META.json has valid `estimated_apply_time`
- [ ] asset-02/META.json has valid `estimated_apply_time`
- [ ] asset-03/META.json has valid `estimated_apply_time`
- [ ] asset-04/META.json has valid `estimated_apply_time`
- [ ] asset-05/META.json has valid `estimated_apply_time`
- [ ] asset-06/META.json has valid `estimated_apply_time`
- [ ] asset-07/META.json has valid `estimated_apply_time`
- [ ] asset-08/META.json has valid `estimated_apply_time`
- [ ] asset-09/META.json has valid `estimated_apply_time`
- [ ] asset-10/META.json has valid `estimated_apply_time`
- [ ] asset-11/META.json has valid `estimated_apply_time`
- [ ] asset-12/META.json has valid `estimated_apply_time`
- [ ] asset-13/META.json has valid `estimated_apply_time`
- [ ] asset-14/META.json has valid `estimated_apply_time`
- [ ] asset-15/META.json has valid `estimated_apply_time`

### 2.2 Automated Verification Script

Run the following script from the project root to validate all asset quality checks programmatically:

```bash
#!/bin/bash
# DiffForge Asset Quality Verification Script
# Run from project root: bash docs/verify_assets.sh

PASS=0
FAIL=0
WARN=0

check() {
  local label="$1"
  local result="$2"
  if [ "$result" = "PASS" ]; then
    echo "  [PASS] $label"
    ((PASS++))
  elif [ "$result" = "WARN" ]; then
    echo "  [WARN] $label"
    ((WARN++))
  else
    echo "  [FAIL] $label"
    ((FAIL++))
  fi
}

for i in $(seq -w 1 15); do
  dir="assets/asset-$i"
  meta="$dir/META.json"
  patch="$dir/changes.patch"
  echo ""
  echo "=== Checking $dir ==="

  # File existence
  for f in changes.patch APPLY.md META.json SOURCE_RUN.md RISK_GUIDE.md; do
    if [ -f "$dir/$f" ]; then
      check "$f exists" "PASS"
    else
      check "$f exists" "FAIL"
    fi
  done

  # META.json checks (requires jq)
  if [ -f "$meta" ]; then
    # Valid JSON
    if jq empty "$meta" 2>/dev/null; then
      check "META.json is valid JSON" "PASS"
    else
      check "META.json is valid JSON" "FAIL"
    fi

    # Risk field
    risk=$(jq -r '.risk // empty' "$meta" 2>/dev/null)
    if [[ "$risk" =~ ^(low|medium|high)$ ]]; then
      check "risk field valid ($risk)" "PASS"
    else
      check "risk field valid" "FAIL"
    fi

    # Portability field
    port=$(jq -r '.portability // empty' "$meta" 2>/dev/null)
    if [[ "$port" =~ ^(low|medium|high)$ ]]; then
      check "portability field valid ($port)" "PASS"
    else
      check "portability field valid" "FAIL"
    fi

    # Gate pass
    gate=$(jq -r '.gate_pass // empty' "$meta" 2>/dev/null)
    if [ "$gate" = "true" ]; then
      check "gate_pass is true" "PASS"
    else
      check "gate_pass is true" "FAIL"
    fi

    # Gate condition
    gc=$(jq -r '.gate_condition // empty' "$meta" 2>/dev/null)
    if [ -n "$gc" ]; then
      check "gate_condition defined" "PASS"
    else
      check "gate_condition defined" "FAIL"
    fi

    # Source run ID
    srid=$(jq -r '.source_run_id | length' "$meta" 2>/dev/null)
    if [ "$srid" -gt 0 ] 2>/dev/null; then
      check "source_run_id has entries ($srid)" "PASS"
    else
      check "source_run_id has entries" "FAIL"
    fi

    # Asset ID matches folder
    aid=$(jq -r '.asset_id // empty' "$meta" 2>/dev/null)
    expected="asset-$i"
    if [ "$aid" = "$expected" ]; then
      check "asset_id matches folder ($aid)" "PASS"
    else
      check "asset_id matches folder (got: $aid, expected: $expected)" "FAIL"
    fi

    # Compatible stack
    cs=$(jq -r '.compatible_stack | length' "$meta" 2>/dev/null)
    if [ "$cs" -gt 0 ] 2>/dev/null; then
      check "compatible_stack non-empty ($cs entries)" "PASS"
    else
      check "compatible_stack non-empty" "FAIL"
    fi

    # Estimated apply time
    eat=$(jq -r '.estimated_apply_time // empty' "$meta" 2>/dev/null)
    if [ -n "$eat" ]; then
      check "estimated_apply_time defined ($eat)" "PASS"
    else
      check "estimated_apply_time defined" "FAIL"
    fi
  fi

  # Patch line count
  if [ -f "$patch" ]; then
    lines=$(wc -l < "$patch")
    if [ "$lines" -gt 10 ]; then
      check "changes.patch > 10 lines ($lines lines)" "PASS"
    else
      check "changes.patch > 10 lines ($lines lines)" "FAIL"
    fi
  fi
done

echo ""
echo "================================"
echo "RESULTS: $PASS passed, $FAIL failed, $WARN warnings"
echo "================================"

if [ "$FAIL" -gt 0 ]; then
  echo "VERDICT: LAUNCH BLOCKED - Fix $FAIL failing checks before launch."
  exit 1
else
  echo "VERDICT: ALL CHECKS PASSED - Clear for launch."
  exit 0
fi
```

---

## Section 3: MARKET READINESS VERIFICATION

Verify that the site content, messaging, and business logic are ready for public launch.

### 3.1 Landing Page (site/index.md)

- [ ] `site/index.md` has a clear, prominent call-to-action (CTA)
- [ ] CTA directs users to pricing or signup
- [ ] Hero section communicates the core value proposition in one sentence
- [ ] At least 3 feature highlights are listed
- [ ] Social proof or credibility indicators are present (testimonials, metrics, logos)
- [ ] Page includes a visual or diagram showing how DiffForge works
- [ ] Mobile-responsive layout considerations are documented
- [ ] Page load time target specified (< 3 seconds)

### 3.2 Competitive Differentiation

- [ ] Differentiation vs. Git (raw patches) is clearly stated
  - Expected messaging: DiffForge assets are curated, documented, validated, and risk-assessed -- unlike raw git patches which lack context, documentation, and quality guarantees
- [ ] Differentiation vs. Entire (full project cloning) is clearly stated
  - Expected messaging: DiffForge applies surgical, targeted changes rather than copying entire projects -- reducing bloat, preserving existing code, and enabling incremental adoption
- [ ] Differentiation is visible on at least 2 pages (index.md, faq.md, or about.md)
- [ ] Comparison table or section exists showing DiffForge vs. alternatives side-by-side
- [ ] Unique selling points are specific and quantifiable where possible

### 3.3 Pricing Strategy (site/pricing.md)

- [ ] Pricing tiers are clearly defined (minimum: Free, Starter, Pro)
- [ ] Each tier lists included features and limitations
- [ ] Bundle strategy is defined (e.g., "5 assets for X", "10 assets for Y")
- [ ] Bundle discount percentage is explicitly stated
- [ ] Annual vs. monthly pricing comparison is shown (if applicable)
- [ ] Enterprise or custom pricing option is mentioned
- [ ] Price points are in KRW (primary) with USD equivalent noted
- [ ] Free tier includes at least 1 asset to reduce friction
- [ ] Upgrade path between tiers is clear

### 3.4 Subscription Logic (site/subscription.md)

- [ ] Subscription billing cycle is defined (monthly/annual)
- [ ] Subscription includes details on what subscribers receive each cycle
- [ ] Cancellation policy is clearly documented
- [ ] Refund policy is defined
- [ ] Subscription pause option is addressed (available or not)
- [ ] Auto-renewal behavior is documented
- [ ] Payment methods accepted are listed
- [ ] Grace period for failed payments is defined
- [ ] Subscriber-only benefits are listed (early access, discounts, etc.)

### 3.5 Manifesto (site/manifesto.md)

- [ ] Manifesto communicates the core value proposition
- [ ] Problem statement is clear: what pain does DiffForge solve?
- [ ] Solution statement is clear: how does DiffForge solve it?
- [ ] Vision for the future is articulated
- [ ] Tone is inspiring but grounded in practical developer reality
- [ ] Manifesto is concise (under 1,000 words)

### 3.6 FAQ (site/faq.md)

- [ ] FAQ covers at least 15 questions
- [ ] Questions are organized by category (General, Pricing, Technical, Legal)
- [ ] General questions include: What is DiffForge? Who is it for? How does it work?
- [ ] Pricing questions include: How much does it cost? Is there a free tier? What payment methods are accepted?
- [ ] Technical questions include: How do I apply an asset? What if the patch fails? What stacks are supported?
- [ ] Legal questions include: What is your refund policy? Can I use assets commercially? Who owns the code?
- [ ] Answers are concise but complete (2-5 sentences each)
- [ ] FAQ links to relevant pages (pricing, terms, subscription) where appropriate

### 3.7 Legal Pages

- [ ] `site/terms.md` covers terms of service
  - [ ] Acceptable use policy defined
  - [ ] Limitation of liability stated
  - [ ] Dispute resolution mechanism specified
  - [ ] Governing law jurisdiction defined
  - [ ] Modification of terms clause included
- [ ] `site/privacy.md` covers privacy policy
  - [ ] Data collected is listed
  - [ ] How data is used is explained
  - [ ] Third-party sharing policy defined
  - [ ] Data retention period stated
  - [ ] User rights (access, deletion, portability) documented
  - [ ] Cookie policy included or referenced
- [ ] `site/copyright.md` covers copyright and licensing
  - [ ] Asset license type defined (what buyers can and cannot do)
  - [ ] Attribution requirements stated (if any)
  - [ ] Redistribution policy defined
  - [ ] Modification rights for purchased assets defined
  - [ ] DiffForge intellectual property rights stated

---

## Verification Sign-Off

### Pre-Launch Gate

| Section | Checked By | Date | Status |
|---------|-----------|------|--------|
| Section 1: Structure Verification | | | [ ] PASS / [ ] FAIL |
| Section 2: Asset Quality Verification | | | [ ] PASS / [ ] FAIL |
| Section 3: Market Readiness Verification | | | [ ] PASS / [ ] FAIL |

### Final Verdict

- [ ] **ALL THREE SECTIONS PASS** -- Cleared for launch
- [ ] **ONE OR MORE SECTIONS FAIL** -- Launch blocked until resolved

**Final Approver**: ___________________________
**Date**: ___________________________
**Signature**: ___________________________

---

## Appendix: Quick Reference Counts

| Category | Expected Count |
|----------|---------------|
| Asset folders | 15 |
| Files per asset | 5 |
| Total asset files | 75 |
| Site pages | 10 |
| Documentation files | 3 |
| Quality checklist items per asset | 12 |
| Total quality checks (15 assets x 12 items) | 180 |
| FAQ minimum questions | 15 |
| Legal pages | 3 (terms, privacy, copyright) |
| Market readiness checklist items | 41 |
| **Total checklist items** | **~300** |
