"""Does the APOO/MIC26 N-terminus look like a secretory signal peptide or a
mitochondrial presequence?

UniProt annotates Q9BUR5 (MIC26) residues 1-25 as SIGNAL (ECO:0000255, i.e.
sequence-analysis prediction only), and the record still carries `Secreted`,
`Golgi apparatus membrane` and `Endoplasmic reticulum membrane` subcellular
locations.  The paralogue Q6UXV4 (MIC27), the same family and the same
compartment, is instead annotated with a TRANSIT peptide.  This script asks
whether MIC26's N-terminal segment carries the sequence features of a secretory
signal peptide or of a mitochondrial matrix-targeting presequence, by scoring it
against two control panels of human proteins whose N-terminal segments UniProt
annotates as SIGNAL and as TRANSIT respectively.

Everything is fetched live from the UniProt REST API; nothing is hardcoded
except the two published hydrophobicity scales and the accession panels.

The discriminating features are the textbook ones:
  * mitochondrial presequences are strongly basic, essentially devoid of acidic
    residues, and form amphipathic helices (high hydrophobic moment);
  * secretory signal peptides have a short basic n-region followed by a long
    uncharged hydrophobic h-region (high mean hydrophobicity, low net charge).

Run:  uv run python targeting_sequence_analysis.py
"""

from __future__ import annotations

import json
import math
import re
import sys
from dataclasses import dataclass, field

import requests

UNIPROT_TXT = "https://rest.uniprot.org/uniprotkb/{acc}.txt"

# Target and its paralogue.
TARGETS = {
    "Q9BUR5": "APOO / MIC26 (target)",
    "Q6UXV4": "APOOL / MIC27 (paralogue, same family PTHR14564)",
}

# Human proteins whose N-terminus UniProt annotates as a mitochondrial TRANSIT
# peptide.  Chosen as well-characterised matrix / inner-membrane proteins.
MITO_PANEL = {
    "P10809": "HSPD1 (mt-HSP60)",
    "P04179": "SOD2",
    "P36542": "ATP5F1C",
    "P31930": "UQCRC1",
    "P21912": "SDHB",
    "O75439": "PMPCB",
    "P31040": "SDHA",
    "P30049": "ATP5F1D",
    "Q16891": "IMMT / MIC60",
    "P38646": "HSPA9",
}

# Human proteins whose N-terminus UniProt annotates as a secretory SIGNAL
# peptide.  Deliberately weighted towards plasma apolipoproteins, because the
# historical claim under test is that MIC26 is a secreted apolipoprotein.
SECRETED_PANEL = {
    "P02647": "APOA1",
    "P02649": "APOE",
    "P06727": "APOA4",
    "P02749": "APOH",
    "P04114": "APOB",
    "P01019": "AGT",
    "P02768": "ALB",
    "P01009": "SERPINA1",
    "P02652": "APOA2",
    "P05090": "APOD",
}

# Eisenberg consensus hydrophobicity scale (Eisenberg et al. 1984), used for the
# hydrophobic moment; and Kyte-Doolittle (1982) for the h-region hydropathy.
EISENBERG = {
    "A": 0.62, "R": -2.53, "N": -0.78, "D": -0.90, "C": 0.29,
    "Q": -0.85, "E": -0.74, "G": 0.48, "H": -0.40, "I": 1.38,
    "L": 1.06, "K": -1.50, "M": 0.64, "F": 1.19, "P": 0.12,
    "S": -0.18, "T": -0.05, "W": 0.81, "Y": 0.26, "V": 1.08,
}
KYTE_DOOLITTLE = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5,
    "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5,
    "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6,
    "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}

HELIX_ANGLE_DEG = 100.0  # alpha-helix residue rotation
MOMENT_WINDOW = 11
HREGION_WINDOW = 7


@dataclass
class Entry:
    accession: str
    entry_name: str
    sequence: str
    features: dict[str, tuple[int, int]] = field(default_factory=dict)
    transmem: list[tuple[int, int]] = field(default_factory=list)

    @property
    def length(self) -> int:
        return len(self.sequence)


