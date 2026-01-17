---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T13:08:06.676302'
end_time: '2026-01-15T13:25:19.950373'
duration_seconds: 1033.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ACSL4
  gene_symbol: ACSL4
  uniprot_accession: O60488
  protein_description: 'RecName: Full=Long-chain-fatty-acid--CoA ligase 4 {ECO:0000305};
    EC=6.2.1.3 {ECO:0000269|PubMed:21242590, ECO:0000269|PubMed:22633490, ECO:0000269|PubMed:24269233};
    AltName: Full=Arachidonate--CoA ligase {ECO:0000305}; EC=6.2.1.15 {ECO:0000269|PubMed:21242590};
    AltName: Full=Long-chain acyl-CoA synthetase 4; Short=LACS 4;'
  gene_info: Name=ACSL4; Synonyms=ACS4, FACL4, LACS4;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the ATP-dependent AMP-binding enzyme family.
  protein_domains: AMP-bd_C_sf. (IPR045851); AMP-binding_CS. (IPR020845); AMP-dep_synth/lig_dom.
    (IPR000873); ANL_N_sf. (IPR042099); AMP-binding (PF00501)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O60488
- **Protein Description:** RecName: Full=Long-chain-fatty-acid--CoA ligase 4 {ECO:0000305}; EC=6.2.1.3 {ECO:0000269|PubMed:21242590, ECO:0000269|PubMed:22633490, ECO:0000269|PubMed:24269233}; AltName: Full=Arachidonate--CoA ligase {ECO:0000305}; EC=6.2.1.15 {ECO:0000269|PubMed:21242590}; AltName: Full=Long-chain acyl-CoA synthetase 4; Short=LACS 4;
- **Gene Information:** Name=ACSL4; Synonyms=ACS4, FACL4, LACS4;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the ATP-dependent AMP-binding enzyme family.
- **Key Domains:** AMP-bd_C_sf. (IPR045851); AMP-binding_CS. (IPR020845); AMP-dep_synth/lig_dom. (IPR000873); ANL_N_sf. (IPR042099); AMP-binding (PF00501)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ACSL4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ACSL4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ACSL4** (gene ID: ACSL4, UniProt: O60488) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ACSL4 (Long-chain-fatty-acid--CoA ligase 4): A Comprehensive Review

## Introduction

Acyl-CoA Synthetase Long-Chain Family Member 4 (ACSL4), also known as FACL4, ACS4, or LACS4, is an X-linked gene (Xq23) that encodes a member of the long-chain fatty-acid-coenzyme A ligase family [cao-1998-cloning]. The enzyme is classified under two EC numbers reflecting its substrate preferences: EC 6.2.1.3 (long-chain fatty acid-CoA ligase) for general long-chain fatty acid activation, and EC 6.2.1.15 (arachidonate-CoA ligase) specifically recognizing its preferential activity toward arachidonic acid. ACSL4 catalyzes the ATP-dependent formation of fatty acyl-CoA esters from long-chain fatty acids, a fundamental activation step that commits fatty acids to diverse metabolic fates including membrane phospholipid biosynthesis, lipid storage as triglycerides, and energy production through β-oxidation [kuwata-2019-arachidonic-abstract]. What distinguishes ACSL4 from other ACSL family members (ACSL1, ACSL3, ACSL5, and ACSL6) is its marked substrate preference for polyunsaturated fatty acids (PUFAs), particularly arachidonic acid (AA, 20:4) and adrenic acid (AdA, 22:4), rather than saturated or monounsaturated fatty acids [kang-1997-discovery, doll-2017-ferroptosis-abstract].

