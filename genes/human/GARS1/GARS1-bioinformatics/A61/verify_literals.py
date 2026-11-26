"""Independently check alignment blocks by literal slices and official translation."""
import argparse,json
from pathlib import Path
from Bio import SeqIO
p=argparse.ArgumentParser();p.add_argument("query");p.add_argument("target");p.add_argument("uniprot");p.add_argument("fit");p.add_argument("output");a=p.parse_args()
q=SeqIO.read(a.query,"genbank");t=SeqIO.read(a.target,"genbank");u=json.loads(Path(a.uniprot).read_text());f=json.loads(Path(a.fit).read_text());z=f["reverse_optima"][0]
tcds=next(x for x in t.features if x.type=="CDS");qcds=next(x for x in q.features if x.type=="CDS")
tprotein=str(tcds.extract(t.seq)[int(tcds.qualifiers.get("codon_start",[1])[0])-1:].translate()).rstrip("*");qprotein=str(qcds.extract(q.seq)[int(qcds.qualifiers.get("codon_start",[1])[0])-1:].translate()).rstrip("*")
assert tprotein==tcds.qualifiers["translation"][0]==u["sequence"]["value"]
assert qprotein==qcds.qualifiers["translation"][0]
tp=z["target_start"]-1;qp=0;runs=[];run=[]
for tb,qb in zip(z["aligned_target"],z["aligned_oriented_query"]):
 if tb!="-":tp+=1
 if qb!="-":qp+=1
 if tb==qb and tb!="-":run.append((tp,qp))
 else:
  if run:runs.append(run);run=[]
if run:runs.append(run)
blocks=[]
for run in runs:
 s,e=run[0],run[-1];ts=str(t.seq[s[0]-1:e[0]]);qs=str(q.seq.reverse_complement()[s[1]-1:e[1]]);assert ts==qs
 if len(run)>=10:blocks.append(dict(target_start=s[0],target_end=e[0],oriented_query_start=s[1],oriented_query_end=e[1],original_query_start=len(q)-e[1]+1,original_query_end=len(q)-s[1]+1,length=len(run),sequence=ts))
assert sum(len(x)for x in runs)==z["matching_nt"]
result=dict(refseq_translation_equals_official_UniProt=True,refseq_translation_length=len(tprotein),original_query_declared_peptide_matches_translation=True,original_query_peptide_exact_start_1based=tprotein.find(qprotein)+1 if qprotein in tprotein else None,exact_unbroken_blocks=blocks,reverse_all_optima_same_span_and_counts=len({tuple(x[k]for k in ["target_start","target_end","matching_nt","substitutions","query_inserted_nt","target_inserted_nt"])for x in f["reverse_optima"]})==1,matching_query_fraction=z["matching_nt"]/len(q),matching_alignment_column_fraction=z["matching_nt"]/z["alignment_columns"])
Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
