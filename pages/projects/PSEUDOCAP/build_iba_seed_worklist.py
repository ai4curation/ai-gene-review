"""Build the PseudoCAP IBA-seed worklist.

Finds every PAINT IBD node annotation (``IBD.gaf``) that cites a
*Pseudomonas aeruginosa* PAO1 protein as a seed, works out which of that
protein's experimental GO annotations can support the node term (the seed
term equals the node term or is an is_a/part_of descendant of it), and counts
how many leaf IBA annotations each node term propagates to.

A seeding is "PseudoCAP-supported" when at least one supporting annotation was
assigned by PseudoCAP. A node term is "sole-seeded" when the PAO1 protein is
its only seed: if the PseudoCAP annotation is wrong, so is the IBD.

Inputs are downloaded into the git-ignored ``.cache/paint/`` directory:

* PAINT ``IBD.gaf`` and ``gene_association.paint_uniprot.gaf.gz`` (PANTHER FTP)
* PAO1 proteome (UniProt REST, organism_id 208964)
* PAO1 experimental annotations (QuickGO, ECO:0000269/ECO:0000006 descendants)
* ``go-basic.obo``

Output: ``projects/PSEUDOCAP/iba_seed_worklist.yaml``.

Usage::

    uv run python projects/PSEUDOCAP/build_iba_seed_worklist.py
"""

from __future__ import annotations

import collections
import csv
import gzip
import sys
from datetime import date
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".cache" / "paint"
OUT = Path(__file__).resolve().parent / "iba_seed_worklist.yaml"
TAXON = "208964"

PAINT = "https://data.pantherdb.org/ftp/downloads/paint/current"
SOURCES = {
    "IBD.gaf": f"{PAINT}/IBD.gaf",
    "leaf.gaf.gz": f"{PAINT}/gene_association.paint_uniprot.gaf.gz",
    "go-basic.obo": "https://purl.obolibrary.org/obo/go/go-basic.obo",
    "pao1.tsv": (
        "https://rest.uniprot.org/uniprotkb/stream?query=organism_id:"
        f"{TAXON}&format=tsv&fields=accession,gene_names,gene_oln,reviewed,protein_name"
    ),
    "pao1_exp.tsv": (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?"
        f"taxonId={TAXON}&taxonUsage=exact&evidenceCode=ECO:0000269,ECO:0000006"
        "&evidenceCodeUsage=descendants&downloadLimit=50000"
    ),
}


def fetch(name: str) -> Path:
    path = CACHE / name
    if not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        headers = {"Accept": "text/tsv"} if "QuickGO" in SOURCES[name] else {}
        with requests.get(SOURCES[name], headers=headers, stream=True, timeout=600) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
    return path


def load_go(path: Path):
    parents: dict[str, set[str]] = collections.defaultdict(set)
    names: dict[str, str] = {}
    cur = None
    for line in open(path):
        line = line.rstrip()
        if line.startswith("["):
            cur = None
        elif line.startswith("id: GO:"):
            cur = line[4:]
        elif cur:
            if line.startswith("name: "):
                names[cur] = line[6:]
            elif line.startswith("is_a: "):
                parents[cur].add(line[6:16])
            elif line.startswith("relationship: part_of "):
                parents[cur].add(line[22:32])
    closure: dict[str, set[str]] = {}

    def ancestors(term: str) -> set[str]:
        if term not in closure:
            s = {term}
            for p in parents.get(term, ()):
                s |= ancestors(p)
            closure[term] = s
        return closure[term]

    return names, ancestors


