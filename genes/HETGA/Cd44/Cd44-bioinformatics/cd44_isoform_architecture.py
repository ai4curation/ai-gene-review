"""Compare the naked mole-rat CD44 reference protein (A0AAX6R0R7, 701 aa,
RefSeq model XP_012930388.1) with human CD44 (P16070) to ask a single question:

    Is the HETGA reference protein architecturally a *standard* CD44 (CD44s,
    no variant exons) or a *variant-exon-containing* CD44v form?

Method
------
Human P16070-1 (742 aa, canonical) is the full variant-exon-containing form.
UniProt annotates the human "Stem" region as 224-649 and records that human
isoform 11 (CD44R2) is "Missing 223..535" -- i.e. residues 223-535 of the human
canonical sequence are the alternatively spliced variant-exon insert.

If the naked mole-rat protein were a standard CD44s form it would have no
homologous counterpart to human 223-535.  We therefore:

  1. globally align HETGA A0AAX6R0R7 to human P16070-1 (Needleman-Wunsch,
     BLOSUM62, affine gaps);
  2. map human residues 223-535 through the alignment and report how many of
     them align to a real HETGA residue (rather than to a gap).

Nothing is hardcoded; if the alignment is poor the script says so.

Run:  uv run --with biopython python cd44_isoform_architecture.py
"""

from __future__ import annotations

import json
import pathlib
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

HERE = pathlib.Path(__file__).parent
ACCESSIONS = {"human_P16070": "P16070", "hetga_A0AAX6R0R7": "A0AAX6R0R7"}

# UniProt-annotated landmarks (read from the two UniProt flat files, not guessed)
HUMAN_LINK = (32, 120)
HUMAN_TM = (650, 670)
HUMAN_VARIANT_INSERT = (223, 535)  # VSP_022797 "Missing (in isoform 11)"
HETGA_LINK = (34, 122)
HETGA_TM = (609, 630)

# UniProt P16070 feature-table positions (1-based, human numbering)
HUMAN_HA_BINDING = [41, 78, 79, 105]          # FT BINDING /ligand="hyaluronan"
HUMAN_LINK_CYS = [28, 53, 77, 97, 118, 129]   # FT DISULFID 28..129, 53..118, 77..97


def fetch(acc: str) -> str:
    cache = HERE / f"{acc}.fasta"
    if not cache.exists():
        url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
        cache.write_text(urllib.request.urlopen(url, timeout=60).read().decode())
    lines = cache.read_text().splitlines()
    return "".join(l.strip() for l in lines if not l.startswith(">"))


def main() -> None:
    seqs = {name: fetch(acc) for name, acc in ACCESSIONS.items()}
    human, hetga = seqs["human_P16070"], seqs["hetga_A0AAX6R0R7"]

    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aln = aligner.align(human, hetga)[0]

    # aln.aligned gives paired blocks of ungapped (human, hetga) coordinates
    human_blocks, hetga_blocks = aln.aligned
    aligned_human_positions = set()
    identities = 0
    for (h0, h1), (n0, n1) in zip(human_blocks, hetga_blocks):
        for off in range(h1 - h0):
            aligned_human_positions.add(h0 + off)          # 0-based
            if human[h0 + off] == hetga[n0 + off]:
                identities += 1

    ident_at = {}
    for (h0, h1), (n0, n1) in zip(human_blocks, hetga_blocks):
        for off in range(h1 - h0):
            ident_at[h0 + off] = human[h0 + off] == hetga[n0 + off]

    def covered(lo: int, hi: int) -> tuple[int, int]:
        """lo/hi are 1-based inclusive human coordinates."""
        span = range(lo - 1, hi)
        return sum(1 for p in span if p in aligned_human_positions), len(span)

    def pid(lo: int, hi: int) -> float:
        """Percent identity over the aligned columns of a 1-based human span."""
        span = [p for p in range(lo - 1, hi) if p in aligned_human_positions]
        if not span:
            return float("nan")
        return round(100 * sum(ident_at[p] for p in span) / len(span), 1)

    link_cov, link_n = covered(*HUMAN_LINK)
    insert_cov, insert_n = covered(*HUMAN_VARIANT_INSERT)
    tm_cov, tm_n = covered(*HUMAN_TM)

    # Map individual human residues of interest onto the HETGA sequence
    human_to_hetga = {}
    for (h0, h1), (n0, n1) in zip(human_blocks, hetga_blocks):
        for off in range(h1 - h0):
            human_to_hetga[h0 + off] = n0 + off

    def residue_map(positions: list[int]) -> dict[str, str]:
        out = {}
        for hp in positions:
            hidx = hp - 1
            if hidx not in human_to_hetga:
                out[f"human_{human[hidx]}{hp}"] = "gap (no aligned HETGA residue)"
            else:
                nidx = human_to_hetga[hidx]
                out[f"human_{human[hidx]}{hp}"] = f"HETGA {hetga[nidx]}{nidx + 1}"
        return out

    result = {
        "human_length": len(human),
        "hetga_length": len(hetga),
        "alignment_score": aln.score,
        "aligned_columns": len(aligned_human_positions),
        "identities": identities,
        "percent_identity_over_aligned": round(
            100 * identities / max(1, len(aligned_human_positions)), 1
        ),
        "human_link_domain_32_120_aligned": f"{link_cov}/{link_n}",
        "human_TM_650_670_aligned": f"{tm_cov}/{tm_n}",
        "human_variant_insert_223_535_aligned": f"{insert_cov}/{insert_n}",
        "human_variant_insert_fraction_aligned": round(insert_cov / insert_n, 3),
        "percent_identity_link_domain_32_120": pid(*HUMAN_LINK),
        "percent_identity_variant_insert_223_535": pid(*HUMAN_VARIANT_INSERT),
        "percent_identity_cytoplasmic_tail_671_742": pid(671, len(human)),
        "hyaluronan_binding_residues": residue_map(HUMAN_HA_BINDING),
        "link_domain_disulfide_cysteines": residue_map(HUMAN_LINK_CYS),
        "hetga_ectodomain_len_after_signal": HETGA_TM[0] - 21,
        "human_ectodomain_len_after_signal": HUMAN_TM[0] - 21,
    }
    print(json.dumps(result, indent=2))
    (HERE / "cd44_isoform_architecture.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
