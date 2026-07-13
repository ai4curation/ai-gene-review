---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T06:05:11.727845'
end_time: '2026-07-07T06:05:18.647013'
duration_seconds: 6.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: atpF
  gene_symbol: atpF
  uniprot_accession: Q88BX0
  protein_description: 'RecName: Full=ATP synthase subunit b {ECO:0000255|HAMAP-Rule:MF_01398};
    AltName: Full=ATP synthase F(0) sector subunit b {ECO:0000255|HAMAP-Rule:MF_01398};
    AltName: Full=ATPase subunit I {ECO:0000255|HAMAP-Rule:MF_01398}; AltName: Full=F-type
    ATPase subunit b {ECO:0000255|HAMAP-Rule:MF_01398}; Short=F-ATPase subunit b {ECO:0000255|HAMAP-Rule:MF_01398};'
  gene_info: Name=atpF {ECO:0000255|HAMAP-Rule:MF_01398}; OrderedLocusNames=PP_5417;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATPase B chain family. {ECO:0000255|HAMAP-
  protein_domains: ATP_synth_B-like_membr_sf. (IPR028987); ATP_synth_b/b'su_bac/chlpt.
    (IPR002146); ATP_synth_F0_bsu_bac. (IPR005864); ATP_synthase_B_chain. (IPR050059);
    ATP-synt_B (PF00430)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    query_char_limit: 500
    paper_limit: 50
    snippet_limit: 20
    snippet_paper_limit: 50
    restrict_snippets_to_papers: false
    paper_fields: title,abstract,authors,year,url,venue,journal,tldr,publicationDate,citationCount,influentialCitationCount,externalIds
    publication_date_range: ''
    venues: ''
    inserted_before: ''
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88BX0
- **Protein Description:** RecName: Full=ATP synthase subunit b {ECO:0000255|HAMAP-Rule:MF_01398}; AltName: Full=ATP synthase F(0) sector subunit b {ECO:0000255|HAMAP-Rule:MF_01398}; AltName: Full=ATPase subunit I {ECO:0000255|HAMAP-Rule:MF_01398}; AltName: Full=F-type ATPase subunit b {ECO:0000255|HAMAP-Rule:MF_01398}; Short=F-ATPase subunit b {ECO:0000255|HAMAP-Rule:MF_01398};
- **Gene Information:** Name=atpF {ECO:0000255|HAMAP-Rule:MF_01398}; OrderedLocusNames=PP_5417;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATPase B chain family. {ECO:0000255|HAMAP-
- **Key Domains:** ATP_synth_B-like_membr_sf. (IPR028987); ATP_synth_b/b'su_bac/chlpt. (IPR002146); ATP_synth_F0_bsu_bac. (IPR005864); ATP_synthase_B_chain. (IPR050059); ATP-synt_B (PF00430)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atpF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atpF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atpF** (gene ID: atpF, UniProt: Q88BX0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Asta Literature Retrieval: Gene Research for Functional Annotation ⚠️ CRITICAL: Gene/Protein Identification Context BEFORE YOU BEGIN RESEARCH: Y...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 19
- Snippets retrieved: 20

## Relevant Papers

### [1] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
- Authors: Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al.
- Year: 2021
- Venue: mSystems
- URL: https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
- DOI: 10.1128/mSystems.00673-21
- PMID: 34726489
- PMCID: 8562490
- Citations: 15
- Summary: This work systematically updates the functional genome annotation of Mycobacterium tuberculosis virulent type strain H37Rv and identifies hundreds of high-confidence candidates for mechanisms of antibiotic resistance, virulence factors, and basic metabolism and other functions key in clinical and basic tuberculosis research.
- Evidence snippets:
  - Snippet 1 (score: 0.794)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.686)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology
- Authors: Stefania D'Alessio, Katherine M. Buckley, I. Kraev, P. Hayes, S. Lange
- Year: 2021
- Venue: Biology
- URL: https://www.semanticscholar.org/paper/e2b33d9697175a6e724fdb85e3ac2ec169d92871
- DOI: 10.3390/biology10090866
- PMID: 34571743
- PMCID: 8464700
- Citations: 14
- Summary: This study assessed EVs present in the coelomic fluid of the purple sea urchin, and identified both total protein cargo as well as the deiminated protein cargo, adding to current understanding of how post-translational deimination may shape immunity across the phylogeny tree.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > For the detection of a putative PAD homologue from sea urchins, anti-human PAD2-specific antibody was used in Western blotting to assess any cross-reaction with a (B) KEGG pathways identified from STRING analysis for EV total protein cargo (annotated hits). (C) Gene Ontology (GO) Biological processes identified from STRING analysis for total EV protein cargo (annotated hits). (D) GO Molecular Function pathways identified from STRING analysis for total EV protein cargo (annotated hits; protein names of hits are presented in the figures; additional interacting proteins are: LOC579085 = ATP synthase subunit gamma, mitochondrial; LOC587430 = ATP synthase subunit O, mitochondrial; LOC373382 = ATP synthase subunit alpha; LOC576006 = ATP synthase subunit delta, mitochondrial; LOC579751 = ATP synthase F(0) complex subunit B1, mitochondrial).

### [3] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
- Authors: L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al.
- Year: 2021
- Venue: Frontiers in Research Metrics and Analytics
- URL: https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
- DOI: 10.3389/frma.2021.689059
- PMID: 34322655
- PMCID: 8311438
- Citations: 23
- Influential citations: 1
- Summary: The literature knowledge panels developed and implemented in PubChem help to uncover and summarize important relationships between chemicals, genes, proteins, and diseases by analyzing co-occurrences of terms in biomedical literature abstracts.
- Evidence snippets:
  - Snippet 1 (score: 0.724)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [4] Escherichia coli F1Fo-ATP Synthase with a b/δ Fusion Protein Allows Analysis of the Function of the Individual b Subunits*
- Authors: C. Gajadeera, J. Weber
- Year: 2013
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/d6e7ac8b54142570af6f71a319c1c47c7df37428
- DOI: 10.1074/jbc.M113.503722
- PMID: 23893411
- Citations: 13
- Influential citations: 1
- Summary: It is shown that it is possible to generate a functional E. coli ATP synthase containing a b/δ fusion protein, which allowed the analysis of the roles of the individual b subunits.
- Evidence snippets:
  - Snippet 1 (score: 0.718)
    > The Function of Each of the b Subunits-The finding that in E. coli dimerization of b is required for binding to F 1 (31) certainly suggests that both b subunits are contributing to this function. On the other hand, in chloroplasts and some bacteria the C-terminal helix of b, which appears to be most directly involved in the contacts to ␦ (10, 15-17), is missing, indicating that at least in those organisms one of the b subunits might play a less prominent role in binding of ␦ and F 1 . Similarly, it is not known whether both b subunits are required for binding to a.
    > To answer the question of the role of each b subunit, we first generated strain pCG12/DK8 which contains the gene for the hybrid b/␦ fusion protein (but not that for the additional b subunit), with the DNA sequence encoding the transmembrane helix of the fusion protein deleted. As expected, without the possibility to anchor the fusion protein (independent whether monomeric or dimeric) to a, (b ⌬N /␦) ATP synthase fails to assemble. Neither membrane-bound F 1 nor any ATP synthase activity could be detected. In contrast, activity could be restored when the b gene was added to pCG12, to give pCG13. Strain pCG13/DK8 expressed a functional b(b ⌬N /␦) ATP synthase, which showed a level of expression (and/or stability) and activity very similar to the b(b/␦) enzyme (Table 2), demonstrating that a single transmembrane helix is sufficient to anchor the stator stalk to the a subunit and F o .
    > As mentioned above, in mycobacteria the b subunit contained in the fusion protein is of the full-length b type, whereas the additional b subunit is of the shorter bЈ variety. To test whether it is possible to omit the C-terminal helix in the additional b subunit in E. coli ATP synthase containing the b/␦ fusion protein, thereby essentially generating a bЈ subunit, we engineered plasmid pCG16.

### [5] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
- Authors: Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al.
- Year: 2020
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
- DOI: 10.1186/s12859-020-03764-3
- PMID: 33176685
- PMCID: 7661159
- Citations: 6
- Summary: The Avian Immunome DB (Avimm) for easy gene property extraction as exemplified by avian immune genes is presented and described, which contains 1170 distinct avian immune genes with canonical gene symbols and 612 synonyms across 363 bird species.
- Evidence snippets:
  - Snippet 1 (score: 0.717)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [6] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
- Authors: Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al.
- Year: 2020
- Venue: RNA
- URL: https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
- DOI: 10.1261/rna.075580.120
- PMID: 32669294
- PMCID: 7566566
- Citations: 3
- Summary: Gene ontology analysis reveals an enrichment of genes related to translation, including mRNAs of ribosomal proteins, tRNAs, tRNA ligases, and t RNA-modifying enzymes, consistent with a key role of Hera in ribosome and tRNA metabolism.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [7] Evaluation of 6-Hydroxydopamine and Rotenone In Vitro Neurotoxicity on Differentiated SH-SY5Y Cells Using Applied Computational Statistics
- Authors: Rui F. Simões, Paulo J. Oliveira, Teresa Cunha-Oliveira, F. Pereira
- Year: 2022
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/59030907c78858d46692b09591ebb5bdc3eecf65
- DOI: 10.3390/ijms23063009
- PMID: 35328430
- PMCID: 8953223
- Citations: 9
- Summary: Both biochemical and computational analyses resulted in an evident distinction between the neurotoxic effects of 6-hydroxydopamine and rotenone, specifically for the highest concentrations of both compounds.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > 3.0; Bio-Rad, Hercules, CA, USA).
    > Table 2. List of forward (Fwd) and reverse (Rev) primers used for real time-PCR, respective gene, accession number, and annealing temperature (Ta) for genes used in the calculation of mtDNA copy number and for genes encoding electron transport chain complex and ATP synthase subunits, proteins involved in mitochondrial fission and fusion, antioxidant enzymes, mitochondrial biogenesisrelated gene transcripts, and mitochondrial biogenesis-related gene transcripts. CYB: cytochrome b; B2M: β2 microglobulin; ATP5G1: ATP synthase membrane subunit c locus 1; ATP6: ATP synthase membrane subunit 6; COX1: cytochrome c oxidase I; COX4I1: cytochrome c oxidase subunit 4I1; CYB: cytochrome b; ND5: NADH: Ubiquinone oxidoreductase core subunit 5; NDUFA9: NADH: Ubiquinone oxidoreductase subunit A9; SDHA: succinate dehydrogenase complex flavoprotein subunit A; UQCRC2: ubiquinol-cytochrome c reductase core protein 2; DRP1: dynamin-related protein 1; FIS1: mitochondrial fission 1 protein; MFF: mitochondrial fission factor; MFN1: mitofusin 1; MFN2: mitofusin 2; MIEF2: mitochondrial elongation factor 2; OPA1: optic atrophy 1 protein; CAT: catalase; GPX1: glutathione peroxidase 1; GPX4: glutathione peroxidase 4; SOD1: superoxide dismutase 1; SOD2: superoxide dismutase 2; AMPK: adenosine monophosphate-activated protein kinase; GABPB1: GA binding protein transcription factor subunit beta 1; NRF1: nuclear respiratory factor 1; SIRT1: sirtuin 1; TFAM: mitochondrial transcription factor A.

