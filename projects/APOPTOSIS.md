---
title: "Apoptosis Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, zebrafish]
---

# Apoptosis Project

**Bottom line:** scoped and underway as a review campaign. This project will
separate mammalian apoptosis into mechanistic modules, audit annotations parked
at the broad `GO:0006915` apoptotic process term, and look for over-annotation
from caspase, TUNEL, annexin V, viability, or generic cell-death readouts. Two
draft modules already exist for [intrinsic apoptotic
signaling](../modules/intrinsic_apoptotic_signaling.html) and [death receptor
apoptotic signaling](../modules/death_receptor_apoptotic_signaling.html); both
should be reviewed before adding execution-phase and BCL2/MOMP submodules. The
first review slice should stay mammal-focused, with human and mouse rows handled
together, while using conserved opisthokont components as comparators rather
than blindly transferring every mammalian branch to flies, worms, or fungi.

## Overview

Apoptosis is a caspase-centered programmed cell-death program in metazoans. In
mammals, the best-defined inputs are:

- **Extrinsic/death-receptor signaling**, where FAS, TRAIL, or TNF-family
  receptor complexes recruit FADD and initiator caspases such as CASP8.
- **Intrinsic/mitochondrial signaling**, where BCL2-family decisions at the
  outer mitochondrial membrane lead to cytochrome c release, apoptosome
  assembly by APAF1, and CASP9 activation.
- **Execution**, where effector caspases such as CASP3, CASP6, and CASP7 cleave
  substrates that dismantle nuclear, cytoskeletal, and repair systems.
- **Restraint and checkpointing**, where anti-apoptotic BCL2 proteins, IAPs,
  c-FLIP/CFLAR, and survival kinases decide whether a stress or receptor signal
  is amplified into cell death.

Those arms should not all collapse to the same GO term. The top-level
`GO:0006915` term is often correct for a core executioner but too imprecise for
mechanistic curation; `positive regulation of apoptotic process` and `negative
regulation of apoptotic process` are often correct for direct regulators, but
are noisy when a paper only measured final cell death after a broad
perturbation.

## Immediate Goals

1. **Module boundaries**
   - Review the existing draft `intrinsic_apoptotic_signaling` and
     `death_receptor_apoptotic_signaling` modules.
   - Split reusable stages where useful: receptor/DISC assembly, BCL2-family
     MOMP control, apoptosome assembly, initiator-caspase activation, and the
     effector-caspase execution phase.
   - Keep direct apoptotic execution distinct from upstream survival signaling,
     generic stress responses, and regulation of neighboring death programs
     such as necroptosis.

2. **Top-level apoptosis annotations**
   - Find existing annotations to `GO:0006915` apoptotic process and ask whether
     the source supports a more specific stage such as intrinsic signaling,
     extrinsic death-receptor signaling, apoptosome assembly, caspase activation,
     or execution phase.
   - Use the exact human and mouse `GO:0006915` snapshot in
     [GO0006915](APOPTOSIS/GO0006915.md) as the first broad-row triage list.
   - Prioritize generic mammalian rows and caspase-family IBA/IEA propagation.
   - Defer trivial downcasts such as `neuron apoptotic process` unless the row
     also hides a mechanistic problem.

3. **Over-annotation from assays**
   - Treat caspase activity, TUNEL, annexin V/PI, mitochondrial depolarization,
     and viability assays as high-convergence phenotypic readouts unless the
     paper connects the gene product to a proximal apoptotic step.
   - Use the [ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md) readout rubric for
     evidence from cell-death assays.
   - Track APOPTOSIS-specific cases in
     [apoptosis readout over-annotation](APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.md).
   - Add recurring failure modes to [OVER_ANNOTATION_PATTERNS](OVER_ANNOTATION_PATTERNS.md)
     when a mouse or mammalian genetics paper licenses only a non-core survival
     phenotype but GOA asserts generic apoptosis.

## Scope

**Primary:** human and mouse, with a zebrafish exact-term audit as a first
non-mammalian vertebrate extension. Review human and mouse orthologs together
for the first mammalian slice so MGI phenotypes, GOA propagation, and human
biochemistry can be compared rather than curated in isolation; use the ZFIN
slice to find DANRE rows where embryonic cell-death assays have been lifted to
generic apoptosis, and use the InterPro slice to find broad domain-to-GO
mappings that should be challenged upstream.

**Comparators:** Drosophila, Caenorhabditis, budding/fission yeasts, and other
opisthokonts. Use these to understand conserved caspase/metacaspase,
BCL2-like, apoptosome-like, nuclease, and AIF/EndoG biology. Treat absence or
rewiring as a biological finding: metazoan intrinsic apoptosis is not simply
the mammalian CASP9/cytochrome-c pathway in every opisthokont, and fungal
programmed cell death should not be promoted to `apoptotic process` without
evidence that the GO definition is satisfied.

## Draft Modules

| Module | Status | Next check |
|---|---|---|
| [Intrinsic apoptotic signaling](../modules/intrinsic_apoptotic_signaling.html) | AUDITED DRAFT | Mammal-scope the CYCS/APAF1/CASP9 apoptosome and link out to the BCL2/MOMP and execution companion modules. |
| [Death receptor apoptotic signaling](../modules/death_receptor_apoptotic_signaling.html) | AUDITED DRAFT | Add TRAIL-R1/TRAIL-R2, TNFR1, CFLAR, and CASP10 variants around the FAS/FADD/CASP8 seed. |
| [Execution phase of apoptosis](../modules/apoptotic_execution_phase.html) | DRAFT | Expand beyond the CASP3/CASP6/CASP7, XIAP, DIABLO, DFFA-DFFB/CAD, ACIN1, and AIFM1 seed to lamins, PARP branches, and apoptotic surface exposure only after substrate reviews. |
| [BCL2-family MOMP control](../modules/bcl2_family_momp_control.html) | DRAFT | Expand the BAX/BAK, BCL2/BCL-xL/MCL1, and BID/BIM/PUMA/NOXA seed to the remaining mammalian BCL2-family paralogs. |
| Conserved non-mammalian apoptosis | TODO | Compare worm CED-3/CED-4/CED-9/EGL-1, Drosophila Ark/caspase/IAP wiring, and fungal metacaspase/AIF/EndoG systems before proposing any cross-opisthokont model. |

## Candidate Review Set

### Priority 1: Mammalian Core Machinery

| Species | Genes | Why first |
|---|---|---|
| human | CASP3, CASP6, CASP7, CASP8, CASP9, APAF1, CYCS | Core initiator and effector caspases plus apoptosome components; these define whether `GO:0006915` should be replaced by signaling- or execution-phase descendants. |
| human | BAX, BAK1, BCL2, BCL2L1, MCL1, BID, BCL2L11, BBC3, PMAIP1 | Direct BCL2-family control of MOMP; central to distinguishing intrinsic signaling from generic positive/negative regulation. |
| human | FAS, FASLG, FADD, TNFRSF1A, TNFSF10, TNFRSF10A, TNFRSF10B, CFLAR, CASP10 | Death-receptor/DISC branch and the CASP8 checkpoint that toggles apoptosis, survival, and necroptosis. |
| human | XIAP, DIABLO, DFFA, DFFB, ENDOG, AIFM1, ACIN1 | IAP control and downstream dismantling of the cell after effector-caspase activation. |

### Priority 2: Mouse Over-Annotation Slice

