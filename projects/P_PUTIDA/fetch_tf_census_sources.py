#!/usr/bin/env python3
"""Snapshot primary-source regulator records and domain/GO vocabularies.

Run from repository root with uv run python. Raw downloads stay in the cache;
compact, lossless-for-selected-fields extracts and checksums are committed.
This extracts regulator identities, not regulatory edges or iModulon membership.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import openpyxl
import requests
from bs4 import BeautifulSoup


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


class Fetcher:
    def __init__(self, cache: Path):
        self.cache = cache
        cache.mkdir(parents=True, exist_ok=True)
        self.records: dict[str, dict] = {}

    def get(self, name: str, url: str) -> bytes:
        path = self.cache / name
        sidecar = path.with_name(path.name + '.provenance.json')
        if sidecar.exists():
            old = json.loads(sidecar.read_text())
            if old['url'] != url:
                raise ValueError(f'Cache URL changed for {name}; use a fresh cache directory')
        if not path.exists():
            response = requests.get(url, timeout=(15, 120))
            response.raise_for_status()
            path.write_bytes(response.content)
        data = path.read_bytes()
        record = {
            'url': url, 'sha256': digest(data), 'bytes': len(data),
            'retrieved_utc': datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
            'timestamp_basis': 'cached download file modification time',
        }
        if sidecar.exists() and old['sha256'] != record['sha256']:
            raise ValueError(f'Cached source changed: {path}')
        write_json(sidecar, record)
        self.records[name] = record
        return data


def parse_regprecise_page(content: bytes, record: dict) -> dict:
    soup = BeautifulSoup(content, 'html.parser')
    props = {}
    for tr in soup.select('tr'):
        cells = tr.find_all('td', recursive=False)
        if len(cells) == 2:
            props[cells[0].get_text(' ', strip=True).rstrip(':')] = cells[1].get_text(' ', strip=True)
    if 'Regulator type' not in props:
        raise ValueError(f'Missing properties in {record["url"]}')
    return {**record, 'source_properties': props,
            'locus_tag': props.get('TF locus tag', ''),
            'family': props.get('Regulator family', '')}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metadata', type=Path, default=Path('projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv'))
    parser.add_argument('--cache', type=Path, default=Path('.cache/putida_tf_census'))
    parser.add_argument('--output', type=Path, default=Path('projects/P_PUTIDA/tf_census/sources'))
    parser.add_argument('--commit', default='f63a0dfab124ea9022123ce6227d132f39de0108', help='Pinned modulome_ppu source commit')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    fetcher = Fetcher(args.cache)
    with args.metadata.open() as handle:
        metadata = list(csv.DictReader(handle, delimiter='\t'))
    observed = {v for row in metadata for key in ('InterPro', 'Pfam') for v in row[key].split(';') if v}

    ipr = fetcher.get('interpro.raw', 'https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/entry.list')
    pfam = fetcher.get('pfam.raw', 'https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.clans.tsv.gz')
    domains = {}
    for row in csv.DictReader(io.StringIO(ipr.decode()), delimiter='\t'):
        if row['ENTRY_AC'] in observed:
            domains[row['ENTRY_AC']] = {'name': row['ENTRY_NAME'], 'type': row['ENTRY_TYPE'], 'database': 'InterPro'}
    for row in csv.reader(io.StringIO(gzip.decompress(pfam).decode()), delimiter='\t'):
        if row[0] in observed:
            domains[row[0]] = {'name': row[4], 'short_name': row[3], 'type': 'Pfam_signature', 'database': 'Pfam'}
    if not domains:
        raise ValueError('No domain identifiers resolved')
    write_json(args.output / 'domains.json', domains)

    go = {}
    for name, term, rel in [('go.raw', 'GO:0003700', 'is_a'), ('go-regulation.json', 'GO:0006355', 'is_a,part_of'), ('go-sigma.json', 'GO:0016987', 'is_a')]:
        url = f'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{term}/descendants?relations={rel}'
        obj = json.loads(fetcher.get(name, url))['results'][0]
        if obj['id'] != term or obj['isObsolete']:
            raise ValueError(f'Unexpected GO root: {term}')
        go[term] = {'name': obj['name'], 'relations': rel, 'ids': sorted(set(obj['descendants']) | {term})}
    write_json(args.output / 'go_branches.json', go)

    index_url = 'https://regprecise.lbl.gov/genome.jsp?genome_id=267'
    html = fetcher.get('regprecise-html.raw', index_url)
    soup = BeautifulSoup(html, 'html.parser')
    records = []
    for tr in soup.select('tr'):
        anchor = tr.select_one('a[href^="regulon.jsp?regulon_id="]')
        if anchor is None:
            continue
        cells = [c.get_text(' ', strip=True) for c in tr.find_all('td', recursive=False)]
        if len(cells) != 6:
            raise ValueError('Unexpected RegPrecise table layout')
        records.append({'source_id': anchor['href'].split('=')[-1], 'source_name': cells[1],
                        'record_type': cells[0], 'effector_text': cells[2], 'pathway_text': cells[3],
                        'url': 'https://regprecise.lbl.gov/' + anchor['href']})
    if not records or not any(r['record_type'] == 'TF' for r in records):
        raise ValueError('RegPrecise index contains no TF records')

    def fetch_record(record: dict) -> dict:
        data = fetcher.get(f'regprecise-{record["source_id"]}.html', record['url'])
        return parse_regprecise_page(data, record)

    with ThreadPoolExecutor(max_workers=5) as executor:
        details = list(executor.map(fetch_record, records))
    write_json(args.output / 'regprecise.json', sorted(details, key=lambda r: int(r['source_id'])))
    print(f'RegPrecise: {len(details)} records', flush=True)

    prefix = f'https://raw.githubusercontent.com/SBRG/modulome_ppu/{args.commit}'
    fetcher.get('precise321.xlsx', prefix + '/Manuscript_supp_data/Supplementary_Data.xlsx')
    license_data = fetcher.get('precise-license.txt', prefix + '/LICENSE')
    (args.output / 'modulome_ppu.LICENSE').write_bytes(license_data)
    workbook = openpyxl.load_workbook(args.cache / 'precise321.xlsx', read_only=True, data_only=True)
    module_rows = list(workbook['4-iM table'].iter_rows(values_only=True))
    if module_rows[0][1] != 'regulator':
        raise ValueError('Unexpected iModulon table header')
    modules = [{'module_id': row[0], 'regulator': row[1], 'category': row[15],
                'function': row[17], 'module_type': row[18]} for row in module_rows[1:] if row[0] is not None]
    trn_rows = list(workbook['3-TRN'].iter_rows(values_only=True))
    if trn_rows[0][1:3] != ('regulator_id', 'gene_id'):
        raise ValueError('Unexpected TRN table header')
    regulators = {}
    for row in trn_rows[1:]:
        if not row[0]:
            continue
        key = (str(row[0]), str(row[1] or ''))
        regulators.setdefault(key, set()).add(str(row[5] or ''))
    regulator_rows = [{'source_name': name, 'locus_tag': locus, 'upstream_evidence': sorted(evidence)}
                      for (name, locus), evidence in sorted(regulators.items())]
    gene_rows = list(workbook['2-Gene table'].iter_rows(values_only=True))
    if gene_rows[0][:3] != ('locus_tag', 'gene_name', 'accession'):
        raise ValueError('Unexpected source gene table header')
    names = {str(m['regulator']).casefold() for m in modules if m['regulator']}
    loci = {r['locus_tag'] for r in regulator_rows}
    genes = [{'locus_tag': r[0], 'gene_name': r[1], 'assembly_accession': r[2],
              'gene_product': r[7], 'uniprot': r[9]} for r in gene_rows[1:]
             if r[0] and (str(r[1]).casefold() in names or r[0] in loci)]
    workbook.close()
    write_json(args.output / 'precise321.json', {
        'dataset': 'putidaPRECISE321', 'publication': 'PMID:35489688',
        'github_commit': args.commit, 'modules': modules, 'regulators': regulator_rows,
        'regulator_gene_records': genes,
        'note': 'TRN regulator identities aid locus mapping; upstream_evidence records prior-knowledge reuse. No targets, module memberships, weights or regulatory signs imported.',
    })
    manifest = {
        'metadata_path': args.metadata.as_posix(), 'metadata_sha256': digest(args.metadata.read_bytes()),
        'modulome_ppu_commit': args.commit,
        'raw_sources': dict(sorted(fetcher.records.items())),
        'normalized_files': {p.name: digest(p.read_bytes()) for p in sorted(args.output.iterdir()) if p.name != 'manifest.json'},
        'reuse_notes': {'modulome_ppu': 'MIT license copied alongside extracts',
                        'RegPrecise': 'Attributed public regulator records; explicit bulk redistribution terms not established',
                        'vocabularies': 'Official InterPro/Pfam names and QuickGO branch identifiers; only metadata-observed domain entries retained'},
    }
    write_json(args.output / 'manifest.json', manifest)
    print(f'PRECISE321: {len(modules)} modules, {len(regulator_rows)} TRN regulator-name/locus pairs; {len(domains)} domain labels', flush=True)


if __name__ == '__main__':
    main()
