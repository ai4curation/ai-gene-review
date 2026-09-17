#!/usr/bin/env python3
"""Map source-record active sites through a Pfam profile alignment; no biological calls."""
import argparse, hashlib, json, subprocess
from pathlib import Path

def fasta(path):
    seqs={}; key=None
    for line in Path(path).read_text().splitlines():
        if line.startswith('>'): key=line[1:].split()[0]; seqs[key]=''
        elif key: seqs[key]+=line.strip()
    return seqs

def main():
    p=argparse.ArgumentParser(); p.add_argument('--hmm',required=True); p.add_argument('--target',required=True); p.add_argument('--reference',action='append',required=True); p.add_argument('--output',required=True); a=p.parse_args()
    out=Path(a.output); out.mkdir(exist_ok=True)
    seqs=fasta(a.target); target=next(iter(seqs)); records=[]
    for path in a.reference:
        rec=json.loads(Path(path).read_text()); acc=rec['primaryAccession']; seqs[acc]=rec['sequence']['value']; records.append(rec)
    inputs=out/'combined.fasta'; inputs.write_text(''.join(f'>{k}\n{v}\n' for k,v in seqs.items()))
    alignment=subprocess.run(['hmmalign','--outformat','afa',a.hmm,str(inputs)],capture_output=True,text=True,check=True).stdout
    (out/'profile-alignment.fasta').write_text(alignment)
    ali=fasta(out/'profile-alignment.fasta'); positions={}
    for name,s in ali.items():
        pos=0; d={}
        for col,res in enumerate(s):
            if res not in '.-': pos+=1; d[col]=(pos,res)
        positions[name]=d
    maps=[]
    for rec in records:
        acc=rec['primaryAccession']
        for f in rec.get('features',[]):
            if f['type']!='Active site': continue
            pos=f['location']['start']['value']; col=next(c for c,v in positions[acc].items() if v[0]==pos)
            maps.append({'reference':acc,'reference_position':pos,'reference_residue':seqs[acc][pos-1], 'alignment_column':col+1,'reference_in_profile_match':ali[acc][col].isupper(), 'target_position':positions[target].get(col,[None,None])[0], 'target_residue':positions[target].get(col,[None,None])[1], 'target_context':ali[target][max(0,col-8):col+9]})
    subprocess.run(['hmmsearch','--domtblout',str(out/'domains.tsv'),'-o',str(out/'hmmsearch.txt'),a.hmm,str(inputs)],check=True)
    metrics={k:{'length':len(v),'sha256':hashlib.sha256(v.encode()).hexdigest(),'matched_residues':sum(c.isupper() for c in ali[k])} for k,v in seqs.items()}
    (out/'results.json').write_text(json.dumps({'hmm_sha256':hashlib.sha256(Path(a.hmm).read_bytes()).hexdigest(),'sequences':metrics,'active_site_mapping':maps},indent=2)+'\n')
if __name__=='__main__': main()