The discovery of ACSL4 began with Kang et al. (1997), who identified a novel arachidonate-preferring acyl-CoA synthetase (termed Acs4) in steroidogenic tissues of rat adrenal, ovary, and testis [kang-1997-discovery]. Subsequently, Cao et al. (1998) cloned and characterized the human homolog, FACL4, demonstrating its high substrate preference for arachidonic acid and mapping it to chromosome Xq23 [cao-1998-cloning]. The enzyme has since emerged as a critical regulator at the intersection of lipid metabolism, inflammation, steroidogenesis, and most notably, ferroptosis—an iron-dependent form of regulated cell death characterized by lethal accumulation of lipid peroxides [doll-2017-ferroptosis-abstract].

## Enzymatic Function and Substrate Specificity

ACSL4 catalyzes the formation of fatty acyl-CoA thioesters according to the reaction: fatty acid + ATP + CoA → acyl-CoA + AMP + PPi. The human ACSL4 gene contains 18 exons and encodes a 74.4 kDa protein of 670 amino acids. Structurally, the protein belongs to the ATP-dependent AMP-binding enzyme family and contains a characteristic AMP-binding domain (Pfam: PF00501) that forms the catalytic core. The AMP adaptor region consists of two substructures—a nucleotide-binding substructure and a CoA-binding substructure—linked by a cantilever peptide. The enzyme operates through a two-step ping-pong mechanism involving an acyl-adenylate intermediate [yan-2015-mutagenesis-abstract]. The catalytic center contains a conserved acylase kinetic triad of lysine-aspartate-cysteine residues, where lysine and aspartate facilitate protonation and deprotonation during catalysis while cysteine serves as the pivotal site for fatty acid binding to CoA [kuwata-2019-arachidonic-abstract].

Kinetic studies have established ACSL4's remarkable selectivity for polyunsaturated fatty acids. The enzyme exhibits highest activity with arachidonic acid, with Vmax of approximately 7,180 μmol/min/mg and Km of 11.4 μM [yan-2015-mutagenesis-abstract]. While ACSL4 can activate saturated and monounsaturated fatty acids (C14-C26), it demonstrates negligible activity toward these substrates compared to PUFAs containing three or more double bonds [shimbara-matsubayashi-2019-substrate-abstract]. Both ACSL4 splice variants preferentially activate docosahexaenoic acid (DHA), adrenic acid, eicosapentaenoic acid (EPA), and arachidonic acid, with comparable affinities but differing reaction rates between variants [shimbara-matsubayashi-2019-substrate-abstract].

The structural basis for this substrate preference has been elucidated through mutagenesis studies using the bacterial ttLC-FACS crystal structure as a template. These studies identified a "gated fatty acid binding tunnel" model where specific residues control substrate access and selectivity [yan-2015-mutagenesis-abstract]. Critical amino acids include G401 at the entry region (mutation to leucine causes complete inactivation), S291 at the pocket terminus (tyrosine substitution reduces activity toward C20:5 and C22:6 by 17-18%), and Q525 in the selectivity region (lysine substitution decreases arachidonate activation by 48%) [yan-2015-mutagenesis-abstract]. Although no experimental crystal structure of ACSL4 exists, AlphaFold-based three-dimensional modeling has identified Q464 as critical for inhibitor binding, with mutations at this position abolishing interactions with the ferroptosis inhibitor AS-252424 [huang-2024-inhibitor].

## Subcellular Localization and Compartmentalization

ACSL4 exhibits complex subcellular distribution that varies by cell type and splice variant. The enzyme localizes primarily to the endoplasmic reticulum (ER), with additional presence at mitochondria, plasma membrane, and peroxisomes [radif-2018-localization-abstract]. Studies in sarcoma and breast cancer cells demonstrated that ACSL4 distribution closely correlates with ER-resident proteins such as calnexin and HMG-CoA reductase, with only a minor fraction present in isolated mitochondria-associated membrane (MAM) fractions [radif-2018-localization-abstract].

