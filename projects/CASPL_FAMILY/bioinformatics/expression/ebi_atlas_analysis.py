#!/usr/bin/env python3
"""Real poplar expression analysis for the CASPL genes, from EBI Expression Atlas.

Unlike the PlantGenIE route (session-gated; see NOTES.md), EBI Expression Atlas
publishes processed matrices over an open FTP, keyed by EnsemblPlants P. trichocarpa
gene IDs (`POPTR_<chr>G<num>v3`), which map 1:1 from the UniProt `Potri.<chr>G<num>`
IDs in gene_ids.tsv. So this analysis is fully programmatic and reproducible.

Datasets:
  * E-MTAB-5540  (differential)  RNA-seq of poplar root / stem xylem / vascular leaf
        under cold, drought, heat, salt (short-term & prolonged) vs control.
        -> tests the CASPL4C "cold" hypothesis and general stress responsiveness.
  * E-GEOD-81077 (baseline)      RNA-seq across leaf, phloem, primary root, shoot apex
        and xylem cell types.
        -> tests tissue specificity (e.g. CASPL1B/1D root/endodermis suberization
           hypothesis; xylem-associated CASPLs).

Outputs (results/):
  caspl_stress_log2fc.tsv     long table: gene x contrast -> log2FC, p, significant?
  caspl_stress_significant.tsv  only |log2FC|>=1 & p<0.05
  caspl_baseline_tpm.tsv      gene x tissue TPM + peak tissue
Prints a summary. Downloads to data/ebi/ (gitignored) if not already present.
Nothing is fabricated; if a download fails the script reports it and stops.
"""
from __future__ import annotations

import csv
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data" / "ebi"
RESULTS = HERE / "results"
DATA.mkdir(parents=True, exist_ok=True)
RESULTS.mkdir(exist_ok=True)

FTP = "https://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments"
FILES = {
    "stress_analytics": f"{FTP}/E-MTAB-5540/E-MTAB-5540-analytics.tsv",
    "stress_config": f"{FTP}/E-MTAB-5540/E-MTAB-5540-configuration.xml",
    "baseline_tpms": f"{FTP}/E-GEOD-81077/E-GEOD-81077-tpms.tsv",
    "baseline_config": f"{FTP}/E-GEOD-81077/E-GEOD-81077-configuration.xml",
}
SIG_P, SIG_LFC = 0.05, 1.0


def fetch(key: str) -> Path:
    dest = DATA / (key + (".xml" if "config" in key else ".tsv"))
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    url = FILES[key]
    print(f"  downloading {key} ...")
    try:
        urllib.request.urlretrieve(url, dest)
    except Exception as e:  # noqa: BLE001
        sys.exit(f"Download failed for {url}: {e}\nNo analysis run.")
    return dest


def potri_to_ensembl() -> dict[str, str]:
    """POPTR_..v3 -> CASPL symbol, from gene_ids.tsv (mapped genes only)."""
    out = {}
    p = HERE / "gene_ids.tsv"
    with open(p) as fh:
        rdr = csv.DictReader(fh, delimiter="\t")
        for r in rdr:
            pid = r.get("potri_v_id", "NA")
            if pid and pid != "NA":
                ens = "POPTR_" + pid.split("Potri.")[1] + "v3"
                out[ens] = r["gene"]
    return out


def contrast_names(xml: Path) -> dict[str, str]:
    t = xml.read_text()
    cmap = {}
    for m in re.finditer(r'<contrast id="([^"]+)"[^>]*>.*?<name>(.*?)</name>', t, re.S):
        cmap[m.group(1)] = m.group(2).strip().replace("'", "")
    return cmap


def assay_labels(xml: Path) -> dict[str, str]:
    t = xml.read_text()
    return dict(re.findall(r'<assay_group id="(g\d+)"[^>]*label="([^"]*)"', t))


