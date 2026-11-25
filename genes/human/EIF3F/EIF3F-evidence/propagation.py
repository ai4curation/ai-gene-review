"""Literal database projection; no annotation decisions or network access."""
import collections,csv,hashlib,json,re,io
EXP = {'EXP', 'IDA', 'IPI', 'IMP', 'IGI', 'IEP', 'HDA', 'HMP', 'HGI', 'HEP'}
PAINT_ROWS = [3, 100, 108, 113, 117]
RULE_ROWS = [0, 2, 8, 10, 97, 104, 105, 107, 109, 110, 114, 116]
ALL_ROWS = sorted(PAINT_ROWS + RULE_ROWS + [112])

def source(a):
    return {k: v for k, v in a.items() if k != 'review'}

def slim_node(n):
    return {k: v for k, v in n.items() if k not in ['children'] and (not k.startswith('PANTHER_GO_')) and (k != 'PANTHER_PC')}

def compute():
    sources = read('inputs/source-objects.json')
    human = read('inputs/UniProt-O00303.json')
    seq = human['sequence']['value']
    if not len(seq) == 357:
        raise ValueError('Propagation input invariant failed')
    tree = read('propagation/' + 'PTHR10540-tree.json')
    msa = read('propagation/' + 'PTHR10540-msa.json')
    nodes = {}
    paths = {}

    def walk(n, path):
        k = n['persistent_id']
        if not k not in nodes:
            raise ValueError('Propagation input invariant failed')
        nodes[k] = n
        paths[k] = path + [k]
        children = n.get('children', {}).get('annotation_node', [])
        if isinstance(children, dict):
            children = [children]
        for c in children:
            walk(c, path + [k])
    walk(tree['search']['tree_topology']['annotation_node'], [])
    align = {s['persistent_id']: s['sequence'] for s in msa['search']['MSA_list']['sequence_info']}
    if not len(align) == len(nodes) == 747:
        raise ValueError('Propagation input invariant failed')
    products = {'O00303': human}
    for acc in ['Q9DCH4', 'O43060', 'Q9VN50']:
        products[acc] = read('propagation/' + f'UniProt-{acc}.json')
    identities = {}
    aligned = []
    for acc, u in products.items():
        matches = [n for n in nodes.values() if n.get('node_name', '').endswith('UniProtKB=' + acc)]
        if not len(matches) == 1:
            raise ValueError('Propagation input invariant failed')
        n = matches[0]
        s = align[n['persistent_id']]
        ungap = re.sub('[^A-Za-z]', '', s).upper()
        identities[acc] = dict(accession=u['primaryAccession'], taxon=u['organism']['taxonId'], organism=u['organism']['scientificName'], genes=u.get('genes'), official_sequence_length=len(u['sequence']['value']), official_sequence_sha256=hashlib.sha256(u['sequence']['value'].encode()).hexdigest(), alternative_products=[x for x in u.get('comments', []) if x['commentType'] == 'ALTERNATIVE PRODUCTS'], official_cross_references=[x for x in u['uniProtKBCrossReferences'] if x['database'] in ['MGI', 'FlyBase', 'PomBase', 'Ensembl', 'PANTHER', 'RefSeq']], tree_leaf=slim_node(n), tree_path=paths[n['persistent_id']], msa_alignment_columns=len(s), msa_ungapped_length=len(ungap), msa_sequence_sha256=hashlib.sha256(ungap.encode()).hexdigest(), msa_equals_official_displayed_sequence=ungap == u['sequence']['value'])
        aligned.append('>' + acc + '|' + n['persistent_id'] + '\n' + s + '\n')
    if not identities['O00303']['msa_equals_official_displayed_sequence']:
        raise ValueError('Propagation input invariant failed')
    target_id = identities['O00303']['tree_leaf']['persistent_id']
    target_path = paths[target_id]
    family = []
    headers = []
    path_records = []
    for ln, line in enumerate(text('inputs/IBD.gaf').splitlines(), 1):
        if line.startswith('!'):
            headers.append(line)
            continue
        fields = line.split('\t')
        if len(fields) > 6 and fields[1] in nodes:
            rec = dict(physical_line=ln, fields=fields, node=fields[1], qualifier=fields[3], term=fields[4], evidence=fields[6], donors=fields[7].split('|'), on_human_path=fields[1] in target_path)
            family.append(rec)
            if rec['on_human_path']:
                path_records.append(rec)
    loss = [x for x in family if 'NOT' in x['qualifier'].split('|') or x['evidence'] in ['IRD', 'IKR']]
    iba = []
    for i in PAINT_ROWS:
        a = sources[i]
        matches = [x for x in family if x['node'] == 'PTN000056988' and x['term'] == a['term']['id'] and (x['evidence'] == 'IBD')]
        if not (len(matches) == 1 and matches[0]['on_human_path']):
            raise ValueError('Propagation input invariant failed')
        literal = set(a['supporting_entities']) - {'PANTHER:PTN000056988'}
        if not literal == set(matches[0]['donors']):
            raise ValueError('Propagation input invariant failed')
        iba.append(dict(source_index=i, source=a, ibd=matches[0], assertion_node_position=target_path.index('PTN000056988'), descendant_path=target_path[target_path.index('PTN000056988'):], recorded_losses_on_descendant_path=[x for x in loss if x['node'] in target_path[target_path.index('PTN000056988'):]], donor_count_is_not_evidence_weight=True, target_self_donor_is_not_circular=True))
    queries = {}
    for acc in ['Q9DCH4', 'O43060', 'Q9VN50']:
        q = read('propagation/' + f'{acc}-QuickGO-page1.json')
        if not q['numberOfHits'] == len(q['results']):
            raise ValueError('Propagation input invariant failed')
        if not all((r['geneProductId'] == 'UniProtKB:' + acc for r in q['results'])):
            raise ValueError('Propagation input invariant failed')
        queries[acc] = q
    grows = list(csv.DictReader(io.StringIO(text('inputs/EIF3F-goa.tsv')), delimiter='\t'))
    human_annotations = [dict(goId=r['GO TERM'], goEvidence=r['GO EVIDENCE CODE'], reference=r['REFERENCE'], qualifier=r['QUALIFIER'], assignedBy=r['ASSIGNED BY'], date=r['DATE'], withFrom_raw=r['WITH/FROM'], source_goa_row=i) for i, r in enumerate(grows)]
    ontology = {x['id']: x for x in read('owner/GO-source-terms.json')['results']}
    if not {'id': 'GO:0002183', 'relation': 'is_a'} in ontology['GO:0006413']['children']:
        raise ValueError('Propagation input invariant failed')
    aliases = {'UniProtKB:O00303': 'O00303', 'MGI:MGI:1913335': 'Q9DCH4', 'PomBase:SPBC4C3.07': 'O43060', 'FB:FBgn0037270': 'Q9VN50'}
    grounding = []
    for x in iba:
        for donor in x['ibd']['donors']:
            acc = aliases[donor]
            term = x['source']['term']['id']
            records = human_annotations if acc == 'O00303' else queries[acc]['results']
            exact = [r for r in records if r['goId'] == term and r['goEvidence'] in EXP]
            descendant = [r for r in records if term == 'GO:0006413' and r['goId'] == 'GO:0002183' and (r['goEvidence'] in EXP)]
            grounding.append(dict(source_index=x['source_index'], ibd_donor=donor, mapped_product=acc, exact_experimental_code_records=exact, verified_descendant_experimental_code_records=descendant, scope='Experimental evidence codes and primary reference identifiers are recorded literally. Assay species, constructs and chemistry require the separately reserved original-paper review; not established by the evidence code alone.'))
    mouse_maps = []
    for i in RULE_ROWS + [112]:
        a = sources[i]
        if 'UniProtKB:Q9DCH4' in a.get('supporting_entities', []):
            matching = [r for r in queries['Q9DCH4']['results'] if r['goId'] == a['term']['id']]
            mouse_maps.append(dict(source_index=i, source=a, mouse_accession='Q9DCH4', mouse_protein_id='ENSMUSP00000033342.7', seed_protein_id_unversioned='ensembl:ENSMUSP00000033342', exact_term_current_records=matching, experimental_code_records=[r for r in matching if r['goEvidence'] in EXP], scope='Each aggregate IEA channel is retained separately; a donor identity match does not prove an assayed insert or the human activity.'))
    xrefs = collections.defaultdict(set)
    for x in human['uniProtKBCrossReferences']:
        xrefs[x['database']].add(x['id'])
    lineage = set(human['organism']['lineage'] + [human['organism']['scientificName']])
    fragment = 'Fragment' in str(human.get('proteinDescription', {}).get('flag', ''))

    def condition(c):
        typ = c['type']
        values = [v['value'] for v in c.get('conditionValues', [])]
        if typ == 'taxon':
            present = any((v in lineage for v in values))
            evidence = sorted(set(values) & lineage)
        elif typ == 'fragment':
            present = fragment
            evidence = {'proteinDescription.flag': human.get('proteinDescription', {}).get('flag'), 'fragment_flag_present': fragment}
        elif typ.endswith(' id') and typ[:-3] in ['HAMAP', 'InterPro', 'PANTHER', 'FunFam']:
            db = typ[:-3]
            present = any((v in xrefs[db] for v in values))
            evidence = sorted(set(values) & xrefs[db])
        else:
            raise ValueError('Unsupported main-rule predicate ' + typ)
        return dict(condition=c, positive_predicate=present, satisfied=not present if c.get('isNegative') else present, matched_target_values=evidence)
    rules = []
    for filename in ['UniRule-UR000106280.json', 'ARBA00088589.json', 'ARBA00033914.json', 'ARBA00026566.json']:
        r = read('propagation/' + filename)
        cs = []
        for i, s in enumerate(r['mainRule']['conditionSets']):
            c = [condition(x) for x in s['conditions']]
            cs.append(dict(condition_set_index=i, conditions=c, satisfied=all((x['satisfied'] for x in c))))
        go = [a['dbReference']['id'] for a in r['mainRule']['annotations'] if a.get('dbReference', {}).get('database') == 'GO']
        other_go = [dict(other_rule_index=i, term=a['dbReference']['id']) for i, x in enumerate(r.get('otherRules', [])) for a in x.get('annotations', []) if a.get('dbReference', {}).get('database') == 'GO']
        rules.append(dict(rule_id=r['uniRuleId'], information=r['information'], createdDate=r.get('createdDate'), modifiedDate=r.get('modifiedDate'), main_go_outputs=go, condition_sets=cs, matched_condition_sets=[x['condition_set_index'] for x in cs if x['satisfied']], other_rule_count=len(r.get('otherRules', [])), other_rule_go_outputs=other_go, source_rows=[i for i in RULE_ROWS if any((s.endswith(':' + r['uniRuleId']) for s in sources[i].get('supporting_entities', [])))], scope='Literal current rule applicability and GO outputs; no validation of biological truth or transfer breadth.'))
    ipr = read('propagation/' + 'InterPro-O00303-entries.json')
    if not (ipr['count'] == len(ipr['results']) and ipr['next'] is None):
        raise ValueError('Propagation input invariant failed')
    domains = []
    for x in ipr['results']:
        if x['metadata']['accession'] in ['IPR000555', 'IPR027531']:
            if not (len(x['proteins']) == 1 and x['proteins'][0]['accession'] == 'o00303' and (x['proteins'][0]['protein_length'] == 357)):
                raise ValueError('Propagation input invariant failed')
            m = read('propagation/' + ('InterPro-' + x['metadata']['accession'] + '.json'))['metadata']
            domains.append(dict(accession=m['accession'], name=m['name'], type=m['type'], go_terms=m['go_terms'], member_databases=m['member_databases'], target_match=x['proteins'][0], source_rows=[i for i in RULE_ROWS if 'InterPro:' + m['accession'] in sources[i].get('supporting_entities', [])], scope='Domain/family recognition and database mapping only; no target assay, metal dependence, or catalytic-residue conclusion.'))
    ec = []
    for ln, line in enumerate(text('propagation/ec2go.txt').splitlines(), 1):
        if line.startswith('EC:3.4.19.12 '):
            ec.append(dict(physical_line=ln, text=line))
    if not (len(ec) == 1 and 'GO:0004843' in ec[0]['text']):
        raise ValueError('Propagation input invariant failed')
    output = {'identity.json': dict(target_product=read('inputs/product-boundary.json'), products=identities, scope='Displayed database products and aligned reference sequences, not assayed constructs or interchangeable natural isoforms.'), 'paint-evidence.json': dict(tree_product=tree['search']['product'], msa_product=msa['search']['product'], tree_nodes=len(nodes), alignment_records=len(align), human_target=slim_node(nodes[target_id]), human_path=[slim_node(nodes[k]) for k in target_path], ibd_source_headers=headers, all_family_records=family, all_family_loss_records=loss, requested_iba_traces=iba, donor_grounding=grounding, scope='No donor-count weighting, no target-self circularity claim. No recorded loss in this release is not proof that a function is present in every descendant. PANTHER GO_SLIM summaries are not substituted for literal IBD records.'), 'rule-domain-evidence.json': dict(target_xrefs={k: sorted(v) for k, v in xrefs.items() if k in ['HAMAP', 'InterPro', 'PANTHER', 'FunFam']}, target_lineage=sorted(lineage), target_fragment_flag=fragment, rules=rules, domains=domains, ec2go=ec, ec_source_row=sources[10], scope='Separate sequence classification, rules, EC mapping and experimental claims; no annotation verdicts.'), 'donor-evidence.json': dict(complete_queries={acc: dict(numberOfHits=q['numberOfHits'], records=q['results']) for acc, q in queries.items()}, mouse_source_maps=mouse_maps, human_frozen_annotations=human_annotations, scope='Complete successful UniProt-mapped QuickGO captures. Failed literal MOD-ID query responses are retained separately and are not negative biological evidence.'), 'row-map.json': [dict(source_index=i, source=sources[i], evidence_files=['paint-evidence.json', 'identity.json'] if i in PAINT_ROWS else ['rule-domain-evidence.json', 'donor-evidence.json', 'identity.json']) for i in ALL_ROWS], 'target-donor-alignment.fasta': ''.join(aligned)}
    return output
