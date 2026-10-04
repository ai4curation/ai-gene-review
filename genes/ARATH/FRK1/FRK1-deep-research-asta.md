---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-10-02T06:39:16.462024'
end_time: '2026-10-02T06:39:20.768084'
duration_seconds: 4.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: FRK1
  gene_symbol: SIRK
  uniprot_accession: O64483
  protein_description: 'RecName: Full=Senescence-induced receptor-like serine/threonine-protein
    kinase; AltName: Full=FLG22-induced receptor-like kinase 1; Flags: Precursor;'
  gene_info: Name=SIRK; Synonyms=FRK1; OrderedLocusNames=At2g19190; ORFNames=T20K24.21;
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); Leu-rich_rpt. (IPR001611); LRR_dom_sf.
    (IPR032675); Malectin-like_Carb-bd_dom. (IPR024788); Prot_kinase_dom. (IPR000719)
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
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O64483
- **Protein Description:** RecName: Full=Senescence-induced receptor-like serine/threonine-protein kinase; AltName: Full=FLG22-induced receptor-like kinase 1; Flags: Precursor;
- **Gene Information:** Name=SIRK; Synonyms=FRK1; OrderedLocusNames=At2g19190; ORFNames=T20K24.21;
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); Leu-rich_rpt. (IPR001611); LRR_dom_sf. (IPR032675); Malectin-like_Carb-bd_dom. (IPR024788); Prot_kinase_dom. (IPR000719)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SIRK" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SIRK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SIRK** (gene ID: FRK1, UniProt: O64483) in ARATH.

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

- Papers retrieved: 20
- Snippets retrieved: 20

## Relevant Papers

