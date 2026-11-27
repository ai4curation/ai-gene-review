---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-11-26T19:02:09.795861'
end_time: '2026-11-26T19:02:15.510927'
duration_seconds: 5.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KRT9
  gene_symbol: KRT9
  uniprot_accession: P35527
  protein_description: 'RecName: Full=Keratin, type I cytoskeletal 9; AltName: Full=Cytokeratin-9;
    Short=CK-9; AltName: Full=Keratin-9; Short=K9;'
  gene_info: Name=KRT9 {ECO:0000312|HGNC:HGNC:6447};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the intermediate filament family.
  protein_domains: IF_conserved. (IPR018039); IF_rod_dom. (IPR039008); Keratin_I.
    (IPR002957); Filament (PF00038)
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
- **UniProt Accession:** P35527
- **Protein Description:** RecName: Full=Keratin, type I cytoskeletal 9; AltName: Full=Cytokeratin-9; Short=CK-9; AltName: Full=Keratin-9; Short=K9;
- **Gene Information:** Name=KRT9 {ECO:0000312|HGNC:HGNC:6447};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the intermediate filament family.
- **Key Domains:** IF_conserved. (IPR018039); IF_rod_dom. (IPR039008); Keratin_I. (IPR002957); Filament (PF00038)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRT9" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRT9' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRT9** (gene ID: KRT9, UniProt: P35527) in human.

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

### [1] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
- Authors: P. Pinto-Pinho, J. Quelhas, F. Impens, Sara Dufour, D. Van Haver et al.
- Year: 2025
- Venue: Animals : an Open Access Journal from MDPI
- URL: https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
- DOI: 10.3390/ani15040484
- PMID: 40002966
- PMCID: 11852025
- Citations: 3
- Summary: Differences in surface proteins between X- and Y-chromosome-bearing bovine spermatozoa are explored to identify potential targets for sperm sexing by LC-MS/MS analysis, with 5 transmembrane proteins showing promise as markers for X-sperm.
- Evidence snippets:
  - Snippet 1 (score: 0.767)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [2] Protocol for identifying and comparing molecular prognosis subtypes of IgAN using R
- Authors: Juan Wang, Yi Liu, Xi-Zhao Chen, Man-Sheng Li, Yunping Zhu
- Year: 2024
- Venue: STAR Protocols
- URL: https://www.semanticscholar.org/paper/6794ab2424155d4a65b28cd139731c21d4d37aa2
- DOI: 10.1016/j.xpro.2024.103138
- PMID: 38878284
- PMCID: 11234001
- Summary: A general workflow for identifying and comparing molecular subtypes of disease using proteomics data using R software is presented and steps for data preprocessing, feature selection, determination of subtypes, and functional interpretation of subtypes are described.
- Evidence snippets:
  - Snippet 1 (score: 0.744)
    > The UniProt database (https://www.uniprot.org/) can perform ID mapping on the UniProt ID of each protein to obtain corresponding annotation information, including Entry name, Protein name, Gene name, Organism, and Length.
    > Note: Considering the efficiency and readability of subsequent analysis, users need to convert the ID in the raw data. In this protocol, we choose to convert UniProt ID to Gene Symbol, and when multiple UniProt ID correspond to one Gene Symbol, we can use the make.unique() function to add a serial number to Gene Symbol to make it unique.
    > 7. Group samples by type.

### [3] LMPD: LIPID MAPS proteome database
- Authors: Dawn Cotter, Andreia Maer, C. Guda, Brian Saunders, S. Subramaniam
- Year: 2005
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
- DOI: 10.1093/nar/gkj122
- PMID: 16381922
- PMCID: 1347484
- Citations: 94
- Influential citations: 2
- Summary: The initial release of the LIPID MAPS Proteome Database contains 2959 records, representing human and mouse proteins involved in lipid metabolism, and this LMPD protein list was enhanced with annotations from UniProt, EntrezGene, ENZYME, GO, KEGG and other public resources.
- Evidence snippets:
  - Snippet 1 (score: 0.734)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [4] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.731)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [5] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
