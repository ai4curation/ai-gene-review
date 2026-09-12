# AASS (human) — gene review notes

UniProt: Q9UDR5 (AASS_HUMAN); HGNC:17366; gene ID 10157; chromosome 7q31.3.
926 aa precursor; mitochondrial transit peptide (1..27); mature chain 28..926.

## Core biology (bifunctional enzyme)

AASS = alpha-aminoadipic semialdehyde synthase, mitochondrial. It is a **bifunctional**
enzyme (alias LKR/SDH) that catalyzes the **first two steps of the main (saccharopine)
pathway of L-lysine degradation** in the mitochondrial matrix:

1. **Lysine-ketoglutarate reductase (LKR, EC 1.5.1.8)** — N-terminal domain
   (region 28..476). Condenses L-lysine + 2-oxoglutarate to L-saccharopine using NADPH.
   UniProt CATALYTIC ACTIVITY: "L-saccharopine + NADP(+) + H2O = L-lysine + 2-oxoglutarate
   + NADPH + H(+)"; PhysiologicalDirection=right-to-left (i.e. lysine-forming direction
   is left, so physiological flux is lysine + 2-OG → saccharopine). RHEA:19373; EC 1.5.1.8.
   GO term: GO:0047130 saccharopine dehydrogenase (NADP+, L-lysine-forming) activity.

2. **Saccharopine dehydrogenase (SDH, EC 1.5.1.9)** — C-terminal domain
   (region 477..926). Oxidizes L-saccharopine to (S)-2-amino-6-oxohexanoate
   (= L-2-aminoadipate-6-semialdehyde / alpha-aminoadipic semialdehyde) + L-glutamate,
   reducing NAD+. UniProt: "L-saccharopine + NAD(+) + H2O = (S)-2-amino-6-oxohexanoate +
   L-glutamate + NADH + H(+)"; PhysiologicalDirection=left-to-right. RHEA:24520; EC 1.5.1.9.
   GO term: GO:0047131 saccharopine dehydrogenase (NAD+, L-glutamate-forming) activity.

Net: L-lysine + 2-OG + NADPH → saccharopine → alpha-aminoadipate-6-semialdehyde +
L-glutamate. This is the committed entry into lysine catabolism (steps 1/6 and 2/6 of
glutaryl-CoA from L-lysine; UniPathway UPA00868 UER00835/UER00836).

Structure: homotetramer (by similarity to mouse Q99K67). NAD-binding residues in SDH
domain resolved by crystallography (PDB 5L76/5L78/5O1N/5O1O/5O1P for SDH domain 455-926;
8DDA/8E8T/8E8U/8E8V for LKR domain). L-saccharopine-binding residues 577-578, 604, 703,
724-726 (by similarity to Q9P4R4).

Tissue: expressed broadly, highest in liver. Induced by starvation (by similarity).

## Disease

- **Hyperlysinemia type 1 / HYPLYS1 (MIM 238700)**: autosomal recessive; both AASS
  enzyme activities defective; increased serum lysine (+/- saccharopine); ~half of probands
  asymptomatic; generally considered a benign metabolic variant. [PMID:10775527]
- **Saccharopinuria**: patients retaining significant LKR but low SDH → saccharopine
  accumulation; few/no clinical manifestations. [PMID:463877]
- **DECRD (MIM 616034)**: AASS is one of the NADP(H)-dependent mitochondrial enzymes
  secondarily impaired when NADK2 is mutated (mitochondrial NADP(H) deficiency), producing
  hyperlysinemia alongside 2,4-dienoyl-CoA reductase deficiency. [PMID:24847004] (AASS is
  affected but the primary defect is in NADK2.)

## Annotation assessment

- **GO:0047130 / GO:0047131** (both MF activities): core. Supported by EXP (PMID:463877,
  enzyme assays in human fibroblasts/liver) and IMP (PMID:10775527, loss-of-function
  patient variant). ACCEPT. GO:0004753 (parent "saccharopine dehydrogenase activity", IBA):
  ACCEPT as a valid broader grouping.
