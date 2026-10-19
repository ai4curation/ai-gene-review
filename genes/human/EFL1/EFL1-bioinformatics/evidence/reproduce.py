"""Verify bundled raw inputs and independently regenerate EFL1 evidence projections."""
from pathlib import Path
import argparse
import hashlib
import json
import tempfile
import zipfile
from derive import derive

def require(condition, message):
    if not condition:
        raise ValueError(message)

def read_json(path):
    return json.loads(path.read_text())

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional new JSON output; never overwrites bundled evidence')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    manifest = read_json(here / 'source-manifest.json')
    archive = here / manifest['archive']['path']
    require(archive.is_file(), 'Missing inputs.zip; restore the published archive before replay')
    require(hashlib.sha256(archive.read_bytes()).hexdigest() == manifest['archive']['sha256'], 'Archive SHA256 mismatch')
    with tempfile.TemporaryDirectory(prefix='efl1-evidence-') as td:
        root = Path(td)
        with zipfile.ZipFile(archive) as z:
            require(set(z.namelist()) == {r['path'] for r in manifest['inputs']}, 'Archive member set mismatch')
            for record in manifest['inputs']:
                name = record['path']
                require(not Path(name).is_absolute() and '..' not in Path(name).parts, 'Unsafe archive path')
                data = z.read(name)
                require(len(data) == record['bytes'], 'Input length mismatch: ' + name)
                require(hashlib.sha256(data).hexdigest() == record['sha256'], 'Input SHA256 mismatch: ' + name)
                dest = root / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(data)
        official = read_json(root / 'UniProt-Q7Z2Z2.json')
        result = derive(root / 'raw', read_json(root / 'source-objects.json'), official)
        require(result == read_json(here / 'results.json'), 'Raw-derived result differs from published result')
        canonical = official['sequence']['value']
        features = {f['featureId']: f for f in official['features'] if 'featureId' in f}
        feature = features['VSP_030152']
        start = feature['location']['start']['value']
        end = feature['location']['end']['value']
        require(not feature.get('alternativeSequence', {}).get('alternativeSequences'), 'Unexpected replacement sequence')
        shorter = canonical[:start-1] + canonical[end:]
        products = []
        for accession, sequence in [('Q7Z2Z2-1', canonical), ('Q7Z2Z2-2', shorter)]:
            fasta = (root / 'raw' / (accession + '.fasta')).read_text().splitlines()
            observed = ''.join(line.strip() for line in fasta if not line.startswith('>'))
            require(observed == sequence, 'Official product reconstruction mismatch: ' + accession)
            products.append({'id': accession, 'length': len(sequence), 'sha256': hashlib.sha256(sequence.encode()).hexdigest()})
        ancestors = read_json(root / 'raw/GO-large-subunit-binding-ancestors.json')['results'][0]
        require('GO:0043022' in ancestors['ancestors'], 'Large-subunit binding ancestry')
        if args.output:
            require(args.output.resolve() != (here / 'results.json').resolve(), 'Do not overwrite published results')
            require(not args.output.exists(), 'Output exists; choose a new path')
            args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
        print(json.dumps({'status':'PASS', 'inputs':len(manifest['inputs']), 'tree_nodes':result['target']['tree_node_count'], 'IBA':len(result['iba']), 'donor_joins':len(result['donors']), 'ARBA_rules':len(result['rules']), 'current_pair_records':len(result['interactions']['pairs']), 'products':products, 'ordinary_gene_validation':False}))

if __name__ == '__main__':
    main()
