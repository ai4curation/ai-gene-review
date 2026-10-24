"""Record Ensembl Compara's view of the brorin-family genes in zebrafish:
within-species paralogy of si:dkey-283b1.7 and vwc2, and each gene's orthologs in
spotted gar, human and medaka (REST /homology). This is an independent gene-tree
view to set against the PANTHER call in panther_tgd_pairs.tsv.

Run from the repository root:
    uv run python genes/DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/compara_check.py
"""

import json
import time
import urllib.error
import urllib.request

GENES = {
    "ENSDARG00000053460": "si:dkey-283b1.7",
    "ENSDARG00000076495": "vwc2",
    "ENSDARG00000069134": "vwc2l",
}
TARGETS = ["lepisosteus_oculatus", "homo_sapiens", "oryzias_latipes"]


def get(path: str) -> dict:
    url = f"https://rest.ensembl.org{path}{'&' if '?' in path else '?'}content-type=application/json"
    for attempt in range(4):
        try:
            return json.loads(urllib.request.urlopen(url, timeout=180).read())
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(url)


def main() -> None:
    print("## Within-zebrafish paralogy (Ensembl Compara)\n")
    ids = list(GENES)
    for a in ids:
        d = get(f"/homology/id/danio_rerio/{a}?type=paralogues;format=condensed")
        for h in d["data"][0]["homologies"]:
            if h["id"] in GENES and h["id"] != a:
                print(f"- {GENES[a]} vs {GENES[h['id']]}: {h['type']} at {h['taxonomy_level']}")
    print("\n## Orthologs\n")
    print("| zebrafish gene | species | ortholog | type | taxonomy level | % id (query) | % id (target) |")
    print("|---|---|---|---|---|---|---|")
    for g, name in GENES.items():
        for sp in TARGETS:
            d = get(f"/homology/id/danio_rerio/{g}?type=orthologues;target_species={sp}")
            hs = d["data"][0]["homologies"] if d.get("data") else []
            if not hs:
                print(f"| {name} | {sp} | none | | | | |")
            for h in hs:
                print(f"| {name} | {sp} | {h['target']['id']} | {h['type']} | {h['taxonomy_level']} | "
                      f"{h['source']['perc_id']:.1f} | {h['target']['perc_id']:.1f} |")


if __name__ == "__main__":
    main()
