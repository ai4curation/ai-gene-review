"""Import pinned iModulonDB exports without manufacturing regulatory evidence.

Published gene tables define membership. Named matrix columns and the published
per-module thresholds independently check those calls. Imported overlap metrics
refer to the source reference regulon, not to our review YAML.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

import openpyxl  # type: ignore[import-untyped]  # Upstream package has no bundled stubs.
import requests
import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / 'src/ai_gene_review/data/imodulondb_organisms.yaml'


class ImportErrorDetail(ValueError):
    """Invalid, ambiguous or incompatible source data; do not produce success."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_text(value) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True, allow_nan=False) + '\n'


def normalize(value: str) -> str:
    value = value.strip()
    match = re.fullmatch(r'PP_?(\d{4,5})', value, re.I)
    return f'pp_{match[1]}' if match else value.casefold()


def optional_number(value, *, integer=False):
    if value is None or str(value).strip() in {'', 'NA', 'NaN', 'nan', 'null'}:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ImportErrorDetail(f'Invalid numerical value: {value!r}') from exc
    if not math.isfinite(number):
        raise ImportErrorDetail(f'Nonfinite numerical value: {value!r}')
    if integer and not number.is_integer():
        raise ImportErrorDetail(f'Expected integer, got {value!r}')
    return int(number) if integer else number


def csv_rows(data: bytes, required: set[str]) -> list[dict]:
    reader = csv.DictReader(io.StringIO(data.decode('utf-8-sig')))
    if len(reader.fieldnames or []) != len(set(reader.fieldnames or [])):
        raise ImportErrorDetail('Duplicate CSV headers')
    if not required <= set(reader.fieldnames or []):
        raise ImportErrorDetail(f'Missing CSV columns: {sorted(required - set(reader.fieldnames or []))}')
    rows = list(reader)
    if any(None in row for row in rows):
        raise ImportErrorDetail('CSV row contains extra fields')
    return rows


def unique_rows(rows: list[dict], key: str) -> dict[str, dict]:
    result = {}
    for row in rows:
        value = str(row[key])
        if not value or value in result:
            raise ImportErrorDetail(f'Empty or duplicate {key}: {value!r}')
        result[value] = row
    return result


def regulator_tokens(expression: str | None) -> list[str]:
    # Preserve the expression separately; these tokens do not change its logic.
    # Hyphens and digits remain part of names (e.g. GltR-II, MetR-I).
    return [x.strip() for x in re.split(r'\s+(?:and|or)\s+|[+/]', expression or '') if x.strip()]


class SourceCache:
    def __init__(self, directory: Path, offline: bool = False):
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=True)
        self.offline = offline
        self.records: dict[str, dict] = {}

    def get(self, url: str) -> bytes:
        key = hashlib.sha256(url.encode()).hexdigest()
        path = self.directory / key
        provenance = path.with_suffix('.json')
        if path.exists() != provenance.exists():
            raise ImportErrorDetail(f'Incomplete cache entry for {url}; remove it and retry')
        if path.exists():
            record = json.loads(provenance.read_text())
            data = path.read_bytes()
            if record['url'] != url or record['sha256'] != digest(data):
                raise ImportErrorDetail(f'Cache integrity failure: {url}')
        else:
            if self.offline:
                raise ImportErrorDetail(f'Not cached in offline mode: {url}')
            response = requests.get(url, timeout=(15, 120))
            response.raise_for_status()
            data = response.content
            record = {'url': url, 'sha256': digest(data), 'bytes': len(data),
                      'retrieved_utc': datetime.now(timezone.utc).isoformat()}
            temporary = path.with_suffix('.tmp')
            temporary.write_bytes(data)
            temporary.replace(path)
            provenance.write_text(json_text(record))
        self.records[url] = record
        return data