Start with reviewed mouse genes that already have dense apoptosis or survival
phenotype rows, then expand by querying mouse GOA for `GO:0006915` and
regulation descendants.

| Mouse gene | Review question |
|---|---|
| Bcl2 | Use the existing human and mouse BCL2 pair as the worked example for separating direct anti-apoptotic mitochondrial activity from a large tissue-development phenotyping tail. |
| Casp3 | Check whether generic `apoptotic process` and tissue-specific descendants can be tightened to execution-phase activity or kept as non-core developmental outcomes. |
| Tnfrsf1a | Distinguish TNF death-receptor apoptosis from NF-kappaB survival and necroptosis checkpoint biology. |
| Akt1, Mapk1 | Test survival-kinase rows for the common pattern where altered final cell death was curated as apoptosis regulation. |

### Priority 3: Conserved Opisthokont Comparators

- **C. elegans**: `ced-3`, `ced-4`, `ced-9`, `egl-1`, and <gene species="worm" symbol="cep-1">CEP-1</gene> for the
  compact core apoptosis circuit.
- **Drosophila**: initiator/effector caspases, Ark/Apaf-1, DIAP/IAP regulators,
  and Reaper/Hid/Grim-like IAP antagonists.
- **Fungi**: metacaspases, AIF/EndoG-like nucleases, and ER-stress-sensor death
  assertions where mammalian ER-stress apoptosis may have been propagated too
  far.

## Curation Heuristics

- **Tighten broad rows only with proximal evidence.** A CASP3 row to
  `GO:0006915` can often move to execution phase; an upstream kinase row usually
  needs evidence for a named BCL2, death-receptor, or apoptosome step before it
  should move deeper than generic regulation.
- **Separate direct regulators from outcome reporters.** Knockout survival,
  fewer TUNEL-positive cells, or less cleaved caspase-3 can justify a cautious
  process row, often non-core, but does not by itself name the substrate or
  complex the gene product acts on.
- **Do not conflate apoptosis with cell death.** A viability defect, necrosis
  assay, or mitochondrial depolarization readout needs orthogonal evidence
  before it can support apoptosis rather than another regulated or accidental
  death path.
- **Check taxon-specific wiring before accepting IBA.** Caspase-family and
  cytochrome c annotations are exactly where a PAINT node can be biologically
  meaningful in one animal clade and misleading in another branch.
- **Treat regulation terms as first-class when the mechanism is restraint.**
  BCL2, XIAP, and CFLAR can be direct apoptosis regulators even though their
  function is to prevent execution; the problem is unsupported distance, not
  regulation per se.

## Project Status

- [x] Audit the two existing draft apoptosis modules
- [x] Add missing execution/BCL2/MOMP module pieces
- [x] Query GOA for `GO:0006915` rows in human and mouse
- [x] Review the Priority 1 mammalian core genes
- [x] Review a first mouse over-annotation slice
- [x] Compare worm, fly, and fungal conserved components
- [x] Query GOA for `GO:0006915` rows in zebrafish and triage the ZFIN-authored exact rows

---

# STATUS

