---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T18:47:58.775949'
end_time: '2026-01-22T19:01:50.051407'
duration_seconds: 831.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KCNRG
  gene_symbol: KCNRG
  uniprot_accession: Q8N5I3
  protein_description: 'RecName: Full=Potassium channel regulatory protein; Short=Potassium
    channel regulator; AltName: Full=Protein CLLD4;'
  gene_info: Name=KCNRG; Synonyms=CLLD4;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: BTB/POZ_dom. (IPR000210); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB.
    (IPR003131); BTB_2 (PF02214)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 8
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8N5I3
- **Protein Description:** RecName: Full=Potassium channel regulatory protein; Short=Potassium channel regulator; AltName: Full=Protein CLLD4;
- **Gene Information:** Name=KCNRG; Synonyms=CLLD4;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** BTB/POZ_dom. (IPR000210); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KCNRG" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KCNRG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KCNRG** (gene ID: KCNRG, UniProt: Q8N5I3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KCNRG: Potassium Channel Regulatory Protein

## Introduction and Summary

KCNRG (Potassium Channel Regulator, also known as CLLD4) is a human protein encoded by the gene located at chromosome 13q14.3, a region frequently deleted in B-cell chronic lymphocytic leukemia (B-CLL) and other malignancies [ivanov-2003-kcnrg-discovery-abstract]. The protein functions as a negative regulator of voltage-gated potassium channels, specifically members of the Kv1 (Shaker) family, by sequestering channels in the endoplasmic reticulum and preventing their surface expression [usman-2010-kcnrg-shaker-abstract]. KCNRG is a 272-amino acid protein containing a BTB/POZ domain homologous to the tetramerization (T1) domain of voltage-gated potassium channels, through which it interacts with and inhibits channel function [ivanov-2003-kcnrg-discovery-abstract].

The protein has emerged as a multifaceted molecule with roles extending beyond simple potassium channel regulation. It functions as a putative tumor suppressor, with overexpression leading to growth inhibition, cell cycle arrest, and apoptosis induction through suppression of mTOR and VEGFR2 signaling pathways [birerdinc-2010-kcnrg-tumor-suppressor-abstract]. Additionally, KCNRG has been identified as a tissue-specific autoantigen in autoimmune polyendocrine syndrome type 1 (APS-1), where autoantibodies against this protein are strongly associated with pulmonary disease [alimohammadi-2009-aps1-autoantigen-abstract].

## Gene and Protein Structure

The KCNRG gene is located on chromosome 13q14.2-14.3, spanning positions 50,015,444 to 50,020,922 on the GRCh38 reference assembly (NCBI Gene ID: 283518). The gene comprises three exons and produces two protein isoforms through alternative splicing: KCNRG-L (272 amino acids, ~31 kDa) and KCNRG-S (229 amino acids), which differ in their C-terminal sequences while sharing a common N-terminal region of 184 amino acids [ivanov-2003-kcnrg-discovery-abstract]. The gene overlaps with TRIM13 on the same strand and has been assigned the aliases CLLD4 (Chronic Lymphocytic Leukemia Deletion region gene 4) and DLTET.

The defining structural feature of KCNRG is its N-terminal BTB (Bric-a-brac, Tramtrack, Broad complex) domain, also called the POZ domain, which spans amino acid residues 5-106 (InterPro domains: IPR000210 for BTB/POZ_dom, IPR003131 for T1-type BTB). This domain is homologous to the tetramerization (T1) domain found in voltage-gated potassium channels such as those of the Kv1 (Shaker) family [usman-2010-kcnrg-shaker-abstract]. The T1 domain in potassium channels normally mediates the assembly of four alpha-subunits into functional tetrameric channels, and the structural similarity of KCNRG's BTB domain to this region enables it to interact with and interfere with channel assembly.

Recent AlphaFold structural predictions have provided insights into the oligomeric state of KCNRG. These computational analyses predict that KCNRG forms pentameric structures with C5 symmetry, and molecular dynamics simulations over 200 nanoseconds have validated the stability of this pentameric state [esposito-2022-alphafold-kctd-abstract]. KCNRG has been classified within Cluster 2 of the KCTD protein family based on structural analysis, sharing this cluster with KCTD6, KCTD11, and KCTD21. The C-terminal domain (CTD) of KCNRG adopts a propeller-like structure with a central cavity delimited by five exposed and regular beta-strands, a feature shared with other KCTD family members despite the absence of sequence similarity [esposito-2022-alphafold-kctd-abstract].