def parse_module_table(data: bytes) -> dict[str, dict]:
    rows = csv_rows(data, {'k', 'name', 'regulator_readable', 'n_genes', 'precision', 'recall'})
    unique_rows(rows, 'name')
    modules = {}
    for key, row in unique_rows(rows, 'k').items():
        count = optional_number(row['n_genes'], integer=True)
        if count is None or count < 0:
            raise ImportErrorDetail(f'Invalid membership size for module {key}')
        modules[key] = {
            'module_id': key, 'name': row['name'], 'regulator_expression': row['regulator_readable'] or None,
            'regulator_tokens': regulator_tokens(row['regulator_readable']), 'source_member_count': count,
            'function': row.get('function') or None, 'category': row.get('category') or None,
            'source_reference_regulon_metrics': {k: optional_number(row.get(k)) for k in ('precision', 'recall', 'exp_var')},
            'membership_basis': 'published_gene_table',
        }
    return modules


def parse_members(data: bytes) -> list[dict]:
    # A membership-only CSV legitimately lacks weights; do not invent them.
    rows = csv_rows(data, {'locus', 'gene_name', 'gene_product'})
    unique_rows(rows, 'locus')
    return sorted([{'locus': r['locus'], 'gene_name': r['gene_name'] or None,
                    'gene_product': unquote(r['gene_product']) or None,
                    'weight': optional_number(r.get('gene_weight'))} for r in rows], key=lambda r: r['locus'])


def parse_thresholds(data: bytes) -> dict[str, float | None]:
    rows = csv_rows(data, {''})
    if rows and len(rows[0]) != 2:
        raise ImportErrorDetail('Threshold table must have one ID and one value column')
    result = {}
    for key, row in unique_rows(rows, '').items():
        value = optional_number(next(v for k, v in row.items() if k != ''))
        if value is not None and value < 0:
            raise ImportErrorDetail(f'Negative threshold for {key}')
        result[key] = value
    return result


def check_matrix(data: bytes, modules: dict[str, dict], thresholds: dict) -> dict:
    reader = csv.DictReader(io.StringIO(data.decode('utf-8-sig')))
    headers = reader.fieldnames or []
    if not headers or len(set(headers)) != len(headers) or set(headers[1:]) != set(modules):
        raise ImportErrorDetail('M-matrix named columns do not exactly match source module IDs')
    if set(thresholds) != set(modules):
        raise ImportErrorDetail('Threshold IDs do not exactly match source module IDs')
    member_maps = {k: {r['locus']: r for r in m['members']} for k, m in modules.items()}
    selected: dict[str, set[str]] = {k: set() for k in modules}
    seen = set()
    for row in reader:
        locus = row[headers[0]]
        if not locus or locus in seen or None in row:
            raise ImportErrorDetail(f'Empty/duplicate matrix locus or malformed row: {locus}')
        seen.add(locus)
        for key in modules:
            weight = optional_number(row[key])
            threshold = thresholds[key]
            if weight is not None and threshold is not None and abs(weight) > threshold:
                selected[key].add(locus)
            member = member_maps[key].get(locus)
            if member is not None and member['weight'] is not None:
                if weight is None or not math.isclose(weight, member['weight'], rel_tol=1e-9, abs_tol=1e-12):
                    raise ImportErrorDetail(f'Member weight differs from named M column: {key}/{locus}')
    for key, module in modules.items():
        published = set(member_maps[key])
        if not published <= seen:
            raise ImportErrorDetail(f'Module {key} has members absent from M')
        if len(published) != module['source_member_count']:
            raise ImportErrorDetail(f'Published member-count mismatch for module {key}')
        if thresholds[key] is not None and selected[key] != published:
            raise ImportErrorDetail(f'Threshold membership differs from published table for {key}: '
                                    f'only_threshold={sorted(selected[key]-published)}, only_table={sorted(published-selected[key])}')
        module['threshold'] = thresholds[key]
        module['threshold_check'] = 'passed' if thresholds[key] is not None else 'unavailable'
    return {'matrix_gene_count': len(seen), 'module_count': len(modules), 'named_column_check': 'passed',
            'member_count_check': 'passed', 'measured_weight_check': 'passed'}


