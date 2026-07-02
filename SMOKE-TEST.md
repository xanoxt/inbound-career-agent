# SMOKE-TEST

Latest result of `scripts/smoke_test.py` — a reusable repo-consistency check.

## Run

```bash
python3 scripts/smoke_test.py
```

## Checks

| # | Check | Status |
|---|---|---|
| 1 | `AgentContract.xml` well-formed | ✅ |
| 2 | All 9 contract playbooks exist in both locales (ru, en) | ✅ |
| 3 | All templates exist in both locales | ✅ |
| 4 | No stale root-level playbook refs (bare `playbooks/00-…` without a locale dir) | ✅ |
| 5 | `LAUNCHER.md` carries the `<REPO_URL>` placeholder (expected pre-publish) | ✅ |
| 6 | Locale parity — playbook counts equal (`ru: 9, en: 9`) | ✅ |
| 7 | Locale parity — template counts equal (`ru: 3, en: 3`) | ✅ |

**Result: all checks passed** (as of the P5 commit).

## Notes

- Check 5 is intentionally a "placeholder present" gate — `<REPO_URL>` must be filled **only at publish time**, so its presence pre-publish is correct.
- The smoke test catches the most common regression: referencing a playbook by its old root-level path after the locale split. If you add a new playbook/template, update `AgentContract.xml` and both locales, then re-run.
