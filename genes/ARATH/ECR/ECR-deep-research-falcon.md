---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:49:29.136498'
end_time: '2026-09-30T06:03:41.427853'
duration_seconds: 852.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: ECR
  gene_symbol: ECR
  uniprot_accession: Q9M2U2
  protein_description: 'RecName: Full=Very-long-chain enoyl-CoA reductase {ECO:0000305};
    EC=1.3.1.93 {ECO:0000305|PubMed:14673020, ECO:0000305|PubMed:15829606}; AltName:
    Full=Enoyl-CoA reductase; Short=AtECR {ECO:0000303|PubMed:15829606}; AltName:
    Full=Protein ACQUIRED OSMOTOLERANCE-DEFECTIVE 2 {ECO:0000303|PubMed:35812913};
    AltName: Full=Protein ECERIFERUM 10 {ECO:0000303|PubMed:35812913}; AltName: Full=Synaptic
    glycoprotein SC2-like protein;'
  gene_info: Name=ECR {ECO:0000303|PubMed:15829606}; Synonyms=AOD2 {ECO:0000303|PubMed:35812913},
    AtTSC13 {ECO:0000303|PubMed:14673020}, CER10 {ECO:0000303|PubMed:15829606}; OrderedLocusNames=At3g55360
    {ECO:0000312|EMBL:AEE79372.1}; ORFNames=T22E16.20 {ECO:0000312|EMBL:CAB75894.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the steroid 5-alpha reductase family.
  protein_domains: 3-oxo-5_a-steroid_4-DH_C. (IPR001104); SRD5A/TECR. (IPR039357);
    Steroid_dh (PF02544)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: ECR-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: ECR-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: ECR-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9M2U2
- **Protein Description:** RecName: Full=Very-long-chain enoyl-CoA reductase {ECO:0000305}; EC=1.3.1.93 {ECO:0000305|PubMed:14673020, ECO:0000305|PubMed:15829606}; AltName: Full=Enoyl-CoA reductase; Short=AtECR {ECO:0000303|PubMed:15829606}; AltName: Full=Protein ACQUIRED OSMOTOLERANCE-DEFECTIVE 2 {ECO:0000303|PubMed:35812913}; AltName: Full=Protein ECERIFERUM 10 {ECO:0000303|PubMed:35812913}; AltName: Full=Synaptic glycoprotein SC2-like protein;
- **Gene Information:** Name=ECR {ECO:0000303|PubMed:15829606}; Synonyms=AOD2 {ECO:0000303|PubMed:35812913}, AtTSC13 {ECO:0000303|PubMed:14673020}, CER10 {ECO:0000303|PubMed:15829606}; OrderedLocusNames=At3g55360 {ECO:0000312|EMBL:AEE79372.1}; ORFNames=T22E16.20 {ECO:0000312|EMBL:CAB75894.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the steroid 5-alpha reductase family.
- **Key Domains:** 3-oxo-5_a-steroid_4-DH_C. (IPR001104); SRD5A/TECR. (IPR039357); Steroid_dh (PF02544)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ECR" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ECR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ECR** (gene ID: ECR, UniProt: Q9M2U2) in ARATH.

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
- **UniProt Accession:** Q9M2U2
- **Protein Description:** RecName: Full=Very-long-chain enoyl-CoA reductase {ECO:0000305}; EC=1.3.1.93 {ECO:0000305|PubMed:14673020, ECO:0000305|PubMed:15829606}; AltName: Full=Enoyl-CoA reductase; Short=AtECR {ECO:0000303|PubMed:15829606}; AltName: Full=Protein ACQUIRED OSMOTOLERANCE-DEFECTIVE 2 {ECO:0000303|PubMed:35812913}; AltName: Full=Protein ECERIFERUM 10 {ECO:0000303|PubMed:35812913}; AltName: Full=Synaptic glycoprotein SC2-like protein;
- **Gene Information:** Name=ECR {ECO:0000303|PubMed:15829606}; Synonyms=AOD2 {ECO:0000303|PubMed:35812913}, AtTSC13 {ECO:0000303|PubMed:14673020}, CER10 {ECO:0000303|PubMed:15829606}; OrderedLocusNames=At3g55360 {ECO:0000312|EMBL:AEE79372.1}; ORFNames=T22E16.20 {ECO:0000312|EMBL:CAB75894.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the steroid 5-alpha reductase family.
- **Key Domains:** 3-oxo-5_a-steroid_4-DH_C. (IPR001104); SRD5A/TECR. (IPR039357); Steroid_dh (PF02544)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ECR" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ECR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ECR** (gene ID: ECR, UniProt: Q9M2U2) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: ECR Gene (At3g55360, UniProt Q9M2U2) in Arabidopsis thaliana

## Gene Identity and Nomenclature

The gene ECR (At3g55360, UniProt Q9M2U2) encodes a very-long-chain enoyl-CoA reductase in *Arabidopsis thaliana*. This protein is known by multiple synonyms: **ECR** (Enoyl-CoA Reductase), **CER10** (ECERIFERUM 10), **AtECR**, **AOD2** (ACQUIRED OSMOTOLERANCE-DEFECTIVE 2), and **AtTSC13** (zheng2005disruptionsofthe pages 2-3, fukuda2022eceriferum10encoding pages 1-2). The gene was originally identified through sequence homology to the yeast TSC13 gene encoding an enoyl-CoA reductase, and its function was confirmed by heterologous complementation of temperature-sensitive yeast *tsc13* mutants (zheng2005disruptionsofthe pages 2-3, zheng2005disruptionsofthe pages 3-6). This confirms that the research focuses on the correct gene as specified in the UniProt annotation.

## Primary Enzymatic Function and Biochemical Reaction

### Catalytic Activity

ECR/CER10 functions as a **very-long-chain enoyl-CoA reductase** (EC 1.3.1.93) that catalyzes the fourth and final step of each fatty acid elongation cycle in the endoplasmic reticulum (zheng2005disruptionsofthe pages 8-9, haslam2017theuniquerole pages 1-3, zheng2005disruptionsofthe pages 1-2). The specific biochemical reaction catalyzed is:

**trans-2,3-enoyl-CoA + NADPH + H⁺ → saturated acyl-CoA + NADP⁺**

This reduction converts the enoyl-CoA intermediate produced by the preceding dehydratase (HCD) step into a fully saturated acyl-CoA product that is two carbons longer than the starting acyl-CoA primer (zheng2005disruptionsofthe pages 8-9, haslam2017theuniquerole pages 3-5, haslam2017theuniquerole pages 1-3). The enzyme utilizes **NADPH** as the reducing cofactor, consistent with plant ECR homologs containing a conserved NADP/NAD-binding motif (liu2022ectopicoverexpressionof pages 1-2).

### Substrate Specificity

Unlike the 3-ketoacyl-CoA synthase (KCS) enzymes that determine chain-length specificity in the fatty acid elongase complex, ECR exhibits **broad substrate specificity** across different very-long-chain fatty acid (VLCFA) chain lengths (zheng2005disruptionsofthe pages 8-9, haslam2017theuniquerole pages 1-3). ECR is characterized as a "generalist" elongase component that functions with substrates of all chain lengths processed by the elongase complex, rather than being restricted to one particular VLCFA chain length (haslam2017theuniquerole pages 3-5, haslam2017theuniquerole pages 1-3, batsale2021biosynthesisandfunctions pages 5-6). This broad specificity allows ECR to participate in VLCFA elongation reactions throughout the plant, generating VLCFAs of diverse chain lengths that serve as precursors for multiple lipid classes including cuticular waxes, seed triacylglycerols, and sphingolipids (zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 2-3).

| Gene name / synonyms | Enzymatic function | Biochemical reaction | Substrate specificity | Cofactor | Key citations |
|---|---|---|---|---|---|
| **ECR = CER10 = AtECR = AOD2 = AtTSC13**; locus **At3g55360**; UniProt **Q9M2U2** | ER-associated **very-long-chain enoyl-CoA reductase** (**EC 1.3.1.93**) and terminal reductase of the microsomal fatty-acid elongase complex. Arabidopsis genetic complementation and rescue of a yeast *tsc13* elongase mutant support this assignment. | Reduces the trans-2,3 double bond of a VLC enoyl-CoA intermediate: **trans-2,3-enoyl-CoA + NADPH + H⁺ → saturated acyl-CoA + NADP⁺**. This is the fourth and final reaction in each elongation cycle, producing an acyl-CoA two carbons longer than the cycle’s starting primer. | Acts broadly on enoyl-CoA intermediates generated during VLCFA elongation; available evidence does **not** establish a narrow preference for one chain length. Chain-length selection is attributed mainly to the KCS condensing enzyme, whereas ECR, KCR, and HCD are shared generalist components. | **NADPH** is the expected physiological reducing cofactor. Plant ECR homologs contain a conserved NADP/NAD-binding motif, although detailed kinetic cofactor measurements for purified Arabidopsis ECR were not identified in the cited studies. | Functional identity and complementation (zheng2005disruptionsofthe pages 2-3, zheng2005disruptionsofthe pages 3-6); reaction and elongase position (haslam2017theuniquerole pages 1-3); broad specificity (zheng2005disruptionsofthe pages 8-9, haslam2017theuniquerole pages 3-5, batsale2021biosynthesisandfunctions pages 5-6); pathway outputs and AOD2 identity (zheng2005disruptionsofthe pages 2-3, zheng2005disruptionsofthe pages 3-6, fukuda2022eceriferum10encoding pages 1-2) |


*Table: Summary of the verified identity, catalytic reaction, substrate range, and cofactor usage of Arabidopsis ECR/CER10 (Q9M2U2). The evidence identifies ECR, CER10, AtECR, AOD2, and AtTSC13 as aliases of the same terminal reductase in very-long-chain fatty-acid elongation.*

## Subcellular Localization

ECR/CER10 is localized to the **endoplasmic reticulum (ER) membrane**, where it carries out its function in VLCFA elongation (zheng2005disruptionsofthe pages 9-12, zheng2005disruptionsofthe pages 2-3, zheng2005disruptionsofthe pages 3-6). This localization was demonstrated through GFP fusion studies showing that functional GFP-ECR labels a reticulate network characteristic of the ER, which was confirmed by co-staining with the ER marker hexyl rhodamine B (zheng2005disruptionsofthe pages 2-3). The protein is distributed relatively uniformly throughout the ER network, including the cortical ER and nuclear envelope, with similar fluorescence intensity across these regions (zheng2005disruptionsofthe pages 9-12, zheng2005disruptionsofthe pages 3-6). This contrasts with the yeast homolog Tsc13p, which is enriched in a specialized ER domain at the nuclear-vacuolar junction (zheng2005disruptionsofthe pages 9-12, zheng2005disruptionsofthe pages 8-9).

The ER localization is consistent with ECR's role in the ER-associated fatty acid elongase complex and places it at the site where VLCFA synthesis occurs for subsequent incorporation into various lipid classes (rowland2006cer4encodesan pages 8-9, zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 6-8).

## Role in Very-Long-Chain Fatty Acid Elongation Pathway

### The Fatty Acid Elongase Complex

ECR/CER10 functions as one of four core enzymatic activities in the membrane-bound fatty acid elongase (FAE) complex located in the ER (haslam2017theuniquerole pages 1-3). The four sequential reactions of each two-carbon elongation cycle are:

1. **Condensation**: KCS (3-ketoacyl-CoA synthase) condenses an acyl-CoA primer with malonyl-CoA to form β-ketoacyl-CoA
2. **First reduction**: KCR (β-ketoacyl-CoA reductase) reduces β-ketoacyl-CoA to β-hydroxyacyl-CoA
3. **Dehydration**: HCD (β-hydroxyacyl-CoA dehydratase) dehydrates β-hydroxyacyl-CoA to enoyl-CoA
4. **Second reduction**: ECR/CER10 reduces enoyl-CoA to saturated acyl-CoA (haslam2017theuniquerole pages 1-3, batsale2021biosynthesisandfunctions pages 5-6, haslam2017theuniquerole pages 3-5)

The newly elongated acyl-CoA can re-enter the cycle as a primer for additional two-carbon extensions, enabling repeated elongation to produce the range of VLCFAs found in plants (haslam2017theuniquerole pages 1-3, haslam2017theuniquerole pages 3-5). While the condensing enzyme (KCS) determines chain-length specificity and is the rate-limiting step, ECR, KCR, and HCD are shared "generalist" components with broad substrate specificities that function across all FAE complexes (haslam2017theuniquerole pages 1-3, batsale2021biosynthesisandfunctions pages 5-6, zheng2005disruptionsofthe pages 2-3).

### Integration with Other Elongase Components

ECR/CER10 works in concert with other elongase components, though the precise stoichiometry and physical architecture of the elongase complex remain incompletely defined (haslam2017theuniquerole pages 3-5). When expressed in yeast, Arabidopsis ECR physically interacted with yeast condensing enzymes Elo2p and Elo3p, supporting its integration into an elongase complex (zheng2005disruptionsofthe pages 1-2). Current models propose that multiple elongase systems may exist in Arabidopsis, with different combinations of KCS enzymes paired with shared core components including CER10, KCR1, and PAS2/HCD (haslam2017theuniquerole pages 3-5).

## Role in Cuticular Wax Biosynthesis

### Wax Precursor Production

ECR/CER10 is essential for cuticular wax biosynthesis by producing the VLCFA precursors required for wax component synthesis (zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 2-3, zheng2005disruptionsofthe pages 3-6). VLCFAs generated by the elongase complex, particularly those with 24-34 carbons, are subsequently processed through two major pathways: (1) the alcohol-forming pathway, producing primary alcohols and wax esters, and (2) the alkane-forming pathway, producing aldehydes, alkanes, secondary alcohols, and ketones (liu2020investigatingtheregulatory pages 21-26, liu2020investigatingtheregulatory pages 16-21).

### Mutant Phenotypes in Wax Production

Classical *cer10* mutants display a characteristic **glossy stem phenotype** due to reduced cuticular wax accumulation (zheng2005disruptionsofthe pages 3-6, zheng2005disruptionsofthe pages 1-2). Biochemical analyses revealed that *cer10-1* and *cer10-2* mutants contain approximately **60% less total stem cuticular wax** compared to wild-type plants, with proportional reductions across major wax components including primary alcohols, aldehydes, alkanes, secondary alcohols, and ketones (zheng2005disruptionsofthe pages 3-6, zheng2005disruptionsofthe pages 6-8).

More detailed compositional analysis of the *aod2* allele (which carries a CER10 defect) showed that while total wax content was not always dramatically reduced, there was a specific decrease in **very-long-chain components ≥C30**, particularly fatty acids, primary alcohols, and aldehydes longer than C28-C30, while C26 and C28 fatty acids accumulated (fukuda2022eceriferum10encoding pages 1-2, fukuda2022eceriferum10encoding pages 8-10). This suggests CER10/ECR is particularly important for extending fatty acid chains beyond C30 rather than simply controlling overall wax quantity.

The *aod2* mutant also showed a **dramatic reduction in epicuticular wax crystals** on stem surfaces, as visualized by scanning electron microscopy, and exhibited substantially greater toluidine blue uptake, indicating **increased cuticle permeability** (fukuda2022eceriferum10encoding pages 7-8, fukuda2022eceriferum10encoding pages 1-2). Detached *aod2* leaves shriveled more severely and lost water significantly faster than wild-type leaves, demonstrating impaired water retention due to the defective cuticular barrier (fukuda2022eceriferum10encoding pages 7-8).

## Role in Sphingolipid Metabolism and Membrane Organization

### Sphingolipid VLCFA Composition

Beyond its role in wax biosynthesis, ECR/CER10 supplies VLCFAs for **sphingolipid biosynthesis**, which is critical for proper membrane organization and function (zheng2005disruptionsofthe pages 12-13, zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 1-2). Loss of CER10 does not eliminate sphingolipids completely but causes a shift in their acyl-chain composition toward shorter species (zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 6-8). In *cer10-1* mutant plants, glucosylceramides contained 36.3% VLCFA-OH compared to 47.2% in wild-type Ler, with specific reductions in hydroxylated C26:0 and increases in hydroxylated C16:0 (zheng2005disruptionsofthe pages 8-9).

### Impact on Membrane Trafficking and Golgi Organization

The altered sphingolipid composition in *cer10* mutants disrupts membrane organization and function, particularly affecting **endocytic membrane trafficking** (zheng2005disruptionsofthe pages 12-13, zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 1-2). In *cer10* epidermal cells, Golgi stacks were enlarged and formed abnormal **ring-like clusters**, and the endocytic tracer FM4-64 accumulated in large clusters surrounded by Golgi stacks, indicating defective endocytic membrane organization (zheng2005disruptionsofthe pages 8-9). The mutant was also hypersensitive to brefeldin A, further supporting impaired membrane trafficking, although steady-state secretion to the apoplast remained relatively intact (zheng2005disruptionsofthe pages 8-9).

These trafficking defects are thought to result from disruption of sphingolipid-rich membrane microdomains or lipid rafts, which are important for protein trafficking, protein stability, endocytosis, and cell polarity (zheng2005disruptionsofthe pages 1-2, zheng2005disruptionsofthe pages 9-12). Because plant sphingolipids commonly contain C24-C26 VLCFAs, shortening these acyl chains disrupts the organization and function of these specialized membrane domains.

## Role in Cell Expansion and Plant Morphogenesis

### Developmental Phenotypes

*cer10* mutants exhibit **severe morphological abnormalities** affecting all aerial organs (zheng2005disruptionsofthe pages 3-6, zheng2005disruptionsofthe pages 1-2, zheng2005disruptionsofthe pages 2-3). These include small or crinkled leaves, downward-pointing cotyledons, reduced plant stature, zigzag-shaped stems, abnormal flowers, and partial male sterility due to shriveled, inviable pollen (zheng2005disruptionsofthe pages 1-2, zheng2005disruptionsofthe pages 2-3).

### Cellular Basis: Impaired Cell Expansion

The morphological defects primarily result from **defective cell expansion** rather than reduced cell number (zheng2005disruptionsofthe pages 3-6, zheng2005disruptionsofthe pages 9-12). Detailed cellular analysis revealed that leaf epidermal pavement cells in *cer10* mutants are approximately **three times smaller** than wild-type cells: an area containing 4-6 wild-type cells contained 13-15 mutant cells (zheng2005disruptionsofthe pages 3-6, zheng2005disruptionsofthe pages 9-12). Cell initiation proceeds normally, but both the direction and extent of expansion are compromised during early and late leaf development (zheng2005disruptionsofthe pages 6-8).

### Mechanistic Link to Sphingolipids

Tissue-specific RNA interference experiments demonstrated that **altered sphingolipid composition**, rather than wax or seed storage lipid deficiency alone, is the principal cause of the developmental phenotype (zheng2005disruptionsofthe pages 1-2, zheng2005disruptionsofthe pages 2-3). Epidermal-specific ECR silencing reduced cuticular wax without producing the characteristic *cer10* morphological defects, while the complete mutant's phenotype correlated with defective sphingolipid-dependent membrane trafficking (zheng2005disruptionsofthe pages 1-2). The impaired endocytic trafficking likely disrupts delivery and recycling of proteins and materials needed for cell-wall remodeling, pectin recycling, and correct localization of auxin transporters, all of which are essential for cell expansion (zheng2005disruptionsofthe pages 12-13).

| Biological Process | Role/Function | Mutant Phenotype | Supporting Evidence |
|---|---|---|---|
| Very-long-chain fatty-acid elongation | ER-localized ECR/CER10 catalyzes the terminal reduction of trans-2,3-enoyl-CoA to the corresponding saturated acyl-CoA in each elongation cycle. It supplies VLCFAs to several lipid pathways and acts as a broadly used elongase component; chain-length specificity is determined mainly by KCS enzymes. | Loss-of-function alleles reduce VLCFA incorporation into cuticular waxes, seed triacylglycerols, and sphingolipids, although residual elongation suggests partial compensation by other reductase-like activities. | Arabidopsis genetic disruption, yeast complementation, lipid profiling, and pathway analysis (zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 2-3, haslam2017theuniquerole pages 1-3) |
| Cuticular-wax biosynthesis and loading | Produces elongated acyl-CoA precursors for the alcohol-forming and alkane-forming wax pathways; normal CER10 activity supports wax composition and epicuticular crystal deposition. | Classical *cer10* mutants have glossy stems and approximately 60% less total stem wax. The *aod2* allele has fewer ≥C30 fatty acids and long-chain primary alcohols and aldehydes, markedly fewer stem wax crystals, increased cuticle permeability, and faster water loss from detached leaves. | Stem-wax chemical analysis, scanning electron microscopy, toluidine-blue permeability assays, and detached-leaf water-loss measurements (zheng2005disruptionsofthe pages 3-6, fukuda2022eceriferum10encoding pages 7-8, fukuda2022eceriferum10encoding pages 1-2, fukuda2022eceriferum10encoding pages 8-10) |
| Sphingolipid metabolism and membrane composition | Supplies VLCFAs—especially C24–C26 species—for sphingolipids that contribute to membrane packing, ordered domains, and membrane-protein organization. | Total sphingolipid abundance is not necessarily eliminated, but acyl-chain composition shifts toward shorter species. In one analysis, glucosylceramide VLCFA-OH content fell from 47.2% in wild type to 36.3% in *cer10-1*, with reduced 26:0-OH and increased 16:0-OH. | Sphingolipid and glucosylceramide profiling, supported by comparison with tissue-specific silencing lines (zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 6-8, zheng2005disruptionsofthe pages 1-2) |
| Cell expansion and organ morphogenesis | ECR-dependent VLCFA composition supports membrane and cell-wall trafficking processes needed for anisotropic cell expansion. Evidence favors altered sphingolipids, rather than wax or seed-storage-lipid deficiency alone, as the principal cause of the severe developmental phenotype. | Mutants develop small or crinkled leaves, downward-pointing cotyledons, reduced stature, zigzag stems, abnormal flowers and trichomes, and partial male sterility. Approximately 13–15 mutant epidermal cells occupy an area containing 4–6 wild-type cells, implying roughly threefold smaller cells. | Morphometric analysis, epidermal-cell imaging, tissue-specific RNA interference, and mutant complementation (zheng2005disruptionsofthe pages 3-6, zheng2005disruptionsofthe pages 1-2, zheng2005disruptionsofthe pages 9-12, zheng2005disruptionsofthe pages 2-3) |
| Endocytic membrane trafficking and Golgi organization | Appropriate VLCFA-containing sphingolipids help organize endosomal and Golgi membranes required for recycling plasma-membrane proteins and cell-wall material. | *cer10* cells show enlarged, ring-like Golgi clusters, abnormal accumulation of internalized FM4-64-labeled membranes, and hypersensitivity to brefeldin A. Bulk secretion to the apoplast remains comparatively intact, indicating a stronger defect in endocytosis or recycling. | Confocal imaging of Golgi and FM4-64 trafficking, brefeldin-A assays, and secretion analysis (zheng2005disruptionsofthe pages 12-13, zheng2005disruptionsofthe pages 8-9, zheng2005disruptionsofthe pages 9-12) |
| Osmotic and salt-stress tolerance | CER10/AOD2 promotes stress tolerance through long-chain wax production and loading, maintenance of the cuticular water barrier, and membrane-lipid homeostasis. Its contribution is not explained simply by canonical osmotic-marker-gene induction. | *aod2* is defective in salt-acclimation-induced acquired osmotolerance and is hypersensitive to acute osmotic and salt shock. Among four tested Col-0 wax mutants, *cer10* showed the strongest epidermal-wax loss and osmotic sensitivity. | Causal mapping to *At3g55360*, transgenic complementation, comparative wax-mutant assays, and stress-survival measurements (fukuda2022eceriferum10encoding pages 7-8, fukuda2022eceriferum10encoding pages 1-2, fukuda2022eceriferum10encoding pages 3-5, fukuda2022eceriferum10encoding pages 5-7) |
| ER-stress control under adverse conditions | By sustaining ER-based VLCFA synthesis and downstream membrane composition, CER10 limits maladaptive ER stress during osmotic challenge. | Under osmotic stress, *aod2* shows enhanced bZIP60-pathway activation, including elevated *SAR1A* and *SEC31A* expression; it also has reduced long-term heat tolerance. | Stress-responsive transcript analysis and osmotic- and heat-tolerance assays (fukuda2022eceriferum10encoding pages 7-8, fukuda2022eceriferum10encoding pages 1-2, fukuda2022eceriferum10encoding pages 8-10) |


*Table: This table summarizes the experimentally supported biological functions of Arabidopsis ECR/CER10 and the corresponding loss-of-function phenotypes. It distinguishes the enzyme’s primary VLCFA-elongation role from downstream effects on waxes, sphingolipids, development, membrane trafficking, and stress tolerance.*

## Role in Osmotic and Abiotic Stress Tolerance

### AOD2 (Acquired Osmotolerance-Defective 2) Function

A major recent discovery established that **CER10 is identical to AOD2**, a gene required for osmotic stress tolerance in Arabidopsis (fukuda2022eceriferum10encoding pages 7-8, fukuda2022eceriferum10encoding pages 1-2, fukuda2022eceriferum10encoding pages 3-5). The *aod2* mutant was isolated from an ion-beam-mutagenized population of the osmotolerant Bu-5 accession based on its acquired-osmotolerance-defective phenotype (fukuda2022eceriferum10encoding pages 1-2). Genetic mapping and complementation experiments demonstrated that disruption of At3g55360/CER10 is the causal lesion, and introduction of the wild-type CER10 gene restored osmotolerance (fukuda2022eceriferum10encoding pages 3-5, fukuda2022eceriferum10encoding pages 5-7).

### Stress Tolerance Phenotypes

Compared to the Bu-5 wild type, *aod2/cer10* mutants are defective in multiple stress responses:
- **Acquired osmotolerance**: Inability to develop osmotic stress tolerance after salt acclimation
- **Osmotic shock tolerance**: Hypersensitivity to acute high-sorbitol treatment
- **Salt shock tolerance**: Increased sensitivity to sudden salt stress
- **Long-term heat tolerance**: Reduced ability to withstand prolonged heat stress (fukuda2022eceriferum10encoding pages 1-2)

Among four Col-0 background cuticular wax-related mutants tested, **cer10 showed the strongest epidermal wax loss and the most severe osmosensitive phenotype**, distinguishing it from other wax biosynthesis mutants (fukuda2022eceriferum10encoding pages 7-8).

### Mechanisms of Stress Tolerance

The stress-tolerance defects in *aod2/cer10* appear to result from at least two interconnected mechanisms:

1. **Impaired cuticular barrier function**: The reduced accumulation of long-chain (≥C30) wax components compromises the protective water barrier, leading to increased water loss and reduced water retention capacity (fukuda2022eceriferum10encoding pages 7-8, fukuda2022eceriferum10encoding pages 8-10, fukuda2022eceriferum10encoding pages 5-7)

2. **Enhanced ER stress**: Under osmotic stress, *aod2* exhibits elevated expression of **bZIP60** and its target genes SAR1A and SEC31A, indicating enhanced endoplasmic reticulum stress (fukuda2022eceriferum10encoding pages 7-8). This may reflect the combined impact of defective VLCFA metabolism on both surface protection and membrane lipid homeostasis.

CER10 expression itself is induced by osmotic stress in wild-type plants, linking its activity to the stress response (fukuda2022eceriferum10encoding pages 5-7). The findings indicate that appropriate VLCFA elongation and cuticular wax chain-length composition contribute significantly to Arabidopsis osmotolerance, rather than CER10 acting solely through regulation of canonical stress-marker genes (fukuda2022eceriferum10encoding pages 3-5, fukuda2022eceriferum10encoding pages 5-7).

## Additional Biological Functions

### Seed Storage Lipids

ECR/CER10 also contributes VLCFAs to **seed triacylglycerols** (TAGs), with *cer10* mutants showing approximately 30% reduction in seed TAG VLCFA content (zheng2005disruptionsofthe pages 3-6). However, seed-specific silencing of ECR did not produce morphological defects, indicating that VLCFA incorporation into storage lipids is not critical for the developmental phenotype (zheng2005disruptionsofthe pages 1-2).

### Transcriptional Regulation

Recent work has identified CER10 as a direct target of drought- and ABA-responsive transcription factors. The transcription factor **MYB94**, which is induced by drought and abscisic acid, directly targets CER10 along with other wax biosynthetic genes including KCS2/DAISY, CER2, CER4, and WSD1 (lewandowska2020waxbiosynthesisin pages 4-6). This transcriptional regulation connects CER10 expression to environmental stress signaling pathways.

## Recent Research Developments (2020-2024)

| Year | Study / authors | Key findings | Plant species |
|---|---|---|---|
| 2020 | Kong et al., *Epigenetic Activation of Enoyl-CoA Reductase by an Acetyltransferase Complex Triggers Wheat Wax Biosynthesis* | Identified epigenetic activation of an ECR gene by a histone-acetyltransferase complex as a trigger for cuticular-wax biosynthesis, extending ECR regulation beyond the enzyme’s established catalytic role in VLCFA elongation. [DOI](https://doi.org/10.1104/pp.20.00603) | Bread wheat (*Triticum aestivum*) |
| 2020 | Lewandowska, Keyl & Feussner, review of stress-regulated wax biosynthesis | Placed Arabidopsis **CER10/ECR** among direct targets of the drought- and ABA-responsive transcription factor MYB94. The review reported that water deficit can increase Arabidopsis leaf wax as much as fourfold, primarily through VLC alkane accumulation, connecting transcriptional control of elongation genes with drought protection. [DOI](https://doi.org/10.1111/nph.16571) (lewandowska2020waxbiosynthesisin pages 4-6) | *Arabidopsis thaliana* and other plants |
| 2021 | Batsale et al., *Biosynthesis and Functions of Very-Long-Chain Fatty Acids in the Responses of Plants to Abiotic and Biotic Stresses* | Synthesized evidence that CER10 is the shared ECR component of the ER fatty-acid elongase complex, completing each two-carbon elongation cycle. It emphasized that KCS enzymes principally determine chain-length specificity, whereas ECR, KCR and HCD act as broadly shared catalytic components supplying VLCFAs to waxes, sphingolipids and storage lipids. [DOI](https://doi.org/10.3390/cells10061284) (batsale2021biosynthesisandfunctions pages 3-5, batsale2021biosynthesisandfunctions pages 5-6) | Primarily *Arabidopsis thaliana*; broader plant evidence |
| 2022 | Fukuda et al., *ECERIFERUM 10 Encoding an Enoyl-CoA Reductase Plays a Crucial Role in Osmotolerance and Cuticular Wax Loading in Arabidopsis* | Established that **AOD2 is CER10/ECR**. The mutant was defective in acquired osmotolerance, osmotic and salt shock tolerance, and long-term heat tolerance; it accumulated fewer ≥C30 fatty acids, primary alcohols and aldehydes, formed fewer epicuticular wax crystals, and showed enhanced bZIP60-mediated ER stress. [DOI](https://doi.org/10.3389/fpls.2022.898317) (fukuda2022eceriferum10encoding pages 1-2) | *Arabidopsis thaliana* |
| 2022 | Liu et al., *Ectopic Overexpression of CsECR From Navel Orange Increases Cuticular Wax Accumulation in Tomato and Enhances Its Tolerance to Drought Stress* | **CsECR** expression was induced by PEG and ABA. Heterologous overexpression increased total and aliphatic wax fractions in tomato leaves and fruits, reduced cuticle permeability, and enhanced drought tolerance, supporting ECR as an engineering target for crop surface-barrier traits. [DOI](https://doi.org/10.3389/fpls.2022.924552) (liu2022ectopicoverexpressionof pages 1-2) | Navel orange (*Citrus sinensis*); transgenic tomato (*Solanum lycopersicum*) |
| 2023 | Batsale et al., *Tackling Functional Redundancy of Arabidopsis Fatty Acid Elongase Complexes* | Used CRISPR-engineered yeast reconstitution and transient expression in *Nicotiana benthamiana* to resolve functional redundancy among Arabidopsis FAE complexes. The work reinforced the current model in which numerous KCS enzymes confer substrate and chain-length selectivity while ECR/CER10 is a shared terminal reductase; direct ECR complex stoichiometry remains unresolved. [DOI](https://doi.org/10.3389/fpls.2023.1107333) (haslam2017theuniquerole pages 1-3, haslam2017theuniquerole pages 3-5) | *Arabidopsis thaliana*, yeast, and *Nicotiana benthamiana* |
| 2024 | State of target-specific literature | No major 2024 primary study directly redefining Arabidopsis Q9M2U2/CER10 enzymology was identified in the searched literature. The best-supported target-specific advance therefore remains the 2022 AOD2 study, while 2023–2024 research largely addresses broader FAE architecture, wax regulation and stress adaptation rather than new CER10 substrate kinetics. (haslam2017theuniquerole pages 1-3, fukuda2022eceriferum10encoding pages 1-2) | Primarily *Arabidopsis thaliana* |


*Table: Recent developments connect ECR-mediated VLCFA elongation to wax deposition, membrane lipids, and abiotic-stress resilience. The table distinguishes direct Arabidopsis CER10 evidence from comparative and broader fatty-acid-elongase research.*

Recent research has expanded our understanding of ECR function across multiple plant species and contexts:

**2020**: Lewandowska et al. demonstrated that water deficit can increase Arabidopsis leaf wax up to fourfold, primarily through VLC alkane accumulation, and identified CER10 among the direct targets of the drought-responsive transcription factor MYB94 (lewandowska2020waxbiosynthesisin pages 4-6). Kong et al. discovered epigenetic activation of an ECR gene by a histone acetyltransferase complex in wheat, revealing additional layers of ECR regulation beyond transcriptional control.

**2021**: A comprehensive review by Batsale et al. synthesized evidence on VLCFA biosynthesis and functions in stress responses, emphasizing ECR/CER10's role as the shared terminal reductase of the FAE complex that supplies VLCFAs to waxes, sphingolipids, and storage lipids across diverse stress contexts (batsale2021biosynthesisandfunctions pages 3-5, batsale2021biosynthesisandfunctions pages 5-6).

**2022**: The landmark study by Fukuda et al. established the identity of AOD2 as CER10 and demonstrated its crucial role in osmotolerance through effects on cuticular wax loading, particularly long-chain components (≥C30), and its connection to ER stress pathways (fukuda2022eceriferum10encoding pages 1-2). Liu et al. showed that overexpression of a citrus ECR (CsECR) in tomato increased cuticular wax accumulation and enhanced drought tolerance, demonstrating the potential for ECR-based crop improvement (liu2022ectopicoverexpressionof pages 1-2).

**2023**: Batsale et al. used CRISPR-engineered yeast reconstitution systems to investigate functional redundancy among Arabidopsis FAE complexes, reinforcing the model that numerous KCS enzymes confer substrate specificity while ECR/CER10 serves as a shared terminal reductase (haslam2017theuniquerole pages 1-3, haslam2017theuniquerole pages 3-5).

These recent studies collectively demonstrate continued interest in ECR as a key regulator of plant surface properties, membrane composition, and abiotic stress adaptation, with potential applications in crop improvement.

## Summary

ECR/CER10/AOD2 (At3g55360, Q9M2U2) encodes a very-long-chain enoyl-CoA reductase localized to the endoplasmic reticulum that catalyzes the final reduction step in fatty acid elongation cycles. As a core component of the FAE complex, ECR exhibits broad substrate specificity and supplies VLCFAs for multiple essential biological processes. Its primary functions include: (1) cuticular wax biosynthesis, providing long-chain precursors that form the protective surface barrier; (2) sphingolipid metabolism, contributing VLCFAs essential for membrane organization, trafficking, and cell expansion; and (3) stress tolerance, particularly osmotic and drought stress, through effects on both cuticular protection and membrane lipid homeostasis. Loss-of-function mutants display reduced wax accumulation, severe morphological defects due to impaired cell expansion, altered membrane trafficking, and hypersensitivity to osmotic and other abiotic stresses. Recent research continues to validate ECR as a critical determinant of plant surface properties and stress resilience, with potential for crop improvement applications.

---

**URLs and Key Citations:**
- Zheng et al. 2005, *Plant Cell* 17:1467-1481 - Original characterization of CER10/ECR function (https://doi.org/10.1105/tpc.104.030155)
- Fukuda et al. 2022, *Front Plant Sci* 13:898317 - AOD2/CER10 identity and osmotolerance (https://doi.org/10.3389/fpls.2022.898317)
- Batsale et al. 2021, *Cells* 10:1284 - VLCFA functions in stress (https://doi.org/10.3390/cells10061284)
- Haslam et al. 2017, *Plants* 6:23 - ECR in elongase complex (https://doi.org/10.3390/plants6020023)
- Liu et al. 2022, *Front Plant Sci* 13:924552 - Citrus ECR and drought tolerance (https://doi.org/10.3389/fpls.2022.924552)

References

1. (zheng2005disruptionsofthe pages 2-3): Huanquan Zheng, Owen Rowland, and Ljerka Kunst. Disruptions of the arabidopsis enoyl-coa reductase gene reveal an essential role for very-long-chain fatty acid synthesis in cell expansion during plant morphogenesis. The Plant Cell Online, 17:1467-1481, May 2005. URL: https://doi.org/10.1105/tpc.104.030155, doi:10.1105/tpc.104.030155. This article has 398 citations.

2. (fukuda2022eceriferum10encoding pages 1-2): Norika Fukuda, Yoshimi Oshima, Hirotaka Ariga, Takuma Kajino, Takashi Koyama, Yukio Yaguchi, Keisuke Tanaka, Izumi Yotsui, Yoichi Sakata, and Teruaki Taji. Eceriferum 10 encoding an enoyl-coa reductase plays a crucial role in osmotolerance and cuticular wax loading in arabidopsis. Frontiers in Plant Science, Jun 2022. URL: https://doi.org/10.3389/fpls.2022.898317, doi:10.3389/fpls.2022.898317. This article has 17 citations.

3. (zheng2005disruptionsofthe pages 3-6): Huanquan Zheng, Owen Rowland, and Ljerka Kunst. Disruptions of the arabidopsis enoyl-coa reductase gene reveal an essential role for very-long-chain fatty acid synthesis in cell expansion during plant morphogenesis. The Plant Cell Online, 17:1467-1481, May 2005. URL: https://doi.org/10.1105/tpc.104.030155, doi:10.1105/tpc.104.030155. This article has 398 citations.

4. (zheng2005disruptionsofthe pages 8-9): Huanquan Zheng, Owen Rowland, and Ljerka Kunst. Disruptions of the arabidopsis enoyl-coa reductase gene reveal an essential role for very-long-chain fatty acid synthesis in cell expansion during plant morphogenesis. The Plant Cell Online, 17:1467-1481, May 2005. URL: https://doi.org/10.1105/tpc.104.030155, doi:10.1105/tpc.104.030155. This article has 398 citations.

5. (haslam2017theuniquerole pages 1-3): Tegan Haslam, Wesley Gerelle, Sean Graham, and Ljerka Kunst. The unique role of the eceriferum2-like clade of the bahd acyltransferase superfamily in cuticular wax metabolism. Plants, 6:23, Jun 2017. URL: https://doi.org/10.3390/plants6020023, doi:10.3390/plants6020023. This article has 59 citations.

6. (zheng2005disruptionsofthe pages 1-2): Huanquan Zheng, Owen Rowland, and Ljerka Kunst. Disruptions of the arabidopsis enoyl-coa reductase gene reveal an essential role for very-long-chain fatty acid synthesis in cell expansion during plant morphogenesis. The Plant Cell Online, 17:1467-1481, May 2005. URL: https://doi.org/10.1105/tpc.104.030155, doi:10.1105/tpc.104.030155. This article has 398 citations.

7. (haslam2017theuniquerole pages 3-5): Tegan Haslam, Wesley Gerelle, Sean Graham, and Ljerka Kunst. The unique role of the eceriferum2-like clade of the bahd acyltransferase superfamily in cuticular wax metabolism. Plants, 6:23, Jun 2017. URL: https://doi.org/10.3390/plants6020023, doi:10.3390/plants6020023. This article has 59 citations.

8. (liu2022ectopicoverexpressionof pages 1-2): Dechun Liu, Wenfang Guo, Xinyue Guo, Li Yang, Wei Hu, Liuqing Kuang, Yingjie Huang, Jingheng Xie, and Yong Liu. Ectopic overexpression of csecr from navel orange increases cuticular wax accumulation in tomato and enhances its tolerance to drought stress. Frontiers in Plant Science, Jul 2022. URL: https://doi.org/10.3389/fpls.2022.924552, doi:10.3389/fpls.2022.924552. This article has 26 citations.

9. (batsale2021biosynthesisandfunctions pages 5-6): Marguerite Batsale, Delphine Bahammou, Laetitia Fouillen, Sébastien Mongrand, Jérôme Joubès, and Frédéric Domergue. Biosynthesis and functions of very-long-chain fatty acids in the responses of plants to abiotic and biotic stresses. Cells, 10:1284, May 2021. URL: https://doi.org/10.3390/cells10061284, doi:10.3390/cells10061284. This article has 262 citations.

10. (zheng2005disruptionsofthe pages 9-12): Huanquan Zheng, Owen Rowland, and Ljerka Kunst. Disruptions of the arabidopsis enoyl-coa reductase gene reveal an essential role for very-long-chain fatty acid synthesis in cell expansion during plant morphogenesis. The Plant Cell Online, 17:1467-1481, May 2005. URL: https://doi.org/10.1105/tpc.104.030155, doi:10.1105/tpc.104.030155. This article has 398 citations.

11. (rowland2006cer4encodesan pages 8-9): Owen Rowland, Huanquan Zheng, Shelley R. Hepworth, Patricia Lam, Reinhard Jetter, and Ljerka Kunst. <i>cer4</i> encodes an alcohol-forming fatty acyl-coenzyme a reductase involved in cuticular wax production in arabidopsis. Sep 2006. URL: https://doi.org/10.1104/pp.106.086785, doi:10.1104/pp.106.086785. This article has 595 citations and is from a highest quality peer-reviewed journal.

12. (zheng2005disruptionsofthe pages 6-8): Huanquan Zheng, Owen Rowland, and Ljerka Kunst. Disruptions of the arabidopsis enoyl-coa reductase gene reveal an essential role for very-long-chain fatty acid synthesis in cell expansion during plant morphogenesis. The Plant Cell Online, 17:1467-1481, May 2005. URL: https://doi.org/10.1105/tpc.104.030155, doi:10.1105/tpc.104.030155. This article has 398 citations.

13. (liu2020investigatingtheregulatory pages 21-26): Shuang Liu. Investigating the regulatory mechanisms of cuticular wax biosynthesis in arabidopsis thaliana. ArXiv, Jan 2020. URL: https://doi.org/10.14288/1.0365829, doi:10.14288/1.0365829. This article has 0 citations.

14. (liu2020investigatingtheregulatory pages 16-21): Shuang Liu. Investigating the regulatory mechanisms of cuticular wax biosynthesis in arabidopsis thaliana. ArXiv, Jan 2020. URL: https://doi.org/10.14288/1.0365829, doi:10.14288/1.0365829. This article has 0 citations.

15. (fukuda2022eceriferum10encoding pages 8-10): Norika Fukuda, Yoshimi Oshima, Hirotaka Ariga, Takuma Kajino, Takashi Koyama, Yukio Yaguchi, Keisuke Tanaka, Izumi Yotsui, Yoichi Sakata, and Teruaki Taji. Eceriferum 10 encoding an enoyl-coa reductase plays a crucial role in osmotolerance and cuticular wax loading in arabidopsis. Frontiers in Plant Science, Jun 2022. URL: https://doi.org/10.3389/fpls.2022.898317, doi:10.3389/fpls.2022.898317. This article has 17 citations.

16. (fukuda2022eceriferum10encoding pages 7-8): Norika Fukuda, Yoshimi Oshima, Hirotaka Ariga, Takuma Kajino, Takashi Koyama, Yukio Yaguchi, Keisuke Tanaka, Izumi Yotsui, Yoichi Sakata, and Teruaki Taji. Eceriferum 10 encoding an enoyl-coa reductase plays a crucial role in osmotolerance and cuticular wax loading in arabidopsis. Frontiers in Plant Science, Jun 2022. URL: https://doi.org/10.3389/fpls.2022.898317, doi:10.3389/fpls.2022.898317. This article has 17 citations.

17. (zheng2005disruptionsofthe pages 12-13): Huanquan Zheng, Owen Rowland, and Ljerka Kunst. Disruptions of the arabidopsis enoyl-coa reductase gene reveal an essential role for very-long-chain fatty acid synthesis in cell expansion during plant morphogenesis. The Plant Cell Online, 17:1467-1481, May 2005. URL: https://doi.org/10.1105/tpc.104.030155, doi:10.1105/tpc.104.030155. This article has 398 citations.

18. (fukuda2022eceriferum10encoding pages 3-5): Norika Fukuda, Yoshimi Oshima, Hirotaka Ariga, Takuma Kajino, Takashi Koyama, Yukio Yaguchi, Keisuke Tanaka, Izumi Yotsui, Yoichi Sakata, and Teruaki Taji. Eceriferum 10 encoding an enoyl-coa reductase plays a crucial role in osmotolerance and cuticular wax loading in arabidopsis. Frontiers in Plant Science, Jun 2022. URL: https://doi.org/10.3389/fpls.2022.898317, doi:10.3389/fpls.2022.898317. This article has 17 citations.

19. (fukuda2022eceriferum10encoding pages 5-7): Norika Fukuda, Yoshimi Oshima, Hirotaka Ariga, Takuma Kajino, Takashi Koyama, Yukio Yaguchi, Keisuke Tanaka, Izumi Yotsui, Yoichi Sakata, and Teruaki Taji. Eceriferum 10 encoding an enoyl-coa reductase plays a crucial role in osmotolerance and cuticular wax loading in arabidopsis. Frontiers in Plant Science, Jun 2022. URL: https://doi.org/10.3389/fpls.2022.898317, doi:10.3389/fpls.2022.898317. This article has 17 citations.

20. (lewandowska2020waxbiosynthesisin pages 4-6): Milena Lewandowska, Alisa Keyl, and Ivo Feussner. Wax biosynthesis in response to danger: its regulation upon abiotic and biotic stress. New Phytologist, 227:698-713, May 2020. URL: https://doi.org/10.1111/nph.16571, doi:10.1111/nph.16571. This article has 455 citations and is from a highest quality peer-reviewed journal.

21. (batsale2021biosynthesisandfunctions pages 3-5): Marguerite Batsale, Delphine Bahammou, Laetitia Fouillen, Sébastien Mongrand, Jérôme Joubès, and Frédéric Domergue. Biosynthesis and functions of very-long-chain fatty acids in the responses of plants to abiotic and biotic stresses. Cells, 10:1284, May 2021. URL: https://doi.org/10.3390/cells10061284, doi:10.3390/cells10061284. This article has 262 citations.

## Artifacts

- [Edison artifact artifact-00](ECR-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](ECR-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](ECR-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. liu2022ectopicoverexpressionof pages 1-2
2. haslam2017theuniquerole pages 1-3
3. zheng2005disruptionsofthe pages 2-3
4. haslam2017theuniquerole pages 3-5
5. zheng2005disruptionsofthe pages 1-2
6. zheng2005disruptionsofthe pages 8-9
7. zheng2005disruptionsofthe pages 6-8
8. zheng2005disruptionsofthe pages 12-13
9. zheng2005disruptionsofthe pages 3-6
10. lewandowska2020waxbiosynthesisin pages 4-6
11. batsale2021biosynthesisandfunctions pages 5-6
12. zheng2005disruptionsofthe pages 9-12
13. liu2020investigatingtheregulatory pages 21-26
14. liu2020investigatingtheregulatory pages 16-21
15. batsale2021biosynthesisandfunctions pages 3-5
16. DOI
17. https://doi.org/10.1104/pp.20.00603
18. https://doi.org/10.1111/nph.16571
19. https://doi.org/10.3390/cells10061284
20. https://doi.org/10.3389/fpls.2022.898317
21. https://doi.org/10.3389/fpls.2022.924552
22. https://doi.org/10.3389/fpls.2023.1107333
23. https://doi.org/10.1105/tpc.104.030155
24. https://doi.org/10.3390/plants6020023
25. https://doi.org/10.1105/tpc.104.030155,
26. https://doi.org/10.3389/fpls.2022.898317,
27. https://doi.org/10.3390/plants6020023,
28. https://doi.org/10.3389/fpls.2022.924552,
29. https://doi.org/10.3390/cells10061284,
30. https://doi.org/10.1104/pp.106.086785,
31. https://doi.org/10.14288/1.0365829,
32. https://doi.org/10.1111/nph.16571,