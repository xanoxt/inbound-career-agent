#!/usr/bin/env python3
"""Smoke test for the Inbound Career Agent pack.

Verifies the repo is internally consistent:
  1. AgentContract.xml is well-formed.
  2. Every playbook id in the contract exists in BOTH locales (ru, en).
  3. All template files exist in BOTH locales.
  4. No stale root-level playbook references (e.g. playbooks/00-... without a locale dir).
  5. LAUNCHER.md still carries the <REPO_URL> placeholder (expected pre-publish).
  6. Locale parity (equal playbook/template counts).

Zero-context: reads only the repo it lives in.
Run:  python3 scripts/smoke_test.py
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ["ru", "en"]
failures = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        failures.append(name)


# 1. XML well-formed
contract = ROOT / "AgentContract.xml"
try:
    root = ET.parse(contract).getroot()
    check("AgentContract.xml well-formed", True)
except Exception as e:
    check("AgentContract.xml well-formed", False, str(e))
    sys.exit(1)

# 2. Playbook ids from contract exist in both locales
pb_ids = [p.get("id") for p in root.findall("./playbooks/playbook")]
missing = []
for loc in LOCALES:
    for pid in pb_ids:
        if not (ROOT / "playbooks" / loc / f"{pid}.md").exists():
            missing.append(f"playbooks/{loc}/{pid}.md")
check(f"all {len(pb_ids)} contract playbooks exist in both locales", not missing, "; ".join(missing))

# 3. Templates exist in both locales
tmpl = ["intake-answers.md", "positioning.md", "materials-present.md"]
missing_t = []
for loc in LOCALES:
    for t in tmpl:
        if not (ROOT / "templates" / loc / t).exists():
            missing_t.append(f"templates/{loc}/{t}")
check("all templates exist in both locales", not missing_t, "; ".join(missing_t))

# 4. No stale root-level playbook references (bare playbooks/<id>.md without a locale dir)
stale = []
pat = re.compile(r"playbooks/(?:00-|0[1-7]-)[A-Za-z0-9-]+\.md")
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix in (".md", ".xml"):
        for m in pat.findall(p.read_text(encoding="utf-8", errors="ignore")):
            stale.append(f"{p.relative_to(ROOT)}: {m}")
check("no stale root-level playbook refs", not stale, "; ".join(stale[:5]))

# 5. No dangling placeholders (post-publish)
remaining = []
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix in (".md", ".xml", ".json"):
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for placeholder, name in [("<REPO_URL>", "<REPO_URL>"), ("<org>", "<org>")]:
            if placeholder in txt:
                remaining.append(f"{p.relative_to(ROOT)}: {name}")
check("no dangling <REPO_URL> or <org> placeholders (post-publish)", not remaining, "; ".join(remaining))

# 6. Locale parity
pcounts = {loc: len(list((ROOT / "playbooks" / loc).glob("*.md"))) for loc in LOCALES}
tcounts = {loc: len(list((ROOT / "templates" / loc).glob("*.md"))) for loc in LOCALES}
check("locale parity (playbooks)", pcounts["ru"] == pcounts["en"], str(pcounts))
check("locale parity (templates)", tcounts["ru"] == tcounts["en"], str(tcounts))

print()
if failures:
    print(f"RESULT: {len(failures)} check(s) FAILED: {', '.join(failures)}")
    sys.exit(1)
print("RESULT: all checks passed")