def main() -> None:
    sys.setrecursionlimit(10000)
    for name in SOURCES:
        fetch(name)
    names, ancestors = load_go(CACHE / "go-basic.obo")

    proteome = {r["Entry"]: r for r in csv.DictReader(open(CACHE / "pao1.tsv"), delimiter="\t")}
    exp = collections.defaultdict(list)
    for r in csv.DictReader(open(CACHE / "pao1_exp.tsv"), delimiter="\t"):
        if "NOT" not in r["QUALIFIER"]:
            exp[r["GENE PRODUCT ID"]].append(r)

    # node-term seedings by PAO1 proteins
    seedings = []
    n_seeds: dict[tuple[str, str], int] = {}
    for line in open(CACHE / "IBD.gaf"):
        if line.startswith("!"):
            continue
        f = line.rstrip("\n").split("\t")
        node, go, ev, qual, aspect, seeds = f[1], f[4], f[6], f[3], f[8], f[7].split("|")
        n_seeds[(node, go)] = len(seeds)
        for s in seeds:
            acc = s.removeprefix("UniProtKB:")
            if s.startswith("UniProtKB:") and acc in proteome:
                seedings.append(dict(acc=acc, node=node, go=go, evidence=ev, qualifier=qual, aspect=aspect))

    keys = {(s["node"], s["go"]) for s in seedings}
    nodes = {k[0] for k in keys}
    leaf = collections.Counter()
    leaf_taxa = collections.defaultdict(set)
    with gzip.open(CACHE / "leaf.gaf.gz", "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            p = line.split("\t", 13)
            node = p[7].split("|", 1)[0].removeprefix("PANTHER:")
            if node in nodes and (node, p[4]) in keys:
                leaf[(node, p[4])] += 1
                leaf_taxa[(node, p[4])].add(p[12])

    genes = collections.defaultdict(list)
    for s in seedings:
        sup = [r for r in exp[s["acc"]] if s["go"] in ancestors(r["GO TERM"])]
        assigners = sorted({r["ASSIGNED BY"] for r in sup})
        if "PseudoCAP" not in assigners:
            continue
        k = (s["node"], s["go"])
        genes[s["acc"]].append(
            dict(
                node=s["node"],
                node_term=dict(id=s["go"], label=names.get(s["go"], "")),
                ibd_qualifier=s["qualifier"] or None,
                n_seeds=n_seeds[k],
                sole_seed=n_seeds[k] == 1,
                leaf_ibas=leaf[k],
                leaf_taxa=len(leaf_taxa[k]),
                pseudocap_only_support=assigners == ["PseudoCAP"],
                supporting_annotations=sorted(
                    {
                        f"{r['GO TERM']} {names.get(r['GO TERM'], '')} | {r['GO EVIDENCE CODE']} | "
                        f"{r['REFERENCE']} | {r['ASSIGNED BY']}"
                        for r in sup
                    }
                ),
            )
        )

    existing = {p.name for p in (ROOT / "genes" / "PSEAE").iterdir() if p.is_dir()}
    entries = []
    for acc, segs in genes.items():
        row = proteome[acc]
        gene_names = row["Gene Names"].split()
        symbol = gene_names[0] if gene_names else acc
        sole = [s for s in segs if s["sole_seed"]]
        entries.append(
            dict(
                uniprot=acc,
                symbol=symbol,
                locus=row["Gene Names (ordered locus)"] or None,
                uniprot_reviewed=row["Reviewed"] == "reviewed",
                tier=1 if sole else 2,
                leaf_ibas_sole_seeded=sum(s["leaf_ibas"] for s in sole),
                leaf_ibas_total=sum(s["leaf_ibas"] for s in segs),
                review_folder=next((f"genes/PSEAE/{n}" for n in gene_names + [acc] if n in existing), None),
                seedings=sorted(segs, key=lambda s: -s["leaf_ibas"]),
            )
        )
    entries.sort(key=lambda e: (e["tier"], -e["leaf_ibas_sole_seeded"], -e["leaf_ibas_total"]))
    for i, e in enumerate(entries, 1):
        e["rank"] = i

    all_segs = [s for e in entries for s in e["seedings"]]
    doc = dict(
        generated=date.today().isoformat(),
        generator="projects/PSEUDOCAP/build_iba_seed_worklist.py",
        summary=dict(
            pao1_seed_proteins=len({s["acc"] for s in seedings}),
            pao1_node_term_seedings=len(seedings),
            pseudocap_supported_proteins=len(entries),
            pseudocap_supported_seedings=len(all_segs),
            tier1_proteins=sum(e["tier"] == 1 for e in entries),
            sole_seeded_node_terms=sum(s["sole_seed"] for s in all_segs),
            leaf_ibas_downstream=sum(s["leaf_ibas"] for s in all_segs),
            leaf_ibas_sole_seeded=sum(s["leaf_ibas"] for s in all_segs if s["sole_seed"]),
        ),
        genes=entries,
    )
    with open(OUT, "w") as f:
        yaml.safe_dump(doc, f, sort_keys=False, width=200)
    print(yaml.safe_dump(doc["summary"], sort_keys=False))


if __name__ == "__main__":
    main()
