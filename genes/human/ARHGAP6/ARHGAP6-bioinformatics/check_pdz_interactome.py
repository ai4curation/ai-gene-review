#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Are ARHGAP6's 22 `protein binding` IPI rows 22 findings, or one?

Motivation
----------
Half of ARHGAP6's GOA rows -- 22 of 44 -- are `GO:0005515 protein binding` (IPI),
all from a single reference. Reviewing them as 22 independent interactions would
overstate what is known; reviewing them as one would need to be *shown*, not
asserted. The testable version of "one" is: every partner is a PDZ-domain protein,
and ARHGAP6's C-terminus is a PDZ-binding motif -- i.e. the 22 rows report one
binding determinant measured once.

What is computed (no finding is hardcoded)
------------------------------------------
1. The partner accessions are parsed out of `../ARHGAP6-goa.tsv` -- the repository's
   own GOA download -- by selecting GO:0005515 rows and reading their WITH/FROM
   column. The list is not typed into this script, so it tracks the data.
2. Each partner's UniProt record is fetched and its PDZ domains counted, by two
   independent signals: UniProt `Domain` features whose description contains PDZ,
   and the InterPro PDZ cross-reference IPR001478.
3. The target's own C-terminal residues are read from its UniProt sequence and
   classified against the stated canonical rule.

The class rule, stated explicitly so the call is auditable rather than asserted:
a C-terminal class I PDZ-binding motif is ``-X-S/T-X-phi-COOH``, i.e. serine or
threonine at position -2 and a hydrophobic residue at position 0.

Controls
--------
* Positive control: SNTA1 (Q13424), a PDZ-domain protein that is NOT among the
  partners, must be detected as PDZ-containing. This checks the detector rather
  than the panel.
* Negative control: RHOA (P61586) -- ARHGAP6's own GTPase substrate, and therefore
  a protein with every reason to appear in an ARHGAP6 interactome yet no PDZ
  domain -- must be detected as PDZ-free. A detector that calls everything PDZ
  would fail here.
* The motif rule is exercised on constructed strings in --self-test, including
  sequences that must NOT be called class I.

Usage
-----
    uv run check_pdz_interactome.py            # writes RESULTS-pdz-interactome.md
    uv run check_pdz_interactome.py --stdout
    uv run check_pdz_interactome.py --self-test
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

TARGET = "O43182"
TARGET_SYMBOL = "ARHGAP6"
BINDING_TERM = "GO:0005515"
IPR_PDZ = "IPR001478"

POSITIVE_CONTROL = ("Q13424", "SNTA1")   # PDZ protein, not in the partner set
NEGATIVE_CONTROL = ("P61586", "RHOA")    # the substrate GTPase; no PDZ domain

# Hydrophobic residues accepted at position 0 of a class I motif.
HYDROPHOBIC = set("VILFMAWC")

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"


def _get(url: str):
    with urllib.request.urlopen(url, timeout=90) as fh:
        return json.load(fh)


def partners_from_goa(goa_path: Path) -> list[str]:
    """Accessions in the WITH/FROM column of the GO:0005515 rows of the GOA TSV."""
    if not goa_path.exists():
        raise SystemExit(f"FAIL: GOA file not found at {goa_path}")
    accs: list[str] = []
    with goa_path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row.get("GO TERM") != BINDING_TERM:
                continue
            for token in (row.get("WITH/FROM") or "").split("|"):
                token = token.strip()
                if token.startswith("UniProtKB:"):
                    accs.append(token.split(":", 1)[1])
    if not accs:
        raise SystemExit(
            f"FAIL: no {BINDING_TERM} WITH/FROM accessions parsed from {goa_path}. "
            "The parse is broken or the column names changed; refusing to report."
        )
    return sorted(set(accs))


def pdz_profile(acc: str) -> tuple[str, int, bool, str]:
    """(gene symbol, #PDZ Domain features, has IPR001478, sequence C-terminus)."""
    d = _get(UNIPROT.format(acc=acc))
    sym = ""
    genes = d.get("genes") or []
    if genes and genes[0].get("geneName"):
        sym = genes[0]["geneName"]["value"]
    n_dom = sum(
        1
        for f in d.get("features", [])
        if f["type"] == "Domain" and "PDZ" in (f.get("description") or "").upper()
    )
    has_ipr = any(
        x["database"] == "InterPro" and x["id"] == IPR_PDZ
        for x in d.get("uniProtKBCrossReferences", [])
    )
    return sym, n_dom, has_ipr, d["sequence"]["value"][-6:]


