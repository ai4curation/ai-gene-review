# TNFRSF10A / DR4 notes

## Core role

- TNFRSF10A is DR4/TRAIL-R1, a type I TNF-receptor-family death receptor for
  TNFSF10/TRAIL. The original cloning paper identified a TRAIL receptor
  "designated death receptor-4, DR4" with a cytoplasmic death domain
  [PMID:9082980].
- The first DR4 report did not see FADD use in its assay system, but this was
  resolved quickly by Schneider et al., who showed that "TRAIL induces
  apoptosis through two closely related receptors, TRAIL-R1 (DR4) and
  TRAIL-R2 (DR5)" and that DR4/DR5 signaling is FADD dependent [PMID:9430228].
  GO rows to generic apoptosis, signal transduction, and death-domain-receptor
  apoptotic signaling are therefore correct in direction but should be narrowed
  to `GO:0036462 TRAIL-activated apoptotic signaling pathway`.
- TNFRSF10A does not just bind ligand in isolation: receptor clustering and
  death-domain signaling are part of the molecular activity. `GO:0036463 TRAIL
  receptor activity` is the best replacement for imported `protein binding`,
  `TRAIL binding`, `death receptor activity`, `signaling receptor activity`,
  and DR4 oligomerization rows that are really describing this same
  receptor-level function.
- Palmitoylation is a DR4-specific activation determinant. Rossin et al. found
  that "DR4 is palmitoylated" and that this modification is required for raft
  localization and oligomerization during TRAIL-induced signaling
  [PMID:19090789]. The specific active location should be
  `GO:0044853 plasma membrane raft`; broader membrane-raft rows can be
  modified to that term.

## Accessory and trafficking evidence

- ARAP1 is a trafficking/accessory interactor rather than the core DR4
  molecular function. The cached abstract reports DR4 intracellular-region
  binding, co-precipitation, co-localization in ER/Golgi, plasma membrane, and
  early endosomes, and compromised DR4 cell-surface localization after ARAP1
  knockdown [PMID:18165900]. That supports a biological role in DR4
  mobilization, but not retention of a generic `GO:0005515 protein binding`
  row for TNFRSF10A.
- ZDHHC3/GODZ regulates DR4 delivery and TRAIL sensitivity. The paper reports
  that "GODZ binds to DR4, but not to DR5" and localizes DR4 to the plasma
  membrane through its DHHC motif [PMID:22240897]. Golgi and cytosol rows from
  this paper are non-core trafficking pools; plasma membrane remains a core
  location.
- DJ-1/PARK7 inhibits TRAIL-induced apoptosis by binding FADD and blocking
  pro-caspase-8 recruitment [PMID:21785459]. The resulting TNFRSF10A-FADD and
  TNFRSF10A-CASP8 co-complex imports support the receptor-proximal TRAIL
  pathway, whereas a TNFRSF10A-PARK7 bare binding row over-scopes the receptor.
- The CUL3/caspase-8 aggregation paper sits downstream of the receptor. Its
  title-level cache supports that it is about "caspase-8 mediate extrinsic
  apoptosis signaling" [PMID:19427028], so TNFSF10 edges can be folded into
  TRAIL receptor activity and CASP8 co-complex rows into the TRAIL pathway.
- Two IntAct imports from the DR5-peptide paper were left `UNDECIDED`: the
  cached record is abstract-only and focused on "Multivalent DR5 peptides"
  [PMID:20103630], so local evidence is not enough to accept or reject its
  DR4/TNFSF10A edges.
- The LGALS3BP interaction from the interferon-stimulated-gene AP-MS screen was
  also left `UNDECIDED`: the cached abstract only describes a
  "mass-spectrometry-based survey" [PMID:30833792] and does not expose the
  TNFRSF10A-specific evidence.

## Reactome and pathway-model exports

- The TRAIL/TRAILR1 GO-CAM places TNFRSF10A in
  `GO:0036462 TRAIL-activated apoptotic signaling pathway`, with a receptor
  molecular function in the plasma-membrane raft. A second HPV E6 model also
  keeps TNFRSF10A/TNFRSF10B at the plasma membrane in the same pathway.
- Reactome rows for TNFSF10 binding to TNFRSF10A/B, receptor trimerization,
  FADD recruitment, and initiator-caspase recruitment at the DISC are
  direct enough to keep as plasma-membrane assertions for DR4. The DR5-only
  procaspase-8 dimerization event is not; its summary explicitly places the
  event at a "TRAIL receptor-2:FADD receptor complex"
  [Reactome:R-HSA-141156].
- TP53-driven transcription of the TNFRSF10A gene is a recurring export trap.
  The Reactome event describes p53 stimulating transcription of TRAIL receptor
  genes [Reactome:R-HSA-5633441]; that is a gene-expression event, not a
  cellular-component observation on mature DR4 protein.
- NF-kappaB output is real but contextual. Both 1997 DR4/DR5 papers and a
  pancreatic adenocarcinoma paper support TRAIL-receptor NF-kappaB activation
  [PMID:9430227; PMID:9430228; PMID:11464292]. Those rows are non-core relative
  to the receptor's apoptotic DISC function and should use a modern canonical
  NF-kappaB signaling term rather than the old NIK wording.
- The mechanical-stimulus rows trace to a prostate-cancer BAD paper and only
  use IEP/expression-pattern evidence for TNFRSF10A. They should stay marked as
  over-annotation, because changed DR4 transcript or surface expression after a
  stretch assay does not make DR4 a performer of the mechanical-stimulus
  response.
