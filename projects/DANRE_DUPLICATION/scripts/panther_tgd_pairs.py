"""Identify zebrafish teleost-genome-duplication (TGD) paralog pairs from PANTHER gene trees.

PANTHER (v19) publishes every paralog pair implied by its gene trees in
``AllParalogs.tar.gz``. Column 4 names the tree branch on which the duplication
separating the two genes was placed, as ``<parent taxon>|<child taxon>``.
PANTHER trees contain zebrafish (DANRE), medaka (ORYLA) and the unduplicated
outgroup spotted gar (LEPOC), so a duplication on ``Neopterygii|Teleostei``
(after the gar split, before the zebrafish-medaka split) is the TGD.

Many real TGD pairs are placed lower, on ``Teleostei|DANRE``: the reconciled
tree puts the duplication after the zebrafish-medaka split whenever the
zebrafish and medaka copies do not group as ((zfA, medA), (zfB, medB)), for
example because medaka lost a copy, or because the copies were resolved
independently in each lineage (delayed rediploidization). For 1:1 pairs on
that branch the script collects the evidence needed to judge them, from
PANTHER's ortholog calls (``AllOrthologs.tar.gz``):

* gar: the gar genes each zebrafish copy is orthologous to at the Neopterygii
  node. A TGD pair should share a single gar co-ortholog.
* medaka: the medaka genes each copy is orthologous to at the Teleostei node,
  and whether those medaka genes were themselves duplicated on
  ``Teleostei|ORYLA`` (a parallel duplication, the signature of a TGD pair the
  tree could not resolve).

Duplications on another branch ending at Teleostei (mostly
``Euteleostomi|Teleostei``) are placed on the teleost stem in a tree with no gar
gene, so PANTHER cannot resolve the branch further; they are TGD-compatible.

``tgd_call`` values:
  TGD_tree             duplication placed on Neopterygii|Teleostei by PANTHER
  TGD_tree_no_gar      duplication on another branch ending at Teleostei
                       (e.g. Euteleostomi|Teleostei); gar gene absent from tree
  TGD_likely_parallel  Teleostei|DANRE pair, one shared gar co-ortholog, and
                       medaka co-orthologs duplicated on Teleostei|ORYLA
  TGD_or_lineage       Teleostei|DANRE pair, one shared gar co-ortholog, medaka
                       has a single co-ortholog (TGD + medaka loss, or a
                       zebrafish-lineage duplication; needs synteny)
  unresolved           anything else (no shared gar co-ortholog, no medaka
                       co-ortholog, or several gar co-orthologs)

A pair is ``1:1`` on a branch when each gene has exactly one partner on that
branch (a clean ohnolog pair); otherwise ``multi``. Only 1:1 pairs are kept
from Teleostei|DANRE, which also contains large zebrafish-specific expansions.

Outputs (in projects/DANRE_DUPLICATION/):
  panther_tgd_pairs.tsv             candidate pairs with evidence and tgd_call
  panther_paralog_branch_counts.tsv DANRE-DANRE pairs/genes per duplication branch

Usage (from repo root; downloads ~1.1 GB into the cache dir on first run):
    uv run python projects/DANRE_DUPLICATION/scripts/panther_tgd_pairs.py
"""

import argparse
import csv
import io
import tarfile
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

PANTHER_FTP = "https://data.pantherdb.org/ftp/ortholog/current_release"
ZFIN_GENES = "https://zfin.org/downloads/gene.txt"
ZFIN_ENSEMBL = "https://zfin.org/downloads/ensembl_1_to_1.txt"
HGNC = "https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt"

TGD_BRANCH = "Neopterygii|Teleostei"
DANRE_BRANCH = "Teleostei|DANRE"
ORYLA_BRANCH = "Teleostei|ORYLA"
# Common-ancestor taxon of a speciation ortholog pair, as PANTHER names it.
GAR_NODE = "Neopterygii"
MEDAKA_NODE = "Teleostei"

PROJECT = Path("projects/DANRE_DUPLICATION")


def fetch(url: str, cache: Path) -> Path:
    dest = cache / url.rsplit("/", 1)[1]
    if not dest.exists():
        cache.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, dest)
    return dest


def tar_lines(path: Path):
    with tarfile.open(path) as tf:
        for member in tf:
            fh = tf.extractfile(member)
            if fh is None:
                continue
            yield from io.TextIOWrapper(fh, encoding="utf-8")


