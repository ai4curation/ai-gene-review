---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T22:05:25.933923'
end_time: '2026-07-10T22:05:32.082414'
duration_seconds: 6.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4853
  gene_symbol: PP_4853
  uniprot_accession: Q88DH2
  protein_description: 'SubName: Full=Permease of the drug/metabolite transporter
    (DMT) superfamily {ECO:0000313|EMBL:AAN70422.1};'
  gene_info: OrderedLocusNames=PP_4853 {ECO:0000313|EMBL:AAN70422.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Diverse_Substrate_Transporter. (IPR051258); EamA_dom. (IPR000620);
    EmrE-like. (IPR037185); EamA (PF00892)
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
- **UniProt Accession:** Q88DH2
- **Protein Description:** SubName: Full=Permease of the drug/metabolite transporter (DMT) superfamily {ECO:0000313|EMBL:AAN70422.1};
- **Gene Information:** OrderedLocusNames=PP_4853 {ECO:0000313|EMBL:AAN70422.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Diverse_Substrate_Transporter. (IPR051258); EamA_dom. (IPR000620); EmrE-like. (IPR037185); EamA (PF00892)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4853" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4853' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4853** (gene ID: PP_4853, UniProt: Q88DH2) in PSEPK.

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

### [1] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.796)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [2] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
- Authors: Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al.
- Year: 2024
- Venue: Current biology : CB
- URL: https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
- DOI: 10.1016/j.cub.2024.02.040
- PMID: 38460514
- PMCID: 11066936
- Citations: 18
- Summary: It is found that evolution in response to extreme feast/famine is characterized by narrow adaptive trajectories with high mutational parallelism and notable mutational order, which demonstrate how microbes can navigate the adaptive landscapes of regularly fluctuating conditions and ultimately follow mutational trajectories that confer benefits across diverse environments.
- Evidence snippets:
  - Snippet 1 (score: 0.786)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

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
  - Snippet 1 (score: 0.736)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [4] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.731)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [5] IIS – Integrated Interactome System: A Web-Based Platform for the Annotation, Analysis and Visualization of Protein-Metabolite-Gene-Drug Interactions by Integrating a Variety of Data Sources and Tools
- Authors: M. Carazzolle, Lucas Miguel de Carvalho, H. Slepicka, R. Vidal, G. Pereira et al.
- Year: 2014
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/e7be8b63fb087b61d5072e02b73cc47e0433a21d
- DOI: 10.1371/journal.pone.0100385
- PMID: 24949626
- PMCID: 4065059
- Citations: 43
- Influential citations: 1
- Summary: The Integrated Interactome System is described, an integrative platform with a web-based interface for the annotation, analysis and visualization of the interaction profiles of proteins/genes, metabolites and drugs of interest that was validated with yeast two-hybrid, proteomics and metabolomics datasets, but it is also extendable to other datasets.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > In the second module, the partially annotated reads from the SUBMISSION MODULE are available to be checked, added to the user's project (chromatogram project type) and assembled into clusters (contigs and singlets) using CAP3 program [34], in order to eliminate redundant reads typically generated by Y2H and transcriptome assays (Figure 1.2).
    > In the genes/metabolites/drugs project type, lists of genes/ proteins (UniProt Accession, RefSeq or gene symbol), metabolites (HMDB, YMDB or ECMD IDs) and/or drugs (DrugBank ID or CAS number) can also be uploaded by the user as a single column TXT file and added to the project (Figure 1.2). Because of the gene symbols redundancies and the presence of aliases in the databases, searching for gene symbols in the selected organism is first performed on Swiss-Prot database and in the case of unreviewed proteins it is extended to TrEMBL database. It is also possible to upload a two-column TXT file containing UniProt Accession, RefSeq or gene symbol and fold change values, respectively, the second one representing expression/concentration levels.

### [6] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.725)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [7] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.724)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [8] The biocontrol effects and mechanisms of mycoparasitic Alternaria alternata against Chinese rose powdery mildew
- Authors: Yanping Tang, Ruotian Gao, Chang-Le Ma, Jin Wang, Jing Li
- Year: 2025
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/b9f627bbebbb6623346dbe0adf3f09ba9902bbb7
- DOI: 10.3389/fmicb.2025.1598458
- PMID: 40535014
- PMCID: 12174065
- Summary: The whole genome of strain KMR13 is sequences using a combination of second-generation Illumina and third-generation nanopore platforms, and chitinase genes related to mycoparasitism are screened by detecting the expression of the genes at different time periods of sporulation induction.
- Evidence snippets:
  - Snippet 1 (score: 0.724)
    > Functional annotation of genes involves the classification of gene functions and metabolic pathways based on existing databases. This involves the prediction of motifs, structural domains, protein functions, and the metabolic pathways in which they are located. To obtain comprehensive gene function information, we performed gene function annotations of nine databases, including Nr, Pfam, KOG, Uniprot, KEGG, GO, Pathway, Refseq, and Interproscan.

### [9] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.717)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [10] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.716)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [11] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.714)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [12] iDS372, a Phenotypically Reconciled Model for the Metabolism of Streptococcus pneumoniae Strain R6
- Authors: Óscar Dias, J. Saraiva, Cristiana Faria, M. Ramirez, F. Pinto et al.
- Year: 2019
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/a9b961f66aa380f0d52504b7ae8ea9ba2e279fde
- DOI: 10.3389/fmicb.2019.01283
- PMID: 31293525
- PMCID: 6603136
- Citations: 18
- Summary: A high-quality GSM model for Streptococcus pneumoniae R6 model strain (iDS372), comprising 372 genes and 529 reactions, was developed to better understand the metabolism of this major pathogen, provide clues regarding new drug targets, and eventually design strategies for fighting infections by these bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.705)
    > Gene annotations in which merlin's assignment matched the information retrieved from reviewed genes in UniProt can be regarded with higher confidence. In these cases, information was often replicated throughout the remaining databases, such as the case of gene Spr0021.
    > The annotation of genes with incomplete EC number, such as the cases of Spr0022 and Spr0064, required an in-depth analysis. Databases such as KEGG, UniProtKB, and CDD were consulted. In the case of Spr0064, the CDD classified the protein as a sugar isomerase. A search of the protein name assigned by BRENDA returned the EC number 5.3.1.26 which also belonged to the sugar isomerase superfamily. Due to the absence of literature support and information on other databases, the gene was annotated with this EC number and assigned the Label E. Regarding gene Spr0022, KEGG assigned it EC number 3.5.4.33 [tRNA(adenine34) deaminase], UniProtKB annotated the product as a hypothetical protein while BioCyc assigned the EC number 3.5.4.5 (cytidine deaminase) to the gene product. Analysis of the protein sequence on CDD revealed that the gene encoded a protein of the cytidine/deoxycytidilate deaminase superfamily and BLAST on UniProtKB revealed similarity to a gene that encodes a cytidine deaminase protein and search of this protein on BRENDA returned the EC number 3.5.4.5. Thus, this gene was assigned the Label E. Labels A, B, and C account for over 86% of the annotation, with approximately 33, 34, and 20% of the classifications, respectively. There were cases in which genes assigned with incomplete EC numbers (e.g., spr0068) were ultimately annotated with complete ones. Despite the classification as hypothetical protein by KEGG and UniProtKB, the analysis of the conserved domains as well as the availability of complete EC numbers that matched protein function by merlin increased reliability of the assigned function (uridine phosphorylase in this example).

