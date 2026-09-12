"""Rebuild the fly census and functional cohort from frozen inputs (no network).

Run with `uv run python projects/PROTNLM_EVALUATION/fly-benchmark/summarize.py`.
The shared census parser preserves original prediction strings. Identity and GO
comparisons use ordinary UniProt records, never prediction-generated gene names.
An exact GO overlap is descriptive metadata, not biological validation.
"""
import csv
import gzip
import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
spec = importlib.util.spec_from_file_location('census', ROOT.parent/'mammal-benchmark/summarize.py')
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)

def read_jsonl(name):
    with gzip.open(ROOT/name, 'rt') as f:
        return [json.loads(line) for line in f]

def write_csv(name, rows):
    with (ROOT/name).open('w') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

def main():
    with (ROOT/'accessions.tsv').open() as f:
        metadata = list(csv.DictReader(f, delimiter='\t'))
    payloads = read_jsonl('predictions.jsonl.gz')
    uniprot = {x['primaryAccession']:x for x in read_jsonl('uniprot.jsonl.gz')}
    inventory, statements, species = census.summarize(metadata, payloads)
    provenance = []
    for payload in payloads:
        claims = []
        for ref in payload.get('uniProtKBCrossReferences', []):
            if ref['database'] == 'GO':
                props = {p['key']:p['value'] for p in ref.get('properties', [])}
                claims.append(('GO', ref['id'], props.get('GoTerm', ''), ref.get('evidences', [])))
        for comment in payload.get('comments', []):
            if comment.get('commentType') == 'FUNCTION':
                for text in comment.get('texts', []):
                    claims.append(('function', '', text['value'], text.get('evidences', [])))
        for kind, term, text, evidences in claims:
            for i, evidence in enumerate(evidences or [{}], 1):
                props = {p['key']:p['value'] for p in evidence.get('properties', [])}
                provenance.append({'accession':payload['primaryAccession'], 'type':kind,
                                   'id':term, 'text':text, 'evidence_index':i,
                                   'model_score':props.get('model_score', ''),
                                   'phmmer_accession':props.get('phmmer_accession', ''),
                                   'tmalign_accession':props.get('tmalign_accession', ''),
                                   'evidence_json':json.dumps(evidence, sort_keys=True)})
    assert {x['Entry'] for x in metadata} == set(uniprot)
    existing = {}
    for p in (REPO/'genes/DROME').glob('*/*-ai-review.yaml'):
        # Only index the literal top-level id; no review text is biological evidence.
        for line in p.read_text().splitlines():
            if line.startswith('id: '):
                existing[line[4:].strip().strip('\"\'')] = str(p.relative_to(REPO))
                break
    with gzip.open(ROOT/'flybase-identifiers.tsv.gz', 'rt') as f:
        lines = [line for line in f if not line.startswith('##') and line.strip()]
    flybase = {}
    for line in lines:
        symbol, organism, primary, secondary, annotation, old_annotations = line.rstrip('\n').split('\t')
        if organism != 'Dmel':
            continue
        record = {'symbol':symbol, 'primary':primary, 'annotation':annotation}
        for identifier in [primary] + secondary.split(','):
            if identifier:
                flybase[identifier] = record
    grouped = defaultdict(list)
    for s in statements:
        grouped[s['accession']].append(s)
    fasta = []
    for row in inventory:
        u = uniprot[row['accession']]
        genes = u.get('genes', [])
        symbol = next((g['geneName']['value'] for g in genes if 'geneName' in g), '')
        loci = [v['value'] for g in genes for v in g.get('orderedLocusNames', [])]
        if not symbol:
            symbol = next((v for v in loci if v.startswith('CG')), '')
        fb = sorted({r['id'] for r in u.get('uniProtKBCrossReferences', []) if r['database']=='FlyBase'})
        matches = {flybase[f]['primary']:flybase[f] for f in fb if f in flybase}
        if len(matches) != 1:
            raise ValueError(f"Expected one FlyBase gene for {row['accession']}, got {matches}")
        resolved = next(iter(matches.values()))
        uniprot_symbol = symbol
        symbol = resolved['symbol']
        gos = [r for r in u.get('uniProtKBCrossReferences', []) if r['database']=='GO']
        go_ids = {r['id'] for r in gos}
        terms = [s for s in grouped[row['accession']] if s['type']=='GO']
        seq = u['sequence']['value']
        row.update(gene_symbol=symbol, uniprot_gene_symbol=uniprot_symbol, flybase_ids=resolved['primary'], uniprot_flybase_ids=';'.join(fb), annotation_symbol=resolved['annotation'], locus_names=';'.join(loci),
                   uniprot_entry_type=u['entryType'], current_length=len(seq),
                   sequence_sha256=hashlib.sha256(seq.encode()).hexdigest(),
                   current_go_count=len(gos), exact_go_overlap=sum(t['id'] in go_ids for t in terms),
                   existing_review=existing.get(row['accession'], ''),
                   cohort='FUNCTIONAL' if row['go_count'] or row['function_count'] else 'NAME_OR_OTHER_ONLY')
        fasta.append('>'+row['accession']+' '+symbol+'\n'+'\n'.join(seq[i:i+60] for i in range(0,len(seq),60))+'\n')
    functional = [r for r in inventory if r['cohort']=='FUNCTIONAL']
    ids = {r['accession'] for r in functional}
    functional_statements = [s for s in statements if s['accession'] in ids and s['type'] in {'GO','function'}]
    for name, rows in [('inventory.csv',inventory),('prediction-statements.csv',statements),
                       ('species-counts.csv',species),('claim-provenance.csv',provenance),('functional-cohort.csv',functional),
                       ('functional-predictions.csv',functional_statements),
                       ('location-keyword-tier.csv',[r for r in inventory if not r['name_only'] and r['cohort'] != 'FUNCTIONAL'])]:
        write_csv(name,rows)
    (ROOT/'sequences.fasta').write_text(''.join(fasta))
    groups = defaultdict(list)
    for r in inventory:
        groups[r['flybase_ids'] or r['gene_symbol'] or r['accession']].append(r['accession'])
    summary = dict(species[0],functional_records=len(functional),
                   functional_gene_groups=len({r['flybase_ids'] or r['gene_symbol'] or r['accession'] for r in functional}),
                   records_with_existing_review=sum(bool(r['existing_review']) for r in inventory),
                   functional_records_with_existing_review=sum(bool(r['existing_review']) for r in functional),
                   entry_types=dict(Counter(r['uniprot_entry_type'] for r in inventory)),
                   shared_gene_groups={k:v for k,v in groups.items() if len(v)>1},
                   gene_group_caveat='UniProt FlyBase cross-references resolve to primary Dmel gene IDs and current symbols in the frozen FlyBase identifier table. This does not verify the protein isoform sequence against FlyBase.')
    (ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    for r in functional:
        print(r['accession'],r['gene_symbol'],r['flybase_ids'],r['current_length'],'GO',r['go_count'],'text',r['function_count'])
        for s in grouped[r['accession']]:
            if s['type'] in {'GO','function'}:
                print(' ',s['id'],s['text'])

if __name__=='__main__':
    main()
