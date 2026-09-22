# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85"]
# ///
"""Global alignment of two downloaded UniProt text records; no orthology inference.
Usage: uv run compare.py human-uniprot.txt horse-uniprot.txt output.json
BLOSUM62, gap opening -10, extension -0.5. Coverage counts paired residues.
"""
import hashlib,json,sys
from pathlib import Path
from Bio import Align,SeqIO
from Bio.Align import substitution_matrices

def compare(left,right):
 records=[SeqIO.read(p,'fasta' if p.suffix in {'.fa','.fasta'} else 'swiss') for p in (left,right)]
 a=Align.PairwiseAligner();a.mode='global';a.substitution_matrix=substitution_matrices.load('BLOSUM62');a.open_gap_score=-10;a.extend_gap_score=-0.5
 best=a.align(records[0].seq,records[1].seq)[0]
 x,y=str(best[0]),str(best[1]);paired=sum(p!='-' and q!='-' for p,q in zip(x,y));identical=sum(p==q and p!='-' for p,q in zip(x,y))
 return dict(method='Biopython 1.85 global BLOSUM62, gap open -10, extension -0.5',inputs=[dict(path=str(p),accession=r.id,length=len(r),sequence_sha256=hashlib.sha256(str(r.seq).encode()).hexdigest()) for p,r in zip((left,right),records)],score=best.score,paired_residues=paired,identical_residues=identical,identity_among_paired=identical/paired,coverage_left=paired/len(records[0]),coverage_right=paired/len(records[1]),alignment=str(best),limitations='Pairwise similarity does not establish reciprocal orthology, full-length gene-model correctness or functional conservation.')
if __name__=='__main__':
 left,right,out=map(Path,sys.argv[1:]);out.write_text(json.dumps(compare(left,right),indent=2)+'\n')
