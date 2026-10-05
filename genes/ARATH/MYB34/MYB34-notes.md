# MYB34 (ATR1, At5g60890) review notes

Context: part of the ARATH_SINGLE_CELL_FUNGAL project (Tang et al. 2023, PMID:37741284).

## Identity
- UniProt O64399, 295 aa R2R3-MYB with two Myb HTH repeats (9-61, 62-116). It belongs to
  subgroup 12 with MYB28/29/76 (aliphatic GSL) and MYB51/MYB122 (indolic GSL).
  [PMID:17420480 "Myb28 and Myb29 belong to the R2R3-Myb gene family, clustered into a small subgroup with Myb34 and Myb76"]
- Found as the dominant allele atr1D, which raises ASA1 transcription.
  [PMID:9576939 "One of these mutants, atr1D is dominant for increased transcription of ASA1 in specific seedling tissues."]
  [PMID:9576939 "ATR1 encodes a Myb-like transcription factor that modulates ASA1 expression."]

## Function: indolic glucosinolate / Trp-pathway transcriptional activator
- Overexpression raises IAA and IGs. Loss of function lowers IG gene expression and IG levels.
  [PMID:15579661 "we show that ATR1 overexpression confers elevated levels of IAA and IGs. In addition, we show that an atr1 loss-of-function mutation impairs expression of IG synthesis genes and confers reduced IG levels."]
- In the atr1-2 mutant, IG is about 20% lower in adult leaves. Trp synthesis genes (ASA1/TSB1) are unchanged.
  [PMID:15579661 "Correspondingly, IG measurements showed approximately 20% reduced IG accumulation in atr1-2 adult leaves"]
- Proposed to act as a direct activator.
  [PMID:15579661 "The simplest model is that ATR1 serves as a direct transcriptional activator of both Trp synthesis genes and Trp secondary metabolism genes"]
- Trans-activates promoters.
  [PMID:23580754 "MYB34, MYB51, and MYB122, identified as regulators of the indolic glucosinolate biosynthetic pathway, exclusively trans-activate the promoters of TSB1, CYP79B2, and CYP79B3"]
- Division of labour among the paralogs.
  [PMID:24431192 "MYB34 controlling biosynthesis of IGs mainly in the roots, MYB51 regulating biosynthesis in shoots, and MYB122 having an accessory role"]
  [PMID:24431192 "MYB34 is the key regulator upon ABA and JA signaling"]
  [PMID:24431192 "The myb34 myb51 myb122 triple mutant is devoid of IGs"]
- bHLH partners.
  [PMID:25049362 "we have uncovered the interactions of MYB34, MYB122, MYB28, and MYB29 with both bHLH05 and bHLH04 using BiFC"]
  PMID:23943862 (abstract): MYC2/3/4 interact directly with GS-related MYBs.
- Brassinosteroids: BR repression of GSL is lost in myb34 (PMID:23580754).
- Sulfur deficiency: MYB34 transcript is down-regulated. This is expression only.
  [PMID:17420480 "Under sulfur-deficiency conditions, the expression of PMG1 / Myb28 , PMG2 / Myb29 , and ATR1 / Myb34 was down-regulated"]

## Defence
- Aphid: atr1D is more resistant because of IG breakdown products.
  [PMID:18346197 "atr1D mutant plants, which overproduce indole glucosinolates, are more resistant to M. persicae"]
- Fungi: the triple mutant is more susceptible to P. cucumerina.
  [PMID:26802248 "MYB34/51/122 contribute to resistance toward P. cucumerina exclusively through IG biosynthesis"]
- Tang et al. 2023 (full text from the user-supplied PDF; the cached copy is abstract only):
  "Three transcription factors were proposed to regulate GSL biosynthesis ... however,
  only MYB51 and MYB122 exhibited induction at infection sites" (MYB122 in the epidermis,
  MYB51 in the vasculature). MYB34 was NOT induced at C. higginsianum infection sites.
  This is consistent with MYB34 acting mainly in roots and under ABA/JA.