### [1] Protocol for identifying and comparing molecular prognosis subtypes of IgAN using R
- Authors: Juan Wang, Yi Liu, Xi-Zhao Chen, Mansheng Li, Yunping Zhu
- Year: 2024
- Venue: STAR Protocols
- URL: https://www.semanticscholar.org/paper/6794ab2424155d4a65b28cd139731c21d4d37aa2
- DOI: 10.1016/j.xpro.2024.103138
- PMID: 38878284
- PMCID: 11234001
- Summary: A general workflow for identifying and comparing molecular subtypes of disease using proteomics data using R software is presented and steps for data preprocessing, feature selection, determination of subtypes, and functional interpretation of subtypes are described.
- Evidence snippets:
  - Snippet 1 (score: 0.772)
    > The UniProt database (https://www.uniprot.org/) can perform ID mapping on the UniProt ID of each protein to obtain corresponding annotation information, including Entry name, Protein name, Gene name, Organism, and Length.
    > Note: Considering the efficiency and readability of subsequent analysis, users need to convert the ID in the raw data. In this protocol, we choose to convert UniProt ID to Gene Symbol, and when multiple UniProt ID correspond to one Gene Symbol, we can use the make.unique() function to add a serial number to Gene Symbol to make it unique.
    > 7. Group samples by type.

### [2] CRONOS: the cross-reference navigation server
- Authors: Brigitte Waegele, Irmtraud Dunger-Kaltenbach, G. Fobo, Corinna Montrone, H-Werner Mewes et al.
- Year: 2008
- Venue: Bioinformatics
- URL: https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
- DOI: 10.1093/bioinformatics/btn590
- PMID: 19010804
- PMCID: 2638938
- Citations: 20
- Summary: CRONOS, a cross-reference server that contains entries from five mammalian organisms presented by major gene and protein information resources, is developed, which shows that the cross-references are highly accurate.
- Evidence snippets:
  - Snippet 1 (score: 0.723)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [3] Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms
- Authors: Xiao Yang, Shyamasree Saha, Aravind Venkatesan, S. Tirunagari, Vid Vartak et al.
- Year: 2023
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
- DOI: 10.1101/2023.02.20.529292
- PMID: 37857688
- PMCID: 10587067
- Citations: 15
- Influential citations: 1
- Summary: A human-annotated full-text corpus for biomedical entities, comprising 300 full-text open-access research articles, is developed, describing the corpus and details how to access and reuse this open community resource.
- Evidence snippets:
  - Snippet 1 (score: 0.715)
    > Examples are for illustrative purposes only and specific to each case, hence not all the entities are shown and highlighted. RED: Gene/Protein BLUE: Disease GREEN: Organism a. Biomedical concepts Gene/Protein: Annotations could be specific gene/protein names or classes/family names of gene/proteins. In particular, very broad concepts like "protein", "gene", "enzyme", "receptors", "kinase", "cytokine", "transcription regulators/factors" are out of the scope of annotations. However, family/subtype names of those concepts are considered for the annotations, such as "amylolytic enzyme", "antioxidant enzyme", "map kinase p38", because these terms narrow the concepts to specific families of gene/protein, enzyme.
    > Annotators can refer to Uniprot and Protein Ontology.

### [4] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
- Authors: Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al.
- Year: 2021
- Venue: mSystems
- URL: https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
- DOI: 10.1128/mSystems.00673-21
- PMID: 34726489
- PMCID: 8562490
- Citations: 16
- Summary: This work systematically updates the functional genome annotation of Mycobacterium tuberculosis virulent type strain H37Rv and identifies hundreds of high-confidence candidates for mechanisms of antibiotic resistance, virulence factors, and basic metabolism and other functions key in clinical and basic tuberculosis research.
- Evidence snippets:
  - Snippet 1 (score: 0.713)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [5] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
- Authors: Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöery, R. Kuo et al.
- Year: 2020
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
- DOI: 10.1186/s12859-020-03764-3
- PMID: 33176685
- PMCID: 7661159
- Citations: 6
- Summary: The Avian Immunome DB (Avimm) for easy gene property extraction as exemplified by avian immune genes is presented and described, which contains 1170 distinct avian immune genes with canonical gene symbols and 612 synonyms across 363 bird species.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [6] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
- Authors: Christina M McCosker, E. Unal, Alayna K. Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al.
- Year: 2025
- Venue: Molecular ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 4
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [7] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.681)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [8] Synthesis, characterization, and computational evaluation of some synthesized xanthone derivatives: focus on kinase target network and biomedical properties
- Authors: Wisam Taher Muslim, L. J. Mohammad, Munaf M. Naji, Isaac Karimi, Matheel D. Al-Sabti et al.
- Year: 2025
- Venue: Frontiers in Pharmacology
- URL: https://www.semanticscholar.org/paper/659ab502877a1d6b5ab7ce45fa51f0f9a13dcf24
- DOI: 10.3389/fphar.2024.1511627
- PMID: 39830340
- PMCID: 11738930
- Citations: 1
- Summary: Acute leukemic T-cells were one of the top predicted tumor cell lines for these ligands and the possible antileukemic effects of synthesized xanthone derivatives are potentially very interesting and warrant further studies.
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > The UniProt accession identification of target kinases was converted to gene symbols for humans using the SynGO gene set analysis tool (Koopmans et al., 2019), and pooled together, and submitted to GeneMANIA to construct target kinase network. GeneMANIA is a handy web interface for acquiring gene ontology, scrutinizing gene lists, and highlighting genes for functional assays (Warde-Farley et al., 2010). After choosing Homo sapiens from the list of optional organisms, the genes of interest in the previous step were entered into the search bar and the results were collated and high-scored genes were culled for further discussion. Moreover, the protein-protein network was also constructed in STRING ver. 12 launched at https://string-db.org, and submitted to Cytoscape ver. 3.10.2 for network analysis using a novel Cytoscape plugin cytoHubba and visualization (Shannon et al. , 2003).

