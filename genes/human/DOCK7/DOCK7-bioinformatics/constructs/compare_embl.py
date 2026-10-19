#!/usr/bin/env python3
"""Extract a CDS translation from saved EMBL, or compare an input FASTA, to UniProt.
All inputs are command-line paths. No biological conclusion is encoded.
"""
import argparse,json,re,hashlib,difflib
from pathlib import Path
p=argparse.ArgumentParser();q=p.add_mutually_exclusive_group(required=True);q.add_argument('--embl',type=Path);q.add_argument('--fasta',type=Path);p.add_argument('--uniprot',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();query=a.embl or a.fasta
if a.embl:
 t=query.read_text();m=re.search(r'/translation="(.*?)"',t,re.S);assert m,'No CDS translation';seq=''.join(re.sub(r'^FT\s*','',m.group(1),flags=re.M).split());identity={'source_format':'EMBL','identification_lines':[x for x in t.splitlines()if x.startswith(('ID ','DE ','OS '))],'protein_id':re.search(r'/protein_id="([^"]+)"',t).group(1)}
else:
 lines=query.read_text().splitlines();assert lines[0].startswith('>');seq=''.join(lines[1:]);identity={'source_format':'FASTA','header':lines[0]}
assert set(seq)<=set('ACDEFGHIKLMNPQRSTVWYBXZUO*');u=json.loads(a.uniprot.read_text());ref=u['sequence']['value'];ops=difflib.SequenceMatcher(None,seq,ref,autojunk=False).get_opcodes()
r={'query_identity':identity,'query_length':len(seq),'reference':u['primaryAccession'],'reference_length':len(ref),'inputs':{name:{'filename':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}for name,f in [('query',query),('reference',a.uniprot)]},'exact_equal':seq==ref,'opcodes':[{'operation':op,'query_zero_based_half_open':[i,j],'reference_zero_based_half_open':[k,l],'query_sequence':seq[i:j]if op!='equal'else None,'reference_sequence':ref[k:l]if op!='equal'else None}for op,i,j,k,l in ops]};a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'query_length':len(seq),'reference_length':len(ref),'exact_equal':r['exact_equal'],'operations':len(ops)}))
