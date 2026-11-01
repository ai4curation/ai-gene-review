"""Check substrate-role coverage; these predicates do not establish native flux."""
from pathlib import Path
import yaml
from ai_gene_review.module_logic import compile_module, is_satisfied, enumerate_routes

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / 'modules/bacterial_23s_rrna_m5u747_methylation.yaml'


def main():
    doc = yaml.safe_load(MODULE.read_text())
    circuit = compile_module(doc)
    def walk(value):
        if isinstance(value, dict):
            yield value
            for child in value.values():
                yield from walk(child)
        elif isinstance(value, list):
            for child in value:
                yield from walk(child)
    selectors = {x['id']: x['participant'] for x in walk(doc) if 'participant' in x}
    assert all(x['selector_type'] == 'GENE_PRODUCT' for x in selectors.values())
    accession = {k: v['gene_product']['term']['id'].removeprefix('UniProtKB:') for k, v in selectors.items()}
    # A dual-specific enzyme can supply both activities; a dedicated enzyme
    # cannot substitute at the other site merely because it shares PTHR11061.
    cases = [
        ('empty context', set(), False),
        ('E. coli paired enzymes', {'P75817', 'P55135'}, True),
        ('E. coli RlmC alone', {'P75817'}, False),
        ('E. coli RlmD alone', {'P55135'}, False),
        ('TrmA alone', {'P23003'}, False),
        ('TrmA does not replace RlmD', {'P75817', 'P23003'}, False),
        ('TrmA does not replace RlmC', {'P55135', 'P23003'}, False),
        ('B. subtilis dual enzyme', {'O31503'}, True),
        ('S. pneumoniae dual enzyme', {'Q97R12'}, True),
    ]
    outcomes = []
    for name, available, expected in cases:
        actual = is_satisfied(circuit, lambda atom: accession[atom.node_id] in available)
        assert actual == expected, (name, actual, expected)
        outcomes.append({'case': name, 'available': sorted(available), 'satisfied': actual})
    for name, activities, expected in [
        ('U747-only activities do not complete paired program', {'ec_c_u747', 'bs_u747', 'sp_u747'}, False),
        ('U1939-only activities do not complete paired program', {'ec_d_u1939', 'bs_u1939', 'sp_u1939'}, False),
        ('Mixed species activities do not complete native variant', {'ec_c_u747', 'sp_u1939'}, False),
    ]:
        actual = is_satisfied(circuit, lambda atom: atom.node_id in activities)
        assert actual == expected, (name, actual, expected)
        outcomes.append({'case': name, 'activities': sorted(activities), 'satisfied': actual})
    routes = enumerate_routes(circuit)
    assert len(routes) == 3 and all(len(route) == 2 for route in routes)
    print(yaml.safe_dump({'cases': outcomes, 'routes': [[a.node_id for a in r] for r in routes]}, sort_keys=False))


if __name__ == '__main__':
    main()
