"""Full-query affine-gap fitting against each transcript orientation; no database search.
Scores are explicit inputs. Transcript flanks may be unaligned; every query base participates.
Coordinates are 1-based inclusive. A substitution is not interpreted as a biological variant.
"""
import argparse,json,hashlib
from pathlib import Path
from Bio import SeqIO,Align
import Bio

def pin(p):b=Path(p).read_bytes();return dict(path=Path(p).as_posix(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def fit(q,t,strand,args,index=0):
 oriented=q.seq if strand=='+'else q.seq.reverse_complement()
 a=Align.PairwiseAligner(mode='global',match_score=args.match,mismatch_score=args.mismatch,open_gap_score=args.open,extend_gap_score=args.extend)
 a.query_left_gap_score=0;a.query_right_gap_score=0
 alignments=a.align(t.seq,oriented);z=alignments[index];ts,qs=str(z[0]),str(z[1]);left=next(i for i,c in enumerate(qs)if c!='-');right=len(qs)-next(i for i,c in enumerate(qs[::-1])if c!='-');tp=qp=0;cols=[]
 for i,(tb,qb)in enumerate(zip(ts,qs)):
  if tb!='-':tp+=1
  if qb!='-':qp+=1
  if left<=i<right:cols.append(dict(target_nt=tp if tb!='-'else None,query_oriented_nt=qp if qb!='-'else None,query_original_nt=(qp if strand=='+'else len(q)-qp+1)if qb!='-'else None,target_base=tb,query_oriented_base=qb))
 tn=[c['target_nt']for c in cols if c['target_nt']is not None];qn=[c['query_oriented_nt']for c in cols if c['query_oriented_nt']is not None];assert qn==list(range(1,len(q)+1))
 changes=[c for c in cols if c['target_base']!=c['query_oriented_base']];matches=sum(c['target_base']==c['query_oriented_base']for c in cols);mismatches=sum(c['target_base']!='-'and c['query_oriented_base']!='-'and c['target_base']!=c['query_oriented_base']for c in cols);ins=sum(c['target_base']=='-'for c in cols);dele=sum(c['query_oriented_base']=='-'for c in cols)
 cds=[]
 for f in t.features:
  if f.type=='CDS':
   start,end=int(f.location.start)+1,int(f.location.end);s,e=min(tn),max(tn);cds.append(dict(start=start,end=end,strand=f.location.strand,wholly_within_CDS=s>=start and e<=end,target_frame_at_region_first_nt=(s-start)%3,overlapped_CDS_residues_1based=[(s-start)//3+1,(e-start)//3+1]))
 return dict(optimal_alignment_index=index,query_orientation=strand,score=z.score,optimal_alignment_count=len(alignments),target_start=min(tn),target_end=max(tn),query_nt=len(q),alignment_columns=len(cols),matching_nt=matches,substitutions=mismatches,query_inserted_nt=ins,target_inserted_nt=dele,aligned_query_fraction=len(qn)/len(q),exact_identity_of_query_nt=matches/len(q),changes=changes,target_CDS_relations=cds,aligned_target=ts[left:right],aligned_oriented_query=qs[left:right])
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('query');ap.add_argument('target');ap.add_argument('output');ap.add_argument('--match',type=float,default=2);ap.add_argument('--mismatch',type=float,default=-3);ap.add_argument('--open',type=float,default=-7);ap.add_argument('--extend',type=float,default=-1);v=ap.parse_args();q=SeqIO.read(v.query,'genbank');t=SeqIO.read(v.target,'genbank');results=[fit(q,t,s,v)for s in ['+','-']];reverse_optima=[fit(q,t,'-',v,i)for i in range(min(results[1]['optimal_alignment_count'],16))];r=dict(reverse_optima=reverse_optima,reverse_optima_limit=16,method='Full-query fitting, affine-gap global alignment with free transcript flanks. Both orientations analyzed; no BLAST or gene-name search.',parameters={k:getattr(v,k)for k in ['match','mismatch','open','extend']},biopython_version=Bio.__version__,query=pin(v.query),target=pin(v.target),results=results);Path(v.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps([{k:z[k]for k in ['query_orientation','score','optimal_alignment_count','target_start','target_end','matching_nt','substitutions','query_inserted_nt','target_inserted_nt','target_CDS_relations']}for z in results],indent=2))