### [8] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2771
- Influential citations: 298
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [9] An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México
- Authors: Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel
- Year: 2023
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
- DOI: 10.3390/microorganisms11071640
- PMID: 37512813
- PMCID: 10384328
- Citations: 8
- Summary: The quality obtained from the biogas suggests that this metabolism is not the main one in carbon use, possibly the sum of several conditions including growth conditions and the pollution present in these sediments.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > When a genome is sequenced or a protein is characterized, databases classify the information in different ways using automatic identification or manual annotation. In the UniProt database, an annotation is possibly made using the formal representation proposed in Gene Ontology (GO) under three aspects related to biological knowledge of the proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively. An example of an ATP-binding protein is the subunit α of V-type ATP synthase (A0A8G2FW98) of Picrophilus oshimae DSM 9789. As expected, this protein has other three annotations related to proton transport. Besides that, the DNA helicase (A0A811T524) of Ca. Argoarchaeum ethanivorans has the MF of DNA binding and ATP binding. Interestingly, metal ion binding proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively.

### [10] Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences
- Authors: M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al.
- Year: 2025
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
- DOI: 10.3390/ijms262411830
- PMID: 41465260
- PMCID: 12733082
- Summary: This work establishes a foundation for investigating the role of mitochondrial genome variation in key plant’s phenotypic traits, such as the enhanced responsiveness to arbuscular mycorrhiza observed in this agronomically valuable line of Medicago lupulina L. vulgaris Koch.
- Evidence snippets:
  - Snippet 1 (score: 0.684)
    > (ii). Annotation of Protein-Coding Genes Among the 33 ORFs encoding proteins with predicted functions were: nine encoding NADH dehydrogenase subunits, one encoding cytochrome b, three encoding cytochrome C oxidase subunits, five encoding ATP synthase subunits, four responsible for cytochrome C maturation, nine encoding ribosomal proteins, and two with other functions (matR and mttB; Table 1, Figure 2). Among these, the cox2, rps3, nad1, nad5, and rpl2 genes were characterized with potential mutations due to single nucleotide polymorphisms (SNPs). The rpl2 sequence from the VIK32, line MlS-1 mtDNA showed identity with exon 2 of the chloroplast gene encoding ribosomal protein L2. For example, it showed identity with an exon of the line MlS-1 chloroplast gene rplB (OR674883.1; coordinates 78,587-79,084; Cover 69%, Identity 98.3%) (Figure 3), as well as with exon 2 of the chloroplast gene rpl2 from M. lupulina (OM681370.1; Cover 72%, Identity 98.4%) and M. truncatula cultivar Jemalong A17 (MT965675.1; Cover 72%, Identity 97.5%). This sequence also showed high similarity to sequences from the chloroplast genomes of phylogenetically distant plants from the genera Trigonella, Melilotus, Lathyrus, and Pisum (Cover 97%, Identity 95.6-96.2%). The 45 protein-coding genes were characterized as genes encoding hypothetical proteins (Figure 2).

