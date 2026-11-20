"""Reproduce the BL21 OpgG precursor to KT2440 residue mapping; no source edits."""
from pathlib import Path
import hashlib
import json
from Bio import Align
from Bio import __version__ as biopython_version

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
source = HERE / "CAQ31569.1.fasta"
target = HERE.parent / "opgG-uniprot.txt"
reference = ROOT / "genes/ECOLI/opgG/opgG-uniprot.txt"

def flat_sequence(path):
    return "".join(path.read_text().split("SQ   SEQUENCE")[1].splitlines()[1:-1]).replace(" ", "")

s = "".join(source.read_text().splitlines()[1:])
t = flat_sequence(target)
a = Align.PairwiseAligner()
a.mode = "global"
a.match_score = 2
a.mismatch_score = -1
a.open_gap_score = -5
a.extend_gap_score = -0.5
aln = a.align(s, t)[0]
mapping = {int(i)+1: int(j)+1 for i, j in zip(*aln.indices) if i >= 0 and j >= 0}
roles = {56: "ligand-contact aromatic residue", 273: "conserved catalytic-pocket aspartate", 332: "conserved catalytic-pocket arginine", 361: "catalytic aspartate, D361N structural mutant", 415: "Loop A", 417: "OpgG-like Loop A leucine"}
result = {
    "source": "NCBI CAQ31569.1, BL21(DE3) precursor used as PCR template in PMID37735577",
    "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=CAQ31569.1&rettype=fasta&retmode=text",
    "biopython": biopython_version,
    "alignment_parameters": {"mode": "global", "match": 2, "mismatch": -1, "gap_open": -5, "gap_extend": -0.5},
    "source_length": len(s), "target_length": len(t),
    "source_equals_frozen_K12_P33136": s == flat_sequence(reference),
    "identical_residues": sum(s[i] == t[j] for i, j in zip(*aln.indices) if i >= 0 and j >= 0),
    "alignment_columns_including_gaps": aln.length,
    "mapping": [{"source_position": k, "source_residue": s[k-1], "target_position": mapping[k], "target_residue": t[mapping[k]-1], "role": v} for k, v in roles.items()],
    "input_sha256": {str(x.relative_to(ROOT)): hashlib.sha256(x.read_bytes()).hexdigest() for x in [source,target,reference]},
    "limitations": "Sequence/active-pocket conservation supports homologous chemical capability, not identical kinetics, a direct KT2440 assay, obligatory native hydrolysis, or an experimentally established OpgG-OpgH complex. The source assay removed a predicted signal sequence and added C-terminal His6. Positions follow full precursor numbering, corroborated by 8IP2 authors' numbering. Y56F precludes claiming every binding contact is identical."
}
(HERE / "residue-map.json").write_text(json.dumps(result, indent=2)+"\n")
(HERE / "alignment.txt").write_text(str(aln)+"\n")
print(json.dumps(result, indent=2))
