"""Read ARHGEF15's measured substrate specificity out of Müller et al. 2020's free supplement.

PMID:32203420 (Nat Cell Biol 2020) is a family-wide RhoGEF/RhoGAP substrate-specificity
screen. Reactome cites it as the evidence for ARHGEF15 in BOTH "RHOA GEFs activate RHOA"
(R-HSA-8980691) and "CDC42 GEFs activate CDC42" (R-HSA-9013159). The paper is paywalled and
Europe PMC has no PMC record, so the cached publication is abstract-only -- but the
supplementary tables are freely downloadable from Springer, and Supplementary Table 2 holds
the per-gene screen result. This is absent from ARHGEF15's GOA entirely.

Read-controls, not decoration: the script also reads GEFs whose specificity is textbook
(TIAM1 = Rac1; ARHGEF1/ARHGEF11/ARHGEF12 = RhoA; FGD1/ITSN1 = Cdc42) and asserts they come
out right. If the column mapping were wrong, those would break before ARHGEF15 did. The
gene is located by NAME, never by row number.

Only the screen columns (which contain plain '+'/'-') are interpreted. The literature-review
columns use a third code, 'c', whose legend is not in the freely available spreadsheet, so
this script reports those verbatim and draws no conclusion from them.

Usage:
    uv run --no-project --with openpyxl python muller2020_specificity.py
    uv run --no-project --with openpyxl python muller2020_specificity.py --self-test
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.request

import openpyxl

HERE = pathlib.Path(__file__).parent
CACHE = HERE / "muller2020_supplementary_tables.xlsx"
OUT = HERE / "muller2020_specificity.json"

URL = (
    "https://media.springernature.com/original/springer-static/esm/"
    "art%3A10.1038%2Fs41556-020-0488-x/MediaObjects/41556_2020_488_MOESM3_ESM.xlsx"
)
SHEET = "Supplementary Table 2"
TARGET = "ARHGEF15"

# gene -> the GTPase the screen is expected to score '+' for, from established literature.
# These are read-controls on the COLUMN MAPPING, not on ARHGEF15.
#
# ITSN1 is included and does NOT recover: a textbook Cdc42 GEF scores negative for all three.
# That is kept in the panel on purpose. It is not a bug in this script -- it is the screen's
# own false-negative rate made visible, and it is the reason a '-' in this table is weak
# evidence while a '+' is a positive detection. Dropping it would hide exactly the caveat
# that governs how the ARHGEF15 row may be read.
READ_CONTROLS = {
    "TIAM1": {"Rac1"},
    "ARHGEF1": {"RhoA"},
    "ARHGEF11": {"RhoA"},
    "ARHGEF12": {"RhoA"},
    "FGD1": {"Cdc42"},
    "ITSN1": {"Cdc42"},
}


def download() -> pathlib.Path:
    if not CACHE.exists():
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=300) as fh:
            CACHE.write_bytes(fh.read())
    return CACHE


def load_sheet():
    wb = openpyxl.load_workbook(download())
    if SHEET not in wb.sheetnames:
        sys.exit(f"sheet {SHEET!r} absent; sheets are {wb.sheetnames}")
    return wb[SHEET]


def column_map(ws) -> dict[str, dict[str, str]]:
    """Locate the screen block by reading the two header rows, not by hardcoding letters.

    Row 2 carries merged block titles ('RhoGEF/RhoGAP activity screen', 'Literature
    review', ...); row 4 carries the GTPase name under each column.
    """
    blocks: dict[str, tuple[int, int]] = {}
    for rng in ws.merged_cells.ranges:
        if rng.min_row == 2:
            title = ws.cell(row=2, column=rng.min_col).value
            if title:
                blocks[str(title)] = (rng.min_col, rng.max_col)
    for col in range(1, ws.max_column + 1):
        v = ws.cell(row=2, column=col).value
        if v and str(v) not in blocks:
            blocks[str(v)] = (col, col)

    out: dict[str, dict[str, str]] = {}
    for title, (lo, hi) in blocks.items():
        cols = {}
        for col in range(lo, hi + 1):
            name = ws.cell(row=4, column=col).value
            if name:
                cols[str(name)] = ws.cell(row=4, column=col).coordinate[:-1]
        if cols:
            out[title] = cols
    return out


def gene_rows(ws) -> dict[str, list[int]]:
    rows: dict[str, list[int]] = {}
    for r in range(5, ws.max_row + 1):
        name = ws.cell(row=r, column=1).value
        if name:
            rows.setdefault(str(name).strip(), []).append(r)
    return rows


def read_gene(ws, blocks, rows, gene: str) -> dict:
    if gene not in rows:
        return {"gene": gene, "error": "not present in Supplementary Table 2"}
    if len(rows[gene]) != 1:
        return {"gene": gene, "error": f"{len(rows[gene])} rows ({rows[gene]}); ambiguous"}
    r = rows[gene][0]
    screen = {
        gtp: ws[f"{col}{r}"].value
        for gtp, col in blocks["RhoGEF/RhoGAP activity screen"].items()
        if gtp in ("RhoA", "Rac1", "Cdc42")
    }
    lit = {}
    for sub, cols in blocks.items():
        if sub == "RhoGEF/RhoGAP activity screen":
            continue
        for gtp, col in cols.items():
            if gtp in ("RhoA", "Rac1", "Cdc42"):
                lit.setdefault(sub, {})[gtp] = ws[f"{col}{r}"].value
    refs = [
        ws.cell(row=r, column=c).value
        for c in range(1, ws.max_column + 1)
        if ws.cell(row=2, column=c).value == "reference PMID"
        or (blocks.get("reference PMID") and False)
    ]
    # reference PMIDs sit in the merged 'reference PMID' block
    ref_block = next((rng for rng in ws.merged_cells.ranges if rng.min_row == 2
                      and ws.cell(row=2, column=rng.min_col).value == "reference PMID"), None)
    if ref_block is not None:
        refs = [
            ws.cell(row=r, column=c).value
            for c in range(ref_block.min_col, ref_block.max_col + 1)
            if ws.cell(row=r, column=c).value is not None
        ]
    return {
        "gene": gene,
        "row": r,
        "kind": ws.cell(row=r, column=2).value,
        "screen": screen,
        "screen_positive_for": sorted(g for g, v in screen.items() if v == "+"),
        "literature_blocks_verbatim": lit,
        "reference_pmids": [str(x) for x in refs],
    }


def interactome_and_localization() -> dict:
    """Two secondary readouts from the same workbook, both bearing on the CC annotations.

    Table 3 is the RhoGEF/RhoGAP AP-MS interactome; Table 4 is the localization call.
    Reported as-is, with no interpretation beyond counting.
    """
    wb = openpyxl.load_workbook(download())
    out: dict = {}

    t3 = next((wb[s] for s in wb.sheetnames if s.strip() == "Supplementary Table 3"), None)
    if t3 is not None:
        hdr = {str(c.value): c.column for c in t3[2] if c.value}
        preys = []
        for r in range(3, t3.max_row + 1):
            if t3.cell(row=r, column=hdr["Bait"]).value == TARGET:
                preys.append(
                    {
                        "confidence": t3.cell(row=r, column=hdr["CONFIDENCE"]).value,
                        "prey": t3.cell(row=r, column=hdr["Prey"]).value,
                        "description": t3.cell(row=r, column=hdr["PreyDescription"]).value,
                        "actin_binding_prey": t3.cell(row=r, column=hdr["ActinbindingPrey"]).value,
                    }
                )
        out["interactome"] = {
            "n_total": len(preys),
            "gold": [p for p in preys if p["confidence"] == "GOLD"],
            "n_by_confidence": {
                c: sum(1 for p in preys if p["confidence"] == c)
                for c in sorted({p["confidence"] for p in preys})
            },
        }

    t4 = next((wb[s] for s in wb.sheetnames if s.strip() == "Supplementary Table 4"), None)
    if t4 is not None:
        hdr = {str(c.value): c.column for c in t4[2] if c.value}
        for r in range(3, t4.max_row + 1):
            if t4.cell(row=r, column=1).value == TARGET:
                out["localization_row"] = {
                    str(k): t4.cell(row=r, column=v).value for k, v in hdr.items()
                }
                break
    return out


def analyse() -> dict:
    ws = load_sheet()
    blocks = column_map(ws)
    rows = gene_rows(ws)
    res = {
        "source": {"pmid": "PMID:32203420", "sheet": SHEET, "url": URL},
        "n_genes_in_table": len(rows),
        "target": read_gene(ws, blocks, rows, TARGET),
        "read_controls": {g: read_gene(ws, blocks, rows, g) for g in READ_CONTROLS},
        "secondary": interactome_and_localization(),
    }
    res["read_controls_ok"] = {
        g: set(res["read_controls"][g].get("screen_positive_for") or []) == expected
        for g, expected in READ_CONTROLS.items()
    }
    res["column_mapping_corroborated"] = mapping_corroborated(res)
    return res


def mapping_corroborated(res: dict) -> dict:
    """The property the controls actually establish: each GTPase column is where we think.

    A single control per column suffices for that, and requiring ALL controls to recover
    would conflate a mapping error with the screen's own sensitivity. The mutation test
    below shows this narrowed predicate still fails when the columns are shifted.
    """
    per_gtpase: dict[str, bool] = {}
    for gtpase in ("RhoA", "Rac1", "Cdc42"):
        expected_here = [g for g, exp in READ_CONTROLS.items() if exp == {gtpase}]
        per_gtpase[gtpase] = any(res["read_controls_ok"][g] for g in expected_here)
    return {
        "per_gtpase": per_gtpase,
        "all_three_corroborated": all(per_gtpase.values()),
        "controls_not_recovered": [g for g, ok in res["read_controls_ok"].items() if not ok],
    }


def self_test() -> int:
    failures = []

    def expect(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
        if not ok:
            failures.append(name)

    res = analyse()
    ws = load_sheet()
    blocks = column_map(ws)
    rows = gene_rows(ws)

    print("read-controls (reported for all; the PASS criterion is the narrowed predicate below):")
    for g, expected in READ_CONTROLS.items():
        got = res["read_controls"][g].get("screen_positive_for")
        print(f"   {'recovered' if res['read_controls_ok'][g] else 'NOT recovered'}: "
              f"{g} expected {sorted(expected)}, screen says {got}")
    expect(
        "each GTPase column is corroborated by at least one control",
        res["column_mapping_corroborated"]["all_three_corroborated"],
        str(res["column_mapping_corroborated"]["per_gtpase"]),
    )
    expect(
        "ITSN1 is the only control not recovered, i.e. the known screen false negative",
        res["column_mapping_corroborated"]["controls_not_recovered"] == ["ITSN1"],
        str(res["column_mapping_corroborated"]["controls_not_recovered"]),
    )

    print("guards:")
    expect("the table has the expected scale (>100 GEF/GAP genes)", res["n_genes_in_table"] > 100,
           str(res["n_genes_in_table"]))
    expect("ARHGEF15 appears exactly once", "error" not in res["target"], str(res["target"].get("error")))
    expect("every ARHGEF15 screen cell is a plain +/- call",
           set(res["target"]["screen"].values()) <= {"+", "-"}, str(res["target"]["screen"]))

    print("mutation tests:")
    # A gene that is genuinely absent must be reported as absent, not silently defaulted.
    absent = read_gene(ws, blocks, rows, "NOT_A_REAL_GENE_XYZ")
    expect("an absent gene is reported as an error, not as an empty result",
           absent.get("error") == "not present in Supplementary Table 2", str(absent))
    # The control predicate must be able to return False.
    expect("the control predicate returns False for a deliberately wrong expectation",
           set(res["read_controls"]["TIAM1"]["screen_positive_for"]) != {"RhoA"},
           f"TIAM1={res['read_controls']['TIAM1']['screen_positive_for']}")
    # Locating by name, not row: ARHGEF15's row must be whatever the name search finds.
    expect("the target row is found by name and carries that name",
           ws.cell(row=res["target"]["row"], column=1).value == TARGET,
           f"row {res['target']['row']}")

    # The narrowed corroboration predicate must still fail on a shifted column mapping.
    # This is the hole that narrowing "all controls recover" could have opened.
    shifted = {
        "read_controls_ok": {},
        "read_controls": {},
    }
    scr = blocks["RhoGEF/RhoGAP activity screen"]
    order = ["RhoA", "Rac1", "Cdc42"]
    rotated = {order[i]: scr[order[(i + 1) % 3]] for i in range(3)}
    for g, expected in READ_CONTROLS.items():
        r = rows[g][0]
        pos = sorted(gt for gt, col in rotated.items() if ws[f"{col}{r}"].value == "+")
        shifted["read_controls"][g] = {"screen_positive_for": pos}
        shifted["read_controls_ok"][g] = set(pos) == expected
    shifted_corr = mapping_corroborated(shifted)
    expect(
        "rotating the screen columns by one breaks the narrowed corroboration predicate",
        not shifted_corr["all_three_corroborated"],
        str(shifted_corr["per_gtpase"]),
    )

    print()
    if failures:
        print(f"SELF-TEST FAILED: {failures}")
        return 1
    print("SELF-TEST PASSED")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    res = analyse()
    OUT.write_text(json.dumps(res, indent=2, sort_keys=True, default=str) + "\n")
    t = res["target"]
    print(f"Müller et al. 2020 ({res['source']['pmid']}), {SHEET}, row {t['row']} — {t['gene']} ({t['kind']})")
    print(f"  activity screen: {t['screen']}")
    print(f"  positive for:    {t['screen_positive_for']}")
    print(f"  cited PMIDs:     {t['reference_pmids']}")
    print(f"  literature blocks (verbatim, 'c' not interpreted): {t['literature_blocks_verbatim']}")
    print("  read-controls:")
    for g, ok in res["read_controls_ok"].items():
        print(f"    {g:<9} positive_for={res['read_controls'][g]['screen_positive_for']} expected_ok={ok}")
    sec = res.get("secondary", {})
    if "interactome" in sec:
        print(f"  AP-MS interactome (Supplementary Table 3): {sec['interactome']['n_by_confidence']}")
        for p in sec["interactome"]["gold"]:
            print(f"    GOLD  {p['prey']:<10} actin_binding_prey={p['actin_binding_prey']}  {p['description']}")
    if "localization_row" in sec:
        loc = sec["localization_row"]
        print("  localization (Supplementary Table 4):")
        for k in ("listed in", "Cell Atlas localisation", "Uniprot localisation"):
            if k in loc:
                print(f"    {k}: {str(loc[k])[:200]}")
    print(f"\nwrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
