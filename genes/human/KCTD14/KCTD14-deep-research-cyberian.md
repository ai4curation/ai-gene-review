---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T19:42:44.861737'
end_time: '2026-01-22T20:01:07.927064'
duration_seconds: 1103.07
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KCTD14
  gene_symbol: KCTD14
  uniprot_accession: Q9BQ13
  protein_description: 'RecName: Full=BTB/POZ domain-containing protein KCTD14;'
  gene_info: Name=KCTD14;
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
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9BQ13
- **Protein Description:** RecName: Full=BTB/POZ domain-containing protein KCTD14;
- **Gene Information:** Name=KCTD14;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** BTB/POZ_dom. (IPR000210); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KCTD14" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KCTD14' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KCTD14** (gene ID: KCTD14, UniProt: Q9BQ13) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KCTD14: A Largely Uncharacterized BTB Domain Protein with Emerging Roles in Cancer Biology

## Introduction and Summary

KCTD14 (Potassium Channel Tetramerization Domain Containing 14; UniProt: Q9BQ13) is a human protein belonging to the KCTD family, a group of 26 proteins characterized by the presence of a conserved N-terminal BTB (Bric-a-brack, Tram-track, Broad complex) domain, also known as the POZ (poxvirus zinc finger) domain [liu-2013-kctd-family-review-abstract]. Despite the family name suggesting a role in potassium channel function, KCTD proteins are not ion channels themselves; rather, the name derives from sequence similarity between their BTB domains and the T1 tetramerization domains of voltage-gated potassium channels [teng-2019-kctd-neurodevelopment-abstract].

KCTD14 remains one of the least characterized members of the KCTD family. In a comprehensive 2019 review of KCTD proteins and neurodevelopmental disorders, KCTD14's BTB structure, binding partners, biological functions, and disease relevance were all marked as "not determined" [teng-2019-kctd-neurodevelopment-abstract]. However, recent structural predictions and a 2025 study investigating KCTD14 in pancreatic cancer have begun to illuminate aspects of this protein's biology. Notably, structural analyses have revealed that KCTD14, unlike its closest paralog KCTD7 and unlike many other KCTD family members, does not bind Cullin3 and therefore may not function as a canonical E3 ubiquitin ligase substrate adaptor [smaldone-2024-kctd-cullin3-recognition-abstract].

## Protein Structure and Domain Organization

KCTD14 is a 234 amino acid protein containing a single N-terminal BTB domain (approximately residues 51-150) and a unique C-terminal domain (CTD) of approximately 139 residues [brauner-2016-kctd7-neuronal-function-abstract]. The BTB domain adopts a canonical fold characterized by a three-to-four-stranded β-sheet surrounded by five α-helices, which is typical of the KCTD protein family [liu-2013-kctd-family-review-abstract].

AlphaFold predictions have provided critical insights into the oligomeric state of KCTD14. Like many KCTD family members, KCTD14 forms pentameric homo-oligomers with C5 symmetry [canettieri-2022-alphafold-kctd-abstract]. The predicted structure is notably rigid, with molecular dynamics simulations over 200 nanoseconds confirming structural stability with minimal deviation from the predicted model [canettieri-2022-alphafold-kctd-abstract].

The architecture of the KCTD14 pentamer is distinctive among KCTD proteins. The five C-terminal domain units assemble to form a large central cavity, creating what has been described as a "Greek krater" shape, with the CTD pentamer forming the bowl-like top of the structure [canettieri-2022-alphafold-kctd-abstract]. This arrangement differs substantially from other KCTD pentamers, where the C-terminal domains typically form a propeller-like configuration without a prominent central cavity [canettieri-2022-alphafold-kctd-abstract]. The functional significance of this unique cavity remains unknown but could potentially serve as a binding site for substrates or interaction partners.

## Phylogenetic Classification and Evolutionary Relationship to KCTD7

KCTD14 is most closely related to KCTD7, with the two proteins sharing approximately 38% full-length sequence identity [brauner-2016-kctd7-neuronal-function-abstract]. Phylogenetic analyses based on minimal BTB domain sequences have led to the proposal that KCTD7 and KCTD14 constitute a distinct eighth clade (clade H) within the KCTD family [teng-2019-kctd-neurodevelopment-abstract]. This gene duplication event producing the KCTD7/KCTD14 pair is estimated to have occurred before the last common ancestor of all chordates, indicating ancient functional divergence [brauner-2016-kctd7-neuronal-function-abstract].

