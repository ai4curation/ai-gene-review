#!/usr/bin/env python3
"""Check the NADP(+)-specificity determinants of C. albicans Gnd1 (A0A1D8PFS4).

6-Phosphogluconate dehydrogenase (6PGDH) exists as NADP+-specific, NAD+-specific
and dual-specificity forms. Hanau & Helliwell (2022, PMID:35234135) summarise the
sequence determinants of coenzyme preference, established from the sheep 6PGDH
crystal structures and by mutagenesis in Lactococcus lactis and Gluconobacter
oxydans 6PGDH:

* the dinucleotide-binding fingerprint in the beta-a/alpha-a turn, which is
  Gly-X-Ala-X-Met-Gly in sheep 6PGDH (sheep residues 9-14);
* an Asn-Arg-Thr motif in the beta-b/alpha-b turn (sheep Asn32-Arg33-Thr34) whose
  Asn and Arg hydrogen-bond the 2'-phosphate of NADP+ and define NADP+
  specificity. NAD+-preferring 6PGDHs carry Asp in place of the Asn (an
  Asp-Arg-Asp motif in the NAD+-preferring Gluconacetobacter diazotrophicus
  enzyme), and the Asp side chain hinders placement of the 2'-phosphate.

This script reads the protein sequence from the local UniProt record, locates the
two motifs by regular expression (no fixed offsets are assumed), reports which
variant the C. albicans enzyme carries, and cross-checks the positions against
the UniProt NADP(+) BINDING features. It is deliberately conservative: a motif
that is not found is reported as INCONCLUSIVE, never guessed.

Usage:  python check_coenzyme_motifs.py [path/to/GND1-uniprot.txt]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_UNIPROT = HERE.parent / "GND1-uniprot.txt"

# Motif definitions (from PMID:35234135). Patterns are anchored to the N-terminal
# coenzyme-binding (Rossmann-like) domain, i.e. the first 60 residues.
FINGERPRINT = re.compile(r"G.A.MG")          # Gly-X-Ala-X-Met-Gly (sheep 9-14)
NAD_FINGERPRINT = re.compile(r"G.G..G")       # classical NAD+-binding fingerprint
NADP_MOTIF = re.compile(r"NR[TS]")            # Asn-Arg-Thr (sheep 32-34); Ser tolerated
NAD_MOTIF = re.compile(r"DRD")                # Asp-Arg-Asp (NAD+-preferring 6PGDH)
NTERM = 60


def read_uniprot(path: Path) -> tuple[str, list[tuple[int, int]]]:
    """Return (sequence, [(start, end), ...] of NADP(+) BINDING features)."""
    seq_lines: list[str] = []
    in_seq = False
    binding: list[tuple[int, int]] = []
    pending: tuple[int, int] | None = None
    for line in path.read_text().splitlines():
        if line.startswith("SQ"):
            in_seq = True
            continue
        if line.startswith("//"):
            in_seq = False
            continue
        if in_seq:
            seq_lines.append(line.replace(" ", ""))
            continue
        if line.startswith("FT   BINDING"):
            span = line.split()[2]
            a, _, b = span.partition("..")
            pending = (int(a), int(b) if b else int(a))
        elif line.startswith("FT ") and pending and '/ligand="NADP(+)"' in line:
            binding.append(pending)
            pending = None
    return "".join(seq_lines), binding


def find(pattern: re.Pattern[str], seq: str, limit: int) -> dict | None:
    m = pattern.search(seq[:limit])
    if not m:
        return None
    return {"match": m.group(0), "start": m.start() + 1, "end": m.end()}  # 1-based


def overlaps(hit: dict | None, features: list[tuple[int, int]]) -> list[str]:
    if not hit:
        return []
    return [f"{a}..{b}" for a, b in features if not (hit["end"] < a or hit["start"] > b)]


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DEFAULT_UNIPROT
    seq, nadp_features = read_uniprot(path)
    if not seq:
        print(f"ERROR: no sequence found in {path}", file=sys.stderr)
        return 1

    fp = find(FINGERPRINT, seq, NTERM)
    fp_nad = find(NAD_FINGERPRINT, seq, NTERM)
    nadp = find(NADP_MOTIF, seq, NTERM)
    nad = find(NAD_MOTIF, seq, NTERM)

    if nadp and not nad:
        verdict = "NADP+-specific determinants present (Asn-Arg-Thr); NAD+-type Asp-Arg-Asp absent"
    elif nad and not nadp:
        verdict = "NAD+-type Asp-Arg-Asp motif present; NADP+ Asn-Arg-Thr absent"
    elif nadp and nad:
        verdict = "AMBIGUOUS: both motif types found in N-terminal domain"
    else:
        verdict = "INCONCLUSIVE: neither coenzyme-specificity motif found in the first 60 residues"

    result = {
        "accession": "A0A1D8PFS4",
        "sequence_length": len(seq),
        "n_terminal_window": NTERM,
        "fingerprint_GxAxMG": fp,
        "fingerprint_GxGxxG_classical_NAD": fp_nad,
        "nadp_motif_NR[TS]": nadp,
        "nad_motif_DRD": nad,
        "uniprot_NADP_binding_features": [f"{a}..{b}" for a, b in nadp_features],
        "fingerprint_overlaps_uniprot_NADP_feature": overlaps(fp, nadp_features),
        "nadp_motif_overlaps_uniprot_NADP_feature": overlaps(nadp, nadp_features),
        "verdict": verdict,
        "source": "Motif definitions from Hanau & Helliwell 2022, PMID:35234135",
    }
    out = HERE / "results.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