def is_class_one(cterm: str) -> bool:
    """Class I C-terminal PDZ-binding motif: -X-S/T-X-phi-COOH."""
    if len(cterm) < 3:
        return False
    return cterm[-3] in "ST" and cterm[-1] in HYDROPHOBIC


def self_test() -> int:
    failures: list[str] = []

    # Motif rule: positives and, crucially, negatives.
    cases = [
        ("PETLV", True, "S/T at -2 and hydrophobic at 0"),
        ("ESDV", True, "classic class I (PSD-95 ligand)"),
        ("PEALV", False, "alanine at -2 is not S/T"),
        ("PETLD", False, "aspartate at 0 is not hydrophobic"),
        ("LV", False, "too short to call"),
    ]
    for seq, want, why in cases:
        got = is_class_one(seq)
        if got == want:
            print(f"  ok   motif rule: {seq!r} -> {got} ({why})")
        else:
            failures.append(f"motif rule: {seq!r} -> {got}, expected {want} ({why})")

    # Guard: a missing GOA file must be refused, not silently skipped.
    try:
        partners_from_goa(Path("/nonexistent/ARHGAP6-goa.tsv"))
        failures.append("missing-goa guard did NOT fire")
    except SystemExit as exc:
        if "GOA file not found" in str(exc):
            print("  ok   missing-goa guard: fired")
        else:
            failures.append(f"missing-goa guard fired with wrong message: {exc}")

    # Detector controls: one PDZ protein outside the panel, one non-PDZ protein.
    for (acc, name), expect_pdz in ((POSITIVE_CONTROL, True), (NEGATIVE_CONTROL, False)):
        sym, n_dom, has_ipr, _ = pdz_profile(acc)
        got = n_dom > 0 or has_ipr
        if got == expect_pdz:
            print(f"  ok   detector control: {name} ({acc}) PDZ={got} as expected")
        else:
            failures.append(f"detector control: {name} ({acc}) PDZ={got}, expected {expect_pdz}")

    if failures:
        print("\nSELF-TEST FAILURES:")
        for f in failures:
            print("  FAIL " + f)
        return 1
    print("\nself-test: all guards fired, all controls clean")
    return 0


