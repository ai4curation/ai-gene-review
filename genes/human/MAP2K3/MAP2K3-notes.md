# MAP2K3 (MKK3) curation notes

UniProt P46734 (MP2K3_HUMAN), 347 aa, HGNC:6843. STE-group protein kinase, MAP kinase kinase subfamily.

## Identity and catalytic function

- Dual-specificity MAP2K: [file:human/MAP2K3/MAP2K3-uniprot.txt "Dual specificity kinase. Is activated by cytokines and"; "of a threonine and a tyrosine residue in the MAP kinase p38."]
- Cloned alongside MKK4 as a p38 activator that does not activate ERK: [PMID:7839144 "Two human MAP kinase kinases (MKK3 and MKK4) were cloned that phosphorylate and activate p38 MAP kinase. These MKK isoforms did not activate the ERK subgroup of MAP kinases, but MKK4 did activate JNK."] -> unlike MKK4, MKK3 is p38-selective (does not activate JNK).
- Activated MKK3 selectively increases p38 activity in cells; downstream reporter output via ATF2/Elk-1: [PMID:8622669 "Expression of activated MKK3 and MKK6 in cultured cells caused a selective increase in p38 MAP kinase activity."]
- Activation loop: Ser218/Thr222 (canonical isoform numbering) are the MAP3K target sites; S/T->A inactivates, S/T->E constitutively activates [file:human/MAP2K3/MAP2K3-uniprot.txt "Activated by dual phosphorylation on Ser-218 and"]. Reactome describes the same sites as Ser189/Thr193 (isoform 1 numbering, which lacks residues 1-29) [Reactome:R-HSA-450346 "Residues involved into these protein kinases activation correspond to human sites Ser189 and Thr193 for MKK3"].
- p38 selectivity: [Reactome:R-HSA-450346 "both phosphorylate and activate p38 MAP kinase at its activation site Thr-Gly-Tyr but do not phosphorylate or activate Erk1/2 or SAPK/JNK."] Note that this Reactome summary contains a typo ("MKK3 (MAP2K4)").
- Deep research (falcon) summary: [file:human/MAP2K3/MAP2K3-deep-research-falcon.md "The strongest conclusion is that MKK3 is selective at the MAPK-family level for **p38 MAPKs**, rather than ERK1/2 or JNK."] Within the p38 family, p38alpha (Thr180/Tyr182) best established; isoform preferences vs MKK6 are context dependent.
- UniProt Rhea mappings list Ser, Thr and Tyr protein kinase reactions for EC 2.7.12.2 (all attributed to PMID:8622669). The physiologically established reaction is Thr+Tyr phosphorylation of the p38 TGY motif; the serine reaction is a generic EC-level mapping. Treat GO:0106310 / GO:0004713 / GO:0004672 as less informative than GO:0004708 (same handling as MAP2K2 review).

## Upstream activators (MAP3Ks)

- ASK1/MAP3K5: [Reactome:R-HSA-3228469 "MAP3K5 (ASK1) phosphorylates and activates MAP2K3 (MKK3) and MAP2K6 (MKK6)"]; ASK1 "substrate MKK3" complex [PMID:21771788 "increasing complex formation between ASK1 and its substrate MKK3"].
- TAK1 (Reactome R-HSA-450346, R-HSA-450302).
- TAO2/TAOK2: [PMID:11279118 "Coimmunoprecipitation demonstrated that endogenous TAO2 specifically associates with MEK3 and MEK6 providing one mechanism for preferential recognition of MEKs upstream of p38."]
- LRRK2 binds and phosphorylates MKK3: [PMID:20067578 "we show that LRRK2 binds to MAPK kinases (MKK) 3, 6, and 7, and that LRRK2 is able to phosphorylate MKK3, 6 and 7."]
- Deep research lists MEKK1-4, MLK2/3, DLK, ASK1, Tpl2/Cot, TAK1 as upstream MAP3Ks.

## Downstream / other partners

- p38alpha (MAPK14) is the substrate; interaction seen in multiple HT interactome studies (PMID:23602568, 31980649, 32707033, 33961781) and UniProt IntAct (NbExp=7). Mxi2 (p38alpha splice variant) binds MKK3/6 [PMID:17255949 "Mxi2 is capable of interacting with MKK 3 and 6"].
- DYRK1B/Mirk: co-IP and MKK3 enhanced Mirk kinase activity [PMID:11980910 "Mirk co-immunoprecipitated with the MAPK kinase MKK3, an upstream activator of p38. MKK3 enhanced Mirk kinase activity and the transcriptional activation of HNF1alpha by Mirk"]. Whether MKK3 phosphorylates Mirk directly is not stated in the abstract.
- AKAP13-PKN1 signalosome with MAPK14, ZAK (MAP3K20) and MAP2K3 downstream of ADRA1B (UniProt, PMID:21224381).
- TINF2: only from a genome-wide BiFC screen (PMID:21044950); no functional follow-up.

## Localisation

- Cytoplasm and nucleus: [Reactome:R-HSA-450296 "The p38 activators MKK3 (MAP2K3) and MKK6 (MAP2K6) were present in both the nucleus and the cytoplasm"]. Membrane detection in NK-cell membrane proteome (PMID:19946888) is HT; ARRB1-dependent recruitment to plasma membrane signalosome reported (UniProt PMID:16709866).

## Biological context (downstream, non-core)

- VEGF-induced endothelial migration: [PMID:22696064 "the VEGF-induced activation of p38 and cell migration are impaired when the MKK3 expression is knocked down by siRNA."]
- Hippo/YAP: MKK3 overexpression promotes F-actin accumulation and YAP nuclear localisation [PMID:27402810 "The Lic homologue MKK3 promoted nuclear localization of YAP by inducing F-actin accumulation."] - indirect, via p38/actin.
- Osmotic stress (sorbitol activates TAO2 toward MEK3/6, PMID:11279118), LPS/inflammation, ischemia, senescence (Reactome oxidative-stress-induced senescence): p38 pathway contexts.
- Anthrax lethal factor cleaves MKK3 in cytosol (Reactome R-HSA-5211400); Yersinia YopJ acetylates MKK3 activation-loop residues (UniProt).

## Curation decisions summary

- Core MF: GO:0004708 MAP kinase kinase activity (IDA, IBA, TAS, IEA all accepted).
- Core BP: GO:0038066 p38MAPK cascade (IMP/IEA/TAS accepted); GO:0031098 SAPK cascade accepted (parent).
- Kinase residue-type terms (GO:0004672, GO:0004713, GO:0106310) -> MODIFY to GO:0004708, following MAP2K2 review.
- Protein binding (12 rows): MAPK14 partners -> GO:0051019 MAP kinase binding; MAP3K5 -> GO:0031435 MAPKKK binding; LRRK2 and DYRK1B -> GO:0019901 protein kinase binding; TINF2 (HT BiFC only) -> REMOVE.
- TAOK2 protein kinase binding IPI -> MODIFY to GO:0031435 (TAO2 acts as a MAP3K for MEK3/6).
- Downstream contexts (VEGF response, EC migration, Hippo, senescence, LPS, sorbitol, ischemia) -> KEEP_AS_NON_CORE; heart development (rat IEA) and positive regulation of transcription (Mirk/HNF1a reporter, indirect) -> MARK_AS_OVER_ANNOTATED.
