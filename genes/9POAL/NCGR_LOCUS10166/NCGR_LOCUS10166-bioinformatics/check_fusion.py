# /// script
# requires-python = ">=3.12"
# dependencies = ["biopython==1.85", "requests==2.32.5"]
# ///
"""Compare deposited CDS coordinates and sequences, without assuming a fusion is real."""
from pathlib import Path
import hashlib
import io
import json
import re
import requests
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
RAW = HERE / "inputs"
RAW.mkdir(exist_ok=True)
ACCESSIONS = {"candidate": "CAD6214881.1", "hdh": "CAD6206931.1", "arv": "CAD6206930.1"}
records = {}
provenance = {}
for name, accession in ACCESSIONS.items():
    path = RAW / f"{accession}.gp"
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
           f"?db=protein&id={accession}&rettype=gp&retmode=text")
    if not path.exists():
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        SeqIO.read(io.StringIO(response.text), "genbank")
        path.write_text(response.text)
    records[name] = SeqIO.read(path, "genbank")
    provenance[name] = {"url": url, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

aligner = Align.PairwiseAligner(mode="local")
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
out = {"method": "Local BLOSUM62, gap open -10, extend -0.5; coordinates are 1-based inclusive.",
       "provenance": provenance, "records": {}, "alignments": {}}
for name, record in records.items():
    cds = next(f for f in record.features if f.type == "CDS")
    coded_by = cds.qualifiers["coded_by"][0]
    spans = re.findall(r"([A-Z0-9]+\.\d+):(\d+)\.\.(\d+)", coded_by)
    out["records"][name] = {"protein": record.id, "length": len(record.seq),
        "locus": cds.qualifiers["locus_tag"][0], "coded_by": coded_by,
        "genomic_accessions": sorted({x[0] for x in spans}),
        "genomic_min": min(int(x[1]) for x in spans),
        "genomic_max": max(int(x[2]) for x in spans),
        "cds_note": cds.qualifiers.get("note", []),
        "sites": [{"positions": [int(p)+1 for p in f.location],
                   "residues": "".join(str(record.seq)[int(p)] for p in f.location),
                   "qualifiers": f.qualifiers} for f in record.features if f.type == "Site"]}

target = str(records["candidate"].seq)
for name in ("hdh", "arv"):
    query = str(records[name].seq)
    alignment = aligner.align(target, query)[0]
    rows = list(alignment)
    matched = sum(a == b for a, b in zip(*rows))
    paired = sum(a != "-" and b != "-" for a, b in zip(*rows))
    start, end = alignment.coordinates[:, 0], alignment.coordinates[:, -1]
    out["alignments"][name] = {"score": alignment.score, "identical": matched,
        "paired_columns": paired, "alignment_columns": len(rows[0]),
        "identity_over_columns": matched/len(rows[0]),
        "target_start": int(start[0])+1, "target_end": int(end[0]),
        "reference_start": int(start[1])+1, "reference_end": int(end[1]),
        "reference_length": len(query),
        "reference_unaligned_N_terminus": query[:int(start[1])],
        "reference_unaligned_C_terminus": query[int(end[1]):]}
    (HERE / f"{name}-local-alignment.txt").write_text(str(alignment))

a, b = out["records"]["arv"], out["records"]["hdh"]
out["separate_gene_coordinates"] = {
    "same_genomic_accession": a["genomic_accessions"] == b["genomic_accessions"],
    "intergenic_bases": b["genomic_min"]-a["genomic_max"]-1,
    "candidate_on_same_accession": a["genomic_accessions"] == out["records"]["candidate"]["genomic_accessions"]}
out["limitations"] = ["Local identity excludes unaligned ends; it is not whole-protein identity.",
    "Deposited CDS models and CDD sites are computational annotations, not transcript or activity assays.",
    "Coordinates establish physical adjacency of the separate genes, not transcript structure at the candidate locus.",
    "No RNA-seq, proteomic, targeting, or fusion-junction experiment is performed here."]
(HERE / "results.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k not in ("records", "provenance")}, indent=2))