## Molecular Function: Potassium Channel Regulation

The primary molecular function of KCNRG is the negative regulation of voltage-gated potassium channels, specifically the Kv1 (Shaker) family. Usman and Mathew (2010) provided definitive experimental evidence for this function using Xenopus oocyte expression systems. They demonstrated that KCNRG reduces K+ currents through human potassium channels hKv1.1 (KCNA1) and hKv1.4 (KCNA4) when co-expressed in oocytes [usman-2010-kcnrg-shaker-abstract]. This current attenuation is dependent on the N-terminal T1 domain of the channels, as immunoprecipitation experiments confirmed direct physical association between KCNRG and the N-terminus of these channel proteins.

The mechanism by which KCNRG inhibits channel function involves retention of Kv1 family channels within endomembrane compartments. KCNRG has been characterized as an endoplasmic reticulum (ER)-associated protein, and it appears to function by sequestering a fraction of potassium channels in the ER rather than allowing their trafficking to the plasma membrane [usman-2010-kcnrg-shaker-abstract]. This ER retention mechanism effectively reduces the number of functional channels at the cell surface and consequently decreases whole-cell potassium currents.

The proposed molecular mechanism involves competitive binding of KCNRG's BTB domain to the T1 domains of Kv channels during channel assembly. Since the T1 domain of Kv channels mediates the tetramerization required for functional channel formation, KCNRG may interfere with proper channel assembly by forming heteromeric complexes with channel subunits. This interpretation is supported by the structural homology between KCNRG's BTB domain and the T1 tetramerization domain of voltage-gated potassium channels. KCNRG is one of only two KCTD family proteins known to interact directly with Kv channels, making it a unique regulatory molecule within this protein family.

The original characterization by Ivanov et al. (2003) demonstrated that KCNRG suppresses K+ channel activity in the human prostate cell line LNCaP using electrophysiological techniques [ivanov-2003-kcnrg-discovery-abstract]. This functional effect has implications for cell proliferation, as potassium channels play important roles in cell cycle progression, and their pharmacological blockade has been shown to suppress cellular proliferation.

## Subcellular Localization

KCNRG is predominantly localized to the endoplasmic reticulum, consistent with its role in retaining potassium channels within this compartment [usman-2010-kcnrg-shaker-abstract]. This ER localization has been confirmed through multiple experimental approaches including immunofluorescence and biochemical fractionation studies. The ER localization is functionally significant because it positions KCNRG at the site of potassium channel biosynthesis and initial assembly, enabling it to intercept and retain newly synthesized channels before they can traffic to the plasma membrane.

Gene Ontology annotations support the ER localization and characterize KCNRG as having identical protein binding capability and the ability to undergo protein homooligomerization. The protein's association with the ER membrane system rather than the plasma membrane distinguishes it from classical potassium channel subunits and reflects its regulatory rather than channel-forming function.

## Tissue Expression Pattern

KCNRG exhibits a tissue-enriched expression pattern, with notably high expression in the fallopian tube compared to other tissues (Tau specificity score of 0.84 according to the Human Protein Atlas). RNA expression levels show the fallopian tube at 33.6 nTPM (normalized transcripts per million), substantially higher than the next highest tissues: lung (2.9 nTPM), testis (2.1 nTPM), and bone marrow (1.8 nTPM). This expression pattern has led to the gene's classification within the "Ciliated tissues - Cilium organization" expression cluster, suggesting a potential role in ciliary structure or function in reproductive and respiratory epithelia.

The original characterization by Ivanov et al. (2003) noted that KCNRG transcripts are expressed in normal tissues and in some tumor cell lines [ivanov-2003-kcnrg-discovery-abstract]. Subsequent studies have identified predominant expression in lung tissue, with additional expression in liver and other tissues at lower levels. This lung expression pattern is particularly relevant to the identification of KCNRG as a bronchial autoantigen in APS-1, where the protein's expression was found to be predominantly restricted to the epithelial cells of terminal bronchioles [alimohammadi-2009-aps1-autoantigen-abstract].

## Tumor Suppressor Function and Signaling Pathways

