"""Verify immutable consultation inputs and actual supporting quotations; no fetching."""

import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.validation.supporting_text import build_supporting_text_validator
from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
AUDIT = HERE.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quotations(value, reference=None):
    if isinstance(value, dict):
        own = value.get('id', '')
        if own.startswith(('PMID:', 'file:', 'DOI:', 'UniProtKB:')):
            reference = own
        source = value.get('reference_id') or value.get('source_id') or reference
        if value.get('supporting_text'):
            yield source, value['supporting_text']
        for key, child in value.items():
            if key != 'supporting_text':
                yield from quotations(child, source)
    elif isinstance(value, list):
        for child in value:
            yield from quotations(child, reference)


def main():
    hashes = {}
    manifest_counts = {}
    for name in ['ecoli-consultation', 'psepk-consultation', 'aciad-consultation',
                 'family-consultation', 'cross-lineage-consultation', 'flaj1-lola-consultation',
                 'module-consultation']:
        path = AUDIT / name / 'handoff.json'
        data = json.loads(path.read_text())
        owned = data.get('files', data.get('files_sha256', {}))
        protected = data.get('protected_sources_sha256', {})
        for rel, expected in (owned | protected).items():
            actual = sha(ROOT / rel)
            assert actual == expected, (name, rel, expected, actual)
            hashes[rel] = actual
        hashes[str(path.relative_to(ROOT))] = sha(path)
        manifest_counts[name] = dict(owned=len(owned), protected=len(protected))
    members = json.loads((HERE / 'member-closure.json').read_text())
    module_path = ROOT / 'modules/bacterial_lol_lipoprotein_trafficking.yaml'
    paths = [module_path, HERE / 'boundary-evidence.yaml'] + [ROOT / record['path'] for record in members.values()]
    validator, _ = build_supporting_text_validator(ROOT / 'publications')
    results, errors = [], []
    for path in paths:
        hashes[str(path.relative_to(ROOT))] = sha(path)
        seen = set()
        for ref, quote in quotations(yaml.safe_load(path.read_text())):
            if (ref, quote) in seen:
                continue
            seen.add((ref, quote))
            assert ref, (path, quote)
            # Use the exact repository helper/config, including local file and wrapped UniProt handling.
            result = validator.validate(quote, ref, path=str(path))
            entry = dict(path=str(path.relative_to(ROOT)), reference=ref,
                         quotation=quote, valid=result.is_valid, skipped=result.skipped,
                         message=result.message)
            if ref.startswith('file:'):
                local = resolve_local_source(ref, ROOT)
                entry.update(valid=bool(local and quote_matches(quote, local)), skipped=False,
                             message='Repository local-source quote matcher (no baseline exemption).')
            results.append(entry)
            if not entry['valid'] or entry['skipped']:
                errors.append(entry)
            if ref.startswith('PMID:'):
                source = ROOT / 'publications' / (ref.replace(':', '_') + '.md')
                assert source.exists(), source
                hashes[str(source.relative_to(ROOT))] = sha(source)
            elif ref.startswith('file:'):
                relative = ref.removeprefix('file:')
                options = [ROOT / relative, ROOT / 'genes' / relative, path.parent / relative]
                source = next((p for p in options if p.is_file()), None)
                assert source, ref
                hashes[str(source.relative_to(ROOT))] = sha(source)
    # Exact identity mapping / physical-role classification inputs, independent of the module selector.
    extra = list((AUDIT / 'identity').glob('*.json'))
    extra += [AUDIT / 'family-consultation/variant-identities.json',
              AUDIT / 'aciad-consultation/identity-mapping.yaml',
              AUDIT / 'literature-curation.yaml',
              ROOT / 'src/ai_gene_review/module_logic.py',
              ROOT / '.cache/module-audit-logs/lol-20261107/ecoli-consultation/28416660-full.txt',
              ROOT / '.cache/module-audit-logs/lol-20261107/ecoli-consultation/28416660-response.html']
    for path in extra:
        hashes[str(path.relative_to(ROOT))] = sha(path)
    report = dict(status='PASS' if not errors else 'FAIL', manifests=manifest_counts,
                  member_count=len(members), quote_count=len(results), errors=errors,
                  quotations=results, input_sha256=hashes)
    (HERE / 'source-closure.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(status=report['status'], member_count=len(members),
                         quote_count=len(results), input_count=len(hashes), errors=len(errors))))
    assert not errors, errors[:3]


if __name__ == '__main__':
    main()
