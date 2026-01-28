---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T00:03:20.553561'
end_time: '2026-01-24T00:13:38.450038'
duration_seconds: 617.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TXN
  gene_symbol: TXN
  uniprot_accession: P10599
  protein_description: 'RecName: Full=Thioredoxin; Short=Trx; AltName: Full=ATL-derived
    factor; Short=ADF; AltName: Full=Surface-associated sulphydryl protein; Short=SASP;
    AltName: Allergen=Hom s Trx {ECO:0000305};'
  gene_info: Name=TXN; Synonyms=TRDX, TRX, TRX1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the thioredoxin family. .
  protein_domains: Thioredoxin. (IPR005746); Thioredoxin-like_sf. (IPR036249); Thioredoxin_CS.
    (IPR017937); Thioredoxin_domain. (IPR013766); Thioredoxin (PF00085)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P10599
- **Protein Description:** RecName: Full=Thioredoxin; Short=Trx; AltName: Full=ATL-derived factor; Short=ADF; AltName: Full=Surface-associated sulphydryl protein; Short=SASP; AltName: Allergen=Hom s Trx {ECO:0000305};
- **Gene Information:** Name=TXN; Synonyms=TRDX, TRX, TRX1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the thioredoxin family. .
- **Key Domains:** Thioredoxin. (IPR005746); Thioredoxin-like_sf. (IPR036249); Thioredoxin_CS. (IPR017937); Thioredoxin_domain. (IPR013766); Thioredoxin (PF00085)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TXN" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TXN' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TXN** (gene ID: TXN, UniProt: P10599) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Human Thioredoxin (TXN): A Comprehensive Functional Annotation Report

## 1. Introduction and Summary

Human thioredoxin (TXN, also known as TRX, TRX1, or TRDX) is a small (approximately 12 kDa), ubiquitous redox protein that plays central roles in cellular redox homeostasis, antioxidant defense, and signal transduction. Originally identified in *Escherichia coli* by Laurent et al. in 1964 as a hydrogen donor for ribonucleotide reductase, the human homolog was subsequently characterized and found to have expanded functions beyond its bacterial counterpart [holmgren-1985-thioredoxin-abstract]. Remarkably, human TXN was independently discovered as the "adult T cell leukemia-derived factor" (ADF), a secreted protein from HTLV-I-transformed T-cells with cytokine-like and chemokine-like activities, highlighting its multifunctional nature [leveillard-2017-extracellular-trx-abstract].