def parse_gene(field: str) -> dict[str, str]:
    """'DANRE|ZFIN=ZDB-GENE-1|UniProtKB=Q9' -> {'species': 'DANRE', 'ZFIN': ..., 'UniProtKB': ...}."""
    species, *rest = field.split("|")
    out = {"species": species}
    for part in rest:
        key, _, val = part.partition("=")
        out[key] = val
    return out


def load_symbol_maps(cache: Path) -> tuple[dict[str, str], dict[str, str]]:
    zfin: dict[str, str] = {}
    for row in csv.reader(fetch(ZFIN_GENES, cache).open(), delimiter="\t"):
        if len(row) >= 3:
            zfin[row[0]] = row[2]
    ensembl: dict[str, str] = {}
    for row in csv.reader(fetch(ZFIN_ENSEMBL, cache).open(), delimiter="\t"):
        if len(row) >= 4:
            ensembl[row[3]] = row[2]
            zfin.setdefault(row[0], row[2])  # gene.txt omits some genes this file has
    return zfin, ensembl


def load_hgnc(cache: Path) -> dict[str, str]:
    with fetch(HGNC, cache).open() as fh:
        return {r["hgnc_id"].removeprefix("HGNC:"): r["symbol"] for r in csv.DictReader(fh, delimiter="\t")}


def load_family_names() -> dict[str, str]:
    names: dict[str, str] = {}
    obo = Path("interpro/panther/panther.obo")
    if not obo.exists():
        return names
    current = None
    for line in obo.open():
        if line.startswith("id: PANTHER:"):
            current = line.split("PANTHER:", 1)[1].strip()
        elif line.startswith("name: ") and current:
            names[current] = line[6:].strip()
            current = None
    return names


def symbol(gene: dict[str, str], zfin: dict[str, str], ensembl: dict[str, str]) -> str:
    if "Gene" in gene:
        return gene["Gene"]
    if "ZFIN" in gene and gene["ZFIN"] in zfin:
        return zfin[gene["ZFIN"]]
    if "Ensembl" in gene:
        ens = gene["Ensembl"].split(".")[0]
        if ens in ensembl:
            return ensembl[ens]
    return ""