### [9] LMPD: LIPID MAPS proteome database
- Authors: Dawn Cotter, A. Maer, Chittibabu Guda, Brian Saunders, S. Subramaniam
- Year: 2005
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
- DOI: 10.1093/nar/gkj122
- PMID: 16381922
- PMCID: 1347484
- Citations: 93
- Influential citations: 2
- Summary: The initial release of the LIPID MAPS Proteome Database contains 2959 records, representing human and mouse proteins involved in lipid metabolism, and this LMPD protein list was enhanced with annotations from UniProt, EntrezGene, ENZYME, GO, KEGG and other public resources.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [10] Genome-wide association study of exotic Fragaria germplasm accessions for resistance to Phytophthora crown rot in strawberry
- Authors: Mandeep Poudel, A. Gogoi, Jakob Junkers, Arne Stensvand, M. Brurberg et al.
- Year: 2026
- Venue: BMC Plant Biology
- URL: https://www.semanticscholar.org/paper/911ebef7865f6b02cfea8b42d258ff4d5dc0571e
- DOI: 10.1186/s12870-026-08186-6
- PMID: 41572166
- PMCID: 12911263
- Summary: Understanding of resistance to P. cactorum in strawberry is advanced and genetic resources that can accelerate the development of crown rot-resistant cultivars through marker-assisted breeding are identified.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > Additionally, Gene Ontology (GO) enrichment analysis indicated that 124 genes were associated with the GO biological process "response to stress" (Fig. S4).
    > Through annotation and manual curation, several putative defence associated genes were identified, including those encoding serine/threonine kinases, receptor-like protein kinases (RLKs), nucleotide-binding leucine-rich repeat proteins (NLRs) including CNLs (coiled-coil (CC)-NLRs) and TNLs (Toll/interleukin-1 receptor (TIR)-NLRs), ABC transporter ATP-binding proteins, F-box domain-containing proteins, immunity associated WRKY transcription factors, Cytochrome P450 family proteins, Ca 2+ dependent protein kinases (CDPKs), cyclic-nucleotide-gated calcium channels (CNGCs), cell wall modification enzymes (e.g., O-acetyltransferases, pectinacetylesterase inhibitors, pectinesterases), mitogen-activated protein kinases (MAPKs) and various zinc finger proteins (A20/AN1/C2H2/CCG/RING-type) (Supplementary File S3).

### [11] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
- Authors: P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al.
- Year: 2025
- Venue: Animals : an Open Access Journal from MDPI
- URL: https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
- DOI: 10.3390/ani15040484
- PMID: 40002966
- PMCID: 11852025
- Citations: 3
- Summary: Differences in surface proteins between X- and Y-chromosome-bearing bovine spermatozoa are explored to identify potential targets for sperm sexing by LC-MS/MS analysis, with 5 transmembrane proteins showing promise as markers for X-sperm.
- Evidence snippets:
  - Snippet 1 (score: 0.663)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [12] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
- Authors: Mary Kate Bonner, Daniel S. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al.
- Year: 2011
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
- DOI: 10.1371/journal.pone.0020489
- PMID: 21647379
- PMCID: 3103581
- Citations: 51
- Influential citations: 3
- Summary: This work reports the first proteomic study of the mitotic spindle from Chinese Hamster Ovary (CHO) cells and identifies proteins that are unique to the CHO spindle.
- Evidence snippets:
  - Snippet 1 (score: 0.662)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [13] GeneTools – application for functional annotation and statistical hypothesis testing
- Authors: V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al.
- Year: 2006
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
- DOI: 10.1186/1471-2105-7-470
- PMID: 17062145
- PMCID: 1630634
- Citations: 106
- Influential citations: 11
- Summary: GeneTools is the first "all in one" annotation tool, providing users with a rapid extraction of highly relevant gene annotation data for e.g. thousands of genes or clones at once.
- Evidence snippets:
  - Snippet 1 (score: 0.659)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [14] Mechanistic basis for mitigating drought tolerance by selenium application in tobacco (Nicotiana tabacum L.): a multi-omics approach
