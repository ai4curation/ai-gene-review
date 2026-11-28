---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-11-26T19:03:23.471355'
end_time: '2026-11-26T19:03:28.818822'
duration_seconds: 5.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SERPINA6
  gene_symbol: SERPINA6
  uniprot_accession: P08185
  protein_description: 'RecName: Full=Corticosteroid-binding globulin; Short=CBG;
    AltName: Full=Serpin A6; AltName: Full=Transcortin; Flags: Precursor;'
  gene_info: Name=SERPINA6; Synonyms=CBG;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the serpin family. .
  protein_domains: Serpin_CS. (IPR023795); Serpin_dom. (IPR023796); Serpin_fam. (IPR000215);
    Serpin_sf. (IPR036186); Serpin_sf_1. (IPR042178)
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
- **UniProt Accession:** P08185
- **Protein Description:** RecName: Full=Corticosteroid-binding globulin; Short=CBG; AltName: Full=Serpin A6; AltName: Full=Transcortin; Flags: Precursor;
- **Gene Information:** Name=SERPINA6; Synonyms=CBG;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the serpin family. .
- **Key Domains:** Serpin_CS. (IPR023795); Serpin_dom. (IPR023796); Serpin_fam. (IPR000215); Serpin_sf. (IPR036186); Serpin_sf_1. (IPR042178)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SERPINA6" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SERPINA6' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SERPINA6** (gene ID: SERPINA6, UniProt: P08185) in human.

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

