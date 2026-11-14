"""Bounded manual curation; original source payloads are checked before writing."""
from pathlib import Path
import json
import os
import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
BASE = json.loads((AUDIT / 'baseline.json').read_text())
PUB = {p: (ROOT / f'publications/PMID_{p}.md').read_text() for p in ('27109061', '26489861')}
Q = {
 'ei': 'we performed in vitro autophosphorylation assays with a purified fraction containing EINtr using [32P]PEP as a phosphoryl donor, in the presence or absence of glutamine.',
 'gln': 'We found that autophosphorylation of EINtr was strongly reduced by glutamine',
 'loci': 'Besides ptsP (EINtr), we found a unique HPr homologue (ptsH, CCNA_00241) and another nitrogen-related PTSNtr component, EIIANtr (ptsN, CCNA_03710).',
 'relay': 'the expression of Caulobacter ptsH (HPr) from the inducible pBAD promoter (pBAD33-ptsHCc) in a Δnpr background restored the interaction between EIIANtr and SpoT only when arabinose was added to the medium',
 'indirect': 'no interaction was detected between HPr (or HPrH18A) and SpoT (or SpoTD81G) on MacConkey maltose agar plates',
 'inhibit': 'these findings demonstrate that EIIANtr∼P inhibits hydrolase activity of SpoT to modulate (p)ppGpp accumulation upon nitrogen availability.',
 'binding': 'both the wild-type EIIANtr (ptsN) and the phosphomimetic mutant of EIIANtr (EIIANtrH66E) were able to interact with SpoT versions',
 'transport': 'In contrast to its EIIA paralog, the EIIANtr component is not associated with permeases, but rather carries out regulatory functions, by interacting with its target(s).',
 'strain': 'All Caulobacter crescentus strains used in this study are derived from the synchronizable wild-type strain NA1000',
 'complex': 'EINtr and SpoT are found in the same protein complex during stationary phase',
 'coip': 'Coimmunoprecipitation (Co−IP) of PtsP with green fluorescent protein (GFP)-tagged SpoT from a GFP-TRAP affinity matrix',
}
for key, quote in Q.items():
    assert quote in PUB['26489861' if key == 'coip' else '27109061'], key

def support(key):
    return {'reference_id': 'PMID:' + ('26489861' if key == 'coip' else '27109061'), 'supporting_text': Q[key]}

def review(action, summary, reason, keys, replacement=None):
    result = {'summary': summary, 'action': action, 'reason': reason,
              'supported_by': [support(k) for k in keys]}
    if replacement:
        result['proposed_replacement_terms'] = [replacement]
    return result

EI = {'id': 'GO:0008965', 'label': 'phosphoenolpyruvate-protein phosphotransferase activity'}
HPR = {'id': 'GO:0016775', 'label': 'phosphotransferase activity, nitrogenous group as acceptor'}
INHIB = {'id': 'GO:0004857', 'label': 'enzyme inhibitor activity'}
CYTO = {'id': 'GO:0005737', 'label': 'cytoplasm'}
GENERIC_SUGAR = ('The term describes coupled sugar uptake/phosphorylation, not every PEP-dependent regulatory phosphorelay. '
 'The native NA1000 study identifies a nitrogen-responsive PtsP–HPr–PtsN regulatory system and separates it from permease-coupled sugar PTS. '
 'The source mapping extends shared PTS chemistry or architecture into a substrate/transport role not established for this target. '
 'MARK_AS_OVER_ANNOTATED judges that over-specific assignment; it is not a claim that every possible secondary carbohydrate role has been experimentally excluded.')
