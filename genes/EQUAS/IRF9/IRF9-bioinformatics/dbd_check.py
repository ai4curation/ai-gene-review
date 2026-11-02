"""Check the IRF tryptophan-pentad DNA-binding domain of donkey IRF9 against human IRF9.
Uses the human DNA_BIND feature and the global alignment from compare_pair.py settings.
Run: uv run python genes/EQUAS/IRF9/IRF9-bioinformatics/dbd_check.py
"""
from pathlib import Path
from Bio import SeqIO, Align
here = Path(__file__).resolve().parent
human = SeqIO.read(here / 'human_Q00978-uniprot.txt', 'swiss')
donkey = SeqIO.read(here.parent / 'IRF9-uniprot.txt', 'swiss')
a, b = str(human.seq), str(donkey.seq)
al = Align.PairwiseAligner(mode='global', match_score=2, mismatch_score=-1,
                           open_gap_score=-10, extend_gap_score=-0.5).align(a, b)[0]
m = {}
for (s, e), (t, u) in zip(*al.aligned):
    for i, j in zip(range(s, e), range(t, u)):
        m[i] = j
dbd = next(f for f in human.features if f.type == 'DNA_BIND')
s, e = int(dbd.location.start), int(dbd.location.end)
pairs = [(i, m.get(i)) for i in range(s, e)]
ident = sum(1 for i, j in pairs if j is not None and a[i] == b[j])
trp = [(i + 1, (m[i] + 1) if i in m else None, b[m[i]] if i in m else '-') for i in range(s, e) if a[i] == 'W']
lines = ['# IRF9 DNA-binding domain check', '',
         f'Human DNA_BIND {s+1}-{e} ({dbd.qualifiers.get("note", "")}): {ident} of {e-s} residues identical in donkey {donkey.id}.',
         '', 'Human tryptophans in the DNA-binding domain and the aligned donkey residue:', '']
lines += [f'- human W{h} -> donkey {r}{d}' for h, d, r in trp]
(here / 'dbd_check.md').write_text('\n'.join(lines) + '\n')
print('\n'.join(lines))