def gene_id(gene: dict[str, str]) -> str:
    """Stable key for any PANTHER gene field: prefer UniProt, fall back to the first xref."""
    return gene.get("UniProtKB") or next((v for k, v in gene.items() if k != "species"), "")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--cache-dir", type=Path, default=PROJECT / ".cache")
    args = ap.parse_args()
    cache = args.cache_dir

    zfin, ensembl = load_symbol_maps(cache)
    hgnc = load_hgnc(cache)
    family_names = load_family_names()
    reviewed = {p.name for p in Path("genes/DANRE").iterdir() if p.is_dir()}

    # --- paralogs: DANRE-DANRE (all branches) and ORYLA-ORYLA (Teleostei|ORYLA only)
    genes: dict[str, dict[str, str]] = {}
    pairs_by_branch: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    medaka_lineage_dup: set[frozenset[str]] = set()
    for line in tar_lines(fetch(f"{PANTHER_FTP}/AllParalogs.tar.gz", cache)):
        if not (line.startswith("DANRE|") or line.startswith("ORYLA|")):
            continue
        cols = line.rstrip("\n").split("\t")
        a, b = parse_gene(cols[0]), parse_gene(cols[1])
        if a["species"] == b["species"] == "DANRE":
            genes[gene_id(a)] = a
            genes[gene_id(b)] = b
            pairs_by_branch[cols[3]].append((gene_id(a), gene_id(b), cols[4]))
        elif a["species"] == b["species"] == "ORYLA" and cols[3] == ORYLA_BRANCH:
            medaka_lineage_dup.add(frozenset((gene_id(a), gene_id(b))))

    # --- orthologs of zebrafish genes: gar (Neopterygii), medaka (Teleostei), human (any)
    gar: dict[str, set[str]] = defaultdict(set)
    medaka: dict[str, set[str]] = defaultdict(set)
    human: dict[str, set[str]] = defaultdict(set)
    for line in tar_lines(fetch(f"{PANTHER_FTP}/AllOrthologs.tar.gz", cache)):
        if "DANRE|" not in line:
            continue
        cols = line.rstrip("\n").split("\t")
        a, b = parse_gene(cols[0]), parse_gene(cols[1])
        if b["species"] == "DANRE":
            a, b = b, a
        if a["species"] != "DANRE":
            continue
        z = gene_id(a)
        if b["species"] == "LEPOC" and cols[3] == GAR_NODE:
            gar[z].add(gene_id(b))
        elif b["species"] == "ORYLA" and cols[3] == MEDAKA_NODE:
            medaka[z].add(gene_id(b))
        elif b["species"] == "HUMAN":
            human[z].add(f"{hgnc.get(b.get('HGNC', ''), gene_id(b))}({cols[2]})")

    with (PROJECT / "panther_paralog_branch_counts.tsv").open("w") as out:
        out.write("duplication_branch\tpairs\tgenes\tfamilies\n")
        for branch, pairs in sorted(pairs_by_branch.items(), key=lambda kv: -len(kv[1])):
            g = {x for p in pairs for x in p[:2]}
            out.write(f"{branch}\t{len(pairs)}\t{len(g)}\t{len({p[2] for p in pairs})}\n")

    def partner_map(pairs):
        partners: dict[str, set[str]] = defaultdict(set)
        for a, b, _ in pairs:
            partners[a].add(b)
            partners[b].add(a)
        return partners

    cols = [
        "tgd_call", "duplication_branch", "pair_class", "family", "family_name",
        "gene_a", "gene_b", "human_orthologs_a", "human_orthologs_b",
        "gar_coorthologs", "gar_a", "gar_b", "medaka_coorthologs", "medaka_parallel_dup",
        "uniprot_a", "uniprot_b", "id_a", "id_b", "reviewed_a", "reviewed_b",
    ]
    rows = []
    stats: Counter = Counter()
    stem_branches = sorted(b for b in pairs_by_branch if b.endswith("|Teleostei") and b != TGD_BRANCH)
    for branch in (TGD_BRANCH, *stem_branches, DANRE_BRANCH):
        pairs = pairs_by_branch.get(branch, [])
        partners = partner_map(pairs)
        for a, b, fam in pairs:
            one = len(partners[a]) == 1 and len(partners[b]) == 1
            if branch == DANRE_BRANCH and not one:
                continue
            shared_gar = gar[a] & gar[b]
            med = medaka[a] | medaka[b]
            parallel = any(frozenset((m1, m2)) in medaka_lineage_dup for m1 in med for m2 in med if m1 < m2)
            if branch == TGD_BRANCH:
                call = "TGD_tree"
            elif branch != DANRE_BRANCH:
                call = "TGD_tree_no_gar"
            elif len(shared_gar) == 1 and len(gar[a]) == 1 and len(gar[b]) == 1 and parallel:
                call = "TGD_likely_parallel"
            elif len(shared_gar) == 1 and len(gar[a]) == 1 and len(gar[b]) == 1 and len(med) == 1:
                call = "TGD_or_lineage"
            else:
                call = "unresolved"
            stats[(branch, "1:1" if one else "multi", call)] += 1
            row = {
                "tgd_call": call, "duplication_branch": branch, "pair_class": "1:1" if one else "multi",
                "family": fam, "family_name": family_names.get(fam, ""),
                "gar_coorthologs": len(shared_gar), "gar_a": len(gar[a]), "gar_b": len(gar[b]),
                "medaka_coorthologs": len(med), "medaka_parallel_dup": "yes" if parallel else "",
            }
            for side, acc in (("a", a), ("b", b)):
                g = genes[acc]
                sym = symbol(g, zfin, ensembl)
                row[f"gene_{side}"] = sym
                row[f"uniprot_{side}"] = g.get("UniProtKB", "")
                row[f"id_{side}"] = g.get("ZFIN") or g.get("Ensembl") or ""
                row[f"human_orthologs_{side}"] = ";".join(sorted(human.get(acc, ())))
                row[f"reviewed_{side}"] = "yes" if sym in reviewed else ""
            if row["gene_b"] and (not row["gene_a"] or row["gene_b"] < row["gene_a"]):
                for c in ("gene", "uniprot", "id", "human_orthologs", "reviewed"):
                    row[f"{c}_a"], row[f"{c}_b"] = row[f"{c}_b"], row[f"{c}_a"]
                row["gar_a"], row["gar_b"] = row["gar_b"], row["gar_a"]
            rows.append(row)

    order = {"TGD_tree": 0, "TGD_tree_no_gar": 1, "TGD_likely_parallel": 2, "TGD_or_lineage": 3, "unresolved": 4}
    rows.sort(key=lambda r: (order[r["tgd_call"]], r["pair_class"] != "1:1", r["gene_a"] or "~", r["gene_b"]))
    with (PROJECT / "panther_tgd_pairs.tsv").open("w", newline="") as out:
        w = csv.DictWriter(out, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    for key, n in sorted(stats.items()):
        print("\t".join(key), n, sep="\t")


if __name__ == "__main__":
    main()
