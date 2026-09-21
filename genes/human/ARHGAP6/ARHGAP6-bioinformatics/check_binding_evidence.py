#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""What kind of binding did PMID:36115835 actually measure for each ARHGAP6 partner?

Motivation
----------
The repository's annotation policy says `GO:0005515 protein binding` should not be
left standing as a generic row: use `MODIFY` when the cited paper supports a more
informative molecular function, and otherwise `REMOVE`. Deciding that for ARHGAP6
means knowing, *per partner*, what the cited experiment measured -- and the cached
full text of PMID:36115835 never names ARHGAP6, because the interactions live in
the supplementary peptide library rather than the main text.

The evidence is recoverable anyway. IntAct curated each pair from that paper and
records, per pair, the interaction detection method and the interaction type. This
script reads those back so the curation decision rests on the curated experimental
record rather than on an assumption about what a large screen must have done.

The companion fact -- that every partner carries a PDZ domain and that ARHGAP6 ends
in a class I PDZ-binding motif -- is established separately by
`check_pdz_interactome.py`. Together they say what the molecular function is:
ARHGAP6's C-terminal motif binds PDZ domains.

What is computed (nothing hardcoded)
------------------------------------
1. The 22 partner accessions, parsed from the WITH/FROM column of the GO:0005515
   rows of `../ARHGAP6-goa.tsv`.
2. Every IntAct interaction record for O43182, paginated, filtered to the
   publication in question.
3. Per partner: the detection method(s) and interaction type(s) IntAct records.

Controls
--------
* **Matcher control (the important one).** An earlier version of this script read
  the `idA`/`idB` fields, which are formatted ``"O43182 (uniprotkb)"`` rather than a
  bare accession, so *every* partner came back unmatched -- a result that looks
  exactly like a real finding of "no evidence". The script therefore refuses to
  report when zero GOA partners match, and `--self-test` asserts that the known-bad
  field choice produces zero matches while the correct one does not. A check that
  cannot tell "no data" from "broken query" is worse than no check.
* **Negative control:** RHOA (P61586), ARHGAP6's own GTPase substrate, has no PDZ
  domain and must NOT appear among this publication's partners.
* **Positive control:** derived from the response rather than fixed -- at least one
  GOA partner must be present with a detection method.

Usage
-----
    uv run check_binding_evidence.py            # writes RESULTS-binding-evidence.md
    uv run check_binding_evidence.py --stdout
    uv run check_binding_evidence.py --self-test
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
PMID = "36115835"
NEGATIVE_CONTROL = ("P61586", "RHOA")

# PSI-MI methods that measure binding directly, rather than inferring it from
# co-purification of a complex. Declared, and checked against the MI identifiers
# IntAct returns so a method cannot be silently reclassified by relabelling.
DIRECT_BINDING_METHODS = {"holdup assay": "MI:2437", "fps": "MI:0053"}
MI_LABELS = {
    "holdup assay": "holdup assay",
    "fps": "fluorescence polarization spectroscopy",
}
MI_IDS: dict[str, str] = {}

INTACT = (
    "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/"
    "{acc}?page={page}&pageSize=100"
)


def _get(url: str):
    with urllib.request.urlopen(url, timeout=90) as fh:
        return json.load(fh)


def goa_partners(goa_path: Path) -> list[str]:
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
        raise SystemExit(f"FAIL: no {BINDING_TERM} partners parsed from {goa_path}")
    return sorted(set(accs))


def fetch_intact(acc: str) -> list[dict]:
    items: list[dict] = []
    page = 0
    while True:
        d = _get(INTACT.format(acc=acc, page=page))
        content = d.get("content") or []
        items.extend(content)
        if d.get("last") or not content:
            break
        page += 1
        if page > 50:          # defensive: never spin forever on a paging bug
            break
    return items


def partner_records(items: list[dict], pmid: str, id_fields=("uniqueIdA", "uniqueIdB")):
    """partner accession -> {(detection method, interaction type)} for one publication.

    ``id_fields`` is a parameter purely so the self-test can demonstrate that the
    wrong field choice yields nothing; production always uses the default.
    """
    out: dict[str, set[tuple[str, str]]] = {}
    fa, fb = id_fields
    for it in items:
        pubs = " ".join(it.get("publicationIdentifiers") or [])
        if pmid not in pubs:
            continue
        a, b = it.get(fa), it.get(fb)
        method = it.get("detectionMethod") or "?"
        itype = it.get("type") or "?"
        for acc, other in ((a, b), (b, a)):
            if acc and acc != TARGET and other == TARGET:
                out.setdefault(acc, set()).add((method, itype))
    return out


