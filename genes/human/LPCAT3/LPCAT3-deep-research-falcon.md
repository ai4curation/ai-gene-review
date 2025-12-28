---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-27T12:55:37.741989'
end_time: '2025-12-27T13:02:13.587818'
duration_seconds: 395.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: LPCAT3
  gene_symbol: LPCAT3
  uniprot_accession: Q6P1A2
  protein_description: 'RecName: Full=Lysophospholipid acyltransferase 5; Short=LPLAT
    5; EC=2.3.1.- {ECO:0000269|PubMed:18195019, ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225};
    AltName: Full=1-acylglycerophosphocholine O-acyltransferase; EC=2.3.1.23 {ECO:0000269|PubMed:18195019,
    ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=1-acylglycerophosphoethanolamine
    O-acyltransferase; EC=2.3.1.n7 {ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225};
    AltName: Full=1-acylglycerophosphoserine O-acyltransferase; EC=2.3.1.n6 {ECO:0000269|PubMed:18195019,
    ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=Lysophosphatidylcholine
    acyltransferase; Short=LPCAT; Short=Lyso-PC acyltransferase; AltName: Full=Lysophosphatidylcholine
    acyltransferase 3; Short=Lyso-PC acyltransferase 3; AltName: Full=Lysophosphatidylserine
    acyltransferase; Short=LPSAT; Short=Lyso-PS acyltransferase; AltName: Full=Membrane-bound
    O-acyltransferase domain-containing protein 5; Short=O-acyltransferase domain-containing
    protein 5;'
  gene_info: Name=LPCAT3; Synonyms=MBOAT5, OACT5;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the membrane-bound acyltransferase family.
  protein_domains: LPLAT_7/PORCN-like. (IPR049941); MBOAT_fam. (IPR004299); MBOAT
    (PF03062)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6P1A2
- **Protein Description:** RecName: Full=Lysophospholipid acyltransferase 5; Short=LPLAT 5; EC=2.3.1.- {ECO:0000269|PubMed:18195019, ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=1-acylglycerophosphocholine O-acyltransferase; EC=2.3.1.23 {ECO:0000269|PubMed:18195019, ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=1-acylglycerophosphoethanolamine O-acyltransferase; EC=2.3.1.n7 {ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=1-acylglycerophosphoserine O-acyltransferase; EC=2.3.1.n6 {ECO:0000269|PubMed:18195019, ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=Lysophosphatidylcholine acyltransferase; Short=LPCAT; Short=Lyso-PC acyltransferase; AltName: Full=Lysophosphatidylcholine acyltransferase 3; Short=Lyso-PC acyltransferase 3; AltName: Full=Lysophosphatidylserine acyltransferase; Short=LPSAT; Short=Lyso-PS acyltransferase; AltName: Full=Membrane-bound O-acyltransferase domain-containing protein 5; Short=O-acyltransferase domain-containing protein 5;
- **Gene Information:** Name=LPCAT3; Synonyms=MBOAT5, OACT5;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the membrane-bound acyltransferase family.
- **Key Domains:** LPLAT_7/PORCN-like. (IPR049941); MBOAT_fam. (IPR004299); MBOAT (PF03062)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LPCAT3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LPCAT3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LPCAT3** (gene ID: LPCAT3, UniProt: Q6P1A2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6P1A2
- **Protein Description:** RecName: Full=Lysophospholipid acyltransferase 5; Short=LPLAT 5; EC=2.3.1.- {ECO:0000269|PubMed:18195019, ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=1-acylglycerophosphocholine O-acyltransferase; EC=2.3.1.23 {ECO:0000269|PubMed:18195019, ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=1-acylglycerophosphoethanolamine O-acyltransferase; EC=2.3.1.n7 {ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=1-acylglycerophosphoserine O-acyltransferase; EC=2.3.1.n6 {ECO:0000269|PubMed:18195019, ECO:0000269|PubMed:18772128, ECO:0000269|PubMed:18782225}; AltName: Full=Lysophosphatidylcholine acyltransferase; Short=LPCAT; Short=Lyso-PC acyltransferase; AltName: Full=Lysophosphatidylcholine acyltransferase 3; Short=Lyso-PC acyltransferase 3; AltName: Full=Lysophosphatidylserine acyltransferase; Short=LPSAT; Short=Lyso-PS acyltransferase; AltName: Full=Membrane-bound O-acyltransferase domain-containing protein 5; Short=O-acyltransferase domain-containing protein 5;
- **Gene Information:** Name=LPCAT3; Synonyms=MBOAT5, OACT5;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the membrane-bound acyltransferase family.
- **Key Domains:** LPLAT_7/PORCN-like. (IPR049941); MBOAT_fam. (IPR004299); MBOAT (PF03062)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LPCAT3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LPCAT3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LPCAT3** (gene ID: LPCAT3, UniProt: Q6P1A2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

Plan and verification
- Identity verified: human LPCAT3 (gene LPCAT3; aliases MBOAT5/OACT5/LPLAT12; UniProt Q6P1A2) is a membrane-bound O-acyltransferase (MBOAT) lysophospholipid acyltransferase that remodels phospholipids in the Lands cycle. It is ER-localized and preferentially incorporates polyunsaturated acyl chains (e.g., arachidonoyl) into the sn-2 position of lysophospholipids, especially lysophosphatidylcholine (LPC). Structural, biochemical, and physiological data align with MBOAT domain features (conserved catalytic His) and the LPLAT family. No symbol ambiguity was encountered (pierce2023arisingtide pages 8-11, zhang2021thestructuralbasis pages 1-2, wang2024researchprogresschallenges pages 4-5).

1) Key concepts and definitions (current understanding)
- Enzymatic function. LPCAT3 catalyzes acyl-CoA-dependent re-acylation of lysophospholipids, primarily LPC, producing phosphatidylcholine (PC) enriched for polyunsaturated fatty acids (PUFAs). Headgroup scope includes LPC as the primary acceptor with reported activity toward LPE and LPS at lower levels; little or no activity for lysoPI/lysoPG is reported in comparative studies of human LPCATs (review synthesis) (korbecki2024phospholipidacyltransferasescharacterization pages 9-10). The acyl donor is typically PUFA-CoA (e.g., arachidonoyl-CoA 20:4-CoA), consistent with in vivo and structural observations of PUFA selectivity (rong2017erphospholipidcomposition pages 6-8, zhang2021thestructuralbasis pages 1-2).
- Structural family features. LPCAT3 is an ER-integral MBOAT enzyme with a central membrane-embedded reaction chamber. High-resolution structures reveal two substrate entry tunnels—one for LPC and one for acyl-CoA—that meet at a catalytic center featuring a conserved histidine, with a side pocket that accommodates the bent PUFA acyl chain, providing a structural basis for PUFA preference (Nature Communications, 2021-11-22; https://doi.org/10.1038/s41467-021-27244-1) (zhang2021thestructuralbasis pages 1-2). Reviews of MBOATs confirm conserved His/Asn motifs and a multi-pass architecture in LPCAT3 (Frontiers in Physiology, 2023-05-30; https://doi.org/10.3389/fphys.2023.1167873) (pierce2023arisingtide pages 8-11).
- Cellular localization and tissue expression. LPCAT3 is predominantly localized to the endoplasmic reticulum; it is highly expressed in liver and small intestine and present in adipose tissue, skeletal muscle, and macrophages, where it controls the PUFA content of membrane PCs (wang2024researchprogresschallenges pages 4-5, rong2017erphospholipidcomposition pages 6-8). Emerging evidence indicates LPCAT3 can also localize to lipid droplets under specific conditions, influencing droplet fusion dynamics (Nature Communications, 2025; human LPCAT3 localization to LDs in cell models) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).
- Pathway context. LPCAT3 operates in the Lands cycle, remodeling sn-2 acyl chains of PCs and other phospholipids, thereby tuning membrane biophysical properties and signaling lipid pools. In hepatocytes, LPCAT3-driven ER PUFA-PC influences SREBP-1c activation and lipogenesis; in enterocytes, LPCAT3 supports chylomicron assembly by resynthesizing PC for lipoprotein surfaces (rong2017erphospholipidcomposition pages 6-8, wang2024researchprogresschallenges pages 4-5, korbecki2024phospholipidacyltransferasescharacterization pages 27-29).

2) Recent developments and latest research (2023–2024 priority)
- Structural and mechanistic clarity. The 2021 structural work continues to underpin 2023–2024 reviews, highlighting the T-shaped reaction chamber, conserved catalytic His, and PUFA-accommodating side pocket that mechanistically explains LPCAT3’s arachidonoyl-CoA preference (2023 review; https://doi.org/10.3389/fphys.2023.1167873) (pierce2023arisingtide pages 8-11, zhang2021thestructuralbasis pages 1-2).
- Transcriptional regulation and ER remodeling. A 2024 review synthesizes that LPCAT3 is an LXR target in liver and intestine; its induction increases PUFA-PC, modifies ER membrane properties, and connects sterol/lipid signaling to VLDL production and SREBP-1c lipogenesis (Int J Mol Med, 2024-02; https://doi.org/10.3892/ijmm.2024.5356) (wang2024researchprogresschallenges pages 4-5, wang2024researchprogresschallenges pages 7-9). Complementary mechanistic mouse data show hepatocyte LPCAT3 loss reduces PUFA-PC and blunts feeding/insulin-induced SREBP-1c activation (J Clin Invest, 2017-08-31; https://doi.org/10.1172/jci93616) (rong2017erphospholipidcomposition pages 6-8).
- NASH and mitochondrial homeostasis. A 2024 Hepatology study demonstrated that hepatic Lpcat3 deletion promotes ROS, reduces mtDNA and respiratory complexes, and worsens NASH and fibrosis, with altered inner mitochondrial membrane phospholipid saturation; hepatic overexpression of Lpcat3 ameliorated NASH features (Hepatology, 2024-04; https://doi.org/10.1097/hep.0000000000000375) (tian2024membranephospholipidremodeling pages 7-11).
- Ferroptosis axis and interactors. Reviews in 2023–2024 consolidated the ACSL4–LPCAT3–ALOX15 axis: ACSL4 activates AA/AdA to acyl-CoAs, LPCAT3 installs PUFA into PE/PC (e.g., AA-PE), and ALOX enzymes oxidize these to drive ferroptosis; loss of ACSL4 or LPCAT3 confers ferroptosis resistance (Signal Transduct Target Ther, 2023-09-14; https://doi.org/10.1038/s41392-023-01606-1; Antioxidants, 2024-02-21; https://doi.org/10.3390/antiox13030298) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29). A 2024 Protein & Cell study identified CEPT1 as an ER protein that interacts with LPCAT3, regulates LPCAT3 protein stability, and suppresses ferroptosis, adding a new node regulating LPCAT3-linked lipid death pathways (Protein & Cell, 2024-03; https://doi.org/10.1093/procel/pwae004) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).
- Intestinal lipid absorption. A 2023 review of dietary TG absorption summarized that intestine-specific Lpcat3 deficiency in mice causes enterocyte lipid accumulation and markedly reduced lipid absorption/chylomicron secretion, supporting LPCAT3’s role in enterocytic PC remodeling for lipoprotein biogenesis (Front Pharmacol, 2023-02-16; https://doi.org/10.3389/fphar.2023.1097835) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29). Human tracer studies show enterocytic PC remodeling from dietary PC involves lyso-PC re-acylation consistent with LPCAT3 activity before chylomicron export (Eur J Nutr, 2023-02; https://doi.org/10.1007/s00394-023-03121-z) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).

3) Current applications and real-world implementations
- Targeting metabolic liver disease. The 2024 NASH study suggests that restoring LPCAT3 levels/activity may improve mitochondrial homeostasis and reduce inflammation/fibrosis, positioning LPCAT3 modulation as a potential therapeutic strategy under investigation (Hepatology, 2024-04; https://doi.org/10.1097/hep.0000000000000375) (tian2024membranephospholipidremodeling pages 7-11). Reviews also propose modulating LXR–LPCAT3 to adjust ER phospholipid composition and lipogenesis in NAFLD (Int J Mol Med, 2024-02; https://doi.org/10.3892/ijmm.2024.5356) (wang2024researchprogresschallenges pages 4-5, wang2024researchprogresschallenges pages 7-9).
- Ferroptosis modulation. Because LPCAT3 contributes to PUFA-PL pools required for ferroptosis, selective inhibition of LPCAT3 or upstream ACSL4 is being explored preclinically to suppress ferroptosis in disease, while enhancing this axis is being studied to sensitize cancer cells; protein interactions (CEPT1) offer additional leverage points (Signal Transduct Target Ther, 2023-09-14; https://doi.org/10.1038/s41392-023-01606-1; Protein & Cell, 2024-03; https://doi.org/10.1093/procel/pwae004) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).
- Cardiometabolic lipid handling. In liver, modulating LPCAT3 affects VLDL production via ER PC composition and SREBP activation; in intestine, LPCAT3 influences chylomicron output and dietary fat absorption. These principles are informing strategies to manage plasma TG/VLDL and intestinal lipid malabsorption syndromes (J Clin Invest, 2017-08-31; https://doi.org/10.1172/jci93616; Front Pharmacol, 2023-02-16; https://doi.org/10.3389/fphar.2023.1097835) (rong2017erphospholipidcomposition pages 6-8, korbecki2024phospholipidacyltransferasescharacterization pages 27-29).

4) Expert opinions and analysis from authoritative sources
- Structural biology consensus. The Nature Communications 2021 structure provides a unifying mechanistic framework for LPCAT3’s PUFA selectivity and catalytic chemistry (https://doi.org/10.1038/s41467-021-27244-1) (zhang2021thestructuralbasis pages 1-2). The 2023 MBOAT-focused review integrates LPCAT3 into the broader MBOAT mechanistic canon, emphasizing the conserved His/Asn catalytic architecture and substrate tunnels (https://doi.org/10.3389/fphys.2023.1167873) (pierce2023arisingtide pages 8-11).
- Metabolic physiology perspective. JCI 2017 and the 2024 IJMM review by multiple groups place LPCAT3 as a determinant of ER membrane composition that tunes SREBP-1c signaling and VLDL secretion, aligning lipid remodeling with nutrient/hormone responses (https://doi.org/10.1172/jci93616; https://doi.org/10.3892/ijmm.2024.5356) (rong2017erphospholipidcomposition pages 6-8, wang2024researchprogresschallenges pages 4-5, wang2024researchprogresschallenges pages 7-9).
- Disease pathogenesis viewpoint. Hepatology 2024 highlights how membrane PUFA-PC deficits from Lpcat3 loss impair mitochondrial integrity and exacerbate NASH, providing a causal link from phospholipid remodeling to organelle dysfunction and inflammation (https://doi.org/10.1097/hep.0000000000000375) (tian2024membranephospholipidremodeling pages 7-11).

5) Relevant statistics and data from recent studies
- Structural binding/catalysis. Substrate-bound LPCAT3 structures directly visualize arachidonoyl-CoA engaging a side pocket and aligning to the catalytic His; the geometry supports specificity for kinked PUFA chains (Nature Communications, 2021-11-22) (zhang2021thestructuralbasis pages 1-2).
- Hepatic ER lipidomics and SREBP-1c control. In mouse liver, hepatocyte Lpcat3 deletion reduces multiple PUFA-PC species; feeding- and insulin-induced SREBP-1c maturation and Fasn induction are significantly blunted (n≈6 per group; multiple independent experiments) (J Clin Invest, 2017-08-31) (rong2017erphospholipidcomposition pages 6-8).
- NASH progression metrics. Liver-specific Lpcat3 knockout shows: increased lipid peroxidation markers; decreased mtDNA content; reduced respiratory complexes I, II, IV; increased JNK signaling; worsened histologic inflammation/fibrosis; rescue by Lpcat3 overexpression (Hepatology, 2024-04) (tian2024membranephospholipidremodeling pages 7-11).
- Intestinal absorption/chylomicron assembly. Enterocyte Lpcat3 deficiency yields intestinal lipid accumulation and markedly reduced lipid absorption and chylomicron secretion in mice (Front Pharmacol, 2023-02-16) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29). Human deuterated-PC tracer studies demonstrate lyso-PC re-acylation consistent with enterocytic LPCAT3 during chylomicron PC assembly (Eur J Nutr, 2023-02) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).
- Ferroptosis sensitivity. Reviews synthesize that ACSL4/LPCAT3-dependent AA-PE generation is necessary for ALOX-mediated lipid peroxidation; loss of ACSL4 or LPCAT3 confers resistance in multiple systems, while ER protein CEPT1 interacts with LPCAT3 and modulates stability and ferroptosis responses (2023–2024) (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).

Mechanistic detail: enzyme specificity and catalytic chemistry
- Substrate headgroup specificity. Human LPCAT3 shows the highest activity with LPC; several biochemical studies and reviews report lower but present activity with LPE/LPS, and negligible activity with lysoPI/lysoPG. In vivo functional emphasis remains on PC remodeling (korbecki2024phospholipidacyltransferasescharacterization pages 9-10).
- Acyl donor preference. Structural capture of arachidonoyl-CoA in the LPCAT3 catalytic chamber, together with liver ER lipidomics, supports a functional preference for PUFA acyl-CoAs (18:2, 20:4), enriching sn-2 PUFA in membrane PCs (zhang2021thestructuralbasis pages 1-2, rong2017erphospholipidcomposition pages 6-8, wang2024researchprogresschallenges pages 4-5).
- Catalytic residues and tunnels. The conserved catalytic histidine sits where the acyl donor and acceptor tunnels meet; a side pocket accommodates the unsaturated chain bend of arachidonate, rationalizing PUFA selectivity (zhang2021thestructuralbasis pages 1-2, pierce2023arisingtide pages 8-11).

Localization and regulation
- ER and LD association. LPCAT3 is ER-resident; experimental data show co-localization at ER and, in model systems, recruitment to lipid droplets where it can influence droplet fusion and size, suggesting context-dependent localization (korbecki2024phospholipidacyltransferasescharacterization pages 27-29, wang2024researchprogresschallenges pages 4-5).
- Transcriptional control. LPCAT3 is directly induced by liver X receptor (LXR) signaling and integrates with SREBP-1c lipogenesis; hepatic Lpcat3 expression is increased in obesity and feeding states and decreased when SCAP/SREBP is suppressed (rong2017erphospholipidcomposition pages 6-8, wang2024researchprogresschallenges pages 4-5, wang2024researchprogresschallenges pages 7-9).

Physiology and disease links
- Intestine. LPCAT3 drives enterocytic PC remodeling necessary for chylomicron assembly; deficiency reduces dietary lipid absorption and plasma lipids due to impaired chylomicron secretion (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).
- Liver. LPCAT3 shapes ER PC composition controlling SREBP-1c and VLDL secretion; deficiency reduces PUFA-PC, blunts lipogenic signaling, and worsens NASH via mitochondrial impairment (rong2017erphospholipidcomposition pages 6-8, tian2024membranephospholipidremodeling pages 7-11).
- Ferroptosis. The ACSL4–LPCAT3–ALOX15 module generates PUFA-PE/PC substrates for peroxidation; genetic or pharmacologic attenuation of ACSL4/LPCAT3 reduces susceptibility, while CEPT1–LPCAT3 interaction adds regulatory complexity (korbecki2024phospholipidacyltransferasescharacterization pages 27-29).

Limitations and open questions
- Human clinical genetics and trials directly targeting LPCAT3 are still limited; most detailed mechanistic data derive from mouse models, structural biology, and cell systems. Nonetheless, human-relevant enterocyte remodeling and disease correlations are accumulating (korbecki2024phospholipidacyltransferasescharacterization pages 27-29, tian2024membranephospholipidremodeling pages 7-11, wang2024researchprogresschallenges pages 4-5).

Key recent sources summary
| Year | Study (first author, journal) | Focus / Claim | Key evidence / stat (citation) | URL |
|---|---|---|---|---|
| 2021 | Zhang et al., Nature Communications | LPCAT3 structure and catalytic mechanism; arachidonoyl-CoA donor; T-shaped reaction chamber | Cryo-EM / X-ray structures (apo, donor- and acceptor-bound); central cavity and conserved catalytic His aligning with arachidonoyl-CoA (structural basis for PUFA preference) (zhang2021thestructuralbasis pages 1-2) | https://doi.org/10.1038/s41467-021-27244-1 |
| 2023 | Pierce & Hougland, Frontiers in Physiology | MBOAT family overview; conserved MBOAT motifs and catalytic His/Asn residues | Comparative MBOAT structural review noting LPCAT3 has 11 TM helices, conserved His/Asn catalytic residues and side pocket accommodating PUFA chains (pierce2023arisingtide pages 8-11) | https://doi.org/10.3389/fphys.2023.1167873 |
| 2017 | Rong et al., Journal of Clinical Investigation | ER phospholipid remodeling by LPCAT3 regulates SREBP-1c–dependent lipogenesis | Hepatocyte-specific Lpcat3 KO blunted feeding-induced SREBP-1c maturation and Fasn induction; ER lipidomics showed loss of many PUFA-PC species (n≈6/group in refed studies) (rong2017erphospholipidcomposition pages 6-8) | https://doi.org/10.1172/jci93616 |
| 2024 | Wang et al., Int J Mol Med (review) | LXR→LPCAT3 regulatory axis; LPCAT3 role in NAFLD and tissue expression | Review: LPCAT3 is ER-localized, highly expressed in liver/intestine/adipose, accounts for >90% hepatic LPC acyltransferase activity; LXR agonists induce LPCAT3 and PUFA-PC levels, linking to VLDL/TG handling (wang2024researchprogresschallenges pages 4-5) | https://doi.org/10.3892/ijmm.2024.5356 |
| 2024 | Tian et al., Hepatology | Lpcat3 deficiency exacerbates NASH via mitochondrial dysfunction | Liver-specific Lpcat3 KO: ↑lipid peroxidation, ↓mtDNA, reduced respiratory complexes I/II/IV, altered inner mitochondrial membrane PL saturation; worsened inflammation/fibrosis in diet models (tian2024membranephospholipidremodeling pages 7-11) | https://doi.org/10.1097/hep.0000000000000375 |
| 2024 | Liu et al., Protein & Cell | CEPT1 interacts with LPCAT3 and modulates ferroptosis | Proteomics and co-localization: CEPT1 binds LPCAT3 at ER, regulates LPCAT3 protein stability; CEPT1 activity suppresses ferroptosis possibly via breaking pro-ferroptotic PUFA-PLs (korbecki2024phospholipidacyltransferasescharacterization pages 27-29) | https://doi.org/10.1093/procel/pwae004 |
| 2023 | Sun et al., Signal Transduct Target Ther. / Punziano et al., Antioxidants (reviews) | ACSL4–LPCAT3–ALOX15 axis generates PUFA‑PL substrates for ferroptosis | Reviews summary: ACSL4 activates AA/AdA→acyl‑CoA; LPCAT3 esterifies PUFA‑CoAs into PUFA‑PE/PC (e.g., AA‑PE) that ALOX enzymes oxidize to drive ferroptosis; loss of ACSL4 or LPCAT3 reduces ferroptosis sensitivity (korbecki2024phospholipidacyltransferasescharacterization pages 27-29) | https://doi.org/10.1038/s41392-023-01606-1 , https://doi.org/10.3390/antiox13030298 |
| 2023 | Li et al., Frontiers in Pharmacology | Intestine-specific Lpcat3 deficiency impairs dietary lipid absorption and chylomicron assembly | Intestine-specific Lpcat3 KO mice: enterocyte lipid accumulation and markedly reduced lipid absorption / chylomicron secretion, implicating LPCAT3 in enterocyte PC remodeling for lipoprotein biogenesis (korbecki2024phospholipidacyltransferasescharacterization pages 27-29) | https://doi.org/10.3389/fphar.2023.1097835 |
| 2023 | Böckmann et al., European Journal of Nutrition | Dietary phosphatidylcholine remodeling in enterocytes involves LPCAT3 | Deuterated-PC feeding in humans shows enterocytic remodeling of PC (cleavage to lyso‑PC and re-acylation), implicating enterocytic LPCAT3 in producing PC species for chylomicron assembly (korbecki2024phospholipidacyltransferasescharacterization pages 27-29) | https://doi.org/10.1007/s00394-023-03121-z |


*Table: Compact summary table of key (2021–2024) primary and review sources on human LPCAT3 covering structure, enzymology, regulation, roles in lipid handling and ferroptosis; citations link to the context IDs used.*

References (with URLs and dates)
- Zhang Q et al. The structural basis for the phospholipid remodeling by LPCAT3. Nature Communications. 2021-11-22. https://doi.org/10.1038/s41467-021-27244-1 (zhang2021thestructuralbasis pages 1-2)
- Pierce MR, Hougland JL. A rising tide lifts all MBOATs. Frontiers in Physiology. 2023-05-30. https://doi.org/10.3389/fphys.2023.1167873 (pierce2023arisingtide pages 8-11)
- Rong X et al. ER phospholipid composition modulates lipogenesis. J Clin Invest. 2017-08-31. https://doi.org/10.1172/jci93616 (rong2017erphospholipidcomposition pages 6-8)
- Wang J et al. LXR–LPCAT3 pathway and NAFLD. Int J Mol Med. 2024-02. https://doi.org/10.3892/ijmm.2024.5356 (wang2024researchprogresschallenges pages 4-5, wang2024researchprogresschallenges pages 7-9)
- Tian Y et al. Membrane phospholipid remodeling modulates NASH. Hepatology. 2024-04. https://doi.org/10.1097/hep.0000000000000375 (tian2024membranephospholipidremodeling pages 7-11)
- Liu X et al. CEPT1 interacts with LPCAT3 to suppress ferroptosis. Protein & Cell. 2024-03. https://doi.org/10.1093/procel/pwae004 (korbecki2024phospholipidacyltransferasescharacterization pages 27-29)
- Sun S et al. Targeting ferroptosis for therapeutics. Signal Transduct Target Ther. 2023-09-14. https://doi.org/10.1038/s41392-023-01606-1 (korbecki2024phospholipidacyltransferasescharacterization pages 27-29)
- Punziano C et al. Antioxidant systems modulate ferroptosis. Antioxidants. 2024-02-21. https://doi.org/10.3390/antiox13030298 (korbecki2024phospholipidacyltransferasescharacterization pages 27-29)
- Li X et al. Dietary TG absorption in obesity. Front Pharmacol. 2023-02-16. https://doi.org/10.3389/fphar.2023.1097835 (korbecki2024phospholipidacyltransferasescharacterization pages 27-29)
- Böckmann KA et al. Choline supplement metabolism; enterocyte PC remodeling. Eur J Nutr. 2023-02. https://doi.org/10.1007/s00394-023-03121-z (korbecki2024phospholipidacyltransferasescharacterization pages 27-29)
- Korbecki J et al. Phospholipid acyltransferases in disease (overview of LPCAT3 scope). Cancers. 2024-05. https://doi.org/10.3390/cancers16112115 (korbecki2024phospholipidacyltransferasescharacterization pages 9-10, korbecki2024phospholipidacyltransferasescharacterization pages 27-29)

References

1. (pierce2023arisingtide pages 8-11): Mariah R. Pierce and James L. Hougland. A rising tide lifts all mboats: recent progress in structural and functional understanding of membrane bound o-acyltransferases. Frontiers in Physiology, May 2023. URL: https://doi.org/10.3389/fphys.2023.1167873, doi:10.3389/fphys.2023.1167873. This article has 20 citations and is from a poor quality or predatory journal.

2. (zhang2021thestructuralbasis pages 1-2): Qing Zhang, Deqiang Yao, Bing Rao, Liyan Jian, Yang Chen, Kexin Hu, Ying Xia, Shaobai Li, Yafeng Shen, An Qin, Jie Zhao, Lu Zhou, Ming Lei, Xian-Cheng Jiang, and Yu Cao. The structural basis for the phospholipid remodeling by lysophosphatidylcholine acyltransferase 3. Nature Communications, Nov 2021. URL: https://doi.org/10.1038/s41467-021-27244-1, doi:10.1038/s41467-021-27244-1. This article has 90 citations and is from a highest quality peer-reviewed journal.

3. (wang2024researchprogresschallenges pages 4-5): Junmin Wang, Jiacheng Li, Yu-Hang Fu, Yingying Zhu, Liubing Lin, and Yong Li. Research progress, challenges and perspectives of phospholipids metabolism in the lxr-lpcat3 signaling pathway and its relation to nafld (review). International Journal of Molecular Medicine, Feb 2024. URL: https://doi.org/10.3892/ijmm.2024.5356, doi:10.3892/ijmm.2024.5356. This article has 11 citations and is from a peer-reviewed journal.

4. (korbecki2024phospholipidacyltransferasescharacterization pages 9-10): Jan Korbecki, Mateusz Bosiacki, Maciej Pilarczyk, Magdalena Gąssowska-Dobrowolska, Paweł Jarmużek, Izabela Szućko-Kociuba, Justyna Kulik-Sajewicz, Dariusz Chlubek, and Irena Baranowska-Bosiacka. Phospholipid acyltransferases: characterization and involvement of the enzymes in metabolic and cancer diseases. Cancers, 16:2115, May 2024. URL: https://doi.org/10.3390/cancers16112115, doi:10.3390/cancers16112115. This article has 7 citations and is from a poor quality or predatory journal.

5. (rong2017erphospholipidcomposition pages 6-8): Xin Rong, Bo Wang, Elisa N.D. Palladino, Thomas Q. de Aguiar Vallim, David A. Ford, and Peter Tontonoz. Er phospholipid composition modulates lipogenesis during feeding and in obesity. The Journal of clinical investigation, 127 10:3640-3651, Aug 2017. URL: https://doi.org/10.1172/jci93616, doi:10.1172/jci93616. This article has 95 citations.

6. (korbecki2024phospholipidacyltransferasescharacterization pages 27-29): Jan Korbecki, Mateusz Bosiacki, Maciej Pilarczyk, Magdalena Gąssowska-Dobrowolska, Paweł Jarmużek, Izabela Szućko-Kociuba, Justyna Kulik-Sajewicz, Dariusz Chlubek, and Irena Baranowska-Bosiacka. Phospholipid acyltransferases: characterization and involvement of the enzymes in metabolic and cancer diseases. Cancers, 16:2115, May 2024. URL: https://doi.org/10.3390/cancers16112115, doi:10.3390/cancers16112115. This article has 7 citations and is from a poor quality or predatory journal.

7. (wang2024researchprogresschallenges pages 7-9): Junmin Wang, Jiacheng Li, Yu-Hang Fu, Yingying Zhu, Liubing Lin, and Yong Li. Research progress, challenges and perspectives of phospholipids metabolism in the lxr-lpcat3 signaling pathway and its relation to nafld (review). International Journal of Molecular Medicine, Feb 2024. URL: https://doi.org/10.3892/ijmm.2024.5356, doi:10.3892/ijmm.2024.5356. This article has 11 citations and is from a peer-reviewed journal.

8. (tian2024membranephospholipidremodeling pages 7-11): Ye Tian, Matthew J. Jellinek, Kritika Mehta, Sun Mi Seok, Shanny H. Kuo, Wei Lu, Ruicheng Shi, Richard Lee, Gee W. Lau, Jongsook Kim Kemper, Kai Zhang, David A. Ford, and Bo Wang. Membrane phospholipid remodeling modulates nonalcoholic steatohepatitis progression by regulating mitochondrial homeostasis. Hepatology, 79:882-897, Apr 2024. URL: https://doi.org/10.1097/hep.0000000000000375, doi:10.1097/hep.0000000000000375. This article has 33 citations and is from a highest quality peer-reviewed journal.

## Citations

1. korbecki2024phospholipidacyltransferasescharacterization pages 9-10
2. zhang2021thestructuralbasis pages 1-2
3. pierce2023arisingtide pages 8-11
4. korbecki2024phospholipidacyltransferasescharacterization pages 27-29
5. rong2017erphospholipidcomposition pages 6-8
6. tian2024membranephospholipidremodeling pages 7-11
7. wang2024researchprogresschallenges pages 4-5
8. wang2024researchprogresschallenges pages 7-9
9. https://doi.org/10.1038/s41467-021-27244-1
10. https://doi.org/10.3389/fphys.2023.1167873
11. https://doi.org/10.3892/ijmm.2024.5356
12. https://doi.org/10.1172/jci93616
13. https://doi.org/10.1097/hep.0000000000000375
14. https://doi.org/10.1038/s41392-023-01606-1;
15. https://doi.org/10.3390/antiox13030298
16. https://doi.org/10.1093/procel/pwae004
17. https://doi.org/10.3389/fphar.2023.1097835
18. https://doi.org/10.1007/s00394-023-03121-z
19. https://doi.org/10.1172/jci93616;
20. https://doi.org/10.1038/s41392-023-01606-1
21. https://doi.org/10.3390/cancers16112115
22. https://doi.org/10.3389/fphys.2023.1167873,
23. https://doi.org/10.1038/s41467-021-27244-1,
24. https://doi.org/10.3892/ijmm.2024.5356,
25. https://doi.org/10.3390/cancers16112115,
26. https://doi.org/10.1172/jci93616,
27. https://doi.org/10.1097/hep.0000000000000375,