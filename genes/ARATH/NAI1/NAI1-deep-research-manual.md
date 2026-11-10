# NAI1 (At2g22770, bHLH020) -- manual literature synthesis

No deep-research API was available for this review; this file is a manual synthesis
from cached publications in `publications/` and PubMed searches
(`NAI1 AND Arabidopsis AND ER body`, 19 hits, all fetched).

## Identity

- UniProt Q8S3F1 (BH020_ARATH), 320 aa, TAIR AT2G22770, GeneID 816807.
- bHLH domain at residues 128-177 (PROSITE PS50888); PANTHER PTHR45959:SF52
  "TRANSCRIPTION FACTOR NAI1"; CDD cd11452 bHLH_AtNAI1_like; C-terminal plant
  ACT-like domain (Pfam PF22754).
- Close paralogs in the same subgroup: AT2G22760 (bHLH019) and AT4G37850 (bHLH025),
  the With/From genes of the IBA cis-regulatory-binding row.

## Molecular function

- Cloned by map-based cloning from the ER-body-less nai1-1 mutant; encodes a bHLH
  protein; transient expression of the cDNA restores ER bodies in nai1-1
  [PMID:15155889 "These results indicate that expression of At2g22770 cDNA complemented the nai1 phenotype."].
- Recombinant NAI1 binds canonical and non-canonical G-box motifs in the NAI2
  promoter and an E-box-containing fragment of the BGLU23/PYK10 promoter; GFP-NAI1
  activates the NAI2 promoter in N. benthamiana in a G-box-dependent manner;
  GFP-NAI1 is nuclear [PMID:33315514 "found that NAI1 binds to the promoter region of NAI2 and activates the NAI2 promoter"]
  (abstract only in cache).
- Homodimerization is inferred by UniProt (ECO:0000305) from the bHLH fold, not shown.

## Targets / downstream genes

- PYK10/BGLU23 and PBP1/JAL30 (At3g16420) are reduced at mRNA and protein level in nai1
  [PMID:15155889].
- NAI2 expression depends on NAI1 [PMID:18780803 "NAI1, a transcription factor responsible for ER body formation, regulates NAI2 gene expression."].
- MEB1 and MEB2 expression reduced in nai1 [PMID:23166355].
- JALs and GLLs reduced in nai1-1 [PMID:18467340].
- NAI1 is required for the active H3K4me3 mark, not for removal of H3K27me3, at PYK10
  [PMID:26479492].
- Inducible (JA / wound) ER bodies and BGLU18 / TSA1 expression are NAI1-independent;
  they depend on MYC2/3/4 [PMID:31879762; PMID:31132914].

## Biological roles

- Required for constitutive ER bodies in seedlings/roots [PMID:12581307; PMID:15155889]
  and for leaf ER bodies (L-ER bodies) [PMID:30696747 "L-ER bodies were seldom observed in nai1 mutant leaves"].
- In ermo3/mvp1/gold36 mutants, ER aggregation requires NAI1 but not NAI2 or PYK10
  [PMID:23155454 "Depletion of NAI1 in ermo3-1 suppressed the formation of ER-aggregates"].
- Plant-microbe: nai1 mutants phenocopy pyk10 in the interaction with Piriformospora indica;
  the effect is attributed to PYK10, not NAI1 per se [PMID:18248598].
- NAI1 expression is induced by MEcPP retrograde signalling [PMID:28965830] and by
  P. syringae; nai1 contributes to the defense response [PMID:34110257].
- Upstream regulator ATML1 activates NAI1 in leaves [PMID:41260534, review].

## Interpretation

NAI1 is a nuclear bHLH DNA-binding transcription activator whose main biological role is
to drive expression of the constitutive ER-body gene battery (PYK10/BGLU23, NAI2, MEB1/2,
JALs, GLLs). ER-body formation is a downstream consequence: NAI1 does not itself build
ER bodies. GO has `GO:0080119 ER body organization` but no regulation-of child.