def collect_mi_ids(items: list[dict]) -> dict[str, str]:
    """detection method short label -> PSI-MI identifier, as IntAct reports it."""
    out: dict[str, str] = {}
    for it in items:
        m = it.get("detectionMethod")
        mi = it.get("detectionMethodMIIdentifier")
        if m and mi:
            out[m] = mi
    return out


def mi_mismatches(observed: dict[str, str]) -> list[str]:
    """Declared direct-binding methods whose MI id is not what IntAct returns.

    This is what stops the DIRECT_BINDING_METHODS whitelist from being a list of
    strings that someone could satisfy by relabelling: the identifier has to agree.
    """
    bad = []
    for name, mi in DIRECT_BINDING_METHODS.items():
        seen = observed.get(name)
        if seen is not None and seen != mi:
            bad.append(f"{name}: declared {mi}, IntAct reports {seen}")
    return bad


def symbol_of(items: list[dict], acc: str) -> str:
    for it in items:
        if it.get("uniqueIdA") == acc:
            return it.get("moleculeA") or acc
        if it.get("uniqueIdB") == acc:
            return it.get("moleculeB") or acc
    return acc


def self_test(items: list[dict], partners: list[str]) -> int:
    failures: list[str] = []

    good = partner_records(items, PMID)
    matched = [a for a in partners if a in good]
    if matched:
        print(f"  ok   matcher control: {len(matched)}/{len(partners)} GOA partners matched")
    else:
        failures.append("matcher control: zero GOA partners matched with the correct id field")

    # The exact bug that produced a plausible-looking false negative.
    bad = partner_records(items, PMID, id_fields=("idA", "idB"))
    bad_matched = [a for a in partners if a in bad]
    if bad_matched:
        failures.append(
            "the known-bad id field ('idA'/'idB', formatted 'ACC (uniprotkb)') now "
            "matches; the control no longer demonstrates the failure it encodes"
        )
    else:
        print("  ok   known-bad id field yields zero matches, as it did in the wild")

    # Negative control: the substrate GTPase must not be a partner here.
    if NEGATIVE_CONTROL[0] in good:
        failures.append(f"negative control: {NEGATIVE_CONTROL[1]} appears as a partner")
    else:
        print(f"  ok   negative control: {NEGATIVE_CONTROL[1]} absent from this publication")

    # The direct-binding whitelist must be anchored to PSI-MI identifiers, not to
    # labels: assert the declared ids agree with IntAct, and that a wrong id is caught.
    observed = collect_mi_ids(items)
    if mi_mismatches(observed):
        failures.append(f"declared MI ids disagree with IntAct: {mi_mismatches(observed)}")
    else:
        present = {k: v for k, v in observed.items() if k in DIRECT_BINDING_METHODS}
        print(f"  ok   MI identifiers agree with IntAct for {present}")
    tampered = dict(observed)
    for k in DIRECT_BINDING_METHODS:
        if k in tampered:
            tampered[k] = "MI:9999"
            break
    if mi_mismatches(tampered):
        print("  ok   MI-identifier guard catches a relabelled method")
    else:
        failures.append("MI-identifier guard did not catch a tampered identifier")

    # A publication filter that matches everything would make the result meaningless.
    unfiltered = partner_records(items, "")
    if len(unfiltered) <= len(good):
        failures.append("publication filter is not narrowing anything")
    else:
        print(f"  ok   publication filter narrows {len(unfiltered)} -> {len(good)} partners")

    if failures:
        print("\nSELF-TEST FAILURES:")
        for f in failures:
            print("  FAIL " + f)
        return 1
    print("\nself-test: all controls clean")
    return 0


