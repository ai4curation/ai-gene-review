"""Draw a reproducible random sample of PANTHER TGD pairs for review.

Sampling frame: every 1:1 pair in panther_tgd_pairs.tsv whose tgd_call is
TGD_tree (duplication placed on Neopterygii|Teleostei). The frame is shuffled
with a fixed seed and pairs are taken in that order. A drawn pair is skipped,
and the skip is recorded, if either gene has no GOA annotation on any of its
UniProt accessions (nothing to review), or if Ensembl Compara does not place
the duplication relating the two genes at a teleost node (Teleostei,
Osteoglossocephalai or Clupeocephala). The Compara check was added after
batch 3, in which 2 of 8 PANTHER TGD_tree pairs were not supported by Compara
or gar synteny; rerunning reapplies it to the batch 3 draws. Unnamed genes (si:, zgc:, LOC...)
are NOT excluded, so the sample is not biased toward well-studied genes.

For each accepted gene the script also picks the UniProt accession holding the
most experimental GOA rows (then most rows overall), using the same helpers as
accession_audit.py, and reports rows that exist only on other accessions.

Usage (from repo root):
    uv run python projects/DANRE_DUPLICATION/scripts/sample_pairs.py --n 18 --seed 20260928 \
        > projects/DANRE_DUPLICATION/random_sample.tsv
"""

import argparse
import csv
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from accession_audit import EXPERIMENTAL, accessions, annotations, key  # noqa: E402

PAIRS = Path("projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv")


def best_accession(primary: str, symbol: str = "") -> tuple[str, int, int, int]:
    """Best accession for the gene behind a PANTHER UniProt accession.

    Candidates are that accession, every UniProt entry sharing its ZFIN gene
    cross-reference, and every zebrafish entry with the same gene symbol (many
    RefSeq-derived TrEMBL entries carry no ZFIN cross-reference). Returns (accession, experimental rows, all rows, experimental
    or IBA rows present only on other candidates).
    """
    import json
    import urllib.parse
    import urllib.request

    q = urllib.parse.urlencode({"query": f"accession:{primary}", "fields": "gene_names,xref_zfin",
                                "format": "json"})
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/search?{q}", timeout=60) as r:
        res = json.load(r)["results"]
    zfin = [x["id"] for x in (res[0].get("uniProtKBCrossReferences", []) if res else []) if x["database"] == "ZFIN"]
    candidates = {primary}
    if symbol and not symbol.startswith("LOC"):
        candidates |= {acc for acc, _ in accessions(symbol)}
    for z in zfin:
        q = urllib.parse.urlencode({"query": f"xref:zfin-{z} AND organism_id:7955", "fields": "accession",
                                    "format": "json", "size": 100})
        with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/search?{q}", timeout=60) as r:
            candidates |= {x["primaryAccession"] for x in json.load(r)["results"]}
    scored = []
    union: set = set()
    for acc in sorted(candidates):
        anns = annotations(acc)
        keys = {key(a) for a in anns}
        union |= keys
        scored.append((sum(a["goEvidence"] in EXPERIMENTAL for a in anns), len(anns), acc, keys))
    scored.sort(key=lambda s: (-s[0], -s[1], s[2]))
    n_exp, n_all, acc, keys = scored[0]
    elsewhere = sum(1 for k in union - keys if k[1] in EXPERIMENTAL or k[1] == "IBA")
    return acc, n_exp, n_all, elsewhere


ENSEMBL = "https://rest.ensembl.org"
ZFIN_ENSEMBL = "https://zfin.org/downloads/ensembl_1_to_1.txt"
# Ensembl Compara taxonomy levels that correspond to the TGD node.
TGD_LEVELS = {"Teleostei", "Osteoglossocephalai", "Clupeocephala"}


def zfin_to_ensembl(cache: Path) -> dict[str, str]:
    import urllib.request

    path = cache / "ensembl_1_to_1.txt"
    if not path.exists():
        cache.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(ZFIN_ENSEMBL, path)
    out = {}
    for row in csv.reader(path.open(), delimiter="\t"):
        if len(row) >= 4:
            out[row[0]] = row[3]
    return out


def zfin_symbols(cache: Path) -> dict[str, str]:
    """ZFIN gene symbol -> ZDB id, from the same ZFIN Ensembl download."""
    out = {}
    for row in csv.reader((cache / "ensembl_1_to_1.txt").open(), delimiter="\t"):
        if len(row) >= 4:
            out.setdefault(row[2], row[0])
    return out


