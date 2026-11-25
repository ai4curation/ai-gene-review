"""Create a new immutable additive handoff after successful focused checks."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PACK = HERE.parent / 'source-packaging'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    target = HERE / 'handoff.json'
    assert not target.exists(), 'Never overwrite a frozen handoff'
    closure = json.loads((HERE / 'closure.json').read_text())
    checks = json.loads((HERE / 'checks.json').read_text())
    assert closure['status'] == checks['status'] == 'PASS'
    for path, expected in closure['inputs_sha256'].items():
        assert sha(ROOT / path) == expected, path
    for path, expected in json.loads((HERE / 'historical-artifacts.json').read_text()).items():
        assert sha(ROOT / path) == expected, path
    replacements = json.loads((PACK / 'replacement-map.json').read_text())['replacements']
    for path, item in replacements.items():
        assert sha(ROOT / path) == item['original_sha256'], path
        subprocess.run(['git', 'ls-files', '--error-unmatch', path], cwd=ROOT, check=True, capture_output=True)
    files = {str(p.relative_to(ROOT)): sha(p) for directory in (HERE, PACK)
             for p in sorted(directory.rglob('*')) if p.is_file() and '__pycache__' not in p.parts}
    for path in ('modules/bacterial_lps_transport.yaml', 'pages/modules/bacterial_lps_transport.html',
                 'history/modules/bacterial_lps_transport/2026-11-07T115529Z-codex-586af7.yaml'):
        files[path] = sha(ROOT / path)
    result = {
        'status': 'FROZEN', 'ownership_released': True,
        'scope': 'Additive durable-source resolution, one terminal-profile coverage note, module history/render and current capacity/closure. No gene/family/science action changes.',
        'files': dict(sorted(files.items())), 'file_count': len(files),
        'source_dependencies': closure['inputs_sha256'],
        'module_supersession': str((HERE / 'module-supersession.json').relative_to(ROOT)),
        'replacement_map': str((PACK / 'replacement-map.json').relative_to(ROOT)),
        'index_removals_authorized_to_parent_only': list(sorted(replacements)),
        'original_cache_custody': {p: r['original_sha256'] for p, r in replacements.items()},
        'original_cache_required_for_current_checker': False,
        'historical_receipts_and_checkers_unchanged': True,
        'capacity_and_preservation': checks,
        'limits': [
            'Four scoped excerpts replace complete article verification dependencies; they cannot reconstruct full original texts. Broader historical full-text conclusions remain provenance-attested.',
            'A standalone PANTHER data licence was not verified; attribution and exact compact-tree source provenance are preserved without inventing a CC licence.',
            'The two existing unresolved family-function advisories remain; exact role/substrate/partner gates are necessary.',
            'No full-corpus validation or Git index operation was performed. Parent must remove only listed cache paths from the index while retaining local originals.'
        ]}
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'handoff': str(target.relative_to(ROOT)), 'sha256': sha(target),
                      'file_count': len(files), 'source_dependencies': len(closure['inputs_sha256']),
                      'module_sha256': closure['module_sha256']}))


if __name__ == '__main__':
    main()
