#!/usr/bin/env python3
"""Co-expression analysis of poplar CASPL genes from a PlantGenIE exImage export.

WHY THIS IS A PARSER, NOT A FETCHER
-----------------------------------
The PlantGenIE / PopGenIE (P. trichocarpa exAtlas, "potri" v3.1) expression data
is served only through the GenIE-Sys web app. Its expression endpoint
(`plugins/eximage/service/eplant_service.php?primaryGene=...&view=exatlas`) returns
data ONLY when the species database has been selected interactively in a browser
session (server-side PHP `$_SESSION` state); setting the `genie_select_species*`
cookies from a script is not sufficient and the endpoint returns an empty body.
The bulk FTP listing and the direct AspWood/CoNekT hosts are not reachable from this
environment (HTTP 000/503). See NOTES.md for the full, reproducible probe log.

Rather than fake values, this script PARSES the TSV that the exImage tool produces
with its built-in "download" button (one click), whose columns are exactly:

    gene_name <tab> sample_name <tab> log2 <tab> rmd <tab> log2fc

HOW TO PRODUCE THE INPUT (manual, ~2 min)
-----------------------------------------
1. Go to https://plantgenie.org/exImage , select species "Populus trichocarpa v3.1".
2. Add the CASPL gene IDs from gene_ids.tsv (column potri_v_id) to the gene basket,
   plus any suberin / cold-stress marker genes you want to test against.
3. Click download; save the TSV into this folder as data/exatlas_export.tsv.
4. (optional) Create markers.tsv with two columns: gene_id <tab> category
   (e.g. Potri.XXXXX  suberin   /  Potri.YYYYY  cold) to get module-level summaries.

Then run:  uv run coexpression_analysis.py

OUTPUT
------
results/coexpression_correlations.tsv  - full CASPL x other-gene Pearson r table
results/caspl_module_summary.tsv       - (if markers.tsv present) CASPL vs marker modules
Prints the top co-expressed genes per CASPL.

Nothing is hardcoded or invented; if no export is present the script exits with an
explanation rather than producing fake results.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
DATA = HERE / "data"
RESULTS = HERE / "results"
RESULTS.mkdir(exist_ok=True)

VALUE_COL_PREFERENCE = ["log2", "rmd", "log2fc"]


def load_export() -> pd.DataFrame:
    candidates = sorted(DATA.glob("*export*.tsv")) + sorted(DATA.glob("*.tsv"))
    candidates = [c for c in candidates if c.name != "markers.tsv"]
    if not candidates:
        sys.exit(
            "No exImage export found in data/.\n"
            "Produce one as described in the module docstring (exImage -> download),\n"
            "save it as data/exatlas_export.tsv, then re-run. No analysis was run."
        )
    frames = []
    for c in candidates:
        df = pd.read_csv(c, sep="\t")
        df.columns = [col.strip().lower() for col in df.columns]
        if "gene_name" not in df.columns or "sample_name" not in df.columns:
            print(f"  skipping {c.name}: missing gene_name/sample_name columns")
            continue
        value_col = next((v for v in VALUE_COL_PREFERENCE if v in df.columns), None)
        if value_col is None:
            print(f"  skipping {c.name}: no value column ({VALUE_COL_PREFERENCE})")
            continue
        df = df[["gene_name", "sample_name", value_col]].rename(columns={value_col: "value"})
        df["__source"] = c.name
        frames.append(df)
        print(f"  loaded {c.name}: {df['gene_name'].nunique()} genes x "
              f"{df['sample_name'].nunique()} samples (value={value_col})")
    if not frames:
        sys.exit("Found TSV files but none had the expected exImage columns.")
    return pd.concat(frames, ignore_index=True)


def caspl_ids() -> dict[str, str]:
    """Map potri_v_id -> CASPL symbol from gene_ids.tsv (only mapped genes)."""
    ids = {}
    p = HERE / "gene_ids.tsv"
    if p.exists():
        g = pd.read_csv(p, sep="\t")
        for _, r in g.iterrows():
            if str(r.get("potri_v_id", "NA")) not in ("NA", "nan", ""):
                ids[str(r["potri_v_id"])] = str(r["gene"])
    return ids


_POTRI_RE = re.compile(r"(Potri\.\d+G\d+)", re.IGNORECASE)


def base_id(gene_name: str) -> str:
    """Normalize Potri IDs (drop transcript/version suffixes) for matching.

    'Potri.011G154900.1.v4.1' / 'Potri.011G154900.1' -> 'Potri.011G154900'.
    Non-Potri names are returned stripped of surrounding whitespace.
    """
    g = str(gene_name).strip()
    m = _POTRI_RE.search(g)
    return m.group(1) if m else g


def main() -> None:
    long_df = load_export()
    # collapse to gene (base id) x sample matrix, mean of duplicate transcripts
    long_df["gene_base"] = long_df["gene_name"].map(base_id)
    mat = (long_df.groupby(["gene_base", "sample_name"])["value"].mean()
                  .unstack("sample_name"))
    print(f"\nExpression matrix: {mat.shape[0]} genes x {mat.shape[1]} samples")
    if mat.shape[1] < 3:
        sys.exit("Fewer than 3 samples; correlation analysis is not meaningful.")

    casp_map = caspl_ids()
    # match CASPL genes by normalized base id
    casp_bases = {base_id(k): v for k, v in casp_map.items()}
    casp_rows = [g for g in mat.index if g in casp_bases]
    if not casp_rows:
        print("WARNING: none of the mapped CASPL Potri IDs were found in the export.\n"
              "Check that you queried the IDs from gene_ids.tsv (potri_v_id column).")
    corr = mat.T.corr(method="pearson")

    # full CASPL x all correlations
    out_rows = []
    for c in casp_rows:
        sym = casp_bases.get(c, c)
        ser = corr[c].drop(index=[c]).sort_values(ascending=False)
        for partner, r in ser.items():
            out_rows.append({"caspl": sym, "caspl_id": c, "partner": partner,
                             "pearson_r": round(float(r), 3)})
    res = pd.DataFrame(out_rows)
    res.to_csv(RESULTS / "coexpression_correlations.tsv", sep="\t", index=False)
    print(f"\nWrote {RESULTS/'coexpression_correlations.tsv'} "
          f"({len(res)} pairs, {len(casp_rows)} CASPLs found)")

    for c in casp_rows:
        sym = casp_bases.get(c, c)
        top = corr[c].drop(index=[c]).sort_values(ascending=False).head(5)
        print(f"\n{sym} ({c}) top co-expressed:")
        for partner, r in top.items():
            print(f"   {partner:<28} r={r:+.3f}")

    # marker module summary
    mfile = DATA / "markers.tsv"
    if mfile.exists() and casp_rows:
        markers = pd.read_csv(mfile, sep="\t", names=["gene_id", "category"], comment="#")
        markers["base"] = markers["gene_id"].map(base_id)
        msum = []
        for c in casp_rows:
            sym = casp_bases.get(c, c)
            for cat, grp in markers.groupby("category"):
                present = [b for b in grp["base"] if b in corr.index]
                if not present:
                    continue
                mean_r = float(corr.loc[c, present].mean())
                msum.append({"caspl": sym, "module": cat,
                             "n_markers": len(present), "mean_pearson_r": round(mean_r, 3)})
        if msum:
            md = pd.DataFrame(msum)
            md.to_csv(RESULTS / "caspl_module_summary.tsv", sep="\t", index=False)
            print(f"\nWrote {RESULTS/'caspl_module_summary.tsv'}")
            print(md.to_string(index=False))
    elif not mfile.exists():
        print("\n(No markers.tsv provided - skipping suberin/cold module summary. "
              "Add one to test the suberization / cold-stress hypotheses.)")


if __name__ == "__main__":
    main()