- Authors: Hua-Xin Dai, Jin-Peng Yang, Lidong Teng, Zhong Wang, Tai-Bo Liang et al.
- Year: 2023
- Venue: Frontiers in Plant Science
- URL: https://www.semanticscholar.org/paper/07c17ee022676e5580bc76c89e15da999a84c188
- DOI: 10.3389/fpls.2023.1255682
- PMID: 37799555
- PMCID: 10548829
- Citations: 4
- Summary: The integrated analysis of miRNA sequencing and metabolome highlighted the significance of the novel-nta-miR97-5p- LRR-RLK- catechin pathway in regulating drought tolerance.
- Evidence snippets:
  - Snippet 1 (score: 0.656)
    > We predicted the target genes of the identified miRNAs using psRNATarget. Gene Ontology (GO) analysis showed that these target genes are mainly involved in cellular process, metabolic process, cell, cell part, organelle, binding and catalytic activity (Figure 5A). Kyoto Encyclopedia of Genes and Genomes (KEGG) analysis revealed that these target genes were involved in translation, transcription and carbohydrate metabolism (Figure 5B). Moreover, these target genes were involved in cellular processes, environmental information processes and organismal systems (Figure 5B). We classified the resultant target genes into Groups I and II based on their predicted functions. Group I contained eleven target genes, including transcription factors, metal transporters, protein kinases and detoxificationrelated proteins (Table 2), with the identification of three transcription-related genes e.g., transcription factor bHLH30-like, squamosa promoter-binding-like protein 4 (SPL4) and homeoboxleucine zipper protein ATHB-15-like. We also detected two metal transporters (metal-nicotianamine transporter YSL7 and cation/ calcium exchanger 4-like SlCCX4) and two protein kinase genes (serine/threonine-protein kinase RUNKEL and LRR receptor-like serine/threonine-protein kinase). The other four genes included D-3-phosphoglycerate dehydrogenase 2, protein DETOXIFICATION 49-like, SPX domain-containing membrane protein At4g22990-like (SPX) and late blight resistance protein homolog R1A-10. In Group II, the targets of the four miRNAs were serine/threonine protein phosphatase 2A 55 kDa regulatory subunit B beta isoform-like (PP2A), TMV resistance protein N-like, extensin-1-like (EXT1) and Reduced Wall Acetylation 2 (RWA2). The putative secondary structures of the six novel miRNAs were also predicted (Figure 6).

### [15] The alpha-ketoacid dehydrogenase complexes of Drosophila melanogaster.
- Authors: Steven J. Marygold
- Year: 2024
- Venue: microPublication Biology
- URL: https://www.semanticscholar.org/paper/50942e603e0e14ee9195c0d7cb52db11a521f964
- DOI: 10.17912/micropub.biology.001209
- PMID: 38741935
- PMCID: 11089389
- Citations: 2
- Summary: This work identifies and classify the genes encoding all Drosophila AKDHC subunits, update their functional annotations and integrate this work into the FlyBase database.
- Evidence snippets:
  - Snippet 1 (score: 0.650)
    > Symbol: gene symbol in FlyBase -asterisk (*) indicates a gene with testis-specific expression. CG#: gene annotation ID in FlyBase. Function: component and associated EC number (where available/applicable). Key reference(s) for initial identification or genetic characterization (in a metabolic context): 1. Gruntenko et al. 1998;2. Chen et al. 2008;3. Yoon et al. 2017;4. Yap et al. 2021a;5. Yap et al. 2021b;6. Whittle et al. 2023;7. González Morales et al. 2023;8. Homem et al. 2014;9. Bonnay et al. 2020;10. Ivanova et al. 2004;11. Boyko et al. 2020;12. Liu et al. 2017;13. Li et al. 2020;14. Devilliers et al. 2021;15. Goyal et al. 2022;16. Huang et al. 2022;17. Plaçais et al. 2017;18. Dung et al. 2018;19. Rabah et al. 2023;20. Klenz et al. 1995;21. Katsube et al. 1997;22. Gándara et al. 2019;23. Lambrechts et al. 2019;24. Lee et al. 2022;25. Chen et al. 2006;26. Kim et al. 2023;27. Tsai et al. 2020. Human ortholog: gene symbol at HGNC, with % amino acid identity between the encoded protein and the Drosophila protein. Human disease: OMIM symbol for disease(s) associated with the human gene (Amberger et al. 2019) -see Extended Data File 1 for details.