def fetch(acc: str) -> Entry:
    resp = requests.get(UNIPROT_TXT.format(acc=acc), timeout=60)
    resp.raise_for_status()
    text = resp.text
    entry_name = text.splitlines()[0].split()[1]

    seq_lines = text.split("\nSQ   ", 1)[1].splitlines()[1:]
    sequence = "".join(l.replace(" ", "") for l in seq_lines if not l.startswith("//"))

    declared = int(re.search(r"^ID .*?\s(\d+) AA\.", text, re.M).group(1))
    if len(sequence) != declared:
        raise ValueError(
            f"{acc}: parsed {len(sequence)} residues but the ID line declares {declared}"
        )

    features: dict[str, tuple[int, int]] = {}
    transmem: list[tuple[int, int]] = []
    for key, start, end in re.findall(
        r"^FT   (SIGNAL|TRANSIT|CHAIN|TRANSMEM)\s+(\d+)\.\.(\d+)", text, re.M
    ):
        span = (int(start), int(end))
        if key == "TRANSMEM":
            transmem.append(span)
        else:
            features.setdefault(key, span)
    return Entry(acc, entry_name, sequence, features, transmem)


def targeting_segment(entry: Entry) -> tuple[str, str]:
    """Return (feature_key, segment) for the annotated N-terminal targeting peptide."""
    for key in ("SIGNAL", "TRANSIT"):
        if key in entry.features:
            start, end = entry.features[key]
            return key, entry.sequence[start - 1 : end]
    raise ValueError(f"{entry.accession}: no SIGNAL or TRANSIT feature annotated")


def hydrophobic_moment(seq: str, window: int = MOMENT_WINDOW) -> float:
    """Maximum Eisenberg hydrophobic moment per residue over a sliding window."""
    if len(seq) < window:
        window = len(seq)
    best = 0.0
    delta = math.radians(HELIX_ANGLE_DEG)
    for i in range(len(seq) - window + 1):
        sub = seq[i : i + window]
        sin_sum = sum(EISENBERG.get(a, 0.0) * math.sin(delta * j) for j, a in enumerate(sub))
        cos_sum = sum(EISENBERG.get(a, 0.0) * math.cos(delta * j) for j, a in enumerate(sub))
        best = max(best, math.hypot(sin_sum, cos_sum) / window)
    return best


def max_hregion_hydropathy(seq: str, window: int = HREGION_WINDOW) -> float:
    """Mean Kyte-Doolittle hydropathy of the most hydrophobic window (the h-region)."""
    if len(seq) < window:
        window = len(seq)
    return max(
        sum(KYTE_DOOLITTLE.get(a, 0.0) for a in seq[i : i + window]) / window
        for i in range(len(seq) - window + 1)
    )


def score(seq: str) -> dict[str, float]:
    n = len(seq)
    pos = sum(seq.count(a) for a in "KR")
    neg = sum(seq.count(a) for a in "DE")
    return {
        "len": n,
        "net_charge": pos - neg,
        "n_acidic": neg,
        "n_arg": seq.count("R"),
        "arg_per_10": 10.0 * seq.count("R") / n,
        "frac_acidic": neg / n,
        "max_moment": hydrophobic_moment(seq),
        "max_hregion_kd": max_hregion_hydropathy(seq),
        "arg_at_minus2": 1.0 if n >= 2 and seq[-2] == "R" else 0.0,
        "arg_at_minus3": 1.0 if n >= 3 and seq[-3] == "R" else 0.0,
    }


def summarise(rows: list[dict[str, float]], key: str) -> tuple[float, float, float, float]:
    vals = sorted(r[key] for r in rows)
    mean = sum(vals) / len(vals)
    var = sum((v - mean) ** 2 for v in vals) / (len(vals) - 1)
    return mean, math.sqrt(var), vals[0], vals[-1]