### [11] Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control
- Authors: Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al.
- Year: 2023
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
- DOI: 10.3390/ijms241713058
- PMID: 37685862
- PMCID: 10488290
- Citations: 3
- Summary: Chilodonella hexasticha is a harmful parasitic ciliate that can cause severe damage to fish and high mortalities worldwide. Its congeneric species, C. uncinata, is a facultative parasite that not only can be free-living but also can parasitize on fish gills and fins. In this study, single-cell transcriptomes of these two species were assembled and characterized. Numerous enzymes related to energy metabolism and parasitic adaption were identified through annotation in the Non-Redundant (NR), C...
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > Some energy metabolism-related enzymes, such as isocitrate dehydrogenase (IDH), cytochrome c oxidase subunit 1 (Cox 1) and ATP synthase, were also up-regulated in C. hexasticha. for this study, while those of C. uncinata were adopted from [7]. The yellow boxes represent the upregulated genes, while the blue boxes represent down-expressed genes. The full names of protein products of these annotated genes are TUB: tubulin, ISCU: iron-sulfur cluster assembly scaffold protein IscU-like; ISCB: 2 iron, 2 sulfur cluster-binding protein, IDH: isocitrate dehydrogenase, Cox1: cytochrome c oxidase subunit 1, ATP5D: ATP synthase F1, delta subunit, OGC: 2oxoglutarate/malate carrier protein, ABC: ABC transporter family protein, ATPase: v-type ATPase subunit family protein, HSP: heat shock protein, ACP: acyl carrier protein, DNAH7: dynein heavy chain 7.