The 139 C-terminal residues of both KCTD7 and KCTD14 form a structured domain that is apparently unique to these two paralogs and is predicted to have a mixed α/β structure [brauner-2016-kctd7-neuronal-function-abstract]. This shared C-terminal domain architecture, combined with their similar overall pentameric organization, suggests these proteins may share some functional properties, though significant differences have emerged from structural and biochemical studies.

## Lack of Cullin3 Binding: A Critical Functional Distinction

One of the most important functional characteristics of KCTD14 is its inability to bind Cullin3 (Cul3). Many KCTD family members function as substrate-specific adaptors for Cullin3-based E3 ubiquitin ligases (CRL3), where they recruit specific protein substrates for ubiquitination and subsequent degradation [liu-2013-kctd-family-review-abstract]. However, comprehensive structural analysis has demonstrated that KCTD14 does not form a functional complex with Cullin3 [smaldone-2024-kctd-cullin3-recognition-abstract].

This conclusion is supported by both experimental and computational evidence. FLAG pull-down experiments directly comparing KCTD7 and KCTD14 demonstrated that while KCTD7 forms stable 5:5 pentameric assemblies with Cullin3, KCTD14 does not [smaldone-2024-kctd-cullin3-recognition-abstract]. AlphaFold-based predictions of the KCTD14 BTB-Cullin3 interaction produce what has been described as a "meaningless complex," indicating no productive binding interface [smaldone-2024-kctd-cullin3-recognition-abstract].

The structural basis for this difference lies in the α2β3 loop of the BTB domain, which is a critical determinant of Cullin3 recognition. In KCTD14, the presence of secondary structure elements within this loop makes it too rigid to establish the necessary interactions with Cullin3 [smaldone-2024-kctd-cullin3-recognition-abstract]. This stands in contrast to KCTD proteins that successfully bind Cullin3, where the α2β3 loop remains flexible enough to properly engage the Cullin3 binding interface [smaldone-2024-kctd-cullin3-recognition-abstract]. The distinction is particularly striking given that KCTD7, the closest paralog of KCTD14, does bind Cullin3; the two proteins share the same pentameric oligomeric state but have opposite Cullin3 binding behaviors [smaldone-2024-kctd-cullin3-recognition-abstract].

This finding is significant because it suggests that KCTD14 does not function through the canonical KCTD mechanism of recruiting substrates for ubiquitin-mediated degradation via CRL3 complexes. The molecular function of KCTD14 must therefore lie elsewhere.

## Lack of GABA-B Receptor Interaction

Some KCTD family members that do not bind Cullin3 instead function as auxiliary subunits of GABA-B receptors. Specifically, KCTD8, KCTD12, and KCTD16 (constituting clade F of the KCTD family) bind to the C-terminal tail of GABA-B2 receptors and modulate receptor signaling by affecting G-protein βγ subunit dynamics and GIRK channel desensitization kinetics. However, KCTD14 is not among these GABA-B receptor-associated proteins [teng-2019-kctd-neurodevelopment-abstract]. This absence of GABA-B receptor binding, combined with the absence of Cullin3 binding, distinguishes KCTD14 from the two major functional categories of characterized KCTD proteins.

## Subcellular Localization

According to the Human Protein Atlas, KCTD14 protein localizes primarily to the nucleoplasm, with additional presence in vesicles and the cytosol [human-protein-atlas-kctd14-summary]. The protein is classified as intracellular with no predicted secretion signal [human-protein-atlas-kctd14-summary]. The nuclear localization is notable given that many BTB domain proteins function in transcription regulation or as adaptors linking Cullin-RING ligases to nuclear substrates. However, the specific function of KCTD14 in the nucleus remains undetermined.

## Tissue Expression Profile

KCTD14 exhibits low tissue specificity, being expressed across many human tissues [human-protein-atlas-kctd14-summary]. The highest expression levels (measured as normalized transcripts per million, nTPM) are found in the salivary gland (27.1 nTPM), pancreas (26.2 nTPM), adrenal gland (22.1 nTPM), stomach (19.6 nTPM), and seminal vesicle (18.0 nTPM) [human-protein-atlas-kctd14-summary]. In the brain, expression is relatively uniform across regions, with the cerebellum showing the highest levels at 9.1 nTPM [human-protein-atlas-kctd14-summary].

