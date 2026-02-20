#!/usr/bin/env python3
import json, os, sys

BASE = "/home/motorboy/diff-forge-launch-stack"
ASSETS = [
    "auth__policy_gate__student_approval__v1.0",
    "auth__middleware__approved_only_access__v1.0",
    "auth__audit_log__role_change_tracking__v1.0",
    "auth__rate_limit__login_protection__v1.0",
    "gov__define__run_manifest_schema__v1.0",
    "gov__enforce__gate_pass_rule__v1.0",
    "gov__freeze__immutable_snapshot__v1.0",
    "gov__classify__risk_scoring_matrix__v1.0",
    "ops__reset__db_migration_pipeline__v1.0",
    "ops__clear__asset_cache_rebuild__v1.0",
    "ops__detect__env_mismatch_guard__v1.0",
    "ops__retry__controlled_backoff_loop__v1.0",
    "sec__inject__visible_watermark__v1.0",
    "sec__render__controller_protected_html__v1.0",
    "sec__log__sensitive_access_trace__v1.0",
]
REQUIRED_FILES = ["changes.patch", "APPLY.md", "META.json", "SOURCE_RUN.md", "RISK_GUIDE.md"]
SITE_PAGES = ["index.md","pricing.md","about.md","packs.md","subscription.md","manifesto.md","faq.md","legal_terms.md","legal_privacy.md","legal_copyright.md"]
DOCS = ["LAUNCH_30D_PLAN.md","ASSET_CREATION_WORKFLOW.md","LAUNCH_VERIFICATION_CHECKLIST.md"]

total_pass = 0
total_fail = 0
failures = []

def check(name, condition, detail=""):
    global total_pass, total_fail, failures
    if condition:
        total_pass += 1
        return True
    else:
        total_fail += 1
        failures.append(f"{name}: {detail}")
        return False

print("=" * 60)
print("DIFFFORGE LAUNCH VERIFICATION")
print("=" * 60)

# STRUCTURE
print("\n## STRUCTURE VERIFICATION\n")
for a in ASSETS:
    path = os.path.join(BASE, "assets", a)
    check(f"folder:{a}", os.path.isdir(path), "folder missing")
    for f in REQUIRED_FILES:
        fp = os.path.join(path, f)
        check(f"file:{a}/{f}", os.path.isfile(fp), "file missing")

for p in SITE_PAGES:
    check(f"site:{p}", os.path.isfile(os.path.join(BASE, "site", p)), "missing")

for d in DOCS:
    check(f"docs:{d}", os.path.isfile(os.path.join(BASE, "docs", d)), "missing")

# ASSET QUALITY
print("## ASSET QUALITY VERIFICATION\n")
for a in ASSETS:
    meta_path = os.path.join(BASE, "assets", a, "META.json")
    patch_path = os.path.join(BASE, "assets", a, "changes.patch")

    try:
        meta = json.load(open(meta_path))
    except:
        check(f"json:{a}", False, "invalid JSON")
        continue

    check(f"risk:{a}", meta.get("risk") in ("low","medium","high"), f"risk={meta.get('risk')}")
    check(f"portability:{a}", meta.get("portability") in ("low","medium","high"), f"port={meta.get('portability')}")
    check(f"gate_pass:{a}", meta.get("gate_pass") == True, f"gate_pass={meta.get('gate_pass')}")
    check(f"gate_cond:{a}", bool(meta.get("gate_condition")), "empty gate_condition")
    check(f"run_ids:{a}", len(meta.get("source_run_ids", [])) > 0, "no run IDs")
    check(f"asset_id:{a}", meta.get("asset_id") == a, f"id={meta.get('asset_id')}")
    check(f"stack:{a}", len(meta.get("compatible_stack", [])) > 0, "no stack")
    check(f"apply_time:{a}", bool(meta.get("estimated_apply_time")), "no apply time")

    with open(patch_path) as f:
        lines = len(f.readlines())
    check(f"patch_size:{a}", lines >= 10, f"only {lines} lines")

# MARKET READINESS
print("## MARKET READINESS VERIFICATION\n")
with open(os.path.join(BASE, "site", "index.md")) as f:
    idx = f.read()
check("cta:index", "pricing" in idx.lower() or "get started" in idx.lower(), "no CTA")
check("diff:index", "git" in idx.lower() and "entire" in idx.lower(), "no differentiation")

with open(os.path.join(BASE, "site", "pricing.md")) as f:
    pricing = f.read()
check("bundle:pricing", "bundle" in pricing.lower(), "no bundle strategy")
check("49000:pricing", "49,000" in pricing or "49000" in pricing, "starter price missing")
check("149000:pricing", "149,000" in pricing or "149000" in pricing, "pro price missing")
check("29000:pricing", "29,000" in pricing or "29000" in pricing, "sub price missing")

with open(os.path.join(BASE, "site", "subscription.md")) as f:
    sub = f.read()
check("sub_logic:subscription", "month" in sub.lower(), "no subscription logic")

with open(os.path.join(BASE, "site", "manifesto.md")) as f:
    man = f.read()
check("value_prop:manifesto", "verified" in man.lower(), "no value proposition")

with open(os.path.join(BASE, "site", "faq.md")) as f:
    faq = f.read()
q_count = faq.count("**")  // 2
check("faq_count", q_count >= 15, f"only {q_count} questions")

for legal in ["legal_terms.md", "legal_privacy.md", "legal_copyright.md"]:
    fp = os.path.join(BASE, "site", legal)
    check(f"legal:{legal}", os.path.getsize(fp) > 500, "too short")

# SUMMARY
print("\n" + "=" * 60)
print(f"TOTAL: {total_pass} PASS / {total_fail} FAIL")
print("=" * 60)

if failures:
    print(f"\nFAILURES ({len(failures)}):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
else:
    print("\nDiffForge Launch Package Verified.")
    sys.exit(0)