def parse_supplement(data: bytes) -> tuple[dict, list[dict], list[dict]]:
    workbook = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True)
    def rows(sheet, first_name, required):
        iterator = workbook[sheet].iter_rows(values_only=True)
        headers = list(next(iterator))
        headers[0] = first_name
        if not required <= set(headers):
            raise ImportErrorDetail(f'Missing required headers in {sheet}')
        return [dict(zip(headers, r)) for r in iterator if r[0] is not None]
    try:
        module_rows = rows('4-iM table', 'name', {'name', 'regulator', 'imodulon_size'})
        stats = {}
        for name, row in unique_rows(module_rows, 'name').items():
            stats[name] = {k: optional_number(row.get(k), integer=k in {'TP', 'regulon_size', 'imodulon_size'})
                           for k in ['pvalue', 'qvalue', 'precision', 'recall', 'f1score', 'TP', 'regulon_size', 'imodulon_size']}
        gene_rows = rows('2-Gene table', 'locus_tag', {'locus_tag', 'gene_name', 'accession', 'uniprot'})
        genes = [{k: r[k] for k in ('locus_tag', 'gene_name', 'accession', 'uniprot')} for r in gene_rows]
        trn_rows = rows('3-TRN', 'regulator_name', {'regulator_name', 'regulator_id', 'evidence'})
        identities = sorted({(str(r['regulator_name']), str(r['regulator_id'] or '')) for r in trn_rows})
        return stats, genes, [{'name': n, 'locus': locus} for n, locus in identities]
    finally:
        workbook.close()


