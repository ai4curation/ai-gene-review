"""Manual, explicitly indexed native E. coli nitrogen-PTS decisions."""
import copy
import json
import re
from pathlib import Path

import yaml

A = Path('analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107')
assert not (A / 'handoff.json').exists(), 'Frozen consultation; do not regenerate'
BASE = json.loads((A / 'seed-baseline.json').read_text())


def norm(s):
    return ' '.join(s.split())


def evidence(pmid, quote):
    assert norm(quote) in norm(Path(f'publications/PMID_{pmid}.md').read_text()), (pmid, quote)
    return {'reference_id': f'PMID:{pmid}', 'supporting_text': quote}


entry = evidence('10473571', 'EI(Ntr) was shown to phosphorylate NPr in vitro using either a [(32)P]PEP-dependent protein phosphorylation assay or a quantitative sugar phosphorylation assay.')
exchange = evidence('7876255', 'Purified IIANtr and NPr exchange phosphate appropriately with Enzyme I, HPr, and Enzyme IIA proteins of the phosphoenolpyruvate: sugar phosphotransferase system.')
sensor = evidence('23517463', 'Autophosphorylation by [32P]PEP of EINtr is inhibited by glutamine (Fig. 5A) and stimulated by α–ketoglutarate (Fig. 5B).')
trk = evidence('17289841', 'dephosphorylated EIIA Ntr interacts with TrkA, resulting in the inhibition of Trk-mediated K + uptake.')
kdp = evidence('19400808', 'Two-hybrid data and biochemical analysis revealed that IIA(Ntr) interacts with sensor kinase KdpD and stimulates kinase activity, resulting in increased levels of phosphorylated response regulator KdpE.')
lpx = evidence('21605551', 'dephosphorylated NPr of the nitrogen PTS interacts with Escherichia coli LpxD which catalyzes biosynthesis of lipid A of the lipopolysaccharide (LPS) layer.')
review_quote = evidence('41870250', 'Instead of a sugar substrate, the PTSNtr appears to carry out its regulatory roles through protein-protein interactions that primarily involve PtsN, although relatively few PtsN protein targets have been characterized.')
ycg = evidence('39742999', 'Copurification studies show that unphospho-PtsN specifically interacts with YcgO, and phosphorylation of PtsN leads to marked attenuation of the interaction.')


def term(id_, label):
    return {'id': id_, 'label': label}


PEP = term('GO:0008965', 'phosphoenolpyruvate-protein phosphotransferase activity')
NITROGEN = term('GO:0016775', 'phosphotransferase activity, nitrogenous group as acceptor')
INHIBITOR = term('GO:0141110', 'transporter inhibitor activity')
ACTIVATOR = term('GO:0030295', 'protein kinase activator activity')
PHOSPHORYLATION = term('GO:0006468', 'protein phosphorylation')
CYTOPLASM = term('GO:0005737', 'cytoplasm')
CYTOSOL = term('GO:0005829', 'cytosol')


def decision(summary, action, reason, support, replacement=None):
    d = {'summary': summary, 'action': action, 'reason': reason, 'supported_by': copy.deepcopy(support)}
    if replacement:
        d['proposed_replacement_terms'] = [replacement]
    return d


D = {}
for gene in ('ptsP', 'ptsO', 'ptsN'):
    p = f'genes/ECOLI/{gene}/{gene}-ai-review.yaml'
    d = yaml.safe_load(BASE[p]['text'])
    d['status'] = 'COMPLETE'
    D[gene] = d

