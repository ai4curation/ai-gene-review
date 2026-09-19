#!/usr/bin/env python3
"""Was the Arhgap4 knockout mouse actually phenotyped, and did anything come out?

Four rows of this review argue that ARHGAP4 is dispensable, and each leans on the mouse
knockout having no phenotype. Stated that way the claim is unverifiable and goes stale
silently, so it is resolved here against IMPC's own Solr endpoints instead.

**The distinction that matters.** "Zero significant phenotypes" is ambiguous and, read
carelessly, is the single most misleading number in the database: it is also what an
**untested** gene returns. Two cores separate the cases:

* ``genotype-phenotype`` -- one document per *significant* gene-to-phenotype association.
* ``statistical-result`` -- one document per *test performed*, significant or not.

``0 / 0`` means nobody looked. ``0 / many`` means people looked hard and found nothing.
Only the second supports a dispensability argument, and the script reports both numbers
for every gene so the two can never be conflated.

Controls are mandatory:

* positives -- Lepr, Dmd, Trp53, genes IMPC certainly has significant hits for. If these
  come back empty the query shape is wrong and every zero below is meaningless.
* an untested negative -- a paralog IMPC has not phenotyped, which must show ``0 / 0`` and
  is reported as *untested* rather than as *unremarkable*.

The run aborts if a positive control returns nothing.

Run:    uv run --with requests python impc_phenotypes.py
        uv run --with requests python impc_phenotypes.py --self-test
Writes: impc_phenotypes.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests

SOLR = "https://www.ebi.ac.uk/mi/impc/solr/{core}/select"

TARGET = "Arhgap4"
# Same PANTHER family (PTHR14166), for the redundancy question.
PARALOGS = ["Srgap1", "Srgap2", "Srgap3"]
# Genes IMPC certainly has significant associations for.
POSITIVE_CONTROLS = ["Lepr", "Dmd", "Trp53"]


def count(core: str, gene: str) -> int:
    r = requests.get(
        SOLR.format(core=core),
        params={"q": f"marker_symbol:{gene}", "rows": 0, "wt": "json"},
        timeout=120,
    )
    r.raise_for_status()
    return int(r.json()["response"]["numFound"])


def significant_terms(gene: str, limit: int = 50) -> list[str]:
    r = requests.get(
        SOLR.format(core="genotype-phenotype"),
        params={
            "q": f"marker_symbol:{gene}",
            "rows": limit,
            "fl": "mp_term_name",
            "wt": "json",
        },
        timeout=120,
    )
    r.raise_for_status()
    docs = r.json()["response"]["docs"]
    return sorted({d["mp_term_name"] for d in docs if d.get("mp_term_name")})


def profile(gene: str) -> dict[str, object]:
    sig = count("genotype-phenotype", gene)
    tests = count("statistical-result", gene)
    if tests == 0:
        verdict = "UNTESTED (0 tests) -- a zero here says nothing about the gene"
    elif sig == 0:
        verdict = f"TESTED AND CLEAN ({tests} tests, 0 significant)"
    else:
        verdict = f"{sig} significant association(s) across {tests} tests"
    return {
        "gene": gene,
        "significant_associations": sig,
        "tests_performed": tests,
        "tested": tests > 0,
        "verdict": verdict,
        "significant_phenotypes": significant_terms(gene) if sig else [],
    }


def run() -> dict[str, object]:
    genes = [TARGET, *PARALOGS, *POSITIVE_CONTROLS]
    rows = {g: profile(g) for g in genes}

    dead_controls = [
        g for g in POSITIVE_CONTROLS if rows[g]["significant_associations"] == 0
    ]
    if dead_controls:
        raise RuntimeError(
            "positive control(s) returned no significant associations: "
            f"{dead_controls}; the query shape is wrong and no zero below can be trusted"
        )

    t = rows[TARGET]
    return {
        "target": TARGET,
        "genes": rows,
        "conclusion": {
            "target_tested": t["tested"],
            "target_tests": t["tests_performed"],
            "target_significant": t["significant_associations"],
            # The only claim this script licenses.
            "supports_dispensability": bool(
                t["tested"] and t["significant_associations"] == 0
            ),
            "untested_genes": sorted(g for g, v in rows.items() if not v["tested"]),
        },
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []

    # 1. Positive control must return significant associations.
    lepr = profile("Lepr")
    checks.append(
        (
            "positive control Lepr has significant associations",
            "PASS" if lepr["significant_associations"] > 0 else f"FAIL {lepr}",
        )
    )
    # 2. ...and named phenotype terms, so the field selection works too.
    checks.append(
        (
            "positive control returns named MP terms",
            "PASS" if lepr["significant_phenotypes"] else "FAIL (no terms)",
        )
    )
    # 3. The target must be distinguishable from untested: many tests, zero hits.
    t = profile(TARGET)
    checks.append(
        (
            "target is tested (nonzero statistical results) and clean",
            "PASS"
            if t["tests_performed"] > 100 and t["significant_associations"] == 0
            else f"FAIL {t}",
        )
    )
    # 4. NEGATIVE CONTROL: a gene IMPC has not phenotyped must read UNTESTED, not clean.
    #    Without this the two zeros are indistinguishable, which is the whole point.
    untested = next(
        (p for p in PARALOGS if profile(p)["tests_performed"] == 0), None
    )
    if untested is None:
        checks.append(
            (
                "untested-vs-clean distinction exercised",
                "FAIL (every paralog is now tested) -- pick an untested comparator",
            )
        )
    else:
        checks.append(
            (
                f"untested gene {untested} reports UNTESTED rather than clean",
                "PASS" if "UNTESTED" in profile(untested)["verdict"] else "FAIL",
            )
        )
    # 5. A nonsense symbol must come back empty rather than matching something.
    bogus = profile("Zzzz9999")
    checks.append(
        (
            "nonexistent symbol returns zero on both cores",
            "PASS"
            if bogus["tests_performed"] == 0 and bogus["significant_associations"] == 0
            else f"FAIL {bogus}",
        )
    )
    # 6. A broken positive control must abort the run rather than be reported.
    saved = POSITIVE_CONTROLS[:]
    POSITIVE_CONTROLS[:] = ["Zzzz9999"]
    try:
        run()
        checks.append(("dead positive control aborts run", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(
            (
                "dead positive control aborts run",
                "PASS" if "positive control" in str(e) else f"FAIL wrong error: {e}",
            )
        )
    finally:
        POSITIVE_CONTROLS[:] = saved

    for name, verdict in checks:
        print(
            f"  [{verdict.split()[0]}] {name}"
            + ("" if verdict.startswith("PASS") else f" -- {verdict}")
        )
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("impc_phenotypes.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"{'gene':<12} {'significant':>11} {'tests':>7}  verdict")
    for g, v in out["genes"].items():
        print(
            f"{g:<12} {v['significant_associations']:>11} {v['tests_performed']:>7}  {v['verdict']}"
        )
    c = out["conclusion"]
    print()
    print(
        f"{TARGET}: tested={c['target_tested']} tests={c['target_tests']} "
        f"significant={c['target_significant']}"
    )
    print("supports a dispensability argument:", c["supports_dispensability"])
    print("genes IMPC has NOT phenotyped (a zero there means nothing):", c["untested_genes"])
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
