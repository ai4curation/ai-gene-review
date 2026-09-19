#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Do the ARHGAP6 review's prose claims match what the files actually contain?

Motivation
----------
Two classes of claim in this review are invisible to CI:

1. **`supporting_text` against `file:` references is not validated.** The
   repository's reference validator checks quotes only for `PMID:`/`DOI:`
   references, so a quote attributed to `RESULTS.md` or to the UniProt record can
   be paraphrased, or invented outright, and every validator still passes. This
   review makes 27 such quotes.
2. **Prose can claim something the artifact does not do.** "Recorded as a finding"
   was written in this PR's notes and body while every `references[].findings` was
   `[]`. Sentences like that are testable propositions about files in the repo, and
   the only way they stay true is if something re-tests them.

So this script re-tests them. It is committed next to the review rather than run
once, because a check that does not re-run cannot notice the day its claim stops
being true.

What is checked
---------------
* every `file:` `supporting_text` occurs in the named file **exactly once**,
  verbatim (zero matches is a fabricated quote; two means the quote is ambiguous);
* every `file:` reference's `title` matches that file's first markdown heading;
* every reference carries a `reference_review` (the manual adjudication), and
  every PMID cached for this gene appears in `references:`;
* the claims the notes make about counts -- findings on specific references, the
  deliberate absence of a `molecular_function` on the actin core function, and the
  four papers excluded on purpose -- hold;
* `check_pdz_interactome.py` contains no hardcoded row denominator in live code.

Controls
--------
`--self-test` mutation-tests each guard: a fabricated quote, a wrong file title, a
stripped `reference_review`, and a reinstated hardcoded denominator must each be
caught, and the clean document must stay silent. The denominator check parses the
module rather than scanning text, because a text scan fired on the docstring that
*documents* the defect's removal -- so it is mutation-tested in both directions.

Usage
-----
    uv run check_review_consistency.py
    uv run check_review_consistency.py --self-test