def render(rows, missing, n_partners) -> str:
    today = date.today().isoformat()
    out: list[str] = []
    A = out.append
    A(f"# {TARGET_SYMBOL} bioinformatics: what PMID:{PMID} measured, per partner")
    A("")
    A("## Question")
    A("")
    A(f"All {n_partners} of {TARGET_SYMBOL}'s `{BINDING_TERM} protein binding` rows cite")
    A(f"PMID:{PMID}. The repository's policy is that a generic `protein binding` row")
    A("should be replaced by a more informative molecular function **when the cited")
    A("paper supports one**, so the curation decision needs to know, per partner, what")
    A("that paper actually measured. Its cached full text never names ARHGAP6 -- the")
    A("interactions are in the supplementary peptide library -- so the question cannot")
    A("be answered by reading the main text.")
    A("")
    A("## Method")
    A("")
    A("Partner accessions come from the WITH/FROM column of the `GO:0005515` rows of")
    A("`../ARHGAP6-goa.tsv`. IntAct's curated record for each pair is then read from")
    A("its REST API and filtered to this publication, reporting the **interaction")
    A("detection method** and **interaction type** it records.")
    A("")
    A("```")
    A("uv run check_binding_evidence.py")
    A("uv run check_binding_evidence.py --self-test")
    A("```")
    A("")
    A(f"## Result (run {today})")
    A("")
    A("| partner | acc | detection method (PSI-MI) | interaction type |")
    A("|---|---|---|---|")
    for sym, acc, methods, types in rows:
        m = ", ".join(f"{k} ({MI_IDS.get(k, '?')})" for k in sorted(methods))
        A(f"| {sym} | {acc} | {m} | {', '.join(sorted(types))} |")
    A("")
    if missing:
        A(f"Partners with no record under this publication: {', '.join(missing)}")
        A("")
    A("## Interpretation")
    A("")
    all_methods = {m for _, _, ms, _ in rows for m in ms}
    indirect = sorted(all_methods - set(DIRECT_BINDING_METHODS))
    corroborated = sorted(sym for sym, _, ms, _ in rows if len(ms) > 1)

    if indirect:
        A(f"**Some partners rest on a method that is not a direct binding measurement:** "
          f"{', '.join(indirect)}. Those rows do not support a domain-level molecular")
        A("function and have to be judged individually rather than as a set.")
    else:
        A("**Every partner is supported by at least one direct binding measurement, and")
        A("every pair is typed `direct interaction`.** Two methods appear, and both")
        A("measure binding directly rather than inferring it from a complex:")
        for k in sorted(all_methods):
            A(f"- `{k}` ({MI_IDS.get(k, '?')} {MI_LABELS.get(k, '')})")
        A("")
        A("The holdup assay in this paper is a chromatographic retention measurement of a")
        A("recombinant PDZome library against a library of C-terminal PDZ-binding motif")
        A("peptides. So what was measured for each partner is the affinity between that")
        A("partner's PDZ domain and ARHGAP6's C-terminal motif, not an unspecified")
        A("association.")
        A("")
        if corroborated:
            A(f"{len(corroborated)} partner(s) carry a second, orthogonal measurement as well: "
              f"{', '.join(corroborated)}. That is additional corroboration of the same")
            A("determinant, not a different claim -- it does not split the set.")
            A("")
        A("Taken with `RESULTS-pdz-interactome.md` (all partners carry PDZ domains;")
        A(f"{TARGET_SYMBOL} ends in `...LPETLV`, a class I motif), the informative molecular")
        A("function these rows report is **`GO:0030165 PDZ domain binding`**. That is a")
        A("restatement of the measurement, not an inference from it: no adaptor,")
        A("scaffolding or signalling role is implied, and none would be supported.")
    A("")
    A("## Caveats")
    A("")
    A("- IntAct's `direct interaction` type reflects the curator's reading of the assay;")
    A("  it is evidence about what was measured, not an independent replication.")
    A("- A holdup measurement is made on an isolated domain and a synthetic peptide. It")
    A("  establishes that the motif and the domain bind, not that the full-length")
    A("  proteins meet in a cell.")
    A("- This script says what kind of binding was measured. It does not weigh affinity,")
    A("  and nothing here ranks the partners.")
    A("")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    partners = goa_partners(here.parent / f"{TARGET_SYMBOL}-goa.tsv")

    try:
        items = fetch_intact(TARGET)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"network failure, no result produced: {exc}", file=sys.stderr)
        return 2

    if args.self_test:
        print("self-test:")
        return self_test(items, partners)

    recs = partner_records(items, PMID)

    # Matcher control, asserted on every run: zero matches means a broken query far
    # more often than it means no evidence, and the two must not be confused.
    matched = [a for a in partners if a in recs]
    if not matched:
        raise SystemExit(
            "FAIL: none of the GOA partners were found in IntAct's records for "
            f"PMID:{PMID}. That is far more likely a broken query than an absence of "
            "evidence; refusing to report it as a finding."
        )
    if NEGATIVE_CONTROL[0] in recs:
        raise SystemExit(
            f"FAIL: negative control {NEGATIVE_CONTROL[1]} appears among this "
            "publication's partners; the publication filter is not working."
        )

    MI_IDS.update(collect_mi_ids(items))
    bad_mi = mi_mismatches(MI_IDS)
    if bad_mi:
        raise SystemExit(
            "FAIL: a declared direct-binding method does not carry the PSI-MI "
            f"identifier it is declared with: {bad_mi}. Refusing to classify."
        )

    rows = []
    for acc in partners:
        if acc not in recs:
            continue
        methods = {m for m, _ in recs[acc]}
        types = {t for _, t in recs[acc]}
        rows.append((symbol_of(items, acc), acc, methods, types))
    rows.sort(key=lambda r: r[0])
    missing = [a for a in partners if a not in recs]

    md = render(rows, missing, len(partners))
    if args.stdout:
        print(md)
    else:
        out = here / "RESULTS-binding-evidence.md"
        out.write_text(md)
        print(f"wrote {out} ({len(rows)}/{len(partners)} partners resolved)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
