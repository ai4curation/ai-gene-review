#!/usr/bin/env python3
"""Does each row's supporting quote talk about the GTPase its claim is about?

This exists because of a real defect in this review, caught in PR review and not
by any validator here. Two ``GO:0005829 cytosol`` rows cite Reactome reactions
with different asserted outputs -- ``R-HSA-205039`` says Rac and Cdc42,
``R-HSA-419166`` says RhoA/B/C -- and both rows were generated from one loop that
attached the *same* quote, the RhoA negative, to both. The RhoA row was right and
the Rac/Cdc42 row was citing evidence about a different GTPase.

Nothing in the repository catches that. The reference validator checks a
``supporting_text`` against its **source publication** -- is this a verbatim
substring of PMID X -- and the quote was a perfectly verbatim substring of the
right paper. What it never checks is the quote against the **claim it sits
under**. A quote can be impeccably sourced and still be evidence for a different
proposition, and for a gene whose whole story is which of five GTPases it acts
on, that distinction is the entire review.

So: for every annotation, collect the GTPases named by the **claim** (from
``RO:0002233 has_input`` extensions and from the "catalysed output is ..." clause
in ``reason``) and the GTPases named by the **union of its quotes**. If both sides
name GTPases and they are disjoint, the row is citing evidence about something
else.

The union is taken deliberately. A row may legitimately quote a negative about
Rac1 while claiming Cdc42 -- the ``GO:0005096`` row does exactly that, pairing the
Cdc42 exchange result with the Rac1/RhoG specificity result -- so requiring every
individual quote to match would fire on correct rows. Requiring that *some* quote
engages the claimed GTPase is the strongest rule that does not.

Run:    uv run --with pyyaml python quote_claim_coherence.py
        uv run --with pyyaml python quote_claim_coherence.py --self-test
Writes: quote_claim_coherence.json
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

import yaml

# Surface forms -> canonical GTPase. Word-boundary matched, so "RhoGEF" and
# "RhoG-dependent" do not make "RHOA" match, and "Rac GEF" counts as Rac.
GTPASE_PATTERNS: dict[str, str] = {
    "RHOA": r"\bRhoA\b",
    "RHOB": r"\bRhoB\b",
    "RHOC": r"\bRhoC\b",
    "RHOG": r"\bRhoG\b",
    "RAC1": r"\bRac1\b|\bRac\b",
    "CDC42": r"\bCdc42\b",
}
# has_input accessions -> canonical GTPase.
ACCESSION_TO_GTPASE = {
    "UniProtKB:P61586": "RHOA",
    "UniProtKB:P62745": "RHOB",
    "UniProtKB:P08134": "RHOC",
    "UniProtKB:P84095": "RHOG",
    "UniProtKB:P63000": "RAC1",
    "UniProtKB:P60953": "CDC42",
}
# The clause in `reason` that states what a cited pathway reaction asserts.
OUTPUT_CLAUSE = re.compile(r"catalysed output is (.{0,60}?), and PMID")


def repo_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "genes").is_dir() and (parent / "publications").is_dir():
            return parent
    raise RuntimeError("could not locate the repository root above this script")


def review_path() -> Path:
    return repo_root() / "genes/human/ARHGEF16/ARHGEF16-ai-review.yaml"


def gtpases_in(text: str) -> set[str]:
    return {g for g, pat in GTPASE_PATTERNS.items() if re.search(pat, text or "")}


def claim_gtpases(annotation: dict) -> tuple[set[str], list[str]]:
    """GTPases the row's own claim is about, with the sources of that reading."""
    found: set[str] = set()
    why: list[str] = []
    for ext in annotation.get("extensions") or []:
        if ext.get("predicate") == "RO:0002233":
            acc = (ext.get("term") or {}).get("id")
            if acc in ACCESSION_TO_GTPASE:
                found.add(ACCESSION_TO_GTPASE[acc])
                why.append(f"has_input {acc}")
    reason = (annotation.get("review") or {}).get("reason") or ""
    m = OUTPUT_CLAUSE.search(reason)
    if m:
        g = gtpases_in(m.group(1))
        if g:
            found |= g
            why.append(f"asserted output {sorted(g)}")
    return found, why


def quote_gtpases(annotation: dict) -> tuple[set[str], list[dict]]:
    found: set[str] = set()
    quotes: list[dict] = []
    for sb in (annotation.get("review") or {}).get("supported_by") or []:
        text = sb.get("supporting_text") or ""
        g = gtpases_in(text)
        found |= g
        quotes.append({
            "reference_id": sb.get("reference_id"),
            "gtpases": sorted(g),
            "excerpt": text[:100],
        })
    return found, quotes


