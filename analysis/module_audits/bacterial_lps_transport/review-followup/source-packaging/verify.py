"""Verify durable source replacements; optionally recheck unchanged local originals."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(originals=False):
    mapping = json.loads((HERE / 'replacement-map.json').read_text())
    assert len(mapping['replacements']) == 9
    byte_equal = excerpts = 0
    for old, item in mapping['replacements'].items():
        target = ROOT / item['replacement_path']
        assert digest(target) == item['replacement_sha256'], target
        if item['mode'] == 'BYTE_IDENTICAL':
            assert digest(target) == item['original_sha256']
            byte_equal += 1
        else:
            excerpts += 1
            assert item['mode'] == 'SCOPED_EXCERPT' and not item['full_source_reconstructable']
            assert ' '.join(item['checked_quote'].split()) in ' '.join(target.read_text().split())
        for path, expected in item.get('additional_scoped_evidence', {}).items():
            assert digest(ROOT / path) == expected
        if originals:
            source = ROOT / old
            assert digest(source) == item['original_sha256'], old
            if item['mode'] == 'SCOPED_EXCERPT':
                text = ' '.join(source.read_text().split())
                assert all(token in text for token in item.get('additional_factual_tokens_checked', []))
                assert ' '.join(item['checked_quote'].split()) in text
                for path in item.get('additional_scoped_evidence', {}):
                    for line in (ROOT / path).read_text().splitlines():
                        if line.startswith('> '):
                            assert ' '.join(line[2:].split()) in text
    assert (byte_equal, excerpts) == (5, 4)
    assert (HERE / 'index-removal-paths.txt').read_text().splitlines() == sorted(mapping['replacements'])
    print(json.dumps({'status': 'PASS', 'byte_identical_snapshots': byte_equal, 'scoped_excerpts': excerpts,
                      'original_bytes_rechecked': originals, 'full_articles_reconstructable': False}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--originals', action='store_true', help='Optional local custody check; not needed in a clean checkout.')
    main(parser.parse_args().originals)