DESCRIPTIONS = {
 'ptsP': 'PtsP (enzyme I Ntr; CCNA_00892) initiates a nitrogen-responsive phosphotransfer relay in Caulobacter vibrioides NA1000. It uses phosphoenolpyruvate to phosphorylate a protein histidine and supplies the HPr–PtsN signaling pathway that controls SpoT-dependent (p)ppGpp accumulation and cell-cycle progression. NA1000 PtsP-containing fractions show glutamine-sensitive autophosphorylation; a GAF-domain L83Q variant loses this response. PtsP also associates with SpoT in cellular affinity-purification experiments. These results connect nitrogen availability to alarmone signaling without establishing direct glutamine binding or an isolated PtsP–SpoT regulatory reaction.',
 'ptsH': 'HPr (CCNA_00241) is the small histidine phosphocarrier of the nitrogen-responsive PtsP–HPr–PtsN relay in Caulobacter vibrioides NA1000. It accepts and transfers phosphoryl groups through a conserved histidine and couples upstream PtsP signaling to PtsN. Native genetic and phosphostate studies and heterologous phosphorelay complementation support this role. HPr also influences (p)ppGpp production through an incompletely resolved branch; the tested two-hybrid assay did not detect HPr–SpoT binding. Its established role is regulatory rather than mannose uptake.',
 'ptsN': 'PtsN (enzyme IIA Ntr; CCNA_03710) is a phosphorylation-dependent regulator in Caulobacter vibrioides NA1000. Its phosphorylated state promotes association with SpoT and inhibits SpoT-mediated (p)ppGpp hydrolysis, allowing alarmone accumulation during nitrogen limitation and influencing the G1-to-S transition. Phosphostate-dependent binding was tested with Caulobacter proteins in bacterial two-hybrid assays, and hydrolase control was dissected in engineered NA1000 cells. PtsN is a downstream regulatory phosphoacceptor, rather than a demonstrated mannose-translocating PTS component.'}
