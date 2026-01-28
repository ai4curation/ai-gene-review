---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T02:01:09.675439'
end_time: '2026-01-24T02:13:13.530635'
duration_seconds: 723.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CLPSL2
  gene_symbol: CLPSL2
  uniprot_accession: Q6UWE3
  protein_description: 'RecName: Full=Colipase-like protein 2; Flags: Precursor;'
  gene_info: Name=CLPSL2; Synonyms=C6orf126; ORFNames=UNQ3045/PRO9861;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the colipase family. {ECO:0000255|PROSITE-
  protein_domains: Colipase. (IPR001981)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6UWE3
- **Protein Description:** RecName: Full=Colipase-like protein 2; Flags: Precursor;
- **Gene Information:** Name=CLPSL2; Synonyms=C6orf126; ORFNames=UNQ3045/PRO9861;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the colipase family. {ECO:0000255|PROSITE-
- **Key Domains:** Colipase. (IPR001981)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CLPSL2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CLPSL2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CLPSL2** (gene ID: CLPSL2, UniProt: Q6UWE3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Colipase-like Protein 2 (CLPSL2): A Comprehensive Research Report

## Introduction

Colipase-like protein 2 (CLPSL2), also known as C6orf126, is a small secreted protein belonging to the colipase protein family in humans. The gene is located on chromosome 6 and encodes a 100-amino acid precursor protein that, after signal peptide cleavage, yields a mature protein of approximately 79 amino acids with a molecular weight of about 10.8 kDa [clark-2003-spdi-abstract][mungall-2003-chromosome6-abstract]. Despite sharing the characteristic colipase domain (InterPro: IPR001981) with canonical pancreatic colipase (CLPS), CLPSL2 has emerged as a functionally distinct protein with a specialized role in male reproductive biology rather than lipid digestion. The protein is predominantly expressed in the epididymis and is secreted into the epididymal lumen where it interacts with maturing spermatozoa [lu-2018-clpsl2-epididymis-abstract]. However, the precise biological function of CLPSL2 remains incompletely characterized, with conflicting evidence from knockdown and knockout studies regarding its essentiality for male fertility.

## Structural Features and Domain Architecture

CLPSL2 contains a single colipase domain that spans most of its mature sequence. The colipase domain is characterized by a compact structure stabilized by multiple disulfide bonds. UniProt annotation indicates five disulfide bonds in CLPSL2 at positions 34-45, 40-56, 44-78, 66-86, and 80-97 of the precursor sequence, which is consistent with the cysteine-rich nature of the colipase fold. The protein is synthesized with a 21-amino acid N-terminal signal peptide (residues 1-21) that directs it to the secretory pathway, confirming its identity as a secreted protein. The signal peptide cleavage site was experimentally verified through Edman sequencing of recombinant protein [zhang-2004-signal-peptide-abstract].

Canonical pancreatic colipase functions as an essential cofactor for pancreatic lipase (PTL) during dietary fat digestion. The colipase-lipase interaction has been extensively characterized at the structural level [vantilbeurgh-1999-colipase-structure-abstract][lowe-1997-pancreatic-lipase-colipase-abstract]. Colipase binds to the C-terminal non-catalytic domain of pancreatic lipase, thereby stabilizing an active conformation of the enzyme and considerably increasing the overall hydrophobic binding surface that enables the complex to anchor to lipid-water interfaces in the presence of bile salts [lowe-2002-triglyceride-lipases-abstract]. The interaction between colipase and lipase involves specific conserved residues that have been mapped through structural and mutagenesis studies.

Critically, sequence analysis has revealed that CLPSL2 lacks the conserved amino acid residues in pancreatic colipase (CLPS) that mediate interaction with lipase [lu-2018-clpsl2-epididymis-abstract]. Consistent with this structural prediction, recombinant CLPSL2 protein does not possess the canonical colipase function of promoting the hydrolysis of lipase substrates such as glycerine trioleate. However, sequence analysis suggests that CLPSL2 retains the capacity to bind lipids directly [lu-2018-clpsl2-epididymis-abstract], implying that the lipid-binding function of the colipase fold may be conserved while the lipase-cofactor function has been lost or repurposed during evolution.

## The Colipase Fold Family and Evolutionary Diversification

The colipase domain represents a versatile protein scaffold that has been evolutionarily recruited for diverse functions beyond its canonical role as a lipase cofactor. Structural studies have revealed that the colipase fold shares significant homology with domains found in several unrelated proteins, including the C-terminal cysteine-rich domain of the Dickkopf family of developmental signaling proteins and mamba intestinal toxin 1 (MIT1) [vantilbeurgh-1999-colipase-structure-abstract][szeto-2000-colipase-fold-abstract]. This structural relationship suggests that the colipase fold may have inherent properties, such as membrane or lipid interaction capability, that have made it a useful scaffold for diverse biological functions.

The evolutionary versatility of the colipase fold is further demonstrated by its convergent recruitment into venom systems across diverse animal taxa. The AVIT/colipase/prokineticin protein scaffold has been independently recruited into venoms of multiple species, suggesting that its structural properties make it particularly suitable for functional diversification [fry-2009-toxinogenomics-abstract]. Studies of spider venom polypeptides with colipase homology have demonstrated that these proteins can adopt the colipase fold while lacking any colipase activity, providing a clear precedent for CLPSL2's apparent divergence from canonical colipase function [szeto-2000-colipase-fold-abstract].

This evolutionary perspective suggests that CLPSL2 represents one of several independent adaptations of the colipase scaffold for novel functions. The conservation of the overall fold while losing lipase-interaction residues may indicate that CLPSL2 has retained membrane or lipid-binding capabilities that are relevant to its function in the epididymal environment.

## Tissue Expression and Subcellular Localization

CLPSL2 exhibits a highly tissue-restricted expression pattern that distinguishes it from the pancreatic expression of canonical colipase. The protein shows tissue-enriched expression in the epididymis, with particularly strong expression in the caput (head) region of the epididymis [lu-2018-clpsl2-epididymis-abstract][noda-2019-epididymis-ko-abstract]. Additional expression has been detected in male germ line stem cells and at lower levels in various other tissues according to expression databases (Bgee).

As a secreted protein, CLPSL2 is released from epididymal epithelial cells into the luminal fluid. Studies in mice have demonstrated that Clpsl2 protein secreted into the epididymal lumen becomes associated with spermatozoa transiting through the epididymis. Specifically, the protein has been shown to coat the acrosome region and the principal piece of the sperm tail [lu-2018-clpsl2-epididymis-abstract]. Interestingly, the binding rate between Clpsl2 and spermatozoa decreases progressively during epididymal transit, suggesting that the protein may be involved in transient modifications of the sperm surface during the maturation process.

UniProt annotation classifies CLPSL2 as a secreted, extracellular protein, which is consistent with its signal peptide and its functional localization to the epididymal lumen. The protein functions in an extracellular compartment, interacting with the sperm surface in the specialized microenvironment of the epididymal duct.

## The Epididymal Microenvironment and Sperm Maturation

To understand the potential function of CLPSL2, it is essential to consider the unique biology of the epididymis. Testicular spermatozoa of all mammalian species are functionally immature, unable to swim progressively or engage in productive interactions with the cumulus-oocyte complex [zhou-2018-epididymal-environment-abstract]. The functional maturation of spermatozoa occurs during transit through the epididymis and is achieved through continuous interactions with the luminal microenvironment. Remarkably, this maturation process occurs without gene transcription or protein translation in the sperm cells themselves, meaning that all modifications are imposed by the epididymal environment.

The epididymal epithelium secretes a complex mixture of proteins, ions, and small non-coding RNAs into the luminal fluid. Both the quantitative and qualitative profiles of these luminal elements display substantial segment-to-segment variation, contributing to the regionalized functionality of the epididymis [zhou-2018-epididymal-environment-abstract]. Spermatozoa acquire functional maturity in the proximal segments (caput and corpus) before being stored in a quiescent state in the distal segment (cauda) in preparation for ejaculation.

Many epididymal secretory proteins are delivered to spermatozoa via epididymosomes, small vesicles released by the epididymal epithelium that can fuse with or attach to the sperm membrane [zhou-2018-epididymal-environment-abstract]. Whether CLPSL2 is delivered to sperm via epididymosomes or through direct binding from the luminal fluid has not been definitively established, though its association with the sperm surface is well documented.

## Biological Function and Role in Sperm Maturation

The biological function of CLPSL2 remains an area of active investigation and some controversy. Given its expression in the caput epididymis and its association with maturing spermatozoa, the protein has been hypothesized to play a role in sperm maturation.

Initial functional studies using RNA interference (RNAi) in mice suggested an important role for Clpsl2 in sperm function. Lu and colleagues demonstrated that lentivirus-mediated knockdown of Clpsl2 expression in vivo caused multiple sperm defects including attenuation of sperm motility, suppressed acrosomal reaction, decreased cauda sperm number, and subfertility [lu-2018-clpsl2-epididymis-abstract]. An earlier study by the same research group also showed that RNAi targeting of the mouse Clpsl2 gene (referred to as meClps) significantly reduced the path velocity of cauda sperm [lian-2014-meclps-rnai-abstract]. These findings suggested that CLPSL2 plays a critical role in regulating sperm motility, maintaining acrosomal integrity, and supporting male fertility.

However, subsequent CRISPR/Cas9 knockout studies have provided contradictory evidence. Noda and colleagues generated complete Clpsl2 knockout mice by deleting the entire coding region and found that homozygous null males displayed normal fertility [noda-2019-epididymis-ko-abstract]. Specifically, Clpsl2 knockout males showed normal epididymal histology, normal sperm morphology, and produced litter sizes comparable to control males (9.1 ± 0.5 pups for knockout versus 9.8 ± 0.8 for controls). The authors noted the discrepancy with the RNAi studies and suggested that the earlier findings may have been influenced by off-target effects of the RNA interference approach, which can affect genes with similar sequences in addition to the intended target [noda-2019-epididymis-ko-summary].

The conflicting results between knockdown and knockout approaches remain unresolved. Several explanations have been proposed: (1) RNAi off-target effects may have caused the observed phenotypes; (2) genetic compensation mechanisms in knockout animals may mask phenotypes that are revealed by acute knockdown approaches; (3) Clpsl2 may contribute to sperm function under certain physiological conditions or stresses not captured in standard laboratory fertility assays; or (4) functional redundancy with other epididymal secretory proteins may compensate for the loss of Clpsl2.

## Evolutionary Conservation

CLPSL2 is evolutionarily conserved across mammalian species, with orthologs identified in humans, mice, chimpanzees, and dogs among others [noda-2019-epididymis-ko-abstract]. The conservation of this gene across mammalian evolution, combined with its tissue-specific expression pattern in the epididymis, suggests a specialized function in male reproduction that has been maintained by selective pressure. Phylogenetic analysis confirms that CLPSL2 is distinct from other colipase family members while sharing the ancestral colipase domain.

The human CLPSL2 gene is located on chromosome 6 at position 6p12.3 [mungall-2003-chromosome6-abstract], and the gene was initially identified as C6orf126 (chromosome 6 open reading frame 126) before receiving its current gene symbol based on its sequence homology to colipase. Two isoforms of CLPSL2 have been reported in humans resulting from alternative splicing, with sequence variation occurring at positions 70-100 of the precursor protein.

## Potential Roles Beyond Reproduction

While the predominant site of CLPSL2 expression is the epididymis, several studies have implicated the protein in other biological contexts, though these associations are largely computational or correlative rather than mechanistically established.

A computational study using machine learning to predict breast cancer-associated proteins identified CLPSL2 among the top-ranked candidates for cancer immunotherapy proteins [lopez-cortes-2020-bc-prediction-abstract]. However, this finding is based on sequence-derived features and protein descriptors rather than experimental evidence of CLPSL2 involvement in cancer biology, and should be interpreted cautiously.

Transcriptomic studies in livestock have also detected CLPSL2 expression changes in metabolic contexts. A study of abnormal ruminal adipose deposition in high-concentrate fed sheep found CLPSL2 among the aberrantly upregulated lipid regulatory factors [xu-2025-sheep-adipose-abstract]. Given the lipid-binding potential of the colipase domain, it is plausible that CLPSL2 could play a role in lipid handling or metabolism, though direct evidence is lacking.

## Protein Interactions

UniProt annotation indicates that CLPSL2 interacts with UBQLN2 (ubiquilin-2) based on six independent experimental observations recorded in the IntAct database. UBQLN2 is a ubiquitin-like protein that functions in protein quality control and is associated with protein degradation pathways. The biological significance of this interaction is unclear and may reflect a role for UBQLN2 in CLPSL2 turnover rather than a functional partnership.

Gene Ontology annotations for CLPSL2 include molecular function terms such as enzyme activator activity (inferred from electronic annotation via InterPro), and biological process terms including digestion, lipid catabolic process, and response to food (inferred from biological aspect of ancestor evidence). These annotations are largely based on homology to canonical colipase and may not accurately reflect the specialized function of CLPSL2 in the epididymis.

## Open Questions

Several important questions about CLPSL2 biology remain unresolved:

1. **Reconciling knockdown versus knockout phenotypes:** The discrepancy between RNAi studies showing fertility defects and knockout studies showing normal fertility needs to be resolved. Additional studies using conditional knockouts, different genetic backgrounds, or challenged conditions may help clarify whether CLPSL2 has essential functions in specific contexts.

2. **Molecular mechanism of sperm interaction:** While CLPSL2 associates with the sperm acrosome and flagellum, the molecular targets on the sperm surface and the functional consequences of this interaction remain unknown.

3. **Lipid-binding function:** The structural prediction that CLPSL2 retains lipid-binding capacity suggests it may interact with specific lipids on the sperm membrane or in the epididymal fluid. Identifying these lipid partners could illuminate its molecular function.

4. **Signaling pathways:** Whether CLPSL2 participates in or modulates signaling pathways affecting sperm maturation, motility, or the acrosome reaction is unknown.

5. **Human relevance:** Most functional studies have been conducted in mice. Whether CLPSL2 has similar functions in human sperm maturation and whether variants in CLPSL2 are associated with male infertility in humans remains to be determined.

6. **Relationship to other epididymal secretory proteins:** The epididymis secretes many proteins that interact with spermatozoa. Understanding how CLPSL2 functions in concert with or is redundant with other epididymal proteins could explain why its knockout does not cause obvious phenotypes.

7. **Role in non-reproductive tissues:** The significance of CLPSL2 expression outside the epididymis and its potential involvement in lipid metabolism or other processes requires further investigation.

8. **Mechanism of delivery to sperm:** Whether CLPSL2 reaches the sperm surface via epididymosomes or direct binding from luminal fluid is not established.

## References

1. **lu-2018-clpsl2-epididymis**: Lu X, Ding F, Lian Z, Chen L, Cao Z, Guan Y, Chen R, Cai D, Yu Y. An epididymis-specific secretory protein Clpsl2 critically regulates sperm motility, acrosomal integrity, and male fertility. *Journal of Cellular Biochemistry*. 2018;119(6):4760-4774. PMID: 29323738. DOI: [10.1002/jcb.26668](https://doi.org/10.1002/jcb.26668)

2. **noda-2019-epididymis-ko**: Noda T, Sakurai N, Nozawa K, Kobayashi S, Devlin DJ, Matzuk MM, Ikawa M. Nine genes abundantly expressed in the epididymis are not essential for male fecundity in mice. *Andrology*. 2019;7(5):644-653. PMID: 30927342. PMCID: PMC6688925. DOI: [10.1111/andr.12621](https://doi.org/10.1111/andr.12621)

3. **lian-2014-meclps-rnai**: Lian Z, Cao Z, Chen R, Chen L, Xue Y, Qin J, Qi X, Zhang C, Yu Y. Lentiviral vector-mediated RNA interference of mouse epididymis-specific meClps gene lowers mouse sperm mobility. *Nan Fang Yi Ke Da Xue Xue Bao*. 2014;34(9):1359-64. PMID: 25263376. (Chinese)

4. **lowe-1997-pancreatic-lipase-colipase**: Lowe ME. Structure and function of pancreatic lipase and colipase. *Annual Review of Nutrition*. 1997;17:141-58. PMID: 9240923. DOI: [10.1146/annurev.nutr.17.1.141](https://doi.org/10.1146/annurev.nutr.17.1.141)

5. **vantilbeurgh-1999-colipase-structure**: van Tilbeurgh H, Bezzine S, Cambillau C, Verger R, Carrière F. Colipase: structure and interaction with pancreatic lipase. *Biochimica et Biophysica Acta*. 1999;1441(2-3):173-84. PMID: 10570245. DOI: [10.1016/s1388-1981(99)00149-3](https://doi.org/10.1016/s1388-1981(99)00149-3)

6. **lowe-2002-triglyceride-lipases**: Lowe ME. The triglyceride lipases of the pancreas. *Journal of Lipid Research*. 2002;43(12):2007-16. PMID: 12454260. DOI: [10.1194/jlr.r200012-jlr200](https://doi.org/10.1194/jlr.r200012-jlr200)

7. **clark-2003-spdi**: Clark HF, Gurney AL, Abaya E, et al. The secreted protein discovery initiative (SPDI), a large-scale effort to identify novel human secreted and transmembrane proteins: a bioinformatics assessment. *Genome Research*. 2003;13(10):2265-70. PMID: 12975309. PMCID: PMC403697. DOI: [10.1101/gr.1293003](https://doi.org/10.1101/gr.1293003)

8. **mungall-2003-chromosome6**: Mungall AJ, Palmer SA, Sims SK, et al. The DNA sequence and analysis of human chromosome 6. *Nature*. 2003;425(6960):805-11. PMID: 14574404. DOI: [10.1038/nature02055](https://doi.org/10.1038/nature02055)

9. **zhang-2004-signal-peptide**: Zhang Z, Henzel WJ. Signal peptide prediction based on analysis of experimentally verified cleavage sites. *Protein Science*. 2004;13(10):2819-24. PMID: 15340161. PMCID: PMC2286551. DOI: [10.1110/ps.04682504](https://doi.org/10.1110/ps.04682504)

10. **szeto-2000-colipase-fold**: Szeto TH, Wang XH, Smith R, Connor M, Christie MJ, Nicholson GM, King GF. Isolation of a funnel-web spider polypeptide with homology to mamba intestinal toxin 1 and the embryonic head inducer Dickkopf-1. *Toxicon*. 2000;38(3):429-42. PMID: 10669030. DOI: [10.1016/s0041-0101(99)00174-9](https://doi.org/10.1016/s0041-0101(99)00174-9)

11. **fry-2009-toxinogenomics**: Fry BG, Roelants K, Champagne DE, et al. The toxicogenomic multiverse: convergent recruitment of proteins into animal venoms. *Annual Review of Genomics and Human Genetics*. 2009;10:483-511. PMID: 19640225. DOI: [10.1146/annurev.genom.9.081307.164356](https://doi.org/10.1146/annurev.genom.9.081307.164356)

12. **zhou-2018-epididymal-environment**: Zhou W, De Iuliis GN, Dun MD, Nixon B. Characteristics of the Epididymal Luminal Environment Responsible for Sperm Maturation and Storage. *Frontiers in Endocrinology*. 2018;9:59. PMID: 29541061. PMCID: PMC5835514. DOI: [10.3389/fendo.2018.00059](https://doi.org/10.3389/fendo.2018.00059)

13. **UniProt Q6UWE3**: UniProt Consortium. UniProtKB entry Q6UWE3 - CLPSL2_HUMAN. URL: https://www.uniprot.org/uniprotkb/Q6UWE3

14. **lopez-cortes-2020-bc-prediction**: López-Cortés A, Cabrera-Andrade A, Vázquez-Naya JM, et al. Prediction of breast cancer proteins involved in immunotherapy, metastasis, and RNA-binding using molecular descriptors and artificial neural networks. *Scientific Reports*. 2020;10(1):8515. PMID: 32444848. PMCID: PMC7244564. DOI: [10.1038/s41598-020-65584-y](https://doi.org/10.1038/s41598-020-65584-y)

15. **xu-2025-sheep-adipose**: Xu Y, Wang G, Wang W, et al. Elucidating the pathogenesis of rumen abnormal adipose deposition in high-concentrate fed Hu sheep through transcriptomic profiling. *BMC Veterinary Research*. 2025;21(1):547. PMID: 41039546. PMCID: PMC12492511. DOI: [10.1186/s12917-025-04988-2](https://doi.org/10.1186/s12917-025-04988-2)


## Citations

1. clark-2003-spdi-abstract.md
2. fry-2009-toxinogenomics-abstract.md
3. lian-2014-meclps-rnai-abstract.md
4. lopez-cortes-2020-bc-prediction-abstract.md
5. lowe-1997-pancreatic-lipase-colipase-abstract.md
6. lowe-2002-triglyceride-lipases-abstract.md
7. lu-2018-clpsl2-epididymis-abstract.md
8. mungall-2003-chromosome6-abstract.md
9. noda-2019-epididymis-ko-abstract.md
10. noda-2019-epididymis-ko-summary.md
11. szeto-2000-colipase-fold-abstract.md
12. vantilbeurgh-1999-colipase-structure-abstract.md
13. xu-2025-sheep-adipose-abstract.md
14. zhang-2004-signal-peptide-abstract.md
15. zhou-2018-epididymal-environment-abstract.md