## Annotation decisions (summary)
- GO:0000162 Trp biosynthesis (IMP, atr1D): MODIFY to GO:2000284 positive regulation of amino acid biosynthetic process. MYB34 is a TF, not a pathway enzyme.
- GO:0009759 IG biosynthesis (IMP): MODIFY to GO:0010439 regulation of glucosinolate biosynthetic process. Also added as NEW (IMP, PMID:24431192). NTR proposed: positive regulation of indole glucosinolate biosynthetic process.
- GO:0000976 x5 (ARBA + four Y1H screens): ACCEPT for the MF.
- GO:0003700 ISS, GO:0045893 IMP, nucleus x3: ACCEPT.
- GO:0005515 Y2H with uncharacterized A0A1P8BA81: REMOVE (uninformative).
- GO:0002213 defense response to insect: KEEP_AS_NON_CORE (gain of function, indirect).
- GO:0006950, GO:0051707 (ARBA), GO:0010438 S-starvation (TAS, expression only): MARK_AS_OVER_ANNOTATED.

## Additional evidence (second pass, synthesizing multiple lines)
- Deep research: `just deep-research-falcon ARATH MYB34 --fallback perplexity-lite`. The
  wrapper hit its 600 s timeout and the perplexity-lite fallback is not available here.
  The falcon run still finished (794 s) and wrote MYB34-deep-research-falcon.md (48
  citations), and that report was used. It agrees with the primary literature: MYB34 is
  a transcriptional regulator, not an enzyme ("MYB34 is neither a biosynthetic enzyme
  nor a glucosinolate transporter"). It also points out that direct MYB34 promoter
  occupancy has not been shown by ChIP; promoter ChIP exists for MYC2 only.
- Target-promoter evidence: MYB34 trans-activates pCYP79B2 but not the camalexin-specific
  pCYP71B15 in cultured Arabidopsis cells.
  [PMID:26379682 "The activity of pCYP79B2:uidA increased, whereas that of pCYP71B15:uidA was not affected by all three MYB factors"]
  Earlier work reports trans-activation of TSB1/CYP79B2/CYP79B3 (PMID:23580754). Four Y1H
  screens recovered MYB34 binding to promoter fragments (GOA IPI rows).
- Expression responses: MYB34 is NOT induced by elicitors, wounding or touch, unlike MYB51 and MYB122.
  [PMID:26379682 "However, the expression of MYB34 was reduced, indicating that it plays a less important role in phytoalexin regulation."]
  [PMID:17461791 "Mechanical stimuli such as touch or wounding transiently induced the expression of HIG1/MYB51 but not of ATR1/MYB34"]
  This fits with Tang 2023 (no induction at C. higginsianum infection sites). So the Tang
  result is one of several consistent lines of evidence and is not decisive on its own.
- Camalexin: MYB34 affects camalexin only indirectly, through the IAOx supply (IAOx
  feeding rescues the triple mutant). No camalexin annotation is proposed (PMID:26379682).
- Brassinosteroid crosstalk: BES1 interacts with MYB34/51/122 and represses indolic GSL
  genes (PMID:31776183). In myb34, BR repression of GSL is lost (PMID:23580754).
- Overexpression in hig1-1 (myb51) partially rescues the IG chemotype and causes a
  high-auxin phenotype (PMID:17461791). This fits with MYB34 pushing flux into IAOx, the
  branch point shared with IAA.
- PANTHER: PTHR47994:SF5 ("F14D16.11-RELATED"), a broad plant R2R3-MYB family. GOA has no
  IBA annotations for MYB34 (or for MYB51), so there are no PAINT node placements to
  evaluate. The ortholog distribution of subgroup 12 was not analysed bioinformatically
  in this review.
- Consistency with the sibling MYB51 review (genes/ARATH/MYB51): the same choices were
  made. GO:0009759 is changed by MODIFY to GO:0010439. GO:0001228 is added as NEW (IDA,
  trans-activation). The core MF is GO:0001228 and the location is nucleus.
