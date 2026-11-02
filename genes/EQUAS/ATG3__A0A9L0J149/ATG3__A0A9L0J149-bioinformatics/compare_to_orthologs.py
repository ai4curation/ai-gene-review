# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare donkey ATG3 A0A9L0J149 to experimentally characterised ATG3 orthologs.

Fetches sequences and PANTHER cross-references from UniProt REST, makes global
pairwise alignments, and reports whether functionally characterised human ATG3
(Q9NT62) residues/motifs are conserved at the aligned positions in the donkey protein.
"""
import sys
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "A0A9L0J149"
REFS = {"Q9NT62": "human ATG3", "Q9CPX6": "mouse Atg3", "P40344": "yeast Atg3"}
# Human positions (Q9NT62 numbering) from the Swiss-Prot record features
FEATURES = {
    "membrane-curvature-sensing N-terminal amphipathic helix (4-19)": (4, 19),
    "Lys9/Lys11 (anionic-lipid recognition, PMID:29142222)": [(9, 9), (11, 11)],
    "LIR motif (104-110, PMID:37252361)": (104, 110),
    "ATG12-interacting region (140-170, PMID:24191030)": (140, 170),
    "caspase-8 LETD motif (166-169)": (166, 169),
    "ATG12 acceptor Lys243": (243, 243),
    "catalytic Cys264 (glycyl thioester)": (264, 264),
}


def fetch(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    d = r.json()
    panther = [x["id"] for x in d.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"]
    return {"seq": d["sequence"]["value"], "panther": panther}


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def pos_map(aln) -> dict[int, int | None]:
    """Map 1-based ref (second seq) positions to 1-based target (first seq) positions."""
    m: dict[int, int | None] = {}
    for (ts, te), (rs, re_) in zip(*aln.aligned):
        for i in range(re_ - rs):
            m[rs + i + 1] = ts + i + 1
    return m


def main() -> None:
    tgt = fetch(TARGET)
    print(f"{TARGET} length={len(tgt['seq'])} PANTHER={tgt['panther']}")
    al = aligner()
    for acc, name in REFS.items():
        ref = fetch(acc)
        aln = al.align(tgt["seq"], ref["seq"])[0]
        ident = sum(1 for (ts, te), (rs, re_) in zip(*aln.aligned)
                    for i in range(te - ts) if tgt["seq"][ts + i] == ref["seq"][rs + i])
        print(f"\n{acc} ({name}) length={len(ref['seq'])} PANTHER={ref['panther']}")
        print(f"  identical aligned residues: {ident}; identity over shorter seq: "
              f"{100 * ident / min(len(tgt['seq']), len(ref['seq'])):.1f}%")
        if acc != "Q9NT62":
            continue
        m = pos_map(aln)
        for label, spans in FEATURES.items():
            spans = spans if isinstance(spans, list) else [spans]
            for s, e in spans:
                r = ref["seq"][s - 1:e]
                tpos = [m.get(p) for p in range(s, e + 1)]
                t = "".join(tgt["seq"][p - 1] if p else "-" for p in tpos)
                print(f"  {label}: human {s}-{e} {r} | donkey {tpos[0]}-{tpos[-1]} {t} | "
                      f"{'identical' if r == t else 'DIFFERS'}")


if __name__ == "__main__":
    sys.exit(main())
