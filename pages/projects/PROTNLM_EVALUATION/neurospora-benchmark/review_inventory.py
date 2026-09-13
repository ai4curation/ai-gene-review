"""Check exact-accession review coverage without assigning biological verdicts.

Run from the repository root with uv run python <this-file>. Reviewed actions and
file presence do not replace schema/evidence validation or manual review.
"""
from collections import Counter
import csv
import gzip
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]


def normalized(value):
    return ' '.join(value.split())


def file_references(value):
    """Collect declared file references without interpreting evidence as truth."""
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {'id', 'reference_id', 'source_reference_id'} and isinstance(child, str) and child.startswith('file:'):
                yield child[5:]
            else:
                yield from file_references(child)
    elif isinstance(value, list):
        for child in value:
            yield from file_references(child)


def uniprot_sequence(path):
    if not path.exists():
        return ''
    text = path.read_text()
    if '\nSQ ' not in text:
        return ''
    sequence = text.split('\nSQ ', 1)[1].split('\n', 1)[1].split('//', 1)[0]
    return ''.join(sequence.split())


def main():
    with (ROOT/'review-cohort.csv').open() as f:
        cohort = list(csv.DictReader(f))
    with (ROOT/'review-predictions.csv').open() as f:
        statements = list(csv.DictReader(f))
    with gzip.open(ROOT/'snapshot/uniprot.jsonl.gz', 'rt') as f:
        frozen_records = [json.loads(line) for line in f if line.strip()]
    frozen_sequences = {r['primaryAccession']: r['sequence']['value'] for r in frozen_records}
    inventory = []
    assessment_counts = Counter()
    for target in cohort:
        gene, accession = target['gene_symbol'], target['accession']
        directory = REPO/'genes/NEUCR'/gene
        main_path = directory/(gene+'-ai-review.yaml')
        review = yaml.safe_load(main_path.read_text()) if main_path.exists() else {}
        annotations = review.get('existing_annotations', [])
        goa_annotations = [a for a in annotations if a.get('review', {}).get('action') != 'NEW']
        new_proposals = len(annotations) - len(goa_annotations)
        main_present = bool(review)
        main_identity = review.get('id') == accession
        pending = sum(a.get('review', {}).get('action') in {None, '', 'PENDING'} for a in annotations)
        main_assessed = main_present and main_identity and pending == 0
        go = [s for s in statements if s['accession']==accession and s['type']=='GO']
        negated_ids = {a['term']['id'] for a in annotations if a.get('negated')}
        negative_conflicts = sorted({s['id'] for s in go} & negated_ids)
        functions = [s for s in statements if s['accession']==accession and s['type']=='function']
        sidecar_path = directory/(gene+'-protnlm-predictions-review.yaml')
        sidecar = yaml.safe_load(sidecar_path.read_text()) if sidecar_path.exists() else {}
        expected = {(s['id'],s['text'].split(':',1)[-1]) for s in go}
        actual = {(p['predicted_term']['id'],p['predicted_term']['label']) for p in sidecar.get('predictions', [])}
        assessments = [p.get('review', {}).get('assessment') for p in sidecar.get('predictions', [])]
        go_assessed = not go or (sidecar.get('id')==accession and actual==expected and len(assessments)==len(go) and all(x in {'COR','CNN','LSP','UNC','PLI','NPI','REP'} for x in assessments))
        if go_assessed:
            assessment_counts.update(assessments)
        narrative_path = directory/(gene+'-protnlm-function-review.md')
        narrative = normalized(narrative_path.read_text()) if narrative_path.exists() else ''
        original_retained = all(normalized(s['text']) in narrative for s in functions)
        function_present = not functions or (bool(narrative) and original_retained)
        locations = [s for s in statements if s['accession']==accession and s['type']=='location']
        location_path = directory/(gene+'-protnlm-location-review.md')
        location_text = location_path.read_text() if location_path.exists() else ''
        locations_present = not locations or (bool(location_text) and all(s['id'] in location_text and s['text'] in location_text for s in locations))
        reports = [str(p.relative_to(REPO)) for p in sorted(directory.glob(gene+'-deep-research-*.md')) if p.stat().st_size]
        sequence = uniprot_sequence(directory/(gene+'-uniprot.txt'))
        missing_refs = sorted({ref for document in (review, sidecar) for ref in file_references(document)
                               if not (REPO/ref).is_file() and not (REPO/'genes'/ref).is_file()})
        history = sorted((REPO/'history/genes/NEUCR'/gene).glob('*.yaml'))
        inventory.append({'gene_symbol':gene,'accession':accession,'main_present':main_present,
                          'main_identity_matches':main_identity,'main_schema_status':review.get('status',''),
                          'goa_rows':len(goa_annotations),'new_annotation_proposals':new_proposals,'negated_goa_rows':sum(bool(a.get('negated')) for a in annotations),
                          'positive_predictions_matching_negated_goa':negative_conflicts,'pending_actions':pending,'main_actions_recorded':main_assessed,
                          'expected_go_predictions':len(go),'go_predictions_assessed':len(go) if go_assessed else 0,
                          'go_sidecar_matches_source':go_assessed,'expected_function_paragraphs':len(functions),
                          'function_review_present_with_original':function_present,
                          'expected_location_claims':len(locations),'location_review_present_with_original_ids_labels':locations_present,
                          'uniprot_sequence_matches_frozen':bool(sequence and sequence == frozen_sequences[accession]),
                          'uniprot_sequence_sha256':hashlib.sha256(sequence.encode()).hexdigest() if sequence else None,
                          'goa_source_present':(directory/(gene+'-goa.tsv')).is_file(),
                          'missing_file_references':missing_refs,
                          'notes_present':(directory/(gene+'-notes.md')).is_file(),
                          'rendered_page_present':(directory/(gene+'-ai-review.html')).is_file(),
                          'history_files':[str(p.relative_to(REPO)) for p in history],
                          'research_files':reports,'ready_for_manual_validation':bool(main_assessed and go_assessed and function_present and locations_present and reports)})
    summary = {'cohort_genes':len(cohort),'genes_with_all_review_outputs':sum(r['ready_for_manual_validation'] for r in inventory),
               'go_predictions_assessed':sum(r['go_predictions_assessed'] for r in inventory),
               'location_claims_with_review_files':sum(r['expected_location_claims'] for r in inventory if r['location_review_present_with_original_ids_labels']),
               'go_assessment_counts':dict(sorted(assessment_counts.items())),
               'new_annotation_proposals':sum(r['new_annotation_proposals'] for r in inventory),
               'function_paragraphs_with_review_files':sum(r['expected_function_paragraphs'] for r in inventory if r['function_review_present_with_original']),
               'positive_predictions_matching_negated_goa':sum(len(r['positive_predictions_matching_negated_goa']) for r in inventory),
               'goa_rows_with_review_actions':sum(r['goa_rows'] for r in inventory if r['main_actions_recorded']),
               'caveat':'Coverage checks exact accession, GO IDs/labels, valid assessment codes, original paragraph retention and localization SL IDs/labels. It does not certify supporting evidence, scientific correctness, narrative atomic assessment or validation success.'}
    (ROOT/'review-inventory.json').write_text(json.dumps({'summary':summary,'genes':inventory},indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
