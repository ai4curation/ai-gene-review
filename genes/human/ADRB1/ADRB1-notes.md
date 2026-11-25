## 2026-11-25 - adrenaline GO-CAM ADRB1 review

ADRB1 was fetched for the adrenaline GO-CAM review session with `just fetch-gene human ADRB1`
and the remaining seeded GOA publications were cached with `just fetch-gene-pmids human ADRB1`.
The standard `just deep-research-falcon human ADRB1 --fallback perplexity-lite` command could not
run because neither the Falcon nor Perplexity providers were available in this runtime, so this is
a manual review over the cached UniProt record, GOA row set, publications, Reactome records and the
adrenaline GO-CAM context. No provider-named deep-research artifact was fabricated.

ADRB1 is the beta-1 adrenergic receptor, a seven-transmembrane catecholamine GPCR that couples to
Gs at the plasma membrane to stimulate adenylyl cyclase and cAMP signaling. UniProt summarizes this
core function as "G protein-coupled receptor for catecholamines that couples to G(s) proteins to
activate adenylate cyclase and cAMP-dependent pathway", and Mason et al. showed that the Arg389
receptor variant has higher isoproterenol-stimulated adenylyl cyclase activity and enhanced Gs
coupling [PMID:10212248 "maximal isoproterenol-stimulated levels were markedly higher for the
Arg-389"; PMID:10212248 "consistent with enhanced coupling to Gs and increased adenylyl cyclase
activation"]. Pak et al. further showed that agonist-activated beta1-AR signals through Gs alpha and
cAMP to a directly associated CNrasGEF/RAPGEF2 PDZ protein [PMID:12391161 "the activation is
transduced via Gsalpha and not via Gbetagamma"].

The 680ad14200003171 GO-CAM uses ADRB1 with `GO:0004940` beta1-adrenergic receptor activity at the
plasma membrane in `GO:0007189` adenylate cyclase-activating GPCR signaling. That activity agrees
with this gene review. Its ADRB1-to-GNAS causal edge is also biologically sound, but the edge cites
unrelated PMID:37963465; the model review already records this as a suspected GO-CAM source defect.
The nested `part_of GO:0001996` heart-rate context is a real ADRB1 physiology output but is not the
core molecular pathway; PMID:11854867 is a genetic association with resting heart rate, not a direct
adrenaline/norepinephrine heart-rate assay.

ADRB1 has a genuine C-terminal PDZ-binding motif. Direct and array-based studies identify RAPGEF2,
MAGI2, MAGI3, DLG4 and other PDZ proteins as partners, so bare `GO:0005515` protein binding rows
from PDZ-domain experiments should be represented as `GO:0030165` PDZ domain binding. Generic
`GO:0005515` rows for A1 adenosine receptor, GPER, PDE4D and RAMP interactions are not informative
ADRB1 molecular functions; these specialized receptor-complex observations are peripheral to the
core catecholamine receptor activity.

Protein-binding policy: bare PDZ-domain protein binding rows map to PDZ domain binding; the
PMID:16533813 DLG4/MAGI2 bare rows are removed because direct ADRB1 evidence already asserts the
specific child term for those PDZ scaffolds. Bare non-PDZ receptor-complex protein binding rows are
removed as uninformative.

ADRB1 also has real but secondary physiological outputs. Human ADRB1 variants associate with
resting heart rate and natural short sleep, mouse Adrb1 loss impairs cold-induced adaptive
thermogenesis, and mouse Adrb1 evidence supports a cardiomyocyte-apoptosis output. The 2019 UniProt
sleep row cites PMID:25083013, but that paper is about BHLHE41/DEC2 short-sleep variants; the
ADRB1 sleep paper is PMID:31473062.

The Ensembl Compara transfer from mouse P34971 maps two neuronal cellular-component rows,
`GO:0098685` Schaffer collateral - CA1 synapse and `GO:0098992` neuronal dense core vesicle, onto
human ADRB1. Shi et al. establish ADRB1-positive dorsal pons neurons in sleep/wake regulation, but
the local cached literature does not support the hippocampal Schaffer-collateral or dense-core-vesicle
placements for human ADRB1, so these specific locations are over-annotations here.