The two major ACSL4 isoforms display distinct localization patterns. Variant 1 (ACSL4_v1), the shorter and more broadly expressed form, localizes to the inner side of the plasma membrane including microvilli and is also present in the cytosol. Variant 2 (ACSL4_v2), which contains an additional 41 N-terminal amino acids encoding a hydrophobic region, localizes to the endoplasmic reticulum and lipid droplets and shows brain-specific expression [radif-2018-localization-abstract]. ACSL4 also contains a peroxisomal targeting signal (PTS1), though subsequent investigations have questioned significant peroxisomal localization.

The enrichment of ACSL4 at ER-mitochondria contact sites (MAMs) has functional significance for fatty acid synthesis and β-oxidation pathways, and ACSL4 has been employed as a marker enzyme for biochemical isolation of MAM fractions. Within distinct organelles, ACSL4 participates in different processes: in mitochondria, it contributes to fatty acid synthesis and β-oxidation; among peroxisomes, it facilitates β-oxidation and alkyl lipid synthesis; in the endoplasmic reticulum, it promotes glycerolipid synthesis.

## The ACSL4-LPCAT3 Pathway in Phospholipid Remodeling

A defining function of ACSL4 is its participation in the Lands cycle of phospholipid remodeling, wherein it acts coordinately with lysophosphatidylcholine acyltransferase 3 (LPCAT3) to shape cellular membrane composition [doll-2017-ferroptosis-abstract]. Free intracellular PUFAs are first converted to their acyl-CoA forms by ACSL4, then esterified into phospholipids by LPCAT3. Specifically, arachidonoyl-CoA and adrenoyl-CoA generated by ACSL4 are incorporated by LPCAT3 into lysophosphatidylethanolamine (LPE) and lysophosphatidylcholine (LPC) to form AA-containing phosphatidylethanolamine (PE) and phosphatidylcholine (PC) [doll-2017-ferroptosis-abstract].

Overexpression of ACSL4 results in higher rates of arachidonoyl-CoA synthesis, increased incorporation of arachidonic acid into phosphatidylethanolamine, phosphatidylinositol, and triacylglycerol, with concomitant reduction in cellular levels of unesterified arachidonate [golej-2011-pge2-abstract]. This channeling of arachidonic acid into membrane phospholipids has important consequences for both membrane biophysical properties and the availability of free arachidonic acid for eicosanoid synthesis.

## Role in Ferroptosis

The discovery of ACSL4 as an essential component of ferroptosis execution represents a landmark in understanding this iron-dependent cell death pathway [doll-2017-ferroptosis-abstract]. In 2017, Doll and colleagues identified ACSL4 through two independent approaches: genome-wide CRISPR-based screening and microarray profiling of ferroptosis-resistant cell lines. They demonstrated that Gpx4-Acsl4 double-knockout cells showed marked resistance to ferroptosis and proliferated normally in culture, whereas no cell type could previously survive without GPX4 function alone [doll-2017-ferroptosis-abstract].

The mechanistic basis for ACSL4's pro-ferroptotic role lies in its enrichment of cellular membranes with long polyunsaturated ω6 fatty acids, particularly arachidonic acid and adrenic acid in phosphatidylethanolamine species. These PUFA-containing phospholipids serve as substrates for lipid peroxidation, which can occur through autoxidation or enzymatic action by 15-lipoxygenase (15-LOX). The resulting lipid hydroperoxides (PE-AA-OOH and PE-AdA-OOH) accumulate to lethal levels when not adequately neutralized by the GPX4/glutathione antioxidant system, ultimately triggering ferroptotic cell death [doll-2017-ferroptosis-abstract].

A critical advancement in understanding ferroptosis regulation came with the identification of a positive feedback loop involving protein kinase C βII (PKCβII) and ACSL4 [zhang-2022-pkcbii-abstract]. Zhang et al. (2022) discovered that PKCβII functions as a sensor of initial lipid peroxides and amplifies lipid peroxidation by phosphorylating ACSL4 at threonine 328 (Thr328). This phosphorylation is critical for ACSL4 dimerization, which represents the active form of the enzyme. The resulting positive feedback mechanism means that even moderate accumulation of lipid peroxides can activate PKCβII, which then enhances ACSL4 activity to amplify PUFA-containing lipid synthesis and further lipid peroxidation to lethal levels [zhang-2022-pkcbii-abstract].