The primary biochemical function of thioredoxin is as a protein disulfide oxidoreductase (thiol-disulfide reductase), catalyzing the reduction of disulfide bonds in target proteins using electrons ultimately derived from NADPH via the thioredoxin reductase (TXNRD) system [lu-holmgren-2013-thioredoxin-antioxidant-abstract]. This enzymatic activity is mediated by the conserved Cys-Gly-Pro-Cys (CGPC) active site motif, which constitutes the hallmark of the thioredoxin family. The protein operates as part of the thioredoxin system—comprising NADPH, thioredoxin reductase (TXNRD1), and thioredoxin itself—which together with the glutathione-glutaredoxin system controls the cellular redox environment in mammalian cells [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

## 2. Catalytic Mechanism and Substrate Specificity

### 2.1 The Thioredoxin Fold and Active Site

The three-dimensional structure of thioredoxin, solved by both X-ray crystallography and NMR spectroscopy, reveals the canonical "thioredoxin fold" consisting of a central four-stranded β-sheet flanked by three α-helices [holmgren-1995-trx-structure-mechanism-abstract]. The redox-active site is located on a loop connecting a β-strand to an α-helix, positioning the two catalytic cysteine residues (Cys32 and Cys35 in human TXN) for optimal redox activity. This structural motif has been conserved across all domains of life and serves as the foundation for the thioredoxin superfamily, which includes protein disulfide isomerases, glutaredoxins, and numerous other thiol-disulfide oxidoreductases [fujimoto-2018-substrates-abstract].

### 2.2 Catalytic Mechanism

The catalytic mechanism of thioredoxin involves a two-step thiol-disulfide exchange reaction. In the first step, the more N-terminal cysteine (Cys32), which exists as a thiolate anion at physiological pH due to its unusually low pKa (~7.1), performs a nucleophilic attack on the disulfide bond of the target protein, forming a transient mixed disulfide intermediate. In the second step, the C-terminal cysteine (Cys35) attacks this mixed disulfide, releasing the reduced target protein and generating oxidized thioredoxin containing an intramolecular disulfide bond [holmgren-1995-trx-structure-mechanism-abstract].

High-resolution solution structures of human and *E. coli* thioredoxin in both oxidized and reduced states support this catalytic model, demonstrating conformational changes upon oxidation that are crucial for function [holmgren-1995-trx-structure-mechanism-abstract]. The oxidized thioredoxin is then regenerated to its reduced form by thioredoxin reductase (TXNRD1 in the cytosol) using electrons from NADPH [mustacich-powis-2000-txnrd-abstract].

### 2.3 Substrate Specificity

Thioredoxin exhibits broad substrate specificity, reducing disulfide bonds in numerous protein substrates. Key substrates include:

1. **Ribonucleotide reductase (RNR)**: Thioredoxin serves as the primary electron donor for RNR, the enzyme that catalyzes the rate-limiting step in DNA synthesis by converting ribonucleotides to deoxyribonucleotides. After each catalytic cycle, a disulfide bond forms at the RNR active site, which must be reduced by thioredoxin for continued activity [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

2. **Peroxiredoxins (Prxs)**: These thiol-dependent peroxidases use thioredoxin as their primary electron donor to reduce hydrogen peroxide, organic hydroperoxides, and peroxynitrite. The thioredoxin-peroxiredoxin system constitutes a major cellular defense against oxidative stress, with reaction rates that are extremely fast [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

3. **Methionine sulfoxide reductases (Msrs)**: Thioredoxin provides reducing equivalents to MsrA and MsrB, enzymes that repair oxidized methionine residues in proteins, thereby contributing to protein repair mechanisms [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

4. **Transcription factors**: Multiple redox-sensitive transcription factors including NF-κB, AP-1, p53, HIF-1α, and others contain critical cysteine residues in their DNA-binding domains that must be reduced for DNA binding activity. Thioredoxin directly or indirectly reduces these cysteines to regulate transcription factor activity [sen-packer-1996-redox-regulation-abstract].

## 3. Subcellular Localization

### 3.1 Cytoplasmic and Nuclear Distribution

Human thioredoxin-1 (TXN) is predominantly a cytoplasmic protein under basal conditions, but it translocates to the nucleus in response to various stimuli including oxidative stress, cell density changes, and growth factor stimulation [spielberger-2008-trx-localization-abstract]. Studies have demonstrated that the subcellular distribution of thioredoxin is dynamic and influenced by the cellular redox environment. In sparse cell cultures with higher reactive oxygen species (ROS) levels, thioredoxin-1 is predominantly nuclear, whereas in confluent cultures it is predominantly cytoplasmic [spielberger-2008-trx-localization-abstract].

The nuclear localization of thioredoxin is functionally significant, as it enables the reduction of redox-sensitive transcription factors. Research has shown that the redox state of key transcription factors like NF-κB differs between the cytoplasm and nucleus: the critical cysteine residue (Cys-62 of p50) is highly oxidized in the cytoplasm and must be converted to a reduced form in the nucleus to enable DNA binding [ando-2008-ape1-ref1-abstract]. Thioredoxin, together with APE1/Ref-1, mediates this nuclear reduction and activation.

### 3.2 Mitochondrial Thioredoxin

Mammalian cells possess a separate mitochondrial thioredoxin system, consisting of thioredoxin-2 (TXN2) and mitochondrial thioredoxin reductase (TXNRD2). This compartmentalized system is critical for mitochondrial redox homeostasis and protection against oxidative stress. Thioredoxin-2 has been identified as a critical regulator of cytochrome c release and mitochondrial apoptosis [masutani-2005-trx-apoptosis-abstract].

### 3.3 Extracellular Secretion

A striking feature of human thioredoxin is its secretion from cells despite lacking a classical N-terminal signal peptide. Human TXN was originally discovered as a secreted protein (ADF) from HTLV-I-transformed T-cells [leveillard-2017-extracellular-trx-abstract]. Thioredoxin secretion is induced by various stimuli including oxidative stress and cytokine stimulation. The secretion mechanism remains incompletely understood but is classified as unconventional protein secretion [leveillard-2017-extracellular-trx-abstract].

Extracellular thioredoxin exhibits cytokine-like and chemokine-like activities. A complete extracellular thioredoxin system exists in blood, with circulating TXN1 and TXNRD1 detected in plasma. However, the source of extracellular NADPH required for thioredoxin recycling remains mysterious. In the absence of regenerative capacity, extracellular thioredoxins may paradoxically act as pro-oxidant rather than antioxidant agents [leveillard-2017-extracellular-trx-abstract].

TRX80, an 80-amino acid N-terminal truncated form of thioredoxin-1, is generated by cleavage via ADAM10 and ADAM17 metalloproteinases in monocytes. TRX80 has distinct biological activities from full-length thioredoxin, acting as a cytokine for monocytes, promoting proinflammatory macrophage phenotype, and activating complement pathways [leveillard-2017-extracellular-trx-abstract].

## 4. Signaling Pathways and Transcription Factor Regulation

### 4.1 The Thioredoxin-APE1/Ref-1 Redox Signaling Pathway

One of the most important functions of thioredoxin is the regulation of redox-sensitive transcription factors. At least two major transcription factors, NF-κB and AP-1, have been identified as regulated by the intracellular redox state, with thioredoxin playing a central role [sen-packer-1996-redox-regulation-abstract].

The multifunctional protein APE1/Ref-1 (apurinic/apyrimidinic endonuclease 1/redox factor 1) cooperates with thioredoxin in this regulatory pathway. APE1/Ref-1 not only directly reduces target transcription factors but also facilitates their reduction by other reducing molecules including glutathione and thioredoxin—a function termed "redox chaperone activity" [ando-2008-ape1-ref1-abstract]. This redox chaperone activity operates at significantly lower concentrations than required for direct redox activity and is independent of APE1/Ref-1's own cysteine residues, suggesting a conformational facilitation mechanism.

### 4.2 NF-κB Regulation

NF-κB is a critical transcription factor regulating immune responses, inflammation, and cell survival. The redox-sensitive cysteine residue Cys-62 in the p50 subunit of NF-κB must be reduced for efficient DNA binding. Thioredoxin, working with APE1/Ref-1, reduces this cysteine in the nucleus to enable transcriptional activation [ando-2008-ape1-ref1-abstract][hirota-2000-nucleoredoxin-abstract].

Interestingly, thioredoxin, glutaredoxin, and nucleoredoxin differentially regulate NF-κB, AP-1, and CREB activation in cells. These redox molecules have distinct subcellular localizations and differentially modulate transcription factor activation induced by TNFα, PMA, and other stimuli [hirota-2000-nucleoredoxin-abstract].

### 4.3 AP-1 Regulation

The transcription factor AP-1 (composed of c-Fos and c-Jun heterodimers) is regulated by thioredoxin through reduction of conserved cysteine residues in the basic leucine zipper (bZIP) DNA-binding domains (Cys-272 of c-Fos and Cys-154 of c-Jun). APE1/Ref-1 promotes the reduction of both c-Fos and c-Jun bZIP domains by thioredoxin or glutathione, facilitating AP-1 DNA binding activity [ando-2008-ape1-ref1-abstract].

### 4.4 Other Transcription Factors

Thioredoxin also regulates the activity of numerous other transcription factors including:
- **p53**: The tumor suppressor p53 requires reduced cysteine residues for DNA binding; thioredoxin maintains p53 in its active reduced state
- **HIF-1α**: Hypoxia-inducible factor 1α, critical for oxygen sensing and angiogenesis
- **Pax proteins**: Paired box transcription factors important in development
- **Egr-1**: Early growth response factor involved in cell proliferation
- **STAT3**: Signal transducer and activator of transcription 3

[thakur-2014-ape1-ref1-abstract]

### 4.5 ASK1-Thioredoxin Interaction and Apoptosis Signaling

A critical signaling pathway involving thioredoxin is its interaction with apoptosis signal-regulating kinase 1 (ASK1), a MAP kinase kinase kinase that lies upstream of JNK and p38 MAPK pathways leading to apoptosis. Reduced thioredoxin binds directly to ASK1 and inhibits its kinase activity. Upon oxidative stress, thioredoxin becomes oxidized and dissociates from ASK1, allowing ASK1 activation and downstream apoptotic signaling [masutani-2005-trx-apoptosis-abstract].

Research has demonstrated that cell exposure to H₂O₂ causes rapid oxidation of ASK1, leading to its multimerization through interchain disulfide bonds. During the subsequent reduction phase, thioredoxin-1 becomes covalently associated with ASK1 to restore its reduced monomeric state. Overexpression of thioredoxin accelerates ASK1 reduction and impairs JNK activation and apoptosis [nadeau-2007-ask1-trx-abstract]. This establishes thioredoxin as a sensor of oxidative stress that modulates the apoptotic threshold.

### 4.6 TXNIP Interaction

Thioredoxin-interacting protein (TXNIP, also known as TBP-2 or vitamin D₃ upregulated protein 1/VDUP1) is a negative regulator of thioredoxin. TXNIP binds to reduced thioredoxin and inhibits its reducing activity. The TXNIP-thioredoxin interaction has been implicated in metabolic regulation, including glucose and lipid metabolism, and in tumor suppression [lillig-holmgren-2007-trx-related-molecules-abstract].

## 5. The Thioredoxin System as an Antioxidant Defense

### 5.1 The Complete Thioredoxin System

The mammalian thioredoxin system consists of three components: NADPH (the ultimate electron donor), thioredoxin reductase (TXNRD), and thioredoxin itself. NADPH is generated primarily through the pentose phosphate pathway, linking thioredoxin function to glucose metabolism [leveillard-2017-extracellular-trx-abstract].

Mammalian thioredoxin reductases (TXNRD1, TXNRD2, and TXNRD3) are distinct from bacterial enzymes in that they are high molecular weight selenoenzymes containing an essential selenocysteine residue at the C-terminus [mustacich-powis-2000-txnrd-abstract]. The selenocysteine-containing C-terminal motif (-Cys-SeCys-) provides mammalian thioredoxin reductases with broader substrate specificity compared to their bacterial counterparts.

### 5.2 Crosstalk with Glutathione System

The thioredoxin and glutathione systems were traditionally viewed as parallel but independent antioxidant pathways. However, recent research has revealed significant crosstalk between these systems, with each capable of serving as a backup for the other under conditions of impairment [lu-holmgren-2013-thioredoxin-antioxidant-abstract]. Glutaredoxins can accept electrons from glutathione and reduce some overlapping substrates with thioredoxin.

### 5.3 Peroxiredoxin Reduction

A major antioxidant function of thioredoxin is providing electrons to peroxiredoxins (Prxs), a family of thiol-dependent peroxidases that catalyze the reduction of H₂O₂, organic hydroperoxides, and peroxynitrite. The thioredoxin-peroxiredoxin system represents a highly efficient mechanism for hydrogen peroxide removal, with extremely fast reaction rates [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

## 6. Structure-Function Relationships

### 6.1 The Thioredoxin Fold

The thioredoxin fold represents one of the most ancient and conserved protein structural motifs, found across all domains of life. The core structure consists of a central four-stranded β-sheet flanked by α-helices, with the redox-active CXXC motif positioned at the N-terminus of an α-helix [fujimoto-2018-substrates-abstract].

The thioredoxin superfamily encompasses numerous proteins sharing this fold, including:
- Thioredoxins (cytosolic, mitochondrial)
- Glutaredoxins
- Protein disulfide isomerases
- Glutathione peroxidases (some family members)
- Peroxiredoxins

### 6.2 Active Site Properties and the CXXC Rheostat

The catalytic cysteines in human thioredoxin (Cys32-Gly-Pro-Cys35) exhibit distinct chemical properties. The N-terminal Cys32 has a low pKa (~7.1) due to its local environment, existing predominantly as the reactive thiolate anion at physiological pH. This nucleophilic thiolate initiates the catalytic cycle by attacking substrate disulfides. The proline residue creates a characteristic kink in the active site loop, and glycine provides conformational flexibility [holmgren-1995-trx-structure-mechanism-abstract].

The CXXC motif functions as a biochemical "rheostat" that determines the reduction potential of thiol-disulfide oxidoreductases [chivers-1997-cxxc-motif-abstract]. The identity of the XX dipeptide between the two catalytic cysteines profoundly affects the redox properties: the pKa of the N-terminal cysteine correlates with the reduction potential, such that lower pKa values make the disulfide bond easier to reduce. However, formal analysis of the Nernst equation reveals that reduction potential contains both pH-dependent and pH-independent components. The differences in reduction potential between thioredoxin (CGPC, approximately -270 mV) and other thiol-disulfide oxidoreductases like DsbA (CPHC, approximately -120 mV) cannot be explained solely by thiol pKa values, indicating that additional structural factors contribute to tuning the redox potential [chivers-1997-cxxc-motif-abstract]. These intricacies enable the thioredoxin superfamily to span a wide range of reduction potentials and thereby serve diverse biochemical roles.

## 7. Genetic Evidence for Essential Functions

The essential nature of thioredoxin has been demonstrated through genetic studies in model organisms. Global deletion of thioredoxin-1 in mice results in embryonic lethality, underscoring its essential role in development. To circumvent this lethality, tissue-specific knockout models have been generated that provide critical insights into thioredoxin function in specific organs.

Cardiac-specific thioredoxin-1 knockout (Trx1cKO) mice were viable at birth but died with a median survival age of only 25.5 days [oka-2020-trx1-knockout-heart-abstract]. These mice developed severe heart failure characterized by contractile dysfunction, hypertrophy, increased fibrosis, and apoptotic cell death. RNA-sequencing revealed marked downregulation of genes involved in energy production, and mitochondrial morphological abnormalities were evident. Even heterozygous cardiac Trx1 knockout mice, while viable at baseline, showed exacerbated cardiac dysfunction under pressure-overload stress, demonstrating haploinsufficiency under stress conditions.

Mechanistically, this study revealed that thioredoxin-1 regulates the mechanistic target of rapamycin (mTOR) through reduction of Cys1483. In Trx1cKO hearts, mTOR was more oxidized, and phosphorylation of mTOR substrates (S6K and 4EBP1) was impaired. An oxidation-resistant mTOR mutant (C1483F) prevented the metabolic gene suppression caused by thioredoxin knockdown, directly demonstrating that thioredoxin maintains mTOR function through redox regulation [oka-2020-trx1-knockout-heart-abstract]. These findings establish that endogenous thioredoxin is essential for maintaining cardiac function and metabolism through mTOR-mediated regulation of mitochondrial gene expression.

## 8. Implications for Disease and Therapeutic Applications

Thioredoxin has been implicated in numerous disease contexts:

1. **Cancer**: Thioredoxin and thioredoxin reductase are often overexpressed in tumors, contributing to tumor cell survival under oxidative stress and resistance to chemotherapy. Thioredoxin inhibition represents a potential therapeutic strategy [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

2. **Infectious Diseases**: The distinct structural features of mammalian versus bacterial thioredoxin reductases offer opportunities for selective targeting of pathogenic bacteria [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

3. **Cardiovascular Disease**: Extracellular thioredoxin levels serve as biomarkers for oxidative stress and inflammation in various conditions including acute lung injury [lu-holmgren-2013-thioredoxin-antioxidant-abstract].

4. **Neurodegeneration**: The thioredoxin system plays protective roles against oxidative damage in neurons.

## 9. Open Questions

Despite extensive research on thioredoxin over several decades, several important questions remain:

1. **Secretion Mechanism**: The unconventional secretion pathway for thioredoxin remains poorly understood. How does this cytosolic protein without a signal peptide reach the extracellular space?

2. **Extracellular NADPH**: The source of extracellular NADPH required for regeneration of secreted thioredoxin remains mysterious. In its absence, what determines whether extracellular thioredoxin acts as a reductant or oxidant?

3. **Substrate Selectivity Determinants**: What structural features beyond the CXXC motif and thioredoxin fold determine the specificity of thioredoxin for particular protein substrates?

4. **Nuclear Import Mechanism**: The mechanism by which thioredoxin translocates to the nucleus in response to oxidative stress requires further characterization.

5. **TRX80 Signaling**: The receptors and signaling pathways mediating the cytokine-like activities of TRX80 remain incompletely characterized.

6. **Tissue-Specific Functions**: How does thioredoxin function differ across different tissues and cell types, and what accounts for these differences?

7. **Therapeutic Window**: Can thioredoxin or thioredoxin reductase be selectively targeted in disease states without disrupting essential cellular functions?

## 10. References

* **holmgren-1985-thioredoxin-abstract**: Holmgren A. Thioredoxin. Annu Rev Biochem. 1985;54:237-71. PMID: 3896121. DOI: [10.1146/annurev.bi.54.070185.001321](https://doi.org/10.1146/annurev.bi.54.070185.001321)

* **lu-holmgren-2013-thioredoxin-antioxidant-abstract**: Lu J, Holmgren A. The thioredoxin antioxidant system. Free Radic Biol Med. 2013;66:75-87. PMID: 23899494. DOI: [10.1016/j.freeradbiomed.2013.07.036](https://doi.org/10.1016/j.freeradbiomed.2013.07.036)

* **holmgren-1995-trx-structure-mechanism-abstract**: Holmgren A. Thioredoxin structure and mechanism: conformational changes on oxidation of the active-site sulfhydryls to a disulfide. Structure. 1995;3(3):239-43. PMID: 7788289. DOI: [10.1016/s0969-2126(01)00153-8](https://doi.org/10.1016/s0969-2126(01)00153-8)

* **mustacich-powis-2000-txnrd-abstract**: Mustacich D, Powis G. Thioredoxin reductase. Biochem J. 2000;346 Pt 1:1-8. PMID: 10657232. PMC: PMC1220815.

* **sen-packer-1996-redox-regulation-abstract**: Sen CK, Packer L. Antioxidant and redox regulation of gene transcription. FASEB J. 1996;10(7):709-20. PMID: 8635688. DOI: [10.1096/fasebj.10.7.8635688](https://doi.org/10.1096/fasebj.10.7.8635688)

* **hirota-2000-nucleoredoxin-abstract**: Hirota K, et al. Nucleoredoxin, glutaredoxin, and thioredoxin differentially regulate NF-kappaB, AP-1, and CREB activation in HEK293 cells. Biochem Biophys Res Commun. 2000;274(1):177-82. PMID: 10903915. DOI: [10.1006/bbrc.2000.3106](https://doi.org/10.1006/bbrc.2000.3106)

* **leveillard-2017-extracellular-trx-abstract**: Léveillard T, Aït-Ali N. Cell Signaling with Extracellular Thioredoxin and Thioredoxin-Like Proteins: Insight into Their Mechanisms of Action. Oxid Med Cell Longev. 2017;2017:8475125. PMID: 29138681. PMC: PMC5613632. DOI: [10.1155/2017/8475125](https://doi.org/10.1155/2017/8475125)

* **ando-2008-ape1-ref1-abstract**: Ando K, et al. A new APE1/Ref-1-dependent pathway leading to reduction of NF-kappaB and AP-1, and activation of their DNA-binding activity. Nucleic Acids Res. 2008;36(13):4327-36. PMID: 18586825. PMC: PMC2490748. DOI: [10.1093/nar/gkn416](https://doi.org/10.1093/nar/gkn416)

* **nadeau-2007-ask1-trx-abstract**: Nadeau PJ, et al. Disulfide Bond-mediated multimerization of Ask1 and its reduction by thioredoxin-1 regulate H(2)O(2)-induced c-Jun NH(2)-terminal kinase activation and apoptosis. Mol Biol Cell. 2007;18(10):3903-13. PMID: 17652454. PMC: PMC1995733. DOI: [10.1091/mbc.e07-05-0491](https://doi.org/10.1091/mbc.e07-05-0491)

* **masutani-2005-trx-apoptosis-abstract**: Masutani H, et al. The thioredoxin system in retroviral infection and apoptosis. Cell Death Differ. 2005;12 Suppl 1:991-8. PMID: 15818395. DOI: [10.1038/sj.cdd.4401625](https://doi.org/10.1038/sj.cdd.4401625)

* **spielberger-2008-trx-localization-abstract**: Spielberger JC, et al. Oxidation and nuclear localization of thioredoxin-1 in sparse cell cultures. J Cell Biochem. 2008;104(5):1879-89. PMID: 18384140. DOI: [10.1002/jcb.21762](https://doi.org/10.1002/jcb.21762)

* **lillig-holmgren-2007-trx-related-molecules-abstract**: Lillig CH, Holmgren A. Thioredoxin and related molecules--from biology to health and disease. Antioxid Redox Signal. 2007;9(1):25-47. PMID: 17115886. DOI: [10.1089/ars.2007.9.25](https://doi.org/10.1089/ars.2007.9.25)

* **hirota-2002-trx-superfamily-abstract**: Hirota K, et al. Thioredoxin superfamily and thioredoxin-inducing agents. Ann N Y Acad Sci. 2002;957:189-99. PMID: 12074972. DOI: [10.1111/j.1749-6632.2002.tb02916.x](https://doi.org/10.1111/j.1749-6632.2002.tb02916.x)

* **fujimoto-2018-substrates-abstract**: Fujimoto T, et al. Methods to identify the substrates of thiol-disulfide oxidoreductases. Protein Sci. 2018;28(1):30-40. PMID: 30341785. PMC: PMC6295885. DOI: [10.1002/pro.3530](https://doi.org/10.1002/pro.3530)

* **thakur-2014-ape1-ref1-abstract**: Thakur S, et al. APE1/Ref-1 as an emerging therapeutic target for various human diseases: phytochemical modulation of its functions. Exp Mol Med. 2014;46(7):e106. PMID: 25033834. PMC: PMC4119211. DOI: [10.1038/emm.2014.42](https://doi.org/10.1038/emm.2014.42)

* **oka-2020-trx1-knockout-heart-abstract**: Oka SI, et al. Thioredoxin-1 maintains mitochondrial function via mechanistic target of rapamycin signalling in the heart. Cardiovasc Res. 2020;116(10):1742-1755. PMID: 31584633. PMC: PMC7825501. DOI: [10.1093/cvr/cvz251](https://doi.org/10.1093/cvr/cvz251)

* **chivers-1997-cxxc-motif-abstract**: Chivers PT, Prehoda KE, Raines RT. The CXXC motif: a rheostat in the active site. Biochemistry. 1997;36(14):4061-6. PMID: 9099998. DOI: [10.1021/bi9628580](https://doi.org/10.1021/bi9628580)


## Citations

1. ando-2008-ape1-ref1-abstract.md
2. chivers-1997-cxxc-motif-abstract.md
3. fujimoto-2018-substrates-abstract.md
4. hirota-2000-nucleoredoxin-abstract.md
5. hirota-2002-trx-superfamily-abstract.md
6. holmgren-1985-thioredoxin-abstract.md
7. holmgren-1995-trx-structure-mechanism-abstract.md
8. leveillard-2017-extracellular-trx-abstract.md
9. lillig-holmgren-2007-trx-related-molecules-abstract.md
10. lu-holmgren-2013-thioredoxin-antioxidant-abstract.md
11. masutani-2005-trx-apoptosis-abstract.md
12. mustacich-powis-2000-txnrd-abstract.md
13. nadeau-2007-ask1-trx-abstract.md
14. oka-2020-trx1-knockout-heart-abstract.md
15. sen-packer-1996-redox-regulation-abstract.md
16. spielberger-2008-trx-localization-abstract.md
17. thakur-2014-ape1-ref1-abstract.md