### [1] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.767)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

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
  - Snippet 1 (score: 0.753)
    > The UniProt database (https://www.uniprot.org/) can perform ID mapping on the UniProt ID of each protein to obtain corresponding annotation information, including Entry name, Protein name, Gene name, Organism, and Length.
    > Note: Considering the efficiency and readability of subsequent analysis, users need to convert the ID in the raw data. In this protocol, we choose to convert UniProt ID to Gene Symbol, and when multiple UniProt ID correspond to one Gene Symbol, we can use the make.unique() function to add a serial number to Gene Symbol to make it unique.
    > 7. Group samples by type.

### [3] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.738)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.660)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [4] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.726)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [5] Working with Worms: Caenorhabditis elegans as a Model Organism
- Authors: P. Meneely, C. Dahlberg, Jacqueline K. Rose
- Year: 2019
- Venue: Current Protocols Essential Laboratory Techniques
- URL: https://www.semanticscholar.org/paper/a7e7665b4cfc67b3e1c04e29a8f86e56c5e12804
- DOI: 10.1002/cpet.35
- Citations: 114
- Influential citations: 3
- Summary: The nematode worm Caenorhabditis elegans has become one of the most widely used and versatile models for nearly all aspects of biological and genomic research.
- Evidence snippets:
  - Snippet 1 (score: 0.700)
    > Current Protocols Essential Laboratory Techniques 1. Choose one of the following gene IDs for your subsequent analysis. Use the entire DNA sequence, including both the uppercase and lowercase letters.
    > C25E10.12 D1022.1 F55A11.3 2. To determine what information is already available on these genes, go to the BLAST website (http://blast.ncbi.nlm.nih.gov/Blast.cgi), enter your sequence and determine the results.
    > 3. The sequences above are the entire unspliced transcripts. Look for the best mRNA/cDNA match for the following questions:
    > a. How far down the list of matches do you need to go in order to find this match? b. C. elegans genes are named with three to four lowercase letters, followed by a dash and one to three numerals. Based on the gene results, what are the names of these genes (Unnamed genes are designated by a longer string of letters and numbers that describe a genes position relative to a short portion of the genome.) c. What is the e-value of the top BLAST hit that you obtained with the gene you chose?
    > 4. From this point forward, choose ONE gene to follow up on.
    > 5. Copy the corresponding Alignment information, accession number, and the description of your BLAST hit below. Locate the information for the following questions.
    > a. If you click on the Sequence ID of your BLAST hit, you will be redirected to the NCBI resource page for that gene. Are there any publications listed for this protein (i.e., has it been studied before)? How could that information be useful for your future studies of this gene? b. What is the predicted protein sequence for your gene (include it below)? Include the number of amino acids in your protein. c. Click on the GeneID link (located under FEATURES within the "gene" description section). What is the gene immediately upstream of your gene? d. Click on "Protein" (right hand link under "Related Information"). You can then use the "Related information" menu to find Conserved Domains. Are there any conserved domains present in your protein? What function does/do it/they serve?

### [6] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.696)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [7] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.692)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [8] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
- Authors: Yanfei Liu, Yue Liu, Wan-Tong Zhang, Ming-Yue Sun, Wei-Liang Weng et al.
- Year: 2020
- Venue: Evidence-based Complementary and Alternative Medicine : eCAM
- URL: https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
- DOI: 10.1155/2020/8508491
- PMID: 32802136
- PMCID: 7403930
- Citations: 9
- Summary: The study found that flavonoids (quercetin, luteolin, and kaempferol) and beta-sitosterol and the top eight candidate targets, namely, PTGS2, PPARG, DPP4, GSK3B, CCNA2, AR, MAPK14, and ESR1, were selected as the main therapeutic targets of EGb.
- Evidence snippets:
  - Snippet 1 (score: 0.689)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [9] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.688)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [10] Identifying orthologs with OMA: A primer
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
  - Snippet 1 (score: 0.686)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [11] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
- Authors: Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani
- Year: 2023
- Venue: Medicine
- URL: https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
- DOI: 10.1097/MD.0000000000034514
- PMID: 37565925
- PMCID: 10419424
- Citations: 3
- Summary: A network pharmacology-based method to determine the potential therapeutic pathways of phytoconstituents of UHPLC-PDA standardized stigma-based Crocus sativus extract for the management of PCOS revealed that the apocarotenoids and carotenoidal could act on various targets to regulate multiple pathways related to PCOS.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [12] An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models
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
  - Snippet 1 (score: 0.682)
    > This study focused on human protein-coding genes because they represent the most well-annotated portion of the genome, with reliable functional summaries, and are typically the primary focus of functional annotation analyses. We obtained functional summaries of individual genes from three widely used databases: (1) NCBI Gene 32 , which curates descriptions from multiple sources such as RefSeq under the "Summary" field, (2) Alliance of Genome Resources 33 , where descriptions are generated from structured gene data such as ontology terms and ortholog sets under the "Automated Description" field, and (3) UniProt 34 , which focuses on protein-level functions under the "Function" field. The NCBI database was accessed using its API, Entrez Programming Utilities (E-utilities), while descriptions from Alliance of Genome Resources and UniProt were directly downloaded from their respective databases. The number of genes retrieved from each database was 18,753 from NCBI, 18,600 from Alliance of Genome Resources, and 16,343 from UniProt, with 16,329 genes shared across all three databases. We preprocessed the gene descriptions to remove irrelevant information, such as source attribution found in NCBI descriptions (e.g., "[provided by RefSeq, Jul 2008]"). After preprocessing, each gene name was combined with its corresponding functional summary and input into the embedding models to generate gene embeddings.
    > We also generated de novo gene descriptions using an RAG approach. For each gene, we first retrieved the 100 most relevant sentences from PubMed and PubMed Central via the LitSense 35 API using biological context-specific queries: "function of 'gene symbol'", "'gene symbol' pathway association", "'gene symbol' transcriptional response", "'gene symbol' disease association". The numbers of genes under each biological context were 18,723, 18,723, 18,288, and 18,548, respectively. To restrict the temporal scope of knowledge and ensure controlled evaluation, we filtered the retrieved sentences to retain only those from publications published in or before October 2023, consistent with the versions of curated gene databases used in this study.

### [13] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.681)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [14] Mapping the plasma proteomic architecture of systemic lupus erythematosus
- Authors: Geoffrey H. D. Leung, C. Bottomley, N. Buang, R. Maughan, B. J. Whittle et al.
- Year: 2025
- Venue: JCI Insight
- URL: https://www.semanticscholar.org/paper/cb81e31cdf40247c48bd4e0f3c0f172095cea8ca
- DOI: 10.1172/jci.insight.206938
- PMID: 42228421
- PMCID: 13461151
- Citations: 2
- Summary: This study identified dysregulated plasma proteins and pathways in SLE, protein signatures associated with disease activity, modules of proteins associated with interferon signalling and renal dysfunction, and distinct proteomic patterns correlated with anti-Smith and anti-dsDNA antibodies.
- Evidence snippets:
  - Snippet 1 (score: 0.670)
    > No missing values were observed in the SomaScan proteomic datasets across either proteins or samples. For the clinical metadata, a small number of samples had missing data on the status of autoantibodies and treatments (enumerated in Table 1) and these samples were omitted from analyses requiring these metadata. Sample sizes used in each are reported in the relevant figures and supplemental tables. Protein nomenclature. Due to non-standardization of protein nomenclature (e.g., where a given protein has multiple names) and the lack of human interpretability of UniProt identifiers, we annotated each protein using the non-italicized HUGO symbol for the encoding gene. In instances where there were multiple distinct SOMAmers mapping to the same HUGO gene symbol (1,669 SOMAmers mapped to 781 unique gene symbols and 782 UniProt identifiers), we concatenated the gene symbol with the SOMAmer identifier to preserve a unique identifier for each analyte. Importantly, in some instances, multiple SOMAmers mapping to the same gene symbol represented measurements of distinct biological entities. For example, the intact complement C3 protein and its distinct cleavage products such as C3a, C3b, and C3d, all mapped to a single HUGO gene symbol and UniProt ID. However, in other instances there were multiple SOMAmers that are nominally directed against the same target protein. A comprehensive annotation file mapping of SOMAmers to their target proteins, UniProt IDs and corresponding gene IDs, and gene symbols is provided in Supplemental Data File 2.
    > Complement proteins. Various complement proteins and cleavage fragments were included on the SomaScan platform. To evaluate the accuracy of complement C3 and C4 quantification, we compared the levels of intact complement C3 and C4 proteins measured by SomaScan in SLE patients to their corresponding values measured in the clinical laboratory from the same blood draw. We performed this analysis separately for each batch to avoid variation related to batch.
    > Identification of differentially abundant proteins in SLE versus HV samples.

### [15] Bioinformatic pipeline to identify potential therapeutic targets with subsequent isolation and characterization of novel human anti- DDR1 antibodies
- Authors: Divya Agrawal, S. Mahler, A. Rathore, Martina L. Jones, J. Mar et al.
- Year: 2026
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/35383063a216fe4870915d6520c4c1fd290abf0c
- DOI: 10.1038/s41598-026-56361-4
- PMID: 42286049
- PMCID: 13518920
- Citations: 2
- Summary: The effectiveness of combining publicly available omics datasets with phage display technology to identify and develop new therapeutic antibody candidates for breast cancer is highlighted.
- Evidence snippets:
  - Snippet 1 (score: 0.667)
    > HUGO gene symbols were selected due to their widespread use and recognition as the official nomenclature for human genes, facilitating linkage of data using different gene/protein identifiers 39 . In this way, RefSeq IDs, Ensembl IDs, and UniProt IDs were mapped to their corresponding HUGO gene symbol by cross-referencing multiple databases, including HGNC for official gene names, GeneCards (The Human gene database) for comprehensive gene information, and NCBI Gene and Protein databases for verifying gene-protein identifier consistency. To ensure accurate and unambiguous mapping to gene-level identifiers some proteomic targets were excluded from the analysis, including targets identified with antibodies against specific post-translationally modified forms of the targets (such as phosphorylated, acetylated, and methylated isoforms), or if targets were protein complex | https://doi.org/10.1038/s41598-026-56361-4 subunits (due to lack of one-to-one mapping with a single gene identifier or a complex-level regulation of abundance), or if the target names contained non-standard characters or punctuations (e.g., slashes, hyphens, or asterisks) (Fig. 4a). 335 proteins were further reduced to 333 unique HUGO gene symbols, with CASP8 and NOTCH1 each mapped twice by two distinct proteins: duplicates were identified, and only one representative for each was retained in the final set. In parallel, the 16,404 mRNAs were reduced to 16,403 unique HUGO gene symbols after removing one redundant instance of POLR2J3 mRNA. When we compared the 16,403 mRNAs with the 333 proteins (Figs. 2-4), we observed an overlap of 320 potential targets (~96% of the filtered proteins, and ~2% of the filtered mRNAs) (Fig. 4a, Supplementary File S5).

### [16] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
- Authors: Anna K. Childers, S. Geib, S. Sim, M. Poelchau, B. Coates et al.
- Year: 2021
- Venue: Insects
- URL: https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
- DOI: 10.3390/insects12070626
- PMID: 34357286
- PMCID: 8307976
- Citations: 45
- Influential citations: 3
- Summary: It is shown that the Ag100Pest Initiative will greatly expand the diversity of publicly available arthropod genome assemblies and demonstrate the high quality of preliminary contig assemblies, which should help other researchers attain similarly high-quality assemblies.
- Evidence snippets:
  - Snippet 1 (score: 0.666)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [17] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.665)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [18] NO VEIN is an ancestral immunity protein involved in plant-virus interaction
