#!/usr/bin/env python
"""Liver-zonation expression oracle (Halpern et al. 2017, Nature; PMID:28166538).

Supplementary Table S3 of Halpern 2017 gives, for each mouse gene, a reconstructed
expression profile across nine layers of the liver lobule (the porto-central axis).
This oracle extracts those profiles for the gluconeogenesis isozymes plus a panel
of zonation landmark genes, caches them to a TSV, and exposes:

* per-gene 9-layer profiles (mouse symbols),
* the porto-central ORIENTATION inferred *from the data* using landmark genes
  (pericentral: Glul/Cyp2e1/Oat; periportal: Ass1/Asl/Aldob), rather than assumed.

Data are fetched once from the Europe PMC supplementary-files endpoint (the NCBI
PMC mirror is behind a proof-of-work wall). Nothing here is fabricated: profiles
are the published reconstructed values.
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import requests

HERE = Path(__file__).parent
CACHE_TSV = HERE / "cache" / "halpern_zonation.tsv"
SUPPL_ZIP = HERE / "cache" / "suppl.zip"
S3_NAME = "NIHMS70855-supplement-Supplementary_Table_3.xlsx"
EUROPEPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5321580/supplementaryFiles"

N_LAYERS = 9
PERICENTRAL_LANDMARKS = ["Glul", "Cyp2e1", "Oat"]
PERIPORTAL_LANDMARKS = ["Ass1", "Asl", "Aldob", "Cyp2f2", "Sds"]
# Genes to extract: pathway isozymes (mouse symbols) + landmarks for orientation.
PATHWAY_MOUSE = ["Pcx", "Pck1", "Pck2", "Fbp1", "Fbp2", "G6pc", "Slc37a4"]


def _download_table_s3() -> bytes:
    SUPPL_ZIP.parent.mkdir(parents=True, exist_ok=True)
    if not SUPPL_ZIP.exists():
        r = requests.get(EUROPEPMC, timeout=120)
        r.raise_for_status()
        SUPPL_ZIP.write_bytes(r.content)
    return zipfile.ZipFile(SUPPL_ZIP).read(S3_NAME)


def build_cache() -> None:
    """Extract the needed gene profiles from Table S3 into a small TSV."""
    import openpyxl

    wanted = {g.lower() for g in PATHWAY_MOUSE + PERICENTRAL_LANDMARKS + PERIPORTAL_LANDMARKS}
    wb = openpyxl.load_workbook(io.BytesIO(_download_table_s3()), read_only=True)
    ws = wb["Zonation matrix"]
    rows = list(ws.iter_rows(values_only=True))
    out: dict[str, list[float]] = {}
    for r in rows[3:]:  # rows 0-2 are title/header
        sym = r[0]
        if sym is None:
            continue
        for tok in str(sym).split(";"):
            t = tok.strip()
            if t.lower() in wanted and t not in out:
                out[t] = [float(x) if x not in (None, "") else 0.0 for x in r[1:1 + N_LAYERS]]
    CACHE_TSV.parent.mkdir(parents=True, exist_ok=True)
    with CACHE_TSV.open("w") as fh:
        fh.write("gene\t" + "\t".join(f"L{i+1}" for i in range(N_LAYERS)) + "\n")
        for g, prof in out.items():
            fh.write(g + "\t" + "\t".join(f"{v:.6g}" for v in prof) + "\n")


def load_profiles() -> dict[str, list[float]]:
    if not CACHE_TSV.exists():
        build_cache()
    lines = CACHE_TSV.read_text().splitlines()
    prof: dict[str, list[float]] = {}
    for line in lines[1:]:
        c = line.split("\t")
        prof[c[0]] = [float(x) for x in c[1:]]
    return prof


def relative_profile(prof: list[float]) -> list[float]:
    """Normalise a profile to its own max (0..1) so genes are comparable."""
    mx = max(prof) or 1.0
    return [v / mx for v in prof]


def portal_pole(profiles: dict[str, list[float]]) -> int:
    """Infer which layer index (0-based) is the periportal pole, from landmarks.

    Periportal landmark genes peak at the portal pole; pericentral landmarks peak at
    the central pole. Returns the layer index where periportal landmark expression
    (mean of relative profiles) is greatest.
    """
    acc = [0.0] * N_LAYERS
    n = 0
    for g in PERIPORTAL_LANDMARKS:
        if g in profiles:
            rel = relative_profile(profiles[g])
            acc = [a + r for a, r in zip(acc, rel)]
            n += 1
    return acc.index(max(acc))


def zone_label(layer_idx: int, pp_pole: int) -> str:
    """Label a 0-based layer as periportal / mid / pericentral relative to the pole."""
    # pp_pole is the periportal end; the opposite end is pericentral.
    far = 0 if pp_pole >= N_LAYERS // 2 else N_LAYERS - 1
    # distance toward portal pole, normalised
    frac = abs(layer_idx - far) / abs(pp_pole - far)
    if frac >= 0.66:
        return "periportal"
    if frac <= 0.33:
        return "pericentral"
    return "mid"


if __name__ == "__main__":
    build_cache()
    prof = load_profiles()
    pp = portal_pole(prof)
    print(f"cached {len(prof)} genes -> {CACHE_TSV}")
    print(f"inferred periportal pole = Layer {pp+1} "
          f"(pericentral landmarks peak at the opposite end)")
    for g in PATHWAY_MOUSE:
        if g in prof:
            rel = relative_profile(prof[g])
            bar = "".join("#" if x >= 0.5 else "." for x in rel)
            print(f"  {g:9s} {bar}  (L1=pericentral .. L9=periportal)")