- [x] Project scope created
- [x] Mammal-first worklist prioritized
- [x] Existing draft modules audited
- [x] BCL2-family MOMP and execution-phase draft modules created and linked from the intrinsic seed
- [x] First gene review started: human CASP3 generic protein-binding rows re-reviewed; no validation warnings remain
- [x] CASP6 reviewed manually from cached primary literature, Reactome, UniProt, GOA, and GO-CAM evidence
- [x] CASP7 reviewed manually from cached primary literature, Reactome, UniProt, GOA, and GO-CAM evidence
- [x] CASP8 reviewed manually from cached primary literature, Reactome, UniProt, GOA, GO-CAM evidence, and annotation-reviewer follow-up
- [x] CASP9 reviewed manually from cached primary literature, Reactome, UniProt, GOA, GO-CAM evidence, and annotation-reviewer follow-up
- [x] APAF1 reviewed manually from cached primary literature, Reactome, UniProt, GOA, and annotation-reviewer follow-up
- [x] CYCS reviewed manually from cached primary literature, Reactome, UniProt, GOA, and annotation-reviewer follow-up
- [x] BAX reviewed manually from cached primary literature, Reactome, UniProt, GOA, and annotation-reviewer follow-up
- [x] BAK1 reviewed manually from cached primary literature, Reactome, UniProt, GO-CAM evidence, and annotation-reviewer follow-up
- [x] Existing human BCL2 review revalidated for the BCL2-family MOMP slice
- [x] Existing human BCL2L1 review revalidated for the BCL2-family MOMP slice
- [x] MCL1 reviewed manually from cached primary literature, UniProt, PAINT/PANTHER evidence, and annotation-reviewer follow-up
- [x] BID reviewed manually from cached primary literature, Reactome, UniProt, GO-CAM, PAINT/PANTHER evidence, and annotation-reviewer follow-up
- [x] BCL2L11 reviewed manually from cached primary literature, Reactome, UniProt, PAINT/PANTHER evidence, and annotation-reviewer follow-up
- [x] BBC3 reviewed manually from cached primary literature, Reactome, UniProt, GOA, and annotation-reviewer follow-up
- [x] PMAIP1 reviewed manually from cached primary literature, Reactome, UniProt, PAINT/PANTHER evidence, and annotation-reviewer follow-up
- [x] Existing human FAS review revalidated and generic partner-specific protein-binding imports resolved with annotation-reviewer follow-up
- [x] FASLG reviewed manually from cached primary literature, Reactome, UniProt, GOA, GO-CAM, PANTHER evidence, and annotation-reviewer follow-up
- [x] FADD reviewed manually from cached primary literature, Reactome, UniProt, GOA, GO-CAM, PANTHER evidence, and annotation-reviewer follow-up
- [x] Existing human TNFRSF1A review refreshed after GOA update; 12 new protein-binding imports resolved with annotation-reviewer follow-up
- [x] TNFSF10 reviewed manually from cached primary literature, Reactome, UniProt, GO-CAM, and annotation-reviewer follow-up
- [x] TNFRSF10A reviewed manually from cached primary literature, Reactome, UniProt, GOA, GO-CAM, PANTHER evidence, and annotation-reviewer follow-up
- [x] TNFRSF10B reviewed manually from cached primary literature, Reactome, UniProt, GOA, GO-CAM, PANTHER evidence, and annotation-reviewer follow-up
- [x] CFLAR reviewed manually from cached primary literature, Reactome, UniProt, PANTHER/PAINT evidence, and annotation-reviewer follow-up
- [x] CASP10 reviewed manually from cached primary literature, Reactome, UniProt, GO-CAM, PANTHER/PAINT evidence, and annotation-reviewer follow-up
- [x] XIAP reviewed manually from cached primary literature, UniProt, GOA, PANTHER/PAINT evidence, and annotation-reviewer follow-up
- [x] DIABLO reviewed manually from cached primary literature, Reactome, UniProt, PANTHER/PAINT evidence, and annotation-reviewer follow-up
- [x] DFFA reviewed manually from cached primary literature, Reactome, UniProt, PANTHER/PAINT evidence, and annotation-reviewer follow-up
- [x] DFFB reviewed manually from cached primary literature, Reactome, UniProt, PANTHER/PAINT evidence, and annotation-reviewer follow-up
- [x] ENDOG reviewed manually from cached primary literature, UniProt, PANTHER/PAINT evidence, and annotation-reviewer follow-up
- [x] Existing human AIFM1 review revalidated after a GOA/PANTHER refresh and annotation-reviewer follow-up
- [x] Existing human ACIN1 review refreshed after GOA update and annotation-reviewer follow-up
- [x] Existing mouse Bcl2 review refreshed after GOA update and annotation-reviewer follow-up
- [x] Existing mouse Casp3 review refreshed after GOA update and annotation-reviewer follow-up
- [x] Existing mouse Tnfrsf1a review refreshed after GOA update and annotation-reviewer follow-up
- [x] Existing mouse Akt1 review refreshed after GOA update, manual cached-publication research, GO-CAM comparison, and annotation-reviewer follow-up
- [x] Existing mouse Mapk1 review refreshed after GOA update, manual cached-publication research, GO-CAM comparison, and annotation-reviewer follow-up
- [x] Mouse Casp9 reviewed manually as the intrinsic initiator-caspase extension of the `GO:0006915` audit
- [x] Mouse Casp8 reviewed manually as the death-receptor initiator-caspase extension of the `GO:0006915` audit
- [x] Worm ced-3 reviewed as the first conserved CED pathway comparator
- [x] Worm ced-4 reviewed as the conserved CED apoptosome adaptor comparator
- [x] Worm ced-9 reviewed as the conserved CED BCL2-family apoptosis inhibitor comparator
- [x] Worm egl-1 reviewed as the conserved CED BH3-only apoptosis activator comparator
- [x] Worm <gene species="worm" symbol="cep-1">CEP-1</gene> reviewed as the conserved p53-family DNA-damage apoptosis comparator
- [x] Zebrafish exact `GO:0006915` rows fetched from QuickGO and ZFIN-authored rows triaged for assay-readout over-annotation
- [x] Drosophila <gene species="DROME" symbol="Dronc">Dronc</gene> reviewed as the conserved Dark-apoptosome initiator-caspase comparator
- [x] Drosophila <gene species="DROME" symbol="Dark">Dark</gene> reviewed as the conserved Apaf-1/CED-4 apoptosome adaptor comparator
- [x] Drosophila <gene species="DROME" symbol="DrICE">DrICE</gene> reviewed as the conserved effector-caspase execution comparator
- [x] Drosophila <gene species="DROME" symbol="Dcp-1">Dcp-1</gene> reviewed as the companion conserved effector-caspase execution comparator
- [x] Drosophila <gene species="DROME" symbol="Diap1">Diap1</gene> reviewed as the conserved IAP caspase-inhibition, ubiquitin-ligase, and NEDD8-ligase comparator
- [x] Drosophila <gene species="DROME" symbol="Diap2">Diap2</gene> reviewed as the conserved IAP/Imd-pathway ubiquitin-ligase comparator
- [x] Drosophila <gene species="DROME" symbol="rpr">rpr</gene> reviewed as the conserved Reaper/RHG IAP-antagonist comparator
- [x] Drosophila <gene species="DROME" symbol="hid">hid</gene> reviewed as the conserved Hid/RHG IAP-antagonist comparator
- [x] Drosophila <gene species="DROME" symbol="grim">grim</gene> reviewed as the conserved Grim/RHG IAP-antagonist comparator
- [x] Drosophila <gene species="DROME" symbol="skl">skl</gene> reviewed as the conserved Sickle/RHG IAP-antagonist comparator
- [x] Budding yeast <gene species="yeast" symbol="MCA1">MCA1</gene> reviewed as the fungal metacaspase programmed-cell-death and protein-quality-control comparator
- [x] Budding yeast <gene species="yeast" symbol="NUC1">NUC1</gene> reviewed as the fungal EndoG-like mitochondrial nuclease, apoptotic-DNA-fragmentation, and meiotic viral-defense comparator
- [x] Budding yeast <gene species="yeast" symbol="IRE1">IRE1</gene> reviewed as the fungal ER-stress UPR comparator and stale ER-stress-apoptosis IBA audit
- [x] Hypocrea/Trichoderma <gene species="HYPJE" symbol="IRE1">IRE1</gene> reviewed as the filamentous-fungal ER-stress UPR comparator and stale TRAF2/ASK1 death-arm TreeGrafter audit
- [x] Exact human and mouse `GO:0006915` QuickGO rows fetched, normalized, and summarized

# NOTES

## 2026-10-01

- Extended the mouse exact-`GO:0006915` audit to the two top-ranked initiator
  caspases left after the first over-annotation slice. `Casp9` was centered on
  APAF1-apoptosome recruitment and effector-procaspase maturation: inherited
  broad apoptosis rows were tightened to intrinsic apoptotic signaling, while
  stimulus-, stress-, tissue-, and c-Abl-binding transfers that could not be
  checked from cached abstracts were left non-core, over-annotated, or
  unresolved.
- Completed the new mouse `Casp8` review with annotation-reviewer follow-up.
  Generic `GO:0006915 apoptotic process` imports were scoped to
  `GO:0008625 extrinsic apoptotic signaling pathway via death domain receptors`;
  the direct PIDD row was marked over-annotated because the cited study does not
  detect procaspase-8 processing in PIDD-expressing MEFs; execution-phase rows
  were replaced by `GO:0051604 protein maturation`; and the anti-necroptotic
  RIPK1/CYLD/gasdermin/N4BP1 cleavage branches were kept as direct but
  apoptosis-adjacent functions.

## 2026-09-30

- Queried QuickGO for exact `GO:0006915` rows in human and mouse with
  descendant usage disabled. The snapshot found 825 human rows across 345
  displayed symbols and 557 mouse rows across 238 displayed symbols; the
  normalized TSVs, raw JSON, and symbol rollups are under
  [APOPTOSIS/go0006915](APOPTOSIS/go0006915/), with a concise summary in
  [APOPTOSIS/GO0006915.md](APOPTOSIS/GO0006915.md).
- Added companion draft modules for BCL2-family MOMP control and the mammalian
  apoptotic execution phase. The BCL2/MOMP module expands the BAX/BCL2
  placeholder into BAX/BAK effectors, BCL2/BCL2L1/MCL1 guardians, and
  BID/BCL2L11/BBC3/PMAIP1 BH3-only activator/sensitizer leaves; the execution
  module separates CASP3/CASP6/CASP7 proteolysis, XIAP/DIABLO restraint,
  DFFA-DFFB/CAD DNA fragmentation, and ACIN1/AIFM1 nuclear remodeling from
  upstream death-receptor and apoptosome signaling.
- Audited the two existing draft apoptosis modules against the completed gene
  reviews and cached GO-CAM models. The intrinsic draft now records explicit
  BCL2/MOMP, mammalian CYCS/APAF1/CASP9, and execution-phase handoff gaps; the
  death-receptor draft now records TRAIL-R1/TRAIL-R2, TNFR1, and CFLAR/CASP10
  expansion gaps and grounds its FAS/FADD/CASP8 seed in the production
  FASL-FAS GO-CAM.
- Re-audited the human CASP6 review after a current GOA refresh and
  annotation-reviewer follow-up. The source set was unchanged at 256 GOA rows;
  the review still removes the high-throughput `GO:0005515` rows and keeps the
  ZBP1/RIPK3 molecular-adaptor assertion, and the two accepted top-level
  `GO:0006915` rows were tightened to `GO:0097194 execution phase of
  apoptosis`.