- Authors: Eirik Lågeide, M. Abraham, Nicolas Glück, Helena Pfingst, Lukas A. Burkhardt et al.
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/25f7f948bdee19c5dc1f2950b3ed514e2140cb14
- DOI: 10.64898/2026.09.30.755639
- Summary: It is shown that NO VEIN (NOV), a plant protein previously characterized for its essential developmental roles in Arabidopsis thaliana, shares domain composition and structural similarity with Tiamat, a bacterial antiphage protein, which uncovers a deeply conserved protein involved in plant-virus interaction.
- Evidence snippets:
  - Snippet 1 (score: 0.665)
    > As the NbLab360 genome annotation provides limited functional information, NbLab360 protein models (CDS-derived amino-acid sequences) were assigned annotations by homology search with DIAMOND (v2.1.24); (Buchfink et al., 2021) in blastp mode against two reference sets: Arabidopsis thaliana proteins (Araport11/TAIR) and UniProt Swiss-Prot reviewed proteins (Viridiplantae). Hits were retained at ≥30% identity, ≥50% query coverage, and E-value ≤ 1x10 -10 for both, keeping the single best hit per query if higher than 40% identity for annotations, with preference for TAIR IDs in cases of ties, and defaulting to NbLAB360 identifiers when hits did not qualify (i.e <30% identity). The resulting TAIR or Uniprot homolog was used for gene annotation in figures 1 F-H and Supplementary Figure 3B. Gene Ontology (GO) annotation was determined through org.At.tair.db based on TAIR identifiers for genes where such a homolog was detected. For defining Defenserelated and heat-stress related gene sets, GO:0006952 (Defense response) and GO:0009408 (Heat response) were used. In overlapping cases, 'Defense response' was preferred over 'Heat response'.
    > Transposable-element annotation of the NbLab360 gene models was assessed by DIAMOND blastp of the amino-acid models against the REXdb Viridiplantae TE protein database v4.0; (Neumann et al., 2019), retaining the best hit per gene at ≥30% identity, ≥30% query coverage, and E-value ≤ 1x10 -5 . TE hits were joined to the REXdb classification table to assign each TE-associated gene a hierarchical classification (class, order, superfamily, and lineage). Genes with a qualifying REXdb hit were flagged as TE-associated for downstream analyses. Genes containing "transposon" in their uniprot or TAIR descriptions were also flagged as TE-associated. (Millman et al., 2022).

