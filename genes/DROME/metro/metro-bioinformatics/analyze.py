"""Map user-specified reference sites across annotated GUK domains; no verdicts."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

p=argparse.ArgumentParser()
p.add_argument('--data', type=Path, required=True)
p.add_argument('--reference', required=True)
p.add_argument('--positions', type=int, nargs='+', required=True)
p.add_argument('--out', type=Path, required=True)
a=p.parse_args()
a.out.mkdir(parents=True, exist_ok=True)
records={}
for path in sorted(a.data.glob('*.json')):
    r=json.loads(path.read_text())
    domains=[f for f in r.get('features',[]) if f['type']=='Domain' and f.get('description')=='Guanylate kinase-like']
    if len(domains)!=1:
        raise ValueError(f'{path}: expected one annotated GUK domain')
    start=domains[0]['location']['start']['value']; end=domains[0]['location']['end']['value']
    records[r['primaryAccession']]={'start':start,'end':end,'sequence':r['sequence']['value'][start-1:end], 'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
if a.reference not in records:
    raise ValueError('Reference absent')
for pos in a.positions:
    if not records[a.reference]['start'] <= pos <= records[a.reference]['end']:
        raise ValueError('Reference site outside domain')
fasta=a.out/'domains.fasta'
fasta.write_text(''.join(f'>{acc}\n{r["sequence"]}\n' for acc,r in records.items()))
results={'records':records,'reference':a.reference,'positions':a.positions,'alignments':{}}
for strategy in ['localpair','globalpair']:
    command=['mafft','--'+strategy,'--maxiterate','1000','--thread','1',str(fasta)]
    cp=subprocess.run(command,capture_output=True,text=True,check=True)
    (a.out/(strategy+'.fasta')).write_text(cp.stdout)
    (a.out/(strategy+'.stderr.txt')).write_text(cp.stderr)
    seqs={}; current=None
    for line in cp.stdout.splitlines():
        if line.startswith('>'): current=line[1:].split()[0];seqs[current]=''
        else: seqs[current]+=line.strip().upper()
    maps={}
    for acc,seq in seqs.items():
        index=records[acc]['start']-1
        maps[acc]=[]
        for ch in seq:
            if ch!='-': index+=1
            maps[acc].append(index if ch!='-' else None)
        assert seq.replace('-','')==records[acc]['sequence']
    sites=[]
    for pos in a.positions:
        col=maps[a.reference].index(pos)
        sites.append({'reference_position':pos,'reference_residue':seqs[a.reference][col], 'targets':{acc:{'position':maps[acc][col],'residue':seq[col],'window':seq[max(0,col-5):col+6]} for acc,seq in seqs.items()}})
    results['alignments'][strategy]={'command':command,'sites':sites}
(a.out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
for method,result in results['alignments'].items():
    print(method)
    for row in result['sites']:
        print(row['reference_position'],row['reference_residue'], ' '.join(f'{acc}:{v["residue"]}{v["position"]}' for acc,v in row['targets'].items()))