At the single-cell level, KCTD14 shows cell type-enhanced specificity, with notably high expression in breast lactating cells (50.4 normalized counts per million), epididymal principal cells (25.5 nCPM), foveolar cells of the stomach (26.8 nCPM), and pancreatic acinar cells (22.1 nCPM) [human-protein-atlas-kctd14-summary]. KCTD14 is not detected in immune cells [human-protein-atlas-kctd14-summary]. The enrichment in secretory cell types (lactating cells, acinar cells, salivary gland) is intriguing and may suggest a role in secretory processes, though this remains speculative.

## Potential Role in G-Protein Signaling

A 2023 study systematically examined interactions between KCTD family members and G-protein βγ subunits (Gβγ), revealing that roughly half of KCTD proteins exhibit agonist-induced interaction with Gβγ, and nearly all KCTDs can interact with Gβγ via immunoprecipitation (with the exceptions of KCTD9 and KCTD20) [brubacher-2023-kctd-gbeta-gamma-abstract]. The functional consequence of these interactions is the suppression of adenylyl cyclase sensitization, demonstrating that KCTD proteins can shape GPCR signal transmission by sequestering Gβγ [brubacher-2023-kctd-gbeta-gamma-abstract].

While KCTD14 was included in the initial screen (a codon-optimized ORF was created for the study), the published work did not provide detailed characterization of KCTD14's Gβγ binding properties specifically [brubacher-2023-kctd-gbeta-gamma-abstract]. Database annotations link KCTD14 to "Sweet Taste Signaling" and "Activation of cAMP-Dependent PKA" pathways, though these associations appear to be inferred from pathway analysis rather than direct experimental evidence with KCTD14.

## Emerging Role in Pancreatic Cancer

The most significant functional insights into KCTD14 come from a 2025 study examining dendritic cell-related gene signatures in pancreatic cancer [liang-2025-kctd14-pancreatic-cancer-abstract]. This research identified KCTD14 as a key component of a prognostic gene signature and demonstrated a direct functional role for the protein in promoting pancreatic cancer cell proliferation, migration, and invasion.

Key findings from this study include the observation that KCTD14 mRNA and protein levels are significantly elevated in pancreatic cancer cell lines (CAPAN-1 and PANC-1) compared to normal pancreatic epithelial cells (H6C7) [liang-2025-kctd14-pancreatic-cancer-abstract]. Single-cell RNA sequencing revealed that KCTD14 is predominantly expressed in malignant epithelial cell clusters within pancreatic tumors [liang-2025-kctd14-pancreatic-cancer-abstract].

Functional validation through siRNA-mediated KCTD14 knockdown demonstrated significant reductions in cell viability, colony formation, and migration/invasion capacity [liang-2025-kctd14-pancreatic-cancer-abstract]. Importantly, KCTD14 knockdown also reduced protein levels of TNF-α, TNFRSF1A (TNFR1), and TNFRSF1B (TNFR2), implicating KCTD14 in the regulation of TNF signaling [liang-2025-kctd14-pancreatic-cancer-abstract]. Cell-cell communication analysis identified the TNF-TNFRSF1A pathway as central to interactions between KCTD14-positive epithelial cells and tumor-infiltrating dendritic cells [liang-2025-kctd14-pancreatic-cancer-abstract].

The authors hypothesized that KCTD14 may scaffold CUL3-dependent ubiquitination that stabilizes TNF/TNFR1 signaling complexes, or alternatively may alter receptor internalization and turnover [liang-2025-kctd14-pancreatic-cancer-abstract]. However, given structural evidence that KCTD14 does not bind Cullin3 [smaldone-2024-kctd-cullin3-recognition-abstract], this hypothesis requires revision. KCTD14's effect on TNF signaling may instead operate through a Cullin3-independent mechanism, perhaps involving direct protein-protein interactions mediated by its BTB domain or the unique central cavity formed by its C-terminal domain pentamer.

In the prognostic risk model developed by Liang et al., KCTD14 carried the largest positive coefficient, indicating it has the strongest prognostic weight among the genes in the signature [liang-2025-kctd14-pancreatic-cancer-abstract]. KCTD14 expression has also been noted as a prognostic marker in kidney renal clear cell carcinoma, skin cutaneous melanoma, and thyroid carcinoma [human-protein-atlas-kctd14-summary].

## KCTD14 as a Prognostic Biomarker in Ovarian Cancer