### [16] Genome-wide association study, combined with bulk segregant analysis, identify plant receptors and defense related genes as candidate genes for downy mildew resistance in quinoa
- Authors: Sara Fondevilla, Álvaro Calderón-González, Borja Rojas-Panadero, Verónica Cruz, J. Matías
- Year: 2024
- Venue: BMC Plant Biology
- URL: https://www.semanticscholar.org/paper/3dca54ed77872b006b0b23971b88cbfc890c6f63
- DOI: 10.1186/s12870-024-05302-2
- PMID: 38910245
- PMCID: 11194881
- Citations: 6
- Summary: The existence of, at least, one major gene conferring resistance to this disease is demonstrated, the genomic regions involved in the trait are identified and plausible candidate genes involved in defense are provided.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > HR is the result of the recognition of pathogen effectors by the plant, unleashing effector-triggered immunity (ETI), and is activated by R-genes.In agreement with that, many of the regions associated with resistance to P. variabilis, according to our GWAS analysis, harbour plant receptor genes or resistance genes (Table 2).Especially exciting is the presence of nine of these genes located exactly in the same position as the MTAs identified by GWAS.These genes include two genes annotated as "disease resistance RPP13-like protein", the gene annotated as RGA2 mentioned above as candidate gene for the major gene conferring resistance to downy mildew in accession PI614911, one gene annotated as RGA1, other gene annotated as RGA3, another annotated as "serine/ threonine-protein kinase", a "F-box/LRR-repeat protein", a "LRR receptor-like serine/threonine-protein kinase" and a "wall-associated-receptor kinase" encoding genes (Suppl.Table S4).Plant resistance gene analogs (RGAs) act as intracellular receptors that perceive the presence of pathogen effectors by direct binding of the pathogen effector proteins, or by monitoring the modification of host proteins after associating with the pathogen, to activate multiple defense signal transductions to restrict pathogen growth [38].RGAs include nucleotide binding site leucine rich repeats, receptor like kinases, receptor like proteins, pentatricopeptide repeats and apoplastic peroxidases [39].The presence of genes similar to RPP13 in two MTAs is especially attractive, since RPP13 is a resistance gene that confers resistance to downy mildew in Arabidopsis [40].Downy mildew in Arabidopsis is caused by Peronospora parasitica, a member of the same genus as the pathogen causing downy mildew in quinoa (Peronospora variabilis).
    > Another remarkable outcome is the presence of genes encoding "Zinc finger BED domain-containing protein" in the genomic regions associated with resistance identified by GWAS.

### [17] An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models
- Authors: Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al.
- Year: 2026
- Venue: Nature Communications
- URL: https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
- DOI: 10.1038/s41467-026-75972-z
- PMID: 42669697
- PMCID: 13526818
- Summary: An embedding-based statistical framework is developed that transforms gene and function descriptions into vector representations, enabling statistical testing of gene-gene and gene-function relationships and quantitative prioritization of de novo functional hypotheses inferred by LLMs.
- Evidence snippets:
  - Snippet 1 (score: 0.646)
    > This study focused on human protein-coding genes because they represent the most well-annotated portion of the genome, with reliable functional summaries, and are typically the primary focus of functional annotation analyses. We obtained functional summaries of individual genes from three widely used databases: (1) NCBI Gene 32 , which curates descriptions from multiple sources such as RefSeq under the "Summary" field, (2) Alliance of Genome Resources 33 , where descriptions are generated from structured gene data such as ontology terms and ortholog sets under the "Automated Description" field, and (3) UniProt 34 , which focuses on protein-level functions under the "Function" field. The NCBI database was accessed using its API, Entrez Programming Utilities (E-utilities), while descriptions from Alliance of Genome Resources and UniProt were directly downloaded from their respective databases. The number of genes retrieved from each database was 18,753 from NCBI, 18,600 from Alliance of Genome Resources, and 16,343 from UniProt, with 16,329 genes shared across all three databases. We preprocessed the gene descriptions to remove irrelevant information, such as source attribution found in NCBI descriptions (e.g., "[provided by RefSeq, Jul 2008]"). After preprocessing, each gene name was combined with its corresponding functional summary and input into the embedding models to generate gene embeddings.
    > We also generated de novo gene descriptions using an RAG approach. For each gene, we first retrieved the 100 most relevant sentences from PubMed and PubMed Central via the LitSense 35 API using biological context-specific queries: "function of 'gene symbol'", "'gene symbol' pathway association", "'gene symbol' transcriptional response", "'gene symbol' disease association". The numbers of genes under each biological context were 18,723, 18,723, 18,288, and 18,548, respectively. To restrict the temporal scope of knowledge and ensure controlled evaluation, we filtered the retrieved sentences to retain only those from publications published in or before October 2023, consistent with the versions of curated gene databases used in this study.

