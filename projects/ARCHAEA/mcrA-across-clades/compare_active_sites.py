"""Compare MCR/ACR alpha-subunit active-site residues across archaeal clades.

Each sequence is read from the UniProt flat file cached in the gene folder
(``genes/<code>/<folder>/<folder>-uniprot.txt``). Reference positions are read
from the BINDING and MOD_RES features of the Methanothermobacter marburgensis
MCR I alpha subunit (P11558, MCRA_METTM), the best characterised MCR. Every
other sequence is aligned globally to P11558 (BLOSUM62, gap open -10, extend
-0.5) and the residue aligned to each reference position is reported, together
with that protein's own UniProt feature at the same position, if any.

No result is hard-coded: re-run with ``python compare_active_sites.py`` from the
repository root (or pass the root as the first argument) to regenerate
``RESULTS.tsv``. Pairwise alignment to a single reference is adequate for the
conserved core of this family (identities 50-90 %); it is not a phylogeny.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3]
REFERENCE = ("METTM", "mcrA")

# Reference positions without a UniProt feature that the structural literature
# singles out. These are inputs (positions to inspect), not results.
EXTRA_POSITIONS = {
    332: "LITERATURE:Gln next to the coenzyme M-coordinating Tyr333; Met in ANME-2d MCR (PMID:40913044)",
}

# (species code, folder, clade label, physiology of the source organism)
ENTRIES = [
    ("METTM", "mcrA", "Methanobacteriales", "hydrogenotrophic methanogen"),
    ("METTH", "mcrA", "Methanobacteriales", "hydrogenotrophic methanogen"),
    ("METJA", "mcrA", "Methanococcales", "hydrogenotrophic methanogen"),
    ("METKA", "mcrA", "Methanopyrales", "hydrogenotrophic methanogen"),
    ("METBF", "mcrA", "Methanosarcinales", "methylotrophic/acetoclastic/hydrogenotrophic methanogen"),
    ("METAC", "mcrA", "Methanosarcinales", "methylotrophic/acetoclastic methanogen"),
    ("9EURY", "mcrA__A0A284VQI9", "ANME-2d (Ca. Methanoperedentaceae)", "anaerobic methanotroph"),
    ("9EURY", "mcrA__A0A7R9R780", "GoM-Arc1 (Ca. Methanoperedentaceae)", "anaerobic ethane oxidizer"),
]


def read_uniprot(path: Path) -> tuple[str, str, dict[int, list[str]]]:
    """Return accession, sequence and {position: [feature descriptions]}."""
    text = path.read_text()
    acc = re.search(r"^AC   (\w+);", text, re.M).group(1)
    seq_block = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//")[0]
    seq = re.sub(r"[^A-Z]", "", seq_block)
    feats: dict[int, list[str]] = {}
    current = None
    for line in text.splitlines():
        m = re.match(r"^FT   (BINDING|MOD_RES)\s+(\d+)(?:\.\.(\d+))?\s*$", line)
        if m:
            kind, start, end = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
            current = {"kind": kind, "positions": range(start, end + 1), "desc": ""}
            for p in current["positions"]:
                feats.setdefault(p, []).append(current)
            continue
        if line.startswith("FT   ") and not line.startswith("FT                   "):
            current = None
            continue
        if current is not None:
            m2 = re.match(r'^FT\s+/(ligand|note|ligand_part)="([^"]*)', line)
            if m2 and not current["desc"]:
                current["desc"] = m2.group(2)
            elif m2 and m2.group(1) == "ligand_part":
                current["desc"] += f" ({m2.group(2)})"
    out = {p: sorted({f"{f['kind']}:{f['desc']}" for f in fs}) for p, fs in feats.items()}
    return acc, seq, out


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def map_positions(ref: str, tgt: str) -> tuple[dict[int, int | None], float]:
    """Map 1-based reference positions to 1-based target positions."""
    aln = aligner().align(ref, tgt)[0]
    mapping: dict[int, int | None] = {i: None for i in range(1, len(ref) + 1)}
    ident = aligned = 0
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for k in range(re_ - rs):
            mapping[rs + k + 1] = ts + k + 1
            aligned += 1
            ident += ref[rs + k] == tgt[ts + k]
    return mapping, 100.0 * ident / aligned


def main() -> None:
    def path(code: str, folder: str) -> Path:
        return ROOT / "genes" / code / folder / f"{folder}-uniprot.txt"

    ref_acc, ref_seq, ref_feats = read_uniprot(path(*REFERENCE))
    for pos, label in EXTRA_POSITIONS.items():
        ref_feats.setdefault(pos, []).append(label)
    ref_positions = sorted(ref_feats)
    rows = []
    for code, folder, clade, physiology in ENTRIES:
        acc, seq, feats = read_uniprot(path(code, folder))
        mapping, pid = map_positions(ref_seq, seq) if acc != ref_acc else ({i: i for i in range(1, len(seq) + 1)}, 100.0)
        for rp in ref_positions:
            tp = mapping.get(rp)
            rows.append({
                "accession": acc, "species_code": code, "clade": clade, "physiology": physiology,
                "length": len(seq), "identity_to_P11558_pct": f"{pid:.1f}",
                "ref_position": rp, "ref_residue": ref_seq[rp - 1],
                "ref_features": "; ".join(ref_feats[rp]),
                "target_position": tp or "", "target_residue": seq[tp - 1] if tp else "-",
                "conserved": "yes" if tp and seq[tp - 1] == ref_seq[rp - 1] else "no",
                "target_uniprot_features": "; ".join(feats.get(tp, [])) if tp else "",
            })
    out = Path(__file__).with_name("RESULTS.tsv")
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    # compact console summary: one line per entry
    by_acc: dict[str, list[dict]] = {}
    for r in rows:
        by_acc.setdefault(r["accession"], []).append(r)
    print(f"reference {ref_acc}: {len(ref_positions)} positions ({len(EXTRA_POSITIONS)} from literature)")
    for acc, rs in by_acc.items():
        changed = [f"{r['ref_residue']}{r['ref_position']}->{r['target_residue']}{r['target_position']}" for r in rs if r["conserved"] == "no"]
        print(f"{acc}\t{rs[0]['clade']}\tid={rs[0]['identity_to_P11558_pct']}%\tchanged: {', '.join(changed) or 'none'}")


if __name__ == "__main__":
    main()
