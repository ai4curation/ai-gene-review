"""Exercise native assemblies and nitrate-input boundaries using production logic.

The explicit oracle enforces exact native products and all complex active units.
The generic Boolean compiler does not itself infer taxonomy or expand subunits.
Extracellular-input cases additionally require the represented uptake mechanism;
this is a boundary check, not a claim that unrepresented transport cannot exist.
"""
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, is_satisfied

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT / "analysis/module_audits/bacterial_assimilatory_nitrate_reduction"


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    doc = yaml.safe_load((ROOT / 'modules/bacterial_assimilatory_nitrate_reduction.yaml').read_text())
    panel = yaml.safe_load((DATA / 'members.yaml').read_text())
    species = {m['accession']: m['organism'] for m in panel}
    products = {(m['organism'], m['gene']): m['accession'] for m in panel}
    inventory = {org: {a for a, s in species.items() if s == org} for org in set(species.values())}
    nodes = {node['id']: node for node in walk(doc['module']) if 'id' in node}
    activities = {a['id']: a for node in walk(doc['module']) for a in node.get('annotons', [])}
    requirements = {}
    for key, activity in activities.items():
        required = {node['term']['id'].split(':', 1)[1] for node in walk(activity['participant'])
                    if str(node.get('term', {}).get('id', '')).startswith('UniProtKB:')}
        assert required and required <= set(species), (key, required)
        assert len({species[a] for a in required}) == 1, ('mixed native assembly', key)
        requirements[key] = required
    uptake = {
        'SYNE7': {products['SYNE7', gene] for gene in ['nrtA', 'nrtB', 'nrtC', 'nrtD']},
        'BACSU': {products['BACSU', 'nasA']},
        'PSEPK': {products['PSEPK', 'nasA']},
    }
    for org, required in uptake.items():
        assert requirements[org.lower() + '_uptake_activity'] == required
    cases = []

    def check(name, node_id, org, present, expected, boundary='intracellular nitrate'):
        def holds(atom):
            required = requirements[atom.node_id]
            return required <= present and all(species[a] == org for a in required)
        observed = is_satisfied(compile_node(nodes[node_id]), holds)
        if boundary == 'extracellular nitrate':
            observed = observed and org in uptake and uptake[org] <= present
        assert observed == expected, (name, expected, observed)
        cases.append({'case': name, 'node': node_id, 'organism_context': org,
                      'input_boundary': boundary, 'present': sorted(present),
                      'expected': expected, 'observed': observed})

    full = doc['module']['id']
    check('Empty panel cannot reduce nitrate', full, 'SYNE7', set(), False)
    for org in ['SYNE7', 'BACSU', 'PSEPK', 'MYCS2']:
        check(org + ' native reduction route', org.lower() + '_route', org, inventory[org], True)
        check(org + ' supports the intracellular module boundary', full, org, inventory[org], True)
        check(org + ' extracellular boundary', full, org, inventory[org], org in uptake,
              'extracellular nitrate')
        for gene, accession in [(m['gene'], m['accession']) for m in panel if m['organism'] == org]:
            present = inventory[org] - {accession}
            is_uptake = accession in uptake.get(org, set())
            check(org + ' lacking ' + gene + ' at intracellular boundary', full, org, present, is_uptake)
            check(org + ' lacking ' + gene + ' at extracellular boundary', full, org, present, False,
                  'extracellular nitrate')
    check('ECOLI comparison alone lacks the upstream nitrate reductase', full, 'ECOLI', inventory['ECOLI'], False)
    check('ECOLI uptake does not complete a nitrate route', full, 'ECOLI', {products['ECOLI', 'narU']}, False,
          'extracellular nitrate')
    check('ECOLI NirBD supports the represented nitrite reaction', 'ecoli_nitrite_reduction_comparison',
          'ECOLI', inventory['ECOLI'], True, 'intracellular nitrite')
    for gene in ['nirB', 'nirD']:
        check('ECOLI NirBD requires ' + gene, 'ecoli_nitrite_reduction_comparison', 'ECOLI',
              inventory['ECOLI'] - {products['ECOLI', gene]}, False, 'intracellular nitrite')
    for org, gene in [('PSEPK', 'nirD'), ('BACSU', 'nasE'), ('SYNE7', 'nirA'), ('MYCS2', 'MSMEG_0428')]:
        mixed = (set(species) - inventory[org]) | (inventory[org] - {products[org, gene]})
        check('Foreign proteins cannot rescue missing native ' + org + ' ' + gene, full, org, mixed, False)
    mixed = {products['MYCS2', 'nasN'], products['PSEPK', 'nirB'], products['PSEPK', 'nirD']}
    for org in ['MYCS2', 'PSEPK']:
        check('Cross-species NasN/NirBD chemistry is not a sampled native route in ' + org,
              full, org, mixed, False)
    # Every multi-subunit activity must fail when any of its required products is absent.
    for key, required in requirements.items():
        if len(required) <= 1:
            continue
        activity_node = {'id': key + '_test_node', 'label': key,
                         'module_type': 'MOLECULAR_FUNCTION', 'annotons': [activities[key]]}
        nodes[activity_node['id']] = activity_node
        org = species[next(iter(required))]
        check(key + ' complete native assembly', activity_node['id'], org, required, True,
              'activity substrates supplied')
        for accession in sorted(required):
            check(key + ' requires ' + accession, activity_node['id'], org, required - {accession}, False,
                  'activity substrates supplied')
    report = {'passed': len(cases), 'failed': 0,
              'limits': 'Exact-product, native-taxon and all-subunit requirements are enforced by the explicit oracle; '
                        'the generic compiler does not guarantee these. Extracellular cases test only the represented '
                        'uptake route. Reducing equivalents, cofactors, maturation, regulation and unrepresented low-affinity '
                        'transport are outside the inventory. The module stops at ammonium and does not model incorporation '
                        'into glutamine/glutamate. Model satisfaction does not establish a new native flux experiment.',
              'cases': cases}
    (DATA / 'route-results.yaml').write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True))
    print(str(len(cases)) + ' native route, assembly and input-boundary cases passed')


if __name__ == '__main__':
    main()