### [18] OrthoDB: the hierarchical catalog of eukaryotic orthologs in 2011
- Authors: R. Waterhouse, E. Zdobnov, F. Tegenfeldt, Jia Li, E. Kriventseva
- Year: 2010
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/486f2d7b7885efe41ef9ceb90d7daf647b266aa9
- DOI: 10.1093/nar/gkq930
- PMID: 20972218
- PMCID: 3013786
- Citations: 155
- Influential citations: 6
- Summary: The updated OrthoDB catalog of eukaryotic orthologs delineated at each radiation of the species phylogeny in an explicitly hierarchical manner of over 100 species of vertebrates, arthropods and fungi is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.642)
    > Annotations describing putative functional attributes were sourced from UniProt (24), as well as from species-specific resources including Mouse Genome Informatics (MGI) (42), FlyBase (25) and Saccharomyces Genome Database (SGD) (43). UniProt identifier cross-referencing allowed mapping of gene annotations to the gene sets retrieved from Ensembl and other sources. The UniProt data were also employed to comprehensively map gene names and synonyms, as well as secondary gene identifiers and cross-referenced database gene identifiers, e.g. RefSeq, Entrez GeneID, GenBank, Protein Data Bank and Mendelian Inheritance in Man, as well as assigned Gene Ontology (GO) (44) attributes. The species-specific model organism databases (MGI, FlyBase and SGD) provided mapping to additional gene synonyms and identifiers as well as selected controlled-vocabulary gene phenotypes from relevant experimental data (Supplementary Table S2). Protein domain signatures were retrieved from InterPro (45) matches to the UniProt Archive (UniParc) of non-redundant protein sequences.

