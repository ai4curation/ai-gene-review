#!/usr/bin/env python3
"""Map curated aldo-keto reductase (AKR) catalytic and cofactor sites onto
Gluconobacter oxydans 621H GOX1598 (UniProtKB Q5FQK7).

Q5FQK7 is an unreviewed (TrEMBL) entry with no GO annotations and no
characterisation. Its only functional signal is signature-based: Pfam PF00248
(Aldo_ket_red), SUPFAM SSF51430, CDD cd19094 (AKR_Tas-like), Gene3D 3.20.20.100
and PANTHER PTHR43364:SF4.

Whether that fold assignment implies a working enzyme depends on whether the AKR
catalytic tetrad is present. This script answers that without any hard-coded
residue numbers: it downloads the UniProt flat files for a set of *reviewed* AKRs
that carry curated ACT_SITE / SITE / BINDING features, aligns each pairwise to
Q5FQK7, and reports which Q5FQK7 residue each curated feature position maps onto.

Everything printed is derived at run time. Nothing is asserted that the
alignment does not show; unalignable positions are reported as gaps.

Usage (from this directory):
    uv run python map_akr_catalytic_sites.py
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"

TARGET = "Q5FQK7"

# Reviewed AKRs with curated active-site / cofactor features.
# The first four are PANTHER PTHR43364:SF4, the same subfamily as Q5FQK7;
# P15121 (human aldose reductase, AKR1A/1B clan) is the structural archetype of
# the superfamily and is included as an out-of-subfamily control.
REFERENCES = {
    "P0A9T4": "E. coli Tas (PTHR43364:SF4)",
    "P77256": "E. coli YdjG, NADH-specific methylglyoxal reductase (PTHR43364:SF4)",
    "P46336": "B. subtilis IolS aldo-keto reductase (PTHR43364:SF4)",
    "O43488": "Human AKR7A2, aflatoxin B1 aldehyde reductase (PTHR43364:SF4)",
    "P15121": "Human AKR1B1 aldose reductase (superfamily archetype)",
}

FEATURE_KINDS = ("ACT_SITE", "SITE", "BINDING")


@dataclass
class Feature:
    kind: str
    start: int
    end: int
    note: str = ""
    ligand: str = ""

    @property
    def positions(self) -> list[int]:
        return list(range(self.start, self.end + 1))


@dataclass
class Entry:
    accession: str
    entry_name: str = ""
    sequence: str = ""
    features: list[Feature] = field(default_factory=list)


def fetch_flat_file(accession: str) -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{accession}.txt"
    if not path.exists():
        url = f"https://rest.uniprot.org/uniprotkb/{accession}.txt"
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        path.write_text(response.text)
    return path.read_text()


RANGE_RE = re.compile(r"^(\??<?)(\d+)(?:\.\.(\??>?)(\d+))?$")


def parse_flat_file(accession: str, text: str) -> Entry:
    entry = Entry(accession=accession)
    seq_lines: list[str] = []
    in_sequence = False
    current: Feature | None = None

    for line in text.splitlines():
        if line.startswith("ID   "):
            entry.entry_name = line.split()[1]
        elif line.startswith("SQ   "):
            in_sequence = True
        elif line.startswith("//"):
            in_sequence = False
        elif in_sequence and line.startswith("     "):
            seq_lines.append(line.replace(" ", ""))
        elif line.startswith("FT   ") and line[5] != " ":
            kind = line[5:13].strip()
            location = line[21:].strip()
            current = None
            if kind in FEATURE_KINDS:
                match = RANGE_RE.match(location)
                if match:
                    start = int(match.group(2))
                    end = int(match.group(4)) if match.group(4) else start
                    current = Feature(kind=kind, start=start, end=end)
                    entry.features.append(current)
        elif line.startswith("FT                   ") and current is not None:
            qualifier = line[21:].strip()
            if qualifier.startswith('/note="'):
                current.note = qualifier[7:].rstrip('"')
            elif qualifier.startswith('/ligand="'):
                current.ligand = qualifier[9:].rstrip('"')

    entry.sequence = "".join(seq_lines)
    return entry


def make_aligner() -> Align.PairwiseAligner:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    return aligner


def position_map(alignment) -> dict[int, int | None]:
    """Map 1-based reference (target of `alignment.aligned[1]`) -> 1-based query.

    `alignment` is built with the reference as the first sequence and Q5FQK7 as
    the second, so `aligned[0]` indexes the reference and `aligned[1]` Q5FQK7.
    """
    mapping: dict[int, int | None] = {}
    for (ref_start, ref_end), (qry_start, qry_end) in zip(*alignment.aligned):
        for offset in range(int(ref_end) - int(ref_start)):
            mapping[int(ref_start) + offset + 1] = int(qry_start) + offset + 1
    return mapping


def percent_identity(alignment) -> float:
    ref, qry = alignment[0], alignment[1]
    matches = sum(1 for a, b in zip(ref, qry) if a == b and a != "-")
    aligned_columns = sum(1 for a, b in zip(ref, qry) if a != "-" and b != "-")
    return 100.0 * matches / aligned_columns if aligned_columns else 0.0


def main() -> int:
    target_entry = parse_flat_file(TARGET, fetch_flat_file(TARGET))
    if not target_entry.sequence:
        print(f"ERROR: no sequence parsed for {TARGET}", file=sys.stderr)
        return 1

    aligner = make_aligner()
    results: dict[str, object] = {
        "target": {
            "accession": TARGET,
            "entry_name": target_entry.entry_name,
            "length": len(target_entry.sequence),
            "curated_features": [f.kind for f in target_entry.features],
        },
        "references": [],
    }

    print(f"Target: {TARGET} ({target_entry.entry_name}), "
          f"{len(target_entry.sequence)} aa")
    print(f"Curated ACT_SITE/SITE/BINDING features on the target: "
          f"{len(target_entry.features)}")
    print()

    alignment_dump: list[str] = []

    for accession, label in REFERENCES.items():
        reference = parse_flat_file(accession, fetch_flat_file(accession))
        alignment = aligner.align(reference.sequence, target_entry.sequence)[0]
        mapping = position_map(alignment)
        identity = percent_identity(alignment)

        print(f"=== {accession} {reference.entry_name} - {label}")
        print(f"    length {len(reference.sequence)} aa; "
              f"pairwise identity to {TARGET}: {identity:.1f}%")

        ref_result: dict[str, object] = {
            "accession": accession,
            "entry_name": reference.entry_name,
            "label": label,
            "length": len(reference.sequence),
            "percent_identity": round(identity, 1),
            "features": [],
        }

        for feature in reference.features:
            # Only report point features and short motifs; long cofactor
            # stretches are summarised by their endpoints.
            mapped = [(p, mapping.get(p)) for p in feature.positions]
            pieces = []
            for ref_pos, qry_pos in mapped:
                ref_aa = reference.sequence[ref_pos - 1]
                if qry_pos is None:
                    pieces.append(f"{ref_aa}{ref_pos}->gap")
                else:
                    qry_aa = target_entry.sequence[qry_pos - 1]
                    same = "=" if qry_aa == ref_aa else "!"
                    pieces.append(f"{ref_aa}{ref_pos}->{qry_aa}{qry_pos}{same}")
            descriptor = feature.note or feature.ligand or ""
            print(f"      {feature.kind:9s} {descriptor[:46]:46s} "
                  f"{' '.join(pieces)}")
            ref_result["features"].append(
                {
                    "kind": feature.kind,
                    "note": feature.note,
                    "ligand": feature.ligand,
                    "mapping": [
                        {
                            "reference_position": ref_pos,
                            "reference_residue": reference.sequence[ref_pos - 1],
                            "target_position": qry_pos,
                            "target_residue": (
                                target_entry.sequence[qry_pos - 1]
                                if qry_pos is not None
                                else None
                            ),
                            "identical": (
                                qry_pos is not None
                                and target_entry.sequence[qry_pos - 1]
                                == reference.sequence[ref_pos - 1]
                            ),
                        }
                        for ref_pos, qry_pos in mapped
                    ],
                }
            )

        print()
        results["references"].append(ref_result)
        alignment_dump.append(
            f">>> {accession} {reference.entry_name} vs {TARGET} "
            f"({identity:.1f}% identity)\n{alignment}\n"
        )

    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (HERE / "alignments.txt").write_text("\n".join(alignment_dump))
    print("Wrote results.json and alignments.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
