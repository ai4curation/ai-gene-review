#!/usr/bin/env python3
"""Sequence-level checks on human apolipoprotein F (APOF, Q13790).

Every number printed is computed from sequences fetched live from the UniProt
REST API at run time. Nothing is hardcoded except the accessions, the UniProt
feature boundaries being tested, and the literature values the computation is
compared against (each tagged with its PMID).

Claims tested
-------------
1. Mature-chain boundary. UniProt annotates SIGNAL 1-35, PROPEP 36-164,
   CHAIN 165-326 on a 326-residue precursor. Day et al. 1994 (PMID:8093033)
   report that the cDNA "encodes apolipoprotein F, which is composed of 162
   amino acids"; Lagor et al. 2009 (PMID:19008531) report a "326 amino acid
   precursor ... cleaved to release the 162 amino acid C-terminus". Check that
   the annotated CHAIN is exactly 162 residues of a 326-residue precursor.

2. Mass gap attributed to glycosylation. Liu & Morton 2020 (PMID:32520778)
   state the apparent mass of mature ApoF is "~30kDa, not the expected
   17.4kDa". Compute the unmodified mass of CHAIN 165-326.

3. Charge polarity of the two halves of the precursor. Liu & Morton 2020 state
   that "At physiologic pH, the N-terminal peptide is strongly positively
   charged, whereas the C-terminal portion (ApoF) is negatively charged".
   Olofsson et al. 1978 (PMID:204339) named ApoF an "acidic apolipoprotein";
   Nishide et al. 1989 (PMID:2715721) measured an isoelectric point of 4.6 and
   Lagor et al. 2009 an isoelectric point of 4.5. Compute pI and net charge at
   pH 7.4 for the propeptide and for the mature chain separately.

4. Glycosylation sites. Locate N-X-S/T sequons (X != P) in the propeptide and
   in the mature chain, and locate the tryptic peptide DANISQPETTK that
   Kumar et al. 2017 (PMID:28935895) had to discard from their assay "since it
   was glycosylated".

5. Amphipathic helix content. Lagor et al. 2012 (PMID:22363685) state ApoF is
   "predicted to lack strong amphipathic alpha helices which are essential for
   the lipid binding properties of other HDL-associated apolipoproteins such as
   apo A-I, apo A-II, apo E and the apo Cs". Compute the Eisenberg hydrophobic
   moment over 18-residue windows for mature ApoF and for the mature chains of
   APOA1, APOE and APOC3 as positive controls.

6. Sequence relatedness to the classical apolipoproteins. Lagor et al. 2012
   state ApoF "bears no structural or sequence similarity to the other
   classical apolipoproteins". Run local (Smith-Waterman) alignments of mature
   human ApoF against APOA1/APOA2/APOE/APOC3, with mouse and rat ApoF as
   positive controls for the same alignment settings.
"""

from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass

from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.SeqUtils.ProtParam import ProteinAnalysis

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}?format=json"

# Accessions under test / used as controls.
APOF_HUMAN = "Q13790"
APOF_MOUSE = "Q91V80"
APOF_RAT = "Q5M889"
CONTROLS = {
    "APOA1_HUMAN": "P02647",
    "APOA2_HUMAN": "P02652",
    "APOE_HUMAN": "P02649",
    "APOC3_HUMAN": "P02656",
}

# UniProt feature boundaries for Q13790 that this script is testing (1-based,
# inclusive). Asserted against the live record rather than trusted.
APOF_SIGNAL = (1, 35)
APOF_PROPEP = (36, 164)
APOF_CHAIN = (165, 326)

# Literature values the computations are compared against.
LIT_MATURE_LENGTH = 162  # PMID:8093033, PMID:19008531
LIT_PRECURSOR_LENGTH = 326  # PMID:19008531 and UniProt Q13790
LIT_EXPECTED_KDA = 17.4  # PMID:32520778
LIT_APPARENT_KDA = (29.0, 33.0)  # PMID:2715721 (29 kDa), PMID:9880564 (~33 kDa)
LIT_PI = (4.5, 4.6)  # PMID:19008531 (4.5), PMID:2715721 (4.6)
LIT_GLYCOPEPTIDE = "DANISQPETTK"  # PMID:28935895

