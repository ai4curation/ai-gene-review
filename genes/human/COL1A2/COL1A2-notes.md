# COL1A2 (human, UniProt P08123) curation notes

## Deep research status

- 2026-10-05: `just deep-research-falcon human COL1A2` failed on the first attempt
  (Edison API returned `429 Too Many Requests`; "Provider falcon exited with code 1 /
  All providers failed"). No perplexity key is available. A single retry also failed (falcon timed out after 600s);
  the review below was written from the UniProt record and the cached publications in
  `publications/` (PubMed abstracts / full texts), not from a deep-research report.
- UPDATE 2026-10-05: the failure statement above is superseded. The falcon job completed
  late (end_time 01:34) and `COL1A2-deep-research-falcon.md` now exists; it has been
  reconciled with the review (see "Falcon deep research reconciliation" below).

## Identity and structure

- Collagen alpha-2(I) chain; precursor with signal peptide (1-22), N-propeptide
  (23-79), mature chain (80-1119) and C-propeptide (1120-1366) carrying the COLFI
  (fibrillar collagen C-terminal) domain [file:human/COL1A2/COL1A2-uniprot.txt].
- "Trimers of one alpha 2(I) and two alpha 1(I) chains" [file:human/COL1A2/COL1A2-uniprot.txt].
- "Type I procollagen is a heterotrimer composed of two proalpha1(I) chains and one
  proalpha2(I) chain, encoded by the COL1A1 and COL1A2 genes, respectively."
  [PMID:18375391]
- C-propeptide drives chain selection and heterotrimer assembly: "the C-propeptide of
  proalpha2(I), like that of the proalpha1(I) C-propeptide, is essential for efficient
  assembly of type I procollagen heterotrimers" [PMID:18375391]. Mutant chains "were
  slow to assemble with proalpha1(I) chains to form heterotrimers and that were retained
  intracellularly" [PMID:18375391].
- Prolines in Y position hydroxylated [file:human/COL1A2/COL1A2-uniprot.txt].

## Function

- Fibrillar (group I) collagen: "Forms the fibrils of tendon, ligaments and bones. In
  bones the fibrils are mineralized with calcium hydroxyapatite."
  [file:human/COL1A2/COL1A2-uniprot.txt]
- Fibrils "are made by alloys of fibrillar collagens (types I, II, III, V, and XI)"
  [PMID:1916105].
- "Collagen-I is the most abundant protein in the human body" [PMID:26848503].
- Core MF: extracellular matrix structural constituent conferring tensile strength
  (GO:0030020); complex: collagen type I trimer (GO:0005584); process: collagen fibril
  organization (GO:0030199); location: extracellular matrix.

## Biosynthesis / trafficking (non-core locations)

- Procollagen folds in ER lumen; TMEM131 PapD-like domain binds the COL1A2 C-terminus
  and links it to TRAPPIII for ER-to-Golgi export: "we identified two human proteins,
  COL1A2 and TRAPPC8, that bind to the N- and C-terminal domains of human TMEM131,
  respectively" [PMID:32095531]. COL1A2 is cargo here, not an effector.
- Collagen-I proteostasis network interactome mapped by IP-MS [PMID:26848503].

## Disease (supports developmental/tissue-level process annotations, non-core)

- Osteogenesis imperfecta types 1-4, EDS arthrochalasia type 2, EDS cardiac valvular
  type (recessive null) [file:human/COL1A2/COL1A2-uniprot.txt].
- Dominant C-propeptide mutations cause OI type IV [PMID:18375391].
- Gene-targeted correction of mutant COL1A2 alleles in OI MSCs: "MSCs targeted at mutant
  COL1A2 alleles produced normal type I procollagen and formed bone" [PMID:17955022].
- Teeth: "The intense expression of pro-alpha 2(I) mRNA in odontoblasts of adult teeth
  suggests that ... they continue to synthesize heterotrimeric type I collagen molecules"
  [PMID:1740554].

## Problematic annotations noted

- PMID:17217948 (TGF-beta receptor signaling; Rho signal transduction, IDA): COL1A2
  promoter activity / mRNA is the readout of TGF-beta2/RhoA signaling in ARPE-19 cells
  ("Constitutively active RhoA increased COL1A2 promoter activity"). COL1A2 protein does
  not perform any step of these pathways (target gene, not participant).
- PMID:17334644 (regulation of blood pressure, IMP): candidate-gene association of a
  (GT)n COL1A2 polymorphism with BP in Japanese men. Association only.
- PMID:8841196 (skeletal system development, IMP): abstract concerns the COL1A1 Sp1
  polymorphism; COL1A2 only mentioned as a candidate. Full text not available; function
  is correct for COL1A2 anyway (OI), so kept as non-core.
- PMID:17211858 (blood vessel development, collagen fibril organization, identical
  protein binding, skin morphogenesis): abstract describes alpha1(I) R-to-C substitutions
  (COL1A1) forming "disulfide-bonded alpha1(I)-dimers". Full text not available; cannot
  confirm what was assayed for COL1A2. Identical protein binding left UNDECIDED.
- Mouse SMAD binding (source of IEA GO:0046332): PMID:14559231 is a Y2H / GST pulldown
  of in vitro translated collagens with Smad MH2 domains; collagen chains are ER-lumenal
  / extracellular while SMADs are cytosolic/nuclear, so the interaction is topologically
  implausible in vivo.
- Protein binding IPIs (SGTA, SGTB, UBQLN1/2, KCNIP4, EIF3F, MESD, SMARCD1) are binary
  Y2H interactome hits [PMID:25416956, PMID:26871637, PMID:32296183]; SGTA/UBQLN bind
  hydrophobic signal sequences of mislocalized secretory proteins; uninformative.
- MMP12 (protease binding): collagen is the substrate - "The catalytic domain of MMP-12
  binds to the triple helix and cleaves the typical sites -Gly(775)-Leu(776)- in alpha-2
  type I collagen" [PMID:19932771].
- PDGF binding: "All radiolabeled PDGF isoforms specifically interacted with type I, II,
  III, IV, V, and VI collagens" [PMID:8900172]; in vitro ECM-growth factor sequestration,
  non-core.

## Falcon deep research reconciliation (2026-10-05)

- `COL1A2-deep-research-falcon.md` completed after the review was written. It is fully
  consistent with the review: alpha2(I) chain of the [alpha1(I)]2alpha2(I) heterotrimer,
  C-propeptide-driven chain assembly in the ER, extracellular load-bearing fibril function,
  ADAMTS2/BMP1 propeptide processing acting on (not by) COL1A2, and TGF-beta/SMAD as
  upstream drivers of COL1A2 expression (supports the REMOVE of the TGF-beta and Rho
  signalling IDA annotations from PMID:17217948).
- Additions noted but not acted on: Malfait 2006 J Med Genet (homozygous COL1A2 frameshift,
  complete alpha2(I) absence, valvular EDS; already reflected in the description via UniProt);
  Lee 2022 DMM (Col1a2-null vs oim mice; already reflected in a suggested question on
  homotrimers); Mariano 2023 bioRxiv preprint (BMP1 site FYRA|DQPR at residue 1120);
  Ling 2024 (DDR2 signalling by type I collagen, not chain-resolved). None changes an
  annotation decision.
- Deep-research file added to references and cited as supporting text on the GO:0007179
  REMOVE. No annotation actions changed. Status set to COMPLETE.
