"""Check stereo coverage and BaeAB assembly using the production Boolean compiler.

This is a capacity model, not a kinetic or growth prediction. The oracle supplies
native-implementation membership, complex assembly and resource availability;
the compiler does not infer those from family membership or GO terms.
"""
from pathlib import Path
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'bacterial_beta_aryl_ether_dimer_cleavage'
DATA = ROOT / 'analysis/module_audits' / SLUG


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    doc = yaml.safe_load((ROOT / 'modules' / f'{SLUG}.yaml').read_text())
    panel = yaml.safe_load((DATA / 'members.yaml').read_text())
    accession = {m['gene']: m['accession'] for m in panel}
    implementation = {m['accession']: ('F199' if m['organism'] == 'NOVAD' else 'ECOLI' if m['organism'] == 'ECOLI' else 'SYK-6') for m in panel}
    native = {s: {a for a, species in implementation.items() if species == s} for s in ['SYK-6', 'F199', 'ECOLI']}
    nodes = {n['id']: n for n in walk(doc['module']) if 'id' in n}
    acts = {a['id']: a for n in walk(doc['module']) for a in n.get('annotons', [])}
    required = {key: {n['gene_product']['term']['id'].split(':')[1] for n in walk(a['participant']) if 'gene_product' in n} for key, a in acts.items()}
    assert all(required.values())
    assert all(len({implementation[p] for p in products}) == 1 for products in required.values())
    bae = acts['f199_baeab_etherase']['participant']['protein_complex']['active_units']
    assert len(bae) == 2 and {x['stoichiometry'] for x in bae} == {'1'}
    assert {x['participant']['gene_product']['term']['id'] for x in bae} == {'UniProtKB:Q2G4B4', 'UniProtKB:Q2G4B5'}
    assert 'betaS-GS-HPV' not in str(acts['f199_baeab_etherase']['function']['products']), 'Do not silently assign BaeAB product epimer'
    # Source-defined chemical distinctions must survive structural edits.
    def chemicals(aid, field):
        return {x['preferred_term'] for x in acts[aid]['function'][field]}
    for gene, beta in [('ligE', 'R'), ('ligP', 'R'), ('ligF', 'S')]:
        aid = 'syk_' + gene + '_etherase'
        assert chemicals(aid, 'substrates') == {'beta' + beta + '-MPHPV', 'glutathione'}
        assert chemicals(aid, 'products') == {'beta' + ('S' if beta == 'R' else 'R') + '-GS-HPV', 'guaiacol'}
    f2 = acts['f199_Saro_2865_analogue_etherase']
    assert 'MPHPV' not in str(f2['function']['substrates'])
    assert 'vanillin' in chemicals(f2['id'], 'products')
    assert 'guaiacol' not in chemicals(f2['id'], 'products')
    assert not any(n.get('gene_product', {}).get('term', {}).get('id') == 'UniProtKB:Q2G4C2' for n in walk(nodes['f199_betaS_etherase']))
    cases = []

    def check(name, node, species, present, expected, resources=None, native_extract=False):
        resources = {'NAD+', 'glutathione'} if resources is None else resources
        def holds(atom):
            key = atom.node_id
            if not required[key] <= present or any(implementation[a] != species for a in required[key]):
                return False
            if native_extract and key == 'syk_ligO_oxidation':
                # PMID19542348: native ligO contribution was negligible; this
                # external phenotype constraint is not inferred from the tree.
                return False
            inputs = {s['preferred_term'] for s in acts[key]['function'].get('substrates', [])}
            return (inputs & {'NAD+', 'glutathione'}) <= resources
        observed = is_satisfied(compile_node(nodes[node]), holds)
        assert observed == expected, (name, expected, observed)
        cases.append({'case': name, 'node': node, 'implementation': species, 'present': sorted(present), 'resources': sorted(resources), 'native_extract_constraint': native_extract, 'expected': expected, 'observed': observed})

    full = SLUG
    check('Empty inventory is insufficient', full, 'SYK-6', set(), False)
    check('Complete SYK-6 stereo coverage', full, 'SYK-6', native['SYK-6'], True)
    for gene in ['ligD', 'ligO', 'ligL', 'ligN', 'ligE', 'ligP', 'ligF', 'ligG', 'ligQ']:
        check('SYK-6 loss of ' + gene, full, 'SYK-6', native['SYK-6'] - {accession[gene]}, gene not in ['ligF', 'ligQ'])
        check('One protein cannot supply complete route: ' + gene, full, 'SYK-6', {accession[gene]}, False)
    for pair in [('ligD', 'ligO'), ('ligL', 'ligN'), ('ligE', 'ligP'), ('ligG', 'ligQ')]:
        check('Loss of both ' + '/'.join(pair), full, 'SYK-6', native['SYK-6'] - {accession[g] for g in pair}, False)
    for genes in [('ligD', 'ligL', 'ligE', 'ligF', 'ligQ'), ('ligO', 'ligN', 'ligP', 'ligF', 'ligQ')]:
        check('Minimal enzyme-capacity set ' + '/'.join(genes), full, 'SYK-6', {accession[g] for g in genes}, True)
    for g in ['ligD', 'ligO']:
        check(g + ' alone covers both alphaR substrates', 'syk_alphaR_oxidation', 'SYK-6', {accession[g]}, True)
        check(g + ' cannot cover alphaS class', 'syk_alphaS_oxidation', 'SYK-6', {accession[g]}, False)
    for g in ['ligL', 'ligN']:
        check(g + ' alone covers both alphaS substrates', 'syk_alphaS_oxidation', 'SYK-6', {accession[g]}, True)
        check(g + ' cannot cover alphaR class', 'syk_alphaR_oxidation', 'SYK-6', {accession[g]}, False)
    check('LigG cannot replace native betaS-conjugate role', 'syk_release', 'SYK-6', {accession['ligG']}, False)
    check('LigQ covers both conjugate epimers', 'syk_release', 'SYK-6', {accession['ligQ']}, True)
    check('No NAD+ prevents entry', full, 'SYK-6', native['SYK-6'], False, {'glutathione'})
    check('No GSH prevents ether cleavage and release', full, 'SYK-6', native['SYK-6'], False, {'NAD+'})
    check('NADPH does not replace the assayed NAD+ resource', full, 'SYK-6', native['SYK-6'], False, {'NADPH', 'glutathione'})
    check('Native-extract full complement', full, 'SYK-6', native['SYK-6'], True, native_extract=True)
    check('LigO does not imply rescue of native ligD deletion', full, 'SYK-6', native['SYK-6'] - {accession['ligD']}, False, native_extract=True)
    check('F199 downstream proteins do not constitute mapped GGE entry', full, 'F199', native['F199'], False)
    late = 'f199_mphpv_to_monomers'
    check('Complete F199 downstream stereo coverage', late, 'F199', native['F199'], True)
    for g in ['Saro_2405', 'Saro_2091', 'Saro_2865', 'Saro_2873', 'Saro_2872', 'Saro_2595']:
        check('F199 loss of ' + g, late, 'F199', native['F199'] - {accession[g]}, g not in ['Saro_2091', 'Saro_2595'])
    for subunit in ['Saro_2873', 'Saro_2872']:
        check('No NaLigE and no ' + subunit, late, 'F199', native['F199'] - {accession['Saro_2405'], accession[subunit]}, False)
        check('Bae subunit alone: ' + subunit, 'f199_betaR_etherase', 'F199', {accession[subunit]}, False)
    check('BaeAB pair supplies betaR role', 'f199_betaR_etherase', 'F199', {accession['Saro_2873'], accession['Saro_2872']}, True)
    check('NaLigF2 alone supplies the assayed substituted-dimer reaction', 'f199_analogue_comparator', 'F199', {accession['Saro_2865']}, True)
    check('NaLigF2 analogue activity does not establish MPHPV turnover', 'f199_betaS_etherase', 'F199', {accession['Saro_2865']}, False)
    check('No F1 or F2 loses betaS role', late, 'F199', native['F199'] - {accession['Saro_2091'], accession['Saro_2865']}, False)
    check('Shared SF8 family does not turn F1/F2 into BaeAB', 'f199_betaR_etherase', 'F199', {accession['Saro_2091'], accession['Saro_2865']}, False)
    check('F199 requires GSH', late, 'F199', native['F199'], False, {'NAD+'})
    check('F199 downstream boundary does not require NAD+', late, 'F199', native['F199'], True, {'glutathione'})
    check('E. coli isolated Nu activity is not full dimer route', full, 'ECOLI', native['ECOLI'], False)
    check('E. coli directly assayed redox comparator', 'ecoli_nu_comparator', 'ECOLI', native['ECOLI'], True)
    check('Foreign YghU does not imply native F199 Nu rescue', late, 'F199', (native['F199'] - {accession['Saro_2595']}) | native['ECOLI'], False)
    check('Foreign etherases do not rescue native SYK-6 LigF', full, 'SYK-6', (native['SYK-6'] - {accession['ligF']}) | native['F199'], False)
    # Validate exact principal-intermediate handoffs, independently of satisfiability.
    edges = [e for n in walk(doc['module']) for e in n.get('connections', [])]
    expected = {(f'syk_alpha{a}_oxidation', f'syk_beta{b}_etherase') for a in ['R', 'S'] for b in ['R', 'S']}
    expected |= {('syk_betaR_etherase', 'syk_GSS_release'), ('syk_betaS_etherase', 'syk_GSR_release'), ('f199_Saro_2405_etherase', 'f199_GSS_release'), ('f199_baeab_etherase', 'f199_release'), ('f199_betaS_etherase', 'f199_GSR_release')}
    assert {(e['source'], e['target']) for e in edges} == expected
    assert len(edges) == len(expected) == 9
    assert all(e.get('evidence') and e['chaining_status'] == 'VERIFIED' for e in edges)
    report = {'cases_passed': len(cases), 'stereochemical_connections': len(edges), 'baeab_stoichiometry': 'one BaeA plus one BaeB', 'limits': ['Supplied substrate and resource capacities, not growth or flux.', 'Native-extract LigO constraint explicitly supplied from PMID19542348.', 'BaeAB product epimer is not assigned; NaGSTNu accepts both.', 'Legacy SPHPI LigG is linked to the assayed SYK-6 strain, with its source taxon unchanged.', 'NaLigF2 is tested on substituted analogues and is not assumed to supply MPHPV turnover.', 'Neither F199 upstream gene identities nor a native E. coli GGE route is inferred.'], 'cases': cases}
    (DATA / 'route-results.yaml').write_text(yaml.safe_dump(report, sort_keys=False))
    print(f"PASS: {len(cases)} capacity/assembly/stereo cases; {len(edges)} handoffs")


if __name__ == '__main__':
    main()