KCNRG has been extensively characterized as a candidate tumor suppressor gene based on its chromosomal location in a frequently deleted region in B-CLL and its functional effects on cell proliferation and apoptosis. Birerdinc et al. (2010) provided comprehensive evidence for the tumor suppressor function of KCNRG through stable overexpression studies in multiple cancer cell lines: RPMI-8226 (multiple myeloma), HL-60 (acute promyelocytic leukemia), and LnCaP (prostate cancer) [birerdinc-2010-kcnrg-tumor-suppressor-abstract].

Overexpression of the longer KCNRG isoform (KCNRG-L) produced significant growth inhibition: 37% reduction in RPMI-8226 (p<0.001), 26% in HL-60 (p<0.0025), and 38% in LnCaP (p<0.009). The shorter isoform (KCNRG-S) showed lesser but still detectable effects on cell growth [birerdinc-2010-kcnrg-tumor-suppressor-abstract]. Beyond growth suppression, KCNRG overexpression dramatically enhanced apoptotic activity: KCNRG-L induced a 180% increase in apoptosis in RPMI-8226, 216% in HL-60, and 46% in LnCaP cells. Additional cellular effects included cell cycle arrest at the G2 phase, morphological changes in suspension cells, and reduced migration capacity.

The molecular mechanisms underlying these tumor suppressor effects involve modulation of key signaling pathways. Proteomics analysis using reverse phase protein arrays revealed that overexpression of either KCNRG isoform was associated with decreased activation of mTOR (mammalian target of rapamycin) through reduced phosphorylation at serines 2481 and 2448 [birerdinc-2010-kcnrg-tumor-suppressor-abstract]. Additionally, decreased phosphorylation of tyrosine 1175 in VEGFR2 (vascular endothelial growth factor receptor 2) was observed. These findings are significant because mTOR and VEGFR2 are central regulators of cell proliferation, survival, and angiogenesis, and their inhibition by KCNRG explains the antiproliferative and pro-apoptotic effects observed.

In RPMI-8226 cells, KCNRG overexpression led to coordinated activation of the apoptotic cascade, with increased cleavage of caspases 3, 6, 7, and 9, as well as the caspase substrate PARP (poly-ADP ribose polymerase) [birerdinc-2010-kcnrg-tumor-suppressor-abstract]. This caspase activation pattern indicates engagement of the intrinsic (mitochondrial) apoptotic pathway, consistent with the effects of mTOR inhibition on cell survival signaling.

## Disease Associations

### B-Cell Chronic Lymphocytic Leukemia and Multiple Myeloma

The chromosomal region 13q14, where KCNRG is located, represents the most frequently deleted region in B-cell chronic lymphocytic leukemia (affecting approximately 55% of CLL patients), with deletions also commonly observed in multiple myeloma, mantle cell lymphoma (38%), and several solid tumors including prostate cancer [ivanov-2003-kcnrg-discovery-abstract, birerdinc-2010-kcnrg-tumor-suppressor-abstract, lia-2012-13q14-mouse-model-abstract]. Extensive characterization of 13q14 deletions has revealed heterogeneous breakpoints affecting multiple genes. A minimal deleted region (MDR) has been defined that encompasses the DLEU2 gene (encoding a non-coding RNA) and the miR-15a/16-1 microRNA cluster located within a DLEU2 intron. Importantly, KCNRG is encoded within an intron of DLEU2 in humans, placing it within this critical tumor suppressor locus [lia-2012-13q14-mouse-model-abstract].

Functional dissection of this locus using transgenic mouse models has demonstrated that deletion of the MDR containing DLEU2/miR-15a/16-1 replicates CLL-associated lymphoproliferations, while larger deletions encompassing the common deleted region (CDR) produce more aggressive disease phenotypes with faster progression [lia-2012-13q14-mouse-model-abstract]. This finding suggests that multiple tumor suppressors cooperate within this region, and the size of 13q14 deletions influences disease severity. While miR-15a/16-1 (which targets BCL2) has been established as a key tumor suppressor in this locus, the contribution of KCNRG and other genes remains an area of active investigation.