### [12] Gene Nomenclature System for Rice
- Authors: S. McCouch
- Year: 2008
- Venue: Rice
- URL: https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
- DOI: 10.1007/s12284-008-9004-9
- Citations: 383
- Influential citations: 9
- Summary: A set of standard procedures for describing genes based on DNA, RNA, and protein sequence information that have been annotated and mapped on the sequenced genome assemblies, as well as those determined by biochemical characterization and/or phenotype characterization by way of forward genetics are outlined.
- Evidence snippets:
  - Snippet 1 (score: 0.675)
    > The name of a protein encoded by a particular gene should be consistent with the gene full name in cases where the gene name is based on phenotype or molecular function (refer to the "Gene full name" section), except that the protein name is written using all upper case characters without italics. If, at a later stage, a gene and its corresponding protein product are determined to have a biochemically characterized molecular function, such as an enzyme or a structural component (subunit) of a macromolecular complex, the protein should be assigned a synonym consistent with the enzyme nomenclature recommended by the IUPAC Enzyme Commission or the macromolecule name adapted by the IUBMB [4]. Because there may be several functional assignments for a given protein (i.e., based on a phenotypic assay, a biochemical assay, or a molecular function), there may be several synonyms for the protein name (and similarly, for the gene full name). The protein symbol should always be consistent with the adopted gene symbol, with the exception that protein symbols are written using all upper case characters without italics, followed by a space and the numeric locus designator. For example, the GLUTINOUS ENDOSPERM 1 (WX1) gene encodes the granule-bound starch synthase enzyme (EC: 2.4.1.11). The protein name is GLUTINOUS ENDOSPERM 1 and the symbol is 'WX1'. The protein name(s), 'WAXY', 'WAXY 1', and GRANULE-BOUND STARCH SYNTHASE (GBSS) will be recorded as synonyms. If a name cannot be assigned based on phenotype, known biochemistry, or other experimental evidence supporting its function, a systematic locus identifier (described above) and a name consistent with the description in Table 1 must be used to describe the gene until its function can be confirmed.