D['ptsP']['description'] = ('PtsP (enzyme I-Ntr) is the soluble phosphoenolpyruvate-dependent entry enzyme of the E. coli nitrogen-regulatory PTS. It transfers phosphate through its phosphohistidine intermediate to NPr/PtsO, which passes it to the PtsN regulatory effector. Its N-terminal GAF domain couples this relay to glutamine and alpha-ketoglutarate: in the characterized E. coli system glutamine inhibits and alpha-ketoglutarate stimulates PtsP autophosphorylation. The relay regulates protein targets rather than constituting a sugar-specific membrane uptake complex.')
D['ptsO']['description'] = ('PtsO (NPr) is a soluble histidine phosphocarrier in the E. coli nitrogen-regulatory PTS. It receives phosphate from PtsP and transfers it to a histidine in PtsN, coupling the PEP-fed entry reaction to phosphostate-dependent regulatory outputs. Phosphate exchange with carbohydrate-PTS proteins has also been demonstrated in vitro. Dephosphorylated NPr interacts with the lipid A biosynthetic enzyme LpxD, linking its phosphostate to an additional regulatory output whose catalytic mechanism is less directly established than the relay.')
D['ptsN']['description'] = ('PtsN (enzyme IIA-Ntr) is the cytosolic terminal phosphoacceptor and regulatory effector of the E. coli PtsP–NPr phosphorelay. Its phosphorylation state controls interactions with potassium-homeostasis proteins. The unphosphorylated form inhibits Trk-mediated potassium uptake through interaction with TrkA, stimulates the sensor kinase KdpD, and inhibits the potassium/proton antiporter YcgO. These partner-specific effects connect metabolic input signals to potassium handling; PtsN is not itself a sugar permease or a KdpD-like kinase.')