The therapeutic potential of targeting ACSL4 in ferroptosis-related diseases has been demonstrated with thiazolidinedione (TZD) compounds—rosiglitazone, pioglitazone, and troglitazone—which selectively inhibit ACSL4 over other ACSL isoforms and prevent ferroptosis independently of their PPARγ agonist activity [doll-2017-ferroptosis-abstract]. In mouse models, rosiglitazone treatment significantly prolonged survival in ferroptotic acute renal failure.

## Eicosanoid Biosynthesis and Inflammation

ACSL4 plays a paradoxical role in eicosanoid metabolism. By esterifying free arachidonic acid into phospholipids, ACSL4 competes with cyclooxygenase (COX) enzymes for substrate, potentially limiting prostaglandin synthesis. Studies in human arterial smooth muscle cells demonstrated that ACSL4 overexpression reduced prostaglandin E2 (PGE2) secretion by sequestering arachidonic acid into phospholipids, while acute pharmacological inhibition increased PGE2 release [golej-2011-pge2-abstract]. However, sustained ACSL4 downregulation paradoxically suppressed PGE2 production, indicating that ACSL4 also maintains the phospholipid pools from which arachidonic acid is released by phospholipases for eicosanoid synthesis [golej-2011-pge2-abstract].

In macrophages, ACSL4 deficiency causes significant reduction of arachidonic acid incorporation into all phospholipid classes with reciprocal increases in oleic and linoleic acid. Following stimulation, diverse AA-derived lipid mediators including leukotrienes, prostaglandins, HETEs, and lipoxins are markedly reduced in ACSL4-deficient cells [kuwata-2019-arachidonic-abstract]. This dual role—both sequestering arachidonic acid away from COX and maintaining the substrate pools for phospholipase-mediated release—positions ACSL4 as a key modulator of inflammatory lipid mediator production.

Maloberti et al. (2010) demonstrated a functional interaction between ACSL4, lipoxygenases, and cyclooxygenase-2 (COX-2) in breast cancer cells, showing that ACSL4 regulates COX-2 expression and prostaglandin production in MDA-MB-231 cells [maloberti-2010-cox2-abstract]. ACSL4 acts as a rate-limiting enzyme compartmentalizing arachidonic acid release within mitochondria and directing it toward lipoxygenase metabolism while simultaneously controlling COX-2 expression through lipoxygenase metabolites.

## Steroidogenesis and Adrenal Function

ACSL4 is highly expressed in steroidogenic tissues including the adrenal gland, ovary, and testis, where it participates in cholesterol ester formation and steroid hormone biosynthesis [kang-1997-discovery, wang-2019-steroidogenesis-abstract]. Steroidogenic tissues are particularly enriched in cholesteryl esters of long-chain polyunsaturated fatty acids, which constitute an important pool supplying cholesterol for steroid synthesis. ACSL4 facilitates formation of these cholesteryl esters by generating the PUFA-CoA substrates required for esterification.

Tissue-specific ablation of ACSL4 in mice revealed its role in adrenal cholesteryl ester formation and composition [wang-2019-steroidogenesis-abstract]. ACSL4 knockout resulted in reduced cholesteryl ester storage and altered cholesteryl ester fatty acid composition, leading to decreased corticosterone and testosterone production. However, the presence of exogenous HDL normalized steroid production, indicating that ACSL4 is dispensable for normal steroidogenesis per se but essential for maintaining intracellular cholesteryl ester stores [wang-2019-steroidogenesis-abstract].