### [19] SNP-based bulk segregant analysis revealed disease resistance QTLs associated with northern corn leaf blight in maize
- Authors: Rui-Ning Zhai, A. Huang, Run-Xiu Mo, Chenglin Zou, Xin-Xing Wei et al.
- Year: 2022
- Venue: Frontiers in Genetics
- URL: https://www.semanticscholar.org/paper/930b7d9b1a8a67d7f2b5191b3c780922fb2dabd1
- DOI: 10.3389/fgene.2022.1038948
- PMID: 36506330
- PMCID: 9732028
- Citations: 12
- Influential citations: 1
- Summary: This study identifies significant QTLs associated with NCLB by utilizing next-generation sequencing-based bulked-segregant analysis (BSA), and identifies 27 candidate genes associated with disease resistance in the QTL regions based on annotation information.
- Evidence snippets:
  - Snippet 1 (score: 0.638)
    > ZmWAK-RLK1 gene has been previously characterized for involvement in NCLB in maize (Hurni et al., 2015;Yang et al., 2017;Yang et al., 2019b;Yang et al., 2021a). The annotation information regarding ZmWAK-RLK1 suggested involvement in several pathways, including protein phosphorylation, cytoplasmic vesicle, protein serine/threonine kinase activity, and ATP binding pathway in this study (Li et al., 2020). Therefore, we further screened genes associated with non-synonymous SNPs using annotation information and identified 27 genes on chromosomes 2 and 5 (Table 2). Q2-5 contains 14 annotated genes associated with pathways related to protein phosphorylation, cytoplasmic vesicle, protein serine/threonine kinase activity, and ATP binding pathway. Q2-5 genes associated with disease resistance encode cyclin11, receptor-like kinase, Putative leucyl-tRNA synthetase, Protein kinase superfamily protein, leucine-rich repeat receptorlike serine, Protein kinase superfamily protein, LRR receptor-like serine/threonine-protein kinase, Serine/threonine-protein kinase UCNL, ATP-dependent DNA helicase, Probable inactive receptor kinase, CHROMATIN REMODELING 5, ATP-dependent DNA helicase chloroplastic, Wall-associated kinase 2-like protein, and ATP-dependent DNA helicase. Mitogen-activated protein kinase 9, Mitogen-activated protein kinase 9, Atypical receptor-like kinase MARK, and DEAD-box ATP-dependent RNA helicase 21 were identified in Q5-1. Moreover, QTLs Q2-4, Q2-5, and Q5-1 were identified with multiple genes associated with disease resistance pathways; therefore, we consider these QTLs as candidates for further functional verification. Further molecular insight into the functions of genes associated with candidate QTLs can provide a comprehensive overview of quantitative disease resistance against NCLB in maize.

### [20] Transcriptome analysis of safflower (Carthamus tinctorius L.) reveals the roles of osmotic adjustment and regulatory mechanisms in response to drought stress
- Authors: Fahime Sabzeali, A. Ahmadikhah, N. Farrokhi, Reza Haghi
- Year: 2026
- Venue: BMC Plant Biology
- URL: https://www.semanticscholar.org/paper/579f3d31d4e7209297d486a501a9cc29e478f339
- DOI: 10.1186/s12870-026-08366-4
- PMID: 41680614
- PMCID: 12998085
- Summary: Functional enrichment analysis indicated that in addition to canonical pathways of response to drought stress (such as metabolic pathways and secondary metabolite biosynthesis), revealed reconnaissance of more specific pathways, including peroxisome, autophagy, photosynthesis, glycerolipid metabolism, beta-alanine biosynthesis, and protein processing.
- Evidence snippets:
  - Snippet 1 (score: 0.633)
    > BLASTp exhibited 603 downregulated genes (with 21.8%-99.7% identity to Uniprot proteins) and 436 upregulated genes (with 24.7%-100% identity to Uniprot proteins). Orthologs found in A. thaliana for only 665 DEGs, including 294 (67.43%) upregulated and 371 (61.5%) downregulated genes. In total, 24 protein classes were recognized for the safflower seedlings transcriptome in response to drought stress. Proteins with the highest abundance were associated with transcription factors (TFs, n = 47), protein kinases (PKs, n = 51), and transferases (n = 58) (Fig. 4A; Table 3). Thirty-nine upregulated TFs (in the order of gene frequency belonging to HD-ZIP, ERF, CO-like, bZIP, TALE, NAC, C2H2, FAR1, GRAS, MYB-related, and Trihelix families) (Fig. 4B), and 59 TFs with decreased expression (in the order of gene frequency belonging to bHLH, GATA, HD-ZIP, bZIP, MYB, LBD, WRKY, G2-like, DBB, and CO-like families) were recognized among DEGs (Fig. 4C). The protein kinases were achieved in this study correspond to 61 safflower gene IDs in a homology search with A. thaliana (Supplementary Table S7). Twenty-six (40.9%) kinase proteins belong to the serine/threonine kinase (STK) subgroup of plants' receptor protein kinases (RPKs) and one was found to be related to histidine kinase (HK2). The STK and AHK2 implicate the phosphorylation of serine/threonine and histidine residues. The HKs are important in signal transduction in response to abiotic and biotic stresses [32].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Juan Wang, Yi Liu, Xi-Zhao Chen, Mansheng Li, Yunping Zhu (2024). Protocol for identifying and comparing molecular prognosis subtypes of IgAN using R. STAR Protocols. https://www.semanticscholar.org/paper/6794ab2424155d4a65b28cd139731c21d4d37aa2