### [13] SHIELD: an integrative gene expression database for inner ear research
- Authors: Jun Shen, D. Scheffer, Kelvin Y. Kwan, D. Corey
- Year: 2015
- Venue: Database: The Journal of Biological Databases and Curation
- URL: https://www.semanticscholar.org/paper/fc7704155cefd9f1c767dc2a03a5025c77d19437
- DOI: 10.1093/database/bav071
- PMID: 26209310
- PMCID: 4513695
- Citations: 130
- Influential citations: 9
- Summary: The Shared Harvard Inner Ear Laboratory Database (SHIELD), an integrated resource that seeks to compile, organize and analyse the genomic, transcriptomic and proteomic knowledge of the inner ear, is developed.
- Evidence snippets:
  - Snippet 1 (score: 0.702)
    > Many public databases of gene information are available (11)(12)(13)(14)(15)(16). However, different public databases often use different sets of unique identifiers (IDs) to describe the same genes or homologous genes in different species. One challenge of comparing large-scale biological datasets is the unification of gene names; otherwise, researchers spend a lot of effort in converting gene IDs when searching different databases. Another is the likelihood of missing some databases due to unfamiliarity; this is particularly true for clinicians and researchers who are specialized in inner ear research but are not necessarily familiar with genomics and bioinformatics. One goal of the SHIELD is to integrate relevant gene annotation information from various public databases in one centralized location.
    > For the SHIELD, annotations were derived from public databases and literature. Currently implemented annotations include official gene symbols, description of the gene name and synonyms, human and mouse chromosome cytogenetic banding, RefSeq RNA and protein (for protein coding genes) accession numbers, National Center for Biotechnology Information (NCBI) Entrez gene ID, genomic coordinates in both mouse reference genome assemblies mm9 and mm10, Ensembl, the Vertebrate Genome Annotation Database (VEGA) Mouse Genome Informatics, UniProt, Online Mendalian Inheritance in Man and gene ontology.
    > For each protein coding genes, we display all UniProt protein isoforms for that gene, the length in amino acid residues and the predicted number of transmembrane domains (TMs). We predicted TMs by running TMHMM2.0 run on all UniProt protein isoforms of each gene (17). The number of TMs is of special interest for research in sensory function, because many key proteins involved in signaling-such as the mechanotransduction ion channels-are integral membrane proteins. This information would help identify candidate genes for the components of the mechanotransduction apparatus of the inner ear.
    > We also performed manual curation of inner ear disorders including syndromic and non-syndromic hearing loss according to the Hereditary Hearing Loss Homepage (http://hereditaryhearingloss.org) and primary literature.

### [14] Genomic basis of the giga-chromosomes and giga-genome of tree peony Paeonia ostii
- Authors: Junhui Yuan, Sanjie Jiang, Jianbo Jian, Ming Liu, Zhen Yue et al.
- Year: 2022
- Venue: Nature Communications
- URL: https://www.semanticscholar.org/paper/ada13a246bd37dc14cb96b07b7a5021c751c3d73
- DOI: 10.1038/s41467-022-35063-1
- PMID: 36443323
- PMCID: 9705720
- Citations: 87
- Influential citations: 12
- Summary: The authors assemble tree peony's genome and reveal the association of a list of candidate genes with fatty acid biosynthesis and the possible contribution of transposon and histone expansion to maintain the giga-chromosomes.
- Evidence snippets:
  - Snippet 1 (score: 0.700)
    > UniProt.org/), GO (http://www.geneontology.org/) or InterPro (https://www.ebi.ac.uk/interpro/) database with a BLASTP e-value <1e −10 and the functions did not match according to 'probable |putative | predicted |uncharacterised |unknown |hypothetical |unnamed', they were transferred to the HC gene set. For genes in the HC gene set, if the function was annotated as 'transposon' or with other TE-related descriptions, then the gene was considered an LC gene. For the genes meeting neither the HC nor LC conditions, if there were supportive functional annotations or RNA-seq/Iso-seq data, they were considered HC genes. Otherwise, they were considered LC genes. The completeness of the genome annotation was assessed using BUSCO (v3.0.2) 40 with the Embryophyta database of 1440 single-copy orthologues.
    > For gene functional annotation, we aligned the proteins of each gene to the SwissProt/TrEMBL (https://www.uniprot.org/), KOG 59 and NR databases (https://www.ncbi.nlm.nih.gov/refseq/about/ nonredundantproteins/) using BLASTP (e-value <1e −10 ), and the function of the best hit was assigned to each gene. We also annotated motifs and domains using InterProScan (v5.11-51.0) 60 by searching against publicly available databases, including Pfam 65 , PRINTS 66 , PAN-THER (http://www.pantherdb.org/), HAMAP 61 , Gene3D 62 , PROSITE 63 , SUPERFAMILY 64 , ProDom 65 and SMART 66 . Gene Ontology 67 functional information was retrieved from the NR database by converting NR accession IDs to GO terms. The tree peony genes were also mapped to the KEGG database (Release 84) 68 to find the best hit for each gene.

### [15] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.699)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [16] Protein Localization Analysis of Essential Genes in Prokaryotes
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
  - Snippet 1 (score: 0.698)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

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
  - Snippet 1 (score: 0.698)
    > Recorded for each protein of the mass spectrometry data sets were, where available, the original protein identifier, subcellular location, sequence of identified peptides, sequence coverage, and the experimental techniques that had been used for the purification, separation, and identification of the protein. If the original protein identifier could not be mapped to a UniProt primary accession number by PIR ID or MGI, then the protein was compared with proteins in UniProt by using BLASTP (14). If there was a significant match, then the UniProt primary accession number was assigned to the protein. Those proteins without a significant match were discarded. By using the PIR ID and the MGI identifier conversion tools, the evidence of mitochondrial localization for a protein was linked to many of the UniProt entries representing it. Identifiers of proteins encoded in the mitochondrial genome of organisms were taken from the Organelle database of the European Molecular Biology Laboratory-European Bioinformatics Institute and used to annotate the appropriate proteins in MitoMiner.
    > The source of protein sequences, related features, and annotation was UniProt (11). All UniProt entries were downloaded for the six species with mitochondrial localization data sets. The literature citations in each UniProt entry were retrieved from PubMed by using an InterMine parser. Additional Gene Ontology annotation on the biological process, metabolic function, and cellular component of each protein was taken from UniProt (15) and individual genome projects of M. musculus (12), Rattus norvegicus (16), Drosophila melanogaster (17), and Saccharomyces cerevisiae (18).
    > Finally lists of human genes and the descriptions of their associated disease phenotypes were taken from OMIM (19), the definitions of groups of homologous proteins were taken from HomoloGene (20), and data on the reactions, enzymes, and compounds of metabolic pathways were taken from KEGG (21). The EC numbers of proteins in UniProt were used to define the cross-reference between proteins and metabolic pathways.

### [18] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2775
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [19] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
- Authors: Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al.
- Year: 2020
- Venue: Evidence-based Complementary and Alternative Medicine : eCAM
- URL: https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
- DOI: 10.1155/2020/8508491
- PMID: 32802136
- PMCID: 7403930
- Citations: 8
- Summary: The study found that flavonoids (quercetin, luteolin, and kaempferol) and beta-sitosterol and the top eight candidate targets, namely, PTGS2, PPARG, DPP4, GSK3B, CCNA2, AR, MAPK14, and ESR1, were selected as the main therapeutic targets of EGb.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [20] An Evidence-Grounded Research Assistant for Functional Genomics and Drug Target Assessment
- Authors: Ksenia Sokolova, Dmitri Kosenkov, Keerthana Nallamotu, S. Vedula, Daniil Sokolov et al.
- Year: 2025
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/f0e30abe5851db793b59fe0d3ce41c67124f3d96
- DOI: 10.64898/2025.12.30.697073
- PMID: 41502944
- PMCID: 12773016
- Citations: 2
- Summary: Alvessa is introduced, an evidence-grounded agentic research assistant designed around verifiability that substantially improves accuracy relative to general-purpose language models and performs comparably to coding-centric agents while producing fully traceable outputs.
- Evidence snippets:
  - Snippet 1 (score: 0.693)
    > Extract gene symbols and drug names from the message, but only if they appear verbatim in the input. Reply with a dictionary of entities, without any additional text. It must be a valid JSON object with two keys: drugs and genes.
    > Example question: Is HER2 or PTEN a drug target of neratinib in breast cancer? Example answer: ```json{"genes": ["HER2", "PTEN"], "drugs": ["neratinib"]} ``` Example invalid answers: 'Found these { "genes"...}', 'The drugs are neratinib...', 'I do not see any genes here.' ["extract_entities", "gencode_gene_node", "query_gwas_by_gene", "variant_annotations", "sei", "expectosc_predictions_agent", "remap_crm_agent"] 2. Variant pathogenicity:
    > ["extract_entities", "query_gwas_by_gene", "variant_annotations", "alphamissense"] 3. Gene-level functional annotation:
    > ["extract_entities", "gencode_gene_node", "humanbase_functions", "uniprot_base", "reactome", "Summarize_bioGRID_GO", "uniprot_gwas", 'clinvar_gene_node'] 4. Protein structure, visualization and druggability:
    > ["extract_entities", "prot", "chembl", "drug_central", "MSigDB"] 5. Protein-protein interactions and gene function questions summaries: ["extract_entities", "Summarize_bioGRID_GO", "Summarize_GO", "AllianceOfGenomes"] 6. Specific protein-protein interactions and gene function questions:

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
5. M. Carazzolle, Lucas Miguel de Carvalho, H. Slepicka, R. Vidal, G. Pereira et al. (2014). IIS – Integrated Interactome System: A Web-Based Platform for the Annotation, Analysis and Visualization of Protein-Metabolite-Gene-Drug Interactions by Integrating a Variety of Data Sources and Tools. PLoS ONE. https://www.semanticscholar.org/paper/e7be8b63fb087b61d5072e02b73cc47e0433a21d
6. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
7. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
8. Yanping Tang, Ruotian Gao, Chang-Le Ma, Jin Wang, Jing Li (2025). The biocontrol effects and mechanisms of mycoparasitic Alternaria alternata against Chinese rose powdery mildew. Frontiers in Microbiology. https://www.semanticscholar.org/paper/b9f627bbebbb6623346dbe0adf3f09ba9902bbb7
9. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
10. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
11. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
12. Óscar Dias, J. Saraiva, Cristiana Faria, M. Ramirez, F. Pinto et al. (2019). iDS372, a Phenotypically Reconciled Model for the Metabolism of Streptococcus pneumoniae Strain R6. Frontiers in Microbiology. https://www.semanticscholar.org/paper/a9b961f66aa380f0d52504b7ae8ea9ba2e279fde
13. Jun Shen, D. Scheffer, Kelvin Y. Kwan, D. Corey (2015). SHIELD: an integrative gene expression database for inner ear research. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/fc7704155cefd9f1c767dc2a03a5025c77d19437
14. Junhui Yuan, Sanjie Jiang, Jianbo Jian, Ming Liu, Zhen Yue et al. (2022). Genomic basis of the giga-chromosomes and giga-genome of tree peony Paeonia ostii. Nature Communications. https://www.semanticscholar.org/paper/ada13a246bd37dc14cb96b07b7a5021c751c3d73
15. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
16. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
17. Anthony C. Smith, A. Robinson (2009). MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data. Molecular & Cellular Proteomics : MCP. https://www.semanticscholar.org/paper/206a60d6d387688ce7f880e0dfe67af5a723c7b8
18. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
19. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
20. Ksenia Sokolova, Dmitri Kosenkov, Keerthana Nallamotu, S. Vedula, Daniil Sokolov et al. (2025). An Evidence-Grounded Research Assistant for Functional Genomics and Drug Target Assessment. bioRxiv. https://www.semanticscholar.org/paper/f0e30abe5851db793b59fe0d3ce41c67124f3d96