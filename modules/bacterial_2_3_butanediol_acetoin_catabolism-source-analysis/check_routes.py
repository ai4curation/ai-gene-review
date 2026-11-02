"""Native component coverage, not a claim of in-vivo flux or purified activity."""
from pathlib import Path
import yaml
from ai_gene_review.module_logic import compile_module, compile_node, is_satisfied, enumerate_routes

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'modules/bacterial_2_3_butanediol_acetoin_catabolism.yaml'

def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)

def main():
    document = yaml.safe_load(PATH.read_text())
    circuit = compile_module(document)
    annotons = {obj['id']: obj for obj in walk(document) if 'participant' in obj and 'function' in obj}
    def requirements(selector):
        kind = selector['selector_type']
        if kind == 'GENE_PRODUCT':
            return {selector['gene_product']['term']['id'].removeprefix('UniProtKB:')}
        if kind == 'PROTEIN_COMPLEX':
            result = set()
            for unit in selector['protein_complex']['active_units']:
                result |= requirements(unit['participant'])
            return result
        assert kind == 'ANY_WITH_FUNCTION'
        # Unidentified native partners cannot be fulfilled by a protein's generic
        # E3 annotation or a foreign exemplar. This is a local evidence predicate,
        # not a claim that the general module compiler enforces partner identity.
        return None
    required = {key: requirements(a['participant']) for key, a in annotons.items()}
    cases = [
        ('empty', set(), False),
        ('Pelobacter complete mapped components', {'Q57102','Q57041','Q59658','Q60154'}, True),
        ('Bacillus complete mapped components', {'O31404','O34591','O31550','O34324'}, True),
        ('Pelobacter alpha alone', {'Q57102','Q59658','Q60154'}, False),
        ('Pelobacter beta alone', {'Q57041','Q59658','Q60154'}, False),
        ('Pelobacter missing E2', {'Q57102','Q57041','Q60154'}, False),
        ('Pelobacter missing E3', {'Q57102','Q57041','Q59658'}, False),
        ('Bacillus missing E3', {'O31404','O34591','O31550'}, False),
        ('foreign E3 does not complete Pelobacter', {'Q57102','Q57041','Q59658','O34324'}, False),
        ('foreign beta does not complete Pelobacter', {'Q57102','O34591','Q59658','Q60154'}, False),
        ('KT2440 unresolved native E3', {'Q88QE2','Q88QD9','Q88QE0','Q88QE1'}, False),
        ('KT2440 plus foreign AcoL still unresolved', {'Q88QE2','Q88QD9','Q88QE0','Q88QE1','Q60154'}, False),
        ('H16 unresolved native E3', {'P27745','P27746','P27747'}, False),
        ('PpG2 comparison is not a complete route', {'Q59696','Q59695'}, False),
        ('BdhA alone', {'Q88QE2'}, False),
    ]
    outcomes=[]
    for name, available, expected in cases:
        actual = is_satisfied(circuit, lambda atom: required[atom.node_id] is not None and required[atom.node_id] <= available)
        assert actual == expected, (name, actual, expected)
        outcomes.append({'case':name,'available':sorted(available),'satisfied':actual})
    # Role coverage separately demonstrates optional entry and complete native
    # conjunctions; asserting E3 here is hypothetical, not evidence of identity.
    for name, roles, expected in [
        ('hypothetical KT core bypasses BDH on acetoin', {'kt_e1','kt_e2','kt_e3'}, True),
        ('hypothetical KT missing E1', {'kt_bdh','kt_e2','kt_e3'}, False),
        ('mixed-species roles cannot complete native route', {'kt_e1','h16_e2','pc_e3'}, False),
    ]:
        actual=is_satisfied(circuit,lambda atom: atom.node_id in roles)
        assert actual == expected,(name,actual,expected)
        outcomes.append({'case':name,'roles':sorted(roles),'satisfied':actual})
    entry_node = document['module']['variant_sets'][0]['variants'][0]['parts'][0]['node']
    entry_circuit = compile_node(entry_node)
    # The compiler treats contexts as metadata. This explicit local predicate
    # checks the curated chemistry/conditions without pretending to infer metal
    # availability, expression or native electron transfer from sequence.
    def entry_holds(atom, available, conditions):
        need = required[atom.node_id]
        if need is None or not need <= available:
            return False
        if atom.node_id == 'kt_bdh':
            return 'NAD+' in conditions and bool({'R,R', 'meso'} & conditions)
        common = {'S,S', 'PQQ', 'electron_transfer_competent'}
        extra = {'Ca2+', 'PedE_expressed'} if atom.node_id == 'kt_pedE' else {'usable_La3+', 'PedH_expressed'}
        return common | extra <= conditions
    good_e = {'S,S', 'PQQ', 'electron_transfer_competent', 'Ca2+', 'PedE_expressed'}
    good_h = {'S,S', 'PQQ', 'electron_transfer_competent', 'usable_La3+', 'PedH_expressed'}
    for name, available, conditions, expected in [
        ('NAD-BDH R,R entry', {'Q88QE2'}, {'NAD+', 'R,R'}, True),
        ('NAD-BDH does not supply S,S entry', {'Q88QE2'}, {'NAD+', 'S,S'}, False),
        ('PedE calcium PQQ entry', {'Q88JH5'}, good_e, True),
        ('PedE protein without cofactors is insufficient', {'Q88JH5'}, set(), False),
        ('PedE missing PQQ is insufficient', {'Q88JH5'}, good_e - {'PQQ'}, False),
        ('PedH usable lanthanide PQQ entry', {'Q88JH0'}, good_h, True),
        ('PedH calcium does not replace lanthanide', {'Q88JH0'}, (good_h - {'usable_La3+'}) | {'Ca2+'}, False),
        ('PedH missing expression is insufficient', {'Q88JH0'}, good_h - {'PedH_expressed'}, False),
        ('PedH without electron transfer is insufficient', {'Q88JH0'}, good_h - {'electron_transfer_competent'}, False),
    ]:
        actual = is_satisfied(entry_circuit, lambda atom: entry_holds(atom, available, conditions))
        assert actual == expected, (name, actual, expected)
        outcomes.append({'case': name, 'available': sorted(available), 'conditions': sorted(conditions), 'entry_satisfied': actual})
    routes=enumerate_routes(circuit)
    assert len(routes)==7 and sorted(map(len,routes))==[3,3,3,3,4,4,4]
    print(yaml.safe_dump({'cases':outcomes,'routes_including_optional_entry':[[a.node_id for a in route] for route in routes]},sort_keys=False))

if __name__ == '__main__':
    main()