An alternative arachidonic acid-releasing pathway for steroidogenesis operates through ACSL4 and mitochondrial acyl-CoA thioesterase 2 (ACOT2), rather than the canonical phospholipase A2 pathway. In this mechanism, ACSL4 converts intracellular free arachidonic acid to AA-CoA and delivers it to ACOT2, which releases arachidonic acid within mitochondria to facilitate cholesterol transport and cleavage into pregnenolone by CYP11A1 [kuwata-2019-arachidonic-abstract].

## Disease Associations

### X-Linked Intellectual Disability (XLID63)

ACSL4 was the first gene identified linking non-syndromic X-linked intellectual disability to fatty acid metabolism [meloni-2002-xlid]. Meloni et al. (2002) identified mutations in FACL4 (ACSL4) in families segregating nonsyndromic X-linked mental retardation, including two missense mutations (R529S and P375L) and one splice site mutation that reduce enzymatic activity by 80-88% compared to normal controls [meloni-2002-xlid]. All carrier females with point mutations or genomic deletions showed completely skewed X-inactivation, suggesting cellular selection against ACSL4 deficiency. The Alport syndrome with intellectual disability (ATS-ID) contiguous gene deletion syndrome results from interstitial microdeletion at Xq22.3, affecting both COL4A5 (causing Alport syndrome) and ACSL4 (causing intellectual disability) [meloni-2002-xlid].

The molecular mechanisms underlying ACSL4-related cognitive impairment have been extensively studied using Drosophila as a model organism. The Drosophila ACSL-like protein (dAcsl) is highly homologous to human ACSL4, and human ACSL4 can functionally substitute for dAcsl in organismal viability, lipid storage, and neural wiring [zhang-2009-drosophila-abstract]. Zhang et al. (2009) demonstrated that dAcsl mutants exhibit diminished production of Decapentaplegic (Dpp), a BMP-like morphogen, specifically in the larval brain. This reduction in BMP signaling leads to decreased numbers of glial cells and neurons, with retinal axons misdirecting in the visual cortex. Critically, wild-type human ACSL4 rescued these brain defects, while patient-derived mutant forms exhibited dominant-negative effects when expressed in a wild-type background, causing lesions in the visual center [zhang-2009-drosophila-abstract].

Additional Drosophila studies have revealed that ACSL4 regulates synaptic development through lipid composition control. Huang et al. (2016) showed that Acsl mutations result in decreased abundance of C16:1 fatty acyls and elevated levels of lipid raft components (mannosyl glucosylceramide, phosphoethanolamine ceramide, and ergosterol) in neuromuscular junctions [huang-2016-synaptic-abstract]. These lipid alterations lead to synaptic overgrowth through enhanced BMP signaling, demonstrating that ACSL4's inhibitory role in synapse growth operates through lipid-mediated pathways. Furthermore, Acsl mutants show reduced neuroblast proliferation in the mushroom body—the center of olfactory learning and memory—due to decreased cyclin E expression and nuclear mislocalization of the transcription factor Prospero. In mammalian systems, ACSL4 is highly expressed in the hippocampus, where it is required for dendritic spine formation, providing a plausible cellular basis for cognitive impairment in ACSL4-deficient patients.

### Cancer

ACSL4 exhibits context-dependent roles in cancer, functioning as either tumor promoter or suppressor depending on cancer type and receptor status. In estrogen receptor-negative breast cancer, hepatocellular carcinoma, colorectal cancer, and prostate cancer, high ACSL4 expression promotes tumor cell proliferation, migration, and invasion. Conversely, ACSL4 inhibits progression of lung cancer, estrogen receptor-positive breast cancer, and cervical cancer, and upregulation can enhance sensitivity to ferroptosis [maloberti-2010-cox2-abstract].

In hepatocellular carcinoma (HCC), ACSL4 overexpression correlates with poor prognosis, with reduced overall and disease-free survival in patients with high expression [wang-2020-hcc]. ACSL4 promotes HCC progression via c-Myc stability mediated by the ERK/FBW7/c-Myc axis. ACSL4 can distinguish HCC tissues from normal tissues with 93.8% sensitivity and predicts response to sorafenib treatment.