### [13] Using Machine Learning to Predict Genes Underlying Differentiation of Multipartite and Unipartite Traits in Bacteria
- Authors: Fatemah Almalki, Janak Sunuwar, R. Azad
- Year: 2023
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/31f0553ef83afa52edbdd1d1cd56a933b481fd21
- DOI: 10.3390/microorganisms11112756
- PMID: 38004767
- PMCID: 10672838
- Summary: This study revealed a small pool of genes that discriminate bacteria with multipartite genomes and their close relatives with single-chromosome genomes, and leveraged machine learning as a means to identify the genetic factors that underlie the differentiation of these bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > Set 2 Set 3   On the other hand, we found the following proteins in the Set 1 genes by using the differentially present genes approach (Table 4): cell division protein ftsz, diguanylate cyclase/phosphodiesterase, and ompa/motb domain protein. These were categorized under cellular processes and signaling. More specifically, these genes have cell-cycle control; cell division; a chromosome-partitioning function (D); signal transduction mechanisms (T); and cell wall, membrane, and envelope biogenesis (M). Also, mannosylglycerate synthase domain protein-encoding gene in this set was categorized under metabolism, and more specifically, nucleotide transport and metabolism (F). Another gene in this set encodes a putative metal-dependent protease that has a replication, recombination, and repair function (L), and more broadly, it is categorized under information storage and processing. In addition to these, three genes were categorized under "unknown function" by the eggNOG program: the cobalamin biosynthesis protein CbiG, extensin family protein, and a protein of unknown function duf1127. Three genes, namely those encoding the gcra cell-cycle regulator, invasion-associated locus b family protein, and HPS_22 (hypothetical protein), were not scanned by the eggNOG program.
    > For Set 2 from the differentially present genes approach, we found the following functional representation (Table 4): genes encoding d-isomer-specific 2-hydroxyacid dehydrogenase and nad-binding protein (CH) were functionally classified as energy production and conversion and coenzyme transport and metabolism, both under the category of metabolism. Additionally, gene-encoding glycine dehydrogenase subunit 2 is associated with amino acid transport and metabolism (E), which is also under metabolism. On the other hand, the genes encoding preprotein translocase, the secg subunit, and the outer membrane chaperone skp family protein were categorized under cellular processes and signaling, and the specific functions are intracellular trafficking; secretion and vascular transport (U); and cell wall, membrane, and envelope biogenesis (M), respectively.

