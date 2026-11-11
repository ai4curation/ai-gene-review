"""Kinase catalytic residues across the DDR clade of PTHR24416, mapped onto the PANTHER tree.

For every leaf below the PAINT DDR node PTN002400507 (the node carrying the
GO:0038062 protein tyrosine kinase collagen receptor activity IBD), this script:

1. downloads the leaf's UniProt sequence (the accession PANTHER gives for the leaf);
2. aligns it globally (BLOSUM62) to human DDR2 (UniProtKB:Q16832);
3. reports the residue aligned to each of four canonical protein-kinase catalytic
   positions, located on DDR2 by motif search: the beta3 lysine (VAVK), the HRD
   aspartate and the catalytic-loop asparagine (HRDLATRN) and the DFG aspartate (ADFG);
4. summarises, for every internal node of the DDR subtree, how many leaves keep
   the beta3 Lys, catalytic-loop Asn and DFG Asp (the three positions whose loss
   characterises Drosophila Ddr).

The tree comes from the PANTHER treeinfo API through ai_gene_review.etl.panther_trees
(cached under .cache/panther_trees/). Nothing is hard-coded but the motifs and the
node id. Run from the repository root:

    uv run python interpro/panther/PTHR24416/PTHR24416-bioinformatics/ddr_catalytic_residues.py
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

from ai_gene_review.etl.panther_trees import load_family

FAMILY = "PTHR24416"
DDR_NODE = "PTN002400507"
REFERENCE = "Q16832"  # human DDR2
# (motif on DDR2, offset of the catalytic residue within the motif, expected residue)
SITES = {
    "b3K": (r"VAVK", 3, "K"),
    "HRD_D": (r"HRDLATRN", 2, "D"),
    "catN": (r"HRDLATRN", 7, "N"),
    "DFG_D": (r"ADFG", 1, "D"),
}
TRIAD = ("b3K", "catN", "DFG_D")
# Central residues of the DDR2 collagen-binding pocket in the DS domain-collagen
# structure (PMID:20004161: "Trp52, Thr56, Asp69, Arg105, Glu113, and Cys73-Cys177
# disulfide bridge", strictly conserved in DDR1). DDR2 numbering; checked on the sequence.
POCKET = {"W52": 52, "T56": 56, "D69": 69, "C73": 73, "R105": 105, "E113": 113, "C177": 177}

POCKET_KEYS = tuple(POCKET)


def expected(site: str) -> str:
    """Expected residue at a named site (kinase motif site or DDR2 pocket position)."""
    return SITES[site][2] if site in SITES else site[0]


def fetch(acc: str) -> str:
    """Canonical UniProt sequence for an accession."""
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    try:
        with urllib.request.urlopen(url, timeout=60) as fh:
            lines = fh.read().decode().splitlines()
    except urllib.error.HTTPError as err:  # retired or unknown accession: record, don't abort
        if err.code in (400, 404, 410):
            return ""
        raise
    return "".join(x.strip() for x in lines if not x.startswith(">"))


def aligner() -> Align.PairwiseAligner:
    """Global BLOSUM62 aligner with affine gaps."""
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al


def position_map(aln) -> dict[int, int | None]:
    """Map 1-based reference positions to 1-based query positions (None for a gap)."""
    out: dict[int, int | None] = {}
    for t, q in zip(*aln.indices):
        if t >= 0:
            out[t + 1] = (q + 1) if q >= 0 else None
    return out


def main() -> None:
    tree = load_family(FAMILY)
    if tree is None:
        sys.exit(f"could not load the {FAMILY} tree")
    leaves, under = tree["leaves"], tree["under"]
    ddr_leaves = under[DDR_NODE]
    ref = fetch(REFERENCE)
    sites = {}
    for name, (pat, off, exp) in SITES.items():
        m = re.search(pat, ref)
        if m is None or ref[m.start() + off] != exp:
            sys.exit(f"{name}: motif {pat} not found as expected in {REFERENCE}")
        sites[name] = m.start() + off + 1
    for name, pos in POCKET.items():
        if ref[pos - 1] != name[0]:
            sys.exit(f"{REFERENCE} residue {pos} is {ref[pos - 1]}, expected {name[0]}")
        sites[name] = pos
    print(f"Reference {REFERENCE} positions: " + ", ".join(f"{k}={v}" for k, v in sites.items()))

    al = aligner()
    calls: dict[str, dict[str, str]] = {}
    print("\nleaf\tuniprot\torganism\t" + "\t".join(list(SITES) + list(POCKET)) + "\tkinase_triad\tpocket")
    for leaf in ddr_leaves:
        info = leaves[leaf]
        acc = info.get("uniprot")
        seq = fetch(acc)
        if not seq:  # accession retired or merged in UniProt since the PANTHER release
            print(f"{leaf}\t{acc}\t{info.get('organism')}\t" + "\t".join("?" * (len(SITES) + len(POCKET)))
                  + "\tunavailable\tunavailable")
            continue
        pmap = position_map(al.align(ref, seq)[0])
        row = {}
        for name, pos in sites.items():
            q = pmap.get(pos)
            row[name] = f"{seq[q - 1]}{q}" if q else "-"
        calls[leaf] = row
        print(f"{leaf}\t{acc}\t{info.get('organism')}\t" + "\t".join(row.values())
              + f"\t{triad_state(row)}\t{triad_state(row, POCKET_KEYS)}")

    print("\nInternal nodes of the DDR subtree (smallest first). Leaf states over b3K, catN and "
          "DFG_D: kept = all three present; substituted = at least one replaced by another "
          "residue; not_covered = no substitution but at least one position falls in an "
          "alignment gap (fragmentary model); unavailable = no sequence.")
    print("node\tleaves\tkin_kept\tkin_subst\tkin_notcov\tkin_unavail"
          "\tpocket_kept\tpocket_subst\tpocket_notcov\tpocket_unavail\tspecies")
    ddr_set = set(ddr_leaves)
    nodes = sorted((len(v), k) for k, v in under.items() if set(v) <= ddr_set and len(v) > 1)
    for n, node in nodes:
        counts = []
        for keys in (TRIAD, POCKET_KEYS):
            states = [triad_state(calls[x], keys) if x in calls else "unavailable"
                      for x in under[node]]
            counts += [states.count(k) for k in ("kept", "substituted", "not_covered", "unavailable")]
        orgs = sorted({leaves[x].get("organism") for x in under[node]})
        shown = ", ".join(orgs) if len(orgs) <= 6 else f"{len(orgs)} species"
        print(f"{node}\t{n}\t" + "\t".join(map(str, counts)) + f"\t{shown}")


def triad_state(row: dict[str, str], keys: tuple[str, ...] = TRIAD) -> str:
    """Classify a leaf by its calls at ``keys`` (default: b3K, catN and DFG_D).

    >>> triad_state({"b3K": "K10", "HRD_D": "D20", "catN": "N25", "DFG_D": "D38"})
    'kept'
    >>> triad_state({"b3K": "A10", "HRD_D": "D20", "catN": "S25", "DFG_D": "S38"})
    'substituted'
    >>> triad_state({"b3K": "-", "HRD_D": "D20", "catN": "N25", "DFG_D": "D38"})
    'not_covered'
    """
    vals = [row[t] for t in keys]
    if any(v != "-" and v[0] != expected(t) for t, v in zip(keys, vals)):
        return "substituted"
    if any(v == "-" for v in vals):
        return "not_covered"
    return "kept"

if __name__ == "__main__":
    main()