def check(doc: dict) -> dict[str, object]:
    rows = []
    violations = []
    for i, a in enumerate(doc.get("existing_annotations") or [], 1):
        claim, why = claim_gtpases(a)
        if not claim:
            continue
        quoted, quotes = quote_gtpases(a)
        if not quoted:
            continue
        record = {
            "index": i,
            "term": a.get("term", {}).get("id"),
            "reference": a.get("original_reference_id"),
            "claim_gtpases": sorted(claim),
            "claim_basis": why,
            "quoted_gtpases": sorted(quoted),
            "overlap": sorted(claim & quoted),
            "quotes": quotes,
        }
        rows.append(record)
        if not (claim & quoted):
            violations.append(record)
    return {"checked": rows, "violations": violations}


def file_quotes(doc: dict) -> list[dict]:
    """Every ``file:`` supporting_text in the review, with its resolved path."""
    out: list[dict] = []

    def walk(o):
        if isinstance(o, dict):
            rid, txt = o.get("reference_id"), o.get("supporting_text")
            if isinstance(rid, str) and rid.startswith("file:") and txt:
                out.append({"reference_id": rid, "supporting_text": txt})
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(doc)
    return out


def check_file_quotes(doc: dict) -> dict[str, object]:
    """Verify ``file:`` quotes against their source. CI never does this.

    ``conf/reference_validator_config.yaml`` lists ``file`` under
    ``skip_prefixes``, so a ``file:`` ``supporting_text`` is not checked against
    anything -- a quote from a repo artifact can be paraphrased, stale, or simply
    invented and every validator here stays green. ``reference_base_dir`` is
    ``genes``, so ``file:human/X/...`` resolves under ``genes/``.
    """
    base = repo_root() / "genes"
    verified, bad = [], []
    for q in file_quotes(doc):
        path = base / q["reference_id"][len("file:"):]
        if not path.exists():
            bad.append({**q, "problem": f"no such file: {path}"})
        elif q["supporting_text"] not in path.read_text():
            bad.append({**q, "problem": "quote is not a verbatim substring of the file"})
        else:
            verified.append(q)
    return {"n_verified": len(verified), "violations": bad}