In breast cancer, ACSL4 expression varies inversely with estrogen receptor alpha (ERα) expression, with highest levels in triple-negative and basal-like subtypes [maloberti-2010-cox2-abstract]. The ZEB2-ACSL4 positive feedback loop regulates lipid metabolism to promote breast cancer metastasis. Combinatory therapies targeting the ACSL4-lipoxygenase-COX-2 system may allow for lower medication doses and reduced side effects [maloberti-2010-cox2-abstract].

### Ischemia-Reperfusion Injury and Metabolic Disease

ACSL4-mediated ferroptosis contributes to tissue damage in ischemia-reperfusion injury affecting brain, heart, kidney, liver, and intestine. ACSL4 Thr328 phosphorylation increases progressively during ischemia-reperfusion and may serve as a ferroptosis biomarker [zhang-2022-pkcbii-abstract]. ACSL4 inhibitors show protective effects when administered prophylactically.

In diabetic kidney disease, ferroptosis mediated through ACSL4 contributes to renal dysfunction, with rosiglitazone ameliorating injury. ACSL4 is upregulated in non-alcoholic fatty liver disease (NAFLD) and non-alcoholic steatohepatitis (NASH), with hypomethylated CpG sites associated with increased disease risk. In atherosclerosis, ACSL4 upregulation correlates with advanced disease and plaque severity.

## Regulatory Mechanisms

ACSL4 expression is controlled at multiple levels. Transcriptionally, key factors include Sp1 (operating under normoxic and hypoxic conditions), CREB (responding to cAMP stimulation), TEAD4/YAP (through Merlin-Hippo pathway activation), and PPARδ (tissue-specific hepatic activation) [kuwata-2019-arachidonic-abstract]. Multiple microRNAs suppress ACSL4 expression including miR-424-5p, miR-141-3p, miR-548p, and miR-211-5p, while miR-347, miR-214-3p, and miR-142-3p promote expression.

Post-translationally, ACSL4 activity is regulated by phosphorylation. The enzyme is a substrate for both PKA and PKC, with phosphorylation occurring after dimer formation [kuwata-2019-arachidonic-abstract]. The PKCβII-mediated phosphorylation at Thr328 represents the most functionally characterized modification, promoting dimerization and activation as part of the ferroptosis amplification loop [zhang-2022-pkcbii-abstract]. SENP1-mediated deSUMOylation protects against ferroptosis under hypoxia.

ACSL4 protein degradation involves multiple pathways: p115 binds and degrades ACSL4 (enhanced by arachidonic acid treatment), while A20 direct interaction suppresses expression. Bidirectional regulation exists between ACSL4 and its substrate arachidonic acid, with AA-mediated ubiquitination contributing to ACSL4 turnover [kuwata-2019-arachidonic-abstract].

## Open Questions

Several important questions remain regarding ACSL4 biology and therapeutic targeting:

1. **Structural biology:** No experimental crystal structure of human ACSL4 exists. High-resolution structural determination would clarify the molecular basis for substrate selectivity and enable rational drug design for selective ACSL4 inhibitors.

2. **Isoform-specific functions:** While the two major ACSL4 variants show distinct subcellular localizations, their specific contributions to different biological processes (ferroptosis, eicosanoid metabolism, steroidogenesis) remain incompletely defined.

3. **Tissue-specific roles:** The balance between ACSL4's pro-ferroptotic and metabolic functions varies by tissue context. Understanding what determines whether ACSL4 promotes or suppresses disease in different settings is critical for therapeutic development.

4. **Metabolic consequences of inhibition:** Long-term consequences of ACSL4 inhibition on lipid metabolism, membrane composition, and cellular function have not been systematically characterized, raising concerns about potential metabolic dysfunction.