# Eisenberg consensus hydrophobicity scale (Eisenberg et al. 1984), used for the
# hydrophobic-moment calculation. This is a published constant, not a result.
EISENBERG = {
    "A": 0.62, "R": -2.53, "N": -0.78, "D": -0.90, "C": 0.29,
    "Q": -0.85, "E": -0.74, "G": 0.48, "H": -0.40, "I": 1.38,
    "L": 1.06, "K": -1.50, "M": 0.64, "F": 1.19, "P": 0.12,
    "S": -0.18, "T": -0.05, "W": 0.81, "Y": 0.26, "V": 1.08,
}
HELIX_TURN_DEG = 100.0


@dataclass
class Entry:
    accession: str
    name: str
    length: int
    sequence: str
    features: list[dict]

    def chain_bounds(self) -> tuple[int, int]:
        """First CHAIN feature, 1-based inclusive."""
        for f in self.features:
            if f["type"] == "Chain":
                loc = f["location"]
                return loc["start"]["value"], loc["end"]["value"]
        raise KeyError(f"{self.accession} has no CHAIN feature")

    def segment(self, start: int, end: int) -> str:
        return self.sequence[start - 1 : end]


def fetch(acc: str) -> Entry:
    with urllib.request.urlopen(UNIPROT.format(acc=acc)) as fh:
        rec = json.load(fh)
    seq = rec["sequence"]["value"]
    name = rec["proteinDescription"]["recommendedName"]["fullName"]["value"]
    entry = Entry(
        accession=rec["primaryAccession"],
        name=name,
        length=rec["sequence"]["length"],
        sequence=seq,
        features=rec.get("features", []),
    )
    assert len(entry.sequence) == entry.length, (
        f"{acc}: declared length {entry.length} != sequence length {len(entry.sequence)}"
    )
    return entry


def net_charge(seq: str, ph: float) -> float:
    return ProteinAnalysis(seq).charge_at_pH(ph)


def sequons(seq: str, offset: int) -> list[tuple[int, str]]:
    """N-X-S/T sequons (X != P), reported in precursor numbering."""
    out = []
    for i in range(len(seq) - 2):
        if seq[i] == "N" and seq[i + 1] != "P" and seq[i + 2] in "ST":
            out.append((offset + i, seq[i : i + 3]))
    return out


def hydrophobic_moments(seq: str, window: int = 18) -> list[tuple[float, int, str]]:
    """Eisenberg mean hydrophobic moment <uH> for every sliding window."""
    import math

    out = []
    for i in range(0, max(1, len(seq) - window + 1)):
        win = seq[i : i + window]
        if len(win) < window or any(r not in EISENBERG for r in win):
            continue
        sx = sum(EISENBERG[r] * math.cos(math.radians(HELIX_TURN_DEG * j)) for j, r in enumerate(win))
        sy = sum(EISENBERG[r] * math.sin(math.radians(HELIX_TURN_DEG * j)) for j, r in enumerate(win))
        out.append((math.hypot(sx, sy) / window, i + 1, win))
    return out


def local_identity(a: str, b: str) -> tuple[float, float, int]:
    """Smith-Waterman score, percent identity over the aligned block, and its length."""
    aligner = PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aln = aligner.align(a, b)[0]
    top, bottom = aln[0], aln[1]
    matches = sum(1 for x, y in zip(top, bottom) if x == y and x != "-")
    span = len(top)
    return aln.score, 100.0 * matches / span, span


