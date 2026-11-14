"""Check family assertion preservation, quotes, tree scope and frozen consultation inputs."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(text):
    return ' '.join(re.sub(r'(?m)^(?:CC|FT|DE)\s+', '', text).split())


def quotes(value):
    if isinstance(value, dict):
        if 'reference_id' in value and 'supporting_text' in value:
            yield value
        for item in value.values():
            yield from quotes(item)
    elif isinstance(value, list):
        for item in value:
            yield from quotes(item)


def assertion(row):
    return {k: v for k, v in row.items() if k not in {'assessment', 'assessment_reason', 'supported_by'}}


def main():
    before = json.loads((HERE / 'baseline.json').read_text())
    failures = []
    for path, digest in before['protected_sources'].items():
        if sha(ROOT / path) != digest:
            failures.append(f'Protected source changed: {path}')
    trees = json.loads((HERE / 'tree-snapshot.json').read_text())
    for family, tree in trees.items():
        if sha(ROOT / tree['source']) != tree['sha256']:
            failures.append(f'Frozen reference tree changed: {family}')
    input_manifests = {}
    for scope in ['ecoli-consultation', 'psepk-consultation', 'neisseria-consultation', 'literature-consultation']:
        path = AUDIT / scope / 'handoff.json'
        manifest = json.loads(path.read_text())
        input_manifests[str(path.relative_to(ROOT))] = sha(path)
        for owned, digest in manifest.get('files', manifest.get('files_sha256', {})).items():
            if isinstance(digest, dict):
                digest = digest['sha256']
            if sha(ROOT / owned) != digest:
                failures.append(f'Frozen consultation file changed: {owned}')
    ledger = {}
    sources = {}
    count = 0
    quote_count = 0
    for path, frozen in before['families'].items():
        old = frozen['document']
        current = yaml.safe_load((ROOT / path).read_text())
        rows = old['node_assessments']
        new = current['node_assessments']
        count += len(rows)
        if [assertion(x) for x in rows] != [assertion(x) for x in new]:
            failures.append(f'Ordered PAINT payload changed: {path}')
        if [x['assessment'] for x in rows] != [x['assessment'] for x in new]:
            failures.append(f'Original node judgment changed: {path}')
        original_refs = {(x['id'], x['title']) for x in old['references']}
        current_refs = {(x['id'], x['title']) for x in current['references']}
        if not original_refs <= current_refs:
            failures.append(f'Original reference identity lost: {path}')
        ledger[path] = []
        for left, right in zip(old['term_assessments'], current['term_assessments'], strict=True):
            if left['assessed_term'] != right['assessed_term']:
                failures.append(f'Original assessed-term identity/order changed: {path}')
            if left['scope'] != right['scope']:
                ledger[path].append({'term': left['assessed_term']['id'], 'before': left['scope'], 'after': right['scope'], 'reason': right['scope_reason']})
        for entry in quotes(current):
            ref = entry['reference_id']
            if ref.startswith('file:'):
                source = ROOT / ref[5:]
                if not source.exists():
                    source = ROOT / 'genes' / ref[5:]
            elif ref.startswith('PMID:'):
                source = ROOT / 'publications' / f"{ref.replace(':', '_')}.md"
            else:
                failures.append(f'Unverified quote source: {ref}')
                continue
            sources[str(source.relative_to(ROOT))] = sha(source)
            if norm(entry['supporting_text']) not in norm(source.read_text()):
                failures.append(f'Quote mismatch: {path}/{ref}')
            quote_count += 1
    # These exact taxon/branch observations independently constrain the scope narrative.
    observations = [
        ('PTHR33529', 'Q9RVF4', 'PTHR33529:SF2'),
        ('PTHR36504', 'Q9RS08', 'PTHR36504:SF1'),
        ('PTHR45772', 'Q9RSJ0', 'PTHR45772:SF10'),
        ('PTHR45772', 'Q9X0E4', 'PTHR45772:SF10'),
    ]
    for family, acc, subfamily in observations:
        matches = [x for x in trees[family]['leaves'].values() if x['uniprot'] == acc]
        if len(matches) != 1 or matches[0]['subfamily'] != subfamily:
            failures.append(f'Expected non-LPS-context classification not reproduced: {acc}')
    e = trees['PTHR38098']
    neis = next(k for k, v in e['leaves'].items() if v['uniprot'] == 'Q9K0A7')
    if neis not in e['under']['PTN002866256'] or neis in e['under']['PTN002211326']:
        failures.append('Neisseria LptE root-versus-gamma distinction not reproduced')
    # A raw record establishes membership, not activity or a native mutant phenotype.
    for org, gene, family in [('NEIMH', 'lptD', 'PTHR30189'), ('NEIMB', 'lptH', 'PTHR36504'), ('NEIMB', 'lptE', 'PTHR38098')]:
        raw = ROOT / f'genes/{org}/{gene}/{gene}-uniprot.txt'
        if f'PANTHER; {family}:SF1;' not in raw.read_text():
            failures.append(f'Neisseria classification missing: {raw}')
    direct = json.loads((HERE / 'direct-membership.json').read_text())
    for item in direct['checks']:
        source = ROOT / item['source']
        if sha(source) != item['sha256']:
            failures.append(f"Membership source changed: {source}")
        if not item['classification_lines'] or any(line not in source.read_text() for line in item['classification_lines']):
            failures.append(f"Membership line missing: {item['accession']}")
        sources[item['source']] = sha(source)
    result = {
        'status': 'FAIL' if failures else 'PASS',
        'original_ordered_paint_assertions': count,
        'node_judgment_changes': 0,
        'scope_changes': sum(map(len, ledger.values())),
        'preserved_protected_sources': len(before['protected_sources']),
        'unchanged_reference_tree_caches': len(trees),
        'quotes_checked': quote_count,
        'verified_input_manifests': input_manifests,
        'source_sha256': sources,
        'verified_neisseria_members': 3,
        'direct_membership_checks': len(direct['checks']),
        'independent_tree_scope_observations': 5,
        'failures': failures,
    }
    (HERE / 'scope-ledger.json').write_text(json.dumps(ledger, indent=2) + '\n')
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in {'source_sha256', 'verified_input_manifests'}}, indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
