"""Map input protein positions by global BLOSUM62 alignment; no functional inference.

Inputs are FASTA files. The first query record is compared with every target record.
Coordinates are one-based. A second equally optimal alignment is reported explicitly.
Scores use gap-open -10 and gap-extension -0.5. No gene identifiers or results are coded.
"""
import argparse, hashlib, json
from pathlib import Path
from itertools import islice
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import Bio

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('query', type=Path)
    ap.add_argument('targets', type=Path)
    ap.add_argument('--positions', default='')
    ap.add_argument('--output', required=True, type=Path)
    args = ap.parse_args()
    queries = list(SeqIO.parse(args.query, 'fasta'))
    assert len(queries) == 1, 'Exactly one query is required'
    query = queries[0]
    positions = [int(x) for x in args.positions.split(',') if x]
    assert all(1 <= p <= len(query) for p in positions)
    aligner = Align.PairwiseAligner(mode='global')
    aligner.substitution_matrix = substitution_matrices.load('BLOSUM62')
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    rows = []
    for target in SeqIO.parse(args.targets, 'fasta'):
        alignments = list(islice(aligner.align(str(query.seq), str(target.seq)), 2))
        assert alignments
        a = alignments[0]
        qi, ti = a.indices
        pairs = [(int(i), int(j)) for i, j in zip(qi, ti) if i >= 0 and j >= 0]
        matches = sum(query.seq[i] == target.seq[j] for i, j in pairs)
        mapping = dict(pairs)
        selected = []
        for p in positions:
            j = mapping.get(p-1)
            alternatives = []
            for alt in alignments:
                m = {int(i): int(j) for i,j in zip(*alt.indices) if i >= 0 and j >= 0}
                alternatives.append(m.get(p-1))
            selected.append({'query_position': p, 'query_residue': query.seq[p-1],
                             'target_position': None if j is None else j+1,
                             'target_residue': None if j is None else target.seq[j],
                             'consistent_in_first_two': len(set(alternatives)) == 1})
        rows.append({'target': target.id, 'description': target.description,
                     'length': len(target), 'score': a.score,
                     'matches': matches, 'aligned_pairs': len(pairs),
                     'query_length': len(query),
                     'identity_over_paired_positions': matches/len(pairs) if pairs else 0,
                     'query_coverage': len(pairs)/len(query),
                     'target_coverage': len(pairs)/len(target),
                     'multiple_optimal': len(alignments)>1,
                     'mapped_positions': selected,
                     'alignment': str(a)})
    assert rows, 'No target proteins'
    rows.sort(key=lambda r: (-r['score'], r['target']))
    result = {'biopython': Bio.__version__, 'query': query.id,
              'input_sha256': {str(p):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in [args.query,args.targets]},
              'parameters': {'matrix':'BLOSUM62','gap_open':-10,'gap_extend':-0.5,
                             'mode':'global','positions':positions},
              'interpretation_limit':'Sequence compatibility only; no assay identity or functional equivalence follows.',
              'display_convention':'In Biopython alignment strings, target is the input query and query is the input target.',
              'targets':rows}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
if __name__ == '__main__':
    main()
