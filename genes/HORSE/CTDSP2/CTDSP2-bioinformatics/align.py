"""Align cached human and horse UniProt sequences; does not infer orthology."""
from pathlib import Path
import json,hashlib
from Bio import Align,SwissProt
here=Path(__file__).resolve().parent
gene=here.parent.name
horse_file=here.parent/(gene+'-uniprot.txt')
human_file=here.parents[2]/'human'/gene/(gene+'-uniprot.txt')
with horse_file.open() as f: horse=SwissProt.read(f)
with human_file.open() as f: human=SwissProt.read(f)
a=Align.PairwiseAligner();a.mode='global';a.match_score=2;a.mismatch_score=-1;a.open_gap_score=-10;a.extend_gap_score=-0.5
aln=a.align(human.sequence,horse.sequence)[0]
x,y=str(aln[0]),str(aln[1]);pairs=[(u,v) for u,v in zip(x,y) if u!='-' and v!='-'];ident=sum(u==v for u,v in pairs)
result={'human_accession':human.accessions[0],'horse_accession':horse.accessions[0],'human_length':len(human.sequence),'horse_length':len(horse.sequence),'paired_residues':len(pairs),'identical_residues':ident,'identity_among_paired_residues':ident/len(pairs),'human_paired_coverage':len(pairs)/len(human.sequence),'horse_paired_coverage':len(pairs)/len(horse.sequence),'human_sequence_sha256':hashlib.sha256(human.sequence.encode()).hexdigest(),'horse_sequence_sha256':hashlib.sha256(horse.sequence.encode()).hexdigest(),'alignment_parameters':{'mode':'global','match':2,'mismatch':-1,'gap_open':-10,'gap_extend':-0.5}}
(here/'alignment.txt').write_text(str(aln)+'\n');(here/'results.json').write_text(json.dumps(result,indent=2)+'\n')
(here/'RESULTS.md').write_text(f'''# {gene}: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **{ident}/{len(pairs)} identical paired residues ({ident/len(pairs):.1%})**. Paired coverage is {len(pairs)/len(human.sequence):.1%} of human {human.accessions[0]} ({len(human.sequence)} aa) and {len(pairs)/len(horse.sequence):.1%} of horse {horse.accessions[0]} ({len(horse.sequence)} aa).

Reproduce from the repository root with `uv run python genes/HORSE/{gene}/{gene}-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.
''')
print(gene,result['identity_among_paired_residues'])
# Map every curated human catalytic/binding/transit/membrane feature through alignment.
map_horse={};hp=qp=0
for u,v in zip(x,y):
 if u!='-':
  hp+=1
  if v!='-':map_horse[hp]=(qp+1,v)
 if v!='-':qp+=1
lines=['\n## Human feature correspondence\n','These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.\n','| Human feature | Human positions | Paired horse positions | Identical / paired |','|---|---|---|---|']
for f in human.features:
 if f.type not in {'ACT_SITE','BINDING','TRANSIT','SIGNAL','TRANSMEM'}:continue
 try:start,end=int(f.location.start)+1,int(f.location.end)
 except (TypeError,ValueError):continue
 mapped=[(n,map_horse[n]) for n in range(start,end+1) if n in map_horse]
 same=sum(human.sequence[n-1]==aa for n,(_,aa) in mapped)
 vals=','.join(str(pos) for _,(pos,_) in mapped)
 lines.append(f'| {f.type} | {start}–{end} | {vals or "unaligned/deleted"} | {same}/{len(mapped)} |')
with (here/'RESULTS.md').open('a') as f:f.write('\n'.join(lines)+'\n')