- Completed the budding yeast <gene species="yeast" symbol="MCA1">MCA1</gene> review by centering
  Mca1 on Ca(2+)-stimulated Arg/Lys metacaspase activity, prion-domain
  recruitment to cytosolic insoluble protein aggregates, core protein quality
  control, and fungal apoptotic programmed cell death under H2O2,
  chronological-aging, and mRNA-decay stress. The broad `GO:0006915` rows were
  accepted as metacaspase-dependent yeast apoptosis rather than narrowed to
  metazoan execution-phase terms.
- Completed the budding yeast <gene species="yeast" symbol="NUC1">NUC1</gene> review by centering
  Nuc1 on mitochondrial inner-membrane DNA/RNA nuclease activity, fungal
  EndoG-like apoptotic DNA fragmentation, and meiotic cytosolic defense against
  L-A/Killer dsRNA mycoviruses. The 2026 `mitophagy` and `regulation of
  mitochondrial DNA metabolic process` rows were narrowed to
  `GO:0032043 mitochondrial DNA catabolic process`, because Nuc1 degrades
  mtDNA exposed by a mitophagy-vacuolar escape route rather than operating the
  Atg11/Atg32 mitophagy machinery.
- Completed the budding yeast <gene species="yeast" symbol="IRE1">IRE1</gene> review by keeping the
  adaptive Ire1-Hac1 unfolded-protein-response kinase/RNase activities as core
  and marking the GO_Central `GO:0070059 intrinsic apoptotic signaling pathway
  in response to endoplasmic reticulum stress` IBA as over-annotated. The
  current PANTHER cache places the death term on a mouse ERN-supported node,
  while the yeast protein remains on the conserved fungal/eukaryotic UPR sensor node;
  broad catalytic, kinase, RNase, nucleotide-binding, metal-binding, and generic
  DCR2 `protein binding` imports were cleaned before marking the review
  complete.
- Completed the Hypocrea/Trichoderma <gene species="HYPJE" symbol="IRE1">IRE1</gene> review by
  keeping the adaptive fungal ER-stress kinase/RNase UPR functions as core,
  preserving the obsolete `GO:0051082 unfolded protein binding` rows as
  `MODIFY` to `GO:0002235 detection of unfolded protein`, and tightening broad
  catalytic, kinase, RNase, nucleotide-binding, and metal-binding IEAs. The
  TreeGrafter ER-stress apoptosis row remains over-annotated as a mammalian
  ERN-branch import to fungal SF6, while the `GO:1990604` TRAF2/ASK1 complex
  row is removed outright because Trichoderma lacks the required TRAF2 and
  ASK1/MAP3K5 partners.
- Completed the Drosophila <gene species="DROME" symbol="Dronc">Dronc</gene> review by separating
  core Dark-apoptosome signaling and DrICE activation from DIAP1 substrate-side binding,
  local nonapoptotic caspase proteolysis, Eiger-specific apoptosis, and atypical programmed necrosis.
- Completed the Drosophila <gene species="DROME" symbol="Dark">Dark</gene> review by centering its
  cytosolic NB-ARC/CARD/WD40 apoptosome scaffold activity, narrowing broad
  apoptosis rows to Dronc-activating apoptotic signaling, keeping direct
  spermatid, chaeta, glial, gamma-radiation, and salivary histolysis outputs as
  non-core, and marking systemic necrosis/inflammation/metabolism phenotypes as
  over-annotated rather than direct Dark functions.
- Completed the Drosophila <gene species="DROME" symbol="DrICE">DrICE</gene> review by centering its
  cytoplasmic C14 cysteine-endopeptidase activity in the execution phase of
  apoptosis, narrowing top-level apoptosis and programmed-cell-death rows to
  execution phase, converting generic DIAP interaction rows to BIR-domain
  binding, removing substrate-side Dronc protein-binding rows, keeping
  spermatid, nurse-cell, SOP-patterning, and innate-immune cleavage outputs as
  non-core, and marking a PAINT neuron-apoptosis propagation as over-specific.
- Completed the Drosophila <gene species="DROME" symbol="Dcp-1">Dcp-1</gene> review by centering its
  short-prodomain C14 cysteine-endopeptidase activity in apoptotic execution,
  narrowing top-level apoptosis and programmed-cell-death rows to execution
  phase, moving broad ovarian transport, starvation, and oogenesis rows toward
  nurse-cell apoptosis or macroautophagy, keeping SesB/mitochondrial
  localization, Toll/NF-kappaB repression, and neuromuscular degeneration as
  non-core outputs, removing neuronal RNP granule rows caused by
  decapping-protein `Dcp1` symbol confusion, and leaving abstract-only
  BIR-domain and neuron-remodeling rows unresolved.
- Completed the Drosophila <gene species="DROME" symbol="Diap1">Diap1</gene> review by centering
  DIAP1/thread on BIR-domain caspase inhibition plus RING-dependent ubiquitin
  and NEDD8 ligase activities. The curation narrows generic Dronc, DrICE, and
  Dcp-1 binding rows to caspase binding where the partner was visible; tightens
  broad catalytic and top-level apoptosis rows; keeps RHG, Jafrac2, dOmi/HtrA2,
  border-cell, SOP, Grim, DTRAF1/JNK, and Wg/Wnt branches as non-core; and marks
  spermatid nuclear differentiation, Toll signaling, Eiger/JNK, and a
  survivin-like cell-cycle PAINT transfer as over-annotated or incorrect for
  DIAP1.
- Completed the Drosophila <gene species="DROME" symbol="Diap2">Diap2</gene> review by centering
  its RING-dependent K63 ubiquitin ligase role in the peptidoglycan/Imd innate
  immune pathway. The curation keeps direct DrICE binding and inhibition as a
  secondary apoptotic-threshold branch, removes generic Hid/Reaper/Grim
  `GO:0005515` interactions, narrows broad catalytic imports to ubiquitin
  protein ligase activity, downgrades organismal Gram-negative defense outputs
  to non-core, and leaves abstract-only DIAP1-degradation and Grim-ubiquitination
  rows unresolved rather than flattening them into the better-supported DREDD,
  IMD, and Kenny K63-linked ubiquitination mechanism.
- Completed the Drosophila <gene species="DROME" symbol="rpr">rpr</gene> review by centering
  Reaper on DIAP1 IAP antagonism, GH3/phospholipid-dependent mitochondrial
  outer-membrane association, and UbcD1-dependent DIAP1 autoubiquitination and
  turnover. The curation narrows broad apoptosis rows to apoptotic signaling,
  keeps ecdysone, midgut, salivary-gland, neuroblast, JNK, and DNA-damage rows
  as contextual non-core branches, narrows generic Reaper-DIAP2 binding to
  ubiquitin protein ligase binding, removes the substrate-side dBruce row, and
  leaves several abstract-only Sickle, dOmi, DmIKKepsilon, and CNS-remodeling
  rows unresolved.