KCTD14 has also been identified as a prognostic biomarker in ovarian cancer through DNA methylation studies. Wang et al. (2023) conducted an integrated analysis of DNA methylation and transcriptome data from ovarian cancer patients and identified KCTD14 as one of 12 DNA methylation-related genes with prognostic significance [wang-2023-kctd14-ovarian-methylation-abstract]. The 12-gene prognostic signature, which includes KCTD14 alongside genes such as CA2, CD3G, HABP2, SERPINB5, and SLAMF7, was validated across multiple cohorts for survival prediction [wang-2023-kctd14-ovarian-methylation-abstract].

In the risk score calculation, KCTD14 was assigned a coefficient of -0.1530112, indicating that higher KCTD14 expression is associated with lower risk in this model [wang-2023-kctd14-ovarian-methylation-abstract]. This contrasts with the pancreatic cancer findings, where higher KCTD14 expression was associated with poorer prognosis (positive coefficient), suggesting tissue-specific roles for KCTD14 in cancer biology. The identification of KCTD14 as a methylation-related gene also suggests that epigenetic regulation may be an important mechanism controlling KCTD14 expression in cancer contexts.

Database analyses have also noted copy number variation (CNV) gains for KCTD14 in 4.5% of ovarian cancers, with a fold change of 1.5 in expression (p < 0.001), supporting a potential protumor role in at least a subset of ovarian cancer cases [teng-2019-kctd-neurodevelopment-abstract].

## KCTD14 Upregulation in Dengue Virus Infection

An unexpected finding from recent research is the strong upregulation of KCTD14 in patients infected with dengue virus. Bansod et al. (2024) performed RNA sequencing on 16 dengue patients and 10 healthy controls and identified KCTD14 among the top 20 upregulated genes in infected individuals [bansod-2024-dengue-kctd14-abstract]. Notably, KCTD14 showed consistent and significant upregulation (5- to 8-fold change) across all dengue patients regardless of disease severity, including both dengue with warning signs and severe dengue groups [bansod-2024-dengue-kctd14-abstract].

The consistent upregulation of KCTD14 alongside immune-related genes such as IFI27 (interferon alpha-inducible protein 27), CCL2, and TNF receptor superfamily members (TNFRSF17, TNFRSF13B) in dengue infection is intriguing, particularly given the link between KCTD14 and TNF signaling identified in pancreatic cancer studies [bansod-2024-dengue-kctd14-abstract]. This observation raises the possibility that KCTD14 may play a role in inflammatory or immune responses beyond its associations with cancer. Whether KCTD14 upregulation in dengue represents a protective host response or contributes to pathology remains to be determined.

## Mouse Model Data and Knockout Resources

The mouse ortholog of KCTD14 (Kctd14) has been the subject of gene knockout studies catalogued by the Mouse Genome Informatics (MGI) database and the International Mouse Phenotyping Consortium (IMPC). According to MGI, there are 27 phenotype references and 9 mutations/alleles for Kctd14, including 4 targeted mutations, 2 gene-trapped alleles, and multiple radiation- and chemically-induced mutations [mgi-kctd14-mouse-summary]. Multiple knockout mouse strains (15 strains or lines) are available through the International Mouse Strain Resource (IMSR) for functional studies [mgi-kctd14-mouse-summary].

Notably, despite the availability of these genetic resources, MGI reports that there is no experimental evidence to support Molecular Function, Biological Process, or Cellular Component annotations for Kctd14 following literature review [mgi-kctd14-mouse-summary]. This underscores the limited functional characterization of KCTD14 even in model organisms. Expression data shows 715 assay results documenting expression patterns across multiple developmental tissues and stages, consistent with the widespread but low-level expression observed in human tissues [mgi-kctd14-mouse-summary].

## Protein-Protein Interactions

Direct protein-protein interaction data for KCTD14 is limited. The BioGRID database reports an interaction between RAC1 and the NDUFC2-KCTD14 readthrough protein, identified through affinity capture-mass spectrometry in a high-throughput study of the EGFR network in colorectal cancer cells [kennedy-2019-egfr-network-abstract]. However, this interaction involves the fusion protein rather than KCTD14 alone, and its functional significance remains unclear.

A 2013 study by Skoblov et al. examined protein partners of KCTD family members to gain insights into their functional roles in cell differentiation and development, but KCTD14 was not among the proteins characterized in that analysis. The proteins examined included KCTD5, KCTD9, KCTD10, KCTD12, KCTD15, and KCTD20, each of which was found to have specific interaction partners relevant to various signaling pathways. The absence of KCTD14 from this comprehensive analysis reflects its status as one of the least-studied family members.

