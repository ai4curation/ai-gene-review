"""Re-review analysis for horse CTDSP2 (F7A4N8): gene-model structure and phylogenetic placement.

Fetches (once, then reuses) UniProt sequences and the Ensembl gene model for
ENSECAG00000018788, then:
  1. lists the Ensembl transcripts of the horse CTDSP2 gene and their exons;
  2. locates the point where each horse CTDSP2 product diverges from human CTDSP2 (O14595);
  3. checks for the FCP1-domain DxDx(T/V) catalytic motif (human D107/D109) in each product;
  4. builds a neighbour-joining tree of the catalytic-domain region of SCP-subfamily
     proteins (CTDSP1, CTDSP2, CTDSPL) from human, mouse, cow and horse to place the
     full-length horse product.

Run from the repository root:
    uv run python genes/HORSE/CTDSP2/CTDSP2-bioinformatics/compare_sequences_rereview.py
Outputs: rereview_sequences.fasta, rereview_ensembl_gene.json, RESULTS-rereview.md, results-rereview.json
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio import Align, Phylo, SeqIO
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

HERE = Path(__file__).resolve().parent
FASTA = HERE / "rereview_sequences.fasta"
ENSEMBL_JSON = HERE / "rereview_ensembl_gene.json"
GENE_ID = "ENSECAG00000018788"

# label -> UniProt accession. Gene names are as given by UniProt/PANTHER for each record.
ACCESSIONS = {
    "human_CTDSP2_O14595": "O14595",
    "human_CTDSP1_Q9GZU7": "Q9GZU7",
    "human_CTDSPL_O15194": "O15194",
    "mouse_Ctdsp2_Q8BX07": "Q8BX07",
    "mouse_Ctdsp1_P58466": "P58466",
    "cow_CTDSP2_Q2KJ43": "Q2KJ43",
    "horse_CTDSP1_F6Q9M8": "F6Q9M8",
    "horse_CTDSP2gene_A0A9L0T5X1": "A0A9L0T5X1",
    "horse_CTDSP2gene_A0A9L0R207": "A0A9L0R207",
    "horse_CTDSP2gene_F7A4N8": "F7A4N8",
}
HORSE_PRODUCTS = [
    "horse_CTDSP2gene_F7A4N8",
    "horse_CTDSP2gene_A0A9L0R207",
    "horse_CTDSP2gene_A0A9L0T5X1",
]
TREE_SET = [k for k in ACCESSIONS if k not in ("horse_CTDSP2gene_F7A4N8",)]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
    with urllib.request.urlopen(req) as r:
        return r.read().decode()


def load_sequences() -> dict[str, str]:
    if not FASTA.exists():
        parts = []
        for label, acc in ACCESSIONS.items():
            fa = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
            seq = "".join(fa.splitlines()[1:])
            parts.append(f">{label} {acc}\n{seq}\n")
        FASTA.write_text("".join(parts))
    return {r.id: str(r.seq) for r in SeqIO.parse(FASTA, "fasta")}


def load_gene_model() -> dict:
    if not ENSEMBL_JSON.exists():
        txt = fetch(
            f"https://rest.ensembl.org/lookup/id/{GENE_ID}?expand=1;content-type=application/json"
        )
        ENSEMBL_JSON.write_text(json.dumps(json.loads(txt), indent=1))
    return json.loads(ENSEMBL_JSON.read_text())


def aligner(mode: str = "global") -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = Align.substitution_matrices.load("BLOSUM62")
    a.mode = mode
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def identical_prefix(a: str, b: str) -> int:
    """Length of the identical-or-near-identical shared prefix, allowing isolated mismatches.

    >>> identical_prefix("MEHGSAAAA", "MEHGSAAAQ")
    9
    >>> identical_prefix("MEHG", "XXXX")
    0
    """
    n = 0
    window_mismatch = 0
    for i, (x, y) in enumerate(zip(a, b)):
        window_mismatch = window_mismatch + 1 if x != y else 0
        if window_mismatch >= 3:
            return n - 2
        n = i + 1
    return n


def motif_positions(seq: str) -> list[tuple[int, str]]:
    """1-based start positions of the FCP1 catalytic motif DxDx(T/V).

    >>> motif_positions("AAVIDLDETLV")
    [(5, 'DLDET')]
    """
    return [(m.start() + 1, seq[m.start() : m.start() + 5]) for m in re.finditer(r"(?=D.D.[TV])", seq)]


def identity(a: str, b: str) -> tuple[int, int]:
    aln = aligner("global").align(a, b)[0]
    pairs = [(x, y) for x, y in zip(str(aln[0]), str(aln[1])) if x != "-" and y != "-"]
    return sum(x == y for x, y in pairs), len(pairs)


def catalytic_region(seq: str) -> str:
    """Region from 10 residues before the first DxDx(T/V) motif to the end."""
    pos = motif_positions(seq)
    start = max(pos[0][0] - 11, 0) if pos else 0
    return seq[start:]


def main() -> None:
    seqs = load_sequences()
    gene = load_gene_model()
    human = seqs["human_CTDSP2_O14595"]
    out: dict = {"gene": {k: gene[k] for k in ("id", "display_name", "seq_region_name", "start", "end", "strand")}}

    tx_rows = []
    for t in gene["Transcript"]:
        exons = sorted(((e["start"], e["end"]) for e in t["Exon"]), reverse=True)
        tx_rows.append(
            {
                "transcript": t["id"],
                "is_canonical": bool(t.get("is_canonical")),
                "protein_length": t.get("Translation", {}).get("length"),
                "exons_genomic_minus_strand_order": exons,
            }
        )
    out["transcripts"] = tx_rows

    prod_rows = []
    for k in HORSE_PRODUCTS:
        s = seqs[k]
        # local alignment to human, to find the shared prefix and the motif.
        ident, paired = identity(human, s)
        prod_rows.append(
            {
                "product": k,
                "length": len(s),
                "shared_prefix_with_human_before_divergence": identical_prefix(human, s),
                "global_identity_vs_human": f"{ident}/{paired}",
                "DxDxT_motifs": motif_positions(s),
            }
        )
    out["human_motifs"] = motif_positions(human)
    out["products"] = prod_rows

    # Distance matrix from pairwise identity over the catalytic region.
    names = TREE_SET
    regions = {n: catalytic_region(seqs[n]) for n in names}
    matrix = []
    pid = {}
    for i, a in enumerate(names):
        row = []
        for j in range(i + 1):
            b = names[j]
            if i == j:
                row.append(0.0)
                continue
            ident, paired = identity(regions[a], regions[b])
            d = 1 - ident / paired
            pid[f"{a}|{b}"] = round(1 - d, 3)
            row.append(d)
        matrix.append(row)
    dm = DistanceMatrix(names, matrix)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup("human_CTDSPL_O15194")
    out["catalytic_region_pairwise_identity"] = pid
    newick_path = HERE / "rereview_tree.nwk"
    Phylo.write(tree, newick_path, "newick")
    out["tree_newick"] = newick_path.read_text().strip()

    horse = "horse_CTDSP2gene_A0A9L0T5X1"
    ranked = sorted(
        ((pid.get(f"{horse}|{n}") or pid.get(f"{n}|{horse}"), n) for n in names if n != horse),
        reverse=True,
    )
    out["A0A9L0T5X1_ranked_identity"] = ranked
    (HERE / "results-rereview.json").write_text(json.dumps(out, indent=2) + "\n")

    md = ["# CTDSP2 (horse) re-review: gene model and phylogenetic placement", ""]
    md.append(
        f"Generated by `compare_sequences_rereview.py` from UniProt sequences ({FASTA.name}) and the Ensembl gene model "
        f"for {GENE_ID} ({ENSEMBL_JSON.name}). Values are computed, not hand-entered."
    )
    md += ["", "## Ensembl transcripts of the horse CTDSP2 gene", "", "| Transcript | Ensembl canonical | Protein length | Exons (genomic, transcript order) |", "|---|---|---|---|"]
    for r in tx_rows:
        ex = "; ".join(f"{a}-{b} ({a - b + 1} bp)" for b, a in [(e[0], e[1]) for e in r["exons_genomic_minus_strand_order"]])
        md.append(f"| {r['transcript']} | {r['is_canonical']} | {r['protein_length']} | {ex} |")
    md += ["", "## Horse CTDSP2-gene products compared with human CTDSP2 (O14595)", "", f"Human DxDx(T/V) motif(s): {out['human_motifs']}", "", "| Product | Length | Shared prefix with human before divergence | Global identity vs human (identical/paired) | DxDx(T/V) motifs |", "|---|---|---|---|---|"]
    for r in prod_rows:
        md.append(f"| {r['product']} | {r['length']} | {r['shared_prefix_with_human_before_divergence']} | {r['global_identity_vs_human']} | {r['DxDxT_motifs'] or 'none'} |")
    md += ["", "## Placement of the full-length horse product A0A9L0T5X1", "", "Pairwise identity over the catalytic region (from 10 residues before the first DxDx(T/V) motif to the C-terminus), ranked:", "", "| Comparator | Identity |", "|---|---|"]
    for v, n in ranked:
        md.append(f"| {n} | {v} |")
    md += ["", "Neighbour-joining tree (rooted on human CTDSPL):", "", "```", out["tree_newick"], "```", ""]
    (HERE / "RESULTS-rereview.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
