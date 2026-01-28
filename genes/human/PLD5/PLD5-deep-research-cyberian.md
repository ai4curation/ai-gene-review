---
provider: cyberian
model: deep-research
cached: true
start_time: '2026-01-23T16:52:57.236229'
end_time: '2026-01-23T16:52:57.237794'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PLD5
  gene_symbol: PLD5
  uniprot_accession: Q8N7P1
  protein_description: 'RecName: Full=Inactive phospholipase D5; Short=Inactive PLD
    5; AltName: Full=Inactive choline phosphatase 5; AltName: Full=Inactive phosphatidylcholine-hydrolyzing
    phospholipase D5; AltName: Full=PLDc;'
  gene_info: Name=PLD5;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the phospholipase D family. .
  protein_domains: Diverse_PLD-related. (IPR050874); PLDc_3. (IPR032803); PLipase_D/transphosphatidylase.
    (IPR001736); PLDc_3 (PF13918)
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
- **UniProt Accession:** Q8N7P1
- **Protein Description:** RecName: Full=Inactive phospholipase D5; Short=Inactive PLD 5; AltName: Full=Inactive choline phosphatase 5; AltName: Full=Inactive phosphatidylcholine-hydrolyzing phospholipase D5; AltName: Full=PLDc;
- **Gene Information:** Name=PLD5;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the phospholipase D family. .
- **Key Domains:** Diverse_PLD-related. (IPR050874); PLDc_3. (IPR032803); PLipase_D/transphosphatidylase. (IPR001736); PLDc_3 (PF13918)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PLD5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PLD5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PLD5** (gene ID: PLD5, UniProt: Q8N7P1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PLD5 (Phospholipase D Family Member 5): A Comprehensive Review

## Introduction and Summary

Phospholipase D family member 5 (PLD5), encoded by the PLD5 gene located on human chromosome 1q43, represents an enigmatic member of the phospholipase D superfamily. Despite its classification within a family of enzymes that typically catalyze the hydrolysis of phosphatidylcholine to phosphatidic acid and choline, PLD5 is designated as an "inactive" phospholipase due to nonconservative substitutions in its putative catalytic site that render it very unlikely to possess canonical phospholipase D enzymatic activity [stutchfield-2015-pld-roles-abstract]. The protein is alternatively known as Inactive phospholipase D5, Inactive PLD 5, Inactive choline phosphatase 5, and PLDc [ncbi-gene-200150-summary]. Definitive cellular and physiological roles for PLD5 have not yet been established, making it one of the least characterized members of the mammalian PLD family [stutchfield-2015-pld-roles-abstract].

The PLD5 gene spans approximately 450 kilobases on chromosome 1q43 (coordinates 242,082,986–242,530,546 on the complement strand of GRCh38.p14) and contains 21 exons that give rise to at least four validated transcript isoforms [ncbi-gene-200150-summary]. The encoded protein contains two putative catalytic domain repeats characteristic of the phospholipase D superfamily (PLDc_vPLD5_1 and PLDc_vPLD5_2), yet lacks the phosphatidylinositol-binding PX (phox homology) and PH (pleckstrin homology) domains that are essential for the membrane interactions and regulatory functions of the catalytically active classical PLDs, PLD1 and PLD2 [becconcino-2014-pld-signaling-abstract].

## The Phospholipase D Family Context

Understanding PLD5 requires placing it within the broader context of the phospholipase D superfamily. In mammals, six PLD isoforms have been identified (PLD1 through PLD6), which can be classified into "classical" and "non-classical" categories based on their domain architecture and enzymatic activities [becconcino-2014-pld-signaling-abstract]. The classical PLDs, PLD1 and PLD2, share approximately 57% amino acid conservation and possess the full complement of regulatory domains including tandem PX and PH domains that govern membrane localization and activity regulation, along with two HKD catalytic motifs that combine to form a functional active site [stutchfield-2015-pld-roles-abstract]. These enzymes catalyze the hydrolysis of phosphatidylcholine to generate phosphatidic acid, a bioactive lipid second messenger with diverse downstream signaling effects, and choline, the precursor for the neurotransmitter acetylcholine.

The non-classical PLDs (PLD3, PLD4, PLD5, and PLD6) all lack the PX and PH domains characteristic of the classical isoforms [becconcino-2014-pld-signaling-abstract]. PLD3, PLD4, and PLD5 retain two HKD motifs, while PLD6 (also known as MitoPLD) possesses only one. Among the mammalian PLD isoforms, only PLD1, PLD2, and PLD6 have been demonstrated to possess lipase activity [becconcino-2014-pld-signaling-abstract]. The lack of lipase activity in PLD3 and PLD4 cannot be attributed solely to the absence of PX and PH domains, since PLD6 also lacks these domains yet remains enzymatically active upon dimerization.

A paradigm-shifting discovery revealed that PLD3 and PLD4, despite their classification as phospholipases, actually function as 5' exonucleases that degrade single-stranded DNA in the acidic environment of endolysosomes [gavin-2018-pld3-pld4-exonuclease-abstract]. These enzymes regulate Toll-like receptor 9 (TLR9) signaling by degrading its nucleic acid ligands, and loss of function leads to autoinflammatory disease in mice [gavin-2018-pld3-pld4-exonuclease-abstract]. This functional repurposing within the PLD superfamily raises important questions about whether PLD5 might similarly possess an unexpected enzymatic activity unrelated to phospholipid hydrolysis.

## Structural Features and Catalytic Inactivity

The defining characteristic of PLD5 is its predicted lack of phospholipase D enzymatic activity. The PLD5 protein consists of 506 amino acids and contains two putative PLDc catalytic domains [zhang-2024-pld-neurodegenerative-abstract]. Sequence analysis has revealed that PLD5 contains nonconservative substitutions in its putative catalytic site that make it very unlikely to be enzymatically active as a phospholipase [stutchfield-2015-pld-roles-abstract]. Specifically, PLD5 lacks critical residues including the first catalytic motif's histidine and the second motif's histidine that are essential for the catalytic mechanism [zhang-2024-pld-neurodegenerative-abstract]. The HKD motif (HxKx4D), which forms the catalytic core of active PLDs, is not well conserved in PLD5 compared to its paralogues [becconcino-2014-pld-signaling-abstract].

Structural studies of PLD4, a related family member, have provided insights into the molecular basis of catalytic inactivity in non-classical PLDs [voshol-2010-pld4-transmembrane-abstract]. In PLD4, several alterations disable catalytic function: modified HKD motifs with critical sequence differences, altered hydrophobic patches containing aromatic amino acids (Phe, Trp, Tyr) instead of conserved hydrophobic residues essential for catalysis, substitution of GT for the GS motif found in functional enzymes, and altered active site geometry relative to enzymatically active family members [voshol-2010-pld4-transmembrane-abstract]. Cell lysates transfected with PLD4 did not exhibit significant PLD activity in either choline release or transphosphatidylation assays under various pH conditions [voshol-2010-pld4-transmembrane-abstract]. PLD5 is noted to contain "less conserved sequences in the HKD motifs" than even PLD4, suggesting even more extensive divergence from the catalytically competent ancestral sequence [voshol-2010-pld4-transmembrane-abstract].

While PLD3 and PLD4 have been shown to function as 5' exonucleases, whether PLD5 possesses any enzymatic activity, phospholipase-related or otherwise, remains an open question. The more extensive divergence of PLD5's catalytic motifs compared to PLD3 and PLD4 may indicate that PLD5 has lost all enzymatic function, or alternatively, that it has acquired an as-yet-undiscovered novel activity.

## Expression Patterns and Tissue Distribution

PLD5 exhibits a highly restricted expression pattern that distinguishes it from other family members. According to data from the Human Protein Atlas, PLD5 shows remarkably concentrated expression with the highest levels observed in the choroid plexus (26.1 nTPM), followed by blood vessels (10.5 nTPM) and the cerebellum (7.0 nTPM) [human-protein-atlas-pld5-summary]. The protein is classified as "group enriched" across blood vessel, brain, and choroid plexus tissues, with a tau specificity score of 0.84 indicating high tissue specificity [human-protein-atlas-pld5-summary]. This pattern places PLD5 among genes detected in only some tissues rather than showing widespread distribution.

The NCBI Gene database reports that during fetal development, PLD5 expression is highest in adrenal tissue (0.532 RPKM at 10 weeks), with moderate expression in stomach tissue and low expression in heart, lung, kidney, and intestine [ncbi-gene-200150-summary]. The enrichment of PLD5 in choroid plexus, a specialized brain structure responsible for cerebrospinal fluid production and the blood-CSF barrier, is particularly intriguing given the gene's reported association with neuropsychiatric disorders.

PLD5 has been assigned to the "Choroid plexus - Transmembrane transport" expression cluster in the Human Protein Atlas, suggesting potential involvement in transport-related processes [human-protein-atlas-pld5-summary]. A 2024 review additionally reported PLD5 expression in liver, spleen, brain, and lymph nodes [zhang-2024-pld-neurodegenerative-abstract], which partially overlaps with but extends the Human Protein Atlas findings. This functional classification is consistent with the prediction that PLD5 is membrane-localized, although the specific transport functions, if any, remain to be characterized.

## Subcellular Localization

The subcellular localization of PLD5 has been investigated through multiple approaches, though some discrepancies exist between studies. Immunocytochemistry studies using confocal microscopy have localized PLD5 to the mitochondria, with this localization receiving an "approved" reliability score based on experiments with the validated antibody HPA028389 [human-protein-atlas-pld5-summary]. This finding was corroborated by a 2024 study examining all six mammalian PLD family members, which demonstrated that when expressed in HMC3 cells, PLD5 and PLD6 both localized to mitochondria, in contrast to PLD1, PLD3, and PLD4 which localized to lysosomes, and PLD2 which localized to the plasma membrane [singh-2024-pld3-pld4-bmp-abstract].

However, some sources report alternative localizations for PLD5. A 2024 review described PLD5 as localizing to the endoplasmic reticulum and Golgi apparatus [zhang-2024-pld-neurodegenerative-abstract], while earlier literature also reported PLD5 as a cytoplasmic protein [becconcino-2014-pld-signaling-abstract]. These discrepancies could reflect cell-type specific differences in PLD5 localization, methodological variations between studies, or the protein's potential trafficking through multiple compartments.

The mitochondrial localization of PLD5 is noteworthy in the context of the PLD family, as PLD6 (MitoPLD) is also anchored to the outer mitochondrial membrane where it plays roles in mitochondrial dynamics and the generation of piwi-interacting RNAs [becconcino-2014-pld-signaling-abstract]. However, while PLD6 has demonstrated phospholipase activity toward cardiolipin on the mitochondrial surface, no such activity has been demonstrated for PLD5. Importantly, the 2024 Cell study investigating BMP synthesis found that PLD5 did not localize to lysosomes and did not participate in the lysosomal BMP synthesis pathway that PLD3 and PLD4 catalyze [singh-2024-pld3-pld4-bmp-abstract], further distinguishing PLD5 functionally from its closest paralogues.

## Disease Associations

Despite the lack of established enzymatic function, PLD5 has been implicated in several disease contexts through genetic association studies, suggesting that the protein serves biologically important functions.

### Neuropsychiatric Disorders

PLD5 is perhaps most widely known for its potential correlation with neuropsychiatric disorders [stutchfield-2015-pld-roles-abstract]. The Autism Genome Project, which genotyped 1,558 rigorously defined autism spectrum disorder (ASD) families for one million SNPs, identified PLD5 among genes showing strong association signals in exploratory analyses of phenotypic subtypes [stutchfield-2015-pld-roles-abstract]. While these signals did not reach genome-wide significance after correction for multiple testing, a SNP in the PLD5 gene has been reported to correlate with verbal performance in autism patients [becconcino-2014-pld-signaling-abstract]. The enriched expression of PLD5 in choroid plexus and cerebellum provides biological plausibility for a role in neurodevelopment or brain function.

### Uterine Fibroids

Association mapping studies have linked PLD5 to uterine fibroid (leiomyoma) risk and growth. A study examining genetic associations across a two-megabase interval on chromosome 1q43 in 1,152 premenopausal women identified several association peaks with fibroid development, with PLD5 emerging among genes acting in signal transduction that appeared to affect tumor growth [aissani-2013-fibroids-1q43-abstract]. PLD5 is located near other candidate genes on 1q43 including FH (fumarate hydratase), EXO1, MAP1LC3C, and RGS7 [aissani-2013-fibroids-1q43-abstract]. The proximity to FH is noteworthy as mutations in this gene cause hereditary leiomyomatosis and renal cell carcinoma syndrome.

### Cancer

PLD5 has been implicated in prostate cancer progression. A study found that PLD5 overexpression exerted oncogenic effects, promoting cell proliferation, migration, invasion, and metastasis in prostate cancer cells [liu-2021-mir145-pld5-prostate-abstract]. The microRNA miR-145-5p was identified as a direct regulator of PLD5 that reverses these oncogenic effects; upregulation of miR-145-5p increased apoptosis and repressed the malignant phenotype through PLD5 suppression [liu-2021-mir145-pld5-prostate-abstract]. This finding suggests that despite lacking classical phospholipase activity, PLD5 participates in signaling pathways relevant to cancer biology.

### Other GWAS Associations

According to the NCBI Gene database, PLD5 has been associated through GWAS with several additional phenotypes including drug response variation, coronary artery calcification, tuberculosis risk, immunoglobulin glycosylation, and childhood obesity [ncbi-gene-200150-summary]. The breadth of these associations, spanning metabolic, immune, and cardiovascular domains, suggests that PLD5 may influence fundamental cellular processes with pleiotropic effects.

## Mouse Knockout Phenotypes

Mice lacking PLD5 have been generated and phenotyped by the International Mouse Phenotyping Consortium (IMPC). Initial reports indicated that no significant abnormalities were observed in high-throughput phenotypic screens [becconcino-2014-pld-signaling-abstract]. However, more detailed IMPC data from standardized phenotyping pipelines testing 20 of 24 physiological systems identified 6 significant phenotypes, with effects observed in homeostasis/metabolism, growth/size/body region, hematopoietic system, and skeletal system [impc-pld5-knockout-summary].

Importantly, no significant phenotypes were detected in 16 other systems including the nervous system, behavior/neurological measures, immune system, cardiovascular system, and reproductive system [impc-pld5-knockout-summary]. The absence of overt neurological phenotypes in PLD5 knockout mice may seem inconsistent with the human genetic associations with autism, but this could reflect species differences, genetic redundancy, or subtle phenotypes not captured by standard behavioral assays. Notably, no associated human diseases are currently documented in the IMPC database for PLD5 [impc-pld5-knockout-summary].

## Potential Functions and Mechanisms

Given the lack of phospholipase D activity and the absence of demonstrated alternative enzymatic function, the molecular mechanisms by which PLD5 might influence the disease phenotypes with which it has been associated remain speculative. Several possibilities warrant consideration.

First, PLD5 might function as a scaffolding or regulatory protein independent of any enzymatic activity. The protein retains the overall fold of the PLD catalytic domain, which could serve as a protein-protein interaction interface even if catalysis is abolished. Such non-enzymatic functions have been demonstrated for other "dead" enzyme homologs across various protein families.

Second, the close evolutionary relationship between PLD5 and the nuclease-active PLD3/PLD4 raises the possibility that PLD5 retains some form of nucleic acid-related function, perhaps as a sensor or regulator rather than an enzyme. However, no experimental evidence currently supports this hypothesis.

Third, the mitochondrial localization of PLD5 suggests potential roles in mitochondrial function, dynamics, or signaling that could account for the metabolic and growth-related phenotypes observed in knockout mice. The relationship to the mitochondrial-localized PLD6 warrants investigation.

Fourth, PLD5's expression in the choroid plexus suggests potential roles in cerebrospinal fluid production, blood-CSF barrier function, or brain homeostasis that could be relevant to its association with neuropsychiatric disorders.

## Open Questions

Several important questions remain regarding PLD5 biology:

1. **Does PLD5 possess any enzymatic activity?** While phospholipase D activity is unlikely, the protein has not been systematically tested for alternative activities such as nuclease function (by analogy to PLD3/PLD4), transphosphatidylation with alternative substrates, or entirely novel catalytic activities.

2. **What are the structural features of PLD5?** No crystal structure or cryo-EM structure of PLD5 has been reported. Structural analysis would reveal whether the protein adopts the canonical PLD fold and identify any unique features that might suggest function.

3. **What proteins interact with PLD5?** Systematic interactome studies could identify binding partners that would illuminate PLD5's cellular role, whether enzymatic or non-enzymatic.

4. **Why is PLD5 enriched in the choroid plexus?** The striking expression pattern suggests a specialized function in this tissue that merits investigation.

5. **What is the molecular basis for the GWAS associations?** The mechanisms by which PLD5 variants influence autism risk, fibroid development, prostate cancer progression, and other phenotypes remain unknown.

6. **Does PLD5 have redundant functions with other family members?** The relatively mild phenotypes in knockout mice could reflect compensation by PLD3, PLD4, or other proteins.

7. **What are the precise catalytic site mutations?** A detailed sequence comparison of the HKD motifs across all PLD family members, with structural modeling, would define exactly which residues are altered in PLD5 and predict whether any residual activity is possible.

8. **Is PLD5 expression or function altered in disease states?** Beyond genetic association, expression changes or post-translational modifications of PLD5 in neuropsychiatric disorders, fibroids, or cancer have not been characterized.

## References

1. **[stutchfield-2015-pld-roles-abstract]** Stutchfield BM, Bhinder T, Horgan PG. Physiological and pathophysiological roles for phospholipase D. Journal of Lipid Research. 2015. PMID: 26637523, PMCID: PMC4655994, DOI: 10.1194/jlr.R056705

2. **[liu-2021-mir145-pld5-prostate-abstract]** Liu J, Li J, Ma Y, Xu C, Wang Y, He Y. MicroRNA miR-145-5p inhibits Phospholipase D 5 (PLD5) to downregulate cell proliferation and metastasis to mitigate prostate cancer. Bioengineered. 2021;12(1):3240-3251. PMID: 34238129, DOI: 10.1080/21655979.2021.1945361

3. **[aissani-2013-fibroids-1q43-abstract]** Aissani B, Wiener H, Zhang K. Multiple hits for the association of uterine fibroids on human chromosome 1q43. PLoS One. 2013;8(3):e58399. PMID: 23555580, DOI: 10.1371/journal.pone.0058399

4. **[gavin-2018-pld3-pld4-exonuclease-abstract]** Gavin AL, Huang D, Huber C, et al. PLD3 and PLD4 are single stranded acid exonucleases that regulate endosomal nucleic acid sensing. Nature Immunology. 2018;19(9):942-953. PMID: 30111894, PMCID: PMC6105523, DOI: 10.1038/s41590-018-0179-y

5. **[voshol-2010-pld4-transmembrane-abstract]** Voshol H, Strang AM, Bhathena A, et al. Phospholipase D Family Member 4, a Transmembrane Glycoprotein with No Phospholipase D Activity, Expression in Spleen and Early Postnatal Microglia. PLoS One. 2010;5(11):e13932. PMID: 21085682, PMCID: PMC2978679, DOI: 10.1371/journal.pone.0013932

6. **[becconcino-2014-pld-signaling-abstract]** Phospholipase D in Cell Signaling: From a Myriad of Cell Functions to Cancer Growth and Metastasis. Molecular and Cellular Biology. 2014. PMCID: PMC4132763

7. **[ncbi-gene-200150-summary]** NCBI Gene Entry for PLD5. Gene ID: 200150. URL: https://www.ncbi.nlm.nih.gov/gene/200150

8. **[human-protein-atlas-pld5-summary]** Human Protein Atlas Entry for PLD5. Gene ID: ENSG00000180287. URLs: https://www.proteinatlas.org/ENSG00000180287-PLD5/tissue and https://www.proteinatlas.org/ENSG00000180287-PLD5/subcellular

9. **[impc-pld5-knockout-summary]** International Mouse Phenotyping Consortium. Pld5 Knockout Mouse Phenotype Data. MGI ID: MGI:2442056. URL: https://www.mousephenotype.org/data/genes/MGI:2442056

10. **UniProt Entry Q8N7P1** - Inactive phospholipase D5 [Homo sapiens]. URL: https://www.uniprot.org/uniprotkb/Q8N7P1/entry

11. **[singh-2024-pld3-pld4-bmp-abstract]** Singh S, Dransfeld U, Ambaw Y, Lopez-Scarim J, Farese RV Jr, Walther TC. PLD3 and PLD4 synthesize S,S-BMP, a key phospholipid enabling lipid degradation in lysosomes. Cell. 2024;187(22):6261-6277.e22. PMID: 38562702, DOI: 10.1016/j.cell.2024.08.042

12. **[zhang-2024-pld-neurodegenerative-abstract]** Zhang et al. Phospholipase D, a Novel Therapeutic Target Contributes to the Pathogenesis of Neurodegenerative and Neuroimmune Diseases. Analytical Cellular Pathology. 2024. PMCID: PMC10940030, DOI: 10.1155/2024/6681911


## Citations

1. aissani-2013-fibroids-1q43-abstract.md
2. becconcino-2014-pld-signaling-abstract.md
3. gavin-2018-pld3-pld4-exonuclease-abstract.md
4. human-protein-atlas-pld5-summary.md
5. impc-pld5-knockout-summary.md
6. liu-2021-mir145-pld5-prostate-abstract.md
7. ncbi-gene-200150-summary.md
8. singh-2024-pld3-pld4-bmp-abstract.md
9. stutchfield-2015-pld-roles-abstract.md
10. voshol-2010-pld4-transmembrane-abstract.md
11. zhang-2024-pld-neurodegenerative-abstract.md