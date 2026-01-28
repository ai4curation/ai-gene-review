---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T00:26:48.016354'
end_time: '2026-01-24T00:38:57.634369'
duration_seconds: 729.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: WDR6
  gene_symbol: WDR6
  uniprot_accession: Q9NNW5
  protein_description: 'RecName: Full=tRNA (34-2''-O)-methyltransferase regulator
    WDR6 {ECO:0000305}; AltName: Full=WD repeat-containing protein 6;'
  gene_info: Name=WDR6;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the WD repeat WDR6 family. .
  protein_domains: Gal_Oxase/kelch_b-propeller. (IPR011043); tRNA_Anticodon_Mtase-Reg.
    (IPR051973); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_dom_sf. (IPR036322);
    WD40_rpt. (IPR001680)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9NNW5
- **Protein Description:** RecName: Full=tRNA (34-2'-O)-methyltransferase regulator WDR6 {ECO:0000305}; AltName: Full=WD repeat-containing protein 6;
- **Gene Information:** Name=WDR6;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the WD repeat WDR6 family. .
- **Key Domains:** Gal_Oxase/kelch_b-propeller. (IPR011043); tRNA_Anticodon_Mtase-Reg. (IPR051973); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_dom_sf. (IPR036322); WD40_rpt. (IPR001680)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "WDR6" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'WDR6' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **WDR6** (gene ID: WDR6, UniProt: Q9NNW5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# WDR6 (Q9NNW5): A Comprehensive Research Report on tRNA Methyltransferase Regulator Function

## Introduction

WDR6 (WD repeat-containing protein 6) is a human protein encoded by the WDR6 gene located on chromosome 15q21. The protein consists of 1,121 amino acids and contains 11 WD-repeat domains organized in a characteristic β-propeller structure [li-2000-wdr6-cloning-abstract]. According to UniProt, WDR6's primary function is as a tRNA (34-2'-O)-methyltransferase regulator, and this role has been substantiated by biochemical reconstitution studies demonstrating that WDR6 forms an obligate complex with FTSJ1 to catalyze 2'-O-methylation at position 34 of specific transfer RNAs [li-2020-ftsj1-wdr6-abstract].

The discovery of WDR6's role in tRNA modification represents a significant advance in understanding epitranscriptomic regulation of translation. Based on articles retrieved from PubMed, Li et al. (2020) demonstrated for the first time that the FTSJ1-WDR6 complex reconstituted in vitro is capable of 2'-O-methylation activity at position 34 of specific tRNAs, with the modification requiring pre-existing 1-methylguanosine at position 37 (mG37) as a prerequisite ([DOI](https://doi.org/10.15252/embr.202050095)). This finding established WDR6 as the human functional equivalent of yeast Trm734, a component of the conserved tRNA modification machinery.

## Molecular Function: tRNA 2'-O-Methylation

The primary and best-characterized molecular function of WDR6 is as a regulatory subunit of the FTSJ1 tRNA 2'-O-methyltransferase complex. WDR6 does not possess catalytic activity itself; rather, it serves as a scaffold protein that binds transfer RNA and positions it correctly for methylation by FTSJ1 [li-2020-ftsj1-wdr6-summary].

The FTSJ1-WDR6 complex specifically catalyzes 2'-O-methylation at the wobble position 34 (Nm34) of certain tRNAs, producing Gm34 (2'-O-methylguanosine) in tRNA-Phe(GAA), tRNA-Trp(CCA), and tRNA-Leu(UAA). FTSJ1 alone cannot perform this catalysis; the presence of WDR6 is essential for enzymatic activity. In vitro reconstitution experiments demonstrated that neither FTSJ1 nor WDR6 alone could methylate tRNA substrates, but the binary FTSJ1-WDR6 complex exhibited robust Gm34 formation activity [li-2020-ftsj1-wdr6-abstract].

The catalytic mechanism involves S-adenosyl-L-methionine (SAM) as the methyl donor. Isothermal titration calorimetry confirmed that FTSJ1 binds SAM directly, while WDR6 primarily functions in substrate recognition and positioning. A critical finding is that the modification requires pre-existing mG37 (1-methylguanosine at position 37) as a prerequisite, establishing a hierarchical order of tRNA modifications where G37 must first be methylated before position 34 can be modified [li-2020-ftsj1-wdr6-summary].

It is important to note that FTSJ1 forms a separate complex with THADA (another regulatory protein) to catalyze 2'-O-methylation at position 32 (Nm32) of tRNAs. According to PubMed, Ishiguro et al. (2025) solved the cryo-EM structure of the human FTSJ1-THADA complex and demonstrated that the interaction mode between FTSJ1 and THADA is distinct from that between FTSJ1 and WDR6 ([DOI](https://doi.org/10.1038/s42003-025-08278-3)). This division of labor—WDR6 for position 34 and THADA for position 32—ensures precise and position-specific tRNA modification.

## Structural Features and Protein Architecture

WDR6 was first cloned and characterized by Li et al. (2000), who identified it as a novel WD-repeat protein containing 11 WD-repeat units arranged in two distinct groups separated by a putative transmembrane domain [li-2000-wdr6-cloning-abstract]. This architecture is unique among human WD-repeat proteins and is conserved across eukaryotes, with homologs found in Arabidopsis thaliana and yeast (Saccharomyces cerevisiae Trm734/YPL183c).

Structural insights into the FTSJ1-WDR6 complex come primarily from crystallographic studies of the yeast ortholog Trm7-Trm734. According to PubMed, Hirata et al. (2019) solved the crystal structure of the Trm7-Trm734 complex and revealed that Trm734 (the WDR6 ortholog) consists of three WD40 β-propeller domains designated BPA, BPB, and BPC ([DOI](https://doi.org/10.1093/nar/gkz856)). BPA and BPC form a unique V-shaped cleft that docks to the methyltransferase Trm7, while BPB contains a positively charged surface that interacts with the D-arm of the tRNA substrate [hirata-2019-trm7-trm734-structure-summary].

The C-terminal region of FTSJ1 (around residue 221) is essential for binding to WDR6. Li et al. identified the peptide sequence FNQLDGPTRIIVPFVTCGDLSS in FTSJ1 as the critical motif for WDR6 interaction using domain mapping and proximity labeling experiments [li-2020-ftsj1-wdr6-summary]. This binding interface is distinct from the FTSJ1-THADA interaction, allowing FTSJ1 to form mutually exclusive complexes with either WDR6 or THADA depending on the target modification site.

## Subcellular Localization

WDR6 and the FTSJ1-WDR6 complex are predominantly cytoplasmic. Immunofluorescence microscopy of Flag-tagged FTSJ1 in HEK293T cells demonstrated that the protein is mainly located in the cytoplasm, with only a small fraction detected in the nucleus [li-2020-ftsj1-wdr6-summary]. This localization is consistent with WDR6's function in modifying cytoplasmic tRNAs that are involved in translation.

Subcellular fractionation experiments confirmed this distribution, with Western blotting showing FTSJ1 predominantly in cytosolic fractions using α-tubulin as a cytoplasmic marker and lamin A/C as a nuclear marker. The cytoplasmic localization was also confirmed in studies of WDR6's interaction with LKB1, where immunofluorescence staining revealed that WDR6 is localized in the cytoplasm, similar to LKB1 ([DOI](https://doi.org/10.1007/s11010-006-9402-5)) [xie-2007-wdr6-lkb1-abstract].

## Biological Processes and Pathways

### Translation Regulation and Codon-Specific Effects

The 2'-O-methylation at position 34 of tRNAs catalyzed by FTSJ1-WDR6 has significant consequences for translation fidelity and efficiency. Loss of Gm34 modification in tRNA-Phe(GAA) specifically reduces translation efficiency of the UUU codon (but not the synonymous UUC codon), demonstrating codon-specific effects of this epitranscriptomic modification [li-2020-ftsj1-wdr6-summary].

Bioinformatic analysis revealed that approximately 40% of genes with high TTT codon bias are related to brain and nervous system functions. This finding provides a mechanistic link between WDR6/FTSJ1 function and the neurological phenotypes observed in patients with FTSJ1 mutations, who present with non-syndromic X-linked intellectual disability (NSXLID) [li-2020-ftsj1-wdr6-abstract].

### Hierarchical tRNA Modification

The modifications at positions 32, 34, and 37 of the anticodon loop are interdependent and occur in a specific hierarchical order. In tRNA-Phe(GAA), the hypermodification wybutosine (yW) or peroxywybutosine (o2yW) at position 37 depends on prior Cm32 and Gm34 formation. FTSJ1 knockout cells show decreased o2yW37 levels and accumulated mG37, indicating that the loss of ribose methylation at positions 32 and 34 impedes the conversion of mG37 to hypermodified forms. This hierarchical relationship is conserved between yeast and humans [li-2020-ftsj1-wdr6-summary].

### Cell Cycle Regulation via LKB1

Beyond its role in tRNA modification, WDR6 has been implicated in cell cycle regulation through interaction with the tumor suppressor kinase LKB1 (also known as STK11). Xie et al. (2007) identified WDR6 as an LKB1-interacting protein using yeast two-hybrid screening and demonstrated that coexpression of WDR6 with LKB1 enhances the inhibitory effect of LKB1 on cell proliferation ([DOI](https://doi.org/10.1007/s11010-006-9402-5)) [xie-2007-wdr6-lkb1-abstract].

Mechanistically, WDR6 synergizes with LKB1 to induce G1 cell cycle arrest by upregulating the cyclin-dependent kinase inhibitor p27(Kip1). Coexpression of WDR6 and LKB1 significantly elevated p27 promoter activity compared to LKB1 alone. These findings suggest that WDR6 participates in the tumor suppressor pathway of LKB1, mutations in which cause Peutz-Jeghers syndrome with increased cancer predisposition.

### Insulin Signaling and Longevity

WDR6 has been linked to insulin/IGF-1 signaling pathways in the brain. According to PubMed, Chiba et al. (2007) identified WDR6 as interacting with insulin receptor substrate 4 (IRS-4) in rat brain and found that WDR6 is abundantly expressed in the hypothalamus ([DOI](https://doi.org/10.1016/j.neurobiolaging.2007.07.008)) [chiba-2007-wdr6-irs4-abstract].

Notably, WDR6 expression in the hypothalamic arcuate nucleus was decreased under conditions associated with extended lifespan, including caloric restriction and growth hormone-antisense transgenic rats. Conversely, insulin and IGF-1 treatment increased WDR6 expression in hypothalamus-derived GT1-7 cells. These findings suggest WDR6 may participate in the regulation of feeding behavior and longevity through insulin/IGF-1 signaling in the brain.

### Hepatic De Novo Lipogenesis

A recent study identified an unexpected role for WDR6 in hepatic lipid metabolism. According to PubMed, Zhang et al. (2023) demonstrated that WDR6 promotes hepatic de novo lipogenesis (DNL) during insulin resistance by interacting with PPP1CB (protein phosphatase 1 catalytic subunit beta) ([DOI](https://doi.org/10.1038/s42255-023-00896-7)) [zhang-2023-wdr6-lipogenesis-abstract].

Mechanistically, WDR6 facilitates PPP1CB-mediated dephosphorylation of the carbohydrate-responsive element-binding protein (ChREBP), leading to ChREBP activation and nuclear translocation. Activated ChREBP then induces expression of lipogenic genes. Importantly, WDR6 knockdown in insulin-resistant mice reduced hepatic steatosis and improved glucose homeostasis, suggesting WDR6 as a potential therapeutic target for metabolic disorders including non-alcoholic fatty liver disease (NAFLD).

### Innate Immunity and Viral Defense

WDR6 has been identified as a host restriction factor for vaccinia virus. According to PubMed, Sivan et al. (2015) performed a genome-wide siRNA screen and discovered that knockdown of WDR6 (along with SAMD9) dramatically enhanced replication of a vaccinia virus mutant lacking the C7L and K1L genes ([DOI](https://doi.org/10.1128/mBio.01122-15)) [sivan-2015-wdr6-vaccinia-abstract].

CRISPR/Cas9 knockout of WDR6 in HeLa cells rendered them permissive for replication of the K1L(-)C7L(-) mutant virus. WDR6 appears to act independently of SAMD9 in this pathway, as no direct interactions between WDR6 and SAMD9 or the viral K1/C7 proteins were detected.

A follow-up study by Sivan et al. (2018) demonstrated that the restriction hierarchy is SAMD9 > WDR6 > FTSJ1, with the C7/K1 deletion mutant reaching wild-type replication levels only in SAMD9 knockout cells ([DOI](https://doi.org/10.1128/JVI.01329-18)) [sivan-2018-wdr6-ftsj1-vaccinia-abstract]. Importantly, the co-identification of WDR6 but not THADA from the genome-wide screen strongly suggests that tRNA methylation at position 34 (catalyzed by FTSJ1-WDR6) is specifically important for host restriction, while position 32 modification (catalyzed by FTSJ1-THADA) is not. This finding directly links WDR6's tRNA modification function to innate antiviral immunity and suggests that proper wobble position modification is required for efficient translation during viral infection.

### E3 Ubiquitin Ligase Complex Association

WDR6 has been identified as a component of a Cullin 4-DDB1 E3 ubiquitin ligase complex. According to PubMed, Xue et al. (2019) used affinity pull-down and mass spectrometry to identify the Cul4-DDB1-WDR3/WDR6 complex as a binding partner of SPAK and OSR1 kinases, which regulate ion homeostasis under osmotic stress ([DOI](https://doi.org/10.1002/cbic.201900454)) [xue-2019-wdr6-spak-abstract].

The interaction between WDR6 and SPAK/OSR1 requires phosphorylation of the S-motif by WNK kinases, suggesting a phosphorylation-dependent regulatory mechanism linking osmotic stress signaling to potential protein degradation pathways. This function of WDR6 as a substrate receptor for the Cul4-DDB1 E3 ligase represents a distinct molecular role from its tRNA modification function.

### Cancer and Tumor Immune Microenvironment

A significant role for WDR6 in hepatocellular carcinoma (HCC) was identified through its E3 ubiquitin ligase function. Zhang et al. (2023) demonstrated that WDR6 promotes HCC progression by targeting the tumor suppressor UVRAG for ubiquitin-mediated degradation via the CUL4A-DDB1-ROC1 E3 ligase complex ([DOI](https://doi.org/10.15252/emmm.202215924)) [zhang-2023-wdr6-hcc-abstract]. WDR6 uses a distinctive WDxR motif to bind UVRAG and direct it to this degradation pathway.

Mechanistically, UVRAG degradation prevents autophagic degradation of NF-κB p65, leading to increased chromatin accessibility at the TNFα locus. This results in elevated TNFα production, which has profound effects on the tumor immune microenvironment: it increases intratumoral myeloid-derived suppressor cells (MDSCs) while reducing CD8+ T cell infiltration, thereby creating an immunosuppressive environment that favors tumor growth. Importantly, TNFα also activates NF-κB signaling to upregulate WDR6 transcription, establishing a self-reinforcing positive feedback loop.

While WDR6 knockdown does not substantially alter HCC cell proliferation or invasion in vitro, it dramatically suppresses tumor growth and lung metastasis in immune-competent mice. This finding underscores the importance of WDR6's role in shaping the tumor immune microenvironment rather than direct effects on cancer cell behavior. Clinically, the WDR6/UVRAG/NF-κB pathway is hyperactivated in HCC patients and predicts poor prognosis. A therapeutic approach using WDxR-mimetic peptides to disrupt the WDR6-UVRAG interaction enhanced the efficacy of anti-PD-L1 immunotherapy in preclinical models.

## Evidence Summary

The evidence for WDR6's function as a tRNA methyltransferase regulator is robust and includes:

1. **Biochemical reconstitution**: In vitro assays demonstrating that purified FTSJ1-WDR6 complex (but not either protein alone) catalyzes Gm34 formation on specific tRNAs [li-2020-ftsj1-wdr6-abstract].

2. **Genetic studies**: CRISPR knockout of WDR6 in HEK293T cells specifically abolishes Gm34 modification of tRNA-Phe while leaving Cm32 intact, confirming position-specific function [li-2020-ftsj1-wdr6-summary].

3. **Structural studies**: Crystal structure of yeast Trm7-Trm734 complex reveals molecular basis for tRNA recognition and positioning by the WDR6 ortholog [hirata-2019-trm7-trm734-structure-abstract].

4. **Mass spectrometry**: UPLC-MS/MS analysis confirming loss of specific nucleoside modifications in knockout cells [li-2020-ftsj1-wdr6-summary].

5. **Evolutionary conservation**: The Trm7-Trm734 system is conserved from yeast to humans, and human FTSJ1/WDR6 can complement yeast deletion mutants [li-2020-ftsj1-wdr6-abstract].

Evidence for alternative functions (LKB1 interaction, insulin signaling, lipogenesis, viral restriction) comes from independent yeast two-hybrid screens, co-immunoprecipitation, and genetic manipulation studies, though these functions may be secondary to or independent from the tRNA modification role.

## Disease Associations

While no human diseases have been directly attributed to WDR6 mutations, the protein has been implicated in several pathological contexts:

1. **Intellectual disability**: Through its role in the FTSJ1 complex, WDR6 function is relevant to NSXLID caused by FTSJ1 mutations, as both proteins are required for proper tRNA modification [li-2020-ftsj1-wdr6-abstract].

2. **Obsessive-compulsive disorder**: According to PubMed, a large genome-wide association study (GWAS) of 53,660 OCD cases identified WDR6 as one of 25 genes classified as most likely causal candidates for OCD ([DOI](https://doi.org/10.1038/s41588-025-02189-z)).

3. **Metabolic disorders**: WDR6's role in promoting hepatic lipogenesis during insulin resistance suggests involvement in NAFLD and metabolic syndrome [zhang-2023-wdr6-lipogenesis-abstract].

4. **Hepatocellular carcinoma**: WDR6 promotes HCC progression through its E3 ubiquitin ligase function by targeting UVRAG for degradation, which remodels the tumor immune microenvironment. WDR6 expression predicts poor prognosis in HCC patients, and targeting WDR6 enhances anti-PD-L1 immunotherapy efficacy [zhang-2023-wdr6-hcc-abstract].

5. **Other cancers**: WDR6 interaction with tumor suppressor LKB1 and its role in the Cul4-DDB1 E3 ligase complex suggest potential broader involvement in tumorigenesis beyond HCC.

## Open Questions

Despite significant advances in understanding WDR6 function, several important questions remain:

1. **Structural basis for human FTSJ1-WDR6 complex**: While the yeast structure has been solved, high-resolution structures of the human FTSJ1-WDR6 complex with tRNA substrate would provide crucial insights into the mechanism of position 34-specific methylation and potential therapeutic targeting.

2. **Coordination of multiple functions**: How WDR6's tRNA modification function relates to its roles in LKB1 signaling, insulin signaling, lipogenesis, and viral restriction remains unclear. Are these independent functions, or does tRNA modification status influence these pathways?

3. **Tissue-specific regulation**: WDR6 is ubiquitously expressed, but its specific functions may vary by tissue. The mechanisms controlling tissue-specific WDR6 activity, particularly in brain versus liver, need further investigation.

4. **Clinical relevance of WDR6 variants**: While WDR6 has been identified in GWAS for OCD and other conditions, the functional consequences of specific variants and their contribution to disease pathogenesis remain to be determined.

5. **Therapeutic potential**: Could WDR6 be targeted pharmacologically for metabolic disorders given its role in hepatic lipogenesis? What would be the consequences on tRNA modification and translation?

6. **Interplay with THADA**: How cells coordinate FTSJ1-WDR6 (for Nm34) and FTSJ1-THADA (for Nm32) complex formation to achieve proper sequential tRNA modification is not fully understood.

## References

1. **li-2020-ftsj1-wdr6**: Li J, Wang YN, Xu BS, Liu YP, Zhou M, Long T, Li H, Dong H, Nie Y, Chen PR, Wang ED, Liu RJ. Intellectual disability-associated gene ftsj1 is responsible for 2'-O-methylation of specific tRNAs. EMBO Rep. 2020;21(8):e50095. PMID: 32558197. DOI: [10.15252/embr.202050095](https://doi.org/10.15252/embr.202050095)

2. **hirata-2019-trm7-trm734-structure**: Hirata A, Okada K, Yoshii K, Shiraishi H, Saijo S, Yonezawa K, Shimizu N, Hori H. Structure of tRNA methyltransferase complex of Trm7 and Trm734 reveals a novel binding interface for tRNA recognition. Nucleic Acids Res. 2019;47(20):10942-10955. PMID: 31586407. DOI: [10.1093/nar/gkz856](https://doi.org/10.1093/nar/gkz856)

3. **li-2000-wdr6-cloning**: Li D, Burch P, Gonzalez O, Kashork CD, Shaffer LG, Bachinski LL, Roberts R. Molecular cloning, expression analysis, and chromosome mapping of WDR6, a novel human WD-repeat gene. Biochem Biophys Res Commun. 2000;274(1):117-23. PMID: 10903905. DOI: [10.1006/bbrc.2000.3012](https://doi.org/10.1006/bbrc.2000.3012)

4. **xie-2007-wdr6-lkb1**: Xie X, Wang Z, Chen Y. Association of LKB1 with a WD-repeat protein WDR6 is implicated in cell growth arrest and p27(Kip1) induction. Mol Cell Biochem. 2007;301(1-2):115-22. PMID: 17216128. DOI: [10.1007/s11010-006-9402-5](https://doi.org/10.1007/s11010-006-9402-5)

5. **chiba-2007-wdr6-irs4**: Chiba T, Inoue D, Mizuno A, Komatsu T, Fujita S, Kubota H, et al. Identification and characterization of an insulin receptor substrate 4-interacting protein in rat brain: implications for longevity. Neurobiol Aging. 2009;30(3):474-82. PMID: 17720279. DOI: [10.1016/j.neurobiolaging.2007.07.008](https://doi.org/10.1016/j.neurobiolaging.2007.07.008)

6. **sivan-2015-wdr6-vaccinia**: Sivan G, Ormanoglu P, Buehler EC, Martin SE, Moss B. Identification of Restriction Factors by Human Genome-Wide RNA Interference Screening of Viral Host Range Mutants Exemplified by Discovery of SAMD9 and WDR6 as Inhibitors of the Vaccinia Virus K1L-C7L- Mutant. mBio. 2015;6(4):e01122. PMID: 26242627. DOI: [10.1128/mBio.01122-15](https://doi.org/10.1128/mBio.01122-15)

7. **zhang-2023-wdr6-lipogenesis**: Upregulation of WDR6 drives hepatic de novo lipogenesis in insulin resistance in mice. Nat Metab. 2023;5:1574-1590. PMID: 37735236. DOI: [10.1038/s42255-023-00896-7](https://doi.org/10.1038/s42255-023-00896-7)

8. **xue-2019-wdr6-spak**: The Cul4-DDB1-WDR3/WDR6 Complex Binds SPAK and OSR1 Kinases in a Phosphorylation-Dependent Manner. ChemBioChem. 2019;20(23):2935-2944. PMID: 31614064. DOI: [10.1002/cbic.201900454](https://doi.org/10.1002/cbic.201900454)

9. **ishiguro-2025-ftsj1-thada**: Ishiguro K, Fujimura A, Shirouzu M. Structural insights into tRNA recognition of the human FTSJ1-THADA complex. Commun Biol. 2025;8(1):893. PMID: 40483304. DOI: [10.1038/s42003-025-08278-3](https://doi.org/10.1038/s42003-025-08278-3)

10. **ocd-gwas-2025**: Genome-wide analyses identify 30 loci associated with obsessive-compulsive disorder. Nat Genet. 2025. PMID: 40360802. DOI: [10.1038/s41588-025-02189-z](https://doi.org/10.1038/s41588-025-02189-z)

11. **angelova-2020-trm7-drosophila**: Angelova MT, et al. tRNA 2'-O-methylation by a duo of TRM7/FTSJ1 proteins modulates small RNA silencing in Drosophila. Nucleic Acids Res. 2020;48(4):2050-2072. PMID: 31943105. DOI: [10.1093/nar/gkaa002](https://doi.org/10.1093/nar/gkaa002)

12. **zhang-2023-wdr6-hcc**: Zhang H, Chen G, Feng X, Song H, et al. Targeting WDxR motif reprograms immune microenvironment and inhibits hepatocellular carcinoma progression. EMBO Mol Med. 2023;15(5):e15924. PMID: 36947051. DOI: [10.15252/emmm.202215924](https://doi.org/10.15252/emmm.202215924)

13. **sivan-2018-wdr6-ftsj1-vaccinia**: Sivan G, Ormanoglu P, Buehler EC, Martin SE, Moss B. Human Host Range Restriction of the Vaccinia Virus C7/K1 Double Deletion Mutant Is Mediated by an Atypical Mode of Translation Inhibition. J Virol. 2018;92(23):e01329-18. PMID: 30209174. DOI: [10.1128/JVI.01329-18](https://doi.org/10.1128/JVI.01329-18)


## Citations

1. chiba-2007-wdr6-irs4-abstract.md
2. hirata-2019-trm7-trm734-structure-abstract.md
3. hirata-2019-trm7-trm734-structure-summary.md
4. ishiguro-2025-ftsj1-thada-abstract.md
5. li-2000-wdr6-cloning-abstract.md
6. li-2020-ftsj1-wdr6-abstract.md
7. li-2020-ftsj1-wdr6-summary.md
8. sivan-2015-wdr6-vaccinia-abstract.md
9. sivan-2018-wdr6-ftsj1-vaccinia-abstract.md
10. xie-2007-wdr6-lkb1-abstract.md
11. xue-2019-wdr6-spak-abstract.md
12. zhang-2023-wdr6-hcc-abstract.md
13. zhang-2023-wdr6-lipogenesis-abstract.md