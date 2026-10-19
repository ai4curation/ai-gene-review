"""Record (1) the InterPro member-database signatures matched by each protein,
with their reported scores, and (2) the KEGG genome neighbourhood of the three
KT2440 MoaA-family genes.

Network lookups only; nothing is hardcoded except the query identifiers.

Usage (from repo root):
  uv run --no-project python -I \
    genes/PSEPK/PP_1969/PP_1969-bioinformatics/context_lookups.py \
    --uniprot Q88E69,Q88LG4,Q88K11,P30745 \
    --loci PP_4597,PP_1969,PP_2482 --flank 6 \
    --outdir genes/PSEPK/PP_1969/PP_1969-bioinformatics/model_scores_out

InterPro API: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/<ACC>/
KEGG REST:    https://rest.kegg.jp/get/ppu:<LOCUS>
"""
import argparse
import json
import re
import time
import urllib.request
from pathlib import Path


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode()
        except Exception:  # retry transient network failures, then re-raise
            if i == tries - 1:
                raise
            time.sleep(2)


def interpro(acc):
    url = f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/?page_size=200"
    rows = []
    while url:
        d = json.loads(get(url))
        for r in d["results"]:
            m = r["metadata"]
            name = m["name"] if isinstance(m["name"], str) else (m["name"] or {}).get("name", "")
            for p in r["proteins"]:
                for loc in p.get("entry_protein_locations") or []:
                    frags = ",".join(f"{f['start']}-{f['end']}" for f in loc["fragments"])
                    rows.append((acc, m["source_database"], m["accession"], name, frags,
                                 "" if loc.get("score") is None else str(loc["score"])))
        url = d.get("next")
    return rows


def kegg_gene(locus):
    txt = get(f"https://rest.kegg.jp/get/ppu:{locus}")
    field = lambda k: (re.search(rf"^{k}\s+(.+)$", txt, re.M) or [None, ""])[1].strip()
    pos = field("POSITION")
    ko = re.search(r"^ORTHOLOGY\s+(K\d+)\s+(.+)$", txt, re.M)
    mods = re.findall(r"(ppu_M\d+)\s+(.+)", txt)
    return dict(locus=locus, name=field("NAME"), position=pos,
                ko=f"{ko.group(1)} {ko.group(2)}" if ko else "",
                modules="; ".join(f"{a} {b}" for a, b in mods))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--uniprot", required=True)
    ap.add_argument("--loci", required=True)
    ap.add_argument("--flank", type=int, default=6)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)

    with (out / "interpro_matches.tsv").open("w") as fh:
        fh.write("uniprot\tsource_database\tsignature\tname\tlocations\tscore\n")
        for acc in a.uniprot.split(","):
            for row in interpro(acc):
                fh.write("\t".join(row) + "\n")
    print(f"wrote {out / 'interpro_matches.tsv'}")

    with (out / "kegg_neighbourhood.tsv").open("w") as fh:
        fh.write("focal\toffset\tlocus\tposition\tname\tko\tkegg_modules\n")
        for focal in a.loci.split(","):
            n = int(focal.split("_")[1])
            for off in range(-a.flank, a.flank + 1):
                locus = f"PP_{n + off:04d}"
                try:
                    g = kegg_gene(locus)
                except Exception as e:  # locus number absent from KEGG
                    g = dict(locus=locus, name=f"not retrieved ({type(e).__name__})", position="", ko="", modules="")
                fh.write("\t".join([focal, f"{off:+d}", g["locus"], g["position"], g["name"], g["ko"], g["modules"]]) + "\n")
                time.sleep(0.4)
    print(f"wrote {out / 'kegg_neighbourhood.tsv'}")


if __name__ == "__main__":
    main()
