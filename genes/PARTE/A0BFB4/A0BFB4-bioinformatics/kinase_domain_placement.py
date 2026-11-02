"""Kinase-domain placement of Paramecium A0BFB4 against a panel of characterised kinases.

Reproducible check, independent of any ML function predictions:

1. Fetch the UniProt record for A0BFB4 and each panel protein and cut out the
   annotated "Protein kinase" domain (UniProt FT DOMAIN feature).
2. Align the kinase domains with MAFFT (L-INS-i).
3. Report pairwise percent identity of A0BFB4 to every panel member over the
   aligned columns where both are non-gap.
4. Build a neighbour-joining tree (BLOSUM62 distance) with 200 bootstrap
   replicates and report which panel members A0BFB4 groups with and the
   bootstrap support for the smallest clade containing A0BFB4 and each
   reference group.

Run:  uv run python kinase_domain_placement.py
Outputs: kinase_domains.fasta, kinase_domains.aln.fasta, nj_tree.nwk,
         placement_results.json (all computed, nothing hard-coded).
"""

import json
import random
import subprocess
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
TARGET = "A0BFB4"

# accession -> reference group (group label is the a-priori classification used to
# interpret the tree; it is not used to build the tree)
PANEL = {
    "O75385": "ATG1/ULK",  # human ULK1
    "Q8IYT8": "ATG1/ULK",  # human ULK2
    "P53104": "ATG1/ULK",  # S. cerevisiae ATG1
    "Q23023": "ATG1/ULK",  # C. elegans unc-51
    "Q6PHR2": "ULK3",  # human ULK3
    "Q14012": "CAMK",  # human CAMK1
    "Q16566": "CAMK",  # human CAMK4
    "Q9UQM7": "CAMK",  # human CAMK2A
    "O15075": "CAMK",  # human DCLK1
    "Q16816": "CAMK",  # human PHKG1 (phosphorylase kinase gamma)
    "O96017": "CHK2",  # human CHEK2
    "O14757": "CHK1",  # human CHEK1
    "Q13131": "AMPK",  # human PRKAA1
    "Q7KZI7": "MARK",  # human MARK2
    "O00311": "CDC7",  # human CDC7
    "O94804": "STE20",  # human STK10 (LOK)
    "Q9H2G2": "STE20",  # human SLK
}


def fetch_entry(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def kinase_domain(entry: dict) -> tuple[str, int, int]:
    seq = entry["sequence"]["value"]
    doms = [
        f
        for f in entry.get("features", [])
        if f["type"] == "Domain" and "kinase" in f.get("description", "").lower()
    ]
    d = doms[0]
    start = d["location"]["start"]["value"]
    end = d["location"]["end"]["value"]
    return seq[start - 1 : end], start, end


def pid(a: str, b: str) -> float:
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    same = sum(1 for x, y in pairs if x == y)
    return round(100.0 * same / len(pairs), 1)


def smallest_clade_with(tree, names: list[str]):
    return tree.common_ancestor(names)


def main() -> None:
    records = []
    meta = {}
    for acc in [TARGET, *PANEL]:
        e = fetch_entry(acc)
        dom, s, en = kinase_domain(e)
        gene = (e.get("genes") or [{}])[0].get("geneName", {}).get("value", "")
        if not gene:
            gene = (e.get("genes") or [{}])[0].get("orfNames", [{}])[0].get("value", acc)
        org = e["organism"]["scientificName"]
        meta[acc] = {
            "gene": gene,
            "organism": org,
            "length": e["sequence"]["length"],
            "kinase_domain": [s, en],
            "group": PANEL.get(acc, "TARGET"),
        }
        records.append(f">{acc}\n{dom}\n")
    fasta = HERE / "kinase_domains.fasta"
    fasta.write_text("".join(records))
    aln_path = HERE / "kinase_domains.aln.fasta"
    out = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fasta)],
        check=True,
        capture_output=True,
        text=True,
    )
    aln_path.write_text(out.stdout)
    aln = AlignIO.read(aln_path, "fasta")
    seqs = {r.id: str(r.seq) for r in aln}

    identities = sorted(
        (
            {
                "accession": acc,
                "gene": meta[acc]["gene"],
                "group": meta[acc]["group"],
                "pct_identity": pid(seqs[TARGET], seqs[acc]),
            }
            for acc in PANEL
        ),
        key=lambda d: -d["pct_identity"],
    )

    calc = DistanceCalculator("blosum62")
    constructor = DistanceTreeConstructor(calc, "nj")
    tree = constructor.build_tree(aln)
    tree.root_with_outgroup("O00311")  # CDC7 as a distant outgroup
    Phylo.write(tree, HERE / "nj_tree.nwk", "newick")

    # nearest neighbours of the target in the NJ tree: members of the smallest
    # clade (excluding the root) that contains the target and at least one other leaf
    target_leaf = next(t for t in tree.get_terminals() if t.name == TARGET)
    path = tree.get_path(target_leaf)
    sister = None
    for node in reversed(path[:-1]):
        leaves = [t.name for t in node.get_terminals()]
        if len(leaves) > 1:
            sister = sorted(n for n in leaves if n != TARGET)
            break
    if sister is None:
        sister = sorted(t.name for t in tree.get_terminals() if t.name != TARGET)

    # bootstrap: fraction of replicates in which target forms a clade with each group
    random.seed(1)
    ncol = aln.get_alignment_length()
    groups = sorted({g for g in PANEL.values()})
    support = {g: 0 for g in groups}
    sister_counts: dict[str, int] = {}
    nrep = 200
    from Bio.Align import MultipleSeqAlignment
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord

    for _ in range(nrep):
        cols = [random.randrange(ncol) for _ in range(ncol)]
        rep = MultipleSeqAlignment(
            [
                SeqRecord(Seq("".join(r.seq[c] for c in cols)), id=r.id)
                for r in aln
            ]
        )
        t = constructor.build_tree(rep)
        t.root_with_outgroup("O00311")
        for g in groups:
            members = [a for a, gg in PANEL.items() if gg == g]
            clade = t.common_ancestor([TARGET, *members])
            names = {x.name for x in clade.get_terminals()}
            if names == {TARGET, *members}:
                support[g] += 1
        tl = next(x for x in t.get_terminals() if x.name == TARGET)
        p = t.get_path(tl)
        for node in reversed(p[:-1]):
            leaves = [x.name for x in node.get_terminals()]
            if len(leaves) > 1:
                key = ",".join(sorted(meta[n]["gene"] for n in leaves if n != TARGET))
                sister_counts[key] = sister_counts.get(key, 0) + 1
                break

    results = {
        "target": TARGET,
        "metadata": meta,
        "alignment_columns": ncol,
        "identity_to_target_ranked": identities,
        "nj_sister_of_target": [
            {"accession": a, "gene": meta[a]["gene"], "group": meta[a]["group"]}
            for a in sister
        ],
        "bootstrap_replicates": nrep,
        "bootstrap_target_plus_group_exact_clade": support,
        "bootstrap_sister_sets": dict(
            sorted(sister_counts.items(), key=lambda kv: -kv[1])[:10]
        ),
    }
    (HERE / "placement_results.json").write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))
    Phylo.draw_ascii(tree)


if __name__ == "__main__":
    main()
