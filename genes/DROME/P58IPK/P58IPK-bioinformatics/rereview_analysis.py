# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Re-review analysis for Drosophila P58IPK (Q9VHA8).

1. Pairwise global identity of Q9VHA8 against DNAJC3 (human, mouse), yeast JEM1,
   C. elegans DNJ-7 and the second fly entry Q7K3H7.
2. J-domain HPD motif presence in each sequence.
3. Ancestral-node path of model-organism leaves in the PANTHER PTHR44140 tree
   (PANTHER treeinfo API), to place the fly gene relative to DNAJC3 and JEM1.
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q9VHA8": "fly P58IPK (target)",
    "Q7K3H7": "fly second UniProt entry, FBgn0037718?",
    "Q13217": "human DNAJC3",
    "Q91YW3": "mouse Dnajc3",
    "P40358": "yeast JEM1",
    "P91189": "worm dnj-7",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a: str, b: str) -> tuple[float, int]:
    al = Align.PairwiseAligner(mode="global")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    aln = al.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(x == y for x, y in pairs)
    return 100.0 * ident / min(len(a), len(b)), len(pairs)


def tree_paths() -> list[str]:
    url = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR44140"
    d = requests.get(url, timeout=120).json()
    out = []

    def walk(n, path):
        if isinstance(n, list):
            for x in n:
                walk(x, path)
            return
        me = f"{n.get('persistent_id')}({n.get('event_type', '') or '-'}:{n.get('species', '') or ''})"
        kids = n.get("children")
        if kids:
            walk(kids["annotation_node"], path + [me])
        else:
            gid = n.get("gene_id") or ""
            if any(k in gid for k in ("FlyBase", "HGNC", "SGD", "WormBase", "MGI")):
                out.append(f"{n.get('gene_symbol')} {gid} {n.get('prop_sf_id')}: " + " > ".join(path))

    walk(d["search"]["tree_topology"]["annotation_node"], [])
    return out


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    target = seqs["Q9VHA8"]
    print("accession\tdescription\tlength\tidentity_to_Q9VHA8_pct\taligned_cols\tHPD_present")
    for a, desc in ACCS.items():
        pid, cols = identity(target, seqs[a])
        print(f"{a}\t{desc}\t{len(seqs[a])}\t{pid:.1f}\t{cols}\t{'HPD' in seqs[a]}")
    print(f"Q9VHA8 == Q7K3H7 sequence: {seqs['Q9VHA8'] == seqs['Q7K3H7']}")
    print("\nPANTHER PTHR44140 leaf paths (root > ... > parent):")
    for line in tree_paths():
        print(line)


if __name__ == "__main__":
    main()