def stress_analysis(ens2sym: dict[str, str]) -> None:
    analytics = fetch("stress_analytics")
    cmap = contrast_names(fetch("stress_config"))
    with open(analytics) as fh:
        rdr = csv.reader(fh, delimiter="\t")
        hdr = next(rdr)
        lfc_cols = {i: hdr[i].split(".")[0] for i, h in enumerate(hdr)
                    if h.endswith(".log2foldchange")}
        rows = {ens2sym[r[0]]: r for r in rdr if r[0] in ens2sym}

    long_rows, sig_rows = [], []
    for sym, r in sorted(rows.items()):
        for i, cid in lfc_cols.items():
            lfc, pv = r[i], r[i - 1]
            if lfc in ("", "NA") or pv in ("", "NA"):
                continue
            lfc_f, pv_f = float(lfc), float(pv)
            cond = cmap.get(cid, cid)
            sig = abs(lfc_f) >= SIG_LFC and pv_f < SIG_P
            row = {"gene": sym, "contrast": cond, "log2fc": round(lfc_f, 2),
                   "p_value": pv_f, "significant": sig}
            long_rows.append(row)
            if sig:
                sig_rows.append(row)

    _write(RESULTS / "caspl_stress_log2fc.tsv", long_rows)
    _write(RESULTS / "caspl_stress_significant.tsv", sig_rows)
    print(f"\nStress (E-MTAB-5540): {len(rows)} CASPLs, "
          f"{len(sig_rows)} significant gene-contrast hits (|log2FC|>=1, p<0.05).")
    print("Significant hits:")
    for r in sorted(sig_rows, key=lambda x: (x["gene"], x["p_value"])):
        print(f"   {r['gene']:<9} {r['log2fc']:+.2f}  p={r['p_value']:.1e}  {r['contrast']}")


def _median_cell(cell: str) -> float:
    """EBI baseline TPM cells are comma-separated quantiles (min,q1,median,q3,max).

    Return the median (middle value); 0.0 for empty/NA.
    """
    if cell in ("", "NA"):
        return 0.0
    parts = [p for p in cell.split(",") if p not in ("", "NA")]
    if not parts:
        return 0.0
    try:
        nums = sorted(float(p) for p in parts)
    except ValueError:
        return 0.0
    return nums[len(nums) // 2]


def baseline_analysis(ens2sym: dict[str, str]) -> None:
    tpms = fetch("baseline_tpms")
    labels = assay_labels(fetch("baseline_config"))
    with open(tpms) as fh:
        rdr = csv.reader(fh, delimiter="\t")
        hdr = next(rdr)
        gcols = [(i, labels.get(hdr[i], hdr[i])) for i in range(2, len(hdr))]
        out = []
        for r in rdr:
            if r[0] not in ens2sym:
                continue
            vals = {lab: _median_cell(r[i]) for i, lab in gcols}
            peak = max(vals, key=vals.get) if vals and max(vals.values()) > 0 else "NA"
            row = {"gene": ens2sym[r[0]], **{k: round(v, 1) for k, v in vals.items()},
                   "peak_tissue": peak}
            out.append(row)
    _write(RESULTS / "caspl_baseline_tpm.tsv", out)
    print(f"\nBaseline (E-GEOD-81077): median tissue TPM for {len(out)} CASPLs.")
    print("Peak tissue per gene (median TPM):")
    for r in sorted(out, key=lambda x: x["gene"]):
        peakval = r.get(r["peak_tissue"], "NA") if r["peak_tissue"] != "NA" else "NA"
        print(f"   {r['gene']:<9} peak={r['peak_tissue']} ({peakval} TPM)")


def _write(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("")
        return
    keys = list(rows[0].keys())
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, delimiter="\t")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    ens2sym = potri_to_ensembl()
    print(f"Mapped CASPL genes (Potri->Ensembl): {len(ens2sym)}")
    stress_analysis(ens2sym)
    baseline_analysis(ens2sym)
    print("\nWrote results/caspl_stress_log2fc.tsv, caspl_stress_significant.tsv, "
          "caspl_baseline_tpm.tsv")


if __name__ == "__main__":
    main()
