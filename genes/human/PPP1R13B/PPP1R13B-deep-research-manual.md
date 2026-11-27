---
title: Manual literature synthesis for human PPP1R13B / ASPP1
gene: PPP1R13B
organism: human
provider: manual
---

# PPP1R13B / ASPP1 manual synthesis

PPP1R13B encodes ASPP1, one of the pro-apoptotic ASPP proteins. Its strongest
curated molecular function is binding p53-family transcription factors via the
ASPP C-terminal ankyrin-repeat/SH3 module. Samuels-Lev et al. identified ASPP1
as homologous to the C-terminal half of ASPP2 and showed that ASPP proteins
interact with p53, enhance p53 binding and transactivation at pro-apoptotic
promoters, and stimulate p53-induced apoptosis but not cell-cycle arrest
[PMID:11684014]. Bergamaschi et al. showed that ASPP1 and ASPP2 also bind p63
and p73 and selectively enhance their transcriptional activity at Bax, PIG3 and
PUMA promoters rather than at the MDM2 or p21 promoters [PMID:14729977].

The protein also binds p300 [PMID:21513714] and PP1 catalytic subunits
[PMID:21998301; PMID:28330616], but these rows are currently represented only
as generic `GO:0005515 protein binding` annotations. Because bare protein
binding does not identify the regulatory activity, these rows are removed by
policy while the row-specific interactors are preserved in `supporting_entities`.

PPP1R13B is not simply interchangeable with TP53BP2 for all transferred
annotations. UniProt describes ASPP1 as cytoplasmic with a nuclear fraction,
and the p53-family literature supports nuclear/nucleoplasmic function, but I
found no direct PPP1R13B evidence for perinuclear-region or adherens-junction
residence. Likewise, the `negative regulation of cell cycle` rows appear to
borrow ASPP2/APP-BP1 biology; the shared ASPP1/ASPP2 p53-family papers
emphasize pro-apoptotic target genes rather than the p21 cell-cycle branch.
Those propagated locations and processes should be marked over-annotated rather
than treated as the conserved ASPP-family core.
