---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-11T06:26:58.960395'
end_time: '2026-07-11T06:27:05.066344'
duration_seconds: 6.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0984
  gene_symbol: PP_0984
  uniprot_accession: Q88P69
  protein_description: 'RecName: Full=RDD domain-containing protein {ECO:0000259|Pfam:PF06271};'
  gene_info: OrderedLocusNames=PP_0984 {ECO:0000313|EMBL:AAN66609.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Pra-immunoreactive. (IPR051791); RDD. (IPR010432); RDD (PF06271)
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
- **UniProt Accession:** Q88P69
- **Protein Description:** RecName: Full=RDD domain-containing protein {ECO:0000259|Pfam:PF06271};
- **Gene Information:** OrderedLocusNames=PP_0984 {ECO:0000313|EMBL:AAN66609.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Pra-immunoreactive. (IPR051791); RDD. (IPR010432); RDD (PF06271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0984" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0984' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0984** (gene ID: PP_0984, UniProt: Q88P69) in PSEPK.

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

### [1] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.789)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [2] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.788)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.788)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [4] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.765)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [5] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.765)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [6] A Genome-Wide Association Study Identifying Novel Genetic Markers of Response to Treatment with Interleukin-23 Inhibitors in Psoriasis
- Authors: Sophia Zachari, K. Liadaki, Angeliki Planaki, E. Zafiriou, Olga Kouvarou et al.
- Year: 2025
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/d5f656311b54e222e7487ea32a061869b30178a1
- DOI: 10.3390/genes16101195
- PMID: 41153410
- PMCID: 12564705
- Summary: These findings provide promising pharmacogenetic markers which, upon validation in larger, independent cohorts, will enable the translation of a patient’s genotype into a response phenotype, thereby guiding clinical decisions and improving drug effectiveness.
- Evidence snippets:
  - Snippet 1 (score: 0.761)
    > The UniProt knowledgebase (www.uniprot.org/uniprotkb/), (accessed on 20 June 2025), the central hub for the collection of functional information on proteins, with accurate and rich annotation [33], was used to retrieve the approved human gene and protein names and symbols.

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
  - Snippet 1 (score: 0.756)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [8] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.750)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [9] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2777
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.745)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [10] Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale
- Authors: P. Kramer, Jack Treml
- Year: 2022
- Venue: Midwestern Journal of Undergraduate Sciences
- URL: https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27
- DOI: 10.17161/mjusc.v1i1.18565
- Summary: The following is a walkthrough of a project designed to overcome the lack of sense for proteins as real objects.
- Evidence snippets:
  - Snippet 1 (score: 0.732)
    > i. Click "See more" to view a bar chart containing data on where in the body's tissues the gene is expressed (as determined by RNA sequencing). Save and include this bar chart as the deliverable for this step.
    > II. Universal Protein Research Knowledgebase (UniProtKB) 8 6. UniProt Entry Number
    > i. Follow the UniProt link in the Resources then search for the protein using the NCBI Gene ID ii. Carefully select the result that best matches the gene and organism of interest by clicking on the blue entry number. iii. This page will be used later to gather further details about the protein.
    > III. RCSB Protein Data Bank (PDB) 9 7. RCSB PDB Solved Structure Identifi er i. Follow the RCSB PDB link in the Resources and search for the protein by either the common name or the NCBI Gene ID, making sure to select the organism of interest on the left. ii. You must ensure that your chosen protein has an existing solved structure in this data bank in order to do a mutational analysis in later parts of this exercise.
    > IV. NCBI GenBank 10 8. AA Protein Sequence i. From the NCBI Gene page, go to the "Genomic regions, transcripts, and products" section and then click "GenBank" on the right. Scroll down to the fi rst Coding Sequence "CDS" section and look directly after "/translation=" for the full protein sequence. ii. Sequence needs to be in FASTA Format consisting of '>' followed by a simple name, a return, and then the sequence in one continuous line of text. See "FASTA Formatting" link in Resources.

### [11] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.731)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [12] Integrating Omics Data in Genome-Scale Metabolic Modeling: A Methodological Perspective for Precision Medicine
- Authors: Partho Sen, M. Orešič
- Year: 2023
- Venue: Metabolites
- URL: https://www.semanticscholar.org/paper/4e267a0a6479bfcb1fcb30151c3e180e49eb09e0
- DOI: 10.3390/metabo13070855
- PMID: 37512562
- PMCID: 10383060
- Citations: 48
- Influential citations: 1
- Summary: The critical challenges that must be overcome to ensure their reproducibility and enhance their prediction accuracy, particularly in the context of precision medicine are discussed and the role of machine learning is explored in addressing these challenges within GEMs.
- Evidence snippets:
  - Snippet 1 (score: 0.730)
    > [69] UniProt An open access database for curated protein information. [70] Human Protein Atlas (HPA) A comprehensive resource providing information on the expression and localization of proteins in human tissues and cells. [71] ProteomicsDB A comprehensive resource for exploring and analyzing protein expression data from a variety of organisms and tissues. [72] Entrez gene Gene-centered information, including gene sequences, annotations, functional data, and genetic variations.
    > [73]

### [13] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.728)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [14] An AI-powered knowledge hub for potato functional genomics
- Authors: Jia Yuxin, Liu Jinye, Yudong Jia, Futing Li, Xiao Su et al.
- Year: 2025
- Venue: Plant Communications
- URL: https://www.semanticscholar.org/paper/f62ae75adb9c06478b08d5d4e5d57191c073a49f
- DOI: 10.1016/j.xplc.2026.101730
- PMID: 41536067
- PMCID: 13174205
- Citations: 2
- Influential citations: 1
- Summary: The Potato Knowledge Hub is developed, leveraging Large Language Models and a systematically curated collection of over 3,200 high-quality potato research papers spanning over 120 years to be a comprehensive resource, fostering advancements in potato functional genomics and supporting breeding programs.
- Evidence snippets:
  - Snippet 1 (score: 0.728)
    > Correspondence gene symbols associated with their respective source publications. To further enhance research utility, we integrated key functional annotations, including InterPro domains, UniProt similarity information, and expression patterns, into each gene entry (Figure 1B and Supplemental Figure 6B). We also developed a toolkit comprising BLAST, Annotator, ID converter, and Gene Ontology and Kyoto Encyclopedia of Genes and Genomes enrichment tools to facilitate rapid BLAST queries, gene domain and symbol annotation, DMv4 and DMv6 to DMv8 ID conversion, and functional enrichment analyses (Supplemental Figure 7). Together, this gene database enables researchers to retrieve comprehensive gene information and associated literature using either current gene symbols or legacy identifiers, significantly simplifying the background research process for functional gene studies and facilitating efficient project initiation.
    > To optimize user interaction with the Potato Knowledge Hub, we implemented an agentic task orchestration architecture and developed the Potato Research Assistant, an AI agent capable of invoking the workflows of the knowledge database, gene database, and integrated toolkit (Figure 1A). This agent interacts with users via natural language, conducts intent analysis, and calls the appropriate internal scripts to summarize potato research knowledge, retrieve gene information and sequences, and execute specific analytical tools. For a queried gene symbol, the assistant can summarize historical research, extract sequences (coding, protein, and customized promoter regions, etc.), and provide detailed information on putative gene function. By integrating these capabilities, the AI agent liberates users from tedious literature mining and complex bioinformatics software, enabling scientists without specialized computational expertise to efficiently explore and utilize a tremendous amount of gene information with ease.
    > To evaluate the performance of the Potato Research Assistant, in addition to the 70 questions used to benchmark the knowledge base, we collected an additional 20 questions focused on gene understanding and 10 questions related to sequence extraction to assess the gene database.

### [15] Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops
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
  - Snippet 1 (score: 0.720)
    > The submenu provides links to a pathway database, a genome browser, an FTP site for downloading genome and gene sequences and annotations, and bioinformatics tools such as BLAST, batch query and basic search functions.
    > A total of 265 334 protein-coding genes have been predicted from these 10 genomes and included in the database. A standard and unified procedure has been developed to comprehensively annotate predicted protein-coding genes. First, protein sequences of the predicted genes are compared against the GenBank non-redundant protein (nr), UniProt (TrEMBL and SwissProt), and Arabidopsis protein databases using the BLAST program with an E-value cutoff of 1e-4. The protein sequences are further compared against the InterPro database using InterProScan (21) to identify functional protein domains. The BLAST results D1130 Nucleic Acids Research, 2019, Vol. 47, Database issue against the nr database and the identified InterPro domains are fed to the Blast2GO program (22) for assigning gene ontology (GO) terms to protein-coding genes, and the BLAST results against the UniProt and Arabidopsis protein databases are loaded into the AHRD program (https: //github.com/groupschoof/AHRD) to assign concise, informative and precise functional descriptions of genes. The top BLAST hits (homologs), GO terms and InterPro domains assigned to each of the protein-coding genes have been imported into CuGenDB using Tripal Analysis Extension Modules (16). The functional descriptions generated by AHRD are loaded into the database using an inhouse Perl script. Each gene has a detailed feature page in the database that contains all the related sequence and annotation information; the gene feature page is divided into different sections based on the content types (Figure 1).

### [16] Identifying orthologs with OMA: A primer
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
  - Snippet 1 (score: 0.719)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [17] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.719)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [18] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
- Authors: E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al.
- Year: 2016
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/f3eda16f7a2760619a7727b38fc2fc6738858040
- DOI: 10.1186/s13059-016-1014-0
- PMID: 27381095
- PMCID: 4933991
- Citations: 93
- Influential citations: 5
- Summary: The results provide the most complete comparative genomics and experimental analysis of mRBPs in P. falciparum and identify and characterize mRNA-binding proteins (mRBPs) that encompass a relatively large proportion of the parasite proteome as compared to other eukaryotes.
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

### [19] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
- Authors: E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al.
- Year: 2016
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
- DOI: 10.1186/s13059-016-1014-0
- Summary: The results provide the most complete comparative genomics and experimental analysis of mRBPs in P. falciparum and identify and characterize mRNA-binding proteins (mRBPs) that encompass a relatively large proportion of the parasite proteome as compared to other eukaryotes.
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

### [20] Protocol for gene annotation, prediction, and validation of genomic gene expansion
- Authors: Quanwei Zhang, Zhengdong D. Zhang
- Year: 2022
- Venue: STAR Protocols
- URL: https://www.semanticscholar.org/paper/af8e3a73daaa04214d43f4ec1d9b1c0fcd42b8e3
- DOI: 10.1016/j.xpro.2022.101692
- PMID: 36125934
- PMCID: 9494284
- Citations: 1
- Summary: A detailed step-by-step protocol for gene annotation, prediction of genomic gene expansion, and its computational and experimental validation is described and steps to discover functionality of each copy of replicated genes are detailed.
- Evidence snippets:
  - Snippet 1 (score: 0.713)
    > 3. Gene annotation and functional annotation. a. Gene structure annotation.
    > In addition to gene prediction models, evidence from orthologous protein sequences and transcriptome assembly could be used to improve annotation quality. Protein sequences of orthologous genes can be obtained from UniProt (The UniProt, 2017). Ones from Swiss-Port have been reviewed and thus are of higher quality. Transcriptome assembly may be available from previous studies or can be assembled de novo from RNA-seq reads by Trinity (Haas et al., 2013). High quality transcriptome assembly can be selected as described in (Zhang et al., 2021). Note: Details about gene structure annotation (Holt and Yandell, 2011) can be found at http:// gmod.org/wiki/MAKER_Tutorial, https://darencard.net/blog/2017-05-16-maker-genomeannotation/, and the protocol (Campbell et al., 2014).
    > b. Quality measurement and functional annotation.
    > For each predicted gene, Maker2 provides the annotation edit distance (AED) score, which measures the goodness of fit between its predicted gene structure and its evidence support. The lower the score, the more accurate the prediction. If more than 90% genes with AED scores lower than 0.5, the genome can be considered well annotated. In addition to the AED score, a high proportion of recognizable domains contained in predicted protein -e.g., higher than 50% -also indicates a good annotation. Recognizable protein domains can by scanned by InterProScan (Jones et al., 2014), assigning potential function to predicted genes.
    > Note: Besides the aforementioned quality measurement, we strongly recommend measuring the completeness of the genome assembly and annotation by checking the existence of a set of Benchmarking Universal Single-Copy Orthologs (BUSCO) (Simao et al., 2015). A high-level completeness of genome assembly and annotation is imperative for a better identification of gene expansion. Based on the result of this analysis, researchers can decide whether they need to further improve the genome assembly before predicting gene expansion. A detailed protocol of BUSCO is available at

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
5. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
6. Sophia Zachari, K. Liadaki, Angeliki Planaki, E. Zafiriou, Olga Kouvarou et al. (2025). A Genome-Wide Association Study Identifying Novel Genetic Markers of Response to Treatment with Interleukin-23 Inhibitors in Psoriasis. Genes. https://www.semanticscholar.org/paper/d5f656311b54e222e7487ea32a061869b30178a1
7. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
8. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
9. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
10. P. Kramer, Jack Treml (2022). Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale. Midwestern Journal of Undergraduate Sciences. https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27
11. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
12. Partho Sen, M. Orešič (2023). Integrating Omics Data in Genome-Scale Metabolic Modeling: A Methodological Perspective for Precision Medicine. Metabolites. https://www.semanticscholar.org/paper/4e267a0a6479bfcb1fcb30151c3e180e49eb09e0
13. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
14. Jia Yuxin, Liu Jinye, Yudong Jia, Futing Li, Xiao Su et al. (2025). An AI-powered knowledge hub for potato functional genomics. Plant Communications. https://www.semanticscholar.org/paper/f62ae75adb9c06478b08d5d4e5d57191c073a49f
15. Yi Zheng, Shan Wu, Yang Bai, Honghe Sun, C. Jiao et al. (2018). Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops. Nucleic Acids Research. https://www.semanticscholar.org/paper/a7bb1e82b8172252d79ee35170dfe038c4b17d78
16. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
17. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
18. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/f3eda16f7a2760619a7727b38fc2fc6738858040
19. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
20. Quanwei Zhang, Zhengdong D. Zhang (2022). Protocol for gene annotation, prediction, and validation of genomic gene expansion. STAR Protocols. https://www.semanticscholar.org/paper/af8e3a73daaa04214d43f4ec1d9b1c0fcd42b8e3