class IModulonDBClient:
    def __init__(self, cache_dir=Path('.cache/imodulondb'), *, config=CONFIG, offline=False):
        self.cache = SourceCache(Path(cache_dir), offline)
        self.config = Path(config)
        self.organisms = yaml.safe_load(self.config.read_text())['mappings']
        self.loaded = {}

    def get_organism_by_code(self, code: str) -> dict:
        hits = [o for o in self.organisms if code.casefold() in {str(x).casefold() for x in [o['canonical_organism'], o['imodulondb_code'], o['taxon_id'], *o.get('aliases', [])]}]
        if len(hits) != 1:
            raise ImportErrorDetail(f'Unknown or ambiguous organism: {code}')
        if not hits[0]['available']:
            raise ImportErrorDetail(hits[0].get('unavailable_reason', 'Dataset not configured'))
        return hits[0]

    def load_dataset(self, organism_code: str) -> dict:
        org = self.get_organism_by_code(organism_code)
        key = org['canonical_organism']
        if key in self.loaded:
            return self.loaded[key]
        commit = org['source_commit']
        if not re.fullmatch('[0-9a-f]{40}', commit):
            raise ImportErrorDetail('Source must be pinned to a full commit SHA')
        prefix = f'https://raw.githubusercontent.com/{org["source_repo"]}/{commit}/{org["source_directory"]}/'
        requested = []
        def get(path):
            url = prefix + path
            requested.append(url)
            return self.cache.get(url)
        table = get('data_files/iM_table.csv')
        modules = parse_module_table(table)
        thresholds = parse_thresholds(get('data_files/M_thresholds.csv'))
        matrix = get('data_files/M.csv')
        metadata = get('dataset_meta.csv')
        def load_members(item):
            module_id, module = item
            module['members'] = parse_members(get(f'iModulon_files/{module_id}/{module_id}_gene_table.csv'))
        with ThreadPoolExecutor(max_workers=6) as executor:
            list(executor.map(load_members, modules.items()))
        checks = check_matrix(matrix, modules, thresholds)
        source_genes: list[dict] = []
        source_identities: list[dict] = []
        if org.get('supplement_url'):
            url = org['supplement_url']
            requested.append(url)
            stats, source_genes, source_identities = parse_supplement(self.cache.get(url))
            if set(stats) != {m['name'] for m in modules.values()}:
                raise ImportErrorDetail('Supplement/dashboard module names differ')
            for module in modules.values():
                source = stats[module['name']]
                if source['imodulon_size'] != module['source_member_count']:
                    raise ImportErrorDetail(f'Supplement/dashboard count mismatch: {module["name"]}')
                for field in ['precision', 'recall']:
                    a, b = source[field], module['source_reference_regulon_metrics'][field]
                    if (a is None) != (b is None) or (a is not None and not math.isclose(a, b, abs_tol=1e-12)):
                        raise ImportErrorDetail(f'Supplement/dashboard {field} mismatch: {module["name"]}')
                module['source_reference_regulon_metrics'].update(source)
            checks['supplement_named_join_check'] = 'passed'
        data = {'organism': org, 'modules': list(modules.values()), 'checks': checks,
                'dataset_metadata_csv': metadata.decode(), 'source_gene_identities': source_genes,
                'source_regulator_identities': source_identities,
                'source_manifest': {url: self.cache.records[url] for url in sorted(set(requested))},
                'importer_sha256': digest(Path(__file__).read_bytes())}
        self.loaded[key] = data
        return data

    def export_dataset(self, code: str, destination: Path) -> dict:
        data = self.load_dataset(code)
        destination.mkdir(parents=True, exist_ok=True)
        (destination / 'dataset.json').write_text(json_text(data))
        with (destination / 'memberships.tsv').open('w', newline='') as handle:
            fields = ['module_id', 'module_name', 'locus', 'gene_name', 'weight', 'membership_basis', 'threshold']
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t', lineterminator='\n')
            writer.writeheader()
            for module in data['modules']:
                for member in module['members']:
                    writer.writerow({'module_id': module['module_id'], 'module_name': module['name'],
                                     **{k: member[k] for k in ['locus', 'gene_name', 'weight']},
                                     'membership_basis': module['membership_basis'], 'threshold': module['threshold']})
        (destination / 'manifest.json').write_text(json_text({
            'source_manifest': data['source_manifest'], 'checks': data['checks'],
            'importer_sha256': data['importer_sha256'],
            'outputs': {n: digest((destination / n).read_bytes()) for n in ['dataset.json', 'memberships.tsv']},
        }))
        return data

    def summarize(self, organism_code: str, query: str, *, repo_root=ROOT) -> dict:
        data = self.load_dataset(organism_code)
        identity, reviews, input_hashes, source_names = resolve_identity(data, query, Path(repo_root))
        assigned = []
        memberships = []
        if identity['status'] == 'resolved':
            for module in data['modules']:
                if {normalize(n) for n in module['regulator_tokens']} & source_names:
                    assigned.append(module)
                for member in module['members']:
                    if normalize(member['locus']) in identity['normalized_loci']:
                        memberships.append({'module_id': module['module_id'], 'module_name': module['name'], 'weight': member['weight']})
        return {'query': query, 'identity': identity, 'review_context': reviews,
                'assigned_modules': assigned, 'gene_memberships': memberships,
                'assignment_status': 'assigned_modules_found' if assigned else 'no_assigned_module' if identity['status'] == 'resolved' else identity['status'],
                'target_comparison_status': 'not_performed_no_structured_curated_target_set',
                'organism': data['organism'], 'source_checks': data['checks'],
                'input_sha256': input_hashes, 'source_manifest': data['source_manifest'],
                'importer_sha256': data['importer_sha256']}

    def compare_with_review(self, organism_code: str, gene_symbol: str, output_dir=Path('.')) -> dict:
        result = self.summarize(organism_code, gene_symbol)
        name = result['identity'].get('report_name') or gene_symbol
        if not re.fullmatch(r'[A-Za-z0-9_.-]+', name):
            raise ImportErrorDetail('Unsafe report name')
        folder = Path(output_dir) / 'genes' / result['organism']['canonical_organism'] / name
        folder.mkdir(parents=True, exist_ok=True)
        write_report(result, folder / f'{name}-imodulondb-comparison.md')
        (folder / f'{name}-imodulondb-comparison.json').write_text(json_text(result))
        return result