### [14] GeneTools – application for functional annotation and statistical hypothesis testing
- Authors: V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al.
- Year: 2006
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
- DOI: 10.1186/1471-2105-7-470
- PMID: 17062145
- PMCID: 1630634
- Citations: 105
- Influential citations: 11
- Summary: GeneTools is the first "all in one" annotation tool, providing users with a rapid extraction of highly relevant gene annotation data for e.g. thousands of genes or clones at once.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [15] Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts
- Authors: J. Doolittle, S. Gomez
- Year: 2011
- Venue: PLoS Neglected Tropical Diseases
- URL: https://www.semanticscholar.org/paper/baff9e82a73e77a021118c0910a5874568cd60b3
- DOI: 10.1371/journal.pntd.0000954
- PMID: 21358811
- PMCID: 3039688
- Citations: 97
- Influential citations: 2
- Summary: Dengue virus manipulates cellular processes to its advantage through specific interactions with the host's protein interaction network, and the interaction networks presented here provide a set of hypothesis for further experimental investigation into the DENV life cycle as well as potential therapeutic targets.
- Evidence snippets:
  - Snippet 1 (score: 0.670)
    > Figure S1 GO term enrichment of A. aegypti proteins based on data from Guo et al. [13]. (A) Enriched GO biological process terms. (B) Enriched GO molecular function terms. Light blue bars represent terms for A. aegypti targets, and pink is for terms from DENV-similar proteins. When more than ten terms were enriched for a set of proteins, only the ten most signicant terms are shown. Bonferroni corrected p-values were transformed by -log10. The following abbreviations are used: "translation factor nucleic acid bind" is "translation factor activity nucleic acid binding," and "macromolecular subunit organiz" is "macromolecular complex subunit organization." Found at: doi:10.1371/journal.pntd.0000954.s001 (1.39 MB TIF)  Table S3 Predicted interactions between DENV2 and human after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the target protein's Uniprot accession, Entrez Gene ID, and Symbol; if the target is a known host factor; and if the predicted interaction was already known in the literature. Found at: doi:10.1371/journal.pntd.0000954.s005 (3.01 MB TXT) Table S4 Predicted interactions between DENV2 and A. aegypti after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the D. melanogaster target protein's FlyBase gene number, and Symbol; the A. aegypti target protein's VectorBase protein ID, and Uniprot accession; and if the target is a known host factor. Found at: doi:10.1371/journal.pntd.0000954.s006

### [16] Integrative genomic and machine learning approaches reveal evolutionary signatures in the winged bean mitochondrial genome
- Authors: Nikhil Kumar Singh, Binay K. Singh, Piyush Kumar, A. Pandey, Sudhir Kumar et al.
- Year: 2025
- Venue: BMC Plant Biology
- URL: https://www.semanticscholar.org/paper/431c722788ae918fa1aba25f05063453d88fefd0
- DOI: 10.1186/s12870-025-07738-6
- PMID: 41315943
- PMCID: 12764132
- Citations: 3
- Summary: This approach not only elucidates the evolutionary architecture of P. tetragonolobus mitogenome but also establishes a transferable model for organelle genome classification and comparative analysis across plants and other eukaryotic lineages.
- Evidence snippets:
  - Snippet 1 (score: 0.666)
    > The mitochondrial genome encodes 64 genes, including 38 protein-coding genes, 20 tRNA genes, and 6 rRNA genes (Fig. 1; Table 1; Supplementary Table S1). These genes are organized into key groups include ATP synthase subunits, NADH dehydrogenase subunits, cytochrome, and ribosomal protein complexes (Fig. 1;). Among the protein-coding genes, the ATP synthase subunits, represented by 5 genes (atp1, atp4, atp6, atp8, and atp9), contribute to ATP production via oxidative phosphorylation. The NADH dehydrogenase subunits are encoded by 11 genes (nad1, nad2, nad3, nad4, nad4L, nad5, nad6, nad7, nad9), which are essential components of Complex I in the electron transport chain, playing a key role in transferring electrons and establishing the proton gradient for ATP synthesis. The cytochrome subunits include 4 genes (cox1, cox2, cox3, and cob), which encode subunits of cytochrome c oxidase (Complex IV) and cytochrome b (Complex III), critical for electron transfer and maintaining the mitochondrial energy cycle. Additionally, the genome includes ribosomal protein genes, with 7 genes (rps3, rps4, rps12, rpl2, rpl5, rpl16, and rpl10) encoding structural components of mitochondrial ribosomes required for efficient protein synthesis within mitochondria. Notably, nine fragmented protein-coding genes are presented in the mitogenome, reflecting the dynamic nature of mitochondrial genome organization (Supplementary Table S1). However, no pseudogenes were identified which are common in species e.g. Vigna radiata and Medicago truncatula [21,22]. These fragmented genes include nad4, nad7, nad2 (with a fragmented form, nad2-fragment), nad5 (with nad5-fragment), nad1 (with nad1-fragment), atp6 (with fragmented forms atp6), rps4-fragment, rps10 and rps3.

