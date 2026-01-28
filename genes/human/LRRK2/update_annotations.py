#!/usr/bin/env python3
"""Script to update LRRK2 GO annotation reviews based on deep research."""

import yaml
import re

# Load the YAML file
with open('LRRK2-ai-review.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Define review decisions based on GO term and evidence
# Key insight from deep research:
# - Core functions: Ser/Thr kinase, GTPase, Rab phosphorylation, endolysosomal trafficking, ciliogenesis
# - Primary substrates: Rab8A, Rab10, Rab12, Rab29
# - Localization: cytosol, Golgi, endosomes, lysosomes
# - Regulation: 14-3-3 binding, autophosphorylation

CORE_MF_TERMS = {
    'GO:0004674': ('ACCEPT', 'Protein serine/threonine kinase activity is a core enzymatic function of LRRK2. The kinase domain phosphorylates Rab GTPases at their switch II regions.'),
    'GO:0004672': ('ACCEPT', 'Protein kinase activity is a core function of LRRK2, phosphorylating Rab GTPases and other substrates.'),
    'GO:0003924': ('ACCEPT', 'GTPase activity is a core function of LRRK2 ROC domain. The ROC domain binds and hydrolyzes GTP.'),
    'GO:0005525': ('ACCEPT', 'GTP binding is essential for LRRK2 ROC domain function and regulates kinase activity.'),
    'GO:0005524': ('ACCEPT', 'ATP binding is required for LRRK2 kinase activity.'),
    'GO:0016301': ('ACCEPT', 'Kinase activity is a core function - LRRK2 is a dual-function kinase/GTPase.'),
    'GO:0034211': ('ACCEPT', 'GTP-dependent protein kinase activity reflects the intramolecular regulation between ROC GTPase and kinase domains.'),
    'GO:0046777': ('ACCEPT', 'Protein autophosphorylation is well-documented for LRRK2, including Ser1292 as an activity marker.'),
    'GO:0106310': ('ACCEPT', 'Protein serine kinase activity - LRRK2 phosphorylates serine/threonine residues on Rab substrates.'),
}

CORE_LOCALIZATION = {
    'GO:0005829': ('ACCEPT', 'Cytosol is the predominant localization of LRRK2, from which it is recruited to membranes.'),
    'GO:0005737': ('ACCEPT', 'Cytoplasm is a major localization for LRRK2.'),
    'GO:0005794': ('ACCEPT', 'Golgi apparatus localization is supported - LRRK2 is recruited to Golgi by Rab29.'),
    'GO:0005764': ('ACCEPT', 'Lysosome localization is consistent with LRRK2 role in endolysosomal trafficking.'),
    'GO:0005768': ('ACCEPT', 'Endosome localization is consistent with LRRK2 role in regulating Rab-dependent trafficking.'),
    'GO:0000139': ('ACCEPT', 'Golgi membrane localization - LRRK2 is recruited to Golgi membranes where Rab29 resides.'),
    'GO:0005802': ('ACCEPT', 'Trans-Golgi network localization is supported by Rab29-mediated recruitment studies.'),
}

CORE_BP_TERMS = {
    'GO:0035556': ('ACCEPT', 'Intracellular signal transduction - LRRK2 functions as a kinase that phosphorylates Rab GTPases.'),
    'GO:0007030': ('ACCEPT', 'Golgi organization - LRRK2 regulates Golgi-related trafficking through Rab phosphorylation.'),
    'GO:0016192': ('ACCEPT', 'Vesicle-mediated transport - core function via Rab GTPase phosphorylation regulating trafficking.'),
    'GO:0006468': ('ACCEPT', 'Protein phosphorylation - core enzymatic function of LRRK2 kinase domain.'),
}

KEEP_AS_NON_CORE = {
    'GO:0005886': ('KEEP_AS_NON_CORE', 'Plasma membrane - LRRK2 can localize to membranes but cytosol is predominant.'),
    'GO:0030425': ('KEEP_AS_NON_CORE', 'Dendrite localization is tissue-specific in neurons, not a core localization.'),
    'GO:0030424': ('KEEP_AS_NON_CORE', 'Axon localization is tissue-specific in neurons.'),
    'GO:0043204': ('KEEP_AS_NON_CORE', 'Perikaryon (neuronal cell body) is tissue-specific localization.'),
    'GO:0043025': ('KEEP_AS_NON_CORE', 'Neuronal cell body is tissue-specific localization.'),
    'GO:0043005': ('KEEP_AS_NON_CORE', 'Neuron projection is tissue-specific in neurons.'),
    'GO:0098794': ('KEEP_AS_NON_CORE', 'Postsynapse is a tissue-specific neuronal localization.'),
    'GO:0043195': ('KEEP_AS_NON_CORE', 'Terminal bouton is tissue-specific neuronal localization.'),
    'GO:0045202': ('KEEP_AS_NON_CORE', 'Synapse is tissue-specific neuronal localization.'),
    'GO:0099523': ('KEEP_AS_NON_CORE', 'Presynaptic cytosol is tissue-specific.'),
    'GO:0098978': ('KEEP_AS_NON_CORE', 'Glutamatergic synapse is tissue-specific.'),
    'GO:0008021': ('KEEP_AS_NON_CORE', 'Synaptic vesicle is tissue-specific in neurons.'),
    'GO:0030672': ('KEEP_AS_NON_CORE', 'Synaptic vesicle membrane is tissue-specific.'),
    'GO:0032839': ('KEEP_AS_NON_CORE', 'Dendrite cytoplasm is tissue-specific.'),
    'GO:0030426': ('KEEP_AS_NON_CORE', 'Growth cone is tissue-specific neuronal structure.'),
}

OVER_ANNOTATED = {
    'GO:0006914': ('MARK_AS_OVER_ANNOTATED', 'Autophagy effects are downstream of LRRK2 trafficking disruption, not a direct evolved function.'),
    'GO:0010508': ('MARK_AS_OVER_ANNOTATED', 'Positive regulation of autophagy is a downstream effect of trafficking disruption, not core function.'),
    'GO:0016242': ('MARK_AS_OVER_ANNOTATED', 'Negative regulation of macroautophagy is downstream of trafficking effects.'),
    'GO:1902902': ('MARK_AS_OVER_ANNOTATED', 'Negative regulation of autophagosome assembly is downstream effect.'),
    'GO:0010506': ('MARK_AS_OVER_ANNOTATED', 'Regulation of autophagy is downstream of trafficking/lysosomal effects.'),
    'GO:0034599': ('MARK_AS_OVER_ANNOTATED', 'Cellular response to oxidative stress is a pleiotropic disease-related effect.'),
    'GO:0006979': ('MARK_AS_OVER_ANNOTATED', 'Response to oxidative stress is pleiotropic/disease-related.'),
    'GO:0034614': ('MARK_AS_OVER_ANNOTATED', 'Cellular response to reactive oxygen species is disease-related.'),
    'GO:2000377': ('MARK_AS_OVER_ANNOTATED', 'Regulation of ROS metabolic process is downstream.'),
    'GO:0007005': ('MARK_AS_OVER_ANNOTATED', 'Mitochondrion organization effects are likely secondary.'),
    'GO:0051646': ('MARK_AS_OVER_ANNOTATED', 'Mitochondrion localization effects are secondary.'),
    'GO:0090140': ('MARK_AS_OVER_ANNOTATED', 'Regulation of mitochondrial fission is secondary effect.'),
    'GO:0070585': ('MARK_AS_OVER_ANNOTATED', 'Protein localization to mitochondrion is secondary.'),
    'GO:0051900': ('MARK_AS_OVER_ANNOTATED', 'Regulation of mitochondrial depolarization is disease-related.'),
    'GO:0048312': ('MARK_AS_OVER_ANNOTATED', 'Intracellular distribution of mitochondria is secondary.'),
    'GO:0043068': ('MARK_AS_OVER_ANNOTATED', 'Positive regulation of programmed cell death is disease-related.'),
    'GO:1901030': ('MARK_AS_OVER_ANNOTATED', 'Positive regulation of mitochondrial outer membrane permeabilization in apoptotic signaling is disease-related.'),
    'GO:1902236': ('MARK_AS_OVER_ANNOTATED', 'Negative regulation of ER stress-induced intrinsic apoptotic signaling pathway is disease-related.'),
    'GO:0008340': ('MARK_AS_OVER_ANNOTATED', 'Determination of adult lifespan is pleiotropic.'),
    'GO:0035640': ('MARK_AS_OVER_ANNOTATED', 'Exploration behavior is a high-level organismal phenotype.'),
    'GO:0035641': ('MARK_AS_OVER_ANNOTATED', 'Locomotory exploration behavior is organismal phenotype.'),
    'GO:0040012': ('MARK_AS_OVER_ANNOTATED', 'Regulation of locomotion is high-level organismal phenotype.'),
    'GO:0021756': ('MARK_AS_OVER_ANNOTATED', 'Striatum development is tissue-specific developmental effect.'),
    'GO:0021772': ('MARK_AS_OVER_ANNOTATED', 'Olfactory bulb development is tissue-specific.'),
    'GO:0022028': ('MARK_AS_OVER_ANNOTATED', 'Tangential migration from subventricular zone is developmental.'),
    'GO:0014041': ('MARK_AS_OVER_ANNOTATED', 'Regulation of neuron maturation is developmental.'),
    'GO:1902692': ('MARK_AS_OVER_ANNOTATED', 'Regulation of neuroblast proliferation is developmental.'),
    'GO:2000172': ('MARK_AS_OVER_ANNOTATED', 'Regulation of branching morphogenesis of a nerve is developmental.'),
    'GO:0048812': ('MARK_AS_OVER_ANNOTATED', 'Neuron projection morphogenesis is developmental.'),
    'GO:0140058': ('MARK_AS_OVER_ANNOTATED', 'Neuron projection arborization is developmental.'),
    'GO:0030182': ('MARK_AS_OVER_ANNOTATED', 'Neuron differentiation is developmental.'),
    'GO:0030154': ('MARK_AS_OVER_ANNOTATED', 'Cell differentiation is very broad.'),
    'GO:0009653': ('MARK_AS_OVER_ANNOTATED', 'Anatomical structure morphogenesis is very broad.'),
    'GO:0048513': ('MARK_AS_OVER_ANNOTATED', 'Animal organ development is very broad.'),
    'GO:0007528': ('MARK_AS_OVER_ANNOTATED', 'Neuromuscular junction development is tissue-specific.'),
    'GO:1903980': ('MARK_AS_OVER_ANNOTATED', 'Positive regulation of microglial cell activation is downstream immune effect.'),
    'GO:0032760': ('MARK_AS_OVER_ANNOTATED', 'Positive regulation of TNF production is downstream immune effect.'),
    'GO:0007283': ('MARK_AS_OVER_ANNOTATED', 'Spermatogenesis is tissue-specific.'),
    'GO:0035564': ('MARK_AS_OVER_ANNOTATED', 'Regulation of kidney size is tissue-specific.'),
    'GO:1904644': ('MARK_AS_OVER_ANNOTATED', 'Cellular response to curcumin is an experimental condition response.'),
    'GO:0071287': ('MARK_AS_OVER_ANNOTATED', 'Cellular response to manganese ion is experimental.'),
    'GO:1903351': ('MARK_AS_OVER_ANNOTATED', 'Cellular response to dopamine is tissue-specific.'),
    'GO:0009267': ('MARK_AS_OVER_ANNOTATED', 'Cellular response to starvation is experimental condition.'),
}

ACCEPT_TRAFFICKING = {
    'GO:0007029': ('ACCEPT', 'ER organization is related to LRRK2 role in Sec16A regulation at ER exit sites.'),
    'GO:0070971': ('ACCEPT', 'ER exit site localization - LRRK2 regulates Sec16A at ER exit sites.'),
    'GO:0070973': ('ACCEPT', 'Protein localization to ER exit site - LRRK2 regulates Sec16A.'),
    'GO:0060628': ('ACCEPT', 'Regulation of ER to Golgi vesicle-mediated transport - via Sec16A regulation.'),
    'GO:1905279': ('ACCEPT', 'Regulation of retrograde transport, endosome to Golgi - via Rab29/RAB7L1 interaction.'),
    'GO:0007040': ('ACCEPT', 'Lysosome organization - consistent with endolysosomal trafficking role.'),
    'GO:0035751': ('ACCEPT', 'Regulation of lysosomal lumen pH - via effects on lysosomal function.'),
    'GO:1902823': ('KEEP_AS_NON_CORE', 'Negative regulation of late endosome to lysosome transport - downstream effect.'),
    'GO:0006897': ('KEEP_AS_NON_CORE', 'Endocytosis - related to synaptic vesicle endocytosis role.'),
    'GO:0060627': ('ACCEPT', 'Regulation of vesicle-mediated transport - core trafficking function.'),
    'GO:0008104': ('ACCEPT', 'Intracellular protein localization - broad but relevant to trafficking role.'),
}

ACCEPT_SYNAPTIC = {
    'GO:1900242': ('ACCEPT', 'Regulation of synaptic vesicle endocytosis - well-documented LRRK2 function.'),
    'GO:1900244': ('KEEP_AS_NON_CORE', 'Positive regulation of synaptic vesicle endocytosis - tissue-specific.'),
    'GO:1902803': ('KEEP_AS_NON_CORE', 'Regulation of synaptic vesicle transport - tissue-specific.'),
    'GO:2000300': ('KEEP_AS_NON_CORE', 'Regulation of synaptic vesicle exocytosis - tissue-specific.'),
    'GO:0035542': ('KEEP_AS_NON_CORE', 'Regulation of SNARE complex assembly - related to vesicle function.'),
    'GO:0050804': ('KEEP_AS_NON_CORE', 'Modulation of chemical synaptic transmission - tissue-specific.'),
    'GO:0051966': ('KEEP_AS_NON_CORE', 'Regulation of synaptic transmission, glutamatergic - tissue-specific.'),
    'GO:0060079': ('KEEP_AS_NON_CORE', 'Excitatory postsynaptic potential - tissue-specific.'),
    'GO:0090394': ('KEEP_AS_NON_CORE', 'Negative regulation of excitatory postsynaptic potential - tissue-specific.'),
    'GO:0042391': ('KEEP_AS_NON_CORE', 'Regulation of membrane potential - neuronal effect.'),
}

ACCEPT_CILIA = {
    'GO:1905504': ('ACCEPT', 'Negative regulation of motile cilium assembly - core function via Rab8/Rab10/RILPL1 axis.'),
    'GO:0031344': ('ACCEPT', 'Regulation of cell projection organization - includes ciliogenesis.'),
    'GO:0061001': ('KEEP_AS_NON_CORE', 'Regulation of dendritic spine morphogenesis - neuronal effect.'),
    'GO:0010977': ('KEEP_AS_NON_CORE', 'Negative regulation of neuron projection development - neuronal.'),
}

WNT_SIGNALING = {
    'GO:0060828': ('KEEP_AS_NON_CORE', 'Regulation of canonical Wnt signaling pathway - LRRK2 acts as scaffold but not core function.'),
    'GO:0090263': ('KEEP_AS_NON_CORE', 'Positive regulation of canonical Wnt signaling pathway - scaffold role.'),
    'GO:0060070': ('KEEP_AS_NON_CORE', 'Canonical Wnt signaling pathway - scaffold role.'),
    'GO:1904887': ('KEEP_AS_NON_CORE', 'Wnt signalosome assembly - via LRP6 bridging.'),
    'GO:1990909': ('KEEP_AS_NON_CORE', 'Wnt signalosome localization - scaffold role.'),
    'GO:1904713': ('KEEP_AS_NON_CORE', 'Beta-catenin destruction complex binding - scaffold role.'),
}

DOPAMINE_SIGNALING = {
    'GO:0060159': ('KEEP_AS_NON_CORE', 'Regulation of dopamine receptor signaling pathway - tissue-specific.'),
    'GO:0060161': ('KEEP_AS_NON_CORE', 'Positive regulation of dopamine receptor signaling pathway - tissue-specific.'),
    'GO:0141161': ('KEEP_AS_NON_CORE', 'Regulation of cAMP/PKA signal transduction - related to dopamine signaling.'),
}

MAPK_SIGNALING = {
    'GO:0004706': ('UNDECIDED', 'JUN kinase kinase kinase activity - reported but may not be physiological core function.'),
    'GO:0004709': ('UNDECIDED', 'MAP kinase kinase kinase activity - reported in vitro but physiological relevance unclear.'),
    'GO:0007254': ('UNDECIDED', 'JNK cascade - reported but physiological relevance as direct function unclear.'),
    'GO:0000165': ('UNDECIDED', 'MAPK cascade - reported but may be downstream effect.'),
    'GO:0043410': ('UNDECIDED', 'Positive regulation of MAPK cascade - may be indirect.'),
}

BINDING_TERMS = {
    'GO:0005515': ('KEEP_AS_NON_CORE', 'Protein binding is uninformative - LRRK2 has many documented interactors.'),
    'GO:0042802': ('ACCEPT', 'Identical protein binding - LRRK2 forms homodimers, important for regulation.'),
    'GO:0042803': ('ACCEPT', 'Protein homodimerization activity - LRRK2 dimerization is well-documented.'),
    'GO:0031267': ('ACCEPT', 'Small GTPase binding - LRRK2 binds Rab substrates and other small GTPases.'),
    'GO:0000166': ('ACCEPT', 'Nucleotide binding - required for kinase and GTPase activities.'),
    'GO:0051018': ('KEEP_AS_NON_CORE', 'Protein kinase A binding - interaction documented but not core.'),
    'GO:0015631': ('KEEP_AS_NON_CORE', 'Tubulin binding - documented but not core function.'),
    'GO:0008017': ('KEEP_AS_NON_CORE', 'Microtubule binding - documented but significance unclear.'),
    'GO:0000149': ('KEEP_AS_NON_CORE', 'SNARE binding - related to vesicle function.'),
    'GO:0003779': ('KEEP_AS_NON_CORE', 'Actin binding - documented interaction.'),
    'GO:0017075': ('KEEP_AS_NON_CORE', 'Syntaxin-1 binding - vesicle-related.'),
    'GO:0030276': ('KEEP_AS_NON_CORE', 'Clathrin binding - endocytosis-related.'),
    'GO:0044325': ('KEEP_AS_NON_CORE', 'Transmembrane transporter binding - various interactions.'),
    'GO:0039706': ('UNDECIDED', 'Co-receptor binding - Wnt-related, needs verification.'),
    'GO:0030159': ('UNDECIDED', 'Signaling receptor complex adaptor activity - Wnt scaffold role.'),
}

OTHER_TERMS = {
    'GO:0005096': ('UNDECIDED', 'GTPase activator activity - LRRK2 has intrinsic GTPase activity but GAP activity on other GTPases is unclear.'),
    'GO:0016740': ('ACCEPT', 'Transferase activity - parent term of kinase activity.'),
    'GO:0016787': ('ACCEPT', 'Hydrolase activity - parent term of GTPase activity.'),
    'GO:0036479': ('UNDECIDED', 'Peroxidase inhibitor activity - reported but unclear if core function.'),
    'GO:0034260': ('UNDECIDED', 'Negative regulation of GTPase activity - needs verification.'),
    'GO:0046039': ('ACCEPT', 'GTP metabolic process - related to GTPase activity.'),
    'GO:0007266': ('UNDECIDED', 'Rho protein signal transduction - may be downstream effect.'),
    'GO:1905289': ('KEEP_AS_NON_CORE', 'Regulation of CAMKK-AMPK signaling cascade - downstream effect.'),
    'GO:0019722': ('KEEP_AS_NON_CORE', 'Calcium-mediated signaling - via NAADP pathway.'),
    'GO:0007166': ('KEEP_AS_NON_CORE', 'Cell surface receptor signaling pathway - very broad.'),
    'GO:0009968': ('KEEP_AS_NON_CORE', 'Negative regulation of signal transduction - broad.'),
    'GO:1902531': ('KEEP_AS_NON_CORE', 'Regulation of intracellular signal transduction - broad.'),
    'GO:0010468': ('KEEP_AS_NON_CORE', 'Regulation of gene expression - very broad downstream effect.'),
    'GO:0051239': ('KEEP_AS_NON_CORE', 'Regulation of multicellular organismal process - very broad.'),
    'GO:0051247': ('KEEP_AS_NON_CORE', 'Positive regulation of protein metabolic process - broad.'),
    'GO:0031398': ('KEEP_AS_NON_CORE', 'Positive regulation of protein ubiquitination - related to parkin interaction.'),
    'GO:1902499': ('KEEP_AS_NON_CORE', 'Positive regulation of protein autoubiquitination - parkin-related.'),
    'GO:0030162': ('KEEP_AS_NON_CORE', 'Regulation of proteolysis - broad.'),
    'GO:0032436': ('KEEP_AS_NON_CORE', 'Positive regulation of proteasomal ubiquitin-dependent protein catabolic process - downstream.'),
    'GO:0031647': ('KEEP_AS_NON_CORE', 'Regulation of protein stability - tau-related.'),
    'GO:0010955': ('KEEP_AS_NON_CORE', 'Negative regulation of protein processing - specific effect.'),
}

LOCALIZATION_OTHER = {
    'GO:0005783': ('ACCEPT', 'Endoplasmic reticulum - documented localization at ER exit sites.'),
    'GO:0005789': ('KEEP_AS_NON_CORE', 'ER membrane - related to ER exit site function.'),
    'GO:0005798': ('ACCEPT', 'Golgi-associated vesicle - consistent with trafficking role.'),
    'GO:0031410': ('ACCEPT', 'Cytoplasmic vesicle - consistent with trafficking role.'),
    'GO:0005856': ('KEEP_AS_NON_CORE', 'Cytoskeleton - microtubule association documented.'),
    'GO:0005741': ('KEEP_AS_NON_CORE', 'Mitochondrial outer membrane - reported but may be minor.'),
    'GO:0005743': ('KEEP_AS_NON_CORE', 'Mitochondrial inner membrane - reported but may be minor.'),
    'GO:0005759': ('KEEP_AS_NON_CORE', 'Mitochondrial matrix - reported but may be minor.'),
    'GO:0005739': ('KEEP_AS_NON_CORE', 'Mitochondrion - reported but not primary localization.'),
    'GO:0032473': ('KEEP_AS_NON_CORE', 'Cytoplasmic side of mitochondrial outer membrane - reported.'),
    'GO:0031966': ('KEEP_AS_NON_CORE', 'Mitochondrial membrane - reported.'),
    'GO:0045335': ('KEEP_AS_NON_CORE', 'Phagocytic vesicle - macrophage-specific.'),
    'GO:0045121': ('KEEP_AS_NON_CORE', 'Membrane raft - reported localization.'),
    'GO:0099400': ('KEEP_AS_NON_CORE', 'Caveola neck - specific localization.'),
    'GO:0005902': ('KEEP_AS_NON_CORE', 'Microvillus - specific localization.'),
    'GO:0044753': ('KEEP_AS_NON_CORE', 'Amphisome - autophagy-related.'),
    'GO:0044754': ('KEEP_AS_NON_CORE', 'Autolysosome - autophagy-related.'),
    'GO:0097487': ('KEEP_AS_NON_CORE', 'Multivesicular body, internal vesicle - endosomal.'),
    'GO:0070013': ('KEEP_AS_NON_CORE', 'Intracellular organelle lumen - very broad.'),
    'GO:1990904': ('KEEP_AS_NON_CORE', 'Ribonucleoprotein complex - specific interaction.'),
    'GO:0005615': ('KEEP_AS_NON_CORE', 'Extracellular space - exosome secretion.'),
    'GO:0070062': ('KEEP_AS_NON_CORE', 'Extracellular exosome - secreted in exosomes.'),
    'GO:0097413': ('KEEP_AS_NON_CORE', 'Lewy body - disease-specific pathological structure.'),
}

# Combine all dictionaries
ALL_DECISIONS = {}
ALL_DECISIONS.update(CORE_MF_TERMS)
ALL_DECISIONS.update(CORE_LOCALIZATION)
ALL_DECISIONS.update(CORE_BP_TERMS)
ALL_DECISIONS.update(KEEP_AS_NON_CORE)
ALL_DECISIONS.update(OVER_ANNOTATED)
ALL_DECISIONS.update(ACCEPT_TRAFFICKING)
ALL_DECISIONS.update(ACCEPT_SYNAPTIC)
ALL_DECISIONS.update(ACCEPT_CILIA)
ALL_DECISIONS.update(WNT_SIGNALING)
ALL_DECISIONS.update(DOPAMINE_SIGNALING)
ALL_DECISIONS.update(MAPK_SIGNALING)
ALL_DECISIONS.update(BINDING_TERMS)
ALL_DECISIONS.update(OTHER_TERMS)
ALL_DECISIONS.update(LOCALIZATION_OTHER)

# Update annotations
updated_count = 0
for ann in data['existing_annotations']:
    go_id = ann['term']['id']
    if ann['review']['action'] == 'PENDING':
        if go_id in ALL_DECISIONS:
            action, reason = ALL_DECISIONS[go_id]
            ann['review']['action'] = action
            ann['review']['summary'] = reason
            ann['review']['reason'] = reason
            updated_count += 1
        else:
            # Default to UNDECIDED for unknown terms
            ann['review']['action'] = 'UNDECIDED'
            ann['review']['summary'] = f'GO term {go_id} requires further review - no pre-defined decision available.'
            ann['review']['reason'] = 'Term not in curated decision list, requires manual review.'
            updated_count += 1

print(f"Updated {updated_count} annotations")

# Write back
with open('LRRK2-ai-review.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)

print("File written successfully")
