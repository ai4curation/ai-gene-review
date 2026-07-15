# RELN review notes

## 2026-07-14 — source review and annotation adjudication

Deep-research providers were unavailable because of a global quota block, so no provider output was retried or fabricated. This review instead used the local UniProt record, all 86 rows in `RELN-goa.tsv`, the cached publications cited by GOA, and additional cached primary papers needed to resolve the receptor-signaling and protease questions.

### Core biochemical and signaling activity

RELN encodes a secreted extracellular protein. Human loss-of-function evidence describes RELN as a large secreted receptor-binding protein and reports that pathogenic splice variants produce low or undetectable reelin [PMID:10973257, "The mutations disrupt splicing of RELN cDNA, resulting in low or undetectable amounts of reelin protein."; PMID:10973257, "RELN encodes a large (388 kD) secreted protein that acts on migrating cortical neurons by binding to the very low density lipoprotein receptor (VLDLR), the apolipoprotein E receptor 2 (ApoER2; refs 9-11 ), alpha3beta1 integrin and protocadherins."]

Direct biochemical evidence establishes binding to the canonical lipoprotein-family receptors [PMID:10571240, "Here, we demonstrate that Reelin binds directly to lipoprotein receptors, preferably the very low-density lipoprotein receptor (VLDLR) and apolipoprotein E receptor 2 (ApoER2)."] Receptor dependence of the downstream DAB1 response is supported by loss-of-receptor experiments [PMID:12670700, "These findings demonstrate that ApoER2 and VLDLR are essential for Reelin signaling and that no other receptor molecules can compensate for their role in mediating tyrosine phosphorylation of Dab1."]

Functional reelin is multimeric. The cached abstract identifies Cys2101 as linking the minimum covalent homodimer [PMID:21844191, "Detailed analysis of tryptic fragments produced from the purified reelin proteins revealed that the minimum unit of the multimer is a homodimeric reelin linked via Cys(2101) present in the central region"] and reports that disrupting this disulfide linkage preserves receptor binding but impairs signaling. The core function was therefore represented as lipoprotein-particle-receptor binding in the reelin-mediated signaling pathway, active in extracellular matrix and as part of the reelin complex.

### Separation of activity from biological outcomes

Neuronal migration, brain lamination, neuronal differentiation, synaptic maturation, plasticity, learning, and behavior are supported consequences of reelin signaling, but they are not additional autonomous molecular activities. The review therefore keeps these annotations as non-core outcomes while retaining receptor binding, receptor-ligand activity, reelin-mediated signaling, extracellular localization, and reelin-complex membership as core assertions. The review article used for many orthology transfers explicitly describes both developmental and adult contexts [PMID:28887403, "Reelin is a large extracellular matrix protein with relevant roles in mammalian central nervous system including neurogenesis, neuronal polarization and migration during development; and synaptic plasticity with its implications in learning and memory, in the adult."]

### Protease activity is disputed

The two serine-type-peptidase annotations were left `UNDECIDED`. An early study reported intrinsic activity [PMID:11689558, "Here we show that reelin is a serine protease and that proteolytic activity is relevant to its function"], whereas a later direct re-evaluation found no laminin degradation and concluded the opposite [PMID:20522975, "It is thus likely that Reelin is not a serine protease and is unable to degrade extracellular matrix."] The latter does not by itself prove that no substrate or condition can reveal proteolysis, so neither confident acceptance nor confident removal is warranted. Protease activity is excluded from the synthesized core function pending independent resolution.

### Cerebellar top-down decomposition context

PMID:20809939 was read in full because it anchors RELN in the slide-driven cerebellar hierarchy. Its conclusion is deliberately narrow: the observed mechanism concerns a subset of early/posterior-born Purkinje cells in mouse lateral cerebellum [PMID:20809939, "Previously unknown behaviors are revealed for a subset of Purkinje cells born early in the posteior lateral cerebellum: tangential migration; early axonogenesis; and Reelin-dependent reorientation initiating PP formation."] The paper supports a Reelin-dependent reorientation/posture-change step that initiates Purkinje-plate formation in that cohort. It does not establish that every Purkinje-cell cohort uses the identical mechanism, and it is not direct human evidence. This outcome is recorded as cerebellar context and a knowledge gap rather than folded into the project-independent core molecular activity.

### Annotation decisions

- `ACCEPT` (20): receptor binding/ligand activity, canonical reelin signaling, extracellular-matrix or extracellular-region localization, and reelin-complex membership.
- `KEEP_AS_NON_CORE` (60): developmental, migratory, differentiation, downstream signaling, synaptic, behavioral, and organism-level outcomes.
- `MARK_AS_OVER_ANNOTATED` (4): plasma membrane, cytoplasm, neuron projection, and dendrite localizations that conflate receptor proximity or biosynthetic transit with the extracellular site of reelin activity.
- `UNDECIDED` (2): serine-type peptidase activity because direct primary studies conflict.

No GOA row was deleted, merged, or reordered; duplicate evidence rows were preserved. No isoform-specific or negated annotations were present in the seeded set.
