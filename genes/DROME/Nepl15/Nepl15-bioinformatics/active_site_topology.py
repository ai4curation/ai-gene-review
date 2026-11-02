"""Nepl15 (Q9VCU1) catalytic-site and topology check.

Fetches sequences from UniProt REST, aligns them with MAFFT L-INS-i, and reports
the Nepl15 residue aligned to each functional position of human neprilysin (MME,
P08473) annotated in UniProt (Zn ligands H584, H588, E647; catalytic E585;
proton donor D651; peptide-binding R103). Also reports a Kyte-Doolittle
hydrophobicity scan of Nepl15 to look for a transmembrane anchor, pairwise
identity of Nepl15 to each sequence, and whether the two UniProt entries for
the gene (Q9VCU1, Q95U74) have identical sequences.
Outputs: input.fasta, aln.fasta, results.json (also printed).
"""
import json
import subprocess
import urllib.request
from pathlib import Path

from Bio import AlignIO

HERE = Path(__file__).parent
ACCS = {
    "Q9VCU1": "Nepl15",
    "Q9VCU2": "Nepl14_SF240",
    "Q9VCU3": "Nepl13_SF240",
    "Q9VAS1": "Nepl19_SF238",
    "Q8T062": "Nep4_SF238",
    "A0A0B4K692": "Nep2_SF224",
    "P08473": "human_MME",
}
# human MME (P08473) positions from UniProt features
MME_SITES = {
    103: "peptide binding (R103)",
    584: "Zn2+ ligand (HExxH first His)",
    585: "catalytic Glu (active site)",
    588: "Zn2+ ligand (HExxH second His)",
    647: "Zn2+ ligand (ENIAD Glu)",
    651: "active site proton donor (Asp; UniProt Active site 651)",
}
KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
      "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
      "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(l.strip() for l in lines if not l.startswith(">"))


def col_of(row: str, pos: int) -> int:
    n = 0
    for i, c in enumerate(row):
        if c != "-":
            n += 1
            if n == pos:
                return i
    raise ValueError(pos)


def pos_at(row: str, col: int) -> int | None:
    if row[col] == "-":
        return None
    return sum(1 for c in row[: col + 1] if c != "-")


def main() -> None:
    seqs = {f"{n}_{a}": fetch(a) for a, n in ACCS.items()}
    alt = fetch("Q95U74")
    fa = HERE / "input.fasta"
    fa.write_text("".join(f">{k}\n{v}\n" for k, v in seqs.items()))
    out = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fa)],
        capture_output=True, text=True, check=True,
    )
    (HERE / "aln.fasta").write_text(out.stdout)
    rows = {r.id: str(r.seq) for r in AlignIO.read(HERE / "aln.fasta", "fasta")}
    tkey, rkey = "Nepl15_Q9VCU1", "human_MME_P08473"
    t, ref = rows[tkey], rows[rkey]

    sites = {}
    for p, desc in MME_SITES.items():
        c = col_of(ref, p)
        sites[f"MME_{ref[c]}{p}"] = {
            "role": desc,
            "aligned": {k: (s[c] + str(pos_at(s, c)) if s[c] != "-" else "-")
                        for k, s in rows.items()},
        }
    c584 = col_of(ref, 584)
    motif = {k: s[c584:c584 + 12].replace("-", "")[:5] for k, s in rows.items()}

    ident = {}
    for k, s in rows.items():
        if k == tkey:
            continue
        pairs = [(a, b) for a, b in zip(t, s) if a != "-" and b != "-"]
        ident[k] = round(100 * sum(a == b for a, b in pairs) / len(pairs), 1)

    seq = seqs[tkey]
    w = 19
    hyd = [(i + 1, round(sum(KD[a] for a in seq[i:i + w]) / w, 2))
           for i in range(len(seq) - w + 1)]
    tm_windows = [(s, v) for s, v in hyd if v >= 1.6]
    res = {
        "Q9VCU1_length": len(seq),
        "Q95U74_identical_to_Q9VCU1": alt == seq,
        "N_terminal_40": seq[:40],
        "C_terminal_20": seq[-20:],
        "kd_windows_ge_1.6_start_positions": [s for s, _ in tm_windows],
        "max_kd_window_after_residue_40": max(v for s, v in hyd if s > 40),
        "hexxh_window_aligned_to_MME_584": motif,
        "functional_sites": sites,
        "percent_identity_of_Nepl15_to": ident,
    }
    print(json.dumps(res, indent=2))
    (HERE / "results.json").write_text(json.dumps(res, indent=2) + "\n")


if __name__ == "__main__":
    main()
