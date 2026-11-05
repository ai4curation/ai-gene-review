# CG3226 (Q9W3Y3) notes

## Identity
- D. melanogaster CG3226 (FBgn0029882), 230 aa, TrEMBL Q9W3Y3; ortholog of mammalian
  CacyBP/SIP (human CACYBP, Q9HB71). Domains (UniProt DR lines): Siah-Interact_N
  (PF09032), CS domain (PF04969; HSP20-like fold), SGS domain (PS51048);
  PANTHER PTHR13164:SF3 "CALCYCLIN-BINDING PROTEIN".
- All UniProt function/location text for Q9W3Y3 is ARBA-only (not usable as evidence).

## Fly literature
Only one fly paper (PubMed search "CG3226", "Siah-interacting protein Drosophila",
"calcyclin-binding Drosophila" -> PMID:22398840, PMID:11146551 [unrelated]).
- Casad et al. 2012 [PMID:22398840]: deficiency screen by OCT in adult flies.
  Df(1)Exel6240 and a 19 kb deletion show dilated cardiomyopathy; CG3226 genomic
  transgene rescues and "Heart specific expression of CG3226 rescued heart function
  in Df(1)Exel6240". Phenotype is adult heart function (enlarged EDD/ESD, reduced
  fractional shortening). Authors note "The Drosophila gene orthologous to SIP has
  not been characterized in the Sina complex nor in the Drosophila Armadillo pathway".
  Decreasing Armadillo signalling in the heart reduced chamber size (not a CG3226
  manipulation). FlyBase curated this as heart development IMP.

## Mammalian ortholog (for inference)
- SIP binds Siah-1 and Skp1, bridging Siah to the F-box protein Ebi for
  beta-catenin degradation [PMID:11389839 "Siah is physically linked to Ebi by
  association with a novel Sgt1 homolog SIP that binds Skp1"].
- Structure: [PMID:16085652 "SIP engages Siah1 by means of two elements"];
  "The E3 complex comprises, in addition to Siah1, Siah-interacting protein (SIP),
  the adaptor protein Skp1, and the F-box protein Ebi" - a Siah RING E3, not a
  cullin-based SCF.
- Human CACYBP binds S100A1, S100A6, S100B, S100P, S100A12 (UniProt Q9HB71 SUBUNIT).
- Reported tubulin binding and ERK1/2 phosphatase activity for mammalian
  CacyBP/SIP are not tested in flies.

## S100 taxonomy (re: Wei et al. 2020, PMID:32470107 flag on GO:0044548)
- [PMID:31837246 "The calcium-binding, vertebrate-specific S100 protein family"]
- [PMID:18275604 "There is no evidence for S100 proteins in invertebrates"]
- [PMID:27764152 "All S100 hits were within vertebrates, with the exception of four
  hits from the tunicate Oikopleura dioica"] - so strictly chordate (vertebrate +
  tunicate) rather than vertebrate-only; none in cephalochordates, echinoderms,
  hemichordates searched.
- Own check (CG3226-bioinformatics/RESULTS.md): Pfam PF01023 S_100 proteins in
  UniProt: D. melanogaster 0; Insecta 1; Arthropoda 3; Vertebrata 12350.
- Verdict: the Wei et al. flag holds. The InterPro2GO mapping IPR037893 ->
  GO:0044548 transfers a vertebrate partner interaction to all CacyBP family
  members; for Drosophila (no S100 genes) the annotation should be removed.
  Better fixed with a taxon constraint on GO:0044548 or by narrowing the mapping.

## Decisions
- S100 protein binding IEA: REMOVE.
- tubulin binding IEA: over-annotated (no fly data; consistent with CACYBP review).
- SCF complex IBA: over-annotated (Siah complex is non-cullin; consistent with CACYBP).
- ubiquitin protein ligase binding IBA/IEA, molecular adaptor activity IBA: ACCEPT
  (conserved Siah-Interact_N and SGS/CS domains; fly Sina orthologs exist) but untested.
- heart development IMP/IBA: KEEP_AS_NON_CORE; phenotype is adult cardiomyopathy;
  deferring to FlyBase curator on term choice.
- nucleus/cytoplasm: ACCEPT by orthology.
