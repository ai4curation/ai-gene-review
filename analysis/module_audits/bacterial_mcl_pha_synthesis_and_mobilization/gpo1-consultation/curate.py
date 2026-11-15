"""Apply the source-grounded GPo1 review, retaining seeded source payloads."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
SCOPE = 'file:analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/gpo1-consultation/primary-scope.md'
IDENTITY = 'file:analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/literature-consultation/recommendations.md'
TERMS = {
    'GO:0016747': 'acyltransferase activity, transferring groups other than amino-acyl groups',
    'GO:0042621': 'poly(3-hydroxyalkanoate) biosynthetic process',
    'GO:0042620': 'poly(3-hydroxyalkanoate) metabolic process',
    'GO:0016788': 'hydrolase activity, acting on ester bonds',
}


def term(i):
    return {'id': i, 'label': TERMS[i]}


def support(ref, quote):
    return {'reference_id': ref, 'supporting_text': quote}


def reference(pmid, note):
    raw = (ROOT / f'publications/PMID_{pmid}.md').read_text()
    meta = yaml.safe_load(raw.split('---')[1])
    return {'id': f'PMID:{pmid}', 'title': meta['title'], 'findings': [],
            'reference_review': {'relevance': 'HIGH', 'correctness': 'VERIFIED',
                                 'review_notes': note}}


for gene in ['phaC1', 'phaC2', 'phaZ']:
    path = ROOT / f'genes/ECTOL/{gene}/{gene}-ai-review.yaml'
    doc = yaml.safe_load(path.read_text())
    rawref = f'file:ECTOL/{gene}/{gene}-uniprot.txt'
    references = doc['references'][:1]
    references[0]['reference_review'] = {
        'relevance': 'HIGH', 'correctness': 'VERIFIED',
        'review_notes': 'Correct annotation-provenance reference. Functional scope is judged from the target evidence, not the mapping label alone.'}
    references += [reference('1989978', 'Abstract and publication-linked curated UniProt statements read; external publisher/repository PDF attempts returned403. Official M58445 translations establish exact GPo1 protein identity; no unobserved purified assay is claimed.'),
                   reference('11133449', 'Protected normal cache is abstract-only; full institutional publisher-PDF copy was read for Methods/Results/Figs5–6. Native GPo1 turnover, leaky phaZ mutant and rescue with a C1/Z fragment; not purified single-enzyme chemistry.'),
                   {'id': rawref, 'title': f'UniProt {doc["id"]} curated record', 'findings': [],
                    'reference_review': {'relevance': 'HIGH', 'correctness': 'VERIFIED', 'review_notes': 'Publication-linked function and official strain/archive/domain classification used. Automated GO/pathway predictions are not independent experimental support.'}},
                   {'id': SCOPE, 'title': 'GPo1 identity and native PHA evidence', 'findings': []},
                   {'id': IDENTITY, 'title': 'MCL-PHA source and taxon consultation', 'findings': []}]
    doc['references'] = references
    doc['status'] = 'COMPLETE'
    if gene != 'phaZ':
        evidence = [support(rawref, 'Synthesizes poly(3-hydroxyalkanoates) (PHA), complements a mutant of P.putida that does not make PHA.')]
        doc['description'] = f'{gene} encodes one of the two class II poly(3-hydroxyalkanoate) synthases of strain GPo1, currently classified as Ectopseudomonas oleovorans. It polymerizes hydroxyacyl-CoA precursors into intracellular medium-chain-length storage polyester. The two synthases can realize the same polymerization role; the original locus study did not resolve a clear substrate-specificity difference between them.'
        doc['existing_annotations'][0]['review'] = {'summary': 'Acyltransferase chemistry is correct and can be refined to non-amino-acyl transfer.', 'action': 'MODIFY', 'reason': 'The publication-linked PHA synthesis function and class II PhaC classification support transfer of hydroxyacyl groups during polyester-chain extension. GO:0016747 is a supported descendant of GO:0016746; no more substrate-specific existing MF was found in the current searches.', 'proposed_replacement_terms': [term('GO:0016747')], 'supported_by': evidence}
        doc['existing_annotations'][1]['review'] = {'summary': 'Generalize the C4-specific PHB claim to the experimentally supported PHA biosynthetic process.', 'action': 'MODIFY', 'reason': 'GO:0042619 specifies a beta-hydroxybutyrate polymer. The target belongs to the class II PhaC group and the source-qualified GPo1 evidence concerns medium-chain-length PHA. The InterPro mapping and uncited UniProt PHB pathway line do not establish C4-only biosynthesis in this protein. GO:0042621 retains the supported biosynthetic role. This generalization is not a claim that C4 acceptance is impossible.', 'proposed_replacement_terms': [term('GO:0042621')], 'supported_by': evidence, 'propagation_review': {'root_cause': 'TERM_SCOPING_PROBLEM', 'failure_modes': ['GRANULARITY_MISMATCH'], 'source_entities': [{'source_id': x, 'source_status': 'SUPPORTS_SOURCE_BUT_NOT_TARGET', 'comment': 'PHA synthase-domain membership supports polymerization; it does not establish the C4-only product named by this GO term.'} for x in doc['existing_annotations'][1]['supporting_entities']]}}
        doc['core_functions'] = [{'description': 'Polymerizes (R)-3-hydroxyacyl-CoA precursors into medium-chain-length PHA storage polyester; one alternative synthase rather than an obligatory second sequential step.', 'molecular_function': term('GO:0016747'), 'directly_involved_in': [term('GO:0042621')], 'supported_by': evidence}]
        doc['proposed_new_terms'] = [{'proposed_name': 'poly(3-hydroxyalkanoate) synthase activity', 'proposed_definition': 'Catalysis of the transfer and polymerization of 3-hydroxyacyl groups from (R)-3-hydroxyacyl-CoA to a growing poly(3-hydroxyalkanoate) chain, releasing coenzyme A.', 'justification': 'The current GO searches recovered the PHA process but no matching specific polymerase MF. This proposal specifies the supported chemistry beyond GO:0016747; it is not an additional annotation row.', 'proposed_parent': term('GO:0016747'), 'supported_by': evidence}]
        doc['suggested_questions'] = [{'question': 'What distinct substrate preferences and quantitative native contributions do the two GPo1 synthases have across carbon sources?'}]
    else:
        evidence = [support(rawref, 'Complements a mutant that does not degrade PHA; might be a lipase.'), support(SCOPE, 'Results/Figs5–6 directly follow intracellular polymer decline.')]
        doc['description'] = 'PhaZ contributes to intracellular medium-chain-length poly(3-hydroxyalkanoate) mobilization in strain GPo1, currently classified as Ectopseudomonas oleovorans. It is an alpha/beta-hydrolase associated genetically with degradation of stored polyester. A leaky phaZ mutant retains polymer longer, and a phaC1/phaZ-containing fragment restores turnover-associated phenotypes. Polymer mobilization supports carbon and energy availability during nutrient limitation.'
        for row in doc['existing_annotations']:
            membrane = row['term']['id'] == 'GO:0016020'
            row['review'] = {'summary': 'Bilayer-membrane localization is unresolved.' if membrane else 'The specific glycerolipid substrate claim exceeds the target evidence.', 'action': 'UNDECIDED' if membrane else 'MARK_AS_OVER_ANNOTATED', 'reason': ('GO:0016020 requires a lipid bilayer or association with one. Positive intracellular PHA turnover does not determine a bilayer location; a PHA granule has a phospholipid monolayer. No target-specific localization or membrane-topology result was recovered. This is uncertainty about localization, not proof that membrane association is absent.' if membrane else 'The established target role is intracellular polyester mobilization. PHA ester bonds do not contain a glycerol backbone, and PTHR43798:SF5/ABHD6 classification alone does not establish the substrate-specific glycerolipid claim. Native GPo1 genetics and curated function support PHA turnover but do not measure monoacylglycerol hydrolysis or physiological acylglycerol catabolism. Mark this propagated specificity as overannotation while leaving possible secondary activity unresolved; no universal negative or ancestral loss is inferred.'), 'supported_by': evidence, 'propagation_review': {'root_cause': 'UNRESOLVED' if membrane else 'TERM_SCOPING_PROBLEM', 'failure_modes': [] if membrane else ['GRANULARITY_MISMATCH'], 'source_entities': [{'source_id': 'PANTHER:PTN002465558', 'source_status': 'UNRESOLVED', 'comment': 'The official node exists, but P26495 is absent from the cached reference tree. Exact target graft and losses cannot be independently resolved; broad family membership does not establish this target localization or substrate.'}]}}
        doc['core_functions'] = [{'description': 'Hydrolyzes ester bonds in intracellular medium-chain-length PHA during storage-polyester mobilization. The native genetic role is supported; exact product-size distribution and secondary lipid substrates remain unresolved.', 'molecular_function': term('GO:0016788'), 'directly_involved_in': [term('GO:0042620')], 'supported_by': evidence}]
        doc['proposed_new_terms'] = [{'proposed_name': 'medium-chain-length poly(3-hydroxyalkanoate) depolymerase activity', 'proposed_definition': 'Catalysis of the hydrolysis of ester bonds in medium-chain-length poly(3-hydroxyalkanoate), yielding shorter polyester chains and hydroxyalkanoate products.', 'justification': 'GO:0050527 specifies poly(3-hydroxyoctanoate) with products of size1–5, whereas the GPo1 evidence establishes turnover of native mixed medium-chain-length polyester without a product-resolved purified assay. The broader ester-hydrolase core is supported without asserting those unmeasured details.', 'proposed_parent': term('GO:0016788'), 'supported_by': evidence}]
        doc['suggested_questions'] = [{'question': 'Which oligomer and monomer products does purified GPo1 PhaZ release from defined native PHA substrates, and does it also hydrolyze monoacylglycerols?'}, {'question': 'Where is native GPo1 PhaZ localized relative to PHA granules and bilayer membranes?'}]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100))
    notes = ROOT / f'genes/ECTOL/{gene}/{gene}-notes.md'
    notes.write_text(f'# {gene}: GPo1 review, 2026-11-07\n\nIdentity and evidence: see `{SCOPE[5:]}` and the frozen literature consultation. PMID1989978 is abstract-only with publication-linked curated UniProt function; PMID11133449 full institutional copy was read for native turnover. Exact M58445 sequence equality is recorded in the literature identity proof. No data from KT2442 or PAO1 is represented as a direct GPo1 assay.\n\nAll seeded annotation payloads and order are preserved. No NEW row is added. The standalone description and core distinguish catalytic role from downstream survival and distinguish PHA chemistry from substrate-specific PHB or glycerolipid predictions. Proposed terms add vocabulary requests, not new source annotations.\n\nActual Falcon request via `just deep-research ECTOL {gene} --provider falcon` failed with HTTP403 authentication. The failure log is in `.cache/module-audit-logs/mcl-pha-20261107/gpo1-consultation/falcon-{gene}.log`; no provider report was fabricated. Manual primary/curated-source review supplies the evidence.\n\n`just paint-losses ECTOL {gene}` found the target absent from the cached reference tree; lineage losses cannot be assessed. The generic no-loss footer is not evidence of a resolved negative. Source membership is verified independently from UniProt/archive records; no PTN placement or loss is invented.\n')
