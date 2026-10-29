# ARA1 (YBR149W, P38115) review notes

## Identity
- D-arabinose dehydrogenase [NAD(P)+] "heavy chain", EC 1.1.1.117; aldo-keto reductase AKR3C [UniProt:P38115].
- UniProt still says heterodimer of heavy and light chain, but the light chain is an N-terminal degradation product and recombinant Ara1 is a homodimer [PMID:17151466 "the small subunit of ARA previously thought as is, in fact, a naturally occuring degradation product of Ara1p"].

## Function
- Purified from the cytosolic fraction [PMID:9920381 "D-Arabinose dehydrogenase was purified 843-fold from the cytosolic fraction of Saccharomyces cerevisiae"].
- Broad sugar specificity with NADP+, high Km [PMID:9920381 "The enzyme catalysed the oxidation of D-arabinose, L-xylose, L-fucose and L-galactose in the presence of NADP+."; Km 161 mM for D-arabinose].
- Deletion abolished activity and erythroascorbate in the original study [PMID:9920381 "In the deletion mutant of this gene, D-arabinose dehydrogenase activity and D-erythroascorbic acid were not detected."], but a later study found eAsA only halved [PMID:17151466 "A deficient mutant of ARA1 lost almost all NADP(+)-ARA activity, but intracellular D-erythroascorbic acid was only halved."]; Ara2 is the main contributor [PMID:17097644 "Ara2p, not Ara1p, mainly contributes to the production of eAsA from d-arabinose in S. cerevisiae."].
- Also a broad carbonyl reductase: reduces (R)-acetoin to meso-2,3-butanediol, contributing in vivo [PMID:33845171 "Ara1, Ypr1, and Ymr226c (named Ora1) were identified as (S)-alcohol-forming reductases, which can reduce (R)-acetoin to meso-2,3-BDO in vitro. However, only Ara1 and Ypr1 contributed to meso-2,3-BDO production in vivo."].

## Curation conclusions
- Core MF GO:0045290 D-arabinose 1-dehydrogenase [NAD(P)+] activity (NADP+ preferred; GO:0106271 is the NADP+-specific child).
- BP GO:0070485 (minor contributor); cytosol.
- Aldose reductase IBA: no aldose-to-alditol reduction tested for Ara1; left UNDECIDED.
- Conflict between PMID:9920381 (no eAsA in deletion) and PMID:17151466 (eAsA halved) noted.