for gene in D:
    uniprot = f'file:ECOLI/{gene}/{gene}-uniprot.txt'
    loc = {'reference_id': uniprot, 'supporting_text': 'Cytoplasm', 'record_section': ['CC:SUBCELLULAR LOCATION']}
    if gene == 'ptsP':
        r = D[gene]['existing_annotations']
        r[0]['review'] = decision('Soluble cytoplasmic relay entry enzyme.', 'ACCEPT', 'Curated UniProt localization and the soluble protein phosphotransfer mechanism agree. No membrane localization is inferred from the related sugar transport pathway.', [loc])
        r[1]['review'] = decision('PtsP catalyzes PEP-fed protein phosphorylation.', 'ACCEPT', 'The full E. coli primary measures PtsP autophosphorylation and downstream relay phosphorylation. The assay uses a PtsN K75D mobility-shift probe for downstream phosphostate; it does not make the reporter mutation a native PtsP feature.', [sensor, entry])
        for i in (2, 3, 4):
            r[i]['review'] = decision('Directly characterized PEP-to-NPr phosphotransfer.', 'ACCEPT', 'Purified E. coli PtsP phosphorylates NPr from PEP, matching the GO reaction. The IBD at PTN000532509 includes P37177 itself as an experimental anchor, which is valid rather than circular; shared chemistry does not imply identical acceptor specificity to PtsI. The retrieved tree places P37177 at PTN000532526 beneath this IBD; the cached assertion slice contains no negative rows. No ancestral loss is inferred.', [entry])
        r[5]['review'] = decision('Native sugar-uptake participation remains unresolved.', 'UNDECIDED', 'The domain mapping joins a regulatory relay enzyme to the coupled carbohydrate uptake process. Native PtsP preferentially serves NPr, but in-vitro coupling assays and exchange between PTS components preclude using specialization as proof that all sugar-related participation is impossible. A target-specific physiological sugar-transport role is not established by the present evidence.', [entry, exchange, review_quote])
        r[6]['review'] = decision('GlcNAc-specific PAINT propagation is not resolved for this target.', 'UNDECIDED', 'The cached IBD places GO0015764 at PTN000532509, also used for the well-supported broad PEP-transfer chemistry. An inherited sugar-specific process cannot be established solely from the shared entry-enzyme family. The target is characterized in the nitrogen relay; the retrieved tree places P37177/PTN000532526 under this broad43-leaf IBD, but a native E. coli PtsP GlcNAc-uptake role remains unestablished. This is not a donor-count or experimentally demonstrated loss argument.', [entry, exchange])
        r[7]['review'] = decision('Refine phosphorus-group transfer to the measured PEP-dependent reaction.', 'MODIFY', 'The broad transferase claim is correct; the accepted GO0008965 rows give the demonstrated donor and protein histidine acceptor chemistry.', [entry], PEP)
        D[gene]['core_functions'] = [{'description': 'Uses PEP to phosphorylate NPr through the PtsP phosphohistidine intermediate; the E. coli GAF input domain responds oppositely to glutamine and alpha-ketoglutarate.', 'molecular_function': PEP, 'directly_involved_in': [PHOSPHORYLATION], 'locations': [CYTOPLASM], 'supported_by': [entry, sensor]}]
    elif gene == 'ptsO':
        r = D[gene]['existing_annotations']
        r[0]['review'] = decision('Reported NPr–LpxD binding is biologically retained, but bare protein binding is uninformative.', 'REMOVE', 'Apply the repository bare-protein-binding policy, not a negative interaction judgment. The primary abstract explicitly reports dephosphorylated NPr binding LpxD and suggests inhibition from lipid-A/antibiotic phenotypes. Thus the physical interaction is positively supported, but GO0005515 provides no useful functional specificity. Full text is unavailable here, so no direct enzyme-inhibition replacement is manufactured and no claim is made that the binding is false.', [lpx])
        r[1]['review'] = decision('Cytoplasmic phosphocarrier.', 'ACCEPT', 'The curated soluble localization agrees with phosphotransfer between PtsP and PtsN; the carrier is not a sugar permease.', [loc])
        for i in (2, 3):
            r[i]['review'] = decision('NPr directly participates in protein phosphorylation.', 'ACCEPT', 'NPr is a reversible phosphate-transfer intermediate that does the transfer work, rather than merely a substrate with no downstream role. The purified-protein exchange and PEP-fed relay support protein phosphorylation. The primary abstracts support this positive claim but do not establish all native cross-system fluxes.', [entry, exchange])
        r[4]['review'] = decision('Carbohydrate-PTS process propagation needs native-context resolution.', 'UNDECIDED', 'PTN002135312 is the cached sugar-PTS IBD. Purified NPr can exchange phosphate with carbohydrate components, so an absolute absence claim would be unwarranted. The characterized native role is the PtsP–NPr–PtsN relay; in-vitro cross-reactivity does not alone establish coupled sugar uptake in vivo. The retrieved tree places P0A9N0/PTN002135339 under this35-leaf IBD alongside carbohydrate-HPr lineages. Native quantitative contribution remains unresolved; no cached negative assertion or invented loss node is used.', [exchange, entry])
        for i in (5, 6):
            r[i]['review'] = decision('Refine transferase to nitrogen-acceptor phosphotransfer.', 'MODIFY', 'NPr transfers phosphate to a protein histidine nitrogen in PtsN. GO0016775 narrows the acceptor chemistry without imposing ATP as donor. This does not assert that generic kinase activity is false: the current kinase definition says usually, not exclusively, ATP. No unsuitable ATP-specific histidine kinase or His-to-Asp response-regulator term is substituted.', [exchange, entry], NITROGEN)
        D[gene]['core_functions'] = [{'description': 'Transfers phosphoryl groups through its histidine intermediate between PtsP and PtsN; purified cross-system exchange is distinguished from the native regulatory relay.', 'molecular_function': NITROGEN, 'directly_involved_in': [PHOSPHORYLATION], 'locations': [CYTOPLASM], 'supported_by': [exchange, entry]}]
    else:
        r = D[gene]['existing_annotations']
        r[0]['review'] = decision('Refine the Trk-directed inhibitory claim to transporter inhibition.', 'MODIFY', 'The full source demonstrates phosphostate-dependent TrkA association and inhibition of Trk-mediated potassium uptake. GO0141110 directly describes binding-dependent transporter inhibition; the paper does not establish inhibition of a distinct catalytic enzyme activity by this interaction. This is a lateral functional correction, not a claim that the physiological inhibition is false.', [trk], INHIBITOR)
        r[1]['review'] = decision('TrkA binding mediates transporter inhibition.', 'MODIFY', 'Bare protein binding is less informative than the measured functional interaction: dephosphorylated PtsN associates with TrkA and inhibits potassium uptake. Retain this specific inhibitory function rather than discarding the physical interaction.', [trk], INHIBITOR)
        for i in (2, 3):
            r[i]['review'] = decision('KdpD interaction supports kinase activation.', 'MODIFY', 'The KdpD-binding claim is refined to the established functional consequence from the target-specific biochemical study. The high-throughput binary interaction source is supporting interaction context, not an independent assay of kinase activation; PMID19400808 supplies the functional evidence.', [kdp], ACTIVATOR)
        cyt = evidence('18304323', 'we identified 1103 proteins from the cytosolic fraction of the Escherichia coli strain MC4100.')
        r[4]['review'] = decision('Refine cytoplasm to the existing supported cytosol location.', 'MODIFY', 'The target already carries curated experimental cytosol evidence, consistent with a soluble relay effector and biochemical recovery from E. coli cytoplasmic extracts. Retain the more precise existing location; the proteomics cohort quote is not presented as a separately re-extracted target-specific supplementary-table row.', [loc, cyt], CYTOSOL)
        r[5]['review'] = decision('Retain the curated cytosol experimental annotation.', 'ACCEPT', 'The full primary profiles the MC4100 cytosolic fraction. The curated target-specific IDA is consistent with the soluble protein and native MG1655 interaction assays. The cohort-level excerpt documents assay scope; no claim is made that the target supplementary-table entry was independently re-extracted here.', [cyt, trk])
        r[6]['review'] = decision('The sugar-coupled transporter activity exceeds the supported Ntr-effector role.', 'MARK_AS_OVER_ANNOTATED', 'GO0008982 describes coupled transmembrane carbohydrate uptake and phosphorylation. An EIIA-related domain and reversible phosphotransfer do not by themselves establish that assembled sugar-transport activity for PtsN. Direct E. coli evidence supports phosphostate-dependent protein regulation. This judgment does not deny the purified phosphate exchange reported for PtsN or claim that every possible cross-system reaction is absent.', [exchange, review_quote, trk])
        r[7]['review'] = decision('Native carbohydrate-PTS process participation remains unresolved.', 'UNDECIDED', 'Domain ancestry and in-vitro exchange with carbohydrate proteins are real, but do not alone demonstrate native coupled sugar uptake by the Ntr effector. PtsN regulates other proteins, including potassium transporters and KdpD. A physiological sugar-transport contribution cannot be established or excluded from those results.', [exchange, review_quote])
        for i in (8, 9):
            r[i]['review'] = decision('E. coli PtsN directly activates KdpD kinase.', 'ACCEPT', 'The target-specific primary combines interaction and biochemical kinase assays and supports the unphosphorylated activating state. PTN002021052 has the same target P69829 as a legitimate experimental anchor, not circular evidence. The retrieved tree places P69829/PTN002021088 beneath this17-leaf IBD. This target judgment does not license kinase activation in all PtsN homologs or transfer the E. coli output sign to other species.', [kdp])
        D[gene]['core_functions'] = [
            {'description': 'Phosphostate-dependent inhibition of potassium transport: unphosphorylated PtsN binds TrkA and inhibits Trk uptake; separate E. coli work supports YcgO interaction/inhibition, with vesicle assays establishing YcgO antiport.', 'molecular_function': INHIBITOR, 'locations': [CYTOSOL], 'supported_by': [trk, ycg]},
            {'description': 'Unphosphorylated PtsN binds KdpD and stimulates its kinase activity, altering KdpE phosphorylation and potassium-uptake gene expression.', 'molecular_function': ACTIVATOR, 'locations': [CYTOSOL], 'supported_by': [kdp]},
        ]
    D[gene]['references'].append({'id': uniprot, 'title': f'UniProtKB curated record for E. coli {gene}', 'findings': [{'statement': 'Curated cytoplasmic localization supports the soluble relay context.', 'supporting_text': 'Cytoplasm', 'record_section': ['CC:SUBCELLULAR LOCATION']}]})

