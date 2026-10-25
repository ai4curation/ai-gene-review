"""Compare blue whale CDK16 products (GeneID 118888515) with human CDK16 (Q00536).

Fetches sequences from UniProt REST, maps each whale product onto human
isoform 1 coordinates, and reports whether residues known from human/mouse
experiments to matter for CDK16 activity and regulation are present.

Run: python3 compare_isoforms.py  (standard library only; needs network access)
"""
from difflib import SequenceMatcher
import urllib.request

ACCS = ["Q00536", "A0A8B8WEG2", "A0A8B8WEF1", "A0A8B8WEA8", "A0A8C0DX89"]

# Human CDK16 isoform-1 positions with experimental relevance
# (Mikolcevic 2012 PMID:22184064; Chen 2012 PMID:22798068; Fu 2011 PMID:21335063;
#  UniProt Q00536 FT ACT_SITE/BINDING).
SITES = {
    12: "Ser12, BRSK2 phosphosite (insulin secretion regulation)",
    95: "Ser95, CDK5 phosphosite (dendrite development)",
    112: "start of conserved CCNY-binding segment 112-121",
    119: "Ser119, required for CCNY binding",
    153: "Ser153, PKA site; phosphorylation blocks CCNY binding",
    158: "Gly158, required for CCNY binding",
    194: "Lys194, catalytic ATP-binding lysine (K194R kinase-dead)",
    286: "Asp286, catalytic proton acceptor (HRD)",
    461: "start of conserved C-terminal segment 461-473 needed for CCNY binding",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(lines[1:])


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    human = seqs["Q00536"]
    for acc in ACCS[1:]:
        s = seqs[acc]
        m = SequenceMatcher(None, human, s, autojunk=False)
        blocks = [b for b in m.get_matching_blocks() if b.size > 0]
        hmap = {}
        for b in blocks:
            for i in range(b.size):
                hmap[b.a + i] = b.b + i
        covered = len(hmap)
        print(f"## {acc}: length {len(s)}; identical aligned residues vs human isoform 1: "
              f"{covered}/{len(human)}; first aligned human residue {min(hmap) + 1}")
        for pos, note in SITES.items():
            j = hmap.get(pos - 1)
            if j is None:
                print(f"  human {pos} ({note}): ABSENT/not identical")
            else:
                print(f"  human {pos} ({note}): present as {s[j]}{j + 1}")


if __name__ == "__main__":
    main()
