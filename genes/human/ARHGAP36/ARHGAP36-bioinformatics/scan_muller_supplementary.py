"""Read ARHGAP36's row out of Muller et al. 2020's own supplementary tables.

PMID:32203420 (Nat Cell Biol 22:498-511) is the primary source of the negative
functional result on ARHGAP36: a systems-scale screen of every human RhoGEF and RhoGAP
against RHOA, RAC1 and CDC42. The article is **not open access** -- Europe PMC reports
no PMC id, ``isOpenAccess: N``, ``inEPMC: N`` -- so the repository's cached record is
abstract-only. Before this script existed the review could only quote the result
second-hand, through the verbatim sentence in PMID:33999959 that cites it.

The *supplementary tables are freely downloadable* from Springer even though the article
text is not. This script fetches them and reads the row directly, so the review's central
functional claim now rests on a number someone can re-derive rather than on a chain of
citations. It deliberately does **not** produce anything for ``supporting_text``: that
field is validated as a verbatim substring of the cached publication, the cache is
abstract-only, and a quote from a supplementary file would be unverifiable there. The
findings are therefore attached to the PMID:32203420 reference as ``statement``-only
entries -- they are claims about what that paper contains -- with the provenance in its
``reference_review.review_notes`` and the argument in the annotation's ``reason``.

Two tables matter:

* **Supplementary Table 1**, the cDNA library. It records which construct was screened.
  This is what rules out the obvious objection -- that an inactive splice variant was
  tested -- and it also carries the authors' own domain call.
* **Supplementary Table 2**, "RhoGEF/RhoGAP specificities identified in this study and in
  the literature". Columns under the "RhoGEF/RhoGAP activity screen" banner give the per
  GTPase call.

Column positions are **derived, not hardcoded**: the header row is located by its
``GENE NAME`` cell and the RhoA/Rac1/Cdc42 columns are read from the sub-header beneath
the activity-screen banner. A table whose shape has changed is a hard error.

Controls are mandatory. A screen in which nothing scores positive would give ARHGAP36 a
negative for free, so the script requires that the named positive controls score ``+``
somewhere and raises if they do not. It also requires that at least one control is
negative for at least one GTPase, so "everything is positive" cannot pass either.

Usage:
    uv run --no-project --with "openpyxl>=3.1" python scan_muller_supplementary.py
    uv run --no-project --with "openpyxl>=3.1" python scan_muller_supplementary.py --self-test
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

import openpyxl

SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPT_DIR / "cache"

PMID = "32203420"
DOI = "10.1038/s41556-020-0488-x"
ESM_URL = (
    "https://media.springernature.com/original/springer-static/esm/"
    "art%3A10.1038%2Fs41556-020-0488-x/MediaObjects/41556_2020_488_MOESM3_ESM.xlsx"
)

QUERY = "ARHGAP36"
# GAPs the same screen scores positive for at least one GTPase. If these come back all
# negative, the table has been misread and the query's negative means nothing.
#
# ARHGAP17 is deliberately NOT in this list. An earlier version included it, which was
# simply wrong: ARHGAP17/RICH1 scores negative for all three GTPases here despite being a
# characterised Cdc42 GAP. It is the screen's false-negative exemplar, not a positive
# control, and calling it one would have let the "at least one control is positive" guard
# pass on a protein that is evidence for the opposite point.
POSITIVE_CONTROLS = ["ARHGAP35", "ARHGAP1"]
# A GAP with characterised activity that this screen nonetheless scores all-negative. The
# false-negative caveat in the report is an assertion about this protein, so it is checked
# rather than narrated: if ARHGAP17 ever stops being all-negative, the caveat is wrong and
# the run must fail rather than keep printing it.
FALSE_NEGATIVE_EXEMPLAR = "ARHGAP17"
GTPASES = ["RhoA", "Rac1", "Cdc42"]

LIBRARY_SHEET = "Supplementary Table 1"
SPECIFICITY_SHEET = "Supplementary Table 2"


class ScanError(RuntimeError):
    """A hard failure. Never downgraded to a missing section."""


def fetch_esm() -> Path:
    dest = CACHE_DIR / "muller2020_MOESM3.xlsx"
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(ESM_URL, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=300) as fh:
            payload = fh.read()
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        raise ScanError(
            f"could not fetch the supplementary workbook for PMID:{PMID} ({DOI}): {exc}. "
            "There is no offline fallback; re-run with network access."
        ) from exc
    if len(payload) < 10_000 or payload[:2] != b"PK":
        raise ScanError(
            f"the response from Springer is not an xlsx file ({len(payload)} bytes, "
            f"magic {payload[:4]!r}); the ESM URL has probably changed"
        )
    dest.write_bytes(payload)
    return dest


def sheet_rows(path: Path, sheet: str) -> list[list[str]]:
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    if sheet not in wb.sheetnames:
        wb.close()
        raise ScanError(f"workbook has no sheet {sheet!r}; sheets present: {wb.sheetnames}")
    ws = wb[sheet]
    rows = [["" if v is None else str(v).strip() for v in row] for row in ws.iter_rows(values_only=True)]
    wb.close()
    return rows


def find_row(rows: list[list[str]], gene: str) -> tuple[int, list[str]]:
    hits = [(i, r) for i, r in enumerate(rows) if r and r[0].strip().upper() == gene.upper()]
    if not hits:
        raise ScanError(f"{gene} has no row in this sheet")
    if len(hits) > 1:
        raise ScanError(f"{gene} matched {len(hits)} rows; expected exactly 1")
    return hits[0]


def specificity_columns(rows: list[list[str]]) -> dict[str, int]:
    """Locate the activity-screen RhoA/Rac1/Cdc42 columns from the header, not by position."""
    header_idx = next((i for i, r in enumerate(rows) if r and r[0].strip().upper() == "GENE NAME"), None)
    if header_idx is None:
        raise ScanError("no 'GENE NAME' header row found; the sheet layout has changed")
    banner = rows[header_idx - 1] if header_idx > 0 else []
    screen_col = next(
        (i for i, v in enumerate(banner) if "activity screen" in v.lower()),
        None,
    )
    if screen_col is None:
        raise ScanError("no 'RhoGEF/RhoGAP activity screen' banner found above the header")
    sub = rows[header_idx + 1] if header_idx + 1 < len(rows) else []
    cols: dict[str, int] = {}
    for gtpase in GTPASES:
        idx = next((i for i, v in enumerate(sub) if i >= screen_col and v.strip() == gtpase), None)
        if idx is None:
            raise ScanError(f"no column for {gtpase} at or right of the activity-screen banner")
        cols[gtpase] = idx
    if sorted(cols.values()) != list(range(min(cols.values()), min(cols.values()) + 3)):
        raise ScanError(f"the three GTPase columns are not contiguous: {cols}; layout has changed")
    return cols


def read_calls(rows: list[list[str]], cols: dict[str, int], gene: str) -> dict[str, str]:
    _, row = find_row(rows, gene)
    out = {}
    for gtpase, idx in cols.items():
        if idx >= len(row):
            raise ScanError(f"{gene} row is shorter than the {gtpase} column index {idx}")
        val = row[idx].strip()
        if val not in {"+", "-"}:
            raise ScanError(f"{gene}/{gtpase} holds {val!r}, which is neither '+' nor '-'")
        out[gtpase] = val
    return out


def run(rows_override: dict[str, list[list[str]]] | None = None) -> dict[str, Any]:
    path = fetch_esm()
    spec = (rows_override or {}).get(SPECIFICITY_SHEET) or sheet_rows(path, SPECIFICITY_SHEET)
    lib = (rows_override or {}).get(LIBRARY_SHEET) or sheet_rows(path, LIBRARY_SHEET)

    cols = specificity_columns(spec)
    calls = {gene: read_calls(spec, cols, gene) for gene in [QUERY] + POSITIVE_CONTROLS + [FALSE_NEGATIVE_EXEMPLAR]}

    # The report asserts that this screen has false negatives, naming this protein. Check
    # it rather than narrate it.
    if any(v == "+" for v in calls[FALSE_NEGATIVE_EXEMPLAR].values()):
        raise ScanError(
            f"{FALSE_NEGATIVE_EXEMPLAR} is not all-negative in this table "
            f"({calls[FALSE_NEGATIVE_EXEMPLAR]}), so the false-negative caveat the report prints "
            "about it is no longer true; fix the caveat rather than keep printing it"
        )

    # Controls. Without these the query's negative is worthless.
    any_positive = [g for g in POSITIVE_CONTROLS if "+" in calls[g].values()]
    if not any_positive:
        raise ScanError(
            f"none of the positive controls {POSITIVE_CONTROLS} scores '+' for any GTPase; "
            "the screen column has been misidentified and the query's negative is meaningless"
        )
    any_negative = [g for g in POSITIVE_CONTROLS if "-" in calls[g].values()]
    if not any_negative:
        raise ScanError(
            "every control is positive for every GTPase, so '-' carries no information here"
        )

    # The construct that was screened, from the library table.
    lib_header_idx = next((i for i, r in enumerate(lib) if r and r[0].strip().upper() == "GENE NAME"), None)
    if lib_header_idx is None:
        raise ScanError(f"no 'Gene Name' header in {LIBRARY_SHEET!r}")
    lib_header = lib[lib_header_idx]
    _, lib_row = find_row(lib, QUERY)
    library = {}
    for key in ("GEF or GAP (or GAP-like)", "size of construct in library (aa)", "Comments", "Species in library"):
        idx = next((i for i, v in enumerate(lib_header) if v.strip() == key), None)
        if idx is None:
            raise ScanError(f"{LIBRARY_SHEET} has no column {key!r}; layout has changed")
        library[key] = lib_row[idx] if idx < len(lib_row) else ""

    # How much is a negative worth in this screen? Counted, not assumed. ARHGAP17/RICH1
    # is a characterised Cdc42 GAP and scores all-negative here, so the assay plainly has
    # false negatives; the honest way to use the query's negative is alongside a measured
    # rate rather than as if it were a clean refutation.
    header_idx = next(i for i, r in enumerate(spec) if r and r[0].strip().upper() == "GENE NAME")
    type_col = 1
    gap_rows = []
    for r in spec[header_idx + 2 :]:
        if not r or not r[0].strip() or r[0].strip().upper() == "GENE NAME":
            continue
        kind = r[type_col].strip() if len(r) > type_col else ""
        if "GAP" not in kind.upper():
            continue
        vals = [r[c].strip() if c < len(r) else "" for c in cols.values()]
        if any(v not in {"+", "-"} for v in vals):
            continue
        gap_rows.append((r[0].strip(), kind, vals))
    if len(gap_rows) < 20:
        raise ScanError(f"only {len(gap_rows)} scorable GAP rows found; the sheet is not being read correctly")
    all_negative = [g for g, _k, v in gap_rows if all(x == "-" for x in v)]

    return {
        "pmid": PMID,
        "doi": DOI,
        "esm_url": ESM_URL,
        "specificity_columns": cols,
        "calls": calls,
        "query_all_negative": all(v == "-" for v in calls[QUERY].values()),
        "positive_controls_scoring_positive": any_positive,
        "controls_scoring_negative_somewhere": any_negative,
        "library": library,
        "screen_scope": {
            "scorable_gap_rows": len(gap_rows),
            "all_negative_rows": len(all_negative),
            "all_negative_fraction": round(len(all_negative) / len(gap_rows), 4),
            "all_negative_genes": sorted(all_negative),
        },
        "residue_agreement": residue_agreement(sorted(all_negative), [g for g, _k, v in gap_rows]),
    }


def residue_agreement(all_negative: list[str], scorable: list[str]) -> dict[str, Any]:
    """Do the screen's all-negative genes coincide with the arginine-finger-less ones?

    The two measurements are independent -- one is a functional assay, the other is a
    residue read off a sequence -- so their agreement is the thing that makes a single
    negative call worth something. The arginine-finger-less set is NOT written here: it
    is read from ``results.json``, the output of ``analyze_arhgap36.py`` in this
    directory, which derives it from all reviewed human PROSITE PS50238 proteins.
    """
    src = SCRIPT_DIR / "results.json"
    if not src.exists():
        raise ScanError(
            f"{src} is missing. Run `analyze_arhgap36.py` first: this cross-check reads the "
            "arginine-finger census from it rather than restating it here."
        )
    res = json.loads(src.read_text())
    flagged = res.get("family", {}).get("flagged")
    if not flagged:
        raise ScanError("results.json carries no family.flagged list; re-run analyze_arhgap36.py")
    # UniProt entry names (RHG36_HUMAN) -> gene symbols the screen uses. Mapped through
    # the UniProt record so no symbol is guessed.
    symbols: dict[str, str] = {}
    for row in flagged:
        acc = row["accession"]
        raw = _fetch_uniprot_json(acc)
        genes = raw.get("genes") or []
        name = (genes[0].get("geneName") or {}).get("value") if genes else None
        if not name:
            raise ScanError(f"UniProt {acc} has no gene name; cannot align it to the screen")
        symbols[acc] = name
    finger_less = sorted(symbols.values())
    scorable_set = {g.upper() for g in scorable}
    in_screen = [g for g in finger_less if g.upper() in scorable_set]
    neg_set = {g.upper() for g in all_negative}
    agree = [g for g in in_screen if g.upper() in neg_set]
    return {
        "arginine_finger_less": finger_less,
        "present_in_screen": in_screen,
        "of_those_all_negative": agree,
        "agreement": f"{len(agree)}/{len(in_screen)}" if in_screen else "0/0",
    }


def _fetch_uniprot_json(acc: str) -> dict[str, Any]:
    dest = CACHE_DIR / f"{acc}.json"
    if dest.exists() and dest.stat().st_size > 0:
        return json.loads(dest.read_bytes())
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json", headers={"Accept": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as fh:
            payload = fh.read()
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        raise ScanError(f"could not fetch UniProt {acc}: {exc}") from exc
    dest.write_bytes(payload)
    return json.loads(payload)


def self_test() -> int:
    failures: list[str] = []

    def check(label: str, cond: bool, detail: str = "") -> None:
        if cond:
            print(f"  ok    {label}")
        else:
            failures.append(label)
            print(f"  FAIL  {label}: {detail}")

    print("self-test")
    base = run()
    check(
        f"baseline: {QUERY} is negative for all three GTPases in the activity screen",
        base["query_all_negative"],
        json.dumps(base["calls"][QUERY]),
    )
    check(
        "baseline: at least one positive control scores '+' (the screen can detect activity)",
        bool(base["positive_controls_scoring_positive"]),
        json.dumps({g: base["calls"][g] for g in POSITIVE_CONTROLS}),
    )
    check(
        "baseline: at least one control scores '-' somewhere ('-' is informative)",
        bool(base["controls_scoring_negative_somewhere"]),
        "",
    )
    check(
        "baseline: the screened construct is recorded as human",
        base["library"]["Species in library"].strip().lower() == "human",
        base["library"]["Species in library"],
    )

    path = fetch_esm()
    spec = sheet_rows(path, SPECIFICITY_SHEET)

    # Mutation 1: blank the query's calls. The reader must refuse rather than default.
    idx, row = find_row(spec, QUERY)
    mutated = [list(r) for r in spec]
    for c in base["specificity_columns"].values():
        mutated[idx][c] = ""
    try:
        run(rows_override={SPECIFICITY_SHEET: mutated})
    except ScanError as exc:
        check("mutation: an empty call cell is refused, not read as negative", "neither '+' nor '-'" in str(exc), str(exc))
    else:
        check("mutation: an empty call cell is refused, not read as negative", False, "no error raised")

    # Mutation 2: make every control negative. The query's negative must stop meaning anything.
    mutated2 = [list(r) for r in spec]
    for gene in POSITIVE_CONTROLS:
        i, _ = find_row(spec, gene)
        for c in base["specificity_columns"].values():
            mutated2[i][c] = "-"
    try:
        run(rows_override={SPECIFICITY_SHEET: mutated2})
    except ScanError as exc:
        check("mutation: an all-negative control set is refused", "positive controls" in str(exc), str(exc))
    else:
        check("mutation: an all-negative control set is refused", False, "no error raised")

    # Mutation 3: make every control positive for everything.
    mutated3 = [list(r) for r in spec]
    for gene in POSITIVE_CONTROLS:
        i, _ = find_row(spec, gene)
        for c in base["specificity_columns"].values():
            mutated3[i][c] = "+"
    try:
        run(rows_override={SPECIFICITY_SHEET: mutated3})
    except ScanError as exc:
        check("mutation: an all-positive control set is refused", "carries no information" in str(exc), str(exc))
    else:
        check("mutation: an all-positive control set is refused", False, "no error raised")

    # Mutation 4: break the header so column positions cannot be derived.
    mutated4 = [list(r) for r in spec]
    hi = next(i for i, r in enumerate(spec) if r and r[0].strip().upper() == "GENE NAME")
    mutated4[hi][0] = "GENE"
    try:
        run(rows_override={SPECIFICITY_SHEET: mutated4})
    except ScanError as exc:
        check("mutation: a changed header is refused rather than guessed around", "GENE NAME" in str(exc), str(exc))
    else:
        check("mutation: a changed header is refused rather than guessed around", False, "no error raised")

    # Mutation 5: the false-negative caveat is an assertion about ARHGAP17. If that
    # protein stops being all-negative the caveat is false, and the run must fail rather
    # than keep printing it.
    mutated6 = [list(r) for r in spec]
    i, _ = find_row(spec, FALSE_NEGATIVE_EXEMPLAR)
    mutated6[i][base["specificity_columns"]["Cdc42"]] = "+"
    try:
        run(rows_override={SPECIFICITY_SHEET: mutated6})
    except ScanError as exc:
        check(
            "mutation: a no-longer-all-negative false-negative exemplar invalidates the caveat",
            "false-negative caveat" in str(exc),
            str(exc),
        )
    else:
        check("mutation: a no-longer-all-negative false-negative exemplar invalidates the caveat", False, "no error raised")

    # Negative control: an edit to an unrelated row must change nothing.
    mutated5 = [list(r) for r in spec]
    i, _ = find_row(spec, "ARHGAP39")
    for c in base["specificity_columns"].values():
        mutated5[i][c] = "+"
    res = run(rows_override={SPECIFICITY_SHEET: mutated5})
    check(
        "negative control: editing an unrelated gene's row leaves the query's calls unchanged",
        res["calls"][QUERY] == base["calls"][QUERY],
        f"{res['calls'][QUERY]} != {base['calls'][QUERY]}",
    )

    print("PASS" if not failures else f"{len(failures)} FAILURE(S)")
    return 0 if not failures else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    res = run()
    print(f"source: PMID:{res['pmid']} supplementary workbook (not open access; ESM is)")
    print(f"        {res['esm_url']}")
    print()
    print(f"{SPECIFICITY_SHEET}, RhoGEF/RhoGAP activity screen columns {res['specificity_columns']}:")
    for gene, calls in res["calls"].items():
        if gene == QUERY:
            mark = "<-- query"
        elif gene == FALSE_NEGATIVE_EXEMPLAR:
            mark = "    false-negative exemplar (characterised Cdc42 GAP)"
        else:
            mark = "    positive control"
        print(f"  {gene:12s} " + "  ".join(f"{g}={v}" for g, v in calls.items()) + f"   {mark}")
    print()
    print(f"{LIBRARY_SHEET}, the construct that was screened:")
    for k, v in res["library"].items():
        print(f"  {k}: {v}")
    print()
    sc = res["screen_scope"]
    print("How much is a negative worth here? (counted, not assumed)")
    print(f"  scorable GAP rows in the screen:     {sc['scorable_gap_rows']}")
    print(f"  scoring negative for all three:      {sc['all_negative_rows']} ({sc['all_negative_fraction']:.0%})")
    print("  The screen has false negatives -- ARHGAP17/RICH1, a characterised Cdc42 GAP,")
    print("  is among the all-negative rows. So this result is corroboration, not proof;")
    print("  the review states that and does not rest on it alone.")
    print()
    ra = res["residue_agreement"]
    print("Do the screen's negatives coincide with the arginine-finger-less proteins?")
    print(f"  arginine-finger-less (from results.json): {ra['arginine_finger_less']}")
    print(f"  of those, present in the screen:          {ra['present_in_screen']}")
    print(f"  of those, all-negative in the screen:     {ra['of_those_all_negative']}  ({ra['agreement']})")
    print("  Two independent measurements -- a functional assay and a residue read off a")
    print("  sequence -- agreeing on the same set is what makes one negative call worth")
    print("  something despite the screen's overall false-negative rate.")
    print("  Not six independent observations, though: OCRL and INPP5B are paralogous")
    print("  inositol polyphosphate 5-phosphatases, so two of the four agreeing entries are")
    print("  not independent of each other and the effective n is smaller than the ratio.")
    print()
    print(f"{QUERY} negative for all three GTPases: {res['query_all_negative']}")
    (SCRIPT_DIR / "muller2020_arhgap36.json").write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    print(f"wrote {SCRIPT_DIR / 'muller2020_arhgap36.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
