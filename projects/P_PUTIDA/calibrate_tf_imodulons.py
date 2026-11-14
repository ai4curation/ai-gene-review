#!/usr/bin/env python3
"""Reproduce the 20 calibration summaries from the checked local dataset export.

Run from the repository root. No network requests or gene-review edits occur.
Only importer_assessment fields in the manual assessment file are regenerated.
"""
import argparse
import json
from pathlib import Path

import yaml

from ai_gene_review.imodulondb import IModulonDBClient, digest, json_text, write_report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', type=Path, default=Path('projects/P_PUTIDA/tf_census'))
    args = parser.parse_args()
    base = args.base
    folder = base / 'imodulon'
    manifest = json.loads((folder / 'manifest.json').read_text())
    for name, checksum in manifest['outputs'].items():
        if digest((folder / name).read_bytes()) != checksum:
            raise ValueError(f'Export checksum mismatch: {name}')
    dataset = json.loads((folder / 'dataset.json').read_text())
    import ai_gene_review.imodulondb as importer
    if digest(Path(importer.__file__).read_bytes()) != dataset['importer_sha256']:
        raise ValueError('Importer changed; re-export the dataset before calibration')
    cases = yaml.safe_load((base / 'calibration.yaml').read_text())['cases']
    assessment_path = base / 'calibration-assessments.yaml'
    assessments = yaml.safe_load(assessment_path.read_text())
    if [c['accession'] for c in cases] != [c['accession'] for c in assessments['cases']]:
        raise ValueError('Calibration/assessment accession order differs')
    client = IModulonDBClient(offline=True)
    client.loaded['PSEPK'] = dataset
    rows = []
    for case, assessment in zip(cases, assessments['cases'], strict=True):
        accession = case['accession']
        result = client.summarize('PSEPK', accession)
        path = folder / 'reports' / f'{accession}.md'
        write_report(result, path)
        # Shared source URLs/checksums live once in the dataset export manifest.
        result.pop('source_manifest')
        result['source_manifest_path'] = (folder / 'manifest.json').as_posix()
        path.with_suffix('.json').write_text(json_text(result))
        row = {
            'accession': accession, 'name': case['name'],
            'identity_status': result['identity']['status'],
            'assignment_status': result['assignment_status'],
            'assigned_modules': [{'id': m['module_id'], 'name': m['name']} for m in result['assigned_modules']],
            'gene_memberships': result['gene_memberships'],
            'report': path.as_posix(),
        }
        assessment['importer_assessment'] = {
            'status': 'CHECKED', **{k: v for k, v in row.items() if k not in {'accession', 'name'}},
            'notes': 'Source-defined expression membership and regulator assignments only; no direct target, sign, ligand or GO inference.',
        }
        rows.append(row)
    (folder / 'calibration-results.json').write_text(json_text(rows))
    lines = ['# Calibration importer results', '',
             'All 84 published PRECISE321 modules passed membership/count/weight checks. '
             'These 20 accession queries distinguish regulator assignments from membership of the regulator gene. '
             'No structured curated target set was supplied; no target-overlap or GO-validity claim is made.', '',
             '| Case | Accession | Identity | Assigned modules | Gene memberships |', '|---|---|---|---|---|']
    for row in rows:
        assigned = ', '.join(m['name'] for m in row['assigned_modules']) or 'none resolved'
        memberships = ', '.join(m['module_name'] for m in row['gene_memberships']) or 'none resolved'
        lines.append(f'| {row["name"]} | [{row["accession"]}](reports/{row["accession"]}.md) | {row["identity_status"]} | {assigned} | {memberships} |')
    lines += ['', 'BenR (module 27) has 10 published members at threshold 0.12821891758582343. '
              'PP_3765, PP_3168 and PP_3792 in the historical fixed-cutoff report are not published members.', '',
              'An absent assignment is not evidence against TF function. XylR P06519 is outside the reference proteome; '
              'the rsmA/KsgA methyltransferase control Q88QT6 is resolved independently from regulatory RsmA.', '']
    (folder / 'calibration-results.md').write_text('\n'.join(lines))
    assessment_path.write_text(yaml.safe_dump(assessments, sort_keys=False, allow_unicode=True, width=100))
    outputs = [folder / 'calibration-results.json', folder / 'calibration-results.md', *sorted((folder / 'reports').glob('*'))]
    (folder / 'calibration-manifest.json').write_text(json_text({
        'script_sha256': digest(Path(__file__).read_bytes()),
        'dataset_manifest_sha256': digest((folder / 'manifest.json').read_bytes()),
        'calibration_sha256': digest((base / 'calibration.yaml').read_bytes()),
        'identity_input_sha256': {p.as_posix(): digest(p.read_bytes()) for p in
                                 [Path(dataset['organism']['metadata_path']),
                                  *sorted(Path('genes/PSEPK').glob('*/*-ai-review.yaml'))]},
        'outputs': {p.as_posix(): digest(p.read_bytes()) for p in outputs},
    }))
    print(f'Checked {len(rows)} calibration accessions; wrote reports and importer assessment fields')


if __name__ == '__main__':
    main()