REFS = {
 '10473571': ('Purified E. coli PtsP phosphorylates NPr from PEP.', entry, 'PRIMARY_RESEARCH', 'Abstract-only; positive purified reaction and specificity are explicit. Detailed donor strain, all constructs and kinetic interpretation were not independently recovered.'),
 '7876255': ('Purified NPr and PtsN exchange phosphate with carbohydrate-PTS components.', exchange, 'PRIMARY_RESEARCH', 'Abstract-only. Positive exchange is explicit; do not infer physiological bypass dominance or a complete membrane transport reaction.'),
 '23517463': ('E. coli glutamine and alpha-ketoglutarate regulate PtsP autophosphorylation in opposite directions.', sensor, 'PRIMARY_RESEARCH', 'Full text read. Direct entry-enzyme assays are distinguished from downstream K75D PtsN mobility-shift reporter measurements and GAF-deletion constructs.'),
 '21605551': ('Dephosphorylated NPr interacts with E. coli LpxD.', lpx, 'PRIMARY_RESEARCH', 'Abstract-only; direct interaction is explicit, but the proposed catalytic inhibition mechanism is not promoted to an independently verified purified enzyme assay.'),
 '17289841': ('Dephosphorylated PtsN inhibits Trk-mediated potassium uptake through TrkA interaction.', trk, 'PRIMARY_RESEARCH', 'Full text read: E. coli K-12/MG1655 interaction, phosphostate and potassium accumulation evidence. Trk transport regulation is distinct from inhibition of a catalytic enzyme.'),
 '19400808': ('PtsN interacts with KdpD and increases kinase activity.', kdp, 'PRIMARY_RESEARCH', 'Abstract-only, but interaction and biochemical kinase assay are explicitly reported. Positive curator-supported E. coli activation is retained without reconstructing uninspected assay details.'),
 '39742999': ('E. coli YcgO antiport is measured in everted vesicles, separately from PtsN binding/phosphostate experiments.', ycg, 'PRIMARY_RESEARCH', 'Full text read. Native K-12 genetic context, overexpressed-protein copurification and everted-vesicle antiport are distinguished; a detailed CorC/RCK activation mechanism remains a model.'),
 '41870250': ('The regulatory PTS is distinguished from the coupled sugar-uptake machinery.', review_quote, 'REVIEW', 'Full 2026 review read as mechanistic synthesis and source discovery, not a new target experiment or universal family-output grant.'),
}
for gene, d in D.items():
    used = set(re.findall(r'PMID:(\d+)', yaml.safe_dump(d)))
    for pmid in sorted(used):
        refs = [r for r in d['references'] if r['id'] == f'PMID:{pmid}']
        pub = Path(f'publications/PMID_{pmid}.md').read_text()
        header = yaml.safe_load(pub.split('---', 2)[1])
        ref = refs[0] if refs else {'id': f'PMID:{pmid}', 'title': header['title']}
        if not refs:
            d['references'].append(ref)
        if not header.get('full_text_available'):
            ref['full_text_unavailable'] = True
        if pmid in REFS:
            statement, ev, kind, notes = REFS[pmid]
            ref['findings'] = [{'statement': statement, 'supporting_text': ev['supporting_text']}]
            ref['reference_review'] = {'relevance': 'HIGH', 'correctness': 'VERIFIED', 'review_notes': notes}
        elif pmid == '18304323':
            ref['findings'] = [{'statement': 'The study profiles E. coli MC4100 cytosolic proteins; the target IDA is retained with its curated attribution.', 'supporting_text': 'we identified 1103 proteins from the cytosolic fraction of the Escherichia coli strain MC4100.'}]
            ref['reference_review'] = {'relevance': 'MEDIUM', 'correctness': 'VERIFIED', 'review_notes': 'Full text read; cohort/strain verified. Target-specific supplementary peptide identification was not independently re-extracted.'}
        elif pmid == '24561554':
            ref['findings'] = [{'statement': 'The binary interaction study supports the inherited KdpD interaction assertion; the functional consequence is independently supported by PMID19400808.'}]
            ref['reference_review'] = {'relevance': 'MEDIUM', 'correctness': 'VERIFIED', 'review_notes': 'Full article describes large-scale binary interaction mapping; do not treat the network as an independent KdpD kinase assay.'}
    d['suggested_questions'] = [{'question': 'What fraction of native phosphotransfer follows the canonical PtsP–NPr–PtsN route versus condition-dependent cross-system exchange, and how does this affect the target-specific regulatory outputs?'}]
    if gene == 'ptsO':
        d['suggested_questions'].append({'question': 'Does NPr directly inhibit purified LpxD catalysis, and what interaction/phosphostate determinants separate that output from phosphate transfer to PtsN?'})
    for annotation in d['existing_annotations']:
        if annotation['evidence_type'] == 'IBA':
            node = next(x for x in annotation['supporting_entities'] if x.startswith('PANTHER:PTN'))
            accepted = annotation['review']['action'] == 'ACCEPT'
            annotation['review']['propagation_review'] = {
                'root_cause': 'NO_FAILURE_CORE' if accepted else 'UNRESOLVED',
                'source_entities': [{'source_id': node, 'source_label': node.split(':')[1],
                                     'source_status': 'SUPPORTS_TRANSFER' if accepted else 'UNRESOLVED',
                                     'comment': 'Exact target leaf descends from the asserted IBD in the retrieved PANTHER tree; raw PAINT join is preserved in the consultation. Target-supported chemistry is retained; native sugar-process scope remains unresolved where indicated. No donor-count or self-source circularity argument is used.'}],
                'residue_claims_not_applicable': 'No catalytic-residue loss assertion; function/context is assessed from target experiments and exact tree ancestry.'}
    path = Path(f'genes/ECOLI/{gene}/{gene}-ai-review.yaml')
    tmp = path.with_suffix('.yaml.tmp')
    tmp.write_text(yaml.safe_dump(d, sort_keys=False, width=105, allow_unicode=True))
    tmp.replace(path)
    notes = f'''# E. coli {gene}: native nitrogen-PTS review\n\n2026-11-07. All seeded annotation payloads and order are retained; every review decision was manually assigned. No NEW annotation was added. Core functions synthesize the demonstrated role and are not additional machine annotation rows.\n\n{d['description']}\n\nThe native reference relay is PtsP(P37177) → NPr/PtsO(P0A9N0) → PtsN(P69829). PMID10473571 and PMID7876255 have explicit positive biochemical abstracts, while PMID23517463 provides full primary entry-enzyme regulation and downstream reporter context. Reversible purified exchange is not a measured native bypass flux. No Pseudomonas FruB bypass, AceE inhibition, or Caulobacter SpoT result is transferred to E. coli.\n\nCurrent official GO definitions are archived in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/go-terms.json. GO0016775 captures a nitrogenous acceptor without requiring ATP. Generic kinase is not rejected merely because its definition says usually ATP. GO0141110 specifies transporter inhibition; TrkA/KdpD/YcgO outputs are kept chemically and experimentally distinct.\n\nPAINT raw IBD assertions were read. A self-source at a target-supported IBD is legitimate experimental grounding. Actual PANTHER tree ancestry was subsequently retrieved and joined to the cached IBD assertions in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/paint-join.json. All three E. coli target leaves descend from their asserted nodes; cached slices contain no negative rows. Sugar-process uncertainty concerns physiological function within those broad clades, not missing ancestry, donor counts or an invented loss. No MSA residue-loss inference was performed. The family-based control PtsI and carbohydrate HPr do not automatically become native nitrogen-relay members.\n\nThe shared real Falcon attempt failed HTTP403 authentication, recorded under analysis/module_audits/bacterial_nitrogen_regulatory_pts/acquisition-20261107/module-falcon-attempt.json and .log. These notes are manual research, not fabricated provider output. No duplicate provider attempt was requested.\n\n## Source-specific findings and access limits\n'''
    for ref in d['references']:
        if ref['id'].startswith('PMID:'):
            notes += f"\n- {ref['id']} — {ref['title']}. {ref['reference_review']['review_notes']}\n"
            for finding in ref.get('findings', []):
                notes += f"  {finding['statement']}"
                if finding.get('supporting_text'):
                    notes += ' Supporting source text: "' + finding['supporting_text'] + '"'
                notes += '\n'
    (path.parent / f'{gene}-notes.md').write_text(notes)
print('Curated three native E. coli reviews; original payloads remain in seed-baseline.json')