- Completed the Drosophila <gene species="DROME" symbol="hid">hid</gene> review by centering
  Head involution defective on mitochondrial RHG-family antagonism of DIAP1 and
  DIAP2 BIR domains. The curation narrows broad apoptosis/programmed-cell-death
  rows to apoptotic signaling, narrows visible DIAP protein-binding rows to
  ubiquitin-protein-ligase or BIR-domain binding, keeps supported tracheal,
  midgut, macroautophagy, DNA-damage, and Ack-buffered developmental contexts as
  non-core or accepted outputs, marks generic ecdysone, organ-growth, radiation,
  and larval/pupal-development rows as over-annotated, and leaves abstract-only
  sex-differentiation, circadian, autophagic-cell-death, and localization rows
  unresolved.
- Completed the Drosophila <gene species="DROME" symbol="grim">grim</gene> review by centering
  Grim on RHG-family BIR-domain binding to DIAP1/DIAP2-family IAPs plus a
  separable GH3-dependent mitochondrial route. The curation narrows top-level
  apoptosis and programmed-cell-death rows to apoptotic signaling, replaces the
  DIAP2 `GO:0005515` row with `BIR domain binding`, broadens mitochondrial
  matrix localization to mitochondrion, broadens cytochrome-c release to
  apoptotic mitochondrial changes because Drosophila Grim redistributes
  cytochrome c rather than detectably releasing it to cytosol, keeps supported
  Malpighian and neuronal/glial developmental contexts as non-core or accepted
  outputs, and leaves abstract-only Sickle, lifespan, melanization, larval CNS
  remodeling, and localization rows unresolved.
- Completed the Drosophila <gene species="DROME" symbol="skl">skl</gene> review by centering
  Sickle on N-terminal IAP-binding-motif binding to DIAP1 and DIAP2 BIR
  domains. The curation adds a missing `GO:1990525 BIR domain binding`
  molecular-function row, narrows six top-level apoptosis rows to
  `GO:0097190 apoptotic signaling pathway`, keeps the corazonergic-neuron
  developmental PCD row as non-core, and leaves the Trends in Genetics
  DOI-only NAS row plus the abstract-only ionizing-radiation row unresolved.
- Completed the worm <gene species="worm" symbol="cep-1">CEP-1</gene> review by centering its nuclear
  p53-family transcription activator role upstream of `egl-1` and `ced-13`.
  Generic DNA-binding and transcription rows were narrowed toward Pol
  II-specific transcription activator terms; the core DNA-damage rows to
  `intrinsic apoptotic signaling pathway in response to DNA damage by p53 class
  mediator` were accepted or narrowed there from broader parents; PRMT-5/CBP-1
  repression and IRE-1/ER-stress apoptosis were retained as secondary contexts;
  and hypoxia, starvation, lifespan, meiotic segregation, paraquat/SMG-1, old
  RAD-51 IGI, zinc-binding, and nucleolar rows were kept non-core,
  over-annotated, or unresolved according to how directly the cached evidence
  supported direct action by the protein.

- Completed the worm egl-1 review by centering EGL-1 on BH3-mediated
  inhibition of the BCL2-family survival protein CED-9. The five generic
  `GO:0005515 protein binding` rows to CED-9 were narrowed to a proposed
  BH3-ligand-side pro-survival BCL2-family inhibitor activity rather than the
  directionally wrong CED-9-side `BH3 domain binding`; broad
  `positive regulation of programmed cell death` rows were tightened to
  apoptosis; and the generic CED-4-complex assembly row was moved to apoptotic
  signaling. The local EGL-1/CED-9/CED-4/CED-3 synapse-pruning branch and
  EGL-1-dependent mitochondrial fragmentation were retained as non-core, while
  Salmonella defense and PIG-1 cell-extrusion endpoints were kept out of the
  core apoptotic-signaling model.

- Completed the worm ced-9 review by centering CED-9 on mitochondrial
  sequestration of CED-4 and EGL-1 BH3-domain recognition. Generic
  `GO:0005515` rows to EGL-1 were narrowed to `BH3 domain binding`; CED-4
  binding rows were narrowed to `protein sequestering activity`; broad
  `apoptotic process` rows were moved to `negative regulation of apoptotic
  process`; and BCL2-family PAINT transfers for cytochrome c release,
  channel/transmembrane transport, and ligandless extrinsic apoptotic signaling
  were removed as mammalian or unsupported leak-throughs. Synapse-pruning and
  DRP-1/FZO-1 mitochondrial-dynamics rows were retained as real but non-core
  branches, while Salmonella defense, PIG-1 cell shedding, DCT-1/ceBNIP3
  binding, and CSP-2/CSP-3 substrate-control rows were kept out of the core
  CED-9 model.

- Completed the worm ced-4 review by centering CED-4 on ATP/Mg-bound
  apoptosome assembly and CED-3 zymogen activation rather than top-level
  apoptosis. The curation narrows generic `GO:0006915`,
  `positive regulation of apoptotic process`, and peptidase/protein-processing
  rows to apoptotic signaling or apoptotic cysteine-endopeptidase activator
  activity; replaces supported CED-3 `GO:0005515 protein binding` rows with
  caspase binding; removes most generic CED-9, SUN-1, MAC-1, FEM-1, and viral
  E1B interaction rows; keeps viral E1B BH-domain binding as non-core; accepts
  mitochondrial and apoptotic perinuclear localization; and keeps local
  CED-pathway synapse pruning plus CED-4-dependent cell-size control separate
  from canonical whole-cell apoptosis.

- Completed the worm ced-3 review as the first conserved non-mammalian
  comparator. The curation centers CED-3 on CED-4-apoptosome-mediated caspase
  zymogen activation and execution-phase substrate cleavage; narrows broad
  `GO:0006915`, `programmed cell death`, generic peptidase, and protein
  processing rows; removes nearly all generic `GO:0005515 protein binding`
  interactor rows except the early CED-3/CED-4 CARD-domain interaction; removes
  CSP-2/CSP-3/NPP-14 inhibitory interactions from activator and
  negative-regulation terms that belong on the inhibitors; keeps the GSNL-1
  synapse-pruning and LIN-14/LIN-28/DISL-2 heterochronic cleavage branches as
  direct but non-core proteolytic outputs; and marks Salmonella defense, PIG-1
  cell-shedding, manganese-response, and adult muscle-homeostasis assertions as
  over-annotated or unresolved phenotype endpoints.

- Refreshed the existing mouse Mapk1 review after a GOA update. The curation
  resolves 18 newly seeded rows: it accepts refreshed nucleoplasm, cytoplasm,
  cytosol, and ERK1/ERK2-cascade source rows; keeps regulation of ossification
  and myelination as non-core developmental outputs; removes four generic
  `GO:0005515 protein binding` partner rows; narrows the DUSP6/MKP-3 row to
  `GO:0019902 phosphatase binding`; marks transferred cholesterol-biosynthesis
  and Smoothened-signaling rows as over-annotated endpoint assertions; narrows
  three `GO:0106310 protein serine kinase activity` rows to
  `GO:0004707 MAP kinase activity`; and drops seven stale ARBA/IEA source
  assertions that were superseded by the refreshed GOA snapshot.

- Refreshed the existing mouse Akt1 review after a GOA update. The curation
  resolves 32 newly seeded rows: it accepts refreshed PAINT and orthology
  support for core serine/threonine kinase activity and cytosol/plasma-membrane
  localization; keeps osteoblast differentiation, Cntnap2/Akt-mTOR
  inflammatory/pain responses, TSC/IRS PI3K-AKT signaling, TORC1, cilium,
  eNOS, and mitochondrial-localization assertions as non-core pathway context;
  accepts UniProt EXP `GO:0106310 protein serine kinase activity` rows for
  GSK3B, cGAS, and MICU1 phosphorylation; removes three generic
  `GO:0005515 protein binding` rows; and drops three stale PAINT/IEA source
  assertions that were superseded by the refreshed GOA snapshot.