def align_paralogues(a: Entry, b: Entry):
    """Global alignment of MIC26 vs MIC27 mature chains; map b's features onto a."""
    from Bio import Align

    aligner = Align.PairwiseAligner()
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.substitution_matrix = __import__(
        "Bio.Align.substitution_matrices", fromlist=["substitution_matrices"]
    ).load("BLOSUM62")
    aln = aligner.align(a.sequence, b.sequence)[0]
    # Build b-position -> a-position map from the aligned blocks.
    mapping: dict[int, int] = {}
    for (a_start, a_end), (b_start, b_end) in zip(*aln.aligned):
        for off in range(a_end - a_start):
            mapping[b_start + off + 1] = a_start + off + 1
    return aln, mapping


def main() -> int:
    print("# APOO/MIC26 N-terminal targeting-sequence analysis\n")
    print("All sequences and features fetched live from UniProt REST.\n")

    entries: dict[str, Entry] = {}
    for acc in list(TARGETS) + list(MITO_PANEL) + list(SECRETED_PANEL):
        entries[acc] = fetch(acc)

    print("## Panel composition\n")
    print("| accession | entry | label | group | length | N-terminal feature | span |")
    print("|---|---|---|---|---|---|---|")
    labelled: list[tuple[str, str, str]] = (
        [(a, l, "target") for a, l in TARGETS.items()]
        + [(a, l, "mitochondrial TRANSIT panel") for a, l in MITO_PANEL.items()]
        + [(a, l, "secretory SIGNAL panel") for a, l in SECRETED_PANEL.items()]
    )
    for acc, label, group in labelled:
        e = entries[acc]
        key, _ = targeting_segment(e)
        span = e.features[key]
        print(
            f"| {acc} | {e.entry_name} | {label} | {group} | {e.length} | {key} "
            f"| {span[0]}..{span[1]} |"
        )

    # Assert the panels are annotated the way the design assumes.
    bad_mito = [a for a in MITO_PANEL if targeting_segment(entries[a])[0] != "TRANSIT"]
    bad_sec = [a for a in SECRETED_PANEL if targeting_segment(entries[a])[0] != "SIGNAL"]
    if bad_mito or bad_sec:
        print(
            f"\n**Panel warning**: TRANSIT panel members not annotated TRANSIT: {bad_mito}; "
            f"SIGNAL panel members not annotated SIGNAL: {bad_sec}. "
            "These were still scored; treat the comparison accordingly.\n"
        )

    metrics = [
        ("net_charge", "net charge (K+R-D-E)"),
        ("n_acidic", "acidic residues (D+E)"),
        ("arg_per_10", "Arg per 10 residues"),
        ("max_moment", "max Eisenberg hydrophobic moment (11-res window)"),
        ("max_hregion_kd", "max Kyte-Doolittle h-region (7-res window)"),
    ]

    mito_rows = [score(targeting_segment(entries[a])[1]) for a in MITO_PANEL]
    sec_rows = [score(targeting_segment(entries[a])[1]) for a in SECRETED_PANEL]

    print("\n## Per-protein scores\n")
    print(
        "| accession | label | group | seg len | net charge | D+E | Arg/10 "
        "| max moment | max h-region KD | R at -2 | R at -3 |"
    )
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for acc, label, group in labelled:
        key, seg = targeting_segment(entries[acc])
        s = score(seg)
        print(
            f"| {acc} | {label} | {group} | {int(s['len'])} | {s['net_charge']:+.0f} "
            f"| {int(s['n_acidic'])} | {s['arg_per_10']:.1f} | {s['max_moment']:.3f} "
            f"| {s['max_hregion_kd']:+.2f} | {'yes' if s['arg_at_minus2'] else 'no'} "
            f"| {'yes' if s['arg_at_minus3'] else 'no'} |"
        )

    print("\n## Panel distributions and where the target falls\n")
    print(
        "| metric | mito TRANSIT mean+/-SD [min,max] | secretory SIGNAL mean+/-SD [min,max] "
        "| APOO/MIC26 | APOOL/MIC27 | closer to |"
    )
    print("|---|---|---|---|---|---|")
    verdicts: dict[str, str] = {}
    for key, label in metrics:
        mm, ms, mlo, mhi = summarise(mito_rows, key)
        sm, ss, slo, shi = summarise(sec_rows, key)
        tgt = score(targeting_segment(entries["Q9BUR5"])[1])[key]
        par = score(targeting_segment(entries["Q6UXV4"])[1])[key]
        # z-distance to each panel mean, using that panel's own SD
        dz_m = abs(tgt - mm) / ms if ms else float("inf")
        dz_s = abs(tgt - sm) / ss if ss else float("inf")
        closer = "mitochondrial" if dz_m < dz_s else "secretory"
        verdicts[key] = closer
        print(
            f"| {label} | {mm:.2f}+/-{ms:.2f} [{mlo:.2f},{mhi:.2f}] "
            f"| {sm:.2f}+/-{ss:.2f} [{slo:.2f},{shi:.2f}] | {tgt:.2f} | {par:.2f} "
            f"| {closer} (|z|={dz_m:.1f} vs {dz_s:.1f}) |"
        )

    n_mito = sum(1 for v in verdicts.values() if v == "mitochondrial")
    print(
        f"\n**Tally**: on {n_mito} of {len(verdicts)} discriminating metrics the "
        f"MIC26 1-25 segment sits closer to the mitochondrial-presequence panel "
        f"than to the secretory-signal-peptide panel.\n"
    )

    # Paralogue architecture comparison.
    print("## MIC26 vs MIC27 architecture\n")
    mic26, mic27 = entries["Q9BUR5"], entries["Q6UXV4"]
    aln, m27_to_m26 = align_paralogues(mic26, mic27)
    a_idx, b_idx = aln.aligned
    matches = 0
    aligned_cols = 0
    for (a_start, a_end), (b_start, b_end) in zip(a_idx, b_idx):
        for off in range(a_end - a_start):
            aligned_cols += 1
            if mic26.sequence[a_start + off] == mic27.sequence[b_start + off]:
                matches += 1
    print(
        f"Global BLOSUM62 alignment of {mic26.accession} ({mic26.length} aa) and "
        f"{mic27.accession} ({mic27.length} aa): {matches}/{aligned_cols} identities in "
        f"aligned columns ({100.0 * matches / aligned_cols:.1f}%).\n"
    )
    print("| MIC27 feature | MIC27 span | aligned MIC26 span | MIC26 residues | max KD (7-res) |")
    print("|---|---|---|---|---|")
    m27_feats = [("TRANSIT", mic27.features.get("TRANSIT"))] + [
        (f"TRANSMEM {i + 1}", span) for i, span in enumerate(mic27.transmem)
    ]
    for name, span in m27_feats:
        if not span:
            continue
        mapped = [m27_to_m26[p] for p in range(span[0], span[1] + 1) if p in m27_to_m26]
        if not mapped:
            print(f"| {name} | {span[0]}..{span[1]} | (no aligned residues) | - | - |")
            continue
        lo, hi = min(mapped), max(mapped)
        seg = mic26.sequence[lo - 1 : hi]
        print(
            f"| {name} | {span[0]}..{span[1]} | {lo}..{hi} | `{seg}` "
            f"| {max_hregion_hydropathy(seg):+.2f} |"
        )
    print(
        f"\nMIC26's own annotated TRANSMEM spans: "
        f"{', '.join(f'{a}..{b}' for a, b in mic26.transmem) or 'none'}.\n"
    )

    json.dump(
        {
            "target": {
                acc: {
                    "entry_name": entries[acc].entry_name,
                    "length": entries[acc].length,
                    "feature": targeting_segment(entries[acc])[0],
                    "segment": targeting_segment(entries[acc])[1],
                    "scores": score(targeting_segment(entries[acc])[1]),
                }
                for acc in TARGETS
            },
            "panel_verdicts": verdicts,
            "paralogue_identity_pct": 100.0 * matches / aligned_cols,
        },
        open("results.json", "w"),
        indent=2,
    )
    print("Raw numbers also written to `results.json`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
