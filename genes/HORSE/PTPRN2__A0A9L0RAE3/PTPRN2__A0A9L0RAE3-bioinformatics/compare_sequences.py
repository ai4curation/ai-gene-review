"""Compare horse PTPRN2 (A0A9L0RAE3) with experimentally characterised SF5 orthologs.

Reads the horse and human UniProt flat files from the repository, fetches mouse
Ptprn2 (P80560) and rat phogrin (Q63475) from the UniProt REST API, globally aligns
each ortholog with the horse sequence, and reports percent identity, PANTHER
subfamily assignments, and the horse residues at human Q92932 functional positions
(catalytic-site, substrate-binding, processing, sorting and transmembrane features).

Run from the repository root:
    uv run python genes/HORSE/PTPRN2__A0A9L0RAE3/PTPRN2__A0A9L0RAE3-bioinformatics/compare_sequences.py
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
REPO = HERE.parents[3]
HORSE = REPO / "genes/HORSE/PTPRN2__A0A9L0RAE3/PTPRN2__A0A9L0RAE3-uniprot.txt"
HUMAN = REPO / "genes/human/PTPRN2/PTPRN2-uniprot.txt"
FETCHED = {"mouse": "P80560", "rat": "Q63475"}

# Human Q92932 positions/ranges taken from its UniProt FT lines (see human flat file).
HUMAN_REGIONS = {
    "dibasic cleavage site (SITE 427..428)": (427, 428),
    "transmembrane helix (TRANSMEM 616..636)": (616, 636),
    "tyrosine-based internalization motif (MOTIF 666..675)": (666, 675),
    "WPD-loop substrate-binding residue (BINDING 913) +/-3": (910, 916),
    "P-loop / PTP signature incl. catalytic Cys945 (BINDING 945..951)": (943, 953),
    "Q-loop substrate-binding residue (BINDING 990) +/-2": (988, 992),
    "leucine-based sorting signal (MOTIF 1004..1010)": (1004, 1010),
    "C-terminus": (1006, 1015),
}

HUMAN_SEGMENTS = {
    "luminal precursor region (22-615)": (22, 615),
    "mature IA-2beta60 chain start to TM (502-615)": (502, 615),
    "cytoplasmic region (637-1015)": (637, 1015),
    "PTP-like domain (745-1005)": (745, 1005),
}


def seq_of(text: str) -> str:
    return "".join(
        re.sub(r"[^A-Z]", "", line)
        for line in text.split("SQ   SEQUENCE", 1)[1].splitlines()[1:]
        if not line.startswith("//")
    )


def field(text: str, prefix: str) -> list[str]:
    return [line for line in text.splitlines() if line.startswith(prefix)]


def fetch_flat(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.txt") as r:
        return r.read().decode()


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def stats_and_map(aln, a: str, b: str) -> tuple[dict, dict[int, int]]:
    """Identity stats and map from 1-based positions of b to a."""
    ident = aligned = 0
    m: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            aligned += 1
            ident += int(a[a0 + k] == b[b0 + k])
            m[int(b0) + k + 1] = int(a0) + k + 1
    return {
        "length": len(b),
        "aligned_columns": aligned,
        "identical": ident,
        "identity_pct": round(100 * ident / aligned, 1),
        "identity_over_shorter_pct": round(100 * ident / min(len(a), len(b)), 1),
    }, m


def main() -> None:
    horse_txt = HORSE.read_text()
    horse = seq_of(horse_txt)
    texts = {"human": HUMAN.read_text()}
    texts.update({k: fetch_flat(v) for k, v in FETCHED.items()})
    out: dict = {
        "horse": {
            "accession": "A0A9L0RAE3",
            "length": len(horse),
            "panther": field(horse_txt, "DR   PANTHER"),
        },
        "orthologs": {},
    }
    al = aligner()
    human_map: dict[int, int] = {}
    for name, txt in texts.items():
        s = seq_of(txt)
        aln = al.align(horse, s)[0]
        st, m = stats_and_map(aln, horse, s)
        st["id_line"] = field(txt, "ID   ")[0]
        st["panther"] = field(txt, "DR   PANTHER")
        out["orthologs"][name] = st
        if name == "human":
            human_map = m
            human = s
    regions = {}
    for label, (start, end) in HUMAN_REGIONS.items():
        hum = human[start - 1 : end]
        hpos = [human_map.get(p) for p in range(start, end + 1)]
        hor = "".join(horse[p - 1] if p else "-" for p in hpos)
        mapped = [p for p in hpos if p]
        regions[label] = {
            "human_range": f"{start}-{end}",
            "human": hum,
            "horse_range": f"{mapped[0]}-{mapped[-1]}" if mapped else None,
            "horse": hor,
            "identical": hum == hor,
        }
    out["human_feature_regions_in_horse"] = regions
    segs = {}
    for label, (start, end) in HUMAN_SEGMENTS.items():
        pairs = [(p, human_map.get(p)) for p in range(start, end + 1)]
        ident = sum(1 for p, q in pairs if q and human[p - 1] == horse[q - 1])
        segs[label] = {
            "human_range": f"{start}-{end}",
            "human_residues": end - start + 1,
            "aligned_to_horse": sum(1 for _, q in pairs if q),
            "identical": ident,
            "identity_pct": round(100 * ident / (end - start + 1), 1),
        }
    out["segment_identity_human_vs_horse"] = segs
    out["horse_catalytic_cys_position"] = human_map.get(945)
    out["horse_residue_at_human_945"] = horse[human_map[945] - 1] if 945 in human_map else None
    (HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
