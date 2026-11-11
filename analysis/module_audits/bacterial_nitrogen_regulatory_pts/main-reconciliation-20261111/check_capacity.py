"""Finite source-grounded native-route oracle around the production compiler.

No network, index build, or curated writes. Unknown combinations are unresolved;
false canonical capacity does not assert absence of separately evidenced bypass.
"""
from copy import deepcopy
import ast
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re

import yaml

from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[4]
OUTPUT = Path(__file__).resolve().parent
A = OUTPUT.parent
HERE = A / 'capacity-review-20261107'
MODULE = ROOT / 'modules/bacterial_nitrogen_regulatory_pts.yaml'
ROLES = {'entry': 'ptsp_enzyme_i_ntr', 'carrier': 'npr_phosphocarrier', 'terminal': 'ptsn_eiia_ntr'}
NODES = {'entry': 'ptsp_phosphate_entry', 'carrier': 'npr_phosphocarrier_relay', 'terminal': 'ptsn_terminal_regulator'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(value):
    return re.sub(r'\s+', ' ', value).strip()


def resolve(ref):
    if ref.startswith('PMID:'):
        return ROOT / ('publications/PMID_' + ref.split(':')[1] + '.md')
    if ref.startswith('file:'):
        return next((p for p in (ROOT / 'genes' / ref[5:], ROOT / ref[5:]) if p.exists()), ROOT / ref[5:])
    if ref.startswith('Reactome:'):
        return ROOT / ('reactome/' + ref.split(':')[1] + '.md')
    return None


def evidence_ok(item):
    p = ROOT / item['source']
    return p.is_file() and norm(item['quote']) in norm(p.read_text())


def authored_quotes(value, reference=None):
    if isinstance(value, dict):
        reference = value.get('reference_id', value.get('source_id', reference))
        if 'findings' in value:
            reference = value['id']
        if value.get('supporting_text'):
            yield reference, value['supporting_text']
        for child in value.values():
            yield from authored_quotes(child, reference)
    elif isinstance(value, list):
        for child in value:
            yield from authored_quotes(child, reference)


def reference_ids(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in ('id', 'reference_id', 'source_id', 'original_reference_id') and isinstance(child, str):
                if child.startswith(('PMID:', 'file:', 'Reactome:')):
                    yield child
            yield from reference_ids(child)
    elif isinstance(value, list):
        for child in value:
            yield from reference_ids(child)


def ancestors():
    result = {}
    for p in [A / 'module-revision-20261107/terminal-function-ancestry.json',
              A / 'psepk-review-20261107/npr-phosphotransfer-ancestors.json',
              A / 'psepk-review-20261107/go-ancestors.json']:
        d = json.loads(p.read_text())
        for term in d.get('response', d).get('results', []):
            result.setdefault(term['id'], set()).update(term.get('ancestors', []))
    return result


ANCESTORS = ancestors()


def supports(core, required):
    """Require an independently enabled, evidenced core MF; no GOA-only inference."""
    term = core.get('molecular_function', {}).get('id')
    if not term or core.get('negated') or core.get('retired') or not core.get('supported_by'):
        return False
    if not (term == required or required in ANCESTORS.get(term, set())):
        return False
    for item in core['supported_by']:
        p = resolve(item.get('reference_id', ''))
        if p is None or not p.exists():
            return False
        if item.get('supporting_text') and norm(item['supporting_text']) not in norm(p.read_text()):
            return False
    return True


def check_model(doc, ledger):
    """Audit declarations against independent source roles, not compiler truth alone."""
    parts = doc['module'].get('parts', [])
    assert len(parts) == 3 and not doc['module'].get('variant_sets'), 'Three canonical roles required'
    chemistry = ledger['role_chemistry']
    seen = set()
    for part in parts:
        node = part['node']
        role = next((r for r, name in NODES.items() if node['id'] == name), None)
        assert role and not part.get('optional'), 'Required role missing/optional'
        seen.add(role)
        assert len(node.get('annotons', [])) == 1
        annoton = node['annotons'][0]
        assert annoton['id'] == ROLES[role]
        assert annoton['function']['term']['id'] == chemistry[role], 'Wrong chemical/output genus'
        assert annoton['participant']['selector_type'] == 'FAMILY'
        family = annoton['participant']['family']
        expected = {edge['donor'] for edge in ledger['native_edges'] if edge['donor_role'] == role}
        expected |= {edge['acceptor'] for edge in ledger['native_edges'] if edge['acceptor_role'] == role}
        actual = {m['term']['id'].removeprefix('UniProtKB:') for m in family['representative_members']}
        assert actual == expected, 'Representative scope changed without supporting partner evidence'
        if role == 'terminal':
            assert family['term'] == {'id': 'PANTHER:PTHR47738:SF1', 'label': 'NITROGEN REGULATORY PROTEIN'}
        else:
            assert not family.get('term') and not family.get('family_terms'), 'Mixed family subdivisions are not native-route selectors'
        assert annoton.get('evidence') and annoton['function'].get('evidence'), 'Missing role/function evidence'
        assert any(e.get('supporting_text') for e in annoton['function']['evidence']), 'No quoted function anchor'
        assert any(e.get('source_id') == anchor['source_id'] and norm(anchor['quote']) in norm(e.get('supporting_text','')) for e in annoton['function']['evidence'] for anchor in ledger['function_anchors'][role]), 'Function evidence lacks an independently reviewed mechanistic anchor'
        for ref, quote in authored_quotes(annoton):
            p = resolve(ref or '')
            assert p and p.exists() and norm(quote) in norm(p.read_text()), ('Source mismatch', ref)
    assert seen == set(ROLES)
    expected_edges = {(NODES['entry'], NODES['carrier'], 'PROVIDES_INPUT_FOR'),
                      (NODES['carrier'], NODES['terminal'], 'PROVIDES_INPUT_FOR')}
    actual_edges = {(e['source'], e['target'], e['connection_type']) for e in doc['module'].get('connections', [])}
    assert actual_edges == expected_edges, 'Native phosphate-flow declarations changed'
    assert doc['module']['context']['taxa'][0]['term']['id'] == 'NCBITaxon:1224'
    assert doc['module']['context'].get('conditions'), 'Native-coherence applicability context absent'
    circuit = compile_module(doc)
    assert len(list(iter_atoms(circuit))) == 3
    return circuit


def evaluate(doc, ledger, genes, available, context, ignore_taxon=False):
    circuit = compile_module(doc)
    available = set(available)
    atom_roles = {v: k for k, v in ROLES.items()}
    valid_edges = [e for e in ledger['native_edges'] if e['organism'] == context
                   and e['relation'] == 'native_relay_transfer' and evidence_ok(e['evidence'])]
    native = {e[side] for e in valid_edges for side in ('donor', 'acceptor')}
    qualified = {}
    for atom in iter_atoms(circuit):
        role = atom_roles.get(atom.node_id)
        witnessed = set()
        for e in valid_edges:
            if e['donor_role'] == role:
                witnessed.add(e['donor'])
            if e['acceptor_role'] == role:
                witnessed.add(e['acceptor'])
        choices = []
        for accession in available & witnessed & set(atom.uniprots):
            gene = genes.get(accession)
            if not gene:
                continue
            if not ignore_taxon and gene['taxon']['id'] != ledger['members'][accession]['taxon']:
                continue
            if not all(any(supports(core, mf) for core in gene.get('core_functions', [])) for mf in atom.function_ids):
                continue
            if not atom.function_ids:
                continue
            if atom.family_ids:
                raw = (ROOT / ledger['members'][accession]['uniprot']).read_text()
                if not all(f.replace('PANTHER:', '') in raw for f in atom.family_ids):
                    continue
            if role == 'terminal' and not evidence_ok(ledger['terminal_outputs'][accession]):
                continue
            choices.append(accession)
        qualified[atom.node_id] = choices
    compiled = is_satisfied(circuit, lambda a: bool(qualified.get(a.node_id)))
    # Partner continuity is an independent graph witness, not a second spelling of
    # the three-atom conjunction: edges must share the same actual carrier.
    witnesses = []
    for left in valid_edges:
        for right in valid_edges:
            if (left['donor_role'], left['acceptor_role'], right['donor_role'], right['acceptor_role']) != ('entry','carrier','carrier','terminal'):
                continue
            if left['acceptor'] != right['donor']:
                continue
            triple = [left['donor'], left['acceptor'], right['acceptor']]
            if all(protein in qualified.get(ROLES[role], []) for role, protein in zip(('entry','carrier','terminal'), triple)):
                witnesses.append(triple)
    supported = compiled and bool(witnesses)
    status = 'SUPPORTED' if supported else 'INCOMPLETE_CANONICAL' if available <= native else 'UNRESOLVED'
    return {'status': status, 'supported': supported, 'compiler': compiled, 'witnesses': witnesses, 'qualified': qualified}



def formatting_successors():
    path = A / 'helper-formatting-20261107/successor.json'
    receipt = json.loads(path.read_text())
    class Normalize(ast.NodeTransformer):
        def __init__(self, renamed=None):
            self.renamed = renamed

        def visit_Name(self, node):
            if self.renamed and node.id == self.renamed:
                node.id = 'l'
            return node

        def visit_arg(self, node):
            if self.renamed and node.arg == self.renamed:
                node.arg = 'l'
            return node

        def visit_Import(self, node):
            return [ast.Import(names=[alias]) for alias in node.names if alias.name != 'copy']

    for item in receipt['scripts']:
        old = ROOT / item['original_archive']
        new = ROOT / item['path']
        assert digest(old) == item['original_sha256']
        assert digest(new) == item['current_sha256']
        before = Normalize().visit(ast.parse(old.read_text()))
        after = Normalize(item['name_cleanup']).visit(ast.parse(new.read_text()))
        assert ast.dump(before) == ast.dump(after), item['path']
    return receipt, {item['path']: item for item in receipt['scripts']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=OUTPUT, help='Additive result directory; use a new directory for post-release reruns.')
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    ledger = json.loads((HERE / 'evidence-ledger.json').read_text())
    doc = yaml.safe_load(MODULE.read_text())
    genes = {acc: yaml.safe_load((ROOT / m['review']).read_text()) for acc, m in ledger['members'].items()}
    for edge in ledger['native_edges']:
        assert evidence_ok(edge['evidence'])
    assert all(evidence_ok(e) for e in ledger['terminal_outputs'].values())
    assert evidence_ok(ledger['bypass'])
    circuit = check_model(doc, ledger)
    cases = []
    triples = {'ECOLI':['P37177','P0A9N0','P69829'], 'PSEPK':['Q88CN5','Q88PA2','Q88PA0'],
               'CAUVN':['A0A0H3C823','A0A0H3C344','A0A0H3CDT8']}

    def case(name, available, context, expected, **options):
        result = evaluate(doc, ledger, genes, available, context, **options)
        assert result['status'] == expected, (name, result, expected)
        cases.append({'name': name, 'available': available, 'context': context, 'expected': expected, **result})

    # Three native positives and all 24 foreign triplets: insufficient evidence is
    # not a claim of chemically impossible cross-species phosphotransfer.
    for combination in itertools.product(triples, repeat=3):
        available = [triples[taxon][i] for i, taxon in enumerate(combination)]
        expected = 'SUPPORTED' if len(set(combination)) == 1 else 'UNRESOLVED'
        case('triplet_' + '_'.join(combination), available, combination[0], expected)
    for context, triple in triples.items():
        for i, role in enumerate(('entry','carrier','terminal')):
            case(context + '_missing_' + role, triple[:i] + triple[i+1:], context, 'INCOMPLETE_CANONICAL')
            case(context + '_only_' + role, [triple[i]], context, 'INCOMPLETE_CANONICAL')
        case(context + '_empty', [], context, 'INCOMPLETE_CANONICAL')
    case('same_MF_carbohydrate_EI', ['P08839','P0A9N0','P69829'], 'ECOLI', 'UNRESOLVED')
    case('same_MF_Ecoli_HPr', ['P37177','P0AA04','P69829'], 'ECOLI', 'UNRESOLVED')
    case('same_SF2_Bacillus_HPr', ['P37177','P08877','P69829'], 'ECOLI', 'UNRESOLVED')
    case('same_SF2_Bacillus_HPr_without_taxon_filter', ['P37177','P08877','P69829'], 'ECOLI', 'UNRESOLVED', ignore_taxon=True)
    case('unknown_carrier', ['P37177','UNKNOWN','P69829'], 'ECOLI', 'UNRESOLVED')
    case('fructose_bypass_context_is_not_canonical_entry', ['Q88PA2','Q88PA0'], 'PSEPK', 'INCOMPLETE_CANONICAL')
    case('partial_route_with_unknown_terminal_output', ['P37177','P0A9N0','UNKNOWN'], 'ECOLI', 'UNRESOLVED')
    # Controls really have the relevant chemistry; excluding them must not be
    # implemented by falsifying their core activities.
    chemical_controls = {acc: any(supports(c, mf) for c in genes[acc]['core_functions']) for acc, mf in
                         [('P08839','GO:0008965'), ('P0AA04','GO:0016775'), ('P08877','GO:0016775')]}
    assert all(chemical_controls.values())
    classification_controls = {}
    for accession, expected in [('P37177','PTHR46244:SF1'),('Q88CN5','PTHR46244:SF1'),('A0A0H3C823','PTHR46244:SF6'),('P08839','PTHR46244:SF6'),('P0A9N0','PTHR33705:SF2'),('Q88PA2','PTHR33705:SF2'),('A0A0H3C344','PTHR33705:SF2'),('P08877','PTHR33705:SF2'),('P0AA04','PTHR33705:SF1'),('P69829','PTHR47738:SF1'),('Q88PA0','PTHR47738:SF1'),('A0A0H3CDT8','PTHR47738:SF1')]:
        raw = (ROOT / ledger['members'][accession]['uniprot']).read_text()
        assert 'DR   PANTHER; ' + expected + ';' in raw
        classification_controls[accession] = expected
    ontology_controls = {term: 'GO:0098772' in ANCESTORS[term] for term in ('GO:0030295','GO:0004857','GO:0141110')}
    assert all(ontology_controls.values())
    assert 'GO:0016301' not in ANCESTORS['GO:0016775']

    mutations = []
    def mutation(name, change):
        altered = deepcopy(doc)
        change(altered)
        try:
            check_model(altered, ledger)
        except (AssertionError, KeyError, ValueError) as error:
            mutations.append({'name': name, 'detected': True, 'reason': str(error)})
        else:
            raise AssertionError('Undetected model mutation: ' + name)
    mutation('carrier_optional', lambda d: d['module']['parts'][1].update(optional=True))
    mutation('missing_entry', lambda d: d['module']['parts'].pop(0))
    mutation('missing_terminal', lambda d: d['module']['parts'].pop(2))
    for index, term, name in [(0,'GO:0004673','ATP_entry'),(1,'GO:0009927','hybrid_kinase_carrier'),(2,'GO:0030295','universal_kinase_output')]:
        mutation(name, lambda d, i=index, t=term: d['module']['parts'][i]['node']['annotons'][0]['function']['term'].update(id=t))
    for index, family, name in [(0,'PANTHER:PTHR46244:SF6','mixed_SF6_entry'),(1,'PANTHER:PTHR33705:SF2','mixed_SF2_carrier'),(2,'PANTHER:PTHR47738','broad_terminal_family')]:
        mutation(name, lambda d, i=index, f=family: d['module']['parts'][i]['node']['annotons'][0]['participant']['family'].update(term={'id':f,'label':'test'}))
    mutation('reversed_phosphate_edge', lambda d: d['module']['connections'][0].update(source=NODES['carrier'],target=NODES['entry']))
    mutation('deleted_phosphate_edge', lambda d: d['module']['connections'].pop())
    mutation('wrong_context_taxon', lambda d: d['module']['context']['taxa'][0]['term'].update(id='NCBITaxon:2'))
    mutation('absent_native_context', lambda d: d['module']['context'].pop('conditions'))
    mutation('unanchored_carrier_function', lambda d: d['module']['parts'][1]['node']['annotons'][0]['function'].update(evidence=[]))
    mutation('invented_function_quote', lambda d: d['module']['parts'][0]['node']['annotons'][0]['function']['evidence'][0].update(supporting_text='Invented ATP-dependent mannose membrane transport'))
    mutation('control_substituted_as_representative', lambda d: d['module']['parts'][0]['node']['annotons'][0]['participant']['family']['representative_members'][0]['term'].update(id='UniProtKB:P08839'))
    mutation('genuine_strain_quote_does_not_establish_function', lambda d: d['module']['parts'][1]['node']['annotons'][0]['function'].update(evidence=[{'source_id':'PMID:27109061','supporting_text':'All Caulobacter crescentus strains used in this study are derived from the synchronizable wild-type strain NA1000'}]))
    mutation('genuine_kinase_quote_does_not_establish_carrier_transfer', lambda d: d['module']['parts'][1]['node']['annotons'][0]['function'].update(evidence=[{'source_id':'PMID:19400808','supporting_text':'stimulates kinase activity'}]))
    mutation('single_protein_selector', lambda d: d['module']['parts'][1]['node']['annotons'][0]['participant'].update(selector_type='GENE_PRODUCT'))

    sensitivities = []
    for context, triple in triples.items():
        for accession in triple:
            altered = deepcopy(genes)
            altered[accession]['core_functions'] = []
            r = evaluate(doc, ledger, altered, triple, context)
            assert not r['supported']
            sensitivities.append({'name':'missing_core_'+accession, 'detected':True})
    for i, edge in enumerate(ledger['native_edges']):
        altered = deepcopy(ledger)
        altered['native_edges'][i]['evidence']['quote'] = 'Unsupported phosphate relay claim'
        assert not evaluate(doc, altered, genes, triples[edge['organism']], edge['organism'])['supported']
        sensitivities.append({'name':f'broken_native_edge_{i}', 'detected':True})
    for context, triple in triples.items():
        altered = deepcopy(genes)
        core = altered[triple[1]]['core_functions'][0]
        core['contributes_to_molecular_function'] = core.pop('molecular_function')
        assert not evaluate(doc, ledger, altered, triple, context)['supported']
        sensitivities.append({'name':context+'_only_complex_contribution_not_independent_carrier', 'detected':True})
    for context, triple in triples.items():
        altered = deepcopy(ledger)
        altered['terminal_outputs'][triple[2]]['quote'] = 'Unsupported terminal output'
        assert not evaluate(doc, altered, genes, triple, context)['supported']
        sensitivities.append({'name':context+'_missing_output_evidence', 'detected':True})
    # Demonstrate actual production compiler limitations rather than hide them.
    mixed = {'P37177','Q88PA2','A0A0H3CDT8'}
    naive_mixed = is_satisfied(circuit, lambda atom: bool(set(atom.uniprots) & mixed))
    assert naive_mixed and not evaluate(doc, ledger, genes, mixed, 'ECOLI')['supported']
    disconnected = deepcopy(doc)
    disconnected['module']['connections'] = []
    assert is_satisfied(compile_module(disconnected), lambda atom: bool(set(atom.uniprots) & set(triples['ECOLI'])))

    sources = {}
    quote_count = 0
    documents = {str(MODULE.relative_to(ROOT)): doc}
    documents.update({m['review']: genes[acc] for acc, m in ledger['members'].items()})
    for family in ('PTHR46244','PTHR33705','PTHR47738'):
        path = f'interpro/panther/{family}/{family}-review.yaml'
        documents[path] = yaml.safe_load((ROOT / path).read_text())
    for path, data in documents.items():
        sources[path] = digest(ROOT / path)
        for ref in set(reference_ids(data)):
            p = resolve(ref)
            assert p is not None and p.exists(), ('Missing current source', path, ref)
            sources[str(p.relative_to(ROOT))] = digest(p)
        for ref, quote in authored_quotes(data):
            p = resolve(ref or '')
            assert p is not None and p.exists() and norm(quote) in norm(p.read_text()), ('Quotation', path, ref, quote)
            quote_count += 1
    # Historical releases remain immutable. This successor evaluates current
    # evidence and the unchanged biological cases; it does not pretend that
    # deliberately reviewed successor files retain old release hashes.
    releases = {}
    successor_receipt = {"mode": "current-source validation after recorded review follow-up",
                         "historical_checker_sha256": digest(HERE / "check_capacity.py")}
    for path, sha in sources.items():
        assert digest(ROOT / path) == sha, ('Source changed during current check', path)
    row_counts = {'rows':sum(len(g['existing_annotations']) for g in genes.values()),
                  'historical_NEW':sum(a['review']['action']=='NEW' for g in genes.values() for a in g['existing_annotations']),
                  'retired_NEW':sum(a['review']['action']=='NEW' and bool(a.get('retired')) for g in genes.values() for a in g['existing_annotations'])}
    assert row_counts == {'rows':108,'historical_NEW':12,'retired_NEW':4}
    output = {'result':'PASS','row_counts':row_counts,'cases':cases,'model_mutations':mutations,'evidence_sensitivities':sensitivities,
              'chemical_controls':chemical_controls,'ontology_controls':ontology_controls,'classification_controls':classification_controls,
              'compiler_limit_witnesses':{'mixed_representative_triplet_passes_naive_compiler':naive_mixed,'deleted_connections_do_not_change_static_compiler':True},
              'current_quote_occurrences_checked':quote_count,'reviewed_members':len(genes),
              'source_dependencies':dict(sorted(sources.items())),'verified_frozen_releases':releases,'verified_helper_successors':successor_receipt,
              'module_sha256':digest(MODULE),
              'counts':{'cases':len(cases),'model_mutations':len(mutations),'evidence_sensitivities':len(sensitivities)}}
    (args.output_dir / 'results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'result':output['result'],**output['counts'],'quotes':quote_count,'sources':len(sources)},indent=2))


if __name__ == '__main__':
    main()