2. Brigitte Waegele, Irmtraud Dunger-Kaltenbach, G. Fobo, Corinna Montrone, H-Werner Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
3. Xiao Yang, Shyamasree Saha, Aravind Venkatesan, S. Tirunagari, Vid Vartak et al. (2023). Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms. Scientific Data. https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
4. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
5. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöery, R. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
6. Christina M McCosker, E. Unal, Alayna K. Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
7. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
8. Wisam Taher Muslim, L. J. Mohammad, Munaf M. Naji, Isaac Karimi, Matheel D. Al-Sabti et al. (2025). Synthesis, characterization, and computational evaluation of some synthesized xanthone derivatives: focus on kinase target network and biomedical properties. Frontiers in Pharmacology. https://www.semanticscholar.org/paper/659ab502877a1d6b5ab7ce45fa51f0f9a13dcf24
9. Dawn Cotter, A. Maer, Chittibabu Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
10. Mandeep Poudel, A. Gogoi, Jakob Junkers, Arne Stensvand, M. Brurberg et al. (2026). Genome-wide association study of exotic Fragaria germplasm accessions for resistance to Phytophthora crown rot in strawberry. BMC Plant Biology. https://www.semanticscholar.org/paper/911ebef7865f6b02cfea8b42d258ff4d5dc0571e
11. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
12. Mary Kate Bonner, Daniel S. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
13. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
14. Hua-Xin Dai, Jin-Peng Yang, Lidong Teng, Zhong Wang, Tai-Bo Liang et al. (2023). Mechanistic basis for mitigating drought tolerance by selenium application in tobacco (Nicotiana tabacum L.): a multi-omics approach. Frontiers in Plant Science. https://www.semanticscholar.org/paper/07c17ee022676e5580bc76c89e15da999a84c188
15. Steven J. Marygold (2024). The alpha-ketoacid dehydrogenase complexes of Drosophila melanogaster.. microPublication Biology. https://www.semanticscholar.org/paper/50942e603e0e14ee9195c0d7cb52db11a521f964
16. Sara Fondevilla, Álvaro Calderón-González, Borja Rojas-Panadero, Verónica Cruz, J. Matías (2024). Genome-wide association study, combined with bulk segregant analysis, identify plant receptors and defense related genes as candidate genes for downy mildew resistance in quinoa. BMC Plant Biology. https://www.semanticscholar.org/paper/3dca54ed77872b006b0b23971b88cbfc890c6f63
17. Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al. (2026). An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models. Nature Communications. https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
18. R. Waterhouse, E. Zdobnov, F. Tegenfeldt, Jia Li, E. Kriventseva (2010). OrthoDB: the hierarchical catalog of eukaryotic orthologs in 2011. Nucleic Acids Research. https://www.semanticscholar.org/paper/486f2d7b7885efe41ef9ceb90d7daf647b266aa9
19. Rui-Ning Zhai, A. Huang, Run-Xiu Mo, Chenglin Zou, Xin-Xing Wei et al. (2022). SNP-based bulk segregant analysis revealed disease resistance QTLs associated with northern corn leaf blight in maize. Frontiers in Genetics. https://www.semanticscholar.org/paper/930b7d9b1a8a67d7f2b5191b3c780922fb2dabd1
20. Fahime Sabzeali, A. Ahmadikhah, N. Farrokhi, Reza Haghi (2026). Transcriptome analysis of safflower (Carthamus tinctorius L.) reveals the roles of osmotic adjustment and regulatory mechanisms in response to drought stress. BMC Plant Biology. https://www.semanticscholar.org/paper/579f3d31d4e7209297d486a501a9cc29e478f339