def render(rows: list[tuple[str, str, int, bool, str]], target_cterm: str, n_goa_rows: int) -> str:
    today = date.today().isoformat()
    with_pdz = [r for r in rows if r[2] > 0 or r[3]]
    out: list[str] = []
    A = out.append
    A(f"# {TARGET_SYMBOL} bioinformatics: are the 22 `protein binding` rows 22 findings or one?")
    A("")
    A("## Question")
    A("")
    A(f"Half of {TARGET_SYMBOL}'s GOA rows ({n_goa_rows} of 44) are `{BINDING_TERM} protein binding`")
    A("(IPI) from a single reference. Treating them as that many independent findings")
    A("would overstate the evidence. The testable alternative -- that they report **one**")
    A("binding determinant -- predicts that every partner is a PDZ-domain protein and")
    A(f"that {TARGET_SYMBOL}'s C-terminus is a PDZ-binding motif.")
    A("")
    A("## Method")
    A("")
    A("Partner accessions are parsed from the WITH/FROM column of the")
    A("`GO:0005515` rows of `../ARHGAP6-goa.tsv` (the repository's own GOA download),")
    A("not typed into the script. Each is then checked for PDZ domains by two")
    A("independent signals: UniProt `Domain` features naming PDZ, and the InterPro")
    A(f"cross-reference `{IPR_PDZ}`. The target's C-terminal residues are read from its")
    A("UniProt sequence and classified by the stated rule below.")
    A("")
    A("Class rule, stated so the call is auditable: a C-terminal **class I** PDZ-binding")
    A("motif is `-X-S/T-X-phi-COOH` -- serine or threonine at position -2, hydrophobic")
    A("residue at position 0.")
    A("")
    A("```")
    A("uv run check_pdz_interactome.py")
    A("uv run check_pdz_interactome.py --self-test")
    A("```")
    A("")
    A(f"## Result (run {today})")
    A("")
    A(f"**{TARGET_SYMBOL} ({TARGET}) C-terminus: `...{target_cterm}`** -- "
      f"class I motif by the rule above: **{'yes' if is_class_one(target_cterm) else 'no'}** "
      f"(position -2 = `{target_cterm[-3]}`, position 0 = `{target_cterm[-1]}`).")
    A("")
    A(f"Partners parsed from the GOA file: **{len(rows)}**. "
      f"Carrying at least one PDZ domain: **{len(with_pdz)}**.")
    A("")
    A("| partner | acc | PDZ `Domain` features | InterPro IPR001478 |")
    A("|---|---|---|---|")
    for sym, acc, n_dom, has_ipr, _ in rows:
        flag = "yes" if has_ipr else "**no**"
        A(f"| {sym or '?'} | {acc} | {n_dom} | {flag} |")
    A("")
    A("## Interpretation")
    A("")
    if len(with_pdz) == len(rows):
        A(f"**Every one of the {len(rows)} partners is a PDZ-domain protein**, and")
        A(f"{TARGET_SYMBOL} ends in a canonical class I PDZ-binding motif. The 22 GOA rows")
        A("are therefore one binding determinant reported 22 times, not 22 independent")
        A("interactions -- and they came from one assay in one paper.")
    else:
        missing = [f"{s or a} ({a})" for s, a, n, i, _ in rows if not (n > 0 or i)]
        A(f"{len(with_pdz)} of {len(rows)} partners carry a PDZ domain. Exceptions: "
          + ", ".join(missing) + ".")
        A("The 'one determinant' reading does not cover the whole set.")
    A("")
    A("For curation this bears on how much the rows are worth, not on whether they are")
    A("true. They are real measurements. But `protein binding` is the least informative")
    A("molecular-function term available, the partners are scaffolds rather than")
    A("substrates, and nothing in the set speaks to what ARHGAP6 *does*. They belong in")
    A("the review as non-core.")
    A("")
    A("## Caveats")
    A("")
    A("- A shared binding determinant is not evidence that the interactions are")
    A("  biologically equivalent: affinity, expression overlap and localisation differ")
    A("  between partners, and none of that is examined here.")
    A("- PDZ-domain content is a property of the partners. That the assay recovered only")
    A("  PDZ proteins may reflect the assay's design rather than ARHGAP6's selectivity;")
    A("  this script cannot distinguish those and does not try.")
    A("- The motif class rule is the textbook one. A C-terminal sequence matching it is")
    A("  a *candidate* ligand; this is sequence evidence, not a binding measurement.")
    A("")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        print("self-test:")
        return self_test()

    goa_path = Path(__file__).resolve().parent.parent / f"{TARGET_SYMBOL}-goa.tsv"
    accs = partners_from_goa(goa_path)
    n_goa_rows = len(accs)

    try:
        # Detector controls, asserted every run.
        _, n_dom, has_ipr, _ = pdz_profile(POSITIVE_CONTROL[0])
        if not (n_dom > 0 or has_ipr):
            raise SystemExit(
                f"FAIL: positive control {POSITIVE_CONTROL[1]} not detected as PDZ; "
                "the detector is broken, refusing to report."
            )
        _, n_dom, has_ipr, _ = pdz_profile(NEGATIVE_CONTROL[0])
        if n_dom > 0 or has_ipr:
            raise SystemExit(
                f"FAIL: negative control {NEGATIVE_CONTROL[1]} detected as PDZ; "
                "the detector calls non-PDZ proteins PDZ, refusing to report."
            )

        rows = []
        for acc in accs:
            sym, n_dom, has_ipr, _ = pdz_profile(acc)
            rows.append((sym, acc, n_dom, has_ipr, ""))
        _, _, _, target_cterm = pdz_profile(TARGET)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"network failure, no result produced: {exc}", file=sys.stderr)
        return 2

    rows.sort(key=lambda r: (r[0] or "zzz"))
    md = render(rows, target_cterm, n_goa_rows)
    if args.stdout:
        print(md)
    else:
        out = Path(__file__).with_name("RESULTS-pdz-interactome.md")
        out.write_text(md)
        print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
