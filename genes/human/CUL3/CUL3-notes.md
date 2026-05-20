# CUL3 notes

Initial Falcon pass, 2026-05-12. CUL3 started as a fully pending review with
228 annotations. I kept this pass centered on the conserved CRL3 scaffold
function and left most generic protein-binding and substrate-specific rows for
later source-level review.

Core molecular function: CUL3 is the scaffold of cullin-RING E3 ligase
complexes. Falcon states that CUL3 bridges RBX1/E2 ubiquitin-conjugating
machinery with BTB-domain substrate adaptors
[file:human/CUL3/CUL3-deep-research-falcon.md "CUL3 is the **central
scaffold** of CRL3 ubiquitin ligases, bridging (i) a **RING protein (RBX1)**
that recruits E2~ubiquitin and (ii) **BTB-domain substrate adaptor/receptor
proteins** that recruit specific substrates."]. I accepted ubiquitin ligase
complex scaffold activity and Cul3-RING ubiquitin ligase complex rows as the
core axis.

Core process: protein ubiquitination, polyubiquitination, and
proteasome-mediated ubiquitin-dependent catabolism are proximal outputs of many
CRL3 complexes [file:human/CUL3/CUL3-deep-research-falcon.md "Proteasomal
targeting is a canonical outcome for many CRLs, and reviews explicitly describe
substrate ubiquitination “for proteasomal degradation” as a CRL3 output"]. I
accepted well-supported ubiquitination and catabolic-process rows, but kept the
caveat that not every CUL3 ubiquitination event is degradative.

Molecular-function specificity: Falcon cautions that CUL3 is best represented
as the scaffold rather than the catalytic ubiquitin transferase
[file:human/CUL3/CUL3-deep-research-falcon.md "evidence best supports a CUL3
annotation consistent with **“ubiquitin ligase complex scaffold activity”** /
**E3 ligase scaffold** rather than “ubiquitin-protein transferase activity”
(which is catalytic and typically attributed to the E2/E3 catalytic machinery
rather than the scaffold)"]. I therefore modified ubiquitin-protein transferase
and ubiquitin protein ligase activity rows to the scaffold term.

Non-core contexts: many CUL3 annotations reflect the substrate/adaptor being
studied: KEAP1/NRF2 oxidative stress, KLHL3/WNK ion transport, KLHL12/COPII,
KBTBD/KCTD complexes, mitotic substrates, neuronal phenotypes, viral processes,
and disease models. Falcon warns that broad phenotypes should not be promoted
to core CUL3 functions without direct mechanistic evidence
[file:human/CUL3/CUL3-deep-research-falcon.md "oxidative stress response,
blood pressure/electrolyte phenotypes, neurodevelopmental phenotypes, or
cancer-associated phenotypes can be downstream of CUL3-dependent substrate
regulation. These should not be treated as core CUL3 BP terms without direct
mechanistic evidence that CUL3’s scaffold activity is required in the specific
pathway node being annotated."].

Localization: CUL3 complex membership is core. I accepted a few broad
cytoplasm/cytosol/nuclear rows, but Falcon notes that specific membrane,
centrosome, cytoskeleton, and other locations require caution
[file:human/CUL3/CUL3-deep-research-falcon.md "**Membrane/centrosome/cytoskeleton
claims require caution:**"]. Most highly specific or repetitive localization
rows remain pending unless a direct source was already strong enough for a
non-core decision.

Left for later: generic protein-binding rows should be triaged by partner
(BTB/POZ adaptor, RBX1, substrate, CSN/CAND1 regulator, or nonspecific
interaction). Substrate-specific phenotype rows should be reviewed one adaptor
module at a time rather than treated as core CUL3 biology.
