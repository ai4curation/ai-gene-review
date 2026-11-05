"""Translate an annotated genomic CDS and compare with protein records, offline.
Uses Biopython from the repository uv environment. Outputs calculated observations only.
"""
import argparse, hashlib, json
from pathlib import Path
from Bio import SeqIO
p = argparse.ArgumentParser()
p.add_argument("--genomic", type=Path, required=True)
p.add_argument("--locus-tag", required=True)
p.add_argument("--protein", type=Path, required=True)
p.add_argument("--uniprot", type=Path, required=True)
p.add_argument("--historical", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
a = p.parse_args()
r = SeqIO.read(a.genomic, "genbank")
features = [f for f in r.features if f.type == "CDS" and a.locus_tag in f.qualifiers.get("locus_tag", [])]
if len(features) != 1:
    raise ValueError(f"Expected one matching CDS, found {len(features)}")
f = features[0]
dna = f.extract(r.seq)
table = int(f.qualifiers.get("transl_table", ["1"])[0])
translated = str(dna.translate(table=table))
protein = SeqIO.read(a.protein, "genbank")
u = SeqIO.read(a.uniprot, "swiss")
h = SeqIO.read(a.historical, "embl")
hf = next(f for f in h.features if f.type == "CDS")
hdna = str(hf.extract(h.seq))
hprotein = hf.qualifiers["translation"][0]
source = next(f for f in r.features if f.type == "source")
result = {
    "genomic_record": r.id, "source_strain": source.qualifiers.get("strain"),
    "locus_tag": a.locus_tag, "feature_location_in_download": str(f.location),
    "cds_location_parts": len(f.location.parts), "translation_table": table,
    "cds_nucleotides": len(dna), "terminal_codon": str(dna[-3:]),
    "terminal_stop": translated.endswith("*"),
    "internal_stop_count": translated[:-1].count("*"),
    "translated_amino_acids_without_terminal_stop": len(translated.rstrip("*")),
    "target_uniprot": u.id, "protein_record": protein.id,
    "translation_matches_uniprot": translated[:-1] == str(u.seq),
    "translation_matches_protein_record": translated[:-1] == str(protein.seq),
    "translation_matches_cds_qualifier": translated[:-1] == f.qualifiers["translation"][0],
    "historical_protein_exact_prefix": str(u.seq).startswith(hprotein),
    "historical_nucleotide_mismatches_in_aligned_prefix": [
        {"coding_position_1based": i+1, "historical": x, "modern": y}
        for i, (x,y) in enumerate(zip(hdna, str(dna))) if x != y],
    "historical_terminal_codon": hdna[-3:],
    "modern_codon_at_historical_termination_position": str(dna[len(hdna)-3:len(hdna)]),
    "input_sha256": {str(x): hashlib.sha256(x.read_bytes()).hexdigest()
                     for x in [a.genomic,a.protein,a.uniprot,a.historical]},
}
a.output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
