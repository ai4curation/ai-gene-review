"""Check member choice and regulator logic, not physiological sufficiency.

The production compiler treats complexes as atoms. The oracle below also
requires their declared active_units so a lone RGS6 cannot stand in for its
RGS6-GNB5 complex. Evidence for expression/assembly is assessed separately.
"""
from pathlib import Path
import json
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]

def walk(x):
    if isinstance(x, dict):
        yield x
        for value in x.values():
            yield from walk(value)
    elif isinstance(x, list):
        for value in x:
            yield from walk(value)

def main():
    doc = yaml.safe_load((ROOT / 'modules/acetylcholine_signaling.yaml').read_text())
    objects = {x['id']: x for x in walk(doc) if 'id' in x}
    assert not any(x.get('selector_type') == 'FAMILY' for x in walk(doc))
    results = []
    def present(selector, available):
        kind = selector['selector_type']
        if kind == 'GENE_PRODUCT':
            return selector['gene_product']['term']['id'].split(':')[1] in available
        assert kind == 'PROTEIN_COMPLEX', kind
        units = selector['protein_complex']['active_units']
        return all(present(unit['participant'], available) for unit in units)
    def probe(node, available, expected):
        circuit = compile_node(objects[node], ROOT / 'modules')
        actual = is_satisfied(circuit, lambda atom: present(objects[atom.node_id]['participant'], set(available)))
        assert actual == expected, (node, available, actual, expected)
        results.append({'node': node, 'available': available, 'satisfied': actual})
    for available, expected in [(['P11229','P50148'],True), (['P11229','P09471'],False),
                                (['P08172','P50148'],False), (['P11229','O95837'],False)]:
        probe('machr_gq_activation', available, expected)
    for available, expected in [(['P08172','P63096'],True), (['P08173','P04899'],True),
                                (['P08172','P09471'],False), (['P11229','P63096'],False)]:
        probe('machr_gi_activation', available, expected)
    for available, expected in [(['P11229','O95837'],True), (['P20309','O95837'],True),
                                (['P08912','O95837'],False)]:
        probe('machr_g14_branch', available, expected)
    probe('machr_go_branch', ['P08172','P09471'], True)
    probe('machr_go_branch', ['P08173','P09471'], False)
    for available, expected in [(['P25098'],True), (['P34947'],True), (['P41220'],True),
                                (['P49798'],True), (['P49758'],False), (['O14775'],False),
                                (['P49758','O14775'],True), ([],False)]:
        probe('ach_muscarinic_termination', available, expected)
    regulator_choices = objects['muscarinic_regulator_choices']
    assert regulator_choices['selection'] == 'ONE_OR_MORE'
    assert len(regulator_choices['variants']) == 5
    out = ROOT / '.cache/module-audit-logs/acetylcholine-signaling-choice-cases.json'
    out.write_text(json.dumps(results, indent=2) + '\n')
    print(f'{len(results)} signaling member/regulator cases PASS')

if __name__ == '__main__':
    main()