Expression analysis in diffuse large B-cell lymphomas (DLBL) revealed decreased levels of both KCNRG mRNA isoforms compared to normal peripheral blood lymphocytes, with the major isoform showing lower expression in DLBL and the minor isoform decreased across a broad range of lymphoma types [birerdinc-2010-kcnrg-tumor-suppressor-abstract]. The haploinsufficiency model has been proposed, whereby loss of one KCNRG allele through deletion may be relevant to disease progression in at least a subset of CLL and MM patients, potentially cooperating with loss of miR-15a/16-1 to produce more aggressive malignancies.

### Hepatocellular Carcinoma

Cho et al. (2006) conducted a comprehensive genetic and expression analysis of KCNRG in hepatocellular carcinomas (HCCs), providing evidence for its role as a tumor suppressor in this malignancy [cho-2006-kcnrg-hcc-abstract]. They identified a missense mutation at codon 92 (CGT→CAT, Arg→His) within the T1 domain of KCNRG. Functional analysis demonstrated that the suppressive cell growth activity of this mutant KCNRG was significantly reduced compared to wild-type protein, indicating that the R92H mutation impairs tumor suppressor function.

Loss of heterozygosity (LOH) at the KCNRG locus was detected in 26.5% of informative HCC cases (17/64), and notably, LOH occurred exclusively in hepatitis B virus (HBV)-positive tumors [cho-2006-kcnrg-hcc-abstract]. This LOH was significantly correlated with adverse clinicopathological features including intrahepatic metastasis (p=0.0247), higher tumor grade (p=0.0078), and advanced clinical stage (p=0.0071). Expression analysis revealed loss of KCNRG transcript in 22 tumor tissues, further supporting a role for KCNRG inactivation in HCC progression.

### Autoimmune Polyendocrine Syndrome Type 1

In a distinct disease context, Alimohammadi et al. (2009) identified KCNRG as a tissue-specific autoantigen in autoimmune polyendocrine syndrome type 1 (APS-1), also known as autoimmune polyendocrinopathy-candidiasis-ectodermal dystrophy (APECED) [alimohammadi-2009-aps1-autoantigen-abstract]. This rare autoimmune disorder is caused by mutations in the AIRE (autoimmune regulator) gene, leading to failure of central immune tolerance and development of multiple organ-specific autoantibodies.

Through immunoscreening of a cDNA library using serum from an APS-1 patient with obstructive respiratory symptoms, KCNRG was identified as a pulmonary autoantigen. Testing of 110 APS-1 patients revealed a striking correlation: autoantibodies to KCNRG were present in 7 of 8 patients with respiratory symptoms but in only 1 of 102 patients without respiratory involvement [alimohammadi-2009-aps1-autoantigen-abstract]. The study described eight APS-1 patients with respiratory symptoms, four of whom had severe airway obstruction, and two died from respiratory disease.

Immunohistochemical analysis demonstrated that KCNRG expression is predominantly restricted to the epithelial cells of terminal bronchioles, explaining the specificity of pulmonary manifestations in patients with anti-KCNRG autoantibodies [alimohammadi-2009-aps1-autoantigen-abstract]. This tissue-restricted expression pattern identifies the terminal bronchiole as a previously unrecognized autoimmune target in APS-1. Anti-KCNRG autoantibodies have been proposed as a biomarker for identifying APS-1 patients at risk for pulmonary disease, and successful treatment with rituximab has been reported in affected patients.

## Mouse Models and Conservation

The mouse ortholog of KCNRG (MGI:2685591) is located on chromosome 14 and shares conserved BTB/POZ domain architecture with the human protein. The Mouse Genome Informatics database documents 9 total mutations and alleles for mouse Kcnrg, including 6 targeted alleles, 1 gene-trapped allele, 1 endonuclease-mediated allele, and 1 chemically-induced allele, with 17 mouse strains or lines available through the International Mouse Strain Resource (IMSR). Expression studies have documented 706 assay results for Kcnrg in the Gene Expression Database (GXD), with expression detected across multiple developmental stages and anatomical structures including the nervous system and cardiovascular system during embryonic development.

While specific phenotype data for KCNRG knockout mice have not been extensively published in the literature, the functional dissection of the 13q14 locus using transgenic mouse models by Lia et al. (2012) demonstrated that deletions encompassing the common deleted region (which includes the KCNRG locus) produced more aggressive lymphoproliferative disease compared to deletions of the minimal deleted region alone [lia-2012-13q14-mouse-model-abstract]. This suggests that KCNRG, along with other genes in this region, contributes to the tumor suppressor function of the 13q14 locus, though disentangling the specific contribution of individual genes remains challenging given their physical overlap and potential functional redundancy.

