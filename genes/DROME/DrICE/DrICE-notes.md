# DrICE notes

## 2026-09-30

Reviewed all 44 seeded GOA rows for the APOPTOSIS conserved-Drosophila
comparator slice. DrICE should be centered on cytoplasmic C14
cysteine-type endopeptidase activity during `GO:0097194 execution phase of
apoptosis`: the original cloning paper showed that DrICE "cleaves baculovirus
p35 and Drosophila lamin DmO" [PMID:9184225], the DrICE-null paper found an
"important non-redundant role" for Ice/DrICE in developmental and
stress-induced deaths plus a partial nonlethal role in spermatid
differentiation [PMID:16887831], and the compensatory-proliferation paper
calls Dronc, DrICE, and Dcp-1 "crucial executioners of apoptosis"
[PMID:16980627].

Broad apoptosis and programmed-cell-death parents were therefore narrowed to
execution phase where the evidence placed DrICE at the effector-caspase step.
This matches the convention used for mammalian CASP3/CASP6/CASP7 and for worm
`ced-3`: a downstream caspase executes substrate cleavage, while Dronc/Dark sit
upstream at apoptotic signaling and caspase activation.

Three generic `GO:0005515 protein binding` rows needed directional cleanup.
The Dronc rows were removed because Dronc binds and cleaves DrICE as an
enzyme acting on its effector-caspase substrate, which does not define a
binding activity performed by DrICE; the metabolic-control paper explicitly
uses "Dronc-mediated cleavage of drICE" [PMID:20700104]. The DIAP rows were
recast as `GO:1990525 BIR domain binding`: DIAP1 inhibits DrICE "through its
BIR1 domain" [PMID:15107838], and DIAP2 "robustly ubiquitylates drICE in vivo"
after forming a stable inhibitory complex [PMID:18166655].

DrICE has several direct nonapoptotic or specialized outputs that should stay
outside the core apoptosis model. The Shaggy/Sgg46 work supports local
Dark/DRONC/DrICE caspase signaling in SOP patterning [PMID:16222340]. Active
DrICE cleaves Grim as a feedback input into DIAP1/RHG control
[PMID:23940367]. DrICE also restrains gut Imd/PGRP signaling through Diap2:
loss of DrICE raises Drosocin and Diptericin, DrICE activity destabilizes
Diap2, and the paper summarizes the branch as "Drice, by restraining Diap2"
[PMID:34262145]. A separate NF-kappaB paper supports Toll attenuation by
DrICE/DCP-1-mediated "degradation of DIF" [PMID:36002459]. These are real
effector-caspase cleavage outputs, but not generic apoptotic execution.

The oogenesis and spermatid rows are also direct but tissue-specific. The
nurse-cell paper reports that the "effector caspases drice and dcp-1 also
display redundant functions during late oogenesis" [PMID:17464325], so those
rows were kept as non-core rather than promoted to the main function. The Ice
knockout paper explicitly states that Ice is important for, but "not
absolutely required for, the non-apoptotic process of spermatid
differentiation" [PMID:16887831].

Rows from abstract-only FlyBase papers were handled conservatively when the
abstract did not expose the exact DrICE assay. PMID:16485033 says "Dronc,
drICE, Strica and Decay are rate limiting for apoptosis" and that "DIAP2 binds
active drICE", which is enough for the BIR/IAP contact but not enough to verify
the exact salivary-gland histolysis or retinal programmed-cell-death rows.
PMID:21035895 supports Malpighian-tubule nuclear sequestration of DRICE and
DRONC; the cytoplasm IDA row was accepted as compatible with the cytoplasmic
effector-caspase mechanism, while the plasma-membrane row remains undecided
until the full localization figure can be checked.

The only clearly bad computational propagation was the PAINT
`GO:0043525 positive regulation of neuron apoptotic process` row. PTN000047947
is a real effector-caspase node, but the inherited claim should be generic
execution-phase apoptosis, not a vertebrate/worm neuronal-apoptosis
descendant projected onto the general fly effector caspase.