Given the pentameric nature of KCTD14 and its unique C-terminal domain cavity structure, identifying specific protein interaction partners remains a priority for understanding its molecular function. The BTB domain typically mediates protein-protein interactions, but the specific partners for KCTD14 have not been systematically characterized.

## Disease Associations

Unlike its paralog KCTD7, which is associated with progressive myoclonic epilepsy (EPM3) and neuronal ceroid lipofuscinosis (CLN14), KCTD14 has no established Mendelian disease associations [teng-2019-kctd-neurodevelopment-abstract]. The GeneCards database reports no confirmed disorders for the KCTD14 gene directly. No GWAS signals have been reported for common variants in KCTD14, though related family members such as KCTD15 have been associated with obesity risk in genome-wide association studies [teng-2019-kctd-neurodevelopment-abstract].

A naturally occurring read-through transcript (NDUFC2-KCTD14) exists between the neighboring NDUFC2 and KCTD14 genes on chromosome 11. This fusion product has been associated with mitochondrial complex I deficiency and mitochondrial disease, though these associations relate to the NDUFC2 component rather than KCTD14 specifically [teng-2019-kctd-neurodevelopment-abstract].

## Open Questions

Several important questions remain regarding KCTD14 function:

1. **What is the molecular function of KCTD14?** Given that it does not bind Cullin3 or GABA-B receptors, KCTD14 cannot function through either of the two major characterized mechanisms of KCTD proteins. What substrates or interaction partners does it engage, and through what biochemical mechanism?

2. **What is the functional significance of the unique "Greek krater" structure?** The large central cavity formed by the C-terminal domain pentamer is distinctive among KCTD proteins. Does this cavity serve as a binding site, and if so, for what ligands?

3. **How does KCTD14 regulate TNF signaling?** The pancreatic cancer study demonstrates functional effects on TNF-α and TNFR1/2 protein levels, but the mechanism is unclear. If KCTD14 cannot recruit proteins for Cullin3-mediated degradation, how does it influence these signaling components?

4. **Why does KCTD14 lack Cullin3 binding while its closest paralog KCTD7 retains this function?** Despite ~38% sequence identity and similar overall architecture, the proteins have diverged in this critical property. What selective pressures drove this divergence?

5. **What is the significance of KCTD14 expression in secretory cell types?** The enrichment in lactating breast cells, pancreatic acinar cells, and salivary gland suggests a potential role in secretory function that merits investigation.

6. **Does KCTD14 interact with Gβγ subunits, and if so, with what functional consequences?** While included in a screen of KCTD-Gβγ interactions, detailed characterization of KCTD14's properties in this system has not been published.

7. **What is the role of KCTD14 in normal pancreas physiology versus pancreatic cancer?** High expression in normal pancreatic acinar cells and upregulation in pancreatic cancer cells suggests complex roles in this tissue.

8. **Why is KCTD14 upregulated in dengue virus infection?** The consistent upregulation across disease severities suggests an active role in viral infection response, but whether this is protective or pathological remains unknown.

9. **Why do the prognostic associations differ between cancer types?** KCTD14 shows a positive risk coefficient in pancreatic cancer but a negative coefficient in ovarian cancer, suggesting context-dependent functions that require investigation.

10. **Is KCTD14 expression epigenetically regulated?** The identification as a DNA methylation-related prognostic gene in ovarian cancer suggests epigenetic control that may be relevant to understanding its tissue-specific expression patterns.

## References

* [liu-2013-kctd-family-review-abstract] - Liu Z, Xiang Y, Sun G. The KCTD family of proteins: structure, function, disease relevance. Cell & Bioscience. 2013;3:45. PMID: 24268103. PMCID: PMC3882106. DOI: 10.1186/2045-3701-3-45. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3882106/

* [teng-2019-kctd-neurodevelopment-abstract] - Teng X, Aouacheria A, Lionnard L, Metz KA, Soane L, Bhattacharya R, et al. KCTD: A new gene family involved in neurodevelopmental and neuropsychiatric disorders. CNS Neuroscience & Therapeutics. 2019;25(7):887-902. PMID: 30929316. PMCID: PMC6566181. DOI: 10.1111/cns.13156. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6566181/

* [canettieri-2022-alphafold-kctd-abstract] - Smaldone G, Coppola L, Balasco N, Pirone L, Pedone E, Vitagliano L. Alphafold Predictions Provide Insights into the Structural Features of the Functional Oligomers of All Members of the KCTD Family. International Journal of Molecular Sciences. 2022;23(21):13346. PMID: 36362138. PMCID: PMC9658877. DOI: 10.3390/ijms232113346. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9658877/

