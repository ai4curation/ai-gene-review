---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:49:29.242441'
end_time: '2026-09-30T06:06:41.483895'
duration_seconds: 1032.24
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: CUT1
  gene_symbol: CUT1
  uniprot_accession: Q9XF43
  protein_description: 'RecName: Full=3-ketoacyl-CoA synthase 6 {ECO:0000303|PubMed:18465198};
    Short=KCS-6 {ECO:0000303|PubMed:18465198}; EC=2.3.1.199 {ECO:0000269|PubMed:10330468};
    AltName: Full=Cuticular protein 1 {ECO:0000303|PubMed:10330468}; AltName: Full=Eceriferum
    6 {ECO:0000303|PubMed:11041893}; AltName: Full=Very long-chain fatty acid condensing
    enzyme 6 {ECO:0000303|PubMed:18465198}; Short=VLCFA condensing enzyme 6 {ECO:0000303|PubMed:18465198};'
  gene_info: Name=CUT1 {ECO:0000303|PubMed:10330468}; Synonyms=CER6 {ECO:0000303|PubMed:11041893},
    EL6, KCS6 {ECO:0000303|PubMed:18465198}; OrderedLocusNames=At1g68530 {ECO:0000312|Araport:AT1G68530};
    ORFNames=T26J14.10 {ECO:0000312|EMBL:AAG52390.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the thiolase-like superfamily. Chalcone/stilbene
  protein_domains: 3-ktacl-CoA_syn. (IPR012392); ACP_syn_III_C. (IPR013747); FAE1_typ3_polyketide_synth.
    (IPR013601); Thiolase-like. (IPR016039); ACP_syn_III_C (PF08541)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: CUT1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: CUT1-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9XF43
- **Protein Description:** RecName: Full=3-ketoacyl-CoA synthase 6 {ECO:0000303|PubMed:18465198}; Short=KCS-6 {ECO:0000303|PubMed:18465198}; EC=2.3.1.199 {ECO:0000269|PubMed:10330468}; AltName: Full=Cuticular protein 1 {ECO:0000303|PubMed:10330468}; AltName: Full=Eceriferum 6 {ECO:0000303|PubMed:11041893}; AltName: Full=Very long-chain fatty acid condensing enzyme 6 {ECO:0000303|PubMed:18465198}; Short=VLCFA condensing enzyme 6 {ECO:0000303|PubMed:18465198};
- **Gene Information:** Name=CUT1 {ECO:0000303|PubMed:10330468}; Synonyms=CER6 {ECO:0000303|PubMed:11041893}, EL6, KCS6 {ECO:0000303|PubMed:18465198}; OrderedLocusNames=At1g68530 {ECO:0000312|Araport:AT1G68530}; ORFNames=T26J14.10 {ECO:0000312|EMBL:AAG52390.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the thiolase-like superfamily. Chalcone/stilbene
- **Key Domains:** 3-ktacl-CoA_syn. (IPR012392); ACP_syn_III_C. (IPR013747); FAE1_typ3_polyketide_synth. (IPR013601); Thiolase-like. (IPR016039); ACP_syn_III_C (PF08541)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CUT1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CUT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CUT1** (gene ID: CUT1, UniProt: Q9XF43) in ARATH.

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
- **UniProt Accession:** Q9XF43
- **Protein Description:** RecName: Full=3-ketoacyl-CoA synthase 6 {ECO:0000303|PubMed:18465198}; Short=KCS-6 {ECO:0000303|PubMed:18465198}; EC=2.3.1.199 {ECO:0000269|PubMed:10330468}; AltName: Full=Cuticular protein 1 {ECO:0000303|PubMed:10330468}; AltName: Full=Eceriferum 6 {ECO:0000303|PubMed:11041893}; AltName: Full=Very long-chain fatty acid condensing enzyme 6 {ECO:0000303|PubMed:18465198}; Short=VLCFA condensing enzyme 6 {ECO:0000303|PubMed:18465198};
- **Gene Information:** Name=CUT1 {ECO:0000303|PubMed:10330468}; Synonyms=CER6 {ECO:0000303|PubMed:11041893}, EL6, KCS6 {ECO:0000303|PubMed:18465198}; OrderedLocusNames=At1g68530 {ECO:0000312|Araport:AT1G68530}; ORFNames=T26J14.10 {ECO:0000312|EMBL:AAG52390.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the thiolase-like superfamily. Chalcone/stilbene
- **Key Domains:** 3-ktacl-CoA_syn. (IPR012392); ACP_syn_III_C. (IPR013747); FAE1_typ3_polyketide_synth. (IPR013601); Thiolase-like. (IPR016039); ACP_syn_III_C (PF08541)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CUT1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CUT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CUT1** (gene ID: CUT1, UniProt: Q9XF43) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: CUT1/CER6/KCS6 Gene Function in Arabidopsis thaliana

## Gene Identity and Nomenclature

The gene CUT1 (UniProt: Q9XF43, locus At1g68530) in *Arabidopsis thaliana* is synonymous with CER6 (ECERIFERUM 6) and KCS6 (3-KETOACYL-COA SYNTHASE 6). These three names refer to the same genetic locus, established through allelic complementation and sequence analyses (fiebig2000alterationsincer6 pages 1-2, fiebig2000alterationsincer6 pages 2-4). The unified nomenclature reflects independent discoveries of the gene's roles in cuticular wax biosynthesis (CER6), pollen fertility (CUT1), and fatty acid elongation (KCS6).

## Primary Enzymatic Function and Substrate Specificity

### Catalytic Activity

CUT1/CER6/KCS6 encodes a 3-ketoacyl-CoA synthase (EC 2.3.1.199), the condensing enzyme that catalyzes the rate-limiting, chain-length-determining step in very-long-chain fatty acid (VLCFA) biosynthesis (huang2022arabidopsiskcs5and pages 1-2). The enzyme functions as the condensing component of a multi-enzyme fatty acid elongase (FAE) complex localized to the endoplasmic reticulum membrane (batsale2021biosynthesisandfunctions pages 9-10, fukuda2022eceriferum10encoding pages 1-2, batsale2021biosynthesisandfunctions pages 3-5).

The specific reaction catalyzed by KCS6 is:

**Long-chain acyl-CoA + malonyl-CoA → 3-ketoacyl-CoA (two carbons longer) + CO₂ + CoA**

This condensation is the first of four sequential reactions in each VLCFA elongation cycle. Following KCS6-catalyzed condensation, the 3-ketoacyl intermediate undergoes reduction by 3-ketoacyl-CoA reductase (KCR), dehydration by 3-hydroxyacyl-CoA dehydrase (HCD), and a second reduction by enoyl-CoA reductase (ECR) to complete the cycle and produce an acyl-CoA that is two carbons longer than the starting substrate (batsale2021biosynthesisandfunctions pages 3-5).

### Substrate Specificity

KCS6 exhibits overlapping substrate specificity toward acyl-CoAs in the C22–C28 range, with its dominant physiological role being the elongation of C26 to C28 fatty acids (batsale2021biosynthesisandfunctions pages 5-6, huang2022arabidopsiskcs5and pages 1-2, batsale2021biosynthesisandfunctions pages 9-10). Heterologous expression studies in yeast demonstrate that KCS6 primarily generates VLCFAs ranging from C24 to C28 (batsale2023tacklingfunctionalredundancy pages 11-12, batsale2023tacklingfunctionalredundancy pages 12-13). The enzyme accepts both unbranched (straight-chain) and iso-branched acyl-CoA substrates, as evidenced by the reduction of both substrate classes in kcs6 mutants (batsale2023tacklingfunctionalredundancy pages 11-12, batsale2023tacklingfunctionalredundancy pages 12-13).

Biochemical analyses of mutant tissues provide strong evidence for the C26→C28 elongation step as KCS6's major in planta activity: kcs6 mutants accumulate C24 and C26 wax derivatives while showing marked depletion of C28 and longer-chain products (batsale2021biosynthesisandfunctions pages 5-6, huang2022arabidopsiskcs5and pages 4-7, huang2022arabidopsiskcs5and pages 7-9).

### Cofactor Requirements and Protein Interactions

While KCS6 intrinsically supports elongation through C28, efficient extension to C30, C32, and longer VLCFAs requires functional cooperation with CER2-family accessory proteins, including CER2 and CER26 (also known as CER2-LIKE proteins) (huang2022arabidopsiskcs5and pages 1-2, huang2022arabidopsiskcs5and pages 4-7, batsale2023tacklingfunctionalredundancy pages 11-12). Co-expression studies demonstrate that CER2 facilitates elongation around C26–C28, while CER26 supports production of VLCFAs exceeding C30 (huang2022arabidopsiskcs5and pages 4-7, huang2022arabidopsiskcs5and pages 2-4).

The molecular mechanism by which CER2-family proteins modulate KCS6 activity remains incompletely resolved. Proposed mechanisms include altering the enzyme's chain-length specificity, stabilizing the FAE complex, or facilitating repeated substrate cycling to generate longer products (batsale2023tacklingfunctionalredundancy pages 11-12, batsale2021biosynthesisandfunctions pages 5-6). Although CER2-family proteins share homology with BAHD acyltransferases, their conserved catalytic residues are not required for cuticular wax biosynthesis, indicating a non-canonical mechanism (batsale2021biosynthesisandfunctions pages 5-6).

Recent evidence suggests that VAP27-1, an ER–plasma membrane contact-site protein, may enhance KCS6–CER2 complex formation or activity, thereby increasing VLCFA accumulation (han2026theroleand pages 4-5). Additionally, KCS3, a catalytically inactive KCS family member, has been proposed to negatively regulate KCS6 by prolonging interactions among elongase-complex subunits, contributing to wax homeostasis (han2026theroleand pages 4-5).

## Subcellular Localization

KCS6 functions at the **endoplasmic reticulum (ER) membrane** as an integral component of the microsomal FAE complex (batsale2021biosynthesisandfunctions pages 9-10, fukuda2022eceriferum10encoding pages 1-2, batsale2021biosynthesisandfunctions pages 3-5). The ER serves as the site of VLCFA biosynthesis, where the elongated acyl-CoA products are subsequently converted into various lipid classes, including cuticular waxes, sphingolipids, and membrane lipids (huang2022arabidopsiskcs5and pages 9-11, batsale2021biosynthesisandfunctions pages 9-10).

Following synthesis in the ER, VLC acyl-CoAs destined for cuticular wax are modified through downstream pathways and then transported from the ER to the plasma membrane. These wax precursors are secreted across the cell wall and deposited as intracuticular and epicuticular wax layers on the epidermal surface (batsale2021biosynthesisandfunctions pages 9-10).

## Biochemical Pathways

### VLCFA Elongation Pathway

KCS6 occupies a central position in the VLCFA elongation pathway, functioning as the rate-limiting enzyme that controls entry of fatty acyl substrates into the elongation cycle (batsale2021biosynthesisandfunctions pages 5-6, huang2022arabidopsiskcs5and pages 1-2, urano2024arabidopsisdreb26erf12and pages 10-12). As KCS6 is the major condensing enzyme for elongating fatty acids beyond 26 carbons in epidermal tissues, its activity is particularly important for producing the C26–C30 VLCFAs that serve as precursors for cuticular wax compounds (batsale2021biosynthesisandfunctions pages 9-10, urano2024arabidopsisdreb26erf12and pages 12-13).

### Cuticular Wax Biosynthesis

The VLCFAs produced by KCS6-dependent elongation feed into two major downstream pathways that generate the diverse chemical classes of cuticular wax (batsale2021biosynthesisandfunctions pages 9-10, huang2022arabidopsiskcs5and pages 1-2):

1. **Alcohol-forming pathway**: Produces primary alcohols and wax esters through reduction of VLC acyl-CoAs
2. **Alkane-forming pathway** (also called decarbonylation pathway): Produces aldehydes, odd-chain alkanes, secondary alcohols, and ketones through aldehyde decarbonylation

These wax compounds form the hydrophobic protective cuticle that covers aerial plant surfaces, providing a barrier against non-stomatal water loss, UV radiation, pathogens, and environmental stresses (batsale2021biosynthesisandfunctions pages 9-10).

## Expression Patterns and Tissue Specificity

KCS6 expression is enriched in the **epidermis of aerial organs**, consistent with its primary role in cuticular wax biosynthesis for stems, leaves, and other aerial surfaces (batsale2021biosynthesisandfunctions pages 6-9, batsale2021biosynthesisandfunctions pages 5-6). This epidermal expression correlates with the severe wax-deficient phenotype observed in mutant stems.

In reproductive tissues, KCS6 is expressed in developing anthers, particularly in the **tapetum**, the nutritive cell layer that supplies materials for pollen development (houlahan2004localizedposttranscriptionalgene pages 53-58, houlahan2004localizedposttranscriptionalgene pages 122-126). This tapetal expression is essential for generating the lipid-rich pollen coat required for successful pollination and male fertility.

Under drought stress conditions, KCS6 transcript abundance increases transiently, with induction occurring approximately 48 hours after dehydration begins (urano2024arabidopsisdreb26erf12and pages 3-5). This delayed induction follows the early activation of drought-responsive transcription factors and contributes to stress-induced wax accumulation.

## Mutant Phenotypes and Functional Consequences

### Cuticular Wax Deficiency

Loss of KCS6 function produces dramatic, organ-specific effects on cuticular wax accumulation (batsale2021biosynthesisandfunctions pages 5-6, huang2022arabidopsiskcs5and pages 9-11, huang2022arabidopsiskcs5and pages 7-9):

- **Stems**: Approximately 90% reduction in total wax content, or wax remaining at only 13% of wild-type levels; complete loss of visible epicuticular wax crystals; glossy stem appearance
- **Flowers**: Total wax reduced to approximately 14% of wild-type levels
- **Rosette leaves**: More moderate reduction to approximately 68% of wild-type levels (or 32% decrease), reflecting partial functional compensation by the paralogous enzyme KCS5

Biochemically, kcs6 mutants show characteristic alterations in wax chain-length distribution: shorter C24–C28 derivatives accumulate, while products longer than C26 or C28 are severely depleted (batsale2021biosynthesisandfunctions pages 5-6, huang2022arabidopsiskcs5and pages 4-7, huang2022arabidopsiskcs5and pages 7-9). This profile directly reflects the block in C26→C28 elongation and subsequent chain-extension steps.

### Reproductive Defects and Male Fertility

CUT1/CER6/KCS6 mutations cause **conditional male sterility** due to defects in pollen coat formation (batsale2021biosynthesisandfunctions pages 9-10, huang2022arabidopsiskcs5and pages 9-11, fiebig2000alterationsincer6 pages 1-2). In severe alleles such as cer6-2, pollen grains completely lack the lipid-rich pollen coat, preventing normal pollen hydration on the stigma surface (fiebig2000alterationsincer6 pages 4-5, fiebig2000alterationsincer6 pages 5-7, houlahan2004localizedposttranscriptionalgene pages 53-58).

The pollen coat is derived from the tapetum and contains very-long-chain lipids that are essential for pollen recognition by the stigma and for initiating pollen hydration and germination (fiebig2000alterationsincer6 pages 1-2, fiebig2000alterationsincer6 pages 2-4). Mutant pollen can physically adhere to the stigma but fails to hydrate, resulting in impaired germination and reduced seed production (fiebig2000alterationsincer6 pages 1-2, houlahan2004localizedposttranscriptionalgene pages 87-90).

The male sterility is conditional because high atmospheric humidity can provide sufficient water to partially bypass the normal stigma-mediated hydration mechanism, allowing some fertility to be restored (fiebig2000alterationsincer6 pages 1-2). Importantly, pollen fertility can be restored by partial restoration of KCS6 activity that is insufficient to restore normal stem wax, indicating that reproductive tissues have lower VLCFA requirements or higher enzyme expression than vegetative tissues (fiebig2000alterationsincer6 pages 4-5, fiebig2000alterationsincer6 pages 2-4).

### Water Relations and Stress Tolerance

Despite the severe wax deficiency, single kcs6 mutants retain water at rates similar to wild-type plants under some test conditions (huang2022arabidopsiskcs5and pages 7-9, huang2022arabidopsiskcs5and pages 11-12). This finding suggests that moderate wax reductions do not necessarily compromise water retention, likely due to partial functional compensation by KCS5 and other wax-biosynthetic enzymes.

However, simultaneous loss of KCS5 and KCS6 causes much more severe water-loss phenotypes and nearly abolishes drought-induced wax accumulation (urano2024arabidopsisdreb26erf12and pages 10-12, huang2022arabidopsiskcs5and pages 9-11). This demonstrates that KCS6 plays a critical role in the plant's adaptive response to water deficit stress.

## Regulation and Stress Responses

### Drought and Environmental Regulation

KCS6 expression is induced by drought stress as part of a broader transcriptional program that enhances cuticular wax biosynthesis under water-limiting conditions (urano2024arabidopsisdreb26erf12and pages 3-5, urano2024arabidopsisdreb26erf12and pages 2-3). The loss of KCS5 and KCS6 together prevents the normal increase in wax production triggered by drought, demonstrating the functional importance of these enzymes in stress adaptation (urano2024arabidopsisdreb26erf12and pages 10-12, huang2022arabidopsiskcs5and pages 9-11).

### Transcriptional Regulation

Several transcription factor families regulate cuticular wax biosynthesis and KCS6 expression:

**MYB96**: This drought- and ABA-responsive MYB transcription factor directly activates KCS6 expression along with other wax-biosynthetic genes including KCS1, KCS2, KCR1, and CER3 (urano2024arabidopsisdreb26erf12and pages 2-3). MYB96 represents the most direct transcriptional activator of KCS6 identified in the literature. The closely related factor MYB94 also contributes to wax regulation, and the myb94 myb96 double mutant shows reduced wax accumulation (batsale2021biosynthesisandfunctions pages 21-22, rahman2021dissectingtheroles pages 2-3).

**DREB26/ERF12, ERF13, and ERF14**: These AP2/ERF transcription factors are induced early during drought stress and regulate cuticular wax biosynthesis, particularly the very-long-chain alkane pathway (urano2024arabidopsisdreb26erf12and pages 10-12, urano2024arabidopsisdreb26erf12and pages 9-10, urano2024arabidopsisdreb26erf12and pages 12-13, urano2024arabidopsisdreb26erf12and pages 3-5). While these factors regulate multiple wax-biosynthetic genes and influence the pathway in which KCS6 operates, direct transcriptional regulation of KCS6 by these factors has not been definitively established.

**SHN/WIN factors**: The SHINE clade of AP2/ERF transcription factors (SHN1, SHN2, SHN3) and related WIND/RAP2.4 factors regulate cutin and wax biosynthesis (urano2024arabidopsisdreb26erf12and pages 12-13, rahman2021dissectingtheroles pages 2-3). SHN overexpression increases epicuticular wax accumulation and drought tolerance, positioning these factors as positive regulators of the wax pathway, though specific effects on KCS6 transcription require further investigation.

### Functional Redundancy with KCS5

KCS6 functions partially redundantly with its paralog KCS5, another 3-ketoacyl-CoA synthase with overlapping but not identical substrate specificity (huang2022arabidopsiskcs5and pages 1-2, huang2022arabidopsiskcs5and pages 9-11). KCS5 preferentially produces C30 products, while KCS6 produces relatively more C24 products and has stronger activity in stems and flowers (huang2022arabidopsiskcs5and pages 9-11, huang2022arabidopsiskcs5and pages 11-12). 

This functional redundancy explains why single kcs6 mutants show organ-specific phenotypes with stronger effects in stems and flowers than in leaves, where KCS5 can provide greater compensation (huang2022arabidopsiskcs5and pages 9-11, huang2022arabidopsiskcs5and pages 11-12). Double kcs5 kcs6 mutants display additive wax defects and nearly complete loss of drought-induced wax production, demonstrating that these two enzymes together account for the majority of epidermal VLCFA elongation capacity (urano2024arabidopsisdreb26erf12and pages 10-12, huang2022arabidopsiskcs5and pages 9-11, huang2022arabidopsiskcs5and pages 1-2).

## Biological Significance and Physiological Roles

CUT1/CER6/KCS6 serves multiple critical functions in *Arabidopsis* development and stress adaptation:

1. **Epidermal barrier formation**: As the major elongase for producing C26–C30 VLCFAs in aerial epidermis, KCS6 is essential for generating the cuticular wax that forms the primary interface between the plant and its environment (batsale2021biosynthesisandfunctions pages 5-6, batsale2021biosynthesisandfunctions pages 9-10).

2. **Water relations and drought tolerance**: Through its contribution to cuticular wax deposition, KCS6 helps minimize non-stomatal water loss and supports adaptive responses to water deficit (batsale2021biosynthesisandfunctions pages 9-10, urano2024arabidopsisdreb26erf12and pages 10-12, huang2022arabidopsiskcs5and pages 9-11).

3. **Reproductive success**: KCS6 is essential for pollen coat formation, enabling stigma recognition, pollen hydration, germination, and male fertility (fiebig2000alterationsincer6 pages 1-2, fiebig2000alterationsincer6 pages 4-5, fiebig2000alterationsincer6 pages 2-4, houlahan2004localizedposttranscriptionalgene pages 53-58).

4. **Protection from biotic and abiotic stresses**: The cuticular wax layer produced through KCS6 activity provides protection against UV radiation, pathogen invasion, and other environmental challenges (batsale2021biosynthesisandfunctions pages 9-10, bird2003signalsfromthe pages 11-12).

## Summary Tables

| Category | Description | Key Evidence |
|---|---|---|
| Gene identity | **CUT1**, **CER6**, and **KCS6** are synonymous names for the *Arabidopsis thaliana* locus **At1g68530**, corresponding to UniProt **Q9XF43**. Foundational genetic work established that CER6 is identical to CUT1 and encodes a very-long-chain fatty-acid (VLCFA) condensing enzyme. | Identity was established through allelic and complementation studies of cuticular-wax and pollen phenotypes (fiebig2000alterationsincer6 pages 1-2, fiebig2000alterationsincer6 pages 2-4). |
| Protein function | The product is **3-ketoacyl-CoA synthase 6 (KCS6; EC 2.3.1.199)**, the condensing and principal chain-length-determining component of an endoplasmic-reticulum fatty-acid elongase (FAE) complex. Its primary physiological function is to generate VLC acyl-CoA precursors for cuticular wax and pollen-coat lipids. | Contemporary FAE-complex analyses identify KCS enzymes as chain-length-selective condensing components and KCS6 as a major epidermal wax enzyme (batsale2023tacklingfunctionalredundancy pages 11-12, batsale2023tacklingfunctionalredundancy pages 12-13, batsale2021biosynthesisandfunctions pages 5-6). |
| Enzymatic activity | KCS6 catalyzes the first, rate-controlling reaction of each elongation cycle: **long-chain acyl-CoA + malonyl-CoA → a 3-ketoacyl-CoA containing two additional carbons + CO₂ + CoA**. KCR, HCD, and ECR subsequently reduce, dehydrate, and reduce this intermediate to the elongated acyl-CoA. | The reaction and organization of the four-step, ER-associated FAE cycle are supported by biochemical reviews and reconstitution studies (batsale2021biosynthesisandfunctions pages 3-5, huang2022arabidopsiskcs5and pages 1-2). |
| Substrate specificity | KCS6 shows overlapping activity toward approximately **C22–C28 acyl substrates**, with its dominant in-planta role generally assigned to **C26→C28 elongation**. Yeast reconstitution places its principal product range around C24–C28. Mutants accumulate C24/C26 or C24–C28 derivatives while losing longer products. Evidence also indicates acceptance of straight-chain and iso-branched substrates. | Heterologous assays and mutant lipid profiles jointly define the substrate range and major C26→C28 step (batsale2021biosynthesisandfunctions pages 5-6, huang2022arabidopsiskcs5and pages 1-2, batsale2023tacklingfunctionalredundancy pages 12-13, huang2022arabidopsiskcs5and pages 4-7, huang2022arabidopsiskcs5and pages 7-9). |
| Cofactor requirements | KCS6 operates with the shared FAE enzymes KCR, HCD, and ECR. Its intrinsic activity principally supports chains through C28; efficient extension beyond C28 to **C30–C32 and longer wax precursors** requires auxiliary **CER2-family proteins**, including CER2 and CER26/CER2-LIKE factors. Their exact mechanism may involve altering chain-length specificity, stabilizing the complex, or promoting repeated substrate cycling. | Co-expression experiments show CER2-family dependence for longer products, although the precise physical interfaces remain incompletely defined (huang2022arabidopsiskcs5and pages 1-2, huang2022arabidopsiskcs5and pages 4-7, batsale2023tacklingfunctionalredundancy pages 11-12, batsale2021biosynthesisandfunctions pages 5-6). |
| Subcellular localization | KCS6 carries out VLCFA elongation at the **endoplasmic-reticulum membrane** as part of the microsomal FAE complex. Its ER-generated products are converted into wax compounds, transported to the plasma membrane, secreted across the cell wall, and deposited as intracuticular and epicuticular wax. Protein-specific microscopy evidence in the cited excerpts is less direct than the biochemical evidence locating FAE activity in the ER. | ER localization is supported by the established location of plant FAE complexes and the intracellular wax-biosynthesis and transport route (batsale2021biosynthesisandfunctions pages 9-10, fukuda2022eceriferum10encoding pages 1-2, batsale2021biosynthesisandfunctions pages 3-5). |
| Expression pattern | Expression is enriched in the **epidermis of aerial organs**, matching the site of cuticular-wax synthesis. Reproductive expression occurs in developing anthers, including the **tapetum**, which supplies pollen-coat materials. KCS6 transcripts are transiently induced approximately 48 hours after dehydration begins. | Epidermal expression, anther/tapetal expression, and drought induction are supported by expression and functional studies (batsale2021biosynthesisandfunctions pages 6-9, houlahan2004localizedposttranscriptionalgene pages 53-58, urano2024arabidopsisdreb26erf12and pages 3-5, batsale2021biosynthesisandfunctions pages 5-6). |
| Mutant phenotypes | Loss of KCS6 produces glossy stems with few or no visible wax crystals and major, organ-dependent decreases in wax. Reported values include approximately **90% loss of stem wax**, or stem wax remaining at about **13% of wild type**; flower wax is about **14% of wild type**, whereas rosette-leaf wax falls by roughly **32%**. Mutants accumulate shorter C24–C28 compounds and lose products longer than C26/C28. | Quantitative organ-specific lipid profiling demonstrates a severe stem/flower defect and partial leaf compensation (batsale2021biosynthesisandfunctions pages 5-6, huang2022arabidopsiskcs5and pages 9-11, huang2022arabidopsiskcs5and pages 7-9, huang2022arabidopsiskcs5and pages 11-12). |
| Biological roles | KCS6 supplies VLC acyl-CoAs to both major wax branches: the alcohol-forming route, which produces primary alcohols and wax esters, and the alkane-forming route, which produces aldehydes, alkanes, secondary alcohols, and ketones. It thereby supports epidermal barrier formation and drought-responsive wax deposition. In anthers, it enables production of pollen-coat lipids required for stigma-mediated pollen hydration, germination, and male fertility. | Pathway, drought, and reproductive studies establish these roles. Strong mutants have defective pollen coats and conditional male sterility; high humidity or partial lipid restoration can rescue fertility (batsale2021biosynthesisandfunctions pages 9-10, urano2024arabidopsisdreb26erf12and pages 10-12, fiebig2000alterationsincer6 pages 1-2, fiebig2000alterationsincer6 pages 4-5, houlahan2004localizedposttranscriptionalgene pages 53-58). |


*Table: This table summarizes the verified identity, catalytic properties, localization, expression, mutant phenotypes, and biological functions of Arabidopsis CUT1/CER6/KCS6. It distinguishes well-supported biochemical conclusions from mechanistic details that remain unresolved.*

| Regulatory Factor/Condition | Type of Regulation | Effect on KCS6 | Evidence/Mechanism |
|---|---|---|---|
| Drought/dehydration | Environmental, transcriptional induction | **KCS6 transcript abundance rises transiently**, approximately 48 hours after dehydration begins; KCS6 contributes to drought-induced wax accumulation. | The delayed induction follows early activation of drought-responsive AP2/ERF factors. Loss of both KCS5 and KCS6 nearly abolishes drought-induced wax production, demonstrating functional importance while also revealing paralog redundancy (urano2024arabidopsisdreb26erf12and pages 10-12, huang2022arabidopsiskcs5and pages 9-11, urano2024arabidopsisdreb26erf12and pages 3-5). |
| MYB96 | Drought- and ABA-responsive transcriptional activation | Activates **KCS6** expression as part of a broader wax-biosynthetic program. | MYB96 is reported as an activator of KCS6 together with KCS1, KCS2, KCR1, and CER3. This is the strongest specific transcription-factor-to-KCS6 relationship among the regulators considered here, although direct promoter occupancy is not established in the cited excerpt (urano2024arabidopsisdreb26erf12and pages 2-3). |
| ABA signaling | Hormonal regulation, principally through MYB transcription factors | Expected to increase KCS6-dependent VLCFA and wax synthesis under water deficit, chiefly through induction of MYB96. | ABA, drought, and salt induce MYB94/MYB96, and the myb94 myb96 double mutant has reduced wax loading. Specific support is strongest for MYB96 activation of KCS6; a direct ABA-to-KCS6 promoter mechanism has not been demonstrated in the cited evidence (batsale2021biosynthesisandfunctions pages 21-22, rahman2021dissectingtheroles pages 2-3, urano2024arabidopsisdreb26erf12and pages 2-3). |
| DREB26/ERF12, ERF13, and ERF14 | Early drought-responsive AP2/ERF regulatory network | Promote the broader wax pathway in which KCS6 operates, but **direct regulation of KCS6 is unproven**. | These factors are induced early during drought and alter VLCFA/alkane profiles. DREB26 regulates KCS2, CER26L, CER1, and SHN3; KCS6 is induced later, but it was not identified as a direct DREB26-responsive target in the reported expression analysis (urano2024arabidopsisdreb26erf12and pages 10-12, urano2024arabidopsisdreb26erf12and pages 9-10, urano2024arabidopsisdreb26erf12and pages 12-13, urano2024arabidopsisdreb26erf12and pages 3-5). |
| SHN2 and SHN3 | AP2/ERF-mediated downstream wax regulation | Likely enhance the KCS6-dependent wax pathway indirectly; a specific effect on KCS6 transcription is not established. | SHN factors regulate cutin and wax biosynthesis and are drought responsive; SHN3 is positively regulated within the DREB26/ERF12 network. Available evidence supports pathway-level regulation rather than direct SHN binding to the KCS6 promoter (urano2024arabidopsisdreb26erf12and pages 10-12, urano2024arabidopsisdreb26erf12and pages 12-13, rahman2021dissectingtheroles pages 2-3). |
| CER2 | FAE-complex accessory factor; functional protein cooperation | Broadens KCS6 activity beyond its principal C24–C28 range, enabling efficient production of approximately C30 VLCFAs. | Co-expression assays identify CER2-family proteins as required cofactors for KCS6-mediated elongation beyond C28. Proposed mechanisms include changing chain-length specificity, stabilizing the elongase complex, or facilitating repeated substrate cycling; the molecular mechanism remains unresolved (huang2022arabidopsiskcs5and pages 1-2, batsale2023tacklingfunctionalredundancy pages 11-12, batsale2021biosynthesisandfunctions pages 5-6). |
| CER26 / CER2-LIKE factors | FAE-complex accessory factor | Supports extension to C30–C32 and longer VLCFAs; under drought, CER26L may cooperate with KCS6 to increase VLCFAs longer than C26. | Functional co-expression supports CER26-family dependence for longer products. Split-luciferase constructs were used to test KCS6–CER26 association, but the cited excerpts do not provide an unequivocal positive physical-interaction result (huang2022arabidopsiskcs5and pages 4-7, huang2022arabidopsiskcs5and pages 2-4, huang2022arabidopsiskcs5and pages 11-12, urano2024arabidopsisdreb26erf12and pages 12-13). |
| VAP27-1 | Proposed ER–plasma-membrane contact-site organizer and protein-complex regulator | Reported to promote KCS6–CER2 complex formation or activity, increasing VLCFA accumulation. | This mechanism is described in a later review summarizing emerging evidence; it should be treated as newer and less established than the genetic and biochemical evidence for CER2-family functional cooperation (han2026theroleand pages 4-5). |
| KCS3 | Negative regulation through elongase-complex interactions | Reported to restrain KCS6-dependent elongation and maintain wax homeostasis. | KCS3 is described as catalytically inactive and as prolonging interactions among elongase-complex subunits, thereby negatively modulating KCS6. The available citation is a later review-level account rather than direct evidence in the retrieved excerpts (han2026theroleand pages 4-5). |
| KCS5 redundancy | Parallel enzymatic activity and genetic buffering | Partially compensates for KCS6, especially in leaves; combined loss causes additive wax defects and nearly blocks drought-induced wax accumulation. | KCS5 and KCS6 have overlapping chain-length specificities, but KCS6 is generally dominant in stems and flowers. This redundancy explains why single-mutant physiological effects can be weaker than the severe biochemical wax defect (huang2022arabidopsiskcs5and pages 9-11, huang2022arabidopsiskcs5and pages 1-2, huang2022arabidopsiskcs5and pages 11-12). |


*Table: This table distinguishes direct KCS6 regulation from pathway-level associations and summarizes environmental, transcriptional, and protein-complex control. It also flags mechanisms for which current evidence remains indirect or review-based.*

## Recent Research Developments (2020-2024)

Recent studies have provided significant advances in understanding KCS6 function:

- **Functional redundancy characterization**: Comprehensive analysis of KCS5 and KCS6 redundancy using CRISPR/Cas9-generated mutants, revealing organ-specific contributions and drought-response roles (huang2022arabidopsiskcs5and pages 1-2, huang2022arabidopsiskcs5and pages 9-11)

- **Regulatory network elucidation**: Identification of DREB26/ERF12 and related AP2/ERF factors as key drought-responsive regulators of the wax biosynthetic pathway (urano2024arabidopsisdreb26erf12and pages 10-12, urano2024arabidopsisdreb26erf12and pages 3-5)

- **FAE complex reconstitution**: Systematic reconstitution of Arabidopsis FAE complexes in yeast to characterize substrate specificities and identify functional redundancies among KCS family members (batsale2023tacklingfunctionalredundancy pages 11-12)

- **Protein-protein interaction networks**: Emerging evidence for regulation of KCS6 activity through protein-complex interactions, including roles for VAP27-1 and negative regulation by KCS3 (han2026theroleand pages 4-5)

## Conclusion

CUT1/CER6/KCS6 encodes a 3-ketoacyl-CoA synthase that serves as the major condensing enzyme for very-long-chain fatty acid biosynthesis in *Arabidopsis thaliana* epidermal tissues. Through its primary role in catalyzing C26→C28 fatty acid elongation at the endoplasmic reticulum, KCS6 supplies the VLCFA precursors essential for cuticular wax formation on aerial organs and pollen coat assembly in reproductive tissues. The enzyme exhibits substrate specificity for C22–C28 acyl-CoAs and requires CER2/CER26 cofactors for efficient extension to longer products. Loss of KCS6 function results in severe cuticular wax deficiency, glossy stems, and conditional male sterility, demonstrating the enzyme's critical importance for both vegetative protection and reproductive success. KCS6 expression is induced by drought stress and regulated by MYB96 and other transcription factors, positioning this enzyme as a key component of the plant's adaptive response to environmental challenges.

References

1. (fiebig2000alterationsincer6 pages 1-2): Aretha Fiebig, Jacob A. Mayfield, Natasha L. Miley, Samantha Chau, Robert L. Fischer, and Daphne Preuss. Alterations in cer6, a gene identical to cut1, differentially affect long-chain lipid content on the surface of pollen and stems. Plant Cell, 12:2001-2008, Oct 2000. URL: https://doi.org/10.1105/tpc.12.10.2001, doi:10.1105/tpc.12.10.2001. This article has 493 citations and is from a highest quality peer-reviewed journal.

2. (fiebig2000alterationsincer6 pages 2-4): Aretha Fiebig, Jacob A. Mayfield, Natasha L. Miley, Samantha Chau, Robert L. Fischer, and Daphne Preuss. Alterations in cer6, a gene identical to cut1, differentially affect long-chain lipid content on the surface of pollen and stems. Plant Cell, 12:2001-2008, Oct 2000. URL: https://doi.org/10.1105/tpc.12.10.2001, doi:10.1105/tpc.12.10.2001. This article has 493 citations and is from a highest quality peer-reviewed journal.

3. (huang2022arabidopsiskcs5and pages 1-2): Haodong Huang, Asma Ayaz, Minglü Zheng, Xianpeng Yang, Wajid Zaman, Huayan Zhao, and Shiyou Lü. Arabidopsis kcs5 and kcs6 play redundant roles in wax synthesis. International Journal of Molecular Sciences, 23:4450, Apr 2022. URL: https://doi.org/10.3390/ijms23084450, doi:10.3390/ijms23084450. This article has 65 citations.

4. (batsale2021biosynthesisandfunctions pages 9-10): Marguerite Batsale, Delphine Bahammou, Laetitia Fouillen, Sébastien Mongrand, Jérôme Joubès, and Frédéric Domergue. Biosynthesis and functions of very-long-chain fatty acids in the responses of plants to abiotic and biotic stresses. Cells, 10:1284, May 2021. URL: https://doi.org/10.3390/cells10061284, doi:10.3390/cells10061284. This article has 262 citations.

5. (fukuda2022eceriferum10encoding pages 1-2): Norika Fukuda, Yoshimi Oshima, Hirotaka Ariga, Takuma Kajino, Takashi Koyama, Yukio Yaguchi, Keisuke Tanaka, Izumi Yotsui, Yoichi Sakata, and Teruaki Taji. Eceriferum 10 encoding an enoyl-coa reductase plays a crucial role in osmotolerance and cuticular wax loading in arabidopsis. Frontiers in Plant Science, Jun 2022. URL: https://doi.org/10.3389/fpls.2022.898317, doi:10.3389/fpls.2022.898317. This article has 17 citations.

6. (batsale2021biosynthesisandfunctions pages 3-5): Marguerite Batsale, Delphine Bahammou, Laetitia Fouillen, Sébastien Mongrand, Jérôme Joubès, and Frédéric Domergue. Biosynthesis and functions of very-long-chain fatty acids in the responses of plants to abiotic and biotic stresses. Cells, 10:1284, May 2021. URL: https://doi.org/10.3390/cells10061284, doi:10.3390/cells10061284. This article has 262 citations.

7. (batsale2021biosynthesisandfunctions pages 5-6): Marguerite Batsale, Delphine Bahammou, Laetitia Fouillen, Sébastien Mongrand, Jérôme Joubès, and Frédéric Domergue. Biosynthesis and functions of very-long-chain fatty acids in the responses of plants to abiotic and biotic stresses. Cells, 10:1284, May 2021. URL: https://doi.org/10.3390/cells10061284, doi:10.3390/cells10061284. This article has 262 citations.

8. (batsale2023tacklingfunctionalredundancy pages 11-12): Marguerite Batsale, Marie Alonso, Stéphanie Pascal, Didier Thoraval, Richard P. Haslam, Frédéric Beaudoin, Frédéric Domergue, and Jérôme Joubès. Tackling functional redundancy of arabidopsis fatty acid elongase complexes. Frontiers in Plant Science, Jan 2023. URL: https://doi.org/10.3389/fpls.2023.1107333, doi:10.3389/fpls.2023.1107333. This article has 48 citations.

9. (batsale2023tacklingfunctionalredundancy pages 12-13): Marguerite Batsale, Marie Alonso, Stéphanie Pascal, Didier Thoraval, Richard P. Haslam, Frédéric Beaudoin, Frédéric Domergue, and Jérôme Joubès. Tackling functional redundancy of arabidopsis fatty acid elongase complexes. Frontiers in Plant Science, Jan 2023. URL: https://doi.org/10.3389/fpls.2023.1107333, doi:10.3389/fpls.2023.1107333. This article has 48 citations.

10. (huang2022arabidopsiskcs5and pages 4-7): Haodong Huang, Asma Ayaz, Minglü Zheng, Xianpeng Yang, Wajid Zaman, Huayan Zhao, and Shiyou Lü. Arabidopsis kcs5 and kcs6 play redundant roles in wax synthesis. International Journal of Molecular Sciences, 23:4450, Apr 2022. URL: https://doi.org/10.3390/ijms23084450, doi:10.3390/ijms23084450. This article has 65 citations.

11. (huang2022arabidopsiskcs5and pages 7-9): Haodong Huang, Asma Ayaz, Minglü Zheng, Xianpeng Yang, Wajid Zaman, Huayan Zhao, and Shiyou Lü. Arabidopsis kcs5 and kcs6 play redundant roles in wax synthesis. International Journal of Molecular Sciences, 23:4450, Apr 2022. URL: https://doi.org/10.3390/ijms23084450, doi:10.3390/ijms23084450. This article has 65 citations.

12. (huang2022arabidopsiskcs5and pages 2-4): Haodong Huang, Asma Ayaz, Minglü Zheng, Xianpeng Yang, Wajid Zaman, Huayan Zhao, and Shiyou Lü. Arabidopsis kcs5 and kcs6 play redundant roles in wax synthesis. International Journal of Molecular Sciences, 23:4450, Apr 2022. URL: https://doi.org/10.3390/ijms23084450, doi:10.3390/ijms23084450. This article has 65 citations.

13. (han2026theroleand pages 4-5): De-Zhi Han, Jia-Min Lu, Caitong Zhao, Shahid Ali, and Zhen-Feng Jiang. The role and regulatory mechanisms of cuticular wax in crop stress tolerance and yield. Plants, 15:554, Feb 2026. URL: https://doi.org/10.3390/plants15040554, doi:10.3390/plants15040554. This article has 6 citations.

14. (huang2022arabidopsiskcs5and pages 9-11): Haodong Huang, Asma Ayaz, Minglü Zheng, Xianpeng Yang, Wajid Zaman, Huayan Zhao, and Shiyou Lü. Arabidopsis kcs5 and kcs6 play redundant roles in wax synthesis. International Journal of Molecular Sciences, 23:4450, Apr 2022. URL: https://doi.org/10.3390/ijms23084450, doi:10.3390/ijms23084450. This article has 65 citations.

15. (urano2024arabidopsisdreb26erf12and pages 10-12): Kaoru Urano, Yoshimi Oshima, Toshiki Ishikawa, Takuma Kajino, Shingo Sakamoto, Mayuko Sato, Kiminori Toyooka, Miki Fujita, Maki Kawai‐Yamada, Teruaki Taji, Kyonoshin Maruyama, Kazuko Yamaguchi‐Shinozaki, and Kazuo Shinozaki. Arabidopsis dreb26/erf12 and its close relatives regulate cuticular wax biosynthesis under drought stress condition. The Plant Journal, 120:2057-2075, Oct 2024. URL: https://doi.org/10.1111/tpj.17100, doi:10.1111/tpj.17100. This article has 29 citations.

16. (urano2024arabidopsisdreb26erf12and pages 12-13): Kaoru Urano, Yoshimi Oshima, Toshiki Ishikawa, Takuma Kajino, Shingo Sakamoto, Mayuko Sato, Kiminori Toyooka, Miki Fujita, Maki Kawai‐Yamada, Teruaki Taji, Kyonoshin Maruyama, Kazuko Yamaguchi‐Shinozaki, and Kazuo Shinozaki. Arabidopsis dreb26/erf12 and its close relatives regulate cuticular wax biosynthesis under drought stress condition. The Plant Journal, 120:2057-2075, Oct 2024. URL: https://doi.org/10.1111/tpj.17100, doi:10.1111/tpj.17100. This article has 29 citations.

17. (batsale2021biosynthesisandfunctions pages 6-9): Marguerite Batsale, Delphine Bahammou, Laetitia Fouillen, Sébastien Mongrand, Jérôme Joubès, and Frédéric Domergue. Biosynthesis and functions of very-long-chain fatty acids in the responses of plants to abiotic and biotic stresses. Cells, 10:1284, May 2021. URL: https://doi.org/10.3390/cells10061284, doi:10.3390/cells10061284. This article has 262 citations.

18. (houlahan2004localizedposttranscriptionalgene pages 53-58): Localized post-transcriptional gene silencing of the very long chain fatty acid condensing enzyme, CER6, and analysis of transcript accumulation in the anthers of developing flower buds of Arabidopsis thaliana This article has 0 citations.

19. (houlahan2004localizedposttranscriptionalgene pages 122-126): Localized post-transcriptional gene silencing of the very long chain fatty acid condensing enzyme, CER6, and analysis of transcript accumulation in the anthers of developing flower buds of Arabidopsis thaliana This article has 0 citations.

20. (urano2024arabidopsisdreb26erf12and pages 3-5): Kaoru Urano, Yoshimi Oshima, Toshiki Ishikawa, Takuma Kajino, Shingo Sakamoto, Mayuko Sato, Kiminori Toyooka, Miki Fujita, Maki Kawai‐Yamada, Teruaki Taji, Kyonoshin Maruyama, Kazuko Yamaguchi‐Shinozaki, and Kazuo Shinozaki. Arabidopsis dreb26/erf12 and its close relatives regulate cuticular wax biosynthesis under drought stress condition. The Plant Journal, 120:2057-2075, Oct 2024. URL: https://doi.org/10.1111/tpj.17100, doi:10.1111/tpj.17100. This article has 29 citations.

21. (fiebig2000alterationsincer6 pages 4-5): Aretha Fiebig, Jacob A. Mayfield, Natasha L. Miley, Samantha Chau, Robert L. Fischer, and Daphne Preuss. Alterations in cer6, a gene identical to cut1, differentially affect long-chain lipid content on the surface of pollen and stems. Plant Cell, 12:2001-2008, Oct 2000. URL: https://doi.org/10.1105/tpc.12.10.2001, doi:10.1105/tpc.12.10.2001. This article has 493 citations and is from a highest quality peer-reviewed journal.

22. (fiebig2000alterationsincer6 pages 5-7): Aretha Fiebig, Jacob A. Mayfield, Natasha L. Miley, Samantha Chau, Robert L. Fischer, and Daphne Preuss. Alterations in cer6, a gene identical to cut1, differentially affect long-chain lipid content on the surface of pollen and stems. Plant Cell, 12:2001-2008, Oct 2000. URL: https://doi.org/10.1105/tpc.12.10.2001, doi:10.1105/tpc.12.10.2001. This article has 493 citations and is from a highest quality peer-reviewed journal.

23. (houlahan2004localizedposttranscriptionalgene pages 87-90): Localized post-transcriptional gene silencing of the very long chain fatty acid condensing enzyme, CER6, and analysis of transcript accumulation in the anthers of developing flower buds of Arabidopsis thaliana This article has 0 citations.

24. (huang2022arabidopsiskcs5and pages 11-12): Haodong Huang, Asma Ayaz, Minglü Zheng, Xianpeng Yang, Wajid Zaman, Huayan Zhao, and Shiyou Lü. Arabidopsis kcs5 and kcs6 play redundant roles in wax synthesis. International Journal of Molecular Sciences, 23:4450, Apr 2022. URL: https://doi.org/10.3390/ijms23084450, doi:10.3390/ijms23084450. This article has 65 citations.

25. (urano2024arabidopsisdreb26erf12and pages 2-3): Kaoru Urano, Yoshimi Oshima, Toshiki Ishikawa, Takuma Kajino, Shingo Sakamoto, Mayuko Sato, Kiminori Toyooka, Miki Fujita, Maki Kawai‐Yamada, Teruaki Taji, Kyonoshin Maruyama, Kazuko Yamaguchi‐Shinozaki, and Kazuo Shinozaki. Arabidopsis dreb26/erf12 and its close relatives regulate cuticular wax biosynthesis under drought stress condition. The Plant Journal, 120:2057-2075, Oct 2024. URL: https://doi.org/10.1111/tpj.17100, doi:10.1111/tpj.17100. This article has 29 citations.

26. (batsale2021biosynthesisandfunctions pages 21-22): Marguerite Batsale, Delphine Bahammou, Laetitia Fouillen, Sébastien Mongrand, Jérôme Joubès, and Frédéric Domergue. Biosynthesis and functions of very-long-chain fatty acids in the responses of plants to abiotic and biotic stresses. Cells, 10:1284, May 2021. URL: https://doi.org/10.3390/cells10061284, doi:10.3390/cells10061284. This article has 262 citations.

27. (rahman2021dissectingtheroles pages 2-3): Tawhidur Rahman, Mingxuan Shao, Shankar Pahari, Prakash Venglat, Raju Soolanayakanahally, Xiao Qiu, Abidur Rahman, and Karen Tanino. Dissecting the roles of cuticular wax in plant resistance to shoot dehydration and low-temperature stress in arabidopsis. International Journal of Molecular Sciences, 22:1554, Feb 2021. URL: https://doi.org/10.3390/ijms22041554, doi:10.3390/ijms22041554. This article has 67 citations.

28. (urano2024arabidopsisdreb26erf12and pages 9-10): Kaoru Urano, Yoshimi Oshima, Toshiki Ishikawa, Takuma Kajino, Shingo Sakamoto, Mayuko Sato, Kiminori Toyooka, Miki Fujita, Maki Kawai‐Yamada, Teruaki Taji, Kyonoshin Maruyama, Kazuko Yamaguchi‐Shinozaki, and Kazuo Shinozaki. Arabidopsis dreb26/erf12 and its close relatives regulate cuticular wax biosynthesis under drought stress condition. The Plant Journal, 120:2057-2075, Oct 2024. URL: https://doi.org/10.1111/tpj.17100, doi:10.1111/tpj.17100. This article has 29 citations.

29. (bird2003signalsfromthe pages 11-12): Susannah M. Bird and Julie E. Gray. Signals from the cuticle affect epidermal cell differentiation. The New phytologist, 157 1:9-23, Jan 2003. URL: https://doi.org/10.1046/j.1469-8137.2003.00543.x, doi:10.1046/j.1469-8137.2003.00543.x. This article has 159 citations.

## Artifacts

- [Edison artifact artifact-00](CUT1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](CUT1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. batsale2021biosynthesisandfunctions pages 3-5
2. batsale2021biosynthesisandfunctions pages 5-6
3. han2026theroleand pages 4-5
4. batsale2021biosynthesisandfunctions pages 9-10
5. batsale2023tacklingfunctionalredundancy pages 11-12
6. batsale2023tacklingfunctionalredundancy pages 12-13
7. batsale2021biosynthesisandfunctions pages 6-9
8. houlahan2004localizedposttranscriptionalgene pages 53-58
9. houlahan2004localizedposttranscriptionalgene pages 122-126
10. houlahan2004localizedposttranscriptionalgene pages 87-90
11. batsale2021biosynthesisandfunctions pages 21-22
12. rahman2021dissectingtheroles pages 2-3
13. bird2003signalsfromthe pages 11-12
14. https://doi.org/10.1105/tpc.12.10.2001,
15. https://doi.org/10.3390/ijms23084450,
16. https://doi.org/10.3390/cells10061284,
17. https://doi.org/10.3389/fpls.2022.898317,
18. https://doi.org/10.3389/fpls.2023.1107333,
19. https://doi.org/10.3390/plants15040554,
20. https://doi.org/10.1111/tpj.17100,
21. https://doi.org/10.3390/ijms22041554,
22. https://doi.org/10.1046/j.1469-8137.2003.00543.x,