## KCTD Protein Family Context

KCNRG belongs to the KCTD (potassium channel tetramerization domain) protein family, which comprises 25 members (KCTD1-21, KCNRG, SHKBP1, TNFAIP1, and BTBD10) characterized by an N-terminal domain homologous to the T1 tetramerization domain of voltage-gated potassium channels [liu-2013-kctd-family-review-abstract]. The BTB domain that defines this family is a highly conserved motif of approximately 100 amino acids that mediates protein-protein interactions and oligomerization.

While many KCTD family members function as substrate adaptors for Cullin3-based E3 ubiquitin ligases, KCNRG appears to have a distinct functional role centered on potassium channel regulation. KCNRG is one of only two KCTD proteins known to interact directly with Kv channels, the other being KCTD5 which has been shown to have different functional outcomes. The KCTD family review by Liu et al. (2013) classified members into seven phylogenetic groups based on BTB domain sequence similarity [liu-2013-kctd-family-review-abstract], though KCNRG's classification within this scheme varies between studies.

Structure-based classification using AlphaFold predictions places KCNRG in Cluster 2 along with KCTD6, KCTD11, and KCTD21 [esposito-2022-alphafold-kctd-abstract]. Interestingly, the other members of this cluster (KCTD11 and KCTD21) have been shown to downregulate histone deacetylase (HDAC) activity, raising the question of whether KCNRG may have similar capabilities that have yet to be characterized.

## Open Questions

Several important questions remain regarding KCNRG function and its role in disease:

1. **Structural basis of channel interaction**: While it is established that KCNRG interacts with Kv1 channels via T1 domain interactions, the precise structural basis for this interaction and how it leads to ER retention of channels remains to be elucidated. High-resolution structures of KCNRG-channel complexes would be valuable.

2. **Mechanism linking channel regulation to tumor suppression**: The relationship between KCNRG's potassium channel regulatory function and its tumor suppressor activity is not fully understood. While potassium channels are known to influence cell proliferation, the precise mechanistic link between channel inhibition and the observed effects on mTOR/VEGFR2 signaling requires further investigation.

3. **Possible HDAC regulatory function**: Given that KCNRG clusters structurally with KCTD proteins that regulate HDAC activity, it would be valuable to determine whether KCNRG also possesses HDAC regulatory capabilities, which could provide an additional mechanism for its tumor suppressor function.

4. **Cullin3 interaction**: While many KCTD family members function as Cullin3 adaptors for E3 ubiquitin ligases, whether KCNRG has this capability and what substrates it might target for ubiquitination remains unexplored.

5. **Role in ciliated epithelia**: The enriched expression of KCNRG in fallopian tube and its classification in the "cilium organization" expression cluster suggests possible roles in ciliary function that have not been characterized.

6. **Pathogenic role of anti-KCNRG autoantibodies**: While anti-KCNRG antibodies are strongly associated with pulmonary disease in APS-1, whether these antibodies are directly pathogenic or merely markers of tissue damage requires further study. The mechanism by which loss of immune tolerance to KCNRG leads to respiratory disease is not fully understood.

7. **Therapeutic potential**: The tumor suppressor function of KCNRG raises the possibility of therapeutic strategies based on restoring or enhancing its activity in cancers with 13q14 deletions. The druggability of this pathway and potential approaches to modulate KCNRG function remain to be explored.

## References

1. **ivanov-2003-kcnrg-discovery-abstract**: Ivanov DV, Tyazhelova TV, Lemonnier L, Kononenko N, Pestova AA, Nikitin EA, Prevarskaya N, Skryma R, Panchin YV, Yankovsky NK, Baranova AV. A new human gene KCNRG encoding potassium channel regulating protein is a cancer suppressor gene candidate located in 13q14.3. *FEBS Letters*. 2003;539(1-3):156-60. PMID: 12650944. DOI: 10.1016/s0014-5793(03)00211-4. https://pubmed.ncbi.nlm.nih.gov/12650944/

