"""How do the two coding transcripts differ? Compare exon structures from the RefSeq GenBank records.

NM_153486 encodes UniProt isoform 1 (507 aa, the 'displayed' sequence); NM_194436
encodes isoform 2 (484 aa) and is the MANE Select transcript. This script locates the
69-nt difference in exon coordinates and reports the donor/acceptor dinucleotide context
that the transcript sequences allow us to see (exon ends only; introns are not in mRNA).
"""
from __future__ import annotations

import json

from Bio import SeqIO

import common as c


def exons(nm):
    rec = SeqIO.read(c.DATA / f"{nm}.gb", "genbank")
    cds = [f for f in rec.features if f.type == "CDS"][0]
    start = int(cds.location.start)
    ex = [(int(f.location.start), int(f.location.end)) for f in rec.features if f.type == "exon"]
    return rec, start, ex


def main():
    out = {}
    recs = {nm: exons(nm) for nm in ("NM_153486", "NM_194436")}
    for nm, (rec, start, ex) in recs.items():
        out[nm] = {"version": rec.id, "n_exons": len(ex), "exon_lengths": [b - a for a, b in ex],
                   "exon_cds_ranges": [[a - start + 1, b - start] for a, b in ex]}
    l1, l2 = out["NM_153486"]["exon_lengths"], out["NM_194436"]["exon_lengths"]
    diff = [(i + 1, a, b) for i, (a, b) in enumerate(zip(l1, l2)) if a != b]
    out["exon_length_differences_(exon,NM_153486,NM_194436)"] = diff
    seg = [f for f in c.uniprot_features() if f["type"] == "Alternative sequence"][0]
    a, b = seg["location"]["start"]["value"], seg["location"]["end"]["value"]
    cds_a, cds_b = (a - 1) * 3 + 1, b * 3
    out["isoform1_only_segment_cds_range_NM_153486"] = [cds_a, cds_b]
    rec1, start1, ex1 = recs["NM_153486"]
    hit = [(i + 1, s - start1 + 1, e - start1) for i, (s, e) in enumerate(ex1) if s - start1 + 1 <= cds_b and e - start1 >= cds_a]
    out["exons_containing_segment_(exon,cds_start,cds_end)"] = hit
    seq1 = str(rec1.seq[start1:])
    out["segment_nt"] = seq1[cds_a - 1:cds_b]
    out["segment_position_within_exon"] = None
    if len(hit) == 1:
        _, s, e = hit[0]
        out["segment_position_within_exon"] = {"nt_from_exon_start": cds_a - s, "nt_to_exon_end": e - cds_b}
        out["segment_first_two_nt"] = seq1[cds_a - 1:cds_a + 1]
        out["segment_last_two_nt"] = seq1[cds_b - 2:cds_b]
        # all 69-nt windows in the exon whose removal reproduces the isoform-2 CDS (the junction is ambiguous by a few nt)
        cds2 = c.transcripts()["NM_194436"]["cds"]
        cds1 = c.transcripts()["NM_153486"]["cds"]
        wins = [i for i in range(s - 1, e - 68) if cds1[:i] + cds1[i + 69:] == cds2]
        out["equivalent_69nt_deletion_windows_(0-based cds start)"] = wins
        out["window_start_dinucleotides"] = [cds1[i:i + 2] for i in wins]
        out["window_end_dinucleotides"] = [cds1[i + 67:i + 69] for i in wins]
        out["nt_from_exon_start_for_windows"] = [i - (s - 1) for i in wins]
        out["nt_to_exon_end_for_windows"] = [e - (i + 69) for i in wins]
    (c.RESULTS / "isoform_exons.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