def main() -> None:
    human = fetch(APOF_HUMAN)
    print("=" * 78)
    print(f"1. PRECURSOR AND MATURE CHAIN  ({human.accession} {human.name})")
    print("=" * 78)
    print(f"precursor length (live UniProt)            : {human.length}")
    print(f"literature precursor length (PMID:19008531): {LIT_PRECURSOR_LENGTH}")
    chain_start, chain_end = human.chain_bounds()
    assert (chain_start, chain_end) == APOF_CHAIN, (
        f"UniProt CHAIN moved: expected {APOF_CHAIN}, record says {(chain_start, chain_end)}"
    )
    mature = human.segment(*APOF_CHAIN)
    propep = human.segment(*APOF_PROPEP)
    signal = human.segment(*APOF_SIGNAL)
    print(f"SIGNAL {APOF_SIGNAL[0]}-{APOF_SIGNAL[1]} length              : {len(signal)}")
    print(f"PROPEP {APOF_PROPEP[0]}-{APOF_PROPEP[1]} length            : {len(propep)}")
    print(f"CHAIN  {APOF_CHAIN[0]}-{APOF_CHAIN[1]} length            : {len(mature)}")
    print(f"literature mature length (PMID:8093033)    : {LIT_MATURE_LENGTH}")
    print(f"CHAIN length == literature 162 aa          : {len(mature) == LIT_MATURE_LENGTH}")
    print(f"precursor == signal+propep+chain           : "
          f"{len(signal) + len(propep) + len(mature) == human.length}")

    print()
    print("=" * 78)
    print("2. MASS OF THE UNMODIFIED MATURE CHAIN vs APPARENT MASS")
    print("=" * 78)
    mw_mature = ProteinAnalysis(mature).molecular_weight() / 1000.0
    mw_precursor = ProteinAnalysis(human.sequence).molecular_weight() / 1000.0
    print(f"computed mass, CHAIN 165-326, unmodified   : {mw_mature:.2f} kDa")
    print(f"computed mass, full precursor              : {mw_precursor:.2f} kDa")
    print(f"'expected 17.4kDa' (PMID:32520778)         : {LIT_EXPECTED_KDA} kDa")
    print(f"computed within 0.5 kDa of 17.4            : {abs(mw_mature - LIT_EXPECTED_KDA) < 0.5}")
    lo, hi = LIT_APPARENT_KDA
    print(f"apparent mass on SDS-PAGE                  : {lo}-{hi} kDa "
          f"(PMID:2715721, PMID:9880564)")
    print(f"unexplained mass, apparent - computed      : {lo - mw_mature:.1f} to "
          f"{hi - mw_mature:.1f} kDa ({100 * (lo / mw_mature - 1):.0f}-"
          f"{100 * (hi / mw_mature - 1):.0f}% above the polypeptide mass)")

    print()
    print("=" * 78)
    print("3. CHARGE POLARITY OF THE TWO HALVES OF THE PRECURSOR")
    print("=" * 78)
    for label, seq, span in (
        ("signal 1-35", signal, APOF_SIGNAL),
        ("propeptide 36-164", propep, APOF_PROPEP),
        ("mature chain 165-326", mature, APOF_CHAIN),
    ):
        pa = ProteinAnalysis(seq)
        neg = seq.count("D") + seq.count("E")
        pos = seq.count("K") + seq.count("R")
        print(f"{label:22s} len={len(seq):3d}  pI={pa.isoelectric_point():5.2f}  "
              f"charge@pH7.4={net_charge(seq, 7.4):+6.2f}  D+E={neg:3d}  K+R={pos:3d}")
    print(f"measured pI of mature ApoF                 : {LIT_PI[0]}-{LIT_PI[1]} "
          f"(PMID:19008531, PMID:2715721)")
    print("NOTE: the measured values are for the sialylated glycoprotein and the computed")
    print("      value is for the bare polypeptide, so they are not the same quantity;")
    print("      the comparison is reported as-is without adjusting either.")

    print()
    print("=" * 78)
    print("4. GLYCOSYLATION SITES")
    print("=" * 78)
    print(f"N-X-S/T sequons in propeptide 36-164 : {sequons(propep, APOF_PROPEP[0])}")
    print(f"N-X-S/T sequons in mature 165-326    : {sequons(mature, APOF_CHAIN[0])}")
    uniprot_carb = [
        (f["location"]["start"]["value"], f.get("description", ""))
        for f in human.features
        if f["type"] == "Glycosylation"
    ]
    print(f"UniProt CARBOHYD features            : {uniprot_carb}")
    idx = human.sequence.find(LIT_GLYCOPEPTIDE)
    assert idx >= 0, f"{LIT_GLYCOPEPTIDE} not found in {human.accession}"
    pep_start, pep_end = idx + 1, idx + len(LIT_GLYCOPEPTIDE)
    print(f"glycosylated tryptic peptide {LIT_GLYCOPEPTIDE} (PMID:28935895)")
    print(f"  precursor coordinates              : {pep_start}-{pep_end}")
    print(f"  lies inside mature chain 165-326   : {pep_start >= APOF_CHAIN[0]}")
    in_pep = [(p, d) for p, d in uniprot_carb if pep_start <= p <= pep_end]
    print(f"  UniProt CARBOHYD sites inside it   : {in_pep}")
    print(f"  sequons inside it                  : {sequons(LIT_GLYCOPEPTIDE, pep_start)}")

    print()
    print("=" * 78)
    print("5. AMPHIPATHIC HELIX POTENTIAL (Eisenberg <uH>, 18-residue windows)")
    print("=" * 78)
    rows = [("APOF_HUMAN mature 165-326", mature)]
    for name, acc in CONTROLS.items():
        ctl = fetch(acc)
        cs, ce = ctl.chain_bounds()
        rows.append((f"{name} mature {cs}-{ce}", ctl.segment(cs, ce)))
    threshold = 0.40
    print(f"'strong' window threshold <uH> >= {threshold}; extent is the fraction of")
    print("18-residue windows clearing it, which is the quantity the literature claim")
    print("is about (how much of the chain is amphipathic), not the single best window.")
    print()
    for label, seq in rows:
        mus = hydrophobic_moments(seq)
        mu, pos, win = max(mus)
        strong = sum(1 for m, _, _ in mus if m >= threshold)
        mean = sum(m for m, _, _ in mus) / len(mus)
        print(f"{label:34s} len={len(seq):3d}  max <uH>={mu:.3f} at {pos:3d}  "
              f"mean <uH>={mean:.3f}  strong windows={strong:3d}/{len(mus):3d} "
              f"({100 * strong / len(mus):4.1f}%)  best={win}")
    print()
    print("Controls APOA1/APOA2/APOE/APOC3 are the classical amphipathic-helix")
    print("apolipoproteins; a comparable or higher amphipathic extent in ApoF would")
    print("contradict PMID:22363685, a clearly lower one is consistent with it.")

    print()
    print("=" * 78)
    print("6. SEQUENCE RELATEDNESS (Smith-Waterman, BLOSUM62, gap -11/-1)")
    print("=" * 78)
    orthologs = {"APOF_MOUSE": APOF_MOUSE, "APOF_RAT": APOF_RAT}
    print("positive controls (ApoF orthologues, full precursors):")
    for name, acc in orthologs.items():
        other = fetch(acc)
        score, ident, span = local_identity(human.sequence, other.sequence)
        print(f"  APOF_HUMAN vs {name:11s} len={other.length:3d}  score={score:7.1f}  "
              f"identity={ident:5.1f}% over {span} aligned columns")
    print("classical apolipoproteins (mature chains vs mature ApoF):")
    for name, acc in CONTROLS.items():
        ctl = fetch(acc)
        cs, ce = ctl.chain_bounds()
        score, ident, span = local_identity(mature, ctl.segment(cs, ce))
        print(f"  APOF mature vs {name:11s} len={ce - cs + 1:3d}  score={score:7.1f}  "
              f"identity={ident:5.1f}% over {span} aligned columns")


if __name__ == "__main__":
    main()
