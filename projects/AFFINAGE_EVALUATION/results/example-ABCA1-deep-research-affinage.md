---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABCA1
affinage_run_date: 2026-06-09T22:02:36
uniprot_accession: O95477
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 32
citation_count: 34
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ABCA1 (human)

## Current model (mechanistic narrative)

ABCA1 is an ATP-hydrolyzing integral membrane transporter that drives the rate-limiting first step of reverse cholesterol transport, exporting cellular cholesterol and phospholipids to lipid-poor apolipoproteins—principally apoA-I—to nucleate nascent HDL particles; loss-of-function mutations cause Tangier disease [PMID:10882340, PMID:11111099, PMID:11483617]. The purified protein reconstituted in liposomes hydrolyzes ATP in a manner preferentially stimulated by phosphatidylcholine and sphingomyelin and inhibited by specific sterols, establishing its direct enzymatic mechanism [PMID:16500904], and it operates as an extracellular phospholipid translocase that extracts outer-leaflet phospholipids through a hydrophobic gateway/annulus tunnel in its extracellular domain rather than as an inner-to-outer floppase [PMID:35974019]. ABCA1 activity generates two classes of cell-surface apoA-I binding sites—a minor direct ABCA1/apoA-I site and a dominant high-capacity site formed by apoA-I engaging ABCA1-generated lipid domains, the latter requiring the apoA-I C-terminus and driving HDL assembly [PMID:17478755]. ApoA-I binding additionally triggers JAK2/STAT3, PKA, PKC, and CDC42 signaling that feeds back on lipid efflux, protein stability, and inflammation [PMID:22064972]. The transporter cycles between the plasma membrane and endosomes via clathrin/Rab5-mediated retroendocytosis with Rab4-dependent recycling that contributes to efflux [PMID:19170766], and it partitions into lipid rafts and phagosomes in association with syntaxin 13 and flotillin-1 [PMID:15469992]. ABCA1 abundance is tightly controlled transcriptionally—induced by LXR/RXR, RAR, and AMPK–LXRα, and repressed by ORP8, TRAK2, and CXCL12/CXCR4–GSK3β/TCF21 signaling [PMID:14560020, PMID:28655204, PMID:27343431, PMID:31662443]—and post-translationally through calpain-mediated degradation accelerated by PLD2-dependent serine phosphorylation, OSBP, and AGE–RAGE–ubiquitin/lysosomal pathways [PMID:16118212, PMID:18450749, PMID:29097054]. Beyond efflux, ABCA1 restrains TLR4-driven macrophage inflammation through membrane lipid remodeling [PMID:19797709], governs beta-cell cholesterol homeostasis and insulin secretion [PMID:17322896, PMID:22315319], directs hepatic HDL assembly and VLDL secretion [PMID:22001232], maintains astrocyte apoE lipidation and neuroinflammatory tone [PMID:23376685], and acts as a myeloid tumor suppressor by limiting IL-3Rβ/MAPK/JAK2 signaling [PMID:32160545].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140657 ATP-dependent activity, GO:0016787 hydrolase activity, GO:0005215 transporter activity, GO:0008289 lipid binding, GO:0140104 molecular carrier activity
- **localization:** GO:0005886 plasma membrane, GO:0005768 endosome, GO:0005764 lysosome
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-382551 Transport of small molecules, R-HSA-168256 Immune System, R-HSA-5653656 Vesicle-mediated transport, R-HSA-74160 Gene expression (Transcription)
- **partners:** APOA1, STX13, FLOT1, OSBP, PMP22, TRAK2, ARF6, CAV1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2000 | High | ABCA1 mediates active transport of cellular cholesterol and phospholipids to lipid-poor apolipoproteins (especially apoA-I), establishing the first step of reverse cholesterol transport and HDL particle formation. Loss-of-function mutations in ABCA1 cause Tangier disease. | PMID:10882340, PMID:11111099, PMID:11483617 | Current opinion in lipidology |
| 2006 | High | Purified human ABCA1 reconstituted in liposomes displays robust ATPase activity that is stimulated preferentially by phosphatidylcholine and sphingomyelin, inhibited by cholesterol in a structure-specific manner (beta-sitosterol and campesterol inhibit; stigmasterol does not), and suppressed by glibenclamide, providing the first direct biochemical evidence of ABCA1 enzymatic mechanism. | PMID:16500904 | The Journal of biological chemistry |
| 2007 | High | ABCA1 activity creates two types of high-affinity apoA-I binding sites at the cell surface: a low-capacity site formed by direct apoA-I/ABCA1 interaction (regulatory role, ~10% of surface-bound apoA-I) and a much higher-capacity site formed by apoA-I interacting with ABCA1-generated lipid domains (functions in nascent HDL assembly). The C-terminal domain of apoA-I is required for lipid-domain binding but not for direct ABCA1 binding. | PMID:17478755 | Arteriosclerosis, thrombosis, and vascular biology |
| 2008 | High | ABCA1 and apoA-I undergo retroendocytosis via a clathrin- and Rab5-mediated pathway; approximately 30% of endocytosed ABCA1 is recycled back to the cell surface via a Rab4-mediated route. Blocking receptor-mediated endocytosis increases cell-surface ABCA1 but decreases apoA-I-mediated cholesterol efflux from cells with accumulated lipoprotein-derived cholesterol, indicating the retroendocytosis pathway contributes to HDL formation. | PMID:19170766 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2005 | High | Unsaturated fatty acids destabilize ABCA1 protein and impair lipid transport through a phospholipase D2 (PLD2)-dependent pathway: activated unsaturated acyl-CoA derivatives stimulate PLD2, which generates diacylglycerols that promote serine phosphorylation of ABCA1, leading to enhanced ABCA1 degradation. | PMID:16118212 | The Journal of biological chemistry |
| 2003 | High | Retinoic acid receptors RARγ and RARα (but not RARβ) directly bind the DR4 element in the ABCA1 promoter and induce ABCA1 mRNA and protein expression in macrophages, operating through the same promoter element as LXR/RXR. In RARγ-/- macrophages, high RARα compensates for absent RARγ. | PMID:14560020 | Molecular and cellular biology |
| 2004 | High | ABCA1 directly associates with syntaxin 13 (but not syntaxins 3 or 6) and flotillin-1 in lipid raft microdomains and phagosomes. Syntaxin 13 siRNA knockdown reduces ABCA1 protein levels and decreases apoA-I-dependent choline-phospholipid efflux. ABCA1 is identified as a phagosomal protein involved in vesicular lipid transport. | PMID:15469992 | Molecular biology of the cell |
| 2007 | High | Beta-cell-specific inactivation of Abca1 in mice causes markedly impaired glucose tolerance and defective insulin secretion (with normal insulin sensitivity), associated with altered islet cholesterol homeostasis. Rosiglitazone requires beta-cell Abca1 for its beneficial effects on glucose tolerance, establishing ABCA1 as a regulator of beta-cell cholesterol homeostasis and insulin secretion. | PMID:17322896 | Nature medicine |
| 2008 | High | OSBP (oxysterol-binding protein) negatively regulates ABCA1 protein stability by a sterol-binding domain-dependent mechanism: OSBP silencing increases ABCA1 protein half-life by 3-fold without affecting ABCA1 mRNA or LXR transcriptional activity. A sterol-binding domain mutation in OSBP abolishes its destabilizing effect on ABCA1. | PMID:18450749 | The Journal of biological chemistry |
| 2007 | Medium | ORP8 localizes to the endoplasmic reticulum, binds 25-hydroxycholesterol, and acts as a negative regulator of ABCA1 transcription in macrophages: ORP8 silencing by RNAi increases ABCA1 expression and cholesterol efflux to apoA-I, an effect partially mediated through the DR4 and E-box elements in the ABCA1 promoter and synergizing with LXR activation. | PMID:17991739 | The Journal of biological chemistry |
| 2009 | Medium | LRP1 deficiency increases PDGFRβ/MAPK signaling, leading to phosphorylation and activation of cytosolic phospholipase A2 (cPLA2), which releases arachidonic acid that suppresses LXR/RXR activation at the ABCA1 promoter, resulting in greatly reduced ABCA1 expression and impaired cholesterol efflux. | PMID:19718435 | PloS one |
| 2012 | High | miR-33a directly suppresses ABCA1 expression in pancreatic islets via binding to the 3'UTR of ABCA1 mRNA, reducing glucose-stimulated insulin secretion and increasing islet cholesterol. miR-33a-induced insulin secretion defects are rescued by cholesterol depletion or ABCA1 overexpression, confirming the causal link between ABCA1-mediated cholesterol efflux and beta-cell function. | PMID:22315319 | Diabetes |
| 2014 | Medium | RNA-binding protein HuR directly binds the 3'UTR of ABCA1 mRNA (demonstrated by RNA immunoprecipitation) and increases ABCA1 translation. HuR silencing reduces ABCA1 protein expression and cholesterol efflux to apoA-I. Cellular cholesterol levels regulate HuR expression, localization, and its interaction with ABCA1 mRNA. | PMID:24729624 | Journal of lipid research |
| 2015 | High | Apoptotic cells trigger ABCA1 upregulation via a plasma membrane-initiated signaling pathway involving the phagocytic receptor BAI1 (recognizing phosphatidylserine), and intracellular intermediates ELMO1 and Rac1. This pathway operates independently of LXR sterol-sensing machinery; macrophages from BAI1-/- mice show attenuated ABCA1 induction. | PMID:26075824 | The Journal of clinical investigation |
| 2019 | Medium | ApoE4 promotes greater ARF6 expression than ApoE3, trapping ABCA1 in late endosomes and impairing its recycling to the plasma membrane. This results in lower ABCA1-mediated cholesterol efflux, greater lipid-free ApoE4 particles, and lower Aβ degradation capacity. Enhancing ABCA1 activity reduces ApoE4 aggregation and ABCA1 aggregation in hippocampus. | PMID:31641056 | The Journal of neuroscience |
| 2022 | Medium | ABCA1 functions as an extracellular phospholipid translocase that extracts phospholipids from the outer leaflet of the plasma membrane (not as a floppase translocating from inner to outer leaflet). Simulations identified a gateway domain and annulus orifice forming a hydrophobic tunnel in the extracellular domain; engineered mutations in these domains strongly inhibit lipid export without affecting cell-surface ABCA1 expression. | PMID:35974019 | Nature communications |
| 2016 | Medium | TRAK2 is a negative regulator of LXR-mediated ABCA1 expression: TRAK2 siRNA knockdown increases ABCA1 mRNA and protein, enhances cholesterol efflux to apoA-I and HDL, and increases LXR binding at the ABCA1 promoter (by ChIP). The effect of TRAK2 knockdown on cholesterol efflux is abolished in ABCA1-deficient cells, confirming ABCA1 dependence. | PMID:28655204 | European heart journal |
| 2017 | Medium | Plasminogen (PLG) promotes cholesterol efflux specifically through the ABCA1 pathway, and this PLG-dependent efflux is inhibited by lipoprotein(a) [Lp(a)], identifying PLG as a non-HDL acceptor for ABCA1-mediated cholesterol efflux. | PMID:28768900 | JCI insight |
| 2019 | Medium | PMP22 physically interacts with ABCA1 at the Schwann cell plasma membrane (co-immunoprecipitation from nerve lysates); loss of PMP22 reduces ABCA1 membrane localization, decreases apoE secretion, and impairs ABCA1-mediated cholesterol efflux, while ABCA1 KO upregulates PMP22 expression. | PMID:31061090 | The Journal of neuroscience |
| 2015 | Medium | High glucose inhibits LXR-dependent ABCA1 expression in macrophages through reduction of PRMT2 (protein arginine methyltransferase 2); PRMT2-/- macrophages have reduced ABCA1 expression and ABCA1-mediated cholesterol efflux, while monocytes from diabetic mice show decreased PRMT2. | PMID:26288135 | PloS one |
| 2017 | Medium | AGE-albumin (advanced glycation end-products) accelerates ABCA1 degradation through both ubiquitin-proteasome and lysosomal pathways in macrophages, dependent on RAGE signaling (RAGE siRNA prevents ABCA1 reduction). Calpain inhibition does not rescue ABCA1 under AGE-albumin, unlike baseline ABCA1 degradation. | PMID:29097054 | Journal of diabetes and its complications |
| 2016 | Medium | AMPK activation increases ABCA1 and LXRα mRNA and protein in human macrophages through LXRα binding to the LXR responsive element in the ABCA1 promoter (confirmed by ChIP). LXRα silencing attenuates ABCA1 expression after AMPK activation; AMPK knockdown decreases ABCA1 and LXRα expression. | PMID:27343431 | The international journal of biochemistry & cell biology |
| 2015 | Medium | CXCL12, acting through CXCR4, activates the GSK3β/β-catenin(T120)/TCF21 signaling pathway to suppress ABCA1 transcription in macrophages: CXCL12 phosphorylates GSK3β and β-catenin(T120), inhibiting TCF21, which normally drives ABCA1 promoter activity. CXCR4 knockdown or inhibition blocks these effects. | PMID:31662443 | Journal of lipid research |
| 2019 | Medium | ABCA1 modulates intraocular pressure by regulating aqueous humor outflow through a caveolin-1/endothelial NOS/NO signaling pathway: ABCA1 upregulation decreases caveolin-1 and increases eNOS expression and NO production in angular aqueous plexus cells, decreasing transendothelial resistance; ABCA1 downregulation has opposite effects. Intracameral injection of LXR agonist GW3965 decreases IOP in vivo. | PMID:32428234 | Investigative ophthalmology & visual science |
| 2020 | Medium | ABCA1 mutations in CMML patients confer a proliferative advantage to myeloid cells; mechanistically, ABCA1 mutations increase IL-3Rβ signaling via MAPK and JAK2, causing metabolic reprogramming. In vivo inactivation or expression of ABCA1 mutants in hematopoietic cells (in Tet2-/- background) promotes myeloproliferation. ApoA-I transgene overexpression dampens myeloproliferation, bypassing ABCA1 defects. | PMID:32160545 | Cell reports |
| 2025 | Medium | Caveolin-1, a sensor of cellular cholesterol accumulation, promotes ABCA1 endolysosomal trafficking and lysosomal trapping. In APOE4 and AD models, oxysterol accumulation increases caveolin-1 and ABCA1 expression, trapping ABCA1 in lysosomes, activating mTORC1, and driving cellular senescence. Cyclodextrin treatment reduces brain oxysterol levels, ABCA1 lysosomal trapping, mTORC1 activation, and senescence markers in APOE4-TR mice. | PMID:39901180 | Molecular neurodegeneration |
| 2013 | Medium | Astrocyte-specific ABCA1 controls brain apoE levels in vivo; ABCA1-deficient astrocytes show reduced apoE, whereas neuronal ABCA1 deficiency does not affect apoE levels. Brain ABCA1 deficiency causes cortical astrogliosis, increased MAPK activation, and augmented TLR4-induced inflammatory responses. Microglia lacking ABCA1 show increased TNFα secretion and decreased phagocytosis. | PMID:23376685 | Neurobiology of disease |
| 2009 | Medium | ABCA1 activity suppresses macrophage inflammation by modulating Toll-like receptor (TLR4) signaling; ABCA1 deficiency increases TLR4-mediated inflammatory cytokine and chemokine signaling, mechanistically linking cholesterol efflux to anti-inflammatory function through membrane lipid organization. | PMID:19797709 | Arteriosclerosis, thrombosis, and vascular biology |
| 2012 | Medium | ApoA-I/ABCA1 interaction activates multiple downstream signaling pathways including JAK2/STAT3, PKA, Rho family GTPase CDC42, and PKC. PKA and CDC42 activation regulate ABCA1-mediated lipid efflux; PKC activation stabilizes ABCA1 protein; JAK2/STAT3 activation regulates both lipid efflux and anti-inflammatory function. | PMID:22064972 | Molecular medicine (Cambridge, Mass.) |
| 2015 | Medium | TLR4 signaling via IRAK1 downregulates ABCA1 expression and promotes lipid accumulation in vascular smooth muscle cells (VSMCs). IRAK1 siRNA knockdown reverses oxLDL/TLR4-induced ABCA1 downregulation. In TLR4 KO mice on a high-fat diet, IRAK1 expression and lipid accumulation are reduced with concomitant restoration of ABCA1. | PMID:26512959 | Cell death & disease |
| 2011 | Medium | Hepatic ABCA1 is required for nascent HDL particle assembly; hepatocyte-specific ABCA1 KO (HSKO) mice show increased hepatic secretion of large TG-enriched VLDL1 particles, 50% lower LDL, and 80% reduction in HDL, with hypercatabolism of apoA-I by the kidney. Silencing ABCA1 in hepatoma cells reduces PI3K activation and increases secretion of large TG-enriched VLDL1, linking hepatic ABCA1 to VLDL metabolism. | PMID:22001232 | Biochimica et biophysica acta |
| 2016 | Low | Piperine stabilizes ABCA1 protein by inhibiting calpain-mediated ABCA1 degradation, increasing ABCA1 half-life without affecting ABCA1 mRNA levels, thereby promoting cholesterol efflux from macrophages. | PMID:27862930 | Molecular nutrition & food research |

## Citations

- PMID:10882340
- PMID:11111099
- PMID:11483617
- PMID:14560020
- PMID:15469992
- PMID:16118212
- PMID:16500904
- PMID:17322896
- PMID:17478755
- PMID:17991739
- PMID:18450749
- PMID:19170766
- PMID:19718435
- PMID:19797709
- PMID:22001232
- PMID:22064972
- PMID:22315319
- PMID:23376685
- PMID:24729624
- PMID:26075824
- PMID:26288135
- PMID:26512959
- PMID:27343431
- PMID:27862930
- PMID:28655204
- PMID:28768900
- PMID:29097054
- PMID:31061090
- PMID:31641056
- PMID:31662443
- PMID:32160545
- PMID:32428234
- PMID:35974019
- PMID:39901180
