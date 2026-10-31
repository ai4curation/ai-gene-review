"""Reproduce ELANE database provenance with Python 3.9+ and no network."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, importlib.util, json, sys, tempfile, zipfile

def require(value, message):
    if not value:
        raise ValueError(message)

def load(path):
    return json.loads(path.read_text())

def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    metadata = load(base / 'archive.json')
    archive = args.archive or base / metadata['archive']
    require(hashlib.sha256(archive.read_bytes()).hexdigest() == metadata['sha256'], 'Archive hash mismatch')
    with tempfile.TemporaryDirectory(prefix='elane-evidence-') as temporary:
        directory = Path(temporary)
        with zipfile.ZipFile(archive) as z:
            require(len(z.namelist()) == len(set(z.namelist())), 'Duplicate archive paths')
            for name in z.namelist():
                path = PurePosixPath(name)
                require(not path.is_absolute() and '..' not in path.parts, 'Unsafe member path')
                require((z.getinfo(name).external_attr >> 16) & 0o170000 != 0o120000, 'Symlink archive member')
            manifest_data = z.read('manifest.json')
            require(hashlib.sha256(manifest_data).hexdigest() == metadata['member_manifest_sha256'], 'Member manifest hash mismatch')
            manifest = json.loads(manifest_data)
            require(set(z.namelist()) == {'manifest.json'} | {r['path'] for r in manifest['files']}, 'Unlisted archive member')
            for record in manifest['files']:
                data = z.read(record['path'])
                require(len(data) == record['bytes'] and hashlib.sha256(data).hexdigest() == record['sha256'], 'Member hash mismatch')
            z.extractall(directory)
        root = directory / 'ELANE-database-root-v1'
        peer = directory / 'ELANE-database-peer-brca-v1'
        sys.path.insert(0, str(root))
        database = module(root / 'replay_portable.py', 'database').run()
        require(database == load(root / 'database-replay-v2.json'), 'Database reconstruction drift')
        assessment = module(peer / 'derive.py', 'assessment').run()
        require(assessment == load(peer / 'derived.json'), 'Donor/rule reconstruction drift')
        contexts = load(directory / 'source-contexts/QuickGO-rows.json')
        require(len(contexts) == 104, 'Raw context count')
        print(json.dumps({'status': 'PASS', 'authenticated_members': len(manifest['files']),
                          'source_objects': database['source_objects'], 'raw_contexts': len(contexts),
                          'definitions': database['source_definitions'], 'typed_ancestry': database['typed_ancestry_records'],
                          'paint_rows': database['paint_joins'], 'canonical_sequence_length': database['canonical_sequence_length'],
                          'Reactome_rows': database['Reactome_source_rows'],
                          'unresolved_Reactome_rows': database['unresolved_Reactome_rows'],
                          'donor_queries': len(assessment['donors']),
                          'ARBA_rule_matches': {x['id']: x['matched_sets'] for x in assessment['rules']},
                          'scientific_verdicts_generated': 0}, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
