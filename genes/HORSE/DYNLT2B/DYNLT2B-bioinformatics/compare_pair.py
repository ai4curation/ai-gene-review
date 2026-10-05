"""Compare the selected horse protein with the fetched human reference.
Run with the repository environment: uv run python PATH/compare_pair.py.
This is a pairwise conservation check, not a phylogenetic orthology test.
"""
from pathlib import Path
import json, hashlib
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
here=Path(__file__).resolve().parent
gene=here.parent.name
root=next(p for p in here.parents if (p/'pyproject.toml').exists())
human=SeqIO.read(root/'genes/human'/gene/f'{gene}-uniprot.txt','swiss')
horse=SeqIO.read(here.parent/f'{gene}-uniprot.txt','swiss')
a,b=str(human.seq),str(horse.seq)
aligner=Align.PairwiseAligner(mode='global',substitution_matrix=substitution_matrices.load('BLOSUM62'),open_gap_score=-10,extend_gap_score=-0.5)
al=aligner.align(a,b)[0]
map_horse={}
for (s,e),(t,u) in zip(*al.aligned):
 for i,j in zip(range(s,e),range(t,u)):map_horse[int(i)]=int(j)
n=len(map_horse); ident=sum(a[i]==b[j] for i,j in map_horse.items())
features=[]
for f in human.features:
 if f.type in ['ACT_SITE','BINDING','METAL','STRAND']:
  pos=range(int(f.location.start),int(f.location.end))
  if len(pos)>20:continue
  features.append({'type':f.type,'human_positions_1based':[i+1 for i in pos],'human_residues':''.join(a[i] for i in pos),'horse_positions_1based':[map_horse[i]+1 if i in map_horse else None for i in pos],'horse_residues':''.join(b[map_horse[i]] if i in map_horse else '-' for i in pos),'qualifiers':f.qualifiers})
r={'human_id':human.id,'horse_id':horse.id,'human_length':len(a),'horse_length':len(b),'paired_residues':n,'identical_residues':ident,'identity_paired_percent':round(100*ident/n,2),'human_paired_coverage_percent':round(100*n/len(a),2),'horse_paired_coverage_percent':round(100*n/len(b),2),'human_sha256':hashlib.sha256(a.encode()).hexdigest(),'horse_sha256':hashlib.sha256(b.encode()).hexdigest(),'human_features_mapped':features}
(here/'results.json').write_text(json.dumps(r,indent=2)+'\n')
(here/'alignment.txt').write_text(str(al))
lines=[f'# {gene}: horse–human sequence comparison','',f"The horse sequence {horse.id} ({len(b)} residues) aligns to human {human.id} ({len(a)} residues) with {r['identity_paired_percent']}% identity across {n} paired residues. Paired coverage is {r['human_paired_coverage_percent']}% of the human sequence and {r['horse_paired_coverage_percent']}% of the horse sequence.",'','Global alignment uses Biopython PairwiseAligner, BLOSUM62, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human structural features are in `results.json`. Reproduce with `uv run python '+str(here.relative_to(root)/'compare_pair.py')+'`.','','This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.','','## Mapped human structural features','']
for x in features:lines.append(f"- {x['type']}: human {x['human_positions_1based']} {x['human_residues']} → horse {x['horse_positions_1based']} {x['horse_residues']}.")
(here/'RESULTS.md').write_text('\n'.join(lines)+'\n')
print(gene,r['identity_paired_percent'],r['human_paired_coverage_percent'],r['horse_paired_coverage_percent'])
