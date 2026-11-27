#!/usr/bin/env python3
"""Build a deterministic KT2440 TF candidate inventory from versioned sources.

Discovery signals and provisional role queues are not curated function claims.
All biological rules and calibration choices live in editable YAML inputs.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict]:
    with path.open() as handle:
        return list(csv.DictReader(handle, delimiter='\t'))


def write_tsv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, delimiter='\t', fieldnames=fields, extrasaction='raise', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def joined(values) -> str:
    return '; '.join(sorted({str(v) for v in values if v is not None and str(v)}))


def tokens(value: str) -> set[str]:
    return {x.strip() for x in value.split(';') if x.strip()}


def normalize(value: str) -> str:
    match = re.fullmatch(r'PP_?(\d{4,5})', value, re.I)
    return f'pp_{match[1]}' if match else value.casefold().strip()


class IdentityIndex:
    def __init__(self, metadata: list[dict], reviews: list[dict]):
        self.by_accession = {r['Entry']: r for r in metadata}
        if len(self.by_accession) != len(metadata):
            raise ValueError('Duplicate metadata accessions')
        self.loci = defaultdict(set)
        self.aliases = defaultdict(set)
        for row in metadata:
            for name in row['Gene Names'].split():
                key = normalize(name)
                self.aliases[key].add(row['Entry'])
                if re.fullmatch(r'pp_\d{4,5}', key):
                    self.loci[key].add(row['Entry'])
        for review in reviews:
            if review['accession'] in self.by_accession and review['taxon_id'] == '160488':
                self.aliases[normalize(review['gene_symbol'])].add(review['accession'])

    def resolve(self, *, accession: str = '', locus: str = '', name: str = '') -> tuple[str, str, set[str]]:
        # Strong identifiers are authoritative. Never silently fall back from a
        # missing accession/locus to an attractive but potentially wrong symbol.
        if accession:
            hits = {accession} if accession in self.by_accession else set()
            method = 'accession'
        elif locus:
            hits = self.loci.get(normalize(locus), set())
            method = 'locus'
        else:
            hits = self.aliases.get(normalize(name), set())
            method = 'alias'
        status = 'mapped' if len(hits) == 1 else 'ambiguous' if hits else 'unmapped'
        return status, method, set(hits)


def load_reviews(directory: Path) -> list[dict]:
    reviews = []
    for path in sorted(directory.glob('*/*-ai-review.yaml')):
        data = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        rows = data.get('existing_annotations') or []
        actions = Counter((r.get('review') or {}).get('action') or 'PENDING' for r in rows)
        reviews.append({
            'accession': str(data.get('id', '')).removeprefix('UniProtKB:'),
            'gene_symbol': str(data.get('gene_symbol', '')),
            'taxon_id': str((data.get('taxon') or {}).get('id', '')).removeprefix('NCBITaxon:'),
            'review_path': path.as_posix(), 'declared_status': str(data.get('status', 'UNSET')),
            'annotation_rows': len(rows), 'pending_rows': actions['PENDING'],
            'undecided_rows': actions['UNDECIDED'], 'has_core_functions': bool(data.get('core_functions')),
            'term_ids': {r.get('term', {}).get('id') for r in rows},
            'validation_status': 'not_run',
        })
    return reviews


def classify(row: dict, domains: dict, go: dict, rules: dict, *, external: bool = False) -> tuple[str, str]:
    name = row['Protein names']
    ids = tokens(row['InterPro']) | tokens(row['Pfam'])
    go_ids = tokens(row['Gene Ontology IDs'])
    def matches(rule, value=name):
        return bool(re.search(rules[rule], value, re.I))
    def has(rule):
        return bool(ids & set(rules[rule]))
    domain_text = ' ; '.join(domains[i]['name'] for i in ids if i in domains and domains[i]['type'] != 'Homologous_superfamily')
    if matches('cofactor_name'):
        return 'transcription_machinery_or_cofactor_candidate', 'Named transcription machinery/accessory role; assess separately from sequence-specific TFs.'
    if matches('post_transcriptional_name') or has('post_transcriptional_ids'):
        return 'post_transcriptional_regulator_candidate', 'RNA-regulatory name or specific family signature; not a DNA-binding TF call.'
    if matches('nucleoid_name') or has('nucleoid_ids'):
        return 'nucleoid_associated_candidate', 'Nucleoid-associated name or signature; sequence-specific TF activity remains a separate question.'
    if matches('sigma_name') or has('sigma_ids') or go_ids & set(go['GO:0016987']['ids']):
        return 'sigma_factor_candidate', 'Sigma-factor name, signature or GO signal; separate scope lane.'
    tf = (matches('tf_name') or matches('tf_domain', domain_text) or bool(go_ids & (set(go['GO:0003700']['ids']) - set(go['GO:0016987']['ids']))))
    if matches('nontranscriptional_name'):
        return ('ambiguous_candidate', 'Transcriptional and non-transcriptional signals conflict.') if tf or external else ('other_signaling_candidate', 'Named non-transcriptional signaling output; receiver domain alone does not establish TF activity.')
    if matches('nonregulatory_name'):
        return ('ambiguous_candidate', 'Regulatory discovery signal conflicts with an enzyme/replication/repair name; inspect multifunctionality.') if tf or external else ('nonregulatory_candidate', 'Name indicates replication/repair/RNA modification; broad DNA-binding/HTH signals do not establish TF function.')
    if tf:
        return ('transcriptional_response_regulator_candidate' if has('receiver_ids') else 'dbtf_candidate', 'TF-associated name, GO or specific architecture; provisional queue, not a curated function verdict.')
    if has('receiver_ids'):
        return 'ambiguous_candidate', 'Receiver domain found without resolved transcriptional output.'
    return 'ambiguous_candidate', 'Broad name/domain/GO or external-regulator signal requires role assessment.'


def external_records(regprecise: list[dict], precise: dict) -> list[dict]:
    records = []
    for r in regprecise:
        records.append({'source': 'RegPrecise', 'record_id': r['source_id'], 'name': r['source_name'],
                        'loci': re.findall(r'PP_?\d{4,5}', r['locus_tag']), 'module_id': '',
                        'protein_record': r['record_type'] == 'TF', 'url': r['url'],
                        'evidence': 'comparative_genomic_inference', 'family': r['family']})
    trn_index = defaultdict(set)
    for r in precise['regulators']:
        if r['locus_tag']:
            trn_index[normalize(r['source_name'])].add(r['locus_tag'])
        records.append({'source': 'PRECISE321_TRN', 'record_id': r['source_name'] + ':' + r['locus_tag'],
                        'name': r['source_name'], 'loci': [r['locus_tag']] if r['locus_tag'] else [],
                        'module_id': '', 'protein_record': True, 'url': 'https://doi.org/10.1016/j.ymben.2022.04.004',
                        'evidence': joined(r['upstream_evidence']), 'family': ''})
    gene_index = defaultdict(set)
    for r in precise['regulator_gene_records']:
        if r['gene_name']:
            gene_index[normalize(r['gene_name'])].add(r['locus_tag'])
    for r in precise['modules']:
        name = r['regulator'] or ''
        loci = trn_index.get(normalize(name)) or gene_index.get(normalize(name)) or set()
        records.append({'source': 'PRECISE321_MODULE', 'record_id': r['module_id'], 'name': name,
                        'loci': sorted(loci), 'module_id': r['module_id'], 'protein_record': bool(name),
                        'url': 'https://doi.org/10.1016/j.ymben.2022.04.004',
                        'evidence': 'published_regulator_assignment; not module gene membership', 'family': ''})
    return records


def write_report(path: Path, summary: dict, inventory: list[dict], mappings: list[dict], calibration: list[dict], reviews: list[dict]) -> None:
    lines = [
        '# KT2440 TF candidate census and review coverage', '',
        'Generated from the pinned inputs in [build_manifest.json](build_manifest.json). '
        'See [methods and limitations](../README.md) and [source provenance](../sources/manifest.json).', '',
        '**This is a provisional candidate census, not a count of experimentally verified TFs.** '
        'Broad discovery intentionally retains uncertain DNA-binding and signaling proteins. '
        'Triage exclusions apply to the main work queue and are not GO annotation removals.', '',
        f'- Reference metadata: **{summary["metadata_proteins"]} proteins**.',
        f'- Candidate union: **{summary["candidates"]} proteins**.',
        f'- Existing review files cover **{summary["candidates_with_reviews"]} candidates**; '
        f'**{summary["candidates_without_reviews"]} candidates** have no accession-matched review.',
        f'- **{summary["ambiguous_aliases"]} ambiguous aliases** are retained in [ambiguous_aliases.tsv](ambiguous_aliases.tsv).',
        f'- Unresolved external records: **{summary["unresolved_source_records"]}**; see [source_mappings.tsv](source_mappings.tsv).', '',
        '## Provisional role queues', '',
        '| Candidate class | Total | With review file | Without review file |',
        '|---|---:|---:|---:|',
    ]
    for role, count in summary['candidate_classes'].items():
        reviewed = sum(bool(r['review_count']) for r in inventory if r['candidate_class'] == role)
        lines.append(f'| {role} | {count} | {reviewed} | {count-reviewed} |')
    lines += ['', '## Discovery signals and source reconciliation', '',
              'Counts overlap and do not represent independent lines of evidence. '
              'PRECISE321_TRN is published prior knowledge, including reused RegPrecise records; '
              'PRECISE321_MODULE is a regulator assignment, not gene membership. '
              'Exact source combinations are in [summary.json](summary.json).', '',
              '| Discovery source | Distinct candidate proteins |', '|---|---:|']
    for source, count in summary['discovery_source_counts'].items():
        lines.append(f'| {source} | {count} |')
    lines += ['', '| External source | Record mapping outcome | Count |', '|---|---|---:|']
    for source, counts in summary['source_mapping_statuses'].items():
        for status, count in counts.items():
            lines.append(f'| {source} | {status} | {count} |')
    lines += ['', 'Explicitly listed multiple source loci contribute candidates for each resolved '
              'protein; the record does not resolve their individual target specificity. '
              'RNA regulons and modules without assigned regulators are retained but do not create protein candidates.', '',
              '### Unresolved external mappings', '']
    for row in mappings:
        if row['mapping_status'] in {'unmapped', 'ambiguous', 'ambiguous_source_loci'}:
            lines.append(f'- [{row["source"]} {row["source_name"]}]({row["source_url"]}): '
                         f'{row["mapping_status"]}; source loci: {row["source_loci"] or "not supplied"}.')
    lines += ['', '## Existing review coverage', '',
              f'Inspected **{summary["all_review_files"]} review files**. '
              'Full-file mapping results are in [review_coverage.tsv](review_coverage.tsv). '
              'No gene validators were run for this inventory; `validation_status` is `not_run`. '
              'A declared COMPLETE status, zero PENDING rows, or a core-function section does not certify biological accuracy.', '',
              f'- Candidates with PENDING rows: {sum(r["pending_rows"] > 0 for r in inventory)}.',
              f'- Candidates with UNDECIDED rows: {sum(r["undecided_rows"] > 0 for r in inventory)}.',
              f'- Candidates with at least one core-function section: {sum(r["reviews_with_core_functions"] > 0 for r in inventory)}.', '',
              '### Reviews outside the accession/taxon join', '']
    for row in reviews:
        if row['mapping_status'] != 'mapped':
            lines.append(f'- {row["gene_symbol"]} ({row["accession"]}): {row["mapping_status"]}; '
                         f'in reference proteome: {row["in_reference_proteome"]}; review taxon: {row["taxon_id"]}.')
    lines += ['', '## Prioritized calibration worklist', '',
              'Scoped identity/evidence and importer assessments are tracked separately from full GO reviews; see '
              '[calibration assessment](../calibration-review.md). The rsmA negative '
              'control and out-of-proteome XylR control are excluded from the candidate denominator. Full rationale and paths '
              'are in [calibration.tsv](calibration.tsv). '
              f'{sum(r["full_go_review_status"] == "REVIEWED_VALIDATED" for r in calibration)} '
              'cases have a recorded full GO re-review and validation in this workstream.', '',
              '| Order | Accession | Display name | Locus | Candidate class |', '|---:|---|---|---|---|']
    for row in calibration:
        lines.append(f'| {row["order"]} | {row["accession"]} | {row["display_name"]} | {row["locus_tags"]} | {row["candidate_class"]} |')
    lines += ['', 'The full [candidate worklist](candidates.tsv) is sorted by calibration selection, '
              'identity/role conflicts, unreviewed regulator candidates, existing-review refresh, '
              'then boundary audits. Reasons and source signals are retained per row.', '',
              '## Coverage limits', '',
              f'- {len(summary["domain_ids_missing_labels"])} observed domain identifiers could not be '
              'resolved in the downloaded current-release catalogs. IDs are listed in summary.json; '
              'no replacement IDs were guessed.',
              '- The July 2026 local UniProt snapshot and the 2022 PRECISE321 source gene table '
              'are different snapshots. Locus joins resolve identifiers but do not certify sequence '
              'identity or functional transfer; no genome coordinates were transferred.',
              '- No sequence classifier, new domain search, systematic literature search, or '
              'direct-target/ligand evidence audit was performed. Proteins outside this candidate '
              'union may still be undiscovered TFs. Missing database coverage is not negative evidence.',
              '- CollecTF, PRODORIC, P2TF/P2CS and groovDB remain subsequent evidence sources; '
              'their coverage is not claimed by this census.', '']
    path.write_text('\n'.join(lines))


def build(args) -> None:
    source_manifest = json.loads((args.sources / 'manifest.json').read_text())
    if sha256(args.metadata) != source_manifest['metadata_sha256']:
        raise ValueError('Metadata snapshot differs from source extraction; refresh sources first')
    for name, checksum in source_manifest['normalized_files'].items():
        if sha256(args.sources / name) != checksum:
            raise ValueError(f'Source checksum mismatch: {name}')
    metadata = read_tsv(args.metadata)
    if {r['Organism (ID)'] for r in metadata} != {'160488'}:
        raise ValueError('Unexpected organism in metadata')
    rules = yaml.safe_load(args.rules.read_text())
    domains = json.loads((args.sources / 'domains.json').read_text())
    go = json.loads((args.sources / 'go_branches.json').read_text())
    reviews = load_reviews(args.reviews)
    identities = IdentityIndex(metadata, reviews)
    review_index = defaultdict(list)
    review_rows = []
    for review in reviews:
        status, method, hits = identities.resolve(accession=review['accession'])
        if review['taxon_id'] != '160488':
            status = 'taxon_mismatch'
        elif status == 'mapped':
            review_index[review['accession']].append(review)
        review_rows.append({k: v for k, v in review.items() if k != 'term_ids'} | {
            'mapping_status': status,
            'in_reference_proteome': review['accession'] in identities.by_accession,
        })

    mapped_external = defaultdict(list)
    mappings = []
    for record in external_records(json.loads((args.sources / 'regprecise.json').read_text()), json.loads((args.sources / 'precise321.json').read_text())):
        if not record['protein_record']:
            status, method, hits = ('not_protein_record' if record['source'] == 'RegPrecise' else 'no_regulator_assignment'), 'none', set()
        elif len(record['loci']) > 1:
            status, method, hits = 'mapped_multiple_loci', 'locus', set()
            for locus in record['loci']:
                locus_status, _, locus_hits = identities.resolve(locus=locus)
                hits |= locus_hits
                if locus_status != 'mapped':
                    status = 'ambiguous_source_loci'
        else:
            status, method, hits = identities.resolve(locus=next(iter(record['loci']), ''), name=record['name'])
        flags = []
        if status in {'mapped', 'mapped_multiple_loci'}:
            # Compare source names to metadata aliases, not aliases already imported
            # from reviews, so review/metadata disagreement stays visible.
            for accession in sorted(hits):
                aliases = {normalize(x) for x in identities.by_accession[accession]['Gene Names'].split()}
                if normalize(record['name']) not in aliases:
                    flags.append('source_name_differs_from_metadata')
                mapped_external[accession].append(record)
            if status == 'mapped_multiple_loci':
                flags.append('source_explicitly_lists_multiple_loci')
        mappings.append({'source': record['source'], 'record_id': record['record_id'], 'source_name': record['name'],
                         'source_loci': joined(record['loci']), 'module_id': record['module_id'], 'mapping_status': status,
                         'mapping_method': method, 'accessions': joined(hits), 'flags': joined(flags),
                         'source_url': record['url'], 'evidence_origin': record['evidence']})

    calibration = yaml.safe_load(args.calibration.read_text())['cases']
    controls = {r['accession']: r for r in calibration}
    inventory = []
    for row in metadata:
        accession = row['Entry']
        ids = tokens(row['InterPro']) | tokens(row['Pfam'])
        go_ids = tokens(row['Gene Ontology IDs'])
        signals = []
        if re.search(rules['name_discovery'], row['Protein names'], re.I):
            signals.append('protein_name')
        if 'Transcription regulation' in tokens(row['Keywords']):
            signals.append('uniprot_keyword')
        matched_go = set()
        for root, label in [('GO:0003700', 'go_tf'), ('GO:0006355', 'go_transcription_regulation'), ('GO:0016987', 'go_sigma')]:
            hits = go_ids & set(go[root]['ids'])
            if hits:
                signals.append(label)
                matched_go |= hits
        domain_hits = {i for i in ids if i in domains and re.search(rules['domain_discovery'], domains[i]['name'] + ' ' + domains[i].get('short_name', ''), re.I)}
        for database in ['InterPro', 'Pfam']:
            if any(domains[i]['database'] == database for i in domain_hits):
                signals.append(database)
        ext = mapped_external[accession]
        signals.extend(sorted({e['source'] for e in ext}))
        matched_reviews = review_index[accession]
        if any(r['term_ids'] & set(go['GO:0003700']['ids']) for r in matched_reviews):
            signals.append('existing_review_tf_row')
        if not signals:
            continue
        role, reason = classify(row, domains, go, rules, external=bool(ext))
        main = role in {'dbtf_candidate', 'transcriptional_response_regulator_candidate'}
        related = role in {'sigma_factor_candidate', 'nucleoid_associated_candidate', 'post_transcriptional_regulator_candidate', 'transcription_machinery_or_cofactor_candidate'}
        disposition = 'main_tf_queue_provisional' if main else 'related_regulator_queue_provisional' if related else 'excluded_from_main_by_triage' if role in {'nonregulatory_candidate', 'other_signaling_candidate'} else 'unresolved'
        names = row['Gene Names'].split()
        flags = []
        if any(len(identities.aliases[normalize(n)]) > 1 for n in names):
            flags.append('nonunique_alias')
        if any(normalize(r['gene_symbol']) not in {normalize(n) for n in names} for r in matched_reviews):
            flags.append('review_symbol_differs_from_metadata')
        if any(normalize(e['name']) not in {normalize(n) for n in names} for e in ext):
            flags.append('source_name_differs_from_metadata')
        if len(matched_reviews) > 1:
            flags.append('multiple_review_files')
        if not matched_reviews:
            flags.append('no_review')
        if any(r['pending_rows'] for r in matched_reviews):
            flags.append('pending_annotation_rows')
        if any(r['declared_status'] == 'COMPLETE' and (r['pending_rows'] or not r['has_core_functions']) for r in matched_reviews):
            flags.append('declared_complete_needs_audit')
        if role == 'ambiguous_candidate':
            flags.append('role_unresolved')
        priority = 'P0_calibration' if accession in controls else 'P1_identity_conflict' if any(x in flags for x in ['review_symbol_differs_from_metadata', 'source_name_differs_from_metadata', 'role_unresolved', 'multiple_review_files']) else 'P2_unreviewed' if not matched_reviews and (main or related) else 'P3_review_refresh' if matched_reviews else 'P4_boundary_audit'
        inventory.append({
            'accession': accession, 'locus_tags': joined(n for n in names if normalize(n).startswith('pp_')),
            'metadata_gene_names': row['Gene Names'], 'protein_name': row['Protein names'],
            'candidate_class': role, 'triage_disposition': disposition, 'triage_reason': reason,
            'priority': priority, 'discovery_sources': joined(signals), 'flags': joined(flags),
            'matched_go_ids': joined(matched_go), 'domain_signals': joined(f'{i} {domains[i]["name"]}' for i in domain_hits),
            'family_labels': joined(f'{i} {domains[i]["name"]}' for i in domain_hits if domains[i]['type'] == 'Family'),
            'regprecise_families': joined(e['family'] for e in ext if e['family']),
            'external_regulator_names': joined(e['name'] for e in ext),
            'imodulon_assignments': joined(e['module_id'] for e in ext if e['module_id']),
            'review_paths': joined(r['review_path'] for r in matched_reviews),
            'review_symbols': joined(r['gene_symbol'] for r in matched_reviews),
            'declared_review_status': joined(r['declared_status'] for r in matched_reviews),
            'review_count': len(matched_reviews), 'annotation_rows': sum(r['annotation_rows'] for r in matched_reviews),
            'pending_rows': sum(r['pending_rows'] for r in matched_reviews),
            'undecided_rows': sum(r['undecided_rows'] for r in matched_reviews),
            'reviews_with_core_functions': sum(r['has_core_functions'] for r in matched_reviews),
            'validation_status': 'not_run',
            'uniprot_function_pmids': joined(re.findall(r'PubMed:(\d+)', row['Function [CC]'])),
            'calibration_rationale': controls.get(accession, {}).get('rationale', ''),
        })
    inventory.sort(key=lambda r: (r['priority'], r['locus_tags'], r['accession']))
    args.output.mkdir(parents=True, exist_ok=True)
    write_tsv(args.output / 'candidates.tsv', inventory, list(inventory[0]))
    write_tsv(args.output / 'source_mappings.tsv', mappings, list(mappings[0]))
    write_tsv(args.output / 'review_coverage.tsv', review_rows, list(review_rows[0]))
    alias_rows = [{'alias': key, 'accessions': joined(values)} for key, values in sorted(identities.aliases.items()) if len(values) > 1]
    write_tsv(args.output / 'ambiguous_aliases.tsv', alias_rows, ['alias', 'accessions'])
    inv_index = {r['accession']: r for r in inventory}
    assessment_path = args.calibration.with_name('calibration-assessments.yaml')
    assessments = {}
    if assessment_path.exists():
        for assessment in yaml.safe_load(assessment_path.read_text())['cases']:
            accession = assessment['accession']
            if accession in assessments or accession not in controls:
                raise ValueError(f'Duplicate or unselected calibration assessment: {accession}')
            assessments[accession] = assessment
    calibration_rows = []
    for number, case in enumerate(calibration, 1):
        row = inv_index.get(case['accession'])
        metadata_row = identities.by_accession.get(case['accession'])
        control_class = (classify(metadata_row, domains, go, rules)[0]
                         if metadata_row else 'outside_reference_proteome')
        calibration_rows.append({'order': number, 'accession': case['accession'], 'display_name': case['name'],
                                 'locus_tags': row['locus_tags'] if row else joined(n for n in (metadata_row or {}).get('Gene Names', '').split() if normalize(n).startswith('pp_')),
                                 'candidate_class': row['candidate_class'] if row else control_class,
                                 'in_candidate_census': bool(row),
                                 'review_paths': row['review_paths'] if row else joined(r['review_path'] for r in reviews if r['accession'] == case['accession']),
                                 'rationale': case['rationale'],
                                 'scoped_assessment_status': assessments.get(case['accession'], {}).get('assessment_status', 'not_started'),
                                 'importer_assessment_status': assessments.get(case['accession'], {}).get('importer_assessment', {}).get('status', 'not_started'),
                                 'full_go_review_status': assessments.get(case['accession'], {}).get('full_go_review', {}).get('status', 'not_assessed_in_this_calibration')})
    write_tsv(args.output / 'calibration.tsv', calibration_rows, list(calibration_rows[0]))
    summary = {
        'metadata_proteins': len(metadata), 'candidates': len(inventory),
        'candidate_classes': dict(sorted(Counter(r['candidate_class'] for r in inventory).items())),
        'triage_dispositions': dict(sorted(Counter(r['triage_disposition'] for r in inventory).items())),
        'candidates_with_reviews': sum(r['review_count'] > 0 for r in inventory),
        'candidates_without_reviews': sum(r['review_count'] == 0 for r in inventory),
        'all_review_files': len(reviews),
        'review_mapping_statuses': dict(sorted(Counter(r['mapping_status'] for r in review_rows).items())),
        'source_mapping_statuses': {s: dict(sorted(Counter(r['mapping_status'] for r in mappings if r['source'] == s).items())) for s in sorted({r['source'] for r in mappings})},
        'discovery_source_counts': dict(sorted(Counter(s for r in inventory for s in r['discovery_sources'].split('; ')).items())),
        'source_intersections': dict(sorted(Counter(r['discovery_sources'] for r in inventory).items())),
        'ambiguous_aliases': len(alias_rows), 'calibration_cases': len(calibration_rows),
        'calibration_full_go_review_statuses': dict(sorted(Counter(r['full_go_review_status'] for r in calibration_rows).items())),
        'unresolved_source_records': sum(r['mapping_status'] in {'unmapped', 'ambiguous', 'ambiguous_source_loci'} for r in mappings),
        'domain_ids_missing_labels': sorted({i for r in metadata for key in ('InterPro', 'Pfam') for i in tokens(r[key]) if i not in domains}),
    }
    write_report(args.output / 'coverage.md', summary, inventory, mappings, calibration_rows, review_rows)
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
    inputs = [args.metadata, args.rules, args.calibration, args.sources / 'manifest.json'] + sorted(args.sources.glob('*.json')) + sorted(args.reviews.glob('*/*-ai-review.yaml'))
    if assessment_path.exists():
        inputs.append(assessment_path)
    build_manifest = {'inputs': {p.as_posix(): sha256(p) for p in sorted(set(inputs))},
                      'script_sha256': sha256(Path(__file__)),
                      'outputs': {p.name: sha256(p) for p in sorted(args.output.iterdir()) if p.name != 'build_manifest.json'}}
    (args.output / 'build_manifest.json').write_text(json.dumps(build_manifest, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in summary.items() if k not in {'source_intersections', 'domain_ids_missing_labels'}}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metadata', type=Path, default=Path('projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv'))
    parser.add_argument('--sources', type=Path, default=Path('projects/P_PUTIDA/tf_census/sources'))
    parser.add_argument('--reviews', type=Path, default=Path('genes/PSEPK'))
    parser.add_argument('--rules', type=Path, default=Path('projects/P_PUTIDA/tf_census/rules.yaml'))
    parser.add_argument('--calibration', type=Path, default=Path('projects/P_PUTIDA/tf_census/calibration.yaml'))
    parser.add_argument('--output', type=Path, default=Path('projects/P_PUTIDA/tf_census/data'))
    build(parser.parse_args())


if __name__ == '__main__':
    main()