5. **Selectivity challenges:** Many available inhibitors (e.g., triacsin C) affect multiple ACSL family members. Developing truly selective ACSL4 inhibitors with favorable pharmacokinetic properties remains an ongoing challenge.

6. **Neurological function:** The precise mechanism by which ACSL4 deficiency causes intellectual disability is not fully understood. Whether this involves ferroptosis, altered membrane phospholipid composition, or other mechanisms requires further investigation.

7. **PKCβII-ACSL4 axis in disease:** The newly identified positive feedback loop between PKCβII and ACSL4 in ferroptosis raises questions about its role in chronic diseases and whether targeting this axis offers advantages over direct ACSL4 inhibition.

## References

* [cao-1998-cloning] Cao Y, Traer E, Zimmerman GA, McIntyre TM, Prescott SM. Cloning, expression, and chromosomal localization of human long-chain fatty acid-CoA ligase 4 (FACL4). *Genomics*. 1998;49(2):327-330. PMID: 9598322

* [doll-2017-ferroptosis-abstract] Doll S, Proneth B, Tyurina YY, Panzilius E, Kobayashi S, Ingold I, Irmler M, Beckers J, Aichler M, Walch A, Prokisch H, Trümbach D, Mao G, Qu F, Bayir H, Füllekrug J, Scheel CH, Wurst W, Schick JA, Kagan VE, Angeli JP, Conrad M. ACSL4 dictates ferroptosis sensitivity by shaping cellular lipid composition. *Nat Chem Biol*. 2017;13(1):91-98. DOI: 10.1038/nchembio.2239. PMID: 27842070. PMCID: PMC5610546

* [golej-2011-pge2-abstract] Golej DL, Askari B, Kramer F, Barnhart S, Vivekanandan-Giri A, Pennathur S, Bornfeldt KE. Long-chain acyl-CoA synthetase 4 modulates prostaglandin E2 release from human arterial smooth muscle cells. *J Lipid Res*. 2011;52(4):782-793. DOI: 10.1194/jlr.M013292. PMCID: PMC3053208

* [huang-2016-synaptic-abstract] Huang Y, Huang S, Lam SM, Liu Z, Shui G, Zhang YQ. Acsl, the Drosophila ortholog of intellectual-disability-related ACSL4, inhibits synaptic growth by altered lipids. *J Cell Sci*. 2016;129(21):4034-4045. DOI: 10.1242/jcs.195032. PMID: 27656110

* [huang-2024-inhibitor] Huang B, et al. Identification of a targeted ACSL4 inhibitor to treat ferroptosis-related diseases. *Sci Adv*. 2024;10:eadk1200. DOI: 10.1126/sciadv.adk1200

* [kang-1997-discovery] Kang MJ, Fujino T, Sasano H, Minekura H, Yabuki N, Nagura H, Iijima H, Yamamoto TT. A novel arachidonate-preferring acyl-CoA synthetase is present in steroidogenic cells of the rat adrenal, ovary, and testis. *Proc Natl Acad Sci USA*. 1997;94(7):2880-2884. PMID: 9096315

* [kuwata-2019-arachidonic-abstract] Kuwata H, Hara S. Role of acyl-CoA synthetase ACSL4 in arachidonic acid metabolism. *Prostaglandins Other Lipid Mediat*. 2019;144:106363. DOI: 10.1016/j.prostaglandins.2019.106363. PMID: 31306767

* [maloberti-2010-cox2-abstract] Maloberti PM, Duarte AB, Orlando UD, Pasqualini ME, Solano AR, López-Otín C, Podestá EJ. Functional Interaction between Acyl-CoA Synthetase 4, Lipooxygenases and Cyclooxygenase-2 in the Aggressive Phenotype of Breast Cancer Cells. *PLoS ONE*. 2010;5(11):e15540. DOI: 10.1371/journal.pone.0015540