- Refreshed the existing mouse Tnfrsf1a review after a GOA update. The curation
  is now complete and validates cleanly after 18 rat/human ISO rows received
  structured propagation-review metadata. It accepts newly surfaced TNF
  receptor activity, TNF binding, TNF-mediated signaling, TNF receptor
  superfamily complex, and extracellular-region source rows; removes six new
  generic `GO:0005515 protein binding` partner rows and migrates legacy
  Tnfrsf1a generic-binding rows to `REMOVE`; narrows a broad ARBA `response to
  lipopolysaccharide` row to `GO:0071222 cellular response to
  lipopolysaccharide`; marks an ARBA `cellular response to lipid` row as
  over-annotated; and drops nine stale source assertions no longer present in
  the refreshed GOA snapshot.
- Refreshed the existing mouse Casp3 review after a GOA update. The curation
  is now complete after adding propagation-review metadata to 21 rat/human ISO
  transfers. It accepts refreshed cysteine-type endopeptidase,
  cytoplasm/cytosol, proteolysis, broad apoptotic-process, and execution-phase
  source rows; keeps newly surfaced human-ortholog nucleus, GSDME-linked
  pyroptotic inflammatory response, protein maturation,
  regulation-of-protein-localization, and PIDD apoptotic-signaling rows as
  non-core; modifies broad `GO:0008233 peptidase activity` to `GO:0004197
  cysteine-type endopeptidase activity`; removes the new RPS18 `GO:0005515
  protein binding` IntAct row from a substrate screen; drops nine stale source
  assertions no longer present in the refreshed GOA snapshot; and preserves
  three intentional mixed-action warnings for abstract-only evidence rows.
- Refreshed the existing mouse Bcl2 review after a GOA update. The curation now
  has no pending rows and validates cleanly, accepts newly surfaced
  PAINT/ortholog mitochondrial outer-membrane and BCL-2 complex transfers,
  removes the new Gimap3 `GO:0005515 protein binding` row as generic IntAct
  evidence, accepts the Fnip1-rescue apoptosis row from full PMID:22709692 text,
  leaves all seven PMID:15613488 ER-calcium/IP3R rows `UNDECIDED` because the
  cached source is abstract-only, narrows a broad transferred molecular-adaptor
  row to BH3-domain binding, narrows an ARBA neuron-apoptosis parent to negative
  regulation, and drops five stale source assertions no longer present in the
  refreshed GOA snapshot.
- Refreshed the existing human ACIN1 review after a GOA update. The curation
  preserves ACIN1's core nuclear RNA-binding/ASAP/EJC-associated splicing role
  and caspase-activated apoptotic chromatin-condensation role; refreshes UniProt
  and GOA source snapshots; reviews five newly imported RNPS1/PNN generic
  `protein binding` rows; migrates older SF3A2, PCBD1, SRPK2, PNN, and RBM5
  generic interaction rows from the legacy over-annotation action to `REMOVE`;
  and removes generic `enzyme binding` because CASP3 cleavage makes ACIN1 a
  substrate, not a separate enzyme-binding factor. The Drosophila Acinus
  autophagy signal remains a human follow-up question rather than a new human
  autophagy annotation.
- Revalidated the existing human AIFM1 review. The completed curation preserves
  77 reviewed GOA rows and separates three core functions: mitochondrial
  FAD/NADH oxidoreduction, NADH-dependent AIF anchoring and activation of
  CHCHD4/MIA40 for mitochondrial disulfide-relay import, and released nuclear
  DNA/PAR-dependent death-effector activity. It keeps broad apoptosis and
  programmed-cell-death rows where AIF does direct prodeath work, removes or
  tightens generic protein-binding and oxidoreductase rows, and intentionally
  leaves rat stimulus transfers, peroxide-specific NAD(P)H oxidase chemistry,
  respiratory-chain complex assembly placement, and the necroptosis boundary as
  curator follow-up questions.
- Completed the human ENDOG review. The curation centers ENDOG on
  Mg-dependent DNA/RNA endonuclease activity in mitochondria and the nucleus,
  accepts direct human evidence for 5hmC-modified DNA cleavage/recombination,
  mitochondrial DNA catabolism with compensatory mtDNA replication, and
  starvation autophagy, adds a conservative `14-3-3 protein binding` row for the
  YWHAG-dependent mTORC1-suppression mechanism, narrows broad nuclease,
  hydrolase, metal-binding, DNA-catabolism, and TOR rows, keeps apoptotic DNA
  fragmentation as a plausible non-core ENDOG branch, removes generic
  DNAJA4/ITLN2 interactome `protein binding` rows, and marks rat-derived
  stimulus and neuron-localization transfers as over-annotation.
- Completed the human DFFB/CAD review. The curation centers DFFB on its
  caspase-released DNA endonuclease activity in apoptotic oligonucleosomal DNA
  fragmentation, narrows broad nuclease/hydrolase rows to `DNA endonuclease
  activity`, narrows generic `DNA catabolic process` and top-level
  `apoptotic process` rows to `apoptotic DNA fragmentation`, removes the
  DFFA-specific `negative regulation of apoptotic DNA fragmentation` assertion,
  removes generic DFFA `protein binding` rows, keeps DNA binding, TOP2A enzyme
  binding, DFF complex membership, homodimerization, and HPA nucleolus rows as
  non-core, and retains chromatin, nuclear/nucleoplasmic, and cytosolic
  locations needed for the DFF40:DFF45 activation model.
- Completed the human DFFA/ICAD review. The curation keeps DFFA as the
  DFFB/CAD-specific folding chaperone and deoxyribonuclease inhibitor in the DFF
  complex, explicitly avoiding any CAD nuclease assertion on DFFA itself; adds
  `protein folding chaperone` and `protein folding` as conservative new
  annotations for CAD folding; accepts `negative regulation of apoptotic DNA
  fragmentation`, `deoxyribonuclease inhibitor activity`, and cytosolic,
  nucleoplasmic, and chromatin localization; narrows broad top-level apoptosis
  rows to CAD-dependent apoptotic DNA-fragmentation inhibition; removes
  high-throughput or otherwise generic DFFB, HSPB1, and TSPYL4 `protein binding`
  rows; and keeps generic `protein-containing complex` only as a non-core
  placeholder pending a DFF-specific complex term.
- Completed the human DIABLO/SMAC review. The curation centers DIABLO on
  mitochondrial IAP antagonism after PARL maturation and MOMP-dependent cytosolic
  release; removes most `protein binding` rows from survivin, ARTS-context,
  AREL1, PKCdelta, Livin degradation, and large interactome evidence; narrows
  core XIAP, cIAP1, ML-IAP/Livin, and BIRC6/BRUCE edges to broad
  `molecular function inhibitor activity` until GO has a specific IAP-antagonist
  MF; tightens top-level apoptosis rows to `intrinsic apoptotic signaling
  pathway`; keeps mitochondrion, mitochondrial intermembrane space, and cytosol
  locations; removes mouse-transferred CD40-complex localization; and drops an
  unsupported `survivin complex` row.