def resolve_identity(dataset: dict, query: str, root: Path) -> tuple[dict, list[dict], dict, set[str]]:
    org = dataset['organism']
    metadata_path = root / org.get('metadata_path', '')
    proteins: dict[str, dict] = {}
    loci: dict[str, set[str]] = {}
    aliases: dict[str, set[str]] = {}
    review_data = []
    hashes = {}
    def add(index, key, accession):
        if key:
            index.setdefault(normalize(str(key)), set()).add(accession)
    if org.get('metadata_path'):
        hashes[org['metadata_path']] = digest(metadata_path.read_bytes())
        # The repository proteome snapshot is TSV, unlike source dashboard CSVs.
        with metadata_path.open() as handle:
            for row in csv.DictReader(handle, delimiter='\t'):
                if 'NCBITaxon:' + row['Organism (ID)'] != org['taxon_id']:
                    raise ImportErrorDetail('Metadata taxon does not match requested dataset')
                accession = row['Entry']
                if accession in proteins:
                    raise ImportErrorDetail('Duplicate metadata accession')
                proteins[accession] = row
                for name in row['Gene Names'].split():
                    add(aliases, name, accession)
                    if re.fullmatch(r'PP_?\d{4,5}', name, re.I):
                        add(loci, name, accession)
    else:
        # Generic source-only identities use locus keys and cannot certify a
        # reference-proteome accession join without a configured metadata table.
        for module in dataset['modules']:
            for member in module['members']:
                locus = member['locus']
                proteins.setdefault(locus, {'Entry': locus, 'Gene Names': locus, 'Protein names': member['gene_product']})
                add(loci, locus, locus)
                add(aliases, member['gene_name'], locus)
    for path in sorted((root / 'genes' / org['canonical_organism']).glob('*/*-ai-review.yaml')):
        review = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        accession = str(review.get('id', '')).removeprefix('UniProtKB:')
        taxon = (review.get('taxon') or {}).get('id')
        review_data.append((path, review, accession, taxon))
        if accession in proteins and taxon == org['taxon_id']:
            add(aliases, review.get('gene_symbol'), accession)
    # Authoritative source regulator-to-locus mapping, retaining multiple loci.
    regulator_aliases: dict[str, set[str]] = {}
    for record in dataset['source_regulator_identities']:
        matches = loci.get(normalize(record['locus']), set())
        for accession in matches:
            add(regulator_aliases, record['name'], accession)
    for row in dataset['source_gene_identities']:
        for accession in loci.get(normalize(row['locus_tag']), set()):
            # Source gene-table aliases are secondary to source TRN regulator IDs.
            if normalize(str(row['gene_name'] or '')) not in regulator_aliases:
                add(aliases, row['gene_name'], accession)
    for name, values in regulator_aliases.items():
        aliases.setdefault(name, set()).update(values)
    query_key = normalize(query)
    if query in proteins:
        hits, method = {query}, 'accession'
    elif re.fullmatch(r'PP_?\d{4,5}', query, re.I):
        hits, method = loci.get(query_key, set()), 'locus'
    elif re.fullmatch(r'(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})', query):
        hits, method = set(), 'accession'
    else:
        hits, method = aliases.get(query_key, set()), 'alias'
    if len(hits) > 1:
        raise ImportErrorDetail(f'Ambiguous identifier {query}: {sorted(hits)}; use accession or locus')
    if not hits:
        # A module label is not sufficient to claim a regulator identity.
        return {'status': 'outside_reference_or_unresolved', 'query': query, 'report_name': query,
                'mapping_method': method, 'normalized_loci': []}, [], hashes, set()
    accession = next(iter(hits))
    protein = proteins[accession]
    locus_set = {key for key, values in loci.items() if accession in values}
    context = []
    for path, review, review_accession, taxon in review_data:
        if review_accession == accession and taxon == org['taxon_id']:
            relative = path.relative_to(root).as_posix()
            hashes[relative] = digest(path.read_bytes())
            rows = review.get('existing_annotations') or []
            context.append({'path': relative, 'gene_symbol': review.get('gene_symbol'),
                            'declared_status': review.get('status'), 'annotation_rows': len(rows),
                            'pending_rows': sum(not (r.get('review') or {}).get('action') or (r.get('review') or {}).get('action') == 'PENDING' for r in rows),
                            'validation_status': 'not_run'})
    # Only unambiguous source regulator aliases can assign a module to a protein.
    source_names = {name for name, values in regulator_aliases.items() if values == {accession}}
    if not dataset['source_regulator_identities']:
        source_names = {name for name, values in aliases.items() if values == {accession}}
    name = context[0]['gene_symbol'] if len(context) == 1 else protein['Gene Names'].split()[0] if protein['Gene Names'] else accession
    # Avoid colliding output directories for nonunique symbols such as csrA/fur.
    if aliases.get(normalize(name), set()) != {accession}:
        name = accession
    return {'status': 'resolved', 'accession': accession, 'metadata_names': protein['Gene Names'],
            'protein_name': protein['Protein names'], 'normalized_loci': sorted(locus_set),
            'mapping_method': method, 'report_name': name}, context, hashes, source_names


