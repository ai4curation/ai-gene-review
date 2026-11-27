"""Catalytic-motif check for DIRS-1 ORF2 (O96849) and its identical-length copy Q23898.

Fetches sequences from UniProt and Pfam HMMs from InterPro, runs hmmsearch
(HMMER must be on PATH) and reports which target residues align to the
conserved catalytic positions of each domain. Positive controls: reviewed
phage Dam N6-adenine methyltransferases (P51715, Q38156) carrying motif IV NPPY.

Run: uv run python motif_check.py
"""

import gzip
import re
import subprocess
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
WORK = HERE / "work"
ACCS = ["O96849", "Q23898", "P51715", "Q38156"]
PFAMS = {"PF05869": "Dam MTase", "PF00078": "RVT_1", "PF17917": "RT_RNaseH"}


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url) as r:
        return r.read()


def get_seqs() -> dict[str, str]:
    seqs = {}
    for a in ACCS:
        txt = fetch(f"https://rest.uniprot.org/uniprotkb/{a}.fasta").decode()
        seqs[a] = "".join(txt.split("\n")[1:])
    return seqs


def get_hmm(pf: str) -> Path:
    p = WORK / f"{pf}.hmm"
    if not p.exists():
        data = fetch(f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{pf}?annotation=hmm")
        p.write_bytes(gzip.decompress(data))
    return p


def main() -> None:
    WORK.mkdir(exist_ok=True)
    seqs = get_seqs()
    fa = WORK / "seqs.fa"
    fa.write_text("".join(f">{a}\n{s}\n" for a, s in seqs.items()))
    o, q = seqs["O96849"], seqs["Q23898"]
    diffs = [(i + 1, x, y) for i, (x, y) in enumerate(zip(o, q)) if x != y]
    print(f"O96849 length {len(o)}, Q23898 length {len(q)}; {len(diffs)} differences: {diffs}")
    print("Regex motif scan (whole sequence):")
    for a, s in seqs.items():
        yxdd = [(m.start() + 1, m.group()) for m in re.finditer("Y.DD", s)]
        m4 = [(m.start() + 1, m.group()) for m in re.finditer("[DNSH]PP[YFW]", s)]
        print(f"  {a}: YXDD={yxdd} MTase motif IV [DNSH]PP[YFW]={m4}")
    print("Residues at candidate catalytic positions in O96849 (1-based):")
    for label, pos in [("RT Mg D (UniProt FT)", 99), ("RT YXDD D", 165), ("RT YXDD D", 166),
                       ("RNase H D (TDASE)", 331), ("RNase H E (TDASE)", 334),
                       ("RNase H E (REMLA)", 368), ("RNase H D (QTDN)", 393),
                       ("RNase H D? (KADH)", 443), ("Dam motif IV pos1 (N in NPPY)", 519),
                       ("Dam motif IV pos4 (Y in NPPY)", 522)]:
        print(f"  {label} {pos}: {o[pos - 1]}  context {o[pos - 4:pos + 3]}")
    for pf, name in PFAMS.items():
        hmm = get_hmm(pf)
        out = WORK / f"{pf}.out"
        subprocess.run(
            ["hmmsearch", "--domE", "10", "-E", "10", "-o", str(out), str(hmm), str(fa)],
            check=True,
        )
        print(f"\n===== hmmsearch {pf} ({name}) =====")
        text = out.read_text()
        start = text.find("Domain annotation for each sequence")
        end = text.find("Internal pipeline statistics")
        print(text[start:end])


if __name__ == "__main__":
    main()