for gene in ('ptsP', 'ptsH', 'ptsN'):
    path = ROOT / f'genes/CAUVN/{gene}/{gene}-ai-review.yaml'
    data = yaml.safe_load(path.read_text())
    old = yaml.safe_load((AUDIT / f'seed-copies/{gene}-ai-review.yaml').read_text())
    assert data['existing_annotations'] == old['existing_annotations'], 'Do not rerun over curated reviews'
    data['description'] = DESCRIPTIONS[gene]
    data['status'] = 'COMPLETE'
    for ann in data['existing_annotations']:
        term = ann['term']['id']
        if term == 'GO:0005737':
            ann['review'] = review('ACCEPT', 'Cytoplasmic signaling is consistent with the native intracellular phosphorelay.',
              'Retain the broad intracellular compartment as a mechanistic localization inference from the soluble phosphorelay acting on intracellular protein partners and (p)ppGpp signaling. This is not an independent fractionation measurement or a claim of spatially resolved cytosol localization. The ARBA-only UniProt location is not used as evidence. No membrane-crossing activity is inferred.', ['ei' if gene == 'ptsP' else 'relay'])
        elif term == 'GO:0008965':
            ann['review'] = review('ACCEPT', 'NA1000 PtsP-containing fractions undergo PEP-dependent autophosphorylation.',
              'The donor-specific protein-histidine phosphotransfer chemistry is supported by radiolabeled PEP assays in enriched PtsP-containing fractions, together with native phosphorelay genetics and the enzyme-I architecture. The preparation was not homogeneous purified PtsP; downstream HPr transfer is inferred from the relay rather than measured as isolated NA1000 binary kinetics. Glutamine responsiveness does not by itself measure glutamine binding.', ['ei', 'gln'])
        elif term == 'GO:0016772':
            ann['review'] = review('MODIFY', 'The true broad phosphotransferase class can be refined to the measured PEP-dependent activity.',
              'GO:0008965 is a supported descendant of this phosphorus-group transferase term and specifies the PEP donor/protein histidine acceptor chemistry. This refinement preserves the positive enzyme-I evidence and the enriched-fraction assay limitation.', ['ei'], EI)
        elif term in ('GO:0016301', 'GO:0016740'):
            lateral = term == 'GO:0016301'
            ann['review'] = review('MODIFY', 'HPr transfers phosphoryl groups to a nitrogenous acceptor in a protein-histidine relay.',
              ('This is a lateral chemical-acceptor refinement, not a claimed descendant of kinase activity. Kinase activity is not rejected merely because the donor is not ATP. ' if lateral else 'GO:0016775 is a descendant of transferase activity and supplies the supported acceptor class. ')
              + 'HPr supplies phosphoryl transfer to PtsN histidine, supported by native pathway genetics, the HPr phosphohistidine-site signature, and restoration of PtsN–SpoT interaction by Caulobacter HPr in an E. coli npr deletion background. This is not purified native forward kinetics. ATP-specific protein histidine kinase and hybrid-kinase/response-regulator phosphotransfer terms would assert different reactions.', ['relay', 'loci'], HPR)
        elif term == 'GO:0030295':
            ann['review'] = review('UNDECIDED', 'The measured NA1000 output is SpoT hydrolase inhibition; a protein kinase target remains unresolved.',
              'GO:0030295 requires activation of a protein kinase. SpoT alarmone synthetase/hydrolase control does not establish that activity. Nevertheless, a different measured regulatory output does not exclude additional kinase targets. The source is TreeGrafter node PTN002412133; the locally retrieved PAINT slice contains a different kinase-activation node (PTN002021052) with an E. coli positive anchor, while the exact NA1000 accession has no leaf in the retrieved reference tree. Target ancestry or a lineage loss cannot therefore be asserted. Retain uncertainty in this particular functional transfer, not a conclusion that kinase activation is biologically impossible.', ['inhibit'])
        else:
            source = ('The submitter EC:2.7.1.191 mapping specifies mannose-coupled transport without native target support. ' if term == 'GO:0022870' else
                      'This automatic biological-process inference inherits the unsupported mannose-transporter specificity. ' if term == 'GO:0015761' else
                      'The shared InterPro/UniRule PTS features support phosphorelay identity but do not establish sugar transport. ')
            ann['review'] = review('MARK_AS_OVER_ANNOTATED', 'Regulatory phosphotransfer does not establish the mapped sugar/mannose transport function.', source + GENERIC_SUGAR, ['transport', 'loci'])
    findings = [
      {'statement': 'The experimental Caulobacter strains are NA1000-derived, matching the target taxon; the bacterial two-hybrid host is E. coli.', 'supporting_text': Q['strain']},
    ]
    if gene == 'ptsP':
        findings += [{'statement': 'PEP-dependent autophosphorylation was measured in enriched PtsP-containing fractions, not a homogeneous purified enzyme.', 'supporting_text': Q['ei']},
                     {'statement': 'Glutamine suppresses phosphorylation; the GAF-domain mechanism is not a direct binding measurement.', 'supporting_text': Q['gln']}]
    elif gene == 'ptsH':
        findings += [{'statement': 'Caulobacter HPr restores phosphostate-dependent downstream interaction in an E. coli npr mutant; this supports relay competence, not isolated native transfer kinetics.', 'supporting_text': Q['relay']},
                     {'statement': 'The tested HPr forms did not bind SpoT in the two-hybrid assay; its downstream effect is indirect in this model.', 'supporting_text': Q['indirect']}]
    else:
        findings += [{'statement': 'Wild-type and H66E PtsN support SpoT binding in two-hybrid assays; H66E is a phosphomimetic, not phosphohistidine itself.', 'supporting_text': Q['binding']},
                     {'statement': 'Engineered native cells separating RelA synthesis from SpoT hydrolysis support PtsN-dependent hydrolase inhibition; purified binary inhibition kinetics were not measured.', 'supporting_text': Q['inhibit']}]
    title = yaml.safe_load(PUB['27109061'].split('---')[1])['title']
    data['references'].append({'id': 'PMID:27109061', 'title': title, 'findings': findings})
    if gene == 'ptsP':
        data['references'].append({'id': 'PMID:26489861', 'title': yaml.safe_load(PUB['26489861'].split('---')[1])['title'], 'findings': [
          {'statement': 'Affinity purification and coimmunoprecipitation in NA1000 support PtsP–SpoT co-complex association, without resolving isolated binary binding or its catalytic consequence.', 'supporting_text': Q['coip']}]})
    core = {
      'ptsP': {'description': 'PEP-dependent protein-histidine phosphotransfer initiates the nitrogen-responsive relay. Native PtsP-enriched fraction assays demonstrate autophosphorylation and glutamine responsiveness; HPr delivery is supported by pathway genetics. PtsP–SpoT co-complex association does not establish an independent direct activation mechanism.', 'molecular_function': EI, 'supported_by': [support('ei'), support('gln'), support('coip')]},
      'ptsH': {'description': 'Protein-histidine phosphotransfer carries the regulatory signal from PtsP toward PtsN. Native genetics, the HPr architecture, and heterologous relay complementation support the activity; isolated native HPr-to-PtsN kinetics and the PtsN-independent downstream branch remain unresolved.', 'molecular_function': HPR, 'supported_by': [support('relay'), support('loci')]},
      'ptsN': {'description': 'Phosphorylation-dependent inhibition of SpoT (p)ppGpp hydrolase regulates alarmone accumulation. This synthesis combines phosphostate-dependent two-hybrid binding with hydrolase-dissection assays in engineered NA1000 cells; it does not imply purified binary inhibition kinetics or a universal PtsN kinase target.', 'molecular_function': INHIB, 'supported_by': [support('binding'), support('inhibit')]},
    }[gene]
    if gene != 'ptsN':
        core['locations'] = [CYTO]
    data['core_functions'] = [core]
    def payload(row):
        return {k: v for k, v in row.items() if k != 'review'}
    assert [payload(a) for a in data['existing_annotations']] == [payload(a) for a in old['existing_annotations']]
    out = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    out = '\n'.join(line.rstrip() for line in out.splitlines()) + '\n'
    temp = path.with_suffix('.yaml.tmp')
    temp.write_text(out)
    os.replace(temp, path)
    notes = ROOT / f'genes/CAUVN/{gene}/{gene}-notes.md'
    text = f'''\n## 2026-11-07 manual primary-source review\n\nReviewed all {len(data['existing_annotations'])} original rows in order; no NEW row or lifecycle change. Target {data['id']} is NA1000 (taxon 565050), not CB15. PMID27109061 explicitly identifies the relevant CCNA loci and uses NA1000-derived Caulobacter strains. Its bacterial two-hybrid experiments use E. coli hosts; H66E is a phosphomimetic. Read canonical full PMID27109061 and, for PtsP, full PMID26489861.\n\n{DESCRIPTIONS[gene]}\n\nCurrent GO definitions distinguish sugar-coupled transport from regulatory phosphotransfer. GO0016775 describes a nitrogenous acceptor; it is a transferase descendant but not a kinase descendant. Thus HPr's kinase refinement is lateral, without an unsupported assertion that all kinases require ATP. No ATP-specific or response-regulator kinase term is substituted. The cytoplasmic interpretation, where retained, is mechanistic inference, not ARBA evidence or a resolved microscopy/fractionation result.\n\nNo independent gene provider report is fabricated. Root's shared module Falcon attempt failed with HTTP403 authentication (sanitized receipt in acquisition-20261107/module-falcon-attempt.json); these are manual notes. Available official tree receipts do not locate the exact NA1000 accessions, so no CB15 replacement, target loss, or loss-free lineage is asserted. PtsN kinase activation remains genuinely unresolved beyond the measured SpoT output.\n\nNo process proposal was added merely to populate the module. Gene core activities summarize independently supported chemistry/regulation even when no suitable existing annotation carries it; intentional coverage warnings should not trigger invented NEW rows.\n'''
    with notes.open('a') as stream:
        stream.write(text)
print('Curated three reviews; ordered source payloads retained.')
