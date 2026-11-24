---
title: "GO-CAM review errors"
maturity: SCOPING
tags: [EVALUATION]
species: [human, yeast, SCHPO, worm, ARATH, ENTFC]
autolink_exclude: [CDC2, cdc2, DUSP18, Dusp18]
index_group: CROSS_CUTTING
description: The ten most serious errors found by the GO-CAM reviews so far, each re-checked against its sources, and a six-class taxonomy of what goes wrong.
manifest:
  artifacts:
    - href: https://claude.ai/artifact/XnDb9mq6w2BvBmYmBSAEf6
      title: Error taxonomy brief
      description: AI generated
---

# GO-CAM review errors

**Bottom line:** the 61 GO-CAM reviews in `gocams/*/*-review.yaml` cover 351
activities: 195 are OK, 136 UNCERTAIN and 20 WRONG, and the reviews record 125
source defects. Most defects are provenance problems (a reference that does not
support the assertion it is attached to), and the assertion itself is usually
true. The errors that change what a model says are rarer: the wrong gene behind
an activity, the wrong molecular function, or a causal edge with the wrong sign.
The ten worst are listed below. Each was re-checked on 2026-11-24 against the
cached source model, the cited papers and the GO term definitions; all ten hold,
and four needed a correction to how the review described them.

