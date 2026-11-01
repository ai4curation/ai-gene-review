# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Pairwise global alignment of Srlp (Q9VG69) against characterised crotonase-fold
enzymes and its fly SF1 paralog CG5611, reporting which Srlp residue aligns to each
reference ACT_SITE/BINDING/SITE position (positions read live from UniProt FT lines).
Also prints PANTHER cross-references for each sequence and a simple N-terminal
composition summary (presequence-like features) for the target.

Usage: uv run active_site_check.py > active_site_check.out
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q9VG69"
REFS = ["P14604", "Q93TU6", "Q2LXU2", "Q9VB17", "Q20376", "Q6NL24"]
# Literature catalytic glutamates of rat ECHS1 (precursor numbering E144, E164) that the
# UniProt feature table does not list as ACT_SITE; checked explicitly in addition to FT lines.
EXTRA = {"P14604": [144, 164]}


def fetch(acc: str) -> str:
    return requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).text


def seq_of(txt: str) -> str:
    s = txt.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", s)


def panther(txt: str) -> list[str]:
    return re.findall(r"^DR   PANTHER; (\S+);", txt, re.M)


def features(txt: str) -> list[tuple[str, int, str]]:
    out = []
    for m in re.finditer(r"^FT   (ACT_SITE|BINDING|SITE)\s+(\d+)\s*\n((?:FT {19}.*\n)*)", txt, re.M):
        note = " ".join(re.findall(r'/(?:note|ligand)="([^"]*)"', m.group(3)))
        out.append((m.group(1), int(m.group(2)), note))
    return out


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    ttxt = fetch(TARGET)
    t = seq_of(ttxt)
    print(f"target {TARGET} length {len(t)} PANTHER {panther(ttxt)}")
    nterm = t[:30]
    print(f"N-terminal 30 aa: {nterm}  R+K={sum(c in 'RK' for c in nterm)} D+E={sum(c in 'DE' for c in nterm)}")
    for acc in REFS:
        txt = fetch(acc)
        r = seq_of(txt)
        aln = aligner.align(t, r)[0]
        rmap = {}
        ident = aligned = 0
        for (ts, te), (rs, re_) in zip(*aln.aligned):
            for k in range(te - ts):
                rmap[rs + k + 1] = ts + k + 1
                aligned += 1
                ident += t[ts + k] == r[rs + k]
        print(f"\n== {acc} length {len(r)} PANTHER {panther(txt)}; aligned {aligned}, identity {ident/aligned:.1%} over aligned columns")
        for kind, pos, note in features(txt):
            tp = rmap.get(pos)
            tres = t[tp - 1] if tp else "-"
            print(f"  {kind} {acc} {r[pos-1]}{pos} [{note}] -> {TARGET} {tres}{tp if tp else ''}")
        for pos in EXTRA.get(acc, []):
            tp = rmap.get(pos)
            tres = t[tp - 1] if tp else "-"
            print(f"  LITERATURE_CATALYTIC {acc} {r[pos-1]}{pos} -> {TARGET} {tres}{tp if tp else ''}")
        print("  full global alignment (Srlp shown as target, reference as query):")
        lines = str(aln).splitlines()
        print("\n".join("    " + ln for ln in lines))


if __name__ == "__main__":
    main()