2. **usman-2010-kcnrg-shaker-abstract**: Usman H, Mathew MK. Potassium channel regulator KCNRG regulates surface expression of Shaker-type potassium channels. *Biochemical and Biophysical Research Communications*. 2010;391(3):1301-5. PMID: 19968958. DOI: 10.1016/j.bbrc.2009.11.143. https://pubmed.ncbi.nlm.nih.gov/19968958/

3. **birerdinc-2010-kcnrg-tumor-suppressor-abstract**: Birerdinc A, Nober T, Engel M, Goheer Agha RA, Engel H, Mottershead C, Baranova A. Pro-apoptotic and antiproliferative activity of human KCNRG, a putative tumor suppressor in 13q14 region. *Tumour Biology*. 2010;31(1):33-45. PMID: 20237900. PMCID: PMC2803748. DOI: 10.1007/s13277-009-0005-0. https://pmc.ncbi.nlm.nih.gov/articles/PMC2803748/

4. **alimohammadi-2009-aps1-autoantigen-abstract**: Alimohammadi M, Dubois N, Sköldberg F, et al. Pulmonary autoimmunity as a feature of autoimmune polyendocrine syndrome type 1 and identification of KCNRG as a bronchial autoantigen. *Proceedings of the National Academy of Sciences U.S.A.* 2009;106(11):4396-401. PMID: 19251657. PMCID: PMC2648890. DOI: 10.1073/pnas.0809986106. https://pubmed.ncbi.nlm.nih.gov/19251657/

5. **cho-2006-kcnrg-hcc-abstract**: Cho YG, Kim CJ, Song JH, Rhie DJ, Park YK, Kim SY, Nam SW, Yoo NJ, Lee JY, Park WS. Genetic and expression analysis of the KCNRG gene in hepatocellular carcinomas. *Experimental & Molecular Medicine*. 2006;38(3):247-55. PMID: 16819283. DOI: 10.1038/emm.2006.30. https://pubmed.ncbi.nlm.nih.gov/16819283/

6. **esposito-2022-alphafold-kctd-abstract**: Esposito L, Balasco N, Vitagliano L. Alphafold Predictions Provide Insights into the Structural Features of the Functional Oligomers of All Members of the KCTD Family. *International Journal of Molecular Sciences*. 2022;23(21):13346. PMID: 36362127. PMCID: PMC9658877. DOI: 10.3390/ijms232113346. https://pmc.ncbi.nlm.nih.gov/articles/PMC9658877/

7. **liu-2013-kctd-family-review-abstract**: Liu Z, Xiang Y, Sun G. The KCTD family of proteins: structure, function, disease relevance. *Cell & Bioscience*. 2013;3(1):45. PMID: 24268103. PMCID: PMC3882106. DOI: 10.1186/2045-3701-3-45. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3882106/

8. **lia-2012-13q14-mouse-model-abstract**: Lia M, Carette A, Tang H, Shen Q, Mo T, Bhagat G, Dalla-Favera R, Klein U. Functional dissection of the chromosome 13q14 tumor-suppressor locus using transgenic mouse lines. *Blood*. 2012;119(13):2981-90. PMID: 22174151. DOI: 10.1182/blood-2011-09-381814. https://pubmed.ncbi.nlm.nih.gov/22174151/

### Database Resources

- **UniProt**: Q8N5I3 - https://www.uniprot.org/uniprotkb/Q8N5I3
- **NCBI Gene**: 283518 - https://www.ncbi.nlm.nih.gov/gene/283518
- **Human Protein Atlas**: ENSG00000198553 - https://www.proteinatlas.org/ENSG00000198553-KCNRG
- **GeneCards**: KCNRG - https://www.genecards.org/cgi-bin/carddisp.pl?gene=KCNRG
- **Mouse Genome Informatics (MGI)**: MGI:2685591 - https://www.informatics.jax.org/marker/MGI:2685591


## Citations

1. alimohammadi-2009-aps1-autoantigen-abstract.md
2. birerdinc-2010-kcnrg-tumor-suppressor-abstract.md
3. cho-2006-kcnrg-hcc-abstract.md
4. esposito-2022-alphafold-kctd-abstract.md
5. ivanov-2003-kcnrg-discovery-abstract.md
6. lia-2012-13q14-mouse-model-abstract.md
7. liu-2013-kctd-family-review-abstract.md
8. usman-2010-kcnrg-shaker-abstract.md