"""

from __future__ import annotations

import argparse
import ast
import copy
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GENES_ROOT = GENE_DIR.parent.parent          # .../genes
REPO = GENES_ROOT.parent
REVIEW = GENE_DIR / "ARHGAP6-ai-review.yaml"
NOTES = GENE_DIR / "ARHGAP6-notes.md"
PDZ_SCRIPT = HERE / "check_pdz_interactome.py"

PUBLICATIONS = REPO / "publications"
PMID_RE = re.compile(r"PMID[:_](\d{6,9})")


def provider_cited_and_cached() -> set[str]:
    """PMIDs the deep-research provider cites that also have a cached publication.

    Derived, not declared. The defect this exists for is the concrete one that
    occurred: the provider cited a paper, it was fetched into ``publications/``,
    and it then appeared nowhere in the review -- so a declared literal would have
    been written *after* the omission and could not have caught it.

    The scope is deliberately the deep-research file rather than the whole gene
    folder. The notes legitimately discuss third-party PMIDs about *other* proteins
    (the arginine-finger comparator panel cites ARHGAP11B's NOT annotations, for
    instance), several of which are cached by unrelated PRs; requiring those in this
    gene's references would be a false positive. Requiring the provider's own cited
    papers to be accounted for is the rule that matches the failure.
    """
    out: set[str] = set()
    for f in sorted(GENE_DIR.glob("*-deep-research-*.md")):
        for pmid in PMID_RE.findall(f.read_text()):
            if (PUBLICATIONS / f"PMID_{pmid}.md").exists():
                out.add(f"PMID:{pmid}")
    return out

EXPECTED_FINDINGS = {"PMID:19038263": 4, "PMID:18434237": 2}

# The four papers cached and deliberately not annotated; the notes must say so.
EXCLUDED_ON_PURPOSE = ["30816546", "33116826", "38287795", "12673365"]


def resolve_file_ref(ref_id: str) -> Path:
    """`file:human/ARHGAP6/x.md` -> absolute path under genes/."""
    return GENES_ROOT / ref_id[len("file:"):]


def iter_supporting(review: dict):
    for a in review.get("existing_annotations", []):
        for sb in (a.get("review", {}) or {}).get("supported_by", []) or []:
            yield sb
    for cf in review.get("core_functions", []) or []:
        for sb in cf.get("supported_by", []) or []:
            yield sb


def hardcoded_denominator_defects(src: str) -> list[str]:
    """Live-code occurrences of the removed hardcoded denominator.

    Parses rather than greps: the module docstring legitimately mentions both
    ``n_goa_rows`` and ``22 of 44`` while explaining that they were removed, and a
    substring scan cannot tell that prose from the code it describes.
    """
    tree = ast.parse(src)
    doc_nodes = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, "body", None)
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
                if isinstance(body[0].value.value, str):
                    doc_nodes.add(id(body[0].value))
    found: list[str] = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in doc_nodes:
            if "of 44" in n.value:
                found.append(f"literal 'of 44' in live code: {n.value[:50]!r}")
        if isinstance(n, ast.Constant) and isinstance(n.value, int) and not isinstance(n.value, bool):
            if n.value == 44:
                found.append("literal int 44 in code")
        if isinstance(n, ast.Name) and n.id == "n_goa_rows":
            found.append("identifier n_goa_rows still used")
        if isinstance(n, ast.arg) and n.arg == "n_goa_rows":
            found.append("parameter n_goa_rows still declared")
    return found


def audit(review: dict, notes: str, pdz_src: str,
          extra_expected: set[str] | None = None) -> list[str]:
    """Return a list of problems. Empty means the document is self-consistent."""
    bad: list[str] = []

    refs = {r["id"]: r for r in review.get("references", [])}

    # 1. file: quotes must be verbatim and unambiguous.
    n_file_quotes = 0
    for sb in iter_supporting(review):
        rid = sb.get("reference_id", "")
        if not rid.startswith("file:"):
            continue
        n_file_quotes += 1
        p = resolve_file_ref(rid)
        if not p.exists():
            bad.append(f"file reference does not exist: {rid}")
            continue
        count = p.read_text().count(sb.get("supporting_text", "\0"))
        if count != 1:
            bad.append(
                f"file quote matches {count}x (want exactly 1) in {p.name}: "
                f"{sb.get('supporting_text','')[:70]!r}"
            )
    if n_file_quotes == 0:
        bad.append("no file: quotes were examined; the check is not doing anything")

    # 2. file: reference titles must match the file's own first heading.
    for rid, r in refs.items():
        if not (rid.startswith("file:") and rid.endswith(".md")):
            continue
        p = resolve_file_ref(rid)
        if not p.exists():
            bad.append(f"file reference does not exist: {rid}")
            continue
        head = next((l[2:].strip() for l in p.read_text().splitlines() if l.startswith("# ")), "")
        if head != (r.get("title") or "").strip():
            bad.append(f"title/heading mismatch for {rid}: {r.get('title')!r} vs {head!r}")

    # 3. adjudication and coverage.
    for rid, r in refs.items():
        if "reference_review" not in r:
            bad.append(f"reference has no reference_review: {rid}")
    expected = extra_expected if extra_expected is not None else provider_cited_and_cached()
    if not expected:
        bad.append(
            "no provider-cited, cached PMIDs were found; the coverage check is "
            "examining nothing"
        )
    for pmid in sorted(expected):
        if pmid not in refs:
            bad.append(f"cached publication absent from references: {pmid}")

    # 4. counted claims the prose makes.
    for rid, want in EXPECTED_FINDINGS.items():
        got = len((refs.get(rid) or {}).get("findings") or [])
        if got != want:
            bad.append(f"{rid}: {got} findings, prose claims {want}")

    cfs = review.get("core_functions") or []
    if len(cfs) < 2:
        bad.append("expected at least two core_functions")
    else:
        cf1 = cfs[1]
        if "molecular_function" in cf1 or "contributes_to_molecular_function" in cf1:
            bad.append(
                "core_functions[1] asserts a molecular function; the review's stated "
                "position is that none is asserted for the GAP-independent actin role"
            )

    for pmid in EXCLUDED_ON_PURPOSE:
        if pmid not in notes:
            bad.append(f"notes do not explain why PMID:{pmid} yields no annotation")

    # 5. the PDZ script's denominator.
    bad.extend(f"check_pdz_interactome.py: {d}" for d in hardcoded_denominator_defects(pdz_src))

    return bad


def self_test(review: dict, notes: str, pdz_src: str) -> int:
    failures: list[str] = []

    def expect_caught(name: str, mutated_review, mutated_notes, mutated_pdz, needle: str):
        found = audit(mutated_review, mutated_notes, mutated_pdz)
        if any(needle in f for f in found):
            print(f"  ok   {name}: caught ({needle!r})")
        else:
            failures.append(f"{name}: NOT caught. got {found}")

    # Negative control: the real document must be silent.
    clean = audit(review, notes, pdz_src)
    if clean:
        failures.append(f"clean document is not clean: {clean}")
    else:
        print("  ok   negative control: the real document raises nothing")

    # Mutation 1: fabricate a file: quote.
    m = copy.deepcopy(review)
    for sb in iter_supporting(m):
        if sb.get("reference_id", "").startswith("file:"):
            sb["supporting_text"] = "a sentence that is not in the file"
            break
    expect_caught("fabricated file: quote", m, notes, pdz_src, "matches 0x")

    # Mutation 2: wrong title on a file: reference.
    m = copy.deepcopy(review)
    for r in m["references"]:
        if r["id"].startswith("file:") and r["id"].endswith(".md"):
            r["title"] = "Some other document entirely"
            break
    expect_caught("wrong file: title", m, notes, pdz_src, "title/heading mismatch")

    # Mutation 3: strip a reference_review.
    m = copy.deepcopy(review)
    for r in m["references"]:
        if "reference_review" in r:
            del r["reference_review"]
            break
    expect_caught("missing reference_review", m, notes, pdz_src, "no reference_review")

    # Mutation 4: the findings claim stops being true.
    m = copy.deepcopy(review)
    for r in m["references"]:
        if r["id"] == "PMID:19038263":
            r["findings"] = []
    expect_caught("findings emptied", m, notes, pdz_src, "prose claims 4")

    # Mutation 5: an MF reappears on the actin core function.
    m = copy.deepcopy(review)
    m["core_functions"][1]["molecular_function"] = {"id": "GO:0005096", "label": "GTPase activator activity"}
    expect_caught("MF asserted on the actin core function", m, notes, pdz_src,
                  "asserts a molecular function")

    # Mutation 6a: a provider-cited, cached paper is dropped from references. This
    # is the exact defect the check exists for, so it is tested on the derived set
    # rather than on a literal -- a declared list would only ever contain papers
    # someone already remembered to reference.
    derived = provider_cited_and_cached()
    if not derived:
        failures.append("provider_cited_and_cached() derived nothing; the check is inert")
    else:
        victim = sorted(derived)[0]
        m = copy.deepcopy(review)
        m["references"] = [r for r in m["references"] if r["id"] != victim]
        found = audit(m, notes, pdz_src)
        if any(f"cached publication absent from references: {victim}" in f for f in found):
            print(f"  ok   dropped provider-cited cached paper: caught ({victim})")
        else:
            failures.append(f"dropping {victim} was NOT caught. got {found}")
        # And the derived set must exclude papers the provider cites but nobody cached,
        # otherwise the rule would demand references for uncached literature.
        uncached_but_cited = {
            f"PMID:{p}"
            for f in GENE_DIR.glob("*-deep-research-*.md")
            for p in PMID_RE.findall(f.read_text())
            if not (PUBLICATIONS / f"PMID_{p}.md").exists()
        }
        if uncached_but_cited & derived:
            failures.append(f"derived set wrongly includes uncached papers: {uncached_but_cited & derived}")
        else:
            print(f"  ok   derived set excludes {len(uncached_but_cited)} cited-but-uncached PMIDs")

    # Mutation 6: the hardcoded denominator comes back -- and the docstring that
    # merely MENTIONS it must not be enough to trigger the guard.
    defective = (
        '"""Docstring that mentions the old n_goa_rows and the old 22 of 44 line."""\n'
        "def render(n_goa_rows):\n"
        '    return f"({n_goa_rows} of 44)"\n'
    )
    expect_caught("hardcoded denominator reinstated", review, notes, defective, "of 44")
    doc_only = (
        '"""Docstring that mentions the old n_goa_rows and the old 22 of 44 line."""\n'
        "def render(a, b):\n"
        '    return f"({a} of {b})"\n'
    )
    if hardcoded_denominator_defects(doc_only):
        failures.append("denominator guard fires on a docstring that only describes the defect")
    else:
        print("  ok   denominator guard ignores prose about the defect")

    if failures:
        print("\nSELF-TEST FAILURES:")
        for f in failures:
            print("  FAIL " + f)
        return 1
    print("\nself-test: every guard caught its mutation, negative controls clean")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    review = yaml.safe_load(REVIEW.read_text())
    notes = NOTES.read_text()
    pdz_src = PDZ_SCRIPT.read_text()

    if args.self_test:
        print("self-test:")
        return self_test(review, notes, pdz_src)

    problems = audit(review, notes, pdz_src)
    if problems:
        print("INCONSISTENCIES:")
        for p in problems:
            print("  " + p)
        return 1
    n_file_quotes = sum(
        1 for sb in iter_supporting(review) if sb.get("reference_id", "").startswith("file:")
    )
    print(
        f"consistent: {n_file_quotes} file: quotes verbatim and unambiguous, "
        f"{len(review['references'])} references adjudicated, counted claims hold"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
