# CRLS1 (human) review notes

UniProt Q9UJA2, Cardiolipin synthase (CMP-forming), EC 2.7.8.41. Synonyms C20orf155, CLS1, hCLS1.
301 aa, five predicted TM helices, Pfam PF01066 (CDP-OH_P_transf), InterPro IPR000462 /
IPR050324 (CDP-alcohol phosphatidyltransferase class I), PANTHER PTHR14269:SF60.

## Process log

- 2026-10-09: `just fetch-gene-pmids human CRLS1` cached the 6 GOA PMIDs. Additionally cached
  PMID:20025994 (Nie 2010), PMID:31914590 (Kasahara 2020), PMID:29343430 (Serricchio 2018),
  PMID:42414597 (2026 heart Crls1 KO) via `just fetch-pmid`.
- Deep research: `just deep-research-falcon human CRLS1 --fallback perplexity-lite` FAILED.
  Falcon timed out after 600 s; the perplexity-lite fallback failed with "Provider 'perplexity'
  not available. Available: falcon, asta, openscientist". The review was written from direct
  PubMed MCP research and the cached publications. The underlying falcon job nevertheless
  completed later (15:56) and wrote CRLS1-deep-research-falcon.md (tool-generated, 69 citations).
  On a scan it agrees with this review: CDP-DAG + PG -> CL + CMP is the core activity, and
  disease and knockout phenotypes (COXPD57, mouse muscle, heart, macrophage complex II) are
  downstream consequences of cardiolipin loss, not additional CRLS1 activities. It does not
  discuss the Nie 2010 LPG acyltransferase claim. No review decisions changed.

## Molecular function: CDP-type cardiolipin synthase

- Final step of eukaryotic de novo CL synthesis: CDP-DAG + PG -> CL + CMP.
  [PMID:16716149 "CLS (cardiolipin synthase) is involved in the final step of cardiolipin synthesis
  by catalysing the transfer of a phosphatidyl residue from CDP-DAG (diacylglycerol) to PG
  (phosphatidylglycerol)"]
- Three independent 2006 groups identified the human gene:
  - Houtkooper et al.: complementation of yeast crd1 null; enzyme characterised in mitochondria
    of the complemented strain; alkaline pH optimum, divalent-cation requirement.
    [PMID:16678169 "Expression of this candidate cDNA in the (cardiolipin synthase-deficient)
    crd1Delta yeast confirmed that it indeed encodes human cardiolipin synthase."]
  - Chen et al. (Lilly): recombinant enzyme in COS-7 makes CL from CDP-DAG + PG in vitro; mito
    localisation by IF and fractionation. [PMID:16716149]
  - Lu et al. (Feingold/Hatch): expression raised CLS activity, specific for CL (no PGP synthase
    increase); CL pool increased. [PMID:16547353 "The enzyme is specific for CL synthesis"]
- It is the CDP-alcohol phosphatidyltransferase (CDP-type) CLS, not the PLD-type
  (2 PG -> CL + glycerol; GO:0008808 "cardiolipin synthase activity") found in bacteria and some
  protist mitochondria. All MF annotations on CRLS1 (GO:0043337 and its ancestor GO:0016780 via
  IPR000462) are on the CDP-type branch; there is no GO:0008808 annotation. Confirmed via
  QuickGO that GO:0016780 is an is_a ancestor of GO:0043337 and that GO:0008808 is defined as the
  PG + PG reaction.
- Chen et al. 2026 Cell comparative mitoproteome paper: LECA mitochondria likely had both
  CDP-type and PLD-type CLS, differentially lost; PLD-type CLS is a candidate pathogen target
  (absent in humans, essential in P. knowlesi). [PMID:42822426 "LECA mitochondria also contained
  multiple pairs of non-homologous enzymes with similar activities, such as class I and"]
  This is comparative/computational context, not evidence for CRLS1's activity.

## Disputed secondary activity: LPG acyltransferase

- Nie et al. 2010 (Shi lab, same group as PMID:16716149) reported acyl-CoA-dependent LPG
  acyltransferase activity of recombinant and purified hCLS1, independent of CDP-DAG.
  [PMID:20025994 "In this report, we identified a novel function of the hCLS1 enzyme as an acyl-CoA dependent LPG acyltransferase."]
- This is the basis of the Reactome events R-HSA-1482546 / R-HSA-1482689 ("LPG is acylated to PG by
  CRLS1") and R-HSA-1482925 (PG acyl-chain remodelling).
- Caveats: (i) single-lab, apparently not replicated; (ii) mechanistically unusual: CRLS1 is a
  CDP-alcohol phosphotransferase with no acyltransferase motif; (iii) the positive control used
  (LPGAT1) has since been reassigned (LPLAT7, see genes/human/LPGAT1 review, PMID:36049524), which
  weakens confidence in the LPG acyltransferase assay system; (iv) the GO terms Reactome mapped
  (GO:0003841, GO:0047144) are lysophosphatidic acid (LPA) acyltransferase activities, a different
  substrate from LPG, so these mappings are wrong regardless.

## Localisation

- Mitochondrial inner membrane, multipass. [PMID:16547353 UniProt cites for IM];
  [PMID:16716149 "the recombinant hCLS1 protein was localized to the mitochondria"]
- Mieap paper (PMID:38322995) treats EGFP-CRLS1 as an inner membrane marker and shows it in the
  Mieap-depleted phase of Mieap condensates; cites a 700-800 kDa CL synthesis complex.
- Serricchio et al. 2018: PGS1 associates with CLS1 and PTPMT1 in large complexes.
  [PMID:29343430 "We show that PGS1 forms oligomers and associates with CLS1 and PTPMT1."]
  (abstract only)

## Physiology / disease

- Biallelic CRLS1 variants cause COXPD57: progressive mitochondrial encephalopathy; patient
  fibroblasts show reduced CL, increased PG; WT CRLS1 rescues mitochondrial morphology.
  [PMID:35147173 "significantly increased levels of phosphatidylglycerol, the substrate of CRLS1"]
- Crls1 null mice: peri-implantation lethality; neuronal cKO -> neurodegeneration, abnormal cristae,
  reduced ETC supercomplexes. [PMID:31914590 "Homozygous null mutant mice exhibited early embryonic lethality at the peri-implantation stage."]
- Cardiomyocyte cKO blocks postnatal CL increase, cristae and respiratory chain maturation, death
  by 2 weeks; tafazzin cKO does not. [PMID:42414597]
- These are downstream consequences of CL loss; they support the CL biosynthesis BP but should not
  generate separate BP annotations (cristae organization, heart development, etc.) for CRLS1.

## Annotation decisions (summary)

- ACCEPT: GO:0043337 (all), GO:0032049 (all), GO:0005743 (all), GO:0005739 IDA/IBA/HTP.
- GO:0016780, GO:0008654, GO:0046474, GO:0016020: correct but general IEA -> ACCEPT (broad IEA
  consistent with the CDP-type mechanism).
- GO:0031966 ISS: accept (IM is more specific, already present).
- GO:0003841 / GO:0047144 (Reactome TAS, LPA acyltransferase): REMOVE (wrong substrate; underlying
  LPG acyltransferase claim single-lab and doubtful).
- GO:0036148 PG acyl-chain remodeling (Reactome TAS): UNDECIDED.
