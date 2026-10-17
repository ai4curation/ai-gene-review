"""Compare the selected donkey protein with its fetched human UniProt reference.
Usage: uv run python PATH/compare_pair.py [HUMAN_UNIPROT_FLATFILE]
Default human file: the single human_*-uniprot.txt in this folder.
This is a pairwise conservation check, not a phylogenetic orthology test.
"""
from pathlib import Path
import json, hashlib, sys
from Bio import SeqIO, Align
here = Path(__file__).resolve().parent
gene = here.parent.name
root = next(p for p in here.parents if (p / 'pyproject.toml').exists())
if len(sys.argv) > 1:
    hpath = Path(sys.argv[1]).resolve()
else:
    hpath = next(here.glob('human_*-uniprot.txt'))
human = SeqIO.read(hpath, 'swiss')
donkey = SeqIO.read(here.parent / f'{gene}-uniprot.txt', 'swiss')
a, b = str(human.seq), str(donkey.seq)
aligner = Align.PairwiseAligner(mode='global', match_score=2, mismatch_score=-1,
                                open_gap_score=-10, extend_gap_score=-0.5)
al = aligner.align(a, b)[0]
m = {}
for (s, e), (t, u) in zip(*al.aligned):
    for i, j in zip(range(s, e), range(t, u)):
        m[int(i)] = int(j)
n = len(m)
ident = sum(a[i] == b[j] for i, j in m.items())
# unaligned donkey segments (insertions relative to human)
dk_aligned = sorted(m.values())
ins = []
prev = -1
for j in dk_aligned + [len(b)]:
    if j - prev > 1:
        ins.append((prev + 2, j))  # 1-based start..end
    prev = j
ins = [(s, e) for s, e in ins if e - s + 1 >= 5]
# unaligned human segments (regions of human absent from the donkey sequence)
hum_ins = []
prev = -1
for i in sorted(m.keys()) + [len(a)]:
    if i - prev > 1:
        hum_ins.append((prev + 2, i))
    prev = i
hum_ins = [(s, e) for s, e in hum_ins if e - s + 1 >= 5]
features = []
for f in human.features:
    if f.type in ['ACT_SITE', 'BINDING', 'METAL', 'SITE', 'MOTIF']:
        pos = range(int(f.location.start), int(f.location.end))
        if len(pos) > 8:
            continue
        features.append({'type': f.type,
                         'note': f.qualifiers.get('note', ''),
                         'human_positions_1based': [i + 1 for i in pos],
                         'human_residues': ''.join(a[i] for i in pos),
                         'donkey_positions_1based': [m[i] + 1 if i in m else None for i in pos],
                         'donkey_residues': ''.join(b[m[i]] if i in m else '-' for i in pos)})
r = {'human_id': human.id, 'donkey_id': donkey.id, 'human_length': len(a), 'donkey_length': len(b),
     'paired_residues': n, 'identical_residues': ident,
     'identity_paired_percent': round(100 * ident / n, 2),
     'human_paired_coverage_percent': round(100 * n / len(a), 2),
     'donkey_paired_coverage_percent': round(100 * n / len(b), 2),
     'donkey_unaligned_segments_ge5': ins,
     'human_unaligned_segments_ge5': hum_ins,
     'human_sha256': hashlib.sha256(a.encode()).hexdigest(),
     'donkey_sha256': hashlib.sha256(b.encode()).hexdigest(),
     'human_features_mapped': features}
(here / 'results.json').write_text(json.dumps(r, indent=2) + '\n')
(here / 'alignment.txt').write_text(str(al))
lines = [f'# {gene}: donkey-human sequence comparison', '',
         f"The donkey sequence {donkey.id} ({len(b)} residues) aligns to human {human.id} ({len(a)} residues) with {r['identity_paired_percent']}% identity across {n} paired residues. Paired coverage is {r['human_paired_coverage_percent']}% of the human sequence and {r['donkey_paired_coverage_percent']}% of the donkey sequence.",
         '',
         'Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `' + str(hpath.relative_to(root)) + '`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python ' + str(here.relative_to(root) / 'compare_pair.py') + (' ' + str(hpath.relative_to(root)) if len(sys.argv) > 1 else '') + '`.',
         '',
         'This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.',
         '', '## Donkey segments not paired with human (>=5 residues)', '']
lines += [f'- donkey residues {s}-{e}.' for s, e in ins] or ['- none.']
lines += ['', '## Human segments not paired with donkey (>=5 residues)', '']
lines += [f'- human residues {s}-{e}.' for s, e in hum_ins] or ['- none.']
lines += ['', '## Mapped human site/motif features', '']
lines += [f"- {x['type']} ({x['note']}): human {x['human_positions_1based']} {x['human_residues']} -> donkey {x['donkey_positions_1based']} {x['donkey_residues']}." for x in features] or ['- none annotated in the human record.']
(here / 'RESULTS.md').write_text('\n'.join(lines) + '\n')
print(gene, r['identity_paired_percent'], r['human_paired_coverage_percent'], r['donkey_paired_coverage_percent'], ins)