- **GO:0004754** (saccharopine dehydrogenase (NAD+, L-lysine-forming) activity, ISS from
  Drosophila Q9VLX0): this is the *biosynthetic* direction SDH (yeast Lys1-type, lysine
  biosynthesis), NOT the human catabolic activity. Human AASS runs the catabolic SDH
  (GO:0047131, glutamate-forming) and the LKR/NADP+ reductase (GO:0047130). The
  L-lysine-forming SDH is the reverse (anabolic) reaction found in fungi. MARK_AS_OVER_ANNOTATED
  / MODIFY toward GO:0047131. (Kept conservative — ISS transfer picked the wrong catalytic
  direction for a catabolic mammalian enzyme.)
- **GO:0019477 L-lysine catabolic process** (IBA + IMP PMID:10775527): core BP. ACCEPT.
- Localization: **mitochondrial matrix (GO:0005759)** is the correct, well-supported
  compartment (Reactome TAS, Ensembl IEA from mouse, UniProt SUBCELL). GO:0005739
  mitochondrion (EXP PMID:463877, HTP PMID:34800366, TAS PMID:10567240, IEA) ACCEPT.
- **GO:0005737 cytoplasm** (IBA): broad but not wrong (matrix is within cytoplasm-ish
  parent); the phylogenetic call is conservative. Keep but non-core given the precise
  matrix annotation exists.
- **Drosophila-derived moonlighting ISS annotations** (all ISS, GO_REF:0000024, WITH
  UniProtKB:Q9VLX0 = D. melanogaster dLKR/SDH): GO:0000122 negative regulation of
  transcription by RNA Pol II, GO:0003714 transcription corepressor activity, GO:0042393
  histone binding, GO:0005634 nucleus, GO:0005829 cytosol. These transfer a fly-specific
  nuclear/transcriptional moonlighting role to human by sequence similarity. No experimental
  support in human; conflicts with the established mitochondrial-matrix metabolic role.
  MARK_AS_OVER_ANNOTATED (per policy, not REMOVE — ISS is an electronic-style transfer but
  the underlying fly biology is real; it is simply unvalidated/non-core for the human enzyme,
  and cytosol/nucleus contradict the matrix localization).

## Verbatim quote sources (for supporting_text)

- PMID:10775527 abstract: "The first two steps in the mammalian lysine-degradation pathway
  are catalyzed by lysine-ketoglutarate reductase and saccharopine dehydrogenase,
  respectively, resulting in the conversion of lysine to alpha-aminoadipic semialdehyde."
  and "we propose that AASS catalyzes the first two steps of the major lysine-degradation
  pathway in human cells and that inactivating mutations in the AASS gene are a cause of
  hyperlysinemia." and "an apparently bifunctional protein, with the N-terminal half similar
  to that of yeast LYS1 and with the C-terminal half similar to that of yeast LYS9."
- PMID:463877 abstract: "In all instances there was a deficiency in lysine-ketoglutarate
  reductase, saccharopine dehydrogenase, and saccharopine oxidoreductase activities."
  and "saccharopine oxidoreductase was partially purified from human liver ... The activity
  did not separate from that of lysine-ketoglutarate reductase or saccharopine dehydrogenase."
- PMID:10567240 abstract: "the bifunctional enzyme is likely to be a mitochondrial protein."
  and "both a bifunctional lysine-oxoglutarate reductase/saccharopine dehydrogenase and a
  monofunctional saccharopine dehydrogenase are likely to be present in this organ."
- PMID:34800366 abstract: "mitochondrial high-confidence proteome of >1,100 proteins
  (MitoCoP)".
- file: UniProt CATALYTIC ACTIVITY / FUNCTION / SUBCELLULAR LOCATION / DOMAIN sections.