- Authors: P. Hornbeck, J. Kornhauser, Sasha L. Tkachev, Bin Zhang, E. Skrzypek et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
- DOI: 10.1093/nar/gkr1122
- PMID: 22135298
- PMCID: 3245126
- Citations: 1660
- Influential citations: 161
- Summary: PhosphoSitePlus (http://www.phosphosite.org) is an open, comprehensive, manually curated and interactive resource for studying experimentally observed post-translational modifications, primarily of human and mouse proteins. It encompasses 1 30 000 non-redundant modification sites, primarily phosphorylation, ubiquitinylation and acetylation. The interface is designed for clarity and ease of navigation. From the home page, users can launch simple or complex searches and browse high-throughput d...
- Evidence snippets:
  - Snippet 1 (score: 0.728)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [6] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
- Authors: Ralf C. Mueller, Nicolai Mallig, J. Smith, Lél Eöery, R. Kuo et al.
- Year: 2020
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
- DOI: 10.1186/s12859-020-03764-3
- PMID: 33176685
- PMCID: 7661159
- Citations: 7
- Summary: The Avian Immunome DB (Avimm) for easy gene property extraction as exemplified by avian immune genes is presented and described, which contains 1170 distinct avian immune genes with canonical gene symbols and 612 synonyms across 363 bird species.
- Evidence snippets:
  - Snippet 1 (score: 0.719)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [7] Identifying orthologs with OMA: A primer
- Authors: Monique Zahn-Zabal, C. Dessimoz, N. Glover
- Year: 2020
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
- DOI: 10.12688/f1000research.21508.1
- PMID: 32089838
- PMCID: 7014581
- Citations: 41
- Summary: This Primer is organized in two parts and provides all the necessary background information to understand the concepts of orthology, how to infer them and the different subtypes of Orthology in OMA, as well as what types of analyses they should be used for.
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [8] Working with Worms: Caenorhabditis elegans as a Model Organism
- Authors: P. Meneely, C. Dahlberg, Jacqueline K. Rose
- Year: 2019
- Venue: Current Protocols Essential Laboratory Techniques
- URL: https://www.semanticscholar.org/paper/a7e7665b4cfc67b3e1c04e29a8f86e56c5e12804
- DOI: 10.1002/cpet.35
- Citations: 114
- Influential citations: 3
- Summary: The nematode worm Caenorhabditis elegans has become one of the most widely used and versatile models for nearly all aspects of biological and genomic research.
- Evidence snippets:
  - Snippet 1 (score: 0.703)
    > Current Protocols Essential Laboratory Techniques 1. Choose one of the following gene IDs for your subsequent analysis. Use the entire DNA sequence, including both the uppercase and lowercase letters.
    > C25E10.12 D1022.1 F55A11.3 2. To determine what information is already available on these genes, go to the BLAST website (http://blast.ncbi.nlm.nih.gov/Blast.cgi), enter your sequence and determine the results.
    > 3. The sequences above are the entire unspliced transcripts. Look for the best mRNA/cDNA match for the following questions:
    > a. How far down the list of matches do you need to go in order to find this match? b. C. elegans genes are named with three to four lowercase letters, followed by a dash and one to three numerals. Based on the gene results, what are the names of these genes (Unnamed genes are designated by a longer string of letters and numbers that describe a genes position relative to a short portion of the genome.) c. What is the e-value of the top BLAST hit that you obtained with the gene you chose?
    > 4. From this point forward, choose ONE gene to follow up on.
    > 5. Copy the corresponding Alignment information, accession number, and the description of your BLAST hit below. Locate the information for the following questions.
    > a. If you click on the Sequence ID of your BLAST hit, you will be redirected to the NCBI resource page for that gene. Are there any publications listed for this protein (i.e., has it been studied before)? How could that information be useful for your future studies of this gene? b. What is the predicted protein sequence for your gene (include it below)? Include the number of amino acids in your protein. c. Click on the GeneID link (located under FEATURES within the "gene" description section). What is the gene immediately upstream of your gene? d. Click on "Protein" (right hand link under "Related Information"). You can then use the "Related information" menu to find Conserved Domains. Are there any conserved domains present in your protein? What function does/do it/they serve?

### [9] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
- Authors: Christina M. McCosker, E. Unal, Alayna K. Gigliotti, W. Puryear, J. Runstadler et al.
- Year: 2025
- Venue: Molecular ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 4
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.701)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [10] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
- Authors: Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, A. Zlotnicki, Nicholas A. Dillon et al.
- Year: 2021
- Venue: mSystems
- URL: https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
- DOI: 10.1128/mSystems.00673-21
- PMID: 34726489
- PMCID: 8562490
- Citations: 18
- Summary: This work systematically updates the functional genome annotation of Mycobacterium tuberculosis virulent type strain H37Rv and identifies hundreds of high-confidence candidates for mechanisms of antibiotic resistance, virulence factors, and basic metabolism and other functions key in clinical and basic tuberculosis research.
- Evidence snippets:
  - Snippet 1 (score: 0.701)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [11] CRONOS: the cross-reference navigation server
- Authors: B. Waegele, I. Dunger-Kaltenbach, G. Fobo, Corinna Montrone, H. Mewes et al.
- Year: 2008
- Venue: Bioinformatics
- URL: https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
- DOI: 10.1093/bioinformatics/btn590
- PMID: 19010804
- PMCID: 2638938
- Citations: 20
- Summary: CRONOS, a cross-reference server that contains entries from five mammalian organisms presented by major gene and protein information resources, is developed, which shows that the cross-references are highly accurate.
- Evidence snippets:
  - Snippet 1 (score: 0.700)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [12] BioXpress: an integrated RNA-seq-derived gene expression database for pan-cancer analysis
- Authors: Quan Wan, Hayley M. Dingerdissen, Yu Fan, N. Gulzar, Yang Pan et al.
- Year: 2015
- Venue: Database: The Journal of Biological Databases and Curation
- URL: https://www.semanticscholar.org/paper/2852ba7d092a2814e304d9dfbe5a79fa4e0250f8
- DOI: 10.1093/database/bav019
- PMID: 25819073
- PMCID: 4377087
- Citations: 101
- Influential citations: 1
- Summary: BioXpress is a gene expression and cancer association database in which the expression levels are mapped to genes using RNA-seq data obtained from The Cancer Genome Atlas, International cancer Genome Consortium, Expression Atlas and publications.
- Evidence snippets:
  - Snippet 1 (score: 0.689)
    > Scientists can find querying datasets useful to identify expression levels between disease and normal pairs to discover differential expression for a gene. They may also want to research on potential biomarkers or pathways that lead to tumor formation or want to explore the overall expression of specific genes across multiple cancer types. Users can search BioXpress using HGNCapproved gene symbols (HUGO Gene Nomenclature Committee), UniProtKB/Swiss-Prot accessions or RefSeq accessions. Differentially expressed genes for a specific cancer type can also be retrieved. Additionally, all data in BioXpress, including lists of genes significantly differentially expressed in two or more cancer types, can be downloaded.
    > Searching using gene name (gene/protein-centric search)
    > A search using the HGNC-approved gene symbol or UniProt/RefSeq accession retrieves differential expression information (cancer vs. normal), tumor-only expression data (where normal samples are not available) and baseline expression information from normal human tissues (Illumina Human Body Map Project). The example below provides an overview of a gene/protein-centric search.

### [13] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
- Authors: L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Si-Qian He, Sunghwan Kim et al.
- Year: 2021
- Venue: Frontiers in Research Metrics and Analytics
- URL: https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
- DOI: 10.3389/frma.2021.689059
- PMID: 34322655
- PMCID: 8311438
- Citations: 25
- Summary: The literature knowledge panels developed and implemented in PubChem help to uncover and summarize important relationships between chemicals, genes, proteins, and diseases by analyzing co-occurrences of terms in biomedical literature abstracts.
- Evidence snippets:
  - Snippet 1 (score: 0.689)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [14] Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops
- Authors: Yi Zheng, Shan Wu, Yang Bai, Hong-He Sun, C. Jiao et al.
- Year: 2018
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/a7bb1e82b8172252d79ee35170dfe038c4b17d78
- DOI: 10.1093/nar/gky944
- PMID: 30321383
- PMCID: 6324010
- Citations: 193
- Influential citations: 9
- Summary: The Cucurbit Genomics Database has been developed using the Tripal toolkit and two new tools have been developed, a ‘SyntenyViewer’ to view genome synteny between different cucurbit species and an ‘RNA-Seq’ module to analyze and visualize gene expression profiles.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > The submenu provides links to a pathway database, a genome browser, an FTP site for downloading genome and gene sequences and annotations, and bioinformatics tools such as BLAST, batch query and basic search functions.
    > A total of 265 334 protein-coding genes have been predicted from these 10 genomes and included in the database. A standard and unified procedure has been developed to comprehensively annotate predicted protein-coding genes. First, protein sequences of the predicted genes are compared against the GenBank non-redundant protein (nr), UniProt (TrEMBL and SwissProt), and Arabidopsis protein databases using the BLAST program with an E-value cutoff of 1e-4. The protein sequences are further compared against the InterPro database using InterProScan (21) to identify functional protein domains. The BLAST results D1130 Nucleic Acids Research, 2019, Vol. 47, Database issue against the nr database and the identified InterPro domains are fed to the Blast2GO program (22) for assigning gene ontology (GO) terms to protein-coding genes, and the BLAST results against the UniProt and Arabidopsis protein databases are loaded into the AHRD program (https: //github.com/groupschoof/AHRD) to assign concise, informative and precise functional descriptions of genes. The top BLAST hits (homologs), GO terms and InterPro domains assigned to each of the protein-coding genes have been imported into CuGenDB using Tripal Analysis Extension Modules (16). The functional descriptions generated by AHRD are loaded into the database using an inhouse Perl script. Each gene has a detailed feature page in the database that contains all the related sequence and annotation information; the gene feature page is divided into different sections based on the content types (Figure 1).

### [15] Effects of 6-Hydroxykaempferol: A Potential Natural Product for Amelioration of Tendon Impairment
- Authors: Tsz N. Mok, Q. He, Xiao-Xi Zhang, Tat-Hang Sin, Hua-Jun Wang et al.
- Year: 2022
- Venue: Frontiers in Pharmacology
- URL: https://www.semanticscholar.org/paper/5051cd4b77d748a62d6efb4ca95e7bcac106c654
- DOI: 10.3389/fphar.2022.919104
- PMID: 35935848
- PMCID: 9354238
- Citations: 4
- Summary: 6-hydroxykaempferol, which reportedly promotes the proliferation of microvascular endothelial cells, is a molecule found in SHT and it is found that it promoted the proliferation and migration of tendon fibroblasts and elevated tendon repair-related gene expression.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > The GeneCards (RRID:SCR_002773) database was used to search for reported tendinopathy-related genes by entering keywords of tendon injuries, tendon rupture, tendon healing, and tendon adhesion for target-based drug applications. The potential tendon-healing targets of the active components of SHT matched the potential gene targets of the active ingredients of SHT. According to the UniProt database (https://www.uniprot.org/), the full names of the target proteins were transformed into gene symbols based on the UniProt ID (The UniProt Consortium, 2017) (Figure 1). The database leverages the unique rich combinatorial annotations of GeneCards. The GeneCards database provides direct links to generelated research reagents, such as antibodies, recombinant proteins, DNA clones, and inhibitory RNAs, and lists of gene-related drugs and compounds. GeneCards was used to depict the GeneCards Inferred Functionality Score annotation landscape tool for scoring the functional status of genes (Fishilevich et al., 2016).

### [16] An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models
- Authors: Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al.
- Year: 2026
- Venue: Nature Communications
- URL: https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
- DOI: 10.1038/s41467-026-75972-z
- PMID: 42669697
- PMCID: 13526818
- Citations: 1
- Summary: An embedding-based statistical framework is developed that transforms gene and function descriptions into vector representations, enabling statistical testing of gene-gene and gene-function relationships and quantitative prioritization of de novo functional hypotheses inferred by LLMs.
- Evidence snippets:
  - Snippet 1 (score: 0.681)
    > This study focused on human protein-coding genes because they represent the most well-annotated portion of the genome, with reliable functional summaries, and are typically the primary focus of functional annotation analyses. We obtained functional summaries of individual genes from three widely used databases: (1) NCBI Gene 32 , which curates descriptions from multiple sources such as RefSeq under the "Summary" field, (2) Alliance of Genome Resources 33 , where descriptions are generated from structured gene data such as ontology terms and ortholog sets under the "Automated Description" field, and (3) UniProt 34 , which focuses on protein-level functions under the "Function" field. The NCBI database was accessed using its API, Entrez Programming Utilities (E-utilities), while descriptions from Alliance of Genome Resources and UniProt were directly downloaded from their respective databases. The number of genes retrieved from each database was 18,753 from NCBI, 18,600 from Alliance of Genome Resources, and 16,343 from UniProt, with 16,329 genes shared across all three databases. We preprocessed the gene descriptions to remove irrelevant information, such as source attribution found in NCBI descriptions (e.g., "[provided by RefSeq, Jul 2008]"). After preprocessing, each gene name was combined with its corresponding functional summary and input into the embedding models to generate gene embeddings.
    > We also generated de novo gene descriptions using an RAG approach. For each gene, we first retrieved the 100 most relevant sentences from PubMed and PubMed Central via the LitSense 35 API using biological context-specific queries: "function of 'gene symbol'", "'gene symbol' pathway association", "'gene symbol' transcriptional response", "'gene symbol' disease association". The numbers of genes under each biological context were 18,723, 18,723, 18,288, and 18,548, respectively. To restrict the temporal scope of knowledge and ensure controlled evaluation, we filtered the retrieved sentences to retain only those from publications published in or before October 2023, consistent with the versions of curated gene databases used in this study.

### [17] KlinkPPI: Single Point of Access to Protein-Protein Interactions Across Databases
- Authors: Ahmad Lutfi, Sukrit Dang, Robert Warneke, Lutz Fischer, J. Rappsilber
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/eca10a7c69be47729504f5df3ccd660dd62a4381
- DOI: 10.64898/2026.08.02.742057
- Summary: KlinkPPI is a web server that retrieves, compares and exports PPI evidence from STRING, BioGRID, IntAct, CORUM, HuRI and Predictomes from a single query, and deliberately does not merge heterogeneous confidence scores, nor collapse functional associations, complex co-membership, binary interactions and structural predictions into a single consensus network.
- Evidence snippets:
  - Snippet 1 (score: 0.679)
    > KlinkPPI accepts UniProtKB accessions, NCBI Gene identifiers, Ensembl identifiers and gene names. Non-UniProt identifiers are mapped to UniProtKB through the UniProt identifier-mapping API, with the supplied taxonomy identifier used to restrict the mapping where available. When the user does not specify an organism, the taxonomy identifier is obtained from the resolved UniProtKB entry. UniProtKB was selected as the principal query identifier because it provides extensive cross-references between protein, gene and organism-specific identifier systems.
    > Gene-name searches were performed against the UniProtKB search service using both the submitted gene name and the selected taxonomy identifier. Candidate entries were ranked by exact agreement with the reported gene symbols, followed by UniProt review status and accession. The user can therefore distinguish between multiple proteins associated with the same or similar gene names before performing the PPI search.
    > For HuRI queries, UniProtKB accessions were additionally mapped to Ensembl gene identifiers using the Ensembl cross-references provided in the corresponding UniProtKB entry. When no UniProtKB mapping was available for a HuRI interactor, the original Ensembl identifier was retained. This avoids discarding interactions merely because a cross-reference is unavailable. Ensembl provides complementary gene-centred annotation and identifier mapping across supported genomes. Species names were normalized independently of protein identifiers. User-provided names were converted to a case-insensitive normalized representation and compared with scientific names, common names and database-specific aliases. Ambiguous species names produced candidate suggestions rather than being assigned automatically. The resolved NCBI taxonomy identifier was subsequently used to determine which PPI resources support the selected organism.

### [18] GeneTools – application for functional annotation and statistical hypothesis testing
- Authors: V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al.
- Year: 2006
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
- DOI: 10.1186/1471-2105-7-470
- PMID: 17062145
- PMCID: 1630634
- Citations: 108
- Influential citations: 11
- Summary: GeneTools is the first "all in one" annotation tool, providing users with a rapid extraction of highly relevant gene annotation data for e.g. thousands of genes or clones at once.
- Evidence snippets:
  - Snippet 1 (score: 0.677)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [19] ActSeekN: A Structural-Motif–Based Pipeline for Interpretable Enzyme Function Annotation
- Authors: Sandra Castillo, Chunhao Gu, Paula Jouhten, Gopal Peddinti, O. H. Samuli Ollila
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/685563319e26ee3350cb480e1316c1a8906e29e0
- DOI: 10.64898/2026.04.24.720574
- Summary: ActSeekN is developed, a structural-motif–based functional annotation pipeline that combines the ActSeek active-site search algorithm with a newly constructed large-scale reference database derived from AlphaFold-predicted structures, UniProt annotations, and curated catalytic residue information that enables rapid and scalable identification of conserved catalytic motifs across structurally related proteins.
- Evidence snippets:
  - Snippet 1 (score: 0.675)
    > To demonstrate that ActSeekN can to improve functional annotation of real organisms, we applied it to a common eukaryotic model and application workhorse, yeast Saccharomyces cerevisiae (reference strain S288C). ActSeekN achieved an overall prediction accuracy of 88.9%. ActSeekN completed 192 previously incomplete EC numbers. For genes lacking EC annotations in UniProt but associated with Gene Ontology (GO) molecular function terms (324 genes), the predicted EC numbers were evaluated for consistency by comparing the enzymatic activities implied by the EC assignments with the corresponding GO functional descriptions. In most cases, the assigned EC numbers matched the known or expected molecular functions of the proteins. Representative cases of these updates-including molecular chaperones, transporters, metabolic enzymes, and previously uncharacterized proteins-are summarized in Table 1. This table highlights how ActSeekN's predictions align with or refine existing functional annotations, offering new enzymatic insights for several proteins lacking experimental characterization.
    > In some cases, the function assigned by ActSeekN did not match the UniProt annotation, or the true function of the gene remains unknown. A notable example is the protein P40037 associated with the HMF1 gene (YER057C). It is originally annotated as a high-dosage growth inhibitor, whereas ActSeekN predicted it to be a 2-iminobutanoate/2-iminopropanoate deaminase (EC 3.5.99.10). Structural superposition of P40037 protein with the representative enzyme for EC 3.5.99.10 in the ActSeekNDB revealed that both share identical catalytic amino acids and a perfectly matched overall fold (Fig. 4). Similarly, the protein P42840 associated with gene N0342 (YNL320W), currently annotated in UniProt as an uncharacterized membrane protein, was assigned by ActSeekN as a palmitoylprotein thioesterase (ABHD10, EC 3.1.2.22).

### [20] Detection of gene annotations and protein-protein interaction associated disorders through transitive relationships between integrated annotations
- Authors: M. Masseroli, Arif Canakoglu, Massimiliano Quigliatti
- Year: 2015
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/8d304f9052541ebc058cb23bcf2516938707836b
- DOI: 10.1186/1471-2164-16-S6-S5
- PMID: 26046679
- PMCID: 4460591
- Citations: 6
- Summary: A software procedure that effectively detects and supplement consistent biomolecular annotations not present in the integrated sources and intrinsically provides their in silico evidence based on available data.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > In so doing, more than half of the genes without known functional annotation results having specific transferred GO functional annotation(s), i.e. with high GO level.
    > Author Statement (NAS)" evidence) of the Swiss-Prot reviewed human Putative insulin-like growth factor 2-associated protein (IG2R_HUMAN). In major databases this protein is not defined as encoded by the IGF2 human gene, which results encoding the Insulin-like growth factor II (IGF2_HUMAN) protein and its isoforms. Such isoforms do not include the IG2R_HUMAN protein, although since 1988 a paper describes it as one of the alternative splicing forms encoded by the IGF2 human gene [18]. Correctness of the new annotation is also supported by, and in agreement with, other GO annotations already available for the IGF2 human gene (Figure 6). In particular, it is not contradictory with the insulin like growth factor receptor binding annotation known for the IGF2 human gene; in fact, the IGF2 human gene encodes both the two alternative splicing forms above mentioned [18], which have different binding affinity within the IGF signaling regulatory system. The detection of this non-trivial gene annotation (i.e. not directly coming from the annotations of a protein explicitly known as encoded by the gene) leverages the power not only of the transitive relationship method, but also of the protein similarity data integrated in the GPKB [13]. In fact, these data include the association of the IG2R_HUMAN protein (P09565 UniProt AC) with the AAL55889 and AAY40360 EMBL/GenBank protein IDs, which are also associated with the IGF2 human gene; thus, they transitively associate the IG2R_HUMAN protein with the IGF2 human gene as another of its encoded isoforms (Figure 3).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. P. Pinto-Pinho, J. Quelhas, F. Impens, Sara Dufour, D. Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
2. Juan Wang, Yi Liu, Xi-Zhao Chen, Man-Sheng Li, Yunping Zhu (2024). Protocol for identifying and comparing molecular prognosis subtypes of IgAN using R. STAR Protocols. https://www.semanticscholar.org/paper/6794ab2424155d4a65b28cd139731c21d4d37aa2
3. Dawn Cotter, Andreia Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. Mary Kate Bonner, Daniel S. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
5. P. Hornbeck, J. Kornhauser, Sasha L. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
6. Ralf C. Mueller, Nicolai Mallig, J. Smith, Lél Eöery, R. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
7. Monique Zahn-Zabal, C. Dessimoz, N. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
8. P. Meneely, C. Dahlberg, Jacqueline K. Rose (2019). Working with Worms: Caenorhabditis elegans as a Model Organism. Current Protocols Essential Laboratory Techniques. https://www.semanticscholar.org/paper/a7e7665b4cfc67b3e1c04e29a8f86e56c5e12804
9. Christina M. McCosker, E. Unal, Alayna K. Gigliotti, W. Puryear, J. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
10. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, A. Zlotnicki, Nicholas A. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
11. B. Waegele, I. Dunger-Kaltenbach, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
12. Quan Wan, Hayley M. Dingerdissen, Yu Fan, N. Gulzar, Yang Pan et al. (2015). BioXpress: an integrated RNA-seq-derived gene expression database for pan-cancer analysis. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/2852ba7d092a2814e304d9dfbe5a79fa4e0250f8
13. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Si-Qian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
14. Yi Zheng, Shan Wu, Yang Bai, Hong-He Sun, C. Jiao et al. (2018). Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops. Nucleic Acids Research. https://www.semanticscholar.org/paper/a7bb1e82b8172252d79ee35170dfe038c4b17d78
15. Tsz N. Mok, Q. He, Xiao-Xi Zhang, Tat-Hang Sin, Hua-Jun Wang et al. (2022). Effects of 6-Hydroxykaempferol: A Potential Natural Product for Amelioration of Tendon Impairment. Frontiers in Pharmacology. https://www.semanticscholar.org/paper/5051cd4b77d748a62d6efb4ca95e7bcac106c654
16. Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al. (2026). An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models. Nature Communications. https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
17. Ahmad Lutfi, Sukrit Dang, Robert Warneke, Lutz Fischer, J. Rappsilber (2026). KlinkPPI: Single Point of Access to Protein-Protein Interactions Across Databases. bioRxiv. https://www.semanticscholar.org/paper/eca10a7c69be47729504f5df3ccd660dd62a4381
18. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
19. Sandra Castillo, Chunhao Gu, Paula Jouhten, Gopal Peddinti, O. H. Samuli Ollila (2026). ActSeekN: A Structural-Motif–Based Pipeline for Interpretable Enzyme Function Annotation. bioRxiv. https://www.semanticscholar.org/paper/685563319e26ee3350cb480e1316c1a8906e29e0
20. M. Masseroli, Arif Canakoglu, Massimiliano Quigliatti (2015). Detection of gene annotations and protein-protein interaction associated disorders through transitive relationships between integrated annotations. BMC Genomics. https://www.semanticscholar.org/paper/8d304f9052541ebc058cb23bcf2516938707836b