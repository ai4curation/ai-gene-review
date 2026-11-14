"""Integrated source payload and consultation preservation, including one additive supersession."""

import hashlib
import json
import subprocess
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != 'review'}


def main():
    baseline = json.loads((HERE / 'baseline.json').read_text())
    originals = {path: row['document'] for path, row in baseline['reviews'].items()}
    protected = dict(baseline['protected_files_sha256'])
    for seed in sorted((HERE / 'new-member-seeds').glob('*.json')):
        row = json.loads(seed.read_text())
        path = f'genes/{row["organism"]}/{row["gene"]}/{row["gene"]}-ai-review.yaml'
        assert path not in originals, path
        originals[path] = row['review']
        for source, sha in row['files_sha256'].items():
            if source.endswith(('-uniprot.txt', '-goa.tsv')):
                protected[source] = sha
    unchanged_cher = []
    for source in sorted((ROOT / 'genes/ECOLI/cheR').glob('*')):
        if not source.is_file():
            continue
        relative = str(source.relative_to(ROOT))
        tracked = subprocess.run(['git', 'cat-file', '-e', baseline['head'] + ':' + relative],
                                 cwd=ROOT, capture_output=True).returncode == 0
        if tracked:
            assert source.read_bytes() == subprocess.check_output(
                ['git', 'show', baseline['head'] + ':' + relative], cwd=ROOT), relative
            unchanged_cher.append(relative)
    cher_path = 'genes/ECOLI/cheR/cheR-ai-review.yaml'
    assert cher_path in unchanged_cher
    originals[cher_path] = yaml.safe_load((ROOT / cher_path).read_text())
    rows = []
    total_original = total_final = total_old_new = total_added = 0
    for path, prior in originals.items():
        current = yaml.safe_load((ROOT / path).read_text())
        assert (current['id'], current['taxon'], current['gene_symbol']) == (
            prior['id'], prior['taxon'], prior['gene_symbol']), path
        assert current['status'] == 'COMPLETE', path
        old = prior.get('existing_annotations', [])
        new = current.get('existing_annotations', [])
        assert len(new) >= len(old), path
        assert [payload(row) for row in new[:len(old)]] == [payload(row) for row in old], path
        old_new = [i for i, row in enumerate(old) if row['review']['action'] == 'NEW']
        assert all(new[i]['review']['action'] == 'NEW' for i in old_new), path
        additions = new[len(old):]
        assert all(row['review']['action'] == 'NEW' for row in additions), path
        if additions:
            assert path == 'genes/DEHMC/cbdbA481/cbdbA481-ai-review.yaml'
            assert len(additions) == 1 and additions[0]['term']['id'] == 'GO:0008172'
            assert additions[0]['evidence_type'] == 'IDA'
        assert all(row['review']['action'] != 'PENDING' for row in new), path
        rows.append({'path': path, 'original_rows': len(old), 'final_rows': len(new),
                     'historical_NEW': len(old_new), 'added_NEW': len(additions),
                     'ordered_source_payloads_and_qualifiers_unchanged': True})
        total_original += len(old)
        total_final += len(new)
        total_old_new += len(old_new)
        total_added += len(additions)
    for path, sha in protected.items():
        assert digest(ROOT / path) == sha, path
    assert not subprocess.check_output(['git', 'diff', '--name-only', '--', 'history'], cwd=ROOT, text=True).strip(), 'Existing history records changed'
    supersession = json.loads((HERE / 'psepk-zinc-followup/supersession.json').read_text())
    replaced = supersession['supersedes_files']
    assert len(replaced) == 3 and supersession['source_payloads_order_qualifiers_lifecycle_core_evidence_exact']
    inventory = json.loads((HERE / 'release-inventory.json').read_text())
    releases = []
    all_inputs = dict(protected)
    for name, expected in inventory.items():
        path = HERE / name / 'handoff.json'
        assert digest(path) == expected, path
        handoff = json.loads(path.read_text())
        for filename, sha in handoff['files'].items():
            effective_sha = sha
            if filename in replaced and sha == replaced[filename]['old_sha256']:
                effective_sha = replaced[filename]['new_sha256']
            assert digest(ROOT / filename) == effective_sha, (name, filename)
            if filename in all_inputs:
                assert all_inputs[filename] == effective_sha, filename
            all_inputs[filename] = effective_sha
        all_inputs[str(path.relative_to(ROOT))] = expected
        releases.append({'directory': name, 'files': len(handoff['files']), 'manifest_sha256': expected})
    for path in unchanged_cher:
        all_inputs[path] = digest(ROOT / path)
    for path in originals:
        all_inputs[path] = digest(ROOT / path)
    output = {'status': 'PASS', 'reviews': len(originals), 'original_rows': total_original,
              'final_rows': total_final, 'historical_NEW': total_old_new, 'added_NEW': total_added,
              'retired_or_deleted_rows': 0, 'protected_sources': len(protected),
              'unchanged_CheR_main_files': unchanged_cher, 'member_preservation': rows,
              'releases': releases, 'explicit_supersession': supersession,
              'input_sha256': all_inputs,
              'limits': 'Checks exact payloads, source bytes and frozen consultation outputs. It does not replace their biological review or full-corpus validation. Original external full-text acquisitions with bounded durable excerpts retain their provenance and explicit access limits.'}
    (HERE / 'closure-results.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({key: output[key] for key in ['status', 'reviews', 'original_rows', 'final_rows',
                                                  'historical_NEW', 'added_NEW', 'protected_sources']}))


if __name__ == '__main__':
    main()