def run() -> dict[str, object]:
    doc = yaml.safe_load(review_path().read_text())

    fq = check_file_quotes(doc)
    if not fq["n_verified"]:
        raise RuntimeError(
            "no file: quote was verified; the extractor found nothing and would "
            "pass vacuously"
        )
    if fq["violations"]:
        lines = [f"{v['reference_id']}: {v['problem']} -- {v['supporting_text'][:70]!r}"
                 for v in fq["violations"]]
        raise RuntimeError("file: quote not verbatim:\n  " + "\n  ".join(lines))

    result = check(doc)
    if not result["checked"]:
        raise RuntimeError(
            "no annotation states both a GTPase claim and a GTPase-bearing quote; "
            "the extractor found nothing to check and would pass vacuously"
        )
    if result["violations"]:
        lines = [
            f"row {v['index']} ({v['term']}, {v['reference']}): claim is about "
            f"{v['claim_gtpases']} but its quotes are about {v['quoted_gtpases']}"
            for v in result["violations"]
        ]
        raise RuntimeError("quote/claim mismatch:\n  " + "\n  ".join(lines))
    return {
        "n_rows_with_a_checkable_gtpase_claim": len(result["checked"]),
        "n_violations": 0,
        "n_file_quotes_verified_verbatim": fq["n_verified"],
        "rows": result["checked"],
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []
    doc = yaml.safe_load(review_path().read_text())

    # 1. The extractor must actually find rows, or everything below is vacuous.
    base = check(doc)
    checks.append((
        "extractor finds rows with both a GTPase claim and a GTPase quote",
        "PASS" if len(base["checked"]) >= 3 else f"FAIL only {len(base['checked'])}",
    ))

    # 2. The committed review must be clean.
    checks.append((
        "committed review has no quote/claim mismatch",
        "PASS" if not base["violations"] else f"FAIL {base['violations']}",
    ))

    # 3. THE REGRESSION. Restore the exact bug this script was written for --
    #    put the RhoA quote back under the Rac/Cdc42 Reactome row -- and require
    #    it to fire. Anchored by reference id, and the anchor must match exactly
    #    once: zero matches would "pass" by mutating nothing.
    mutated = copy.deepcopy(doc)
    targets = [
        a for a in mutated["existing_annotations"]
        if a.get("original_reference_id") == "Reactome:R-HSA-205039"
    ]
    checks.append((
        "regression anchor matches exactly once",
        "PASS" if len(targets) == 1 else f"FAIL matched {len(targets)} rows",
    ))
    if len(targets) == 1:
        targets[0]["review"]["supported_by"] = [{
            "reference_id": "PMID:20679435",
            "supporting_text": "we could not detect the increase in RhoA activity in cells expressing Ephexin4",
        }]
        res = check(mutated)
        fired = [v for v in res["violations"] if v["reference"] == "Reactome:R-HSA-205039"]
        checks.append((
            "the original bug is detected when reintroduced",
            "PASS" if fired else "FAIL the reintroduced bug was not flagged",
        ))

    # 4. NEGATIVE CONTROL for 3: the mutation must not be what makes the checker
    #    fire in general. With the correct quote restored, the same row is clean.
    if len(targets) == 1:
        targets[0]["review"]["supported_by"] = [{
            "reference_id": "PMID:20679435",
            "supporting_text": "we could observe no obvious increase in the activities of Rac1 and Cdc42 in HEK293T cells by expression of Ephexin4",
        }]
        res = check(mutated)
        fired = [v for v in res["violations"] if v["reference"] == "Reactome:R-HSA-205039"]
        checks.append((
            "the same row is clean once the right quote is restored",
            "PASS" if not fired else f"FAIL {fired}",
        ))

    # 4b. The file: quote verifier must reject a quote that is not in the file,
    #     and must accept the real ones. CI skips file: entirely, so this guard is
    #     the only thing standing between a fabricated artifact quote and green.
    fq = check_file_quotes(doc)
    checks.append((
        "every file: quote in the review is verbatim in its source",
        "PASS" if fq["n_verified"] and not fq["violations"]
        else f"FAIL {fq['violations'][:2]}",
    ))
    tampered = copy.deepcopy(doc)
    hit = 0
    for a in tampered.get("existing_annotations") or []:
        for sb in (a.get("review") or {}).get("supported_by") or []:
            if str(sb.get("reference_id", "")).startswith("file:"):
                sb["supporting_text"] = "a sentence that is not in the artifact at all"
                hit += 1
                break
        if hit:
            break
    checks.append((
        "file: tamper anchor matched exactly once",
        "PASS" if hit == 1 else f"FAIL matched {hit}",
    ))
    if hit == 1:
        checks.append((
            "a fabricated file: quote is rejected",
            "PASS" if check_file_quotes(tampered)["violations"] else "FAIL not detected",
        ))

    # 5. The word-boundary matcher must not be fooled by lookalikes. "RhoGEF"
    #    contains "RhoG" as a substring and "Rho" as a prefix; neither should
    #    make a row look like it is about RhoG or RhoA.
    a = gtpases_in("a Dbl-family RhoGEF with a DH domain")
    b = gtpases_in("exchange on RhoG was measured")
    checks.append((
        "matcher is not fooled by RhoGEF / substring lookalikes",
        "PASS" if (a == set() and b == {"RHOG"}) else f"FAIL RhoGEF->{sorted(a)} RhoG->{sorted(b)}",
    ))

    # 6. A vacuous extractor must abort rather than report success.
    saved = dict(GTPASE_PATTERNS)
    try:
        GTPASE_PATTERNS.clear()
        run()
        checks.append(("a vacuous extractor aborts", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append((
            "a vacuous extractor aborts",
            "PASS" if "vacuously" in str(e) else f"FAIL {e}",
        ))
    finally:
        GTPASE_PATTERNS.update(saved)

    # 7. NEGATIVE CONTROL for 6: restored, the real run completes.
    try:
        run()
        checks.append(("restored patterns run clean", "PASS"))
    except RuntimeError as e:
        checks.append(("restored patterns run clean", f"FAIL {e}"))

    for name, verdict in checks:
        mark = verdict.split()[0]
        print(f"  [{mark}] {name}" + ("" if mark == "PASS" else f" -- {verdict}"))
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
    dest = Path(__file__).with_name("quote_claim_coherence.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"rows whose claim names a GTPase and whose quotes do too: "
          f"{out['n_rows_with_a_checkable_gtpase_claim']}")
    for r in out["rows"]:
        print(f"  {r['term']:<12} {str(r['reference']):<24} claim={r['claim_gtpases']} "
              f"quotes={r['quoted_gtpases']} overlap={r['overlap']}")
    print(f"\n  violations: {out['n_violations']}")
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