### [17] MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data
- Authors: Anthony C. Smith, A. Robinson
- Year: 2009
- Venue: Molecular & Cellular Proteomics : MCP
- URL: https://www.semanticscholar.org/paper/206a60d6d387688ce7f880e0dfe67af5a723c7b8
- DOI: 10.1074/mcp.M800373-MCP200
- PMID: 19208617
- PMCID: 2690483
- Citations: 84
- Influential citations: 7
- Summary: Analysis indicated that enzymes of some cytosolic metabolic pathways are regularly detected in mitochondrial proteomics experiments, suggesting that they are associated with the outside of the outer mitochondrial membrane.
- Evidence snippets:
  - Snippet 1 (score: 0.663)
    > Recorded for each protein of the mass spectrometry data sets were, where available, the original protein identifier, subcellular location, sequence of identified peptides, sequence coverage, and the experimental techniques that had been used for the purification, separation, and identification of the protein. If the original protein identifier could not be mapped to a UniProt primary accession number by PIR ID or MGI, then the protein was compared with proteins in UniProt by using BLASTP (14). If there was a significant match, then the UniProt primary accession number was assigned to the protein. Those proteins without a significant match were discarded. By using the PIR ID and the MGI identifier conversion tools, the evidence of mitochondrial localization for a protein was linked to many of the UniProt entries representing it. Identifiers of proteins encoded in the mitochondrial genome of organisms were taken from the Organelle database of the European Molecular Biology Laboratory-European Bioinformatics Institute and used to annotate the appropriate proteins in MitoMiner.
    > The source of protein sequences, related features, and annotation was UniProt (11). All UniProt entries were downloaded for the six species with mitochondrial localization data sets. The literature citations in each UniProt entry were retrieved from PubMed by using an InterMine parser. Additional Gene Ontology annotation on the biological process, metabolic function, and cellular component of each protein was taken from UniProt (15) and individual genome projects of M. musculus (12), Rattus norvegicus (16), Drosophila melanogaster (17), and Saccharomyces cerevisiae (18).
    > Finally lists of human genes and the descriptions of their associated disease phenotypes were taken from OMIM (19), the definitions of groups of homologous proteins were taken from HomoloGene (20), and data on the reactions, enzymes, and compounds of metabolic pathways were taken from KEGG (21). The EC numbers of proteins in UniProt were used to define the cross-reference between proteins and metabolic pathways.