* [smaldone-2024-kctd-cullin3-recognition-abstract] - Smaldone G, Balasco N, Pirone L, Pedone E, Vitagliano L. A Comprehensive Analysis of the Structural Recognition between KCTD Proteins and Cullin 3. International Journal of Molecular Sciences. 2024;25(3):1881. PMCID: PMC10856315. DOI: 10.3390/ijms25031881. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10856315/

* [liang-2025-kctd14-pancreatic-cancer-abstract] - Liang X, et al. Dendritic cell–related gene signature in pancreatic cancer stratifies patient subtypes and implicates a KCTD14–TNF signaling axis. Frontiers in Immunology. 2025;16:1665906. URL: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1665906/full

* [brauner-2016-kctd7-neuronal-function-abstract] - Azizieh R, Orduz D, Van Bogaert P, Bhattacharya R, Bhattacharya K, Bhattacharya S, et al. Pathogenic variants in KCTD7 perturb neuronal K+ fluxes and glutamine transport. Brain. 2016;139(12):3109-3120. PMID: 27679481. DOI: 10.1093/brain/aww244. URL: https://academic.oup.com/brain/article/139/12/3109/2629994

* [zheng-2017-kctd-structural-complexity-abstract] - Zheng S, Bhatt HP, Bhattacharya R, Bhattacharya K. Structural complexity in the KCTD family of Cullin3-dependent E3 ubiquitin ligases. Biochemical Journal. 2017;474(22):3747-3763. PMID: 29005805. PMCID: PMC5664961. DOI: 10.1042/BCJ20170527. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5664961/

* [brubacher-2023-kctd-gbeta-gamma-abstract] - Brubacher JL, et al. Multiple potassium channel tetramerization domain (KCTD) family members interact with Gβγ, with effects on cAMP signaling. Journal of Biological Chemistry. 2023;299(3):102924. PMID: 36709034. PMCID: PMC9976452. DOI: 10.1016/j.jbc.2023.102924. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9976452/

* [human-protein-atlas-kctd14-summary] - The Human Protein Atlas: KCTD14. URL: https://www.proteinatlas.org/ENSG00000151364-KCTD14

* [wang-2023-kctd14-ovarian-methylation-abstract] - Wang S, Fu J, Fang X. A Novel DNA Methylation-Related Gene Signature for the Prediction of Overall Survival and Immune Characteristics of Ovarian Cancer Patients. Journal of Ovarian Research. 2023;16(1):66. PMID: 36978087. DOI: 10.1186/s13048-023-01142-0. URL: https://ovarianresearch.biomedcentral.com/articles/10.1186/s13048-023-01142-0

* [bansod-2024-dengue-kctd14-abstract] - Bansod S, et al. Unraveling potential gene biomarkers for dengue infection through RNA sequencing. Virus Genes. 2024. DOI: 10.1007/s11262-024-02114-2. URL: https://link.springer.com/article/10.1007/s11262-024-02114-2

* [mgi-kctd14-mouse-summary] - Mouse Genome Informatics (MGI): Kctd14. MGI:1289222. URL: https://informatics.jax.org/marker/MGI:1289222

* [kennedy-2019-egfr-network-abstract] - Kennedy SA, et al. Extensive rewiring of the EGFR network in colorectal cancer cells expressing transforming levels of KRASG13D. Nature Communications. 2019;11(1):499. PMID: 31980649. DOI: 10.1038/s41467-019-14224-9. URL: https://pubmed.ncbi.nlm.nih.gov/31980649/


## Citations

1. bansod-2024-dengue-kctd14-abstract.md
2. brauner-2016-kctd7-neuronal-function-abstract.md
3. brubacher-2023-kctd-gbeta-gamma-abstract.md
4. canettieri-2022-alphafold-kctd-abstract.md
5. human-protein-atlas-kctd14-summary.md
6. kennedy-2019-egfr-network-abstract.md
7. liang-2025-kctd14-pancreatic-cancer-abstract.md
8. liu-2013-kctd-family-review-abstract.md
9. mgi-kctd14-mouse-summary.md
10. smaldone-2024-kctd-cullin3-recognition-abstract.md
11. teng-2019-kctd-neurodevelopment-abstract.md
12. wang-2023-kctd14-ovarian-methylation-abstract.md
13. wang-2025-kctd-ovarian-cancer-abstract.md
14. zheng-2017-kctd-structural-complexity-abstract.md