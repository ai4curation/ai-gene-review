# /// script
# dependencies = ["biopython>=1.85", "requests>=2.32"]
# ///
"""Reproduce the 2019 StFtsW primer-to-reference construct mapping.

Run: uv run genes/STRT2/ftsW/ftsW-source-analysis/verify_construct.py
The authoritative genome is retrieved in memory; no raw gene source is changed.
Primers are from PMID30692671 Supplementary Table 5, oAT01 and oAT02.
"""
from pathlib import Path
import hashlib
import io
import json
import requests
from Bio import SeqIO
from Bio.Seq import Seq

ROOT = Path(__file__).resolve().parents[4]
URL = 'https://www.ebi.ac.uk/ena/browser/api/embl/CP000023?download=false'
response = requests.get(URL, timeout=90)
response.raise_for_status()
genome = SeqIO.read(io.StringIO(response.text), 'embl')
cds = next(f for f in genome.features if f.type == 'CDS' and
           f.qualifiers.get('locus_tag') == ['stu0486'])
dna = cds.extract(genome.seq)
uniprot = SeqIO.read(ROOT/'genes/STRT2/ftsW/ftsW-uniprot.txt', 'swiss')
assert str(dna.translate(to_stop=True)) == str(uniprot.seq)
forward = 'ATGAAAATTGAAAAGAAACATCTTTTGG'
reverse = 'CTAACGACTTCTTCTCAAAGGTA'
start = str(dna).find(forward)
end = str(dna).find(str(Seq(reverse).reverse_complement())) + len(reverse)
assert (start, end) == (15, 1296)
protein = dna[start:end].translate(to_stop=True)
assert str(protein) == str(uniprot.seq[5:]) and len(protein) == 426
assert protein[291] == uniprot.seq[296] == 'D'
assert protein[344] == uniprot.seq[349] == 'L'
print(json.dumps({
    'target': 'Q5M5I9', 'genome': 'CP000023.1',
    'genome_response_sha256': hashlib.sha256(response.content).hexdigest(),
    'full_reference_length': len(uniprot.seq), 'construct_length': len(protein),
    'construct_reference_residues': '6..431',
    'paper_to_current_positions': {'D292': 'D297', 'L345': 'L350'},
    'interpretation': 'Assay construct omission; not a proven native start-site error',
}, indent=2))