* [meloni-2002-xlid] Meloni I, Muscettola M, Raynaud M, Longo I, Bruttini M, Moraine C, Renieri A. FACL4, encoding fatty acid-CoA ligase 4, is mutated in nonspecific X-linked mental retardation. *Nat Genet*. 2002;30(4):436-440. DOI: 10.1038/ng857. PMID: 11889466

* [radif-2018-localization-abstract] Radif Y, Ndiaye H, Kalantzi V, Jacobs R, Hall A, Minogue S, Waugh MG. The endogenous subcellular localisations of the long chain fatty acid-activating enzymes ACSL3 and ACSL4 in sarcoma and breast cancer cells. *Mol Cell Biochem*. 2018;448(1-2):275-286. DOI: 10.1007/s11010-018-3332-x

* [shimbara-matsubayashi-2019-substrate-abstract] Shimbara-Matsubayashi S, Kuwata H, Tanaka N, Kato M, Hara S. Analysis on the Substrate Specificity of Recombinant Human Acyl-CoA Synthetase ACSL4 Variants. *Biol Pharm Bull*. 2019;42(5):850-855. DOI: 10.1248/bpb.b19-00085. PMID: 31061331

* [wang-2019-steroidogenesis-abstract] Wang W, Hao X, Han L, Yan Z, Shen WJ, Dong D, Hasbargen K, Bittner S, Cortez Y, Greenberg AS, Azhar S, Kraemer FB. Tissue-Specific Ablation of ACSL4 Results in Disturbed Steroidogenesis. *Endocrinology*. 2019;160(11):2517-2528. DOI: 10.1210/en.2019-00464. PMID: 31504388. PMCID: PMC6773434

* [wang-2020-hcc] Chen J, Ding C, Chen Y, Hu W, Yu C, Peng C, Feng X, Cheng Q, Wu W, Lu Y, Xie H, Zhou L, Wu J, Zheng S. ACSL4 reprograms fatty acid metabolism in hepatocellular carcinoma via c-Myc/SREBP1 pathway. *Cancer Lett*. 2021;502:154-165. DOI: 10.1016/j.canlet.2020.12.019. PMID: 33359517

* [yan-2015-mutagenesis-abstract] Yan S, Yang XF, Liu HL, Fu N, Ouyang Y, Qing K. Long-chain acyl-CoA synthetase in fatty acid metabolism involved in liver and other diseases: an update. *World J Gastroenterol*. 2015;21(12):3492-3498. PMCID: PMC1828365

* [zhang-2009-drosophila-abstract] Zhang Y, Chen D, Wang Z. Analyses of mental dysfunction-related ACSl4 in Drosophila reveal its requirement for Dpp/BMP production and visual wiring in the brain. *Hum Mol Genet*. 2009;18(20):3894-3905. DOI: 10.1093/hmg/ddp332. PMID: 19617635

* [zhang-2022-pkcbii-abstract] Zhang HL, Hu BX, Li ZL, Du T, Shan JL, Ye ZP, Peng XD, Li X, Huang Y, Zhu XY, Chen YH, Feng GK, Yang D, Deng R, Zhu XF. PKCβII phosphorylates ACSL4 to amplify lipid peroxidation to induce ferroptosis. *Nat Cell Biol*. 2022;24(1):88-98. DOI: 10.1038/s41556-021-00818-3. PMID: 35027735


## Citations

1. doll-2017-ferroptosis-abstract.md
2. golej-2011-pge2-abstract.md
3. huang-2016-synaptic-abstract.md
4. kuwata-2019-arachidonic-abstract.md
5. maloberti-2010-cox2-abstract.md
6. radif-2018-localization-abstract.md
7. shimbara-matsubayashi-2019-substrate-abstract.md
8. wang-2019-steroidogenesis-abstract.md
9. yan-2015-mutagenesis-abstract.md
10. zhang-2009-drosophila-abstract.md
11. zhang-2022-pkcbii-abstract.md