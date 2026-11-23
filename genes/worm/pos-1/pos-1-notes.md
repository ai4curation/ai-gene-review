# pos-1 (G5EF15, WBGene00004078) review notes

## Provenance of this research

- Automated deep research (FutureHouse, Perplexity, OpenAI) was not available in this
  environment: no provider API keys. No `-deep-research-<provider>.md` file was generated.
  The only provider file is the verbatim WormBase description
  (`pos-1-deep-research-wormbase.md`).
- Literature gathered by hand on 2026-11-16:
  - PubMed E-utilities query `pos-1[tiab] AND elegans[tiab]` (29 hits, sorted by date);
    relevant papers cached with `just fetch-pmid`.
  - Web searches for the Tabara et al. 1999 phenotype; QuickGO queries for comparator
    annotations (MEX-1, MEX-3, OMA-1, SPN-4).
  - Full texts read online but not in the cache (not used as `supporting_text`):
    Batchelder et al. 1999 (PMC316391), Tenlen et al. 2006 (PMC1698638), Tabara et al. 1999
    (PDF on the Mello lab site), Oldenbroek et al. 2013 (PMC3817945).

## Identity

- 264-aa CCCH tandem zinc finger (TZF) protein of the TIS11 family (PTHR12547:SF110).
  ZF1 aa 98-126, ZF2 aa 141-169. NMR structure of the TZF domain (PDB 6NZL) with Zn
  ligands C104, C113, C119, H123 and C147, C156, C162, H166.
- Maternal; cytoplasmic and P granule-associated, enriched in P1-P4, gone after P4 divides.

## RNA binding and specificity

- [PMID:18952820 "Here, we delineate the consensus POS-1 recognition element (PRE)
  required for specific recognition of its target mRNAs."] [PMID:18952820 "The PRE is
  distinct from sequences recognized by related proteins from both mammals and nematodes"]
  UniProt gives the PRE as 5'-UA(U2-3)RGD(N1-3)G-3'.
- [PMID:39321355 "POS-1 recognizes a broader set of RNA sequences compared to the human
  homologue tristetraprolin"]; the two fingers have different specificities.
- Targets (3' UTR binding shown in vitro unless noted):
  - glp-1, repressed in posterior blastomeres [PMID:12702662 "We show that a CCCH
    zinc-finger protein, POS-1, represses glp-1 mRNA translation by binding to the spatial
    control region."]; POS-1 binding excludes GLD-1 (PMID:23034181).
  - zif-1, repressed in germline blastomeres [PMID:22265679 "POS-1, MEX-3, and SPN-4
    function as repressors of ZIF-1 expression, whereas MEX-5 and MEX-6 antagonize this
    repression. All five proteins bind directly to the zif-1 3' UTR in vitro."]
  - neg-1, repressed in posterior cells by opposing GLD-2/GLD-3 cytoplasmic
    polyadenylation [PMID:26096734 "In posterior cells, POS-1 binds the neg-1 3' UTR to
    oppose GLD-2 and GLD-3 activities that promote NEG-1 expression and cytoplasmic
    lengthening of the neg-1 mRNA poly(A) tail."]; PAT-seq: 436 mRNAs with
    "GLD-2/GLD-3-activated, POS-1-repressed" poly(A) tails.
  - nos-2, activated in P4 [PMID:16499902 "Finally, the germ plasm component POS-1
    activates nos-2 translation in the PGCs."] [PMID:18417623 "POS-1 competes with SPN-4
    for binding to nos-2 RNA in vitro."] Activation is derepression: POS-1 is dispensable
    when MEX-3 or SPN-4 is absent.
  - apx-1, activated in P2 [PMID:9834181 "The earliest defect detected in pos-1 mutants is
    the failure to express APX-1 protein from maternally provided apx-1 mRNA"].
  - mom-2, activated in P2/P3 with PIE-1 and MEX-1 (PMID:24131629; PMC full text, read
    online).
  - mex-6 3' UTR: yeast three-hybrid interaction (PMID:17028349; PMC full text: "We
    tested whether POS-1 can bind the 3'-UTR of mex-6 using the yeast trihybrid assay"),
    and GFP:MEX-6 is unchanged after pos-1(RNAi). Not an in vitro assay.

## Condensates

- P granules (Tabara 1999; UniProt). Germline P-bodies [PMID:36196602 "germline P-bodies
  can be visualized in P4 as discrete SL1+ poly-A− cytoplasmic puncta that are also positive
  for MEG-1, POS-1 and the canonical P-body markers CGH-1 (DDX6) and EDC-3."] MEG-1/2 are
  needed for regulation of POS-1 targets.

## Phenotypes (necessity, not participation)

- [PMID:9834181 "We show that maternal-effect lethal mutations in the gene pos-1 cause germ
  cell precursors to inappropriately adopt somatic cell fates."] Tabara full text (online):
  terminal embryos lack intestine and germ cell progenitors and have excess pharynx; P4
  makes muscle (D-like); ABp adopts ABa-like fates (no APX-1 signal); in laser-isolated
  pos-1 embryos MS and E make hypodermis.
- P2 cytokinesis protection with PIE-1 (PMID:38696255).
- pos-1 3' UTR deletion: POS-1 patterning and fecundity (PMID:42044121).

## The 9925644 rows (transcription)

- Batchelder et al. 1999 (PIE-1 paper) fused the POS-1 zinc finger region to GAL4 in
  mammalian cells: the TTP and POS-1 zinc finger regions "each repress transcription in a
  site-dependent manner", and the authors say this "should be interpreted cautiously"
  (PMC full text, read online). POS-1 is cytoplasmic; no transcriptional role in worms.
  Rows marked over-annotated, with a PROBABLE CHECK defect for WormBase.

## Source text checks

- UniProt FUNCTION: correct and well cited on PRE, glp-1, GLD-1, neg-1 binding. Wrong on
  where endomesoderm is promoted: "promotes endo-mesoderm development in anterior
  blastomeres" (POS-1 acts in posterior blastomeres; NEG-1 is anterior). Omits translational
  activation (nos-2, apx-1, mom-2).
- WormBase: all claims trace to Tabara 1999, Ogura 2003, Tenlen 2006, except "bind the mex-6
  3'-UTR in vitro" (yeast three-hybrid). Omits PRE specificity, neg-1, zif-1, nos-2.

## Annotation decisions (summary)

- Core: mRNA 3'-UTR binding (IDA), translation repressor activity (IBA), negative
  regulation of translation, cell fate specification, cytoplasm, P granule.
- NEW: positive regulation of translation (nos-2, PMID:16499902); P-body (PMID:36196602).