- Completed the human XIAP review. The curation centers XIAP on direct BIR2/BIR3
  inhibition of apoptotic caspases and on RING-domain E3 ligase activity;
  narrows broad ubiquitin-transfer rows to `ubiquitin protein ligase activity`;
  keeps RIPK2/NOD, TLE/Groucho Wnt, COMMD1/CCS copper, and IRF7 antiviral
  ubiquitination branches with non-apoptotic context where appropriate; accepts
  negative regulation of apoptosis rows supported by direct caspase inhibition;
  removes high-throughput generic protein-binding rows; and removes or demotes
  rows for SMAC/DIABLO, HTRA2/3/4, ARTS, SIAH1, XAF1, TRIM32, and USP19 where
  the cited interactor antagonizes or degrades XIAP rather than representing an
  XIAP molecular function.
- Completed the human CASP10 review. The curation keeps CASP10 as a
  catalytically active tandem-DED initiator caspase recruited through FADD to
  Fas/CD95 and TRAIL death-inducing signaling complexes; narrows top-level
  apoptosis and generic DED regulation imports to the death-domain-receptor
  extrinsic pathway; retains CD95 DISC, ripoptosome, cytosolic Reactome, CARP
  E3-binding, and prodomain NF-kappaB rows with non-core context where needed;
  converts the c-FLIP(L) myeloma interaction to negative regulation of
  autophagic cell death; and removes high-throughput or generic RIOK3, XIAP,
  SERPINB9, and RIPK1 protein-binding rows.
- Completed the human CFLAR/c-FLIP review. The curation centers c-FLIP
  isoforms on tandem-death-effector-domain assembly with FADD and
  CASP8/CASP10, explicitly separates FLIP(L) pseudo-caspase heterodimers from
  DED-only FLIP(S) caps, removes PANTHER and InterPro catalytic-caspase
  propagation to the inactive pseudoenzyme, keeps DISC/CD95 DISC/ripoptosome
  component rows, proposes the missing CASP8 inhibitor and negative-necroptosis
  child terms, and marks the large rat/mouse Compara tissue and stimulus tail
  as over-annotation from downstream phenotypes.
- Completed the human TNFRSF10B/TRAIL-R2 review. The curation centers DR5 on
  `GO:0036463 TRAIL receptor activity` at the plasma membrane in
  `TRAIL-activated apoptotic signaling pathway`; narrows generic TRAIL
  ligand-binding imports, broad death-receptor and signaling ancestors, and
  direct TRAIL ligand rows to the receptor activity or TRAIL pathway; removes
  HuRI partner edges as uninformative DR5 molecular-function rows; leaves
  abstract-only sensitization and anti-apoptotic-complex imports undecided;
  marks ER-stress, mechanical-stimulus, TP53, and c-FLIP/CASP8 downstream
  assertions as over-annotations; and keeps the DR5-specific Reactome
  procaspase-8 dimerization event that was intentionally rejected for
  TNFRSF10A.
- Completed the human TNFRSF10A/TRAIL-R1 review. The curation centers DR4 on
  `GO:0036463 TRAIL receptor activity` at plasma-membrane rafts in
  `TRAIL-activated apoptotic signaling pathway`; narrows generic death
  receptor, signaling receptor, TRAIL-binding, self-oligomerization, and
  DISC co-complex rows to that activity or the TRAIL pathway; keeps
  GODZ/ZDHHC3 and ARAP1 evidence as trafficking context; marks DR5-only,
  c-FLIP/CASP8, and TP53-transcription Reactome exports as too indirect for a
  mature DR4 plasma-membrane assertion; and leaves abstract-only DR5-peptide
  and interferon AP-MS imports undecided rather than overruling the curator from
  incomplete local evidence.
- Completed the human TNFSF10/TRAIL review. The curation centered TRAIL on a
  membrane-bound or soluble TNF-family homotrimer that binds TNFRSF10A/DR4 and
  TNFRSF10B/DR5 to initiate `TRAIL-activated apoptotic signaling pathway`;
  narrowed generic receptor-binding, `protein binding`, top-level apoptosis,
  cell-communication, and signal-transduction rows to TNF receptor binding or
  the TRAIL-specific pathway; removed the downstream CUL3/caspase-8 interaction
  import; kept zinc coordination, identical subunit binding, NF-kappaB
  activation, immune response, and exosome detection as non-core contexts; and
  marked cytochrome-c release as a downstream over-annotation through the
  BID/BAX/BAK mitochondrial arm.
- Refreshed the existing human TNFRSF1A review after QuickGO added 12 new
  generic `protein binding` rows. New TRADD, RIPK1, RFK, and SH3RF2 rows were
  folded into `tumor necrosis factor receptor activity`; GRN/progranulin,
  UBB, MON2, and BioPlex-only rows were removed rather than pointed at TNF
  binding or kept as bare interaction edges; and the core-function synthesis
  was retargeted from unreviewed parent processes to the already accepted
  `positive regulation of canonical NF-kappaB signal transduction` and
  `extrinsic apoptotic signaling pathway via death domain receptors` terms.
- Completed the human FADD review. The curation centered FADD on its
  DD-to-DED adaptor role bridging activated FAS/TRAIL/TNFR death receptors to
  CASP8/CASP10-containing death-inducing signaling complexes; narrowed broad
  `protein binding`, `protease binding`, generic apoptosis, complex, and plasma
  membrane rows to caspase binding, death effector domain binding, death
  receptor binding, DISC assembly, or death-domain-receptor extrinsic signaling;
  kept ripoptosome and MAVS/RIG-I-like receptor cytokine/antiviral outputs as
  non-core; removed NleB-substrate and high-throughput interactome rows; and
  marked broad mouse lymphoid-organ, T-cell, kidney, cocaine, NF-kappaB, and
  host-defense projections as over-annotation.
- Completed the human FASLG review. The curation centered FasL on
  TNF-family cytokine/death-receptor binding activity upstream of the FAS/CD95
  DISC; narrowed generic receptor-binding, top-level apoptosis, and
  DISC-context `protein binding` imports to the FAS death-receptor branch;
  removed high-throughput SH3/HuRI/BioPlex/U2OS interactome rows; separated the
  ADAM10/SPPL2A-released nuclear FasL ICD, exosome FasL, endothelial apoptosis,
  and necroptotic signaling as non-core contexts; and removed Reactome FASLG
  transcription events that were being exported as extracellular FASLG protein
  localization.
- Completed a targeted human FAS cleanup after GOA refresh added 17
  partner-specific `protein binding` rows to the existing isoform-aware
  review. Canonical DISC-context FADD/CASP8 rows were tightened to
  FAS/TNFRSF6 receptor activity; exact-partner rows hidden in abstract-only
  papers were left `UNDECIDED`; and non-core GSK3B/BIRC2/PMLRARalpha or
  proximity-ligation/BioPlex generic PPI rows were removed rather than being
  allowed to stand as uninformative molecular functions.
- Completed the human PMAIP1/NOXA review. The curation centered
  NOXA on BH3-mediated inhibition of pro-survival MCL1 and BCL2A1,
  with lower-affinity contextual BCL2 and BCL2L10 binding retained
  under the same proposed NOXA-side inhibitor activity. Generic
  `protein binding`, top-level apoptosis, DNA-damage, permeability,
  cytochrome-c release, and intrinsic-apoptosis rows were tightened to
  MCL1/MOMP biology where the source was proximal; BioPlex and
  expression-module rows were removed; dsRNA, glucose, hypoxia,
  T-cell-homeostasis, ER-stress, and ROS rows were either kept as
  contextual over-annotations or left unresolved when the cache was
  abstract-only.
