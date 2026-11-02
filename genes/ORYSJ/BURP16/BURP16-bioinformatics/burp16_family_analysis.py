"""OsBURP16 (Q7XES5) family placement and motif analysis.

1. Locate Q7XES5 in the PANTHER PTHR31458 tree, print its ancestor path, list
   the leaves sharing its clade below the grass duplication node PTN000779097,
   and test whether it descends from the only PAINT IBD node in the family
   (PTN004827911, interpro/panther/PTHR31458/PTHR31458-paint.tsv).
2. Scan Q7XES5 and characterised PTHR31458 members for the PG1beta repeat
   (F[TS]xYG strict, FxxY loose) and BURP-domain CH dipeptides.
3. Global pairwise identity (BLOSUM62, gap -10/-0.5) of Q7XES5 to comparators.

Run: uv run --with biopython python burp16_family_analysis.py
"""
import json
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

FAMILY = "PTHR31458"
PAINT_NODE = "PTN004827911"
TARGET = "Q7XES5"
DUP_NODE = "PTN000779097"
COMPARATORS = {
    "Q6ZA27": "OsBURP12 (rice)",
    "Q6K2M1": "OsBURP14 (rice)",
    "Q40161": "GP1 PG1beta subunit (tomato)",
    "O80760": "PGL2 (Arabidopsis)",
    "P92990": "PGL3 (Arabidopsis)",
    "P92982": "PGL1 (Arabidopsis)",
}
STRICT = re.compile(r"F[TS].YG")
LOOSE = re.compile(r"(?=(F..Y))")
CH = re.compile(r"CH")


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    return urllib.request.urlopen(req).read()


def fasta(acc: str) -> str:
    text = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").decode()
    return "".join(text.splitlines()[1:])


def leaves_with_paths(node, path, out):
    step = (node.get("persistent_id"), node.get("prop_sf_id"), node.get("species"), node.get("event_type"))
    path = path + [step]
    children = node.get("children", {}).get("annotation_node", [])
    if isinstance(children, dict):
        children = [children]
    if not children:
        out.append((node, path))
    for child in children:
        leaves_with_paths(child, path, out)
    return out


def tree_section() -> None:
    data = json.loads(get(f"https://pantherdb.org/services/oai/pantherdb/treeinfo?family={FAMILY}"))
    root = data["search"]["tree_topology"]["annotation_node"]
    leaves = leaves_with_paths(root, [], [])
    print(f"## PANTHER tree: version {data['search']['product']['version']}; {len(leaves)} leaves")
    target = [(n, p) for n, p in leaves if f"UniProtKB={TARGET}" in (n.get("node_name") or "")]
    if not target:
        print(f"{TARGET}\tNOT_IN_TREE")
        return
    node, path = target[0]
    ids = [p[0] for p in path]
    print(f"{TARGET}\t{node.get('gene_symbol')}\t{node.get('prop_sf_id')}\tunder_{PAINT_NODE}={PAINT_NODE in ids}")
    for step in path:
        print("\t" + "\t".join(str(x) for x in step))
    print(f"\n## Leaves below {DUP_NODE} (grass duplication)")
    for n, p in leaves:
        pids = [s[0] for s in p]
        if DUP_NODE in pids:
            child = pids[pids.index(DUP_NODE) + 1]
            print(f"{child}\t{n.get('organism')}\t{n.get('gene_symbol')}\t{n.get('node_name')}")


def motif_section(seqs: dict) -> None:
    print("\n## Motifs\nacc\tlength\tF[TS]xYG\tFxxY\tCH_positions")
    for acc, s in seqs.items():
        print(f"{acc}\t{len(s)}\t{len(STRICT.findall(s))}\t{len(LOOSE.findall(s))}\t{[m.start() + 1 for m in CH.finditer(s)]}")


def identity_section(seqs: dict) -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    t = seqs[TARGET]
    print(f"\n## Global identity vs {TARGET}\nacc\tlabel\tidentical/aligned_pairs\tidentity_over_target_length")
    for acc, label in COMPARATORS.items():
        aln = aligner.align(t, seqs[acc])[0]
        ident = aligned = 0
        for (a0, a1), (b0, b1) in zip(*aln.aligned):
            for i, j in zip(range(a0, a1), range(b0, b1)):
                aligned += 1
                ident += t[i] == seqs[acc][j]
        print(f"{acc}\t{label}\t{ident}/{aligned}={ident / aligned:.3f}\t{ident / len(t):.3f}")


def main() -> None:
    tree_section()
    seqs = {acc: fasta(acc) for acc in [TARGET, *COMPARATORS]}
    motif_section(seqs)
    identity_section(seqs)


if __name__ == "__main__":
    main()