### [19] Integrative Phosphoproteomic Characterization of ULK1 Phosphosites Reveals Co-Regulatory Networks in Autophagy and Metabolic Adaptation
- Authors: Furqaan Ahmed Basha, Sreeshma Ravindran Kammarambath, Leona Dcunha, Althaf Mahin, Athira Perunelly Gopalakrishnan et al.
- Year: 2026
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/828609178fe15ea3c11dea952be632f79e0d660d
- DOI: 10.3390/ijms27198892
- PMID: 42884135
- PMCID: 13665027
- Summary: A large-scale phosphoproteomic data analysis of ULK1 provided a phosphosite-resolved view of ULK1 regulation and identifies candidate phosphosites and associated proteins for future functional and mechanistic studies.
- Evidence snippets:
  - Snippet 1 (score: 0.661)
    > To minimize inconsistencies in gene nomenclature, all proteins were mapped to their respective HUGO Gene Nomenclature Committee (HGNC)approved gene symbols. To ensure consistent and standardized annotation, phosphosites were mapped to UniProt (2023) accessions using an in-house mapping tool [56].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Christina M. McCosker, E. Unal, Alayna K. Gigliotti, W. Puryear, J. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
2. Juan Wang, Yi Liu, Xi-Zhao Chen, Man-Sheng Li, Yunping Zhu (2024). Protocol for identifying and comparing molecular prognosis subtypes of IgAN using R. STAR Protocols. https://www.semanticscholar.org/paper/6794ab2424155d4a65b28cd139731c21d4d37aa2
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, A. Zlotnicki, Nicholas A. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. B. Waegele, I. Dunger-Kaltenbach, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
5. P. Meneely, C. Dahlberg, Jacqueline K. Rose (2019). Working with Worms: Caenorhabditis elegans as a Model Organism. Current Protocols Essential Laboratory Techniques. https://www.semanticscholar.org/paper/a7e7665b4cfc67b3e1c04e29a8f86e56c5e12804
6. Mary Kate Bonner, Daniel S. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
7. Ralf C. Mueller, Nicolai Mallig, J. Smith, Lél Eöery, R. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
8. Yanfei Liu, Yue Liu, Wan-Tong Zhang, Ming-Yue Sun, Wei-Liang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
9. P. Pinto-Pinho, J. Quelhas, F. Impens, Sara Dufour, D. Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
10. Monique Zahn-Zabal, C. Dessimoz, N. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
11. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
12. Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al. (2026). An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models. Nature Communications. https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
13. Dawn Cotter, Andreia Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
14. Geoffrey H. D. Leung, C. Bottomley, N. Buang, R. Maughan, B. J. Whittle et al. (2025). Mapping the plasma proteomic architecture of systemic lupus erythematosus. JCI Insight. https://www.semanticscholar.org/paper/cb81e31cdf40247c48bd4e0f3c0f172095cea8ca
15. Divya Agrawal, S. Mahler, A. Rathore, Martina L. Jones, J. Mar et al. (2026). Bioinformatic pipeline to identify potential therapeutic targets with subsequent isolation and characterization of novel human anti- DDR1 antibodies. Scientific Reports. https://www.semanticscholar.org/paper/35383063a216fe4870915d6520c4c1fd290abf0c
16. Anna K. Childers, S. Geib, S. Sim, M. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
17. P. Hornbeck, J. Kornhauser, Sasha L. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
18. Eirik Lågeide, M. Abraham, Nicolas Glück, Helena Pfingst, Lukas A. Burkhardt et al. (2026). NO VEIN is an ancestral immunity protein involved in plant-virus interaction. bioRxiv. https://www.semanticscholar.org/paper/25f7f948bdee19c5dc1f2950b3ed514e2140cb14
19. Furqaan Ahmed Basha, Sreeshma Ravindran Kammarambath, Leona Dcunha, Althaf Mahin, Athira Perunelly Gopalakrishnan et al. (2026). Integrative Phosphoproteomic Characterization of ULK1 Phosphosites Reveals Co-Regulatory Networks in Autophagy and Metabolic Adaptation. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/828609178fe15ea3c11dea952be632f79e0d660d