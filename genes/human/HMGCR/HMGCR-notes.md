# HMGCR (human, UniProtKB:P04035) — review notes

Deep research note: falcon provider is out of credits (HTTP 402); no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt
record (`HMGCR-uniprot.txt`), the seeded GOA (`HMGCR-goa.tsv`), and the cached
`publications/PMID_*.md` / `reactome/R-HSA-*.md` entries.

## Core biology

HMGCR is **3-hydroxy-3-methylglutaryl-coenzyme A reductase (NADPH)** (EC 1.1.1.34),
the rate-limiting, committed enzyme of the mevalonate pathway. It catalyzes the
NADPH-dependent four-electron reduction of (3S)-HMG-CoA to (R)-mevalonate + CoA
(two-step reaction consuming 2 NADPH).

- Catalytic reaction (UniProt CATALYTIC ACTIVITY): "(R)-mevalonate + 2 NADP(+) + CoA
  = (3S)-3-hydroxy-3-methylglutaryl-CoA + 2 NADPH + 2 H(+)" (Rhea:RHEA:15989; EC=1.1.1.34).
- [PMID:10698924 "3-hydroxy-3-methylglutaryl-CoA reductase (HMGR) catalyzes the formation of
  mevalonate, the committed step in the biosynthesis of sterols and isoprenoids."]
- [PMID:6995544 "3-Hydroxy-3-methylglutaryl Coenzyme A reductase, the enzyme that synthesizes
  mevalonate, appears to be regulated through a multivalent feedback mechanism."] — rate/feedback.
- [PMID:21357570 "Hydroxy-3-methyl-glutaryl-CoA reductase (HMGR) is the rate-controlling enzyme of
  cholesterol synthesis"]
- [PMID:36745799 "The encoded protein, HMG-CoA reductase, has a key role in the mevalonate pathway
  and facilitates the rate-limiting step in cholesterol synthesis"] — plus LGMDR28 disease + rescue by mevalonolactone.

## Structure / domains

- Polytopic ER membrane protein (multi-pass); 888 aa. N-terminal membrane domain (8 TM helices,
  residues ~1-339) contains the sterol-sensing domain (SSD, 61-218) with the INSIG-binding motif
  (75-78). C-terminal cytosolic domain (~426-888) is catalytic.
- [PMID:2991281 "the membrane-bound glycoprotein that regulates cholesterol synthesis"];
  N-terminal domain "which is predicted to span the endoplasmic reticulum membrane seven times"
  and "mediates accelerated degradation of reductase in the presence of sterols."
- Crystal structures of the catalytic portion (422-888): homotetramer/homodimer; active site with
  CoA, NADP(+), and HMG bound. [PMID:10698924 "Catalytic portions of human HMGR form tight tetramers."]
  UniProt BINDING: CoA (565-571, 720-722, 865-866), NADP(+) (626-628, 653-661, 870-871).

## Regulation / degradation

- Sterol-accelerated ERAD: sterols promote HMGCR binding (via SSD) to INSIG1/INSIG2, recruiting
  ubiquitin ligases (AMFR/gp78, RNF139/TRC8, RNF145), ubiquitination (Lys-248 main site) and
  proteasomal degradation. SREBP/SCAP axis controls transcription. Feedback by sterol + nonsterol
  mevalonate-derived signals [PMID:6995544].
- Target of statins (competitive inhibitors) — cholesterol-lowering drugs [PMID:18540668,
  PMID:10698924 abstract; Reactome R-HSA-9705584].

## Localization

- ER membrane (primary): UniProt SUBCELLULAR LOCATION "Endoplasmic reticulum membrane"; also
  [PMID:17180682] localizes pre-squalene isoprenoid segment (incl. HMGCR) to peroxisomes:
  "isoprenoid/cholesterol biosynthetic pathway occur in peroxisomes". Peroxisomal localization of
  cholesterol-biosynthesis enzymes is contested in the literature; ER is the well-established site.

## Interactions

- UBIAD1 [PMID:23169578 "interacts with HMGCR and SOAT1, enzymes catalyzing cholesterol synthesis
  and" ... "using yeast two-hybrid screening and immunoprecipitation"] — reported IPI (protein binding).
- High-throughput interactome (BioPlex) [PMID:33961781] — AP-MS network; the IPI to UBIAD1 (Q9Y5Z9)
  here is a bare protein-binding assignment.

## Disease

- Autosomal recessive limb-girdle muscular dystrophy 28 (LGMDR28) from bi-allelic HMGCR variants
  [PMID:36745799, PMID:37167966]; statin-associated immune-mediated necrotizing myopathy involves
  anti-HMGCR autoantibodies (background).

## Curation decisions summary

- MF GO:0004420 (HMG-CoA reductase NADPH activity): core; multiple IDA/EXP + IBA/IEA → ACCEPT.
- GO:0120225 coenzyme A binding, GO:0070402 NADPH binding: IDA from crystal structure → ACCEPT (molecular detail of catalysis).
- GO:0050661 NADP binding (IEA/InterPro): redundant, more general than GO:0070402 IDA → KEEP_AS_NON_CORE.
- GO:0016616 (parent oxidoreductase term, IEA): too general vs GO:0004420 → MARK_AS_OVER_ANNOTATED.
- BP: GO:0006695 cholesterol biosynthetic process (IDA), GO:0016126 sterol, GO:0008299 isoprenoid → ACCEPT (core pathway).
- GO:0015936 coenzyme A metabolic process (IEA/InterPro): CoA is a product, not the pathway HMGCR is "in" — over-annotation → MARK_AS_OVER_ANNOTATED.
- CC: GO:0005789 ER membrane (many lines, EXP/IDA/IBA/IEA/TAS) → ACCEPT; GO:0005783 ER (IDA) ACCEPT.
- GO:0005778 peroxisomal membrane (IDA PMID:17180682, IBA, IEA): keep experimental IDA but non-core (contested) → KEEP_AS_NON_CORE; IEA SubCell → KEEP_AS_NON_CORE; IBA → KEEP_AS_NON_CORE.
- GO:0005515 protein binding IPIs (UBIAD1) → MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).
- GO:0042177 neg reg protein catabolic, GO:0050709 neg reg protein secretion, GO:1900222 neg reg amyloid-beta clearance
  (ISS/IEA from mouse Q01237 ortholog): these are indirect/pleiotropic downstream effects of cholesterol
  pathway, not HMGCR molecular function → MARK_AS_OVER_ANNOTATED (ISS/IEA electronic transfers, weak).
</content>
</invoke>
