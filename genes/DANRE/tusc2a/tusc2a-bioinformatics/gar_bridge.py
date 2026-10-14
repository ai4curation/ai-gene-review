"""Gar-bridge synteny check for a zebrafish paralog pair (Ensembl REST, queried at run time).

For the single spotted-gar orthologue of a zebrafish pair, take every protein-coding gar gene
within WINDOW bp, ask Ensembl Compara for its zebrafish orthologues, and report which of them lie
near either zebrafish copy (within NEAR bp) and on which chromosomes the rest fall. Double
conserved synteny (DCS) predicts gar neighbours whose zebrafish orthologues sit next to copy a
and, for other or the same neighbours, next to copy b. Nothing is hardcoded except the gene ids
given on the command line.

Usage (repo root):
    uv run python genes/DANRE/tusc2a/tusc2a-bioinformatics/gar_bridge.py \
        GAR_GENE_ID ZF_GENE_A ZF_GENE_B [WINDOW_BP] [NEAR_BP]
"""

import json
import sys
import time
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENSEMBL = "https://rest.ensembl.org"


def ens(path: str, retries: int = 10):
    url = ENSEMBL + path + ("&" if "?" in path else "?") + "content-type=application/json"
    for i in range(retries):
        try:
            time.sleep(0.1)
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review-gar-bridge/1.0"})
            return json.loads(urllib.request.urlopen(req, timeout=120).read())
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(3 + 3 * i)


def main():
    gar, za, zb = sys.argv[1:4]
    window = int(sys.argv[4]) if len(sys.argv) > 4 else 1_000_000
    near = int(sys.argv[5]) if len(sys.argv) > 5 else 3_000_000
    g = ens(f"/lookup/id/{gar}?")
    loc = {}
    for z in (za, zb):
        d = ens(f"/lookup/id/{z}?")
        loc[z] = (d["seq_region_name"], d["start"], d.get("display_name") or z)
    print(f"# Gar bridge (run {time.strftime('%Y-%m-%d')}): gar {gar} on {g['seq_region_name']}:{g['start']}-{g['end']}")
    for z, (c, s, n) in loc.items():
        print(f"zebrafish {n} ({z}): chr{c}:{s}")
    region = f"{g['seq_region_name']}:{max(1, g['start'] - window)}-{g['end'] + window}"
    neigh = ens(f"/overlap/region/lepisosteus_oculatus/{region}?feature=gene;biotype=protein_coding")
    neigh = [n for n in neigh if n["id"] != gar]
    print(f"gar protein-coding genes within {window/1e6:.1f} Mb: {len(neigh)}")

    def zf_orthologues(gid):
        try:
            h = ens(f"/homology/id/lepisosteus_oculatus/{gid}?type=orthologues;target_species=danio_rerio;sequence=none;format=condensed")
        except Exception:  # noqa: BLE001
            return None
        return [x["id"] for x in h["data"][0]["homologies"]] if h.get("data") else []

    with ThreadPoolExecutor(max_workers=3) as ex:
        orths = list(ex.map(zf_orthologues, [n["id"] for n in neigh]))
    zf_ids = sorted({z for o in orths if o for z in o})

    def zf_loc(zid):
        try:
            d = ens(f"/lookup/id/{zid}?")
            return zid, (d["seq_region_name"], d["start"], d.get("display_name") or zid)
        except Exception:  # noqa: BLE001
            return zid, None

    with ThreadPoolExecutor(max_workers=3) as ex:
        zl = dict(ex.map(zf_loc, zf_ids))
    chrom_counts = Counter()
    near_hits = {z: [] for z in (za, zb)}
    both = 0
    failed = sum(1 for o in orths if o is None)
    with_orth = 0
    for n, o in zip(neigh, orths):
        if not o:
            continue
        with_orth += 1
        chroms = set()
        hit = set()
        for zid in o:
            if not zl.get(zid):
                continue
            c, s, name = zl[zid]
            chroms.add(c)
            for z, (zc, zs, zn) in loc.items():
                if c == zc and abs(s - zs) <= near:
                    near_hits[z].append(f"{n.get('external_name') or n['id']} -> {name} (chr{c}:{s})")
                    hit.add(z)
        if len(hit) == 2:
            both += 1
        for c in chroms:
            chrom_counts[c] += 1
    print(f"gar neighbours with >=1 zebrafish orthologue: {with_orth} ({failed} queries failed)")
    for z, (c, s, n) in loc.items():
        print(f"\ngar neighbours with a zebrafish orthologue within {near/1e6:.1f} Mb of {n} (chr{c}): {len(near_hits[z])}")
        for h in near_hits[z]:
            print(f"- {h}")
    print(f"\ngar neighbours with orthologues near BOTH copies: {both}")
    print("zebrafish chromosomes carrying orthologues of the gar neighbours (count of gar neighbours):")
    for c, k in chrom_counts.most_common(8):
        print(f"- chr{c}: {k}")


if __name__ == "__main__":
    main()
