"""Which spotted gar anatomical entities does Bgee have RNA-seq expression calls for?

Bgee returns only 'expressed' calls, so the absence of a gar call for a gene in some tissue is
only informative if Bgee has gar RNA-seq data for that tissue at all. This script uses broadly
expressed housekeeping genes as a sampling control: the gar orthologues (Ensembl Compara) of
zebrafish gapdh, actb1 and eef1a1l1, and prints the union of their gar Bgee calls, i.e. the
gar anatomical entities that Bgee samples.

Run from the repo root:
    uv run python genes/DANRE/agxta/agxta-bioinformatics/bgee_gar_coverage.py \
        > genes/DANRE/agxta/agxta-bioinformatics/bgee_gar_coverage.txt
"""

import json
import time
import urllib.request

UA = {"User-Agent": "ai-gene-review-pair-analysis/1.0"}
CONTROLS = ["gapdh", "actb1", "eef1a1l1"]


def get(url: str, retries: int = 10) -> bytes:
    for i in range(retries):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()
            if "ensembl.org" in url and data.lstrip()[:1] not in (b"{", b"["):
                raise ValueError("non-JSON response")
            return data
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(5 + 6 * i)
    raise RuntimeError(url)


def ens(path: str):
    sep = "&" if "?" in path else "?"
    return json.loads(get("https://rest.ensembl.org" + path + sep + "content-type=application/json"))


def main():
    union: dict[str, list[str]] = {}
    for sym in CONTROLS:
        zid = ens(f"/lookup/symbol/danio_rerio/{sym}?")["id"]
        homs = ens(f"/homology/id/danio_rerio/{zid}?type=orthologues;sequence=none;format=condensed;"
                   f"target_species=lepisosteus_oculatus")["data"][0]["homologies"]
        for h in homs:
            gid = h["id"]
            d = json.loads(get(f"https://www.bgee.org/api/?page=gene&action=expression&gene_id={gid}"
                               f"&species_id=7918&cond_param=anat_entity&display_type=json"))
            calls = [c["condition"]["anatEntity"]["name"] for c in d["data"]["calls"]]
            print(f"{sym} ({zid}) -> gar {gid}: {len(calls)} Bgee calls: {', '.join(sorted(calls))}")
            for c in calls:
                union.setdefault(c, []).append(sym)
    print(f"\nUnion of gar anatomical entities with a call for any control gene ({len(union)}):")
    for k in sorted(union):
        print(f"- {k}")


if __name__ == "__main__":
    main()