The [error taxonomy brief](https://claude.ai/artifact/XnDb9mq6w2BvBmYmBSAEf6)
presents the same material with links to every model, paper, protein and term.

## Scope and limits

- **Sample.** The 61 reviewed models are about 3% of the 2,040 cached
  production models, and they were chosen for review, not at random. The
  proportions here are not estimates for GO-CAM as a whole.
- **What was re-checked.** The ten ranked errors and the five near misses were
  verified. The taxonomy counts are the reviewers' own tallies of
  `source_defects` and `qc_flags`, and were not re-checked.
- **Depth.** Several cited papers are cached as abstract only. Where a check
  rests on an abstract, the table says so.

## Top 10 outstanding errors

Ranked by how badly the model misstates biology, then by confidence. Model ids
link to the GO-CAM; the review files are under `gocams/<id>/`.

| # | Model | Error | Class | Re-check |
|---|---|---|---|---|
| 1 | [67e5e74400000148](https://model.geneontology.org/67e5e74400000148) Arabidopsis MRG domain proteins | H4K5 acetyltransferase (GO:0043995) is enabled by AT2G45160, which is SCL27 ([Q7XJM8](https://www.uniprot.org/uniprotkb/Q7XJM8)), a GRAS regulator that shares the alias HAM1. The MYST acetyltransferase HAM1 is AT5G64610 ([Q9FLF7](https://www.uniprot.org/uniprotkb/Q9FLF7)). The same wrong gene is also a `has_input` of MRG2. | Wrong gene: alias collision | Holds. The model's own label is SCL27; the full text of [PMID:25183522](https://pubmed.ncbi.nlm.nih.gov/25183522/) describes HAM1 as a MYST protein. |
| 2 | [6796b94c00004996](https://model.geneontology.org/6796b94c00004996) SARS-CoV-2 entry | Cholesterol O-acyltransferase (GO:0034736) is enabled by [P24752](https://www.uniprot.org/uniprotkb/P24752), the mitochondrial thiolase ACAT1. ACE2 is typed endopeptidase where virus receptor activity is the function in play; furin's evidence is the TMPRSS2 cloning paper. | Wrong gene: alias collision; wrong MF | Holds, corrected. [PMID:32944968](https://pubmed.ncbi.nlm.nih.gov/32944968/) knocks down "ACAT1/2", so the intended product is SOAT1 ([P35610](https://www.uniprot.org/uniprotkb/P35610)), SOAT2 ([O75908](https://www.uniprot.org/uniprotkb/O75908)) or both, not SOAT1 alone. |
| 3 | [693b3c0900004859](https://model.geneontology.org/693b3c0900004859) ER to Golgi transport (S. pombe) | Sec23 GTPase activator activity directly *negatively* regulates Sar1 GTPase activity, while the Gyp10 GAP edge to Ypt1 GTPase activity in the same model is positive. | Wrong causal sign | Holds. Both targets are GO:0003924. The edge rests on phylogenetic inference, not an assay. |
| 4 | [66b5638000001589](https://model.geneontology.org/66b5638000001589) PERK and the integrated stress response | eIF2α ([P05198](https://www.uniprot.org/uniprotkb/P05198)) is split into a cap-dependent (GO:0160296) and an IRES-mediated (GO:0160297) initiation factor node. GO defines these as cap binding and IRES interaction, and eIF2 does neither. PERK positively regulates the IRES-typed node, which drives ATF4. | Wrong MF; wrong sign | Holds, corrected. PERK's edge to the cap-dependent node is negative, the right sign; only the edge to the IRES node is positive. The ATF4 edge cites [PMID:16289705](https://pubmed.ncbi.nlm.nih.gov/16289705/), a cell-free translation methods paper whose abstract does not mention ATF4. |
| 5 | [YeastPathways_PWY-5177](https://model.geneontology.org/YeastPathways_PWY-5177) glutaryl-CoA degradation | FOX2 is given the (S)-specific dehydrogenase (GO:0003857) in the cytosol; UniProt records it as the (3R)-specific peroxisomal enzyme. PHS1 (ER membrane, fatty acid elongation) and ERG10 are placed in a catabolic pathway. | Pathway-template artefact | Holds. Every assertion carries only the pathway-import reference. |
| 6 | [59cc772c00000000](https://model.geneontology.org/59cc772c00000000) IL-1β signalling | TOLLIP ([Q9H0E2](https://www.uniprot.org/uniprotkb/Q9H0E2)) directly positively regulates IRAK1. Cytosolic CASP1 also directly regulates extracellular IL1B, with no secretion step. | Wrong causal sign; skipped step | Holds as probable. The abstract of [PMID:10854325](https://pubmed.ncbi.nlm.nih.gov/10854325/) says Tollip overexpression impairs NF-κB activation, but also that Tollip links IRAK to the receptor. Abstract only. |
| 7 | [696022cd00001523](https://model.geneontology.org/696022cd00001523) SMO activation by cholesterol | A CDK1 ([P06493](https://www.uniprot.org/uniprotkb/P06493)) activity sits between ULK3 and SUFU, citing a paper that never mentions CDK1. | Unsupported gene product | Holds, corrected. The full text of [PMID:31279575](https://pubmed.ncbi.nlm.nih.gov/31279575/) (PMC6736714) has no CDK1, CDC2 or cyclin and 33 mentions of CK1, which it places in that position. CDK1 is most likely CK1 mis-keyed. |
| 8 | [59dc728000000351](https://model.geneontology.org/59dc728000000351) GPCR adenylate cyclase activation (FSH) | The GNAS to ADCY1 edge cites [PMID:123](https://pubmed.ncbi.nlm.nih.gov/123/), a 1975 surgery paper, as direct assay. Most other assertions rest on [PMID:27889227](https://pubmed.ncbi.nlm.nih.gov/27889227/), a GPCR trafficking review that never mentions FSH. The G protein is the XLαs entry [Q5JWF2](https://www.uniprot.org/uniprotkb/Q5JWF2). | Placeholder reference; isoform entry | Holds, corrected. Q5JWF2 is in this one cached model and [P63092](https://www.uniprot.org/uniprotkb/P63092) in 97; the review's figure of 91 activities could not be reproduced. |
| 9 | [5fb9cc0600000727](https://model.geneontology.org/5fb9cc0600000727), [5fce9b7300000030](https://model.geneontology.org/5fce9b7300000030) TLR1/TLR2 and TLR2/TLR6 | Both receptor complexes are typed lipopolysaccharide immune receptor activity (GO:0001875), while the models' own ligands are triacyl and diacyl lipopeptides. GO has no lipopeptide sibling term. | Wrong MF: ligand class | Holds. The reviews mark these WRONG but file no `source_defects`. |
| 10 | [65bc474400000029](https://model.geneontology.org/65bc474400000029), [66c7d41500002413](https://model.geneontology.org/66c7d41500002413), [65d7e4ac00001363](https://model.geneontology.org/65d7e4ac00001363), [69b3372b00003343](https://model.geneontology.org/69b3372b00003343) | Direct-assay evidence from papers on other subjects: ZDHHC4 to MAVS cites a glioblastoma GSK3β paper ([PMID:35606353](https://pubmed.ncbi.nlm.nih.gov/35606353/)); BTK to DDX41 cites a BTK–NLRP3 paper ([PMID:34554188](https://pubmed.ncbi.nlm.nih.gov/34554188/)); MCU and SMDT1 cite a mouse Pde8b paper ([PMID:22925203](https://pubmed.ncbi.nlm.nih.gov/22925203/)); PRKACA to CREB1 cites a MAP2c paper ([PMID:11029056](https://pubmed.ncbi.nlm.nih.gov/11029056/)). | Wrong reference | Holds. The first three are cached in full and never mention the target; the MAP2c paper is abstract only. |

### Near misses

These were checked at the model level and hold.

- [62b4ffe300000081](https://model.geneontology.org/62b4ffe300000081): granzyme B
  directly positively regulates perforin; the reviewer reads the direction as
  reversed. The two cited papers were not re-read.
- [568b0f9600000284](https://model.geneontology.org/568b0f9600000284): the JNK
  KGB-1 is typed as bare protein binding.
- [66c7d41500002413](https://model.geneontology.org/66c7d41500002413): DDX41 is
  typed RNA helicase activity, while its only cited paper,
  [PMID:35613581](https://pubmed.ncbi.nlm.nih.gov/35613581/), shows DNA unwinding.
- [69729a3800007453](https://model.geneontology.org/69729a3800007453): the hsp10
  orthology transfer cites SGD S000000004 (SSA1, a cytosolic Hsp70); budding
  yeast HSP10 is S000005546.
- [65692e7e00001822](https://model.geneontology.org/65692e7e00001822): AKT1 is
  part of excitatory postsynaptic potential in a TLR trafficking model.

## Taxonomy

Six classes, from the entity outward to the model as a whole. Counts are source
defects (`source_defects[].defect_type`) or QC flags (`qc_flags`) across the 61
reviews; one activity can carry several, and the 37 `WRONG_TERM` defects are
split between classes B and D.

### A. Entity: who does it

8 `WRONG_GENE_PRODUCT` defects.

- **Alias collision.** A shared symbol resolves to the wrong gene (HAM1, ACAT1).
- **Paralog or isoform slip.** CAMK2A where the paper shows CaMKII γ/δ; XLαs
  for Gs-alpha.
- **Unsupported participant.** A gene the cited paper never assays (CDK1).
- **Reaction-template match.** An enzyme assigned by reaction matching rather
  than evidence (PHS1, ERG10).

### B. Activity: what it does

29 `GENERIC_MF`, 12 `BINDING_AS_FUNCTION` and 4 `WRONG_MF_TERM` flags.

- **Lateral wrong term.** The right family with the wrong ligand or substrate
  class: LPS receptor for lipopeptide, activin receptor for ALK1 with BMP9,
  voltage-gated calcium channel for VDAC1, RNA for DNA helicase.
- **The wrong function of a multifunctional protein.** ACE2 as a peptidase in a
  model about its receptor role.
- **A generic parent where a child applies.** SRC as protein kinase, VanX as
  dipeptidase.
- **Binding as function.** KGB-1, Rud3, OspC1.

### C. Causal wiring: how activities connect

16 `WRONG_CAUSAL_RELATION` defects; 13 `DIRECT_VS_INDIRECT_CAUSAL`, 10
`HAS_INPUT_MISUSE`, 4 `INCORRECT_DIRECTIONALITY` and 2 `WRONG_CAUSAL_SIGN` flags.

- **Wrong sign.** Sec23, TOLLIP, eIF2.
- **Direct asserted for a multi-step path, or the reverse.** This includes four
  edges in the worm p38 model that the model's own comments record as
  mechanically upgraded from indirect to direct in 2023.
- **Reversed direction.** Granzyme B; NBN to TERF2.
- **Wrong relation type.** "Provides input for" used for regulation, or
  regulation used for a substrate hand-off (KISS1R to DUSP18, CUL1 to FBXO42).
- **`has_input` misuse.** A ligand, recruited effector or protein product in
  the slot meant for the substrate or target gene.

### D. Context: where, and in what process

27 `MISSING_LOCATION`, 7 `UNRESOLVED_COMPARTMENT` and 6
`NONADJACENT_COMPARTMENTS` flags. The compartment checks are described in
[GO-CAM compartments](GOCAM_COMPARTMENTS.md).

- **A wrong or template-default compartment.** Tim50 in the matrix, GDI1 in the
  ER, VanA in the membrane, FOX2 in the cytosol.
- **A location that resolves to no single membrane.** The ER–mitochondria
  contact-site term on ITPR1 and VDAC1.
- **An edge across non-adjacent compartments.** A missing secretion or
  translocation step.
- **Wrong or inverted process nesting.** The outer process placed inside the
  inner one (VanS, CASR, KISS1R), a process nested in itself (AKAP8), or an
  unrelated process (AKT1).
- **Wrong cell type.** NK T cell for a natural killer cell activity.

### E. Provenance: why we believe it

34 `WRONG_REFERENCE`, 4 `WRONG_EVIDENCE_CODE` and 4 `WRONG_WITH_FROM` defects;
17 `MISSING_EVIDENCE` flags.

- **A placeholder or mistyped id.** `PMID:123`, `GO_REF:000024`,
  `SGD:SS000005758`.
- **A paralog's paper.** SOCS2 for SOCS3, OspC3 for OspC1, TRAF3 for TRAF3IP3,
  TMPRSS2 for furin.
- **A reference copied onto an edge it does not support.** ATF4 to COX7A2L,
  EGFR to GRB2.
- **A review cited under a direct-assay code.** The FSH models.
- **An evidence code that does not fit its with/from.** Direct assay carrying an
  ortholog with/from; rat data as direct assay in a human model.

### F. Model structure

7 `MISSING_STATEMENT` and 2 `DUPLICATE_ASSERTION` defects; 3 `ORPHAN_ACTIVITY`
flags.

- **Duplicate nodes or edges.** Two VanR nodes; a triplicated GCGR to GNAS edge.
- **A missing branch the title promises.** The phospho-NBN arm; the two
  SARS-CoV-2 entry routes collapsed onto one node.
- **A whole-pathway template import** with no organism-specific evidence behind
  its steps.

## Patterns

- **Provenance is the largest class and the least damaging.** Most wrong
  references sit on assertions that are themselves true.
- **Entity and sign errors are rare but change what the model says**, and they
  are the ones most often marked `CONFIRMED`.
- **Errors travel between sibling models.** The same wrong term, reference or
  with/from recurs across the GRIN, ITPR, FSH and TLR series, so a fix in one
  implies a check of its siblings.
- **Alias collisions recur.** Two of the top three errors are a symbol shared by
  unrelated genes (HAM1, ACAT1), which suggests checking every enabler's
  UniProt entry against the protein the cited paper names.

## Plan

- [ ] File `source_defects` for the WRONG verdicts that have none: the two TLR
  receptor complexes, KGB-1 and Rud3. Until then `just export-source-defects`
  does not carry them upstream.
- [ ] Correct the explanation of the CDK1 defect in
  `gocams/696022cd00001523/696022cd00001523-review.yaml`: it says ULK3 has GLI2
  as input, but the model wires ULK3 to CDK1, CDK1 to SUFU and SUFU to GLI2. Add
  CK1 as the candidate correction.
- [ ] Update the ACAT1 defect in the SARS-CoV-2 review to name SOAT1 and SOAT2
  as candidates.
- [ ] Re-count or drop the "91 activities" figure in the FSH review's
  `WRONG_GENE_PRODUCT` defect.
- [ ] Re-check the taxonomy counts as reviews are added, and widen the sample
  beyond 61 models before quoting proportions.
- [ ] Scan all cached models for enablers whose UniProt entry does not match the
  gene the cited paper names, starting from symbols with known collisions.
