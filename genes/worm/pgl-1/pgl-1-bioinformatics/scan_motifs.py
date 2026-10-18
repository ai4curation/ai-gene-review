#!/usr/bin/env python3
"""Audit explicit motif regexes on arbitrary UniProt JSON inputs; coordinates are 1-based.
Exact short-pattern absence is not an HMM/fold analysis or a negative catalytic assay.
"""
import argparse, hashlib, json, re
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--patterns', type=Path, required=True)
parser.add_argument('records', type=Path, nargs='+')
args=parser.parse_args()
patterns=json.loads(args.patterns.read_text())
results=[]
for path in args.records:
    data=json.loads(path.read_text())
    seq=data['sequence']['value']
    if not re.fullmatch('[A-Z]+',seq):
        raise ValueError(f'Invalid amino-acid sequence in {path}')
    results.append({'input':str(path),'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'accession':data['primaryAccession'],'length':len(seq),
        'motifs':{name:{'regex':pattern,'matches':[{'start':m.start()+1,'end':m.end(),'sequence':m.group()} for m in re.finditer(pattern,seq)]} for name,pattern in patterns.items()}})
print(json.dumps(results,indent=2))
