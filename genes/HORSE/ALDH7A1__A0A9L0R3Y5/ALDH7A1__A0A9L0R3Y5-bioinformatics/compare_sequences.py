"""Compare horse ALDH7A1 (A0A9L0R3Y5) with the PAINT-seed orthologs of node PTN000192435.

Reads the horse and human UniProt flat files from the repository, fetches mouse
Aldh7a1 (Q9DBF1) from the UniProt REST API, globally aligns each ortholog with the
horse sequence, and reports percent identity, the horse residues at the human
catalytic and NAD-binding positions (from the human UniProt FT lines), and the
N-terminal region preceding the first aligned human residue.

Run from the repository root:
    uv run python genes/HORSE/ALDH7A1__A0A9L0R3Y5/ALDH7A1__A0A9L0R3Y5-bioinformatics/compare_sequences.py
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
REPO = HERE.parents[3]
HORSE = REPO / "genes/HORSE/ALDH7A1__A0A9L0R3Y5/ALDH7A1__A0A9L0R3Y5-uniprot.txt"
HUMAN = REPO / "genes/human/ALDH7A1/ALDH7A1-uniprot.txt"
HORSE_BENCH = REPO / "genes/HORSE/ALDH7A1/ALDH7A1-uniprot.txt"


def parse_flat(text: str) -> tuple[str, list[tuple[str, int, str]]]:
    """Return (sequence, [(feature_type, position, note)]) for single-position FT lines."""
    seq = "".join(
        re.sub(r"[^A-Z]", "", line)
        for line in text.split("SQ   SEQUENCE", 1)[1].splitlines()[1:]
        if not line.startswith("//")
    )
    feats = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (ACT_SITE|BINDING|SITE)\s+(\d+)$", line)
        if m:
            note = ""
            for nxt in lines[i + 1 : i + 4]:
                if "/ligand=" in nxt or "/note=" in nxt:
                    note = nxt.split("=", 1)[1].strip('"')
                    break
            feats.append((m.group(1), int(m.group(2)), note))
    return seq, feats


def fetch_flat(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def mapping(aln) -> dict[int, int]:
    """Map 1-based positions of sequence B (target index 1) to sequence A (index 0)."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            m[int(b0) + k + 1] = int(a0) + k + 1
    return m


def identity(aln, a: str, b: str) -> dict:
    ident = aligned = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            aligned += 1
            ident += int(a[a0 + k] == b[b0 + k])
    return {"aligned_columns": aligned, "identical": ident,
            "pct_identity_over_aligned": round(100 * ident / aligned, 1)}


def main() -> None:
    horse_seq, _ = parse_flat(HORSE.read_text())
    human_seq, human_feats = parse_flat(HUMAN.read_text())
    others = {"human_P49419": human_seq,
              "mouse_Q9DBF1": parse_flat(fetch_flat("Q9DBF1"))[0]}
    if HORSE_BENCH.exists():
        others["horse_A0A9L0RRL6"] = parse_flat(HORSE_BENCH.read_text())[0]
    al = aligner()
    result = {"horse_A0A9L0R3Y5_length": len(horse_seq), "comparisons": {}}
    for name, seq in others.items():
        aln = al.align(horse_seq, seq)[0]
        info = identity(aln, horse_seq, seq)
        info["length"] = len(seq)
        m = mapping(aln)
        info["horse_position_of_ortholog_residue_1"] = m.get(1)
        result["comparisons"][name] = info
        if name == "human_P49419":
            sites = []
            seen = set()
            for ftype, pos, note in human_feats:
                if (ftype, pos) in seen:
                    continue
                seen.add((ftype, pos))
                hp = m.get(pos)
                sites.append({"feature": ftype, "human_pos": pos, "note": note,
                              "human_res": human_seq[pos - 1],
                              "horse_pos": hp,
                              "horse_res": horse_seq[hp - 1] if hp else None})
            result["human_site_mapping"] = sites
            result["all_sites_conserved"] = all(s["human_res"] == s["horse_res"] for s in sites)
            if m.get(1):
                result["horse_n_terminal_extension"] = horse_seq[: m[1] - 1]
    out = HERE / "results.json"
    out.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