- Completed the human BBC3/PUMA review. The curation centered PUMA on
  BH3-only derepression of pro-survival BCL2-family proteins, plus weak
  direct BAX/BAK activation, at the mitochondrial MOMP checkpoint. It
  narrows generic `protein binding` rows to proposed PUMA/BIM/BID-side
  molecular functions; removes high-throughput interactome edges and EGFR
  sequestration; separates upstream BBC3 transcription events from PUMA
  protein localization; replaces broad DNA-damage, ER-stress, and apoptosis
  rows with p53, ER-stress, or MOMP descendants where possible; and removes
  hypoxia and ERN1/UPR over-annotations.
- Completed the human BCL2L11/BIM review. The curation centered BIM on
  two complementary BH3-only activities at the mitochondrial BAX/BAK
  checkpoint: direct effector activation and inhibition of pro-survival
  BCL2-family grooves. The review avoids using `BH3 domain binding` for
  BIM-side `GO:0005515` rows, removes high-throughput and viral sequestration
  interaction noise, separates transcriptional induction from BIM protein
  localization, tightens broad apoptosis/complex-assembly rows to MOMP or
  intrinsic signaling where evidence is proximal, and keeps abstract-only
  source rows unresolved when the exact curated interaction is not locally
  recoverable.
- Completed the human BID review. The curation centered cleaved tBID
  as an activator BH3-only relay from CASP8, CASP6, and other cleavage
  events to mitochondrial BAX/BAK outer-membrane permeabilization;
  removed the mis-scoped `death receptor binding` row; avoided
  directionally wrong `BH3 domain binding` replacements for BID-side
  `GO:0005515` interaction imports; tightened broad release,
  mitochondrial-change, complex-assembly, and extrinsic/intrinsic
  signaling rows to direct MOMP or death-receptor descendants; and
  proposed a BID/BIM/PUMA-side BCL2-family effector activator molecular
  function term.
- Revalidated the existing complete human BCL2 and BCL2L1 reviews before
  moving deeper into the BCL2-family MOMP slice. BCL2 already captured the
  direct mitochondrial/ER anti-apoptotic role, conditional converted BCL2
  pro-apoptotic activity, BECN1/AMBRA1 autophagy inhibition, and remaining
  source-level uncertainties; BCL2L1 already captured the Bcl-xL/Bcl-xS
  isoform split and anti-apoptotic mitochondrial function.
- Completed the human MCL1 review. The curation centered canonical MCL-1L
  on BH3-domain binding in OMM BCL2-family complexes that restrain
  BAK/BAX-dependent MOMP; split the pro-apoptotic MCL-1S and caspase-cleaved
  fragment evidence away from the long isoform; removed high-throughput
  and substrate/stabilizer `GO:0005515` rows; tightened broad or wrong-sign
  apoptosis terms to negative regulation of MOMP or cytochrome-c release;
  and kept autophagy, anoikis, mitochondrial fusion, and DNA-damage rows as
  secondary contexts.
- Completed the human BAK1 review. The curation centered BAK1 on its resident
  mitochondrial outer-membrane BCL2-family effector role in MOMP, cytochrome-c
  release, and BAK-complex pore assembly; removed the generic `GO:0005515`
  interaction import set; tightened broad apoptotic-process and membrane-
  permeability rows to MOMP; removed negative-regulation rows where BAK is the
  restrained target; and kept ER calcium, UPR, UV, and chaperone rows as
  secondary.
- Completed the human BAX review. The curation centered BAX on BH3-triggered
  mitochondrial outer-membrane permeabilization, cytochrome-c release, BAX
  oligomerization, and BCL2-family complex assembly; removed all generic
  `GO:0005515` interaction rows; tightened broad apoptotic process and execution
  rows to MOMP or intrinsic signaling; fixed mitochondrial-fusion polarity; and
  removed the historical permeability-transition-pore complex assertion.
- Completed the human CYCS review. The curation kept CYCS's mitochondrial
  electron-transfer and apoptosome functions distinct, tightened broad apoptosis
  rows to intrinsic apoptotic signaling, added a proposed apoptosome complex
  assertion, moved inner-membrane Reactome projections to mitochondrial
  intermembrane space, removed cytosolic precursor translation as a functional
  localization, and removed high-throughput `GO:0005515` interaction rows.
- Completed the human APAF1 review. The curation kept APAF1 centered on
  cytochrome-c-dependent apoptosome assembly in intrinsic apoptotic signaling,
  replaced CASP9 `GO:0005515` rows with CARD-domain binding, removed generic
  regulator and cytochrome-c binding rows lacking a precise GO MF replacement,
  and marked stress, nutrient, tissue, and developmental outcome terms as
  over-annotations of the core apoptosome scaffold role.
- Completed the human CASP9 review. The curation tightened top-level apoptosis
  rows to intrinsic apoptotic signaling or effector-procaspase maturation,
  replaced APaf-1/procaspase-9 `GO:0005515` assertions with CARD-domain binding
  or apoptotic caspase activator terms, removed high-throughput generic binding
  rows, and retained an isoform-specific Caspase-9S negative-regulation proposal.
- Completed the human CASP8 review. The curation kept CASP8's FADD/DED DISC
  assembly, death-domain receptor initiation, RIPK1-dependent necroptosis
  checkpoint, and gasdermin/procaspase maturation branches, while removing the
  generic `GO:0005515` interaction set and tightening or deferring broad
  apoptotic-process, execution-phase, immune-differentiation, and readout-based
  rows.
- Completed the human CASP7 review from local cached evidence, covering its
  core executioner-caspase activity, RNA-assisted PARP1/RNA-binding-protein
  cleavage, and SMPD1 maturation in extracellular pore-repair contexts. The
  review removed uninformative high-throughput `GO:0005515` rows, tightened
  generic `GO:0006915` assertions to execution-phase apoptosis, and left
  abstract-only CASP7-specificity or localization gaps as `UNDECIDED`.
- Completed the human CASP6 review without provider-backed deep research, using
  local cached publications and pathway/model evidence. The review removed the
  high-throughput `GO:0005515` interactome flood, kept direct CASP6 protease and
  ZBP1/RIPK3 PANoptosis biology, added a missing molecular-adaptor assertion for
  the catalysis-independent RIPK3/ZBP1 scaffold role, and left only evidence
  gaps unresolved.

## 2026-09-28

- Created the project as a mammal-first apoptosis campaign with three workstreams:
  module boundary review, generic `GO:0006915` triage, and assay-derived
  over-annotation checks.
- Seeded the project with the existing draft intrinsic and death-receptor
  apoptosis modules rather than treating those pathways as unmodeled.
- Cross-linked the readout-quality and over-annotation projects because this
  project should reuse their rubric for caspase and viability readouts.
- Started the first Priority 1 gene by migrating all human CASP3 generic
  `GO:0005515` rows away from the legacy `MARK_AS_OVER_ANNOTATED` action,
  adding missing PAINT propagation metadata, and marking the CASP3 review
  `COMPLETE` after clean validation.
- Seeded human CASP6 with `just fetch-gene human CASP6`; Falcon deep research
  could not run because no provider API keys were configured.
