#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.85", "requests", "pyyaml"]
# ///
"""N-terminal extension of Dictyostelium scsB (Q869S7) against beta subunits with a known mature start.

Question: UniProt records no transit peptide for Q869S7 and says none is predicted.
Does the protein nevertheless have residues ahead of the conserved mature start of the
succinyl-CoA synthetase beta subunit, and what are they like?

Method: each reference beta subunit is aligned to Q869S7 (global alignment, BLOSUM62,
gap open -10, gap extend -0.5, end gaps free). The first residue of the reference's
mature chain (the residue after its UniProt transit peptide, or residue 1 for the
bacterial subunit, which has none) is mapped onto Q869S7. The script also maps residue
20 of the mature E. coli and pig subunits (the residue that contacts the nucleotide base).

Nothing is hard-coded except accessions. Sequences and features are fetched from UniProt.
The script reports what the alignment gives; it does not predict cleavage.
"""
from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

import requests
import yaml
from Bio.Align import PairwiseAligner, substitution_matrices

QUERY = "Q869S7"
# reference beta subunits; the mature start is read from the UniProt record at run time
REFERENCES = ["Q96I99", "P53590", "Q9Z2I8", "Q9P2R7", "Q55AI5", "P53312", "P0A836"]
UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"


def fetch(acc: str) -> dict:
    r = requests.get(UNIPROT.format(acc=acc), timeout=60)
    r.raise_for_status()
    d = r.json()
    transit = None
    for f in d.get("features", []):
        if f["type"] == "Transit peptide":
            evid = sorted({e.get("evidenceCode", "") for e in f.get("evidences", [])})
            transit = {
                "start": f["location"]["start"].get("value"),
                "start_modifier": f["location"]["start"].get("modifier"),
                "end": f["location"]["end"].get("value"),
                "end_modifier": f["location"]["end"].get("modifier"),
                "evidence_codes": evid,
            }
    gene = (d.get("genes") or [{}])[0].get("geneName", {}).get("value", "")
    return {
        "accession": acc,
        "entry_name": d["uniProtkbId"],
        "organism": d["organism"]["scientificName"],
        "gene": gene,
        "entry_version": d["entryAudit"]["entryVersion"],
        "sequence_version": d["entryAudit"]["sequenceVersion"],
        "length": d["sequence"]["length"],
        "sequence": d["sequence"]["value"],
        "transit": transit,
    }


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def column_map(aln) -> dict[int, int]:
    """0-based reference index -> 0-based query index, for aligned (ungapped) columns."""
    m = {}
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for k in range(te - ts):
            m[int(ts) + k] = int(qs) + k
    return m


def composition(seq: str) -> dict:
    return {
        "length": len(seq),
        "basic_KR": sum(seq.count(c) for c in "KR"),
        "acidic_DE": sum(seq.count(c) for c in "DE"),
        "hydroxylated_ST": sum(seq.count(c) for c in "ST"),
        "hydrophobic_AILMFVWY": sum(seq.count(c) for c in "AILMFVWY"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).parent / "results.yaml"))
    args = ap.parse_args()

    q = fetch(QUERY)
    al = aligner()
    rows = []
    for acc in REFERENCES:
        ref = fetch(acc)
        aln = al.align(ref["sequence"], q["sequence"])[0]
        cmap = column_map(aln)
        t = ref["transit"]
        mature0 = t["end"] if t else 0  # 0-based index of first mature residue
        row = {
            "reference": acc,
            "entry_name": ref["entry_name"],
            "gene": ref["gene"],
            "organism": ref["organism"],
            "entry_version": ref["entry_version"],
            "transit_peptide": (
                None if t is None else
                f"{'<' if t['start_modifier'] == 'OUTSIDE' else ''}{t['start']}..{t['end']}"
            ),
            "transit_evidence_codes": None if t is None else t["evidence_codes"],
            "reference_mature_start": mature0 + 1,
            "reference_mature_first10": ref["sequence"][mature0:mature0 + 10],
        }
        identical = sum(1 for i, j in cmap.items() if ref["sequence"][i] == q["sequence"][j])
        row["aligned_columns"] = len(cmap)
        row["percent_identity_over_aligned_columns"] = round(100 * identical / len(cmap), 1)
        if mature0 in cmap:
            qi = cmap[mature0]
            row["query_residue_aligned_to_mature_start"] = qi + 1
            row["query_first10_from_that_residue"] = q["sequence"][qi:qi + 10]
            row["query_residues_ahead_of_mature_start"] = qi
        else:
            row["query_residue_aligned_to_mature_start"] = None
        p20 = mature0 + 19
        if p20 in cmap:
            qi = cmap[p20]
            row["reference_mature_residue_20"] = ref["sequence"][p20]
            row["query_residue_aligned_to_mature_20"] = f"{q['sequence'][qi]}{qi + 1}"
        rows.append(row)

    starts = sorted({r["query_residue_aligned_to_mature_start"] for r in rows
                     if r["query_residue_aligned_to_mature_start"]})
    ext = {}
    for s in starts:
        seg = q["sequence"][: s - 1]
        ext[int(s)] = {"extension": seg, **composition(seg)}

    out = {
        "generated": datetime.date.today().isoformat(),
        "query": {k: q[k] for k in ("accession", "entry_name", "gene", "organism", "entry_version",
                                    "sequence_version", "length")},
        "query_transit_peptide_in_uniprot": q["transit"],
        "query_first40": q["sequence"][:40],
        "alignment": "global, BLOSUM62, gap open -10, gap extend -0.5, end gaps free (Biopython PairwiseAligner)",
        "references": rows,
        "query_extension_by_inferred_mature_start": ext,
    }
    Path(args.out).write_text(yaml.safe_dump(out, sort_keys=False, width=120))
    yaml.safe_dump(out, sys.stdout, sort_keys=False, width=120)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