### [18] The complete sequence of the mitochondrial genome of Nautilus macromphalus (Mollusca: Cephalopoda)
- Authors: J. Boore
- Year: 2006
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/4daa40c63808105da60ea4ef5fd068ebe3de4602
- DOI: 10.1186/1471-2164-7-182
- PMID: 16854241
- PMCID: 1544340
- Citations: 91
- Influential citations: 8
- Summary: Nautilus macromphalus mtDNA contains an expected gene content that has experienced few rearrangements since the evolutionary split between cephalopod mollusk and polyplacophorans, and implies that mutational bias during replication also plays a role.
- Evidence snippets:
  - Snippet 1 (score: 0.662)
    > cox1,cox2,cox3, cytochrome oxidase subunit I, II, and III protein genes; cob, cytochrome b gene;atp6,atp8, ATP synthase subunit 6 and 8 genes; nad1,nad2,nad3,nad4,nad4L, nad5,nad6, NADH dehydrogenase subunit 1-6, 4L genes; trnA,trnC,trnD,trnE,trnF,trnG,trnH,trnI,trnK,trnL1(nag),trn L2(yaa),trnM,trnN,trnP,trnQ,trnR,trnS1(nct),trnS2(nga),tr nT,trnV,trnW,trnY, transfer RNA genes designated by the one-letter code for the specified amino acid; in cases where there is more than one tRNA for a particular amino acid, they are differentiated by numeral and with anticodon (which is maximally ambiguous, e.g. "nag" rather than "tag", to allow recognizing homology with those of other organisms).

### [19] CRONOS: the cross-reference navigation server
- Authors: Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al.
- Year: 2008
- Venue: Bioinformatics
- URL: https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
- DOI: 10.1093/bioinformatics/btn590
- PMID: 19010804
- PMCID: 2638938
- Citations: 20
- Summary: CRONOS, a cross-reference server that contains entries from five mammalian organisms presented by major gene and protein information resources, is developed, which shows that the cross-references are highly accurate.
- Evidence snippets:
  - Snippet 1 (score: 0.660)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Stefania D'Alessio, Katherine M. Buckley, I. Kraev, P. Hayes, S. Lange (2021). Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology. Biology. https://www.semanticscholar.org/paper/e2b33d9697175a6e724fdb85e3ac2ec169d92871
3. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
4. C. Gajadeera, J. Weber (2013). Escherichia coli F1Fo-ATP Synthase with a b/δ Fusion Protein Allows Analysis of the Function of the Individual b Subunits*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/d6e7ac8b54142570af6f71a319c1c47c7df37428
5. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
6. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
7. Rui F. Simões, Paulo J. Oliveira, Teresa Cunha-Oliveira, F. Pereira (2022). Evaluation of 6-Hydroxydopamine and Rotenone In Vitro Neurotoxicity on Differentiated SH-SY5Y Cells Using Applied Computational Statistics. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/59030907c78858d46692b09591ebb5bdc3eecf65
8. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
9. Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel (2023). An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México. Microorganisms. https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
10. M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al. (2025). Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
11. Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al. (2023). Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
12. S. McCouch (2008). Gene Nomenclature System for Rice. Rice. https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
13. Fatemah Almalki, Janak Sunuwar, R. Azad (2023). Using Machine Learning to Predict Genes Underlying Differentiation of Multipartite and Unipartite Traits in Bacteria. Microorganisms. https://www.semanticscholar.org/paper/31f0553ef83afa52edbdd1d1cd56a933b481fd21
14. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
15. J. Doolittle, S. Gomez (2011). Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts. PLoS Neglected Tropical Diseases. https://www.semanticscholar.org/paper/baff9e82a73e77a021118c0910a5874568cd60b3
16. Nikhil Kumar Singh, Binay K. Singh, Piyush Kumar, A. Pandey, Sudhir Kumar et al. (2025). Integrative genomic and machine learning approaches reveal evolutionary signatures in the winged bean mitochondrial genome. BMC Plant Biology. https://www.semanticscholar.org/paper/431c722788ae918fa1aba25f05063453d88fefd0
17. Anthony C. Smith, A. Robinson (2009). MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data. Molecular & Cellular Proteomics : MCP. https://www.semanticscholar.org/paper/206a60d6d387688ce7f880e0dfe67af5a723c7b8
18. J. Boore (2006). The complete sequence of the mitochondrial genome of Nautilus macromphalus (Mollusca: Cephalopoda). BMC Genomics. https://www.semanticscholar.org/paper/4daa40c63808105da60ea4ef5fd068ebe3de4602
19. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c