def write_report(result: dict, path: Path) -> None:
    identity = result['identity']
    lines = [f'# {result["query"]}: iModulon evidence summary', '',
             f'Dataset: {result["organism"]["dataset"]}; identity status: **{identity["status"]}**; '
             f'assignment status: **{result["assignment_status"]}**.', '',
             'Published module membership is expression association. It does not establish direct '
             'targets, activation/repression, ligand specificity or GO annotation validity. '
             'Source overlap metrics describe the authors’ reference regulon, not this gene review.', '',
             '## Identity and review context', '',
             f'- Accession/locus key: {identity.get("accession", "unresolved")}.',
             f'- Metadata names: {identity.get("metadata_names", "unavailable")}.',
             f'- Source locus keys: {", ".join(identity["normalized_loci"]) or "unavailable"}.',
             f'- Mapping method: {identity["mapping_method"]}.']
    for review in result['review_context']:
        lines.append(f'- Read `{review["path"]}`: declared status {review["declared_status"]}; '
                     f'{review["annotation_rows"]} annotation rows; {review["pending_rows"]} pending; validation not run.')
    if not result['review_context']:
        lines.append('- No accession/taxon-matched review context loaded.')
    lines += ['', 'No structured curated target set was supplied, so target-overlap comparison '
              'was not performed. No GO edits are generated.', '', '## Published regulator assignments', '']
    if not result['assigned_modules']:
        lines.append('No module assignment resolved. This is not negative evidence of TF function.')
    for module in result['assigned_modules']:
        lines += [f'### {module["name"]} (source ID {module["module_id"]})', '',
                  f'Regulator expression: {module["regulator_expression"]}. '
                  f'Published members: **{len(module["members"])}**. Threshold: {module["threshold"]}. '
                  f'Membership check: {module["threshold_check"]}.', '',
                  '| Source reference-regulon metric | Value |', '|---|---:|']
        for field, value in module['source_reference_regulon_metrics'].items():
            lines.append(f'| {field} | {"unavailable" if value is None else value} |')
        lines += ['', '| Locus | Gene | Measured weight |', '|---|---|---:|']
        for member in module['members']:
            lines.append(f'| {member["locus"]} | {member["gene_name"] or ""} | {"unavailable" if member["weight"] is None else member["weight"]} |')
        lines.append('')
    lines += ['## Membership of the queried gene', '',
              'This is separate from which module(s) the regulator is assigned to.', '']
    for membership in result['gene_memberships']:
        lines.append(f'- {membership["module_name"]} (ID {membership["module_id"]}): weight {membership["weight"]}.')
    if not result['gene_memberships']:
        lines.append('- No membership resolved; this does not exclude regulatory activity.')
    lines += ['', '## Provenance', '',
              f'- Source commit: `{result["organism"]["source_commit"]}`.',
              f'- Source publication: https://doi.org/{result["organism"]["doi"]}',
              '- Companion JSON records source checks, identity inputs and measured values, with source URLs/checksums inline or linked by source_manifest_path.', '']
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('organism', nargs='?')
    parser.add_argument('gene', nargs='?')
    parser.add_argument('--cache-dir', type=Path, default=Path('.cache/imodulondb'))
    parser.add_argument('--output-dir', type=Path, default=Path('.'))
    parser.add_argument('--export-dataset', type=Path, help='Write all source modules and membership records')
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--list-organisms', action='store_true')
    args = parser.parse_args()
    try:
        client = IModulonDBClient(args.cache_dir, offline=args.offline)
        if args.list_organisms:
            for org in client.organisms:
                print(f'{org["canonical_organism"]}: {org["dataset"]} ({"available" if org["available"] else "not configured"})')
            return
        if not args.organism or not (args.gene or args.export_dataset):
            parser.error('Provide organism and gene, or organism with --export-dataset')
        if args.export_dataset:
            data = client.export_dataset(args.organism, args.export_dataset)
            print(f'Exported {len(data["modules"])} modules; source membership checks passed')
        if args.gene:
            result = client.compare_with_review(args.organism, args.gene, args.output_dir)
            print(f'{result["query"]}: {result["assignment_status"]}; {len(result["assigned_modules"])} assigned modules')
    except (ImportErrorDetail, requests.RequestException, OSError) as exc:
        print(f'iModulon import failed: {exc}', file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == '__main__':
    main()