def uniprot_zfin(acc: str) -> list[str]:
    import json
    import urllib.parse
    import urllib.request

    q = urllib.parse.urlencode({"query": f"accession:{acc}", "fields": "xref_zfin", "format": "json"})
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/search?{q}", timeout=60) as r:
        res = json.load(r)["results"]
    return [x["id"] for x in (res[0].get("uniProtKBCrossReferences", []) if res else []) if x["database"] == "ZFIN"]


def ensembl_id(xref: str, acc: str, symbol: str, zfin_map: dict[str, str], sym_map: dict[str, str]) -> str:
    """Ensembl gene id from the PANTHER xref, else UniProt's ZFIN xref, else the ZFIN symbol."""
    if xref.startswith("ENSDARG"):
        return xref.split(".")[0]
    if xref in zfin_map:
        return zfin_map[xref]
    for zdb in uniprot_zfin(acc):
        if zdb in zfin_map:
            return zfin_map[zdb]
    return zfin_map.get(sym_map.get(symbol, ""), "")


def compara_level(ens_a: str, ens_b: str) -> str:
    """Taxonomy level of the Ensembl Compara duplication node relating two zebrafish genes."""
    import json
    import time
    import urllib.error
    import urllib.request

    if not ens_a or not ens_b:
        return "unmapped"
    url = f"{ENSEMBL}/homology/id/danio_rerio/{ens_a}?type=paralogues;format=condensed;content-type=application/json"
    for attempt in range(10):
        try:
            with urllib.request.urlopen(url, timeout=120) as resp:
                data = json.load(resp)
            break
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):
                return "not_in_ensembl"
            time.sleep(min(60, 2 ** attempt))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(min(60, 2 ** attempt))
    else:
        return "ensembl_error"
    for entry in data.get("data", []):
        for h in entry.get("homologies", []):
            if h["id"] == ens_b:
                return h.get("taxonomy_level", "?")
    return "not_paralogous_in_compara"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8, help="number of confirmed pairs to accept")
    ap.add_argument("--seed", type=int, default=20260928)
    ap.add_argument("--batch3-draws", type=int, default=10,
                    help="draws already taken in batch 3 (reported as batch3, later draws as batch4)")
    ap.add_argument("--cache-dir", type=Path, default=Path("projects/DANRE_DUPLICATION/.cache"))
    args = ap.parse_args()

    frame = [r for r in csv.DictReader(PAIRS.open(), delimiter="\t")
             if r["tgd_call"] == "TGD_tree" and r["pair_class"] == "1:1"]
    frame.sort(key=lambda r: (r["uniprot_a"], r["uniprot_b"]))
    random.Random(args.seed).shuffle(frame)
    zfin_map = zfin_to_ensembl(args.cache_dir)
    sym_map = zfin_symbols(args.cache_dir)
    reviewed = {d.name for d in Path("genes/DANRE").iterdir()}

    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["draw", "batch", "status", "compara_level", "reviewed", "family", "family_name",
                  "gene_a", "gene_b",
                  "accession_a", "exp_a", "goa_a", "missing_elsewhere_a",
                  "accession_b", "exp_b", "goa_b", "missing_elsewhere_b",
                  "human_orthologs_a", "human_orthologs_b"])
    accepted = 0
    for i, r in enumerate(frame, start=1):
        a = best_accession(r["uniprot_a"], r["gene_a"])
        b = best_accession(r["uniprot_b"], r["gene_b"])
        level = compara_level(ensembl_id(r["id_a"], r["uniprot_a"], r["gene_a"], zfin_map, sym_map),
                              ensembl_id(r["id_b"], r["uniprot_b"], r["gene_b"], zfin_map, sym_map))
        if not (a[2] and b[2]):
            status = "skipped_no_goa"
        elif level in TGD_LEVELS:
            status = "accepted"
            accepted += 1
        else:
            status = "skipped_not_confirmed"
        dirs = {g.replace(":", "_") for g in (r["gene_a"], r["gene_b"])}
        out.writerow([i, "batch3" if i <= args.batch3_draws else "batch4", status, level,
                      "yes" if dirs <= reviewed else "",
                      r["family"], r["family_name"], r["gene_a"], r["gene_b"],
                      *a, *b, r["human_orthologs_a"], r["human_orthologs_b"]])
        sys.stdout.flush()
        if accepted >= args.n:
            break
    print(f"# frame size {len(frame)}; seed {args.seed}; confirmed accepted {accepted}", file=sys.stderr)


if __name__ == "__main__":
    main()
