# Eve (Q8MMJ3, Strongylocentrotus purpuratus) — curation notes

## Identity

- UniProt Q8MMJ3 (TrEMBL, Q8MMJ3_STRPU, "Even-skipped-like protein") is the mRNA
  AF517551 / AAM53251 cloned from endomesoderm cDNA by Ransick et al. 2002, the
  paper that discovered Speve in a differential macroarray screen for
  beta-catenin-dependent zygotic endomesoderm genes [PMID:12027439 "Seven transcript
  species were identified that responded sharply to injection of Cad mRNA, and that
  are not represented in maternal mRNA. Six of those encode transcription factors."].
  The GRN literature calls the gene eve / Sp-eve / Speve. 297 aa; homeodomain at
  143-203 (PROSITE PS50071). PANTHER PTHR46294 / SF4 (family id not asserted in the
  review; see CLAUDE.md on PANTHER labels). UniProt gene id 373529 (NM_214651).
  No identity doubt: the RX reference is the discovery paper of the GRN gene.

## Expression

- Discovery paper: "Speve, an evenskipped orthologue expressed very early in all
  vegetal blastomeres and then gradually shifting to veg(1) derivatives by the
  mesenchyme blastula stage" [PMID:12027439].
- Detailed time course (Smith, Kurokawa & Davidson 2008): "Transcription of eve is also
  evident in the vegetal plate in 6th cleavage" and "Its expression extends across the
  macromeres and their descendents, the veg 1 and veg 2 cells." Then "Expression of eve
  continues in veg 2 descendents until about the hatched blastula stage, when it fades
  from these cells and turns on in veg 1 descendents." Eve runs "at the leading edge of
  the expanding patterning wave" of the blimp1/wnt8 torus cohort [PMID:18061160].
- Peter & Davidson 2010: "By 15 hpf eve expression, however, is clearly restricted to
  the veg1 lineage" [PMID:19895806]; "eve is the only one expressed in the veg1 lineage
  at early blastula stages" [PMID:19895806].
- Cui et al. 2014: "eve expression is specific to all cells of the veg1 lineage from
  15 h on" [PMID:25385617]; Eve is expressed in both veg1 endoderm and veg1 ectoderm
  [PMID:33484703 "Eve and Wnt5 are expressed in both Veg1 endoderm and Veg1 ectoderm"].

## Inputs (cis-regulatory and perturbation)

- Cis-regulatory module (Smith et al. 2008, BAC-GFP knock-in and 2.5 kb Eve-GFP):
  "We verify the cis-regulatory inputs of even-skipped predicted by network analysis.
  These include activation by β-catenin/Tcf and Blimp1, repression within the torus by
  Hox11/13b, and repression outside the torus by Tcf in the absence of Wnt8 signal
  input." [PMID:18061160]. Blimp1-site mutation: "QPCR analysis showed GFP mRNA content
  at 18 h to be only 14 ± 9% that of the control." Tcf-site mutation: "a very high
  frequency of ectopic expression in the ectoderm". Hox-site mutation: "the green
  fluorescence produced by the construct lacking intact Hox sites now extends
  ectopically into the veg 2 domain" [PMID:18061160]. Hox11/13b MASO: "eve transcript
  levels were increased by 2.4 and 2.4 cycles of QPCR in two trials in embryos
  harvested at 22 h post-fertilization." [PMID:18061160].
- Blimp1 input later contradicted by perturbation: "our current perturbation
  experiments show that blimp1 MASO has no effect at all on eve transcript levels
  (Fig. S2)" [PMID:19895806]; the domains of blimp1b (veg2) and eve (veg1) do not
  overlap at 18 h. Recorded as a finding_review conflict on PMID:18061160.
- Autorepression: "The only perturbation resulting in a change of eve expression
  levels was injection of eve MASO itself." and "This result indicates that eve is
  controlled by auto-repression." [PMID:19895806]. "It follows that in normal embryos
  eve auto-repression is required to clear eve expression from veg2 cells, despite the
  presence of levels of Tcf/β-catenin sufficient to support expression of the veg2
  endoderm genes." [PMID:19895806].
- Wnt inputs: C59 (Porcupine inhibitor) and Wnt1/Wnt16 MASO reduce eve in veg1
  endoderm [PMID:25385617 "injection of Wnt16 MASO decreased the expression levels of
  only hox11/13b and eve"].
- Post-transcriptional: miR-31 directly suppresses Eve; de-repression or Eve
  overexpression perturbs PMC patterning and skeletogenesis [PMID:33484703 "Removal of
  miR-31 suppression of Eve and overexpression of Eve result in skeletogenic and PMC
  patterning defects."].

## Outputs (what Eve does)

- Up to 18 hpf, no target other than itself: "eve MASO does not affect any other gene
  analyzed here, other than itself (Fig. S2)" [PMID:19895806]; "with no detectable
  impact on any other regulatory gene at this stage" [PMID:21623371].
- From 24 hpf Eve activates the veg1 (hindgut) endoderm GRN: "Hox11/13b expression is
  activated by Eve in descendants of veg1 cells at 24 h, because injection of eve MASO
  reduces hox11/13b expression only after 24 h (Fig. 3b)." and "The assembly of the veg1
  endoderm GRN, which is spatially activated by Eve, is temporally motivated by a
  predicted signal (V1) expressed under the control of the veg2 endoderm GRN."
  [PMID:21623371]. The veg1 endoderm GRN "specifies future hindgut cell fate"
  [PMID:21623371]. Cui et al. 2014 summarise: "by 21–24 h its product is responsible
  for activating the expression of regulatory genes specific to the future posterior
  endoderm, including hox11/13b , brachyury , and hnf1" [PMID:25385617].
- Eve also drives veg1 wnt genes and the veg1 ectoderm state: "Perturbation of the
  pan-veg1 transcription factor Eve by injection of Eve MASO resulted in decreased
  expression of wnt1 , wnt4 , wnt5 , and wnt16" and "Thus Eve plays a dual role in the
  specification of veg1 ectoderm: It directly represses genes of the animal ectoderm
  in these cells, and it activates the expression of wnt4 in veg1 endoderm and veg1
  ectoderm, leading to the activation of genes of the veg1 ectodermal GRN."
  [PMID:25385617]. "The earliest specification of the veg1 cell lineage, the precursor
  of veg1 endoderm and veg1 ectoderm, is controlled by eve" [PMID:25385617].
- Repressive outputs in the ciliated-band/veg1 ectoderm analysis (Barsi, Li &
  Davidson 2015): "fgf9 expression is excluded from subdomains 3 and 4 (Veg1 ectoderm)
  by Eve" and "myc expression is also excluded from subdomain 4 by Eve" [PMID:25655703].
- Timing of the hox11/13b output (Cui et al. 2014): "In veg1 endoderm cells, expression
  of hox11/13b initiates at 21–24 h under the control of Eve, and transcription of wnt1
  and wnt16 , activated by Hox11/13b, starts at 24 h." [PMID:25385617].
- Signal V2 to veg2: "A second putative signal (V2) is expressed under the control of
  Eve and activates expression of blimp1b and gatae in veg2 endoderm precursors."
  [PMID:21623371] — indirect, not annotated.

## Curation decisions

- Direct DNA binding of the sea urchin protein has never been assayed (no EMSA/ChIP);
  all Eve outputs rest on MASO perturbation within the GRN framework, and no target
  cis-regulatory site for Eve has been mutated. MF activator/repressor terms are
  therefore proposed as IMP, with the caveat recorded.
- Electronic rows: GO:0000981, GO:0005634, GO:0006357 accepted (core); GO:0003677
  accepted as the true but general parent; GO:0006355 marked MODIFY toward the
  Pol II sign-specific children (GO:0045944, GO:0000122).
- All quotes in this file were re-verified as verbatim substrings of the cached
  publications (2026-09-28).
- NEW: GO:0001228 and GO:0045944 (activation of hox11/13b, wnt1/4/5/16), GO:0001227 and
  GO:0000122 (autorepression; repression of animal-ectoderm genes in veg1 ectoderm),
  GO:0001714 endodermal cell fate specification (veg1/hindgut endoderm GRN driver),
  GO:0001715 ectodermal cell fate specification (veg1 ectoderm, Cui 2014).
- Not proposed: hindgut development (downstream outcome of the GRN Eve initiates),
  Wnt signalling terms (Eve is one transcriptional step upstream of the ligands),
  skeletal-system terms (miR-31 de-repression phenotype is indirect via Vegf3).
- gocams/index.tsv has no S. purpuratus entries.
