"""Recreate the EEF1A2 BioPlex selection from four exact full upstream tables."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = 'EEF1A2'
PARTNERS = {'TBXAS1', 'ST6GALNAC1', 'SLC13A5'}
VERSIONS = {
    '2.0': ('BioPlex_interactionList_v4a.tsv', 'BioPlex_2.0_293T_DirectedEdges.tsv', 'p(Interaction)'),
    '3.0': ('BioPlex_293T_Network_10K_Dec_2019.tsv', 'BioPlex_3.0_293T_DirectedEdges.tsv', 'pInt'),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def table(path, left, right):
    incident, total = [], 0
    with path.open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        require(left in (reader.fieldnames or []) and right in reader.fieldnames, f'Unexpected columns: {path.name}')
        for physical_line, fields in enumerate(reader, 2):
            total += 1
            require(None not in fields and None not in fields.values(), f'Malformed row {physical_line}: {path.name}')
            if TARGET in (fields[left], fields[right]):
                incident.append({'physical_line': physical_line, 'fields': fields})
    return total, incident


def analyze(input_dir):
    manifest = json.loads((HERE / 'bioplex-inputs.json').read_text())
    for entry in manifest['inputs']:
        path = input_dir / entry['name']
        require(path.is_file(), f'Missing full upstream input: {path}')
        require(path.stat().st_size == entry['bytes'], f'Input size mismatch: {path.name}')
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256'], f'Input checksum mismatch: {path.name}')
    result = {'target': TARGET, 'selection_partners': sorted(PARTNERS),
              'coordinate_convention': 'Physical lines are 1-based and include the TSV header.',
              'datasets': {}, 'pairs': {}}
    for version, (network_name, directed_name, score_column) in VERSIONS.items():
        total, network = table(input_dir / network_name, 'SymbolA', 'SymbolB')
        directed_total, directed = table(input_dir / directed_name, 'Bait Symbol', 'Prey Symbol')
        result['datasets'][version] = {'network': network_name, 'total_rows': total, 'incident_rows': len(network),
                                       'directed': directed_name, 'directed_total_rows': directed_total,
                                       'directed_incident_rows': len(directed)}
        for partner in sorted(PARTNERS):
            selected = [row for row in network if {row['fields']['SymbolA'], row['fields']['SymbolB']} == {TARGET, partner}]
            selected_directed = [row for row in directed if {row['fields']['Bait Symbol'], row['fields']['Prey Symbol']} == {TARGET, partner}]
            require(len(selected) == 1, f'Expected one filtered network edge: {version}/{partner}')
            require(selected_directed, f'No directed edge: {version}/{partner}')
            score = selected[0]['fields'][score_column]
            float(score)  # Reject nonnumeric scores without imposing a new confidence cutoff.
            result['pairs'].setdefault(partner, {})[version] = {
                'network_record': selected[0], 'directed_records': selected_directed,
                'score_column': score_column, 'score': score,
                'target_bait_edges': sum(row['fields']['Bait Symbol'] == TARGET for row in selected_directed),
                'partner_bait_edges': sum(row['fields']['Bait Symbol'] == partner for row in selected_directed)}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, required=True, help='Directory containing the four full files named in bioplex-inputs.json')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = analyze(args.input_dir)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f'ERROR: {error}\n')
    print('PASS: all-input counts and six selected BioPlex network records reproduced.')


if __name__ == '__main__':
    main()
