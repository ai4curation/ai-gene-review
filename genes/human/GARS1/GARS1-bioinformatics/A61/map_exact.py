"""Map a GenBank query nucleotide sequence to both strands of a GenBank transcript.
No alignment scoring, external lookup, or hardcoded expected sequence/location. Coordinates
are 1-based inclusive in output; Biopython feature coordinates are converted explicitly.
"""
import argparse,json,hashlib
from pathlib import Path
import Bio
from Bio import SeqIO

def pin(p):b=Path(p).read_bytes();return dict(path=Path(p).as_posix(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def occurrences(query,target):
 start=0
 while True:
  x=target.find(query,start)
  if x<0:return
  yield x;start=x+1

def run(query_path,target_path):
 q=SeqIO.read(query_path,'genbank');t=SeqIO.read(target_path,'genbank');qs=str(q.seq).upper();ts=str(t.seq).upper();cds=[f for f in t.features if f.type=='CDS'];matches=[]
 for label,seq in [('+',qs),('-',str(q.seq.reverse_complement()).upper())]:
  for start in occurrences(seq,ts):
   end=start+len(seq);ov=[]
   for f in cds:
    a,b=int(f.location.start),int(f.location.end);n=max(0,min(end,b)-max(start,a));ov.append(dict(target_CDS_start=a+1,target_CDS_end=b,strand=f.location.strand,overlap_nt=n,query_relative_to_CDS='wholly_5prime_UTR'if end<=a else'wholly_3prime_UTR'if start>=b else'wholly_CDS'if start>=a and end<=b else'partial_CDS_overlap',same_strand_as_CDS=(label=='+'and f.location.strand==1)or(label=='-'and f.location.strand==-1),offset_mod3=(start-a)%3))
   matches.append(dict(orientation=label,target_start=start+1,target_end=end,identity_nt=len(qs),query_length=len(qs),CDS_relations=ov))
 qcds=[]
 for f in q.features:
  if f.type=='CDS':
   codon=int(f.qualifiers.get('codon_start',['1'])[0]);seq=f.extract(q.seq)[codon-1:];protein=str(seq[:len(seq)//3*3].translate());decl=f.qualifiers.get('translation',[None])[0];qcds.append(dict(location=str(f.location),codon_start=codon,protein_id=f.qualifiers.get('protein_id'),translated_sequence=protein,declared_translation=decl,translation_exact=(protein==decl)))
 targetcds=[]
 for f in cds:
  codon=int(f.qualifiers.get('codon_start',['1'])[0]);seq=f.extract(t.seq)[codon-1:];p=str(seq[:len(seq)//3*3].translate()).rstrip('*');decl=f.qualifiers.get('translation',[None])[0];targetcds.append(dict(location=str(f.location),protein_id=f.qualifiers.get('protein_id'),gene=f.qualifiers.get('gene'),length=len(p),translated_sequence=p,translation_exact=(p==decl),query_peptide_occurrences=[dict(query_protein_id=x['protein_id'],starts_1based=[i+1 for i in occurrences(x['translated_sequence'],p)])for x in qcds]))
 return dict(method='Exact complete nucleotide substring search on both transcript orientations; independently translate declared query/target CDS using their codon_start. No BLAST or sequence-similarity attribution.',Biopython_version=Bio.__version__,query=pin(query_path),target=pin(target_path),query_id=q.id,target_id=t.id,query_length=len(q.seq),target_length=len(t.seq),query_description=q.description,target_description=t.description,exact_matches=matches,query_CDS=qcds,target_CDS=targetcds)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('query');a.add_argument('target');a.add_argument('output');v=a.parse_args();r=run(v.query,v.target);Path(v.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k]for k in ['query_id','target_id','query_length','target_length','exact_matches']}))
