"""Compare the zebrafish brorin (VWC2) paralogs si:dkey-283b1.7 and vwc2 with
their human, spotted gar and medaka relatives, and with the VWC2L (brorin-like)
lineage.

Questions:
  1. Which human gene (VWC2 or VWC2L) is each zebrafish protein closest to,
     over the whole protein and over the conserved core (the two VWFC /
     chordin-like cysteine-rich domains of human VWC2, residues 153-274)?
  2. Are the core cysteines of human VWC2 kept in each zebrafish copy?
  3. How much of the N-terminal (pre-core) region is shared?

Sequences: zebrafish si:dkey-283b1.7 (E7F8B1) and vwc2 (B0I1T8) from the cached
UniProt records in this repository; everything else from the UniProt REST API
(accessions are the PANTHER v19 ortholog calls for PTHR46252 used in
projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv).

Run from the repository root:
    uv run python genes/DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/protein_compare.py
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
GENES = ROOT / "genes" / "DANRE"

LOCAL = {
    "zf si:dkey-283b1.7 (E7F8B1)": GENES / "si_dkey-283b1.7" / "si_dkey-283b1.7-uniprot.txt",
    "zf vwc2 (B0I1T8)": GENES / "vwc2" / "vwc2-uniprot.txt",
}
REMOTE = {
    "human VWC2 (Q2TAL6)": "Q2TAL6",
    "human VWC2L (B2RUY7)": "B2RUY7",
    "gar vwc2 (W5MCB8)": "W5MCB8",
    "gar vwc2l (W5MAF2)": "W5MAF2",
    "medaka co-ortholog of si:dkey-283b1.7 (A0A3B3HFT2)": "A0A3B3HFT2",
    "medaka co-ortholog of vwc2 (A0A3B3H832)": "A0A3B3H832",
    "zf vwc2l (B0UZC8)": "B0UZC8",
}
REF = "human VWC2 (Q2TAL6)"
CORE = (153, 274)  # VWFC 1 + VWFC 2 of human VWC2 (UniProt features)


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def fetch_json(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    return json.loads(urllib.request.urlopen(url, timeout=60).read())


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner(mode="global")
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def columns(aln):
    """Yield (i, j) 0-based index pairs (None for a gap) for each alignment column."""
    s1, s2 = aln.sequences
    (b1, b2) = aln.aligned
    i = j = 0
    blocks = list(zip(b1, b2))
    for (a0, a1), (c0, c1) in blocks:
        while i < a0:
            yield i, None
            i += 1
        while j < c0:
            yield None, j
            j += 1
        for k in range(a1 - a0):
            yield a0 + k, c0 + k
        i, j = a1, c1
    while i < len(s1):
        yield i, None
        i += 1
    while j < len(s2):
        yield None, j
        j += 1


def identity(a: str, b: str) -> tuple[float, int]:
    aln = aligner().align(a, b)[0]
    cols = list(columns(aln))
    ident = sum(1 for i, j in cols if i is not None and j is not None and a[i] == b[j])
    return 100 * ident / len(cols), len(cols)


def region(ref_seq: str, other: str, start: int, end: int) -> str:
    """Residues of `other` aligned to ref_seq[start-1:end] (gaps dropped)."""
    aln = aligner().align(ref_seq, other)[0]
    out = []
    for i, j in columns(aln):
        if i is not None and start - 1 <= i <= end - 1 and j is not None:
            out.append(other[j])
    return "".join(out)


def main() -> None:
    seqs: dict[str, str] = {k: uniprot_txt_seq(p) for k, p in LOCAL.items()}
    signal: dict[str, str] = {}
    for k, p in LOCAL.items():
        m = re.search(r"^FT   SIGNAL\s+(\d+)\.\.(\d+)", p.read_text(), re.M)
        signal[k] = f"{m.group(1)}-{m.group(2)}" if m else "none annotated"
    for k, acc in REMOTE.items():
        d = fetch_json(acc)
        seqs[k] = d["sequence"]["value"]
        sp = [f for f in d.get("features", []) if f["type"] == "Signal"]
        signal[k] = (
            f"{sp[0]['location']['start']['value']}-{sp[0]['location']['end']['value']}"
            if sp
            else "none annotated"
        )

    names = list(seqs)
    print("## Sequences\n")
    print("| protein | length | signal peptide (UniProt) | cysteines |")
    print("|---|---|---|---|")
    for n in names:
        print(f"| {n} | {len(seqs[n])} | {signal[n]} | {seqs[n].count('C')} |")

    ref = seqs[REF]
    cores = {n: region(ref, seqs[n], *CORE) for n in names}
    ref_core = ref[CORE[0] - 1 : CORE[1]]

    print("\n## Full-length global identity (%) to human, gar and zebrafish proteins\n")
    targets = ["human VWC2 (Q2TAL6)", "human VWC2L (B2RUY7)", "gar vwc2 (W5MCB8)",
               "gar vwc2l (W5MAF2)", "zf vwc2 (B0I1T8)", "zf si:dkey-283b1.7 (E7F8B1)"]
    print("| query | " + " | ".join(targets) + " |")
    print("|---|" + "---|" * len(targets))
    for n in names:
        row = []
        for t in targets:
            row.append("-" if n == t else f"{identity(seqs[n], seqs[t])[0]:.1f}")
        print(f"| {n} | " + " | ".join(row) + " |")

    print(f"\n## Core identity (%): residues aligned to human VWC2 {CORE[0]}-{CORE[1]} "
          "(VWFC 1 + VWFC 2)\n")
    print("| query | core length | " + " | ".join(targets) + " |")
    print("|---|---|" + "---|" * len(targets))
    for n in names:
        row = []
        for t in targets:
            row.append("-" if n == t else f"{identity(cores[n], cores[t])[0]:.1f}")
        print(f"| {n} | {len(cores[n])} | " + " | ".join(row) + " |")

    print("\n## Core cysteines of human VWC2 kept in each protein\n")
    aln_positions = [i for i, c in enumerate(ref_core) if c == "C"]
    print(f"Human VWC2 core has {len(aln_positions)} cysteines.\n")
    print("| protein | core cysteines aligned to human core cysteines |")
    print("|---|---|")
    for n in names:
        aln = aligner().align(ref, seqs[n])[0]
        kept = 0
        for i, j in columns(aln):
            if i is not None and CORE[0] - 1 <= i <= CORE[1] - 1 and ref[i] == "C":
                if j is not None and seqs[n][j] == "C":
                    kept += 1
        print(f"| {n} | {kept}/{len(aln_positions)} |")

    print("\n## N-terminal region (after the signal peptide, before the core)\n")
    print("Residues aligned to human VWC2 28-152, and identity of that stretch to human VWC2.\n")
    print("| protein | aligned residues | identity to human VWC2 28-152 (%) |")
    print("|---|---|---|")
    ref_n = ref[27:152]
    for n in names:
        nt = region(ref, seqs[n], 28, 152)
        pid = identity(nt, ref_n)[0] if nt else 0.0
        print(f"| {n} | {len(nt)} | {pid:.1f} |")

    print("\n## Human VWC2 motif 114-116 ('Mediates cell adhesion', UniProt)\n")
    motif_ref = ref[113:116]
    print(f"Human VWC2 114-116: {motif_ref}\n")
    for n in names:
        print(f"- {n}: {region(ref, seqs[n], 114, 116) or '(no aligned residues)'}")


if __name__ == "__main__":
    main()
