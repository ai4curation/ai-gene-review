---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T21:20:12.520723'
end_time: '2026-07-09T21:20:18.921114'
duration_seconds: 6.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3350
  gene_symbol: PP_3350
  uniprot_accession: Q88HK6
  protein_description: 'RecName: Full=Alginate export domain-containing protein {ECO:0000259|Pfam:PF13372};'
  gene_info: OrderedLocusNames=PP_3350 {ECO:0000313|EMBL:AAN68954.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Alginate_export_dom. (IPR025388); Alginate_Permeability_Chnl. (IPR053728);
    Alginate_exp (PF13372)
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
- **UniProt Accession:** Q88HK6
- **Protein Description:** RecName: Full=Alginate export domain-containing protein {ECO:0000259|Pfam:PF13372};
- **Gene Information:** OrderedLocusNames=PP_3350 {ECO:0000313|EMBL:AAN68954.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Alginate_export_dom. (IPR025388); Alginate_Permeability_Chnl. (IPR053728); Alginate_exp (PF13372)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3350" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3350' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3350** (gene ID: PP_3350, UniProt: Q88HK6) in PSEPK.

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

### [1] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.825)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.
  - Snippet 2 (score: 0.728)
    > To avoid mapping errors, we created lists with ambiguous gene names. These lists were manually revised and contain approximately 1900 terms for H.sapiens. Analysis of These lists are invaluable for bioinformatics applications like text mining. Generation of protein-protein interaction networks using gene names leads to a considerable number of false positive interactions if ambiguous gene names are not removed.
    > Mapping of gene names and protein names is conceptually the core of CRONOS. UniProt, RefSeq and Ensembl provide links to a variety of other resources which allows to include additional identifiers for mapping. Thus, the user might enter Agilent microarray identifiers provided by Ensembl in order to obtain UniProt identifiers. This allows mapping of all over-expressed cDNAs from a microarray experiment easily to another format. Beside gene and protein names, CRONOS offers to search with 18 different identifier types. Conversion of lists of IDs into other database-IDs can be done via batch submission. The results are sent via e-mail in a comma separated value (csv) file. Web services were implemented for fully automated access (Supplementary Material S5).
    > Result pages in CRONOS contain mapping relevant information for UniProt, RefSeq, Ensembl and, if available, OMIM (McKusick, 2007). Additional information like protein domains, pathways and functional annotation is also provided.
    > In conclusion, CRONOS allows easy access to cross-references of major resources. Manually curated lists of ambiguous gene and protein names are provided.

### [2] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
- Authors: P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al.
- Year: 2025
- Venue: Animals : an Open Access Journal from MDPI
- URL: https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
- DOI: 10.3390/ani15040484
- PMID: 40002966
- PMCID: 11852025
- Citations: 2
- Summary: Differences in surface proteins between X- and Y-chromosome-bearing bovine spermatozoa are explored to identify potential targets for sperm sexing by LC-MS/MS analysis, with 5 transmembrane proteins showing promise as markers for X-sperm.
- Evidence snippets:
  - Snippet 1 (score: 0.819)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [3] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
- Authors: H. Chiba, Hiroyo Nishide, I. Uchiyama
- Year: 2015
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
- DOI: 10.1371/journal.pone.0122802
- PMID: 25875762
- PMCID: 4395280
- Citations: 14
- Summary: The ortholog database using the Semantic Web technology can contribute to biological knowledge discovery through integrative data analysis and examples demonstrate that the ortholog information described in RDF can be used to link various biological data such as taxonomy information and Gene Ontology.
- Evidence snippets:
  - Snippet 1 (score: 0.784)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [4] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
- Authors: P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
- DOI: 10.1093/nar/gkr1122
- PMID: 22135298
- PMCID: 3245126
- Citations: 1606
- Influential citations: 155
- Summary: PhosphoSitePlus (http://www.phosphosite.org) is an open, comprehensive, manually curated and interactive resource for studying experimentally observed post-translational modifications, primarily of human and mouse proteins. It encompasses 1 30 000 non-redundant modification sites, primarily phosphorylation, ubiquitinylation and acetylation. The interface is designed for clarity and ease of navigation. From the home page, users can launch simple or complex searches and browse high-throughput d...
- Evidence snippets:
  - Snippet 1 (score: 0.768)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [5] Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B
- Authors: Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al.
- Year: 2022
- Venue: Data in Brief
- URL: https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
- DOI: 10.1016/j.dib.2022.108592
- PMID: 36164296
- PMCID: 9508510
- Citations: 2
- Influential citations: 1
- Summary: Covering differential proteomes of three cell lines in a pairwise model, the data could be used to further screen the kinesins that play a vital role in regulating the growth of UM.
- Evidence snippets:
  - Snippet 1 (score: 0.757)
    > 2.8.1. Annotation methods 2.8.1.1. Functional annotation. UniProt-GOA database was utilized to retrieve Gene Ontology (GO) annotation proteome. First, the identified protein identity was converted to UniProt identity and then mapped to GO identity based on the protein identity. When the identified protein was not annotated by UniProt-GOA, the functional annotation of that protein was conducted using the InterProScan software according to the amino acid sequence alignment approach. All proteins were then classified into 3 groups: molecular function, cellular component and biological process.

### [6] LMPD: LIPID MAPS proteome database
- Authors: Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam
- Year: 2005
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
- DOI: 10.1093/nar/gkj122
- PMID: 16381922
- PMCID: 1347484
- Citations: 92
- Influential citations: 2
- Summary: The initial release of the LIPID MAPS Proteome Database contains 2959 records, representing human and mouse proteins involved in lipid metabolism, and this LMPD protein list was enhanced with annotations from UniProt, EntrezGene, ENZYME, GO, KEGG and other public resources.
- Evidence snippets:
  - Snippet 1 (score: 0.755)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [7] Identifying orthologs with OMA: A primer
- Authors: Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover
- Year: 2020
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
- DOI: 10.12688/f1000research.21508.1
- PMID: 32089838
- PMCID: 7014581
- Citations: 41
- Summary: This Primer is organized in two parts and provides all the necessary background information to understand the concepts of orthology, how to infer them and the different subtypes of Orthology in OMA, as well as what types of analyses they should be used for.
- Evidence snippets:
  - Snippet 1 (score: 0.746)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [8] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
- Authors: Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al.
- Year: 2025
- Venue: Molecular ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 3
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.746)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [9] Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser
- Authors: Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała
- Year: 2025
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
- DOI: 10.1186/s12864-025-12329-8
- PMID: 41408139
- PMCID: 12822150
- Citations: 2
- Summary: An R script is developed that performs a gene symbol update to current official versions combined with identification of ambiguous symbols and retrieval of other IDs from the Ensembl database and provides a single list of updated symbols with annotation about their ambiguity.
- Evidence snippets:
  - Snippet 1 (score: 0.741)
    > Genes are identified not only with symbols but also with additional numeric or alphanumeric identifiers assigned by scientific organizations. Therefore, we tested different types of identifiers assigned to genes in a species-specific manner by the Ensembl, NCBI and specialized committees devoted to gene nomenclature (Table 2). The verification of IDs was composed of two steps. First, we used the results from the previous analyses to extract a complete list of all official symbols that can be affected by the symbol ambiguity. The extraction was performed with the script "R_genes linked to ambiguous symbols" separately for each species based on the previous output files Ambiguous_gene_synonyms_final.csv and Ambiguous_ symbols_protein_protein_final.csv while the results were exported to the file All_genes_linked_to_ambiguous_ symbols.csv (Supplementary Fig. 5 in Supplementary file 1). The list was next used to extract associated IDs from the Ensembl 113 genome datasets described in the section "Summary of protein-coding genes". The selected filter setting was "Gene/Input external references ID list/ Gene Name(s)" while the attributes in Gene/Ensembl and External/External references directories were "Gene name", "Gene stable ID", "NCBI gene (formerly Entrezgene) ID" and one of the IDs provided by the nomenclature committee that is mouse "MGI ID", rat "RGD ID", human "HGNC ID" and pig "VGNC ID". The results were exported to the text file mart_export and processed with scripts adjusted for individual species (R_test of additional IDs in Ensembl Mouse/Human/Rat/Pig). The scripts identified missing IDs and IDs assigned to more than one official gene symbol. The results were exported to the files "Missing_IDs.csv", "Multiplied_Ensembl_IDs_ final.csv", "Multiplied_NCBI_IDs_final.csv" and "Multi-plied_Committee_IDs_final.csv".

### [10] SpermatogenesisOnline 1.0: a resource for spermatogenesis based on manual literature curation and genome-wide data mining
- Authors: Yuanwei Zhang, Liangwen Zhong, Bo Xu, Yifan Yang, Rongjun Ban et al.
- Year: 2012
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/339145b8aff21f3177ce5c1a7f9c00453817a9f2
- DOI: 10.1093/nar/gks1186
- PMID: 23193286
- PMCID: 3531227
- Citations: 40
- Influential citations: 3
- Summary: An algorithm, Greed AUC Stepwise (GAS) model, was developed, which predicted 762 genes to participate in spermatogenesis based on genome-wide transcriptional data in Mus musculus testis from the ArrayExpress database, and protein–protein interaction analysis indicates direct interactions of predicted genes with the experimentally verified ones, which supports the reliability of GAS.
- Evidence snippets:
  - Snippet 1 (score: 0.741)
    > After all the genes (including those both experimentally verified and predicted by GAS) were collected, we annotated them as follows: (i) basic information [e.g. name/synonyms, protein sequences, nucleotide sequences, PI (isoelectric point) and MW (molecular weight)] of the genes/proteins is annotated referring to GenBank and UniProt Knowledgebase; (ii) detailed description of the experimentally verified genes (but not predicted genes) including subcellular location, developmental stages and cell types in which a gene function in spermatogenesis is provided together with the result figures and abstracts of literatures reporting the gene and (iii) the protein-protein interaction (PPI) information [combination of the records from HPRD (17), BioGRID (18), DIP (19), MINT (20), IntAct (21) and String (22) database], functional domain, structural domain and the GO annotation are also provided.
    > SpermatogenesisOnline 1.0 is constructed as an integrated bioinformatic resource. It is implemented in PHP+MySQL+JavaScript. Its online documentation contains the help information to guide first time users how to use this resource (http://mcg.ustc.edu.cn/sdap1/ spermgenes/documentation.php).

### [11] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
- Authors: Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani
- Year: 2023
- Venue: Medicine
- URL: https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
- DOI: 10.1097/MD.0000000000034514
- PMID: 37565925
- PMCID: 10419424
- Citations: 2
- Summary: A network pharmacology-based method to determine the potential therapeutic pathways of phytoconstituents of UHPLC-PDA standardized stigma-based Crocus sativus extract for the management of PCOS revealed that the apocarotenoids and carotenoidal could act on various targets to regulate multiple pathways related to PCOS.
- Evidence snippets:
  - Snippet 1 (score: 0.739)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [12] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.739)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [13] Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops
- Authors: Yi Zheng, Shan Wu, Yang Bai, Honghe Sun, C. Jiao et al.
- Year: 2018
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/a7bb1e82b8172252d79ee35170dfe038c4b17d78
- DOI: 10.1093/nar/gky944
- PMID: 30321383
- PMCID: 6324010
- Citations: 174
- Influential citations: 7
- Summary: The Cucurbit Genomics Database has been developed using the Tripal toolkit and two new tools have been developed, a ‘SyntenyViewer’ to view genome synteny between different cucurbit species and an ‘RNA-Seq’ module to analyze and visualize gene expression profiles.
- Evidence snippets:
  - Snippet 1 (score: 0.736)
    > The submenu provides links to a pathway database, a genome browser, an FTP site for downloading genome and gene sequences and annotations, and bioinformatics tools such as BLAST, batch query and basic search functions.
    > A total of 265 334 protein-coding genes have been predicted from these 10 genomes and included in the database. A standard and unified procedure has been developed to comprehensively annotate predicted protein-coding genes. First, protein sequences of the predicted genes are compared against the GenBank non-redundant protein (nr), UniProt (TrEMBL and SwissProt), and Arabidopsis protein databases using the BLAST program with an E-value cutoff of 1e-4. The protein sequences are further compared against the InterPro database using InterProScan (21) to identify functional protein domains. The BLAST results D1130 Nucleic Acids Research, 2019, Vol. 47, Database issue against the nr database and the identified InterPro domains are fed to the Blast2GO program (22) for assigning gene ontology (GO) terms to protein-coding genes, and the BLAST results against the UniProt and Arabidopsis protein databases are loaded into the AHRD program (https: //github.com/groupschoof/AHRD) to assign concise, informative and precise functional descriptions of genes. The top BLAST hits (homologs), GO terms and InterPro domains assigned to each of the protein-coding genes have been imported into CuGenDB using Tripal Analysis Extension Modules (16). The functional descriptions generated by AHRD are loaded into the database using an inhouse Perl script. Each gene has a detailed feature page in the database that contains all the related sequence and annotation information; the gene feature page is divided into different sections based on the content types (Figure 1).

### [14] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
- Authors: Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al.
- Year: 2021
- Venue: Insects
- URL: https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
- DOI: 10.3390/insects12070626
- PMID: 34357286
- PMCID: 8307976
- Citations: 41
- Influential citations: 2
- Summary: It is shown that the Ag100Pest Initiative will greatly expand the diversity of publicly available arthropod genome assemblies and demonstrate the high quality of preliminary contig assemblies, which should help other researchers attain similarly high-quality assemblies.
- Evidence snippets:
  - Snippet 1 (score: 0.735)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [15] Functional annotation of parasitic worm genomes, by assigning protein names and GO terms
- Authors: Avril Coghlan, M. Berriman
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
- DOI: 10.1038/protex.2018.055
- Citations: 1
- Summary: A computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and Go terms from orthologues in other species.
- Evidence snippets:
  - Snippet 1 (score: 0.734)
    > Given a set of predicted protein-coding genes for a newly sequenced genome, functional annotation involves assigning putative functions to the predicted genes. Two ways in which this can be done are assigning protein names and Gene Ontology (GO;Gene Ontology Consortium, 2010) terms to the predicted proteins. Here we describe a computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and GO terms from orthologues in other species.
    > When assigning protein names, UniProt protein naming rules (www.uniprot.org/docs/nameprot) are followed where possible. This recommends that a good and stable name for a protein is "as neutral as possible"; that a protein name "should be, as far as possible, unique and attributed to all orthologs"; and a protein name "should not contain a specific characteristic of the protein, and in particular it should not reflect the function or role of the protein, nor its subcellular location, its domain structure, its tissue specificity, its molecular weight or its species of origin".
    > In our protocol, a protein name is assigned to each predicted protein based on curated names in UniProt (Bairoch & Apweiler, 2000) for human, zebrafish, Drosophila melanogaster, Caenorhabditis elegans, and Schistosoma mansoni orthologues identified from a database of gene families (e.g. built using Ensembl Compara; Vilella et al. 2009), or (if no information is found from orthologues) based on InterPro (Hunter et al. 2012) domains. Figure 1 shows an example of using our protein naming pipeline for four Strongyloides ratti genes that belong to the tubulin polyglutamylase family (underlined in pink), where four different protein names were assigned to them (in pink), based on names of their C. elegans or human orthologues.
    > Since each of the S. ratti genes belonged to a different subfamily of the tubulin polyglutamylase family, they were assigned different names.

### [16] GeneSet2miRNA: finding the signature of cooperative miRNA activities in the gene lists
- Authors: A. Antonov, S. Dietmann, Philip Wong, D. Lutter, H. Mewes
- Year: 2009
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/90ebadc70236638e9499c1200097725327469ea3
- DOI: 10.1093/nar/gkp313
- PMID: 19420064
- PMCID: 2703952
- Citations: 52
- Influential citations: 5
- Summary: GeneSet2miRNA is the first web-based tool which is able to identify whether or not a gene list has a signature of miRNA-regulatory activity.
- Evidence snippets:
  - Snippet 1 (score: 0.731)
    > As input GeneSet2miRNA accepts several types of gene or protein identifiers. For example, for the human genome GeneSet2miRNA supports identifiers from 'Entrez Gene' (24), 'UniProt/Swiss-Prot', 'Gene Symbol' (24,25), 'UniGene' (24), 'Ensembl' (26), 'RefSeq Protein ID', 'RefSeq Transcript ID' ( 27) and 'Affymetrix probe codes' (28). Additionally a mixture of several identifier types is possible. In the first step user supplied gene Ids are mapped to 'Entrez Gene' identifiers. For this purpose files from NCBI and Affymetrix web sites are used. Detailed information on data sources used by GeneSet2miRNA is in Table 1.
    > The user gets full information on the mapping of the supplied gene ids. We would like to point out that protein and gene identifiers can be highly ambiguous (29) with multiple synonymous variants. For this reason the quality of the retrieved annotation can be different for different types of identifiers. To escape multiple mapping issues we recommend submitting 'Entrez Gene' identifies to GeneSet2miRNA.

### [17] Protein Localization Analysis of Essential Genes in Prokaryotes
- Authors: Chong Peng, Feng Gao
- Year: 2014
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
- DOI: 10.1038/srep06001
- PMID: 25105358
- PMCID: 4126397
- Citations: 28
- Summary: A comprehensive protein localization analysis of essential genes in 27 prokaryotes including 24 bacteria, 2 mycoplasmas and 1 archaeon has been performed and shows that proteins encoded by essential genes are enriched in internal location sites, while exist in cell envelope with a lower proportion compared with non-essential ones.
- Evidence snippets:
  - Snippet 1 (score: 0.730)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

### [18] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2776
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.721)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [19] The Protein Interactome of Glycolysis in Escherichia coli
- Authors: Shomeek Chowdhury, Stephen Hepper, M. Lodi, M. Saier, P. Uetz
- Year: 2021
- Venue: Proteomes
- URL: https://www.semanticscholar.org/paper/ab9b1aae1d278887ece0a69b5e7725e8d494c0ee
- DOI: 10.3390/proteomes9020016
- PMID: 33917325
- PMCID: 8167557
- Citations: 8
- Summary: This work investigates which of these interactions may affect glycolysis in E. coli and possibly across numerous other bacteria, based on the stoichiometry of interacting protein pairs (from proteomic studies) and their conservation across bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.721)
    > In order to identify enzymes among glycolytic interactors, we used the EC number in the Uniprot reference proteome [34]. Similarly, we used the Uniprot GO (Gene Ontology) terms to map proteins to biological processes, including "metabolic process" to find metabolic proteins or proteins not known to be involved in any metabolic pathway. This information was verified using annotations from KEGG [35] to identify proteins involved in carbohydrate metabolism or other processes, such as environmental information processing. Lastly, we identified essential genes/proteins using the Database of Essential Genes (DEG version 15.2) [36].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
2. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
5. Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al. (2022). Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B. Data in Brief. https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
6. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
7. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
8. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
9. Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała (2025). Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser. BMC Genomics. https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
10. Yuanwei Zhang, Liangwen Zhong, Bo Xu, Yifan Yang, Rongjun Ban et al. (2012). SpermatogenesisOnline 1.0: a resource for spermatogenesis based on manual literature curation and genome-wide data mining. Nucleic Acids Research. https://www.semanticscholar.org/paper/339145b8aff21f3177ce5c1a7f9c00453817a9f2
11. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
12. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
13. Yi Zheng, Shan Wu, Yang Bai, Honghe Sun, C. Jiao et al. (2018). Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops. Nucleic Acids Research. https://www.semanticscholar.org/paper/a7bb1e82b8172252d79ee35170dfe038c4b17d78
14. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
15. Avril Coghlan, M. Berriman (2018). Functional annotation of parasitic worm genomes, by assigning protein names and GO terms. https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
16. A. Antonov, S. Dietmann, Philip Wong, D. Lutter, H. Mewes (2009). GeneSet2miRNA: finding the signature of cooperative miRNA activities in the gene lists. Nucleic Acids Research. https://www.semanticscholar.org/paper/90ebadc70236638e9499c1200097725327469ea3
17. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
18. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
19. Shomeek Chowdhury, Stephen Hepper, M. Lodi, M. Saier, P. Uetz (2021). The Protein Interactome of Glycolysis in Escherichia coli. Proteomes. https://www.semanticscholar.org/paper/ab9b1aae1d278887ece0a69b5e7725e8d494c0ee