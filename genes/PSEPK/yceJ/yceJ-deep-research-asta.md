---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-11T01:44:43.860606'
end_time: '2026-07-11T01:44:48.461326'
duration_seconds: 4.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: yceJ
  gene_symbol: yceJ
  uniprot_accession: Q88D46
  protein_description: 'SubName: Full=Cytochrome b561, iron-regulated {ECO:0000313|EMBL:AAN70548.1};'
  gene_info: Name=yceJ {ECO:0000313|EMBL:AAN70548.1}; OrderedLocusNames=PP_4982 {ECO:0000313|EMBL:AAN70548.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the cytochrome b561 family.
  protein_domains: Cyt_b561_bac/Ni-Hgenase. (IPR011577); Cytochrome_b561_oxidase.
    (IPR052168); Di-haem_cyt_TM. (IPR016174); Ni_hydr_CYTB (PF01292)
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
- **UniProt Accession:** Q88D46
- **Protein Description:** SubName: Full=Cytochrome b561, iron-regulated {ECO:0000313|EMBL:AAN70548.1};
- **Gene Information:** Name=yceJ {ECO:0000313|EMBL:AAN70548.1}; OrderedLocusNames=PP_4982 {ECO:0000313|EMBL:AAN70548.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the cytochrome b561 family.
- **Key Domains:** Cyt_b561_bac/Ni-Hgenase. (IPR011577); Cytochrome_b561_oxidase. (IPR052168); Di-haem_cyt_TM. (IPR016174); Ni_hydr_CYTB (PF01292)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "yceJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'yceJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **yceJ** (gene ID: yceJ, UniProt: Q88D46) in PSEPK.

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

### [1] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.757)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [2] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.751)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [3] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.749)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

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
  - Snippet 1 (score: 0.749)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [5] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.739)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [6] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.738)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [7] MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis
- Authors: Xiaohua Jiang, Daren Zhao, Asim Ali, Bo Xu, Wei Liu et al.
- Year: 2021
- Venue: Frontiers in Cell and Developmental Biology
- URL: https://www.semanticscholar.org/paper/aeb08368a5540685473578345739bb569103bd46
- DOI: 10.3389/fcell.2021.673073
- PMID: 34485275
- PMCID: 8415030
- Citations: 6
- Summary: The developed MeiosisOnline provides the most updated and detailed information of experimental verified and predicted genes in meiosis, and will greatly help researchers in studying meiosis in an easy and efficient way.
- Evidence snippets:
  - Snippet 1 (score: 0.735)
    > Annotation information for each gene in MeiosisOnline contains "basic information, " "function annotation and classification, " "protein-protein interaction (PPI) and gene expression."
    > (1) Basic information: gene name/synonyms, nucleotide sequences, etc., were extracted from GenBank3 and UniProt Knowledgebase.4 (2) Function annotation and classification: detailed functional information is also manually collected from literature reports. (i) Which meiotic stage is the gene involved? (ii) Did the gene function in one sex or both sexes? (iii) Whether deletion or mutation of the gene in model organism has a phenotype in fertility? (iv) Which protein complex of the gene is involved? (v) The cellular location and expression pattern in tissues or cell lines.
    > (vi) Experimental methods used for functional analysis.
    > (vii) The information of related literature and figures for illustrating the function of protein/gene. (viii) Gene ontology annotation for collected genes.
    > (3) Protein-protein interaction and gene expression: both verified and predicted PPI information were provided. Gene expression pattern in reproductive system was also provided graphically.

### [8] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.720)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [9] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.717)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [10] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.716)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [11] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.715)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [12] A MOD(ern) perspective on literature curation
- Authors: J. Hirschman, T. Berardini, H. Drabkin, D. Howe
- Year: 2010
- Venue: Molecular Genetics and Genomics
- URL: https://www.semanticscholar.org/paper/c98b7209b7106364e1a9b75cd45217efc63f6be5
- DOI: 10.1007/s00438-010-0525-8
- PMID: 20221640
- PMCID: 2854346
- Citations: 27
- Influential citations: 2
- Summary: Four curators from different MODs describe the literature curation process and highlight approaches taken by the four MODs to address: (1) the decision process by which papers are selected, and (2) the identification and prioritization of the data contained in the paper.
- Evidence snippets:
  - Snippet 1 (score: 0.707)
    > The first step in curating a paper is the identification of the genes and proteins described as well as the organism to which they belong (Fig. 1). Surprisingly, one of the more difficult challenges a biocurator can face is unambiguously linking the gene or genes discussed in a paper to a record in their MOD, particularly when the gene nomenclature is unclear or the research organism is not identified. Inclusion of sequence or database identifiers for each gene in the paper ensures accurate linking between the results presented in that paper and the particular gene or genes described therein, no matter how the name of a gene may change over time. Papers that lack this information may be impossible to curate. Nomenclature standards and collaborative efforts often strive to give orthologous genes the same symbol and name in multiple species. For example, MGI, under the auspices of the International Committee on Standardized Genetic Nomenclature for Mice (Maltais et al. 2002), and the HUGO Gene Nomenclature Committee (HGNC, Bruford et al. 2008), works to co-ordinate nomenclature between mouse, human and rat genes. ZFIN attempts to name zebrafish genes after their human or mouse orthologs. Likewise, ArkDB (Hu et al. 2001) which maintains data on cat, chicken, cow, horse and sheep, adopts the HGNC nomenclature. Consequently, when a paper mentions a gene or protein symbol that is the same in several organisms (such as BRCA1, which is used in more than a dozen species) and it does not state the specific organism of origin or provide a sequence accession number for this particular gene, it is difficult, if not impossible, to determine whether the data in that paper belongs in a particular species-specific database or not. Another nomenclature conundrum for many model organisms is the case where the same symbol is used for more than one gene in a single species. For example, the symbol PAP1 in Arabidopsis thaliana is the primary symbol or alias for four different genes (PURPLE ACID PHOSPHATASE 1, PHOSPHATIDIC ACID PHOSPHATASE 1, PRODUC-TION OF ANTHOCYANIN PIGMENT 1, and PHY-TOCHROME-ASSOCIATED PROTEIN 1).

### [13] BioXpress: an integrated RNA-seq-derived gene expression database for pan-cancer analysis
- Authors: Quan Wan, Hayley M Dingerdissen, Yu Fan, N. Gulzar, Yang Pan et al.
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
  - Snippet 1 (score: 0.706)
    > Scientists can find querying datasets useful to identify expression levels between disease and normal pairs to discover differential expression for a gene. They may also want to research on potential biomarkers or pathways that lead to tumor formation or want to explore the overall expression of specific genes across multiple cancer types. Users can search BioXpress using HGNCapproved gene symbols (HUGO Gene Nomenclature Committee), UniProtKB/Swiss-Prot accessions or RefSeq accessions. Differentially expressed genes for a specific cancer type can also be retrieved. Additionally, all data in BioXpress, including lists of genes significantly differentially expressed in two or more cancer types, can be downloaded.
    > Searching using gene name (gene/protein-centric search)
    > A search using the HGNC-approved gene symbol or UniProt/RefSeq accession retrieves differential expression information (cancer vs. normal), tumor-only expression data (where normal samples are not available) and baseline expression information from normal human tissues (Illumina Human Body Map Project). The example below provides an overview of a gene/protein-centric search.

### [14] GeneTools – application for functional annotation and statistical hypothesis testing
- Authors: V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al.
- Year: 2006
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
- DOI: 10.1186/1471-2105-7-470
- PMID: 17062145
- PMCID: 1630634
- Citations: 107
- Influential citations: 11
- Summary: GeneTools is the first "all in one" annotation tool, providing users with a rapid extraction of highly relevant gene annotation data for e.g. thousands of genes or clones at once.
- Evidence snippets:
  - Snippet 1 (score: 0.705)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [15] Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining
- Authors: Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al.
- Year: 2025
- Venue: npj Drug Discovery
- URL: https://www.semanticscholar.org/paper/000083b7bd96cff5b3d1891b00ad332eed7d9add
- DOI: 10.1038/s44386-025-00006-5
- PMID: 40066064
- PMCID: 11892419
- Citations: 4
- Summary: This study systematically assessed the Plasmodium falciparum genome and identified 867 candidate protein targets with evidence of small-molecule binding and blood-stage essentiality, providing a genome-wide data resource for P. falciparum and implements a generalizable framework for systematically evaluating and prioritizing novel pathogenic disease targets.
- Evidence snippets:
  - Snippet 1 (score: 0.698)
    > List of genes and genomic features (GFF) for Plasmodium falciparum 3D7 genome (PlasmoDB release 66) was downloaded and protein-coding genes were extracted along with their gene annotations and genomic location. Additional genomic annotations were obtained by querying PlasmoDB to extract UniProt and Entrez ID(s), ortholog group (OrthoMCL), protein features (CDS and protein length, molecular weight, isoelectric point), domain annotations (InterPro, Pfam, and Superfamily), number of transmembrane (TM) domains, and enzyme commission (EC) numbers. Gene function (Gene Ontology components, functions, and processes) was extracted either from PlasmoDB or by querying the InterPro ID with the InterPro2GO mapping tool from EMBL-EBI. Gene essentiality data was obtained for P. falciparum 20 and P. berghei 21,22 parasites mapped to their falciparum orthologs using OrthoMCL orthology group IDs. Protein Data Bank (PDB) IDs of crystal structures were obtained by searching either gene symbols, UniProt IDs associated with each gene, or the term "Plasmodium". A report with gene identifier, organism, accession number, method for structure determination and publication information was extracted for the search hits.
    > Mapping genes to associated literature publications A download from the NCBI FTP site was performed for gene2pubmed.gz (version 2024-02-21) containing taxonomy ID, gene ID (Entrez) and PubMed ID information. Gene IDs were mapped to the P. falciparum 3D7 annotation set, and corresponding PMIDs were extracted. To include literature references associated with gene symbols, we queried each symbol in PubMed using the Eutils 77 efetch function from NCBI; additional information for each publication was obtained pragmatically using the same tool, namely title, authors and digital object identifier (DOI). Literature references from gene nomenclature extraction were manually reviewed and filtered for unrelated records (e.g., same name but different meaning across organisms/diseases).

### [16] Analysis of Iron and Iron-Interacting Protein Dynamics During T-Cell Activation
- Authors: Megan R. Teh, Joe N. Frost, A. Armitage, H. Drakesmith
- Year: 2021
- Venue: Frontiers in Immunology
- URL: https://www.semanticscholar.org/paper/912bf84469a61cdc9db3bb47a2104a7bbbcfa4c5
- DOI: 10.3389/fimmu.2021.714613
- PMID: 34880854
- PMCID: 8647206
- Citations: 46
- Influential citations: 2
- Summary: This work identified iron-interacting proteins in CD4+ and CD8+ T-cell proteomes that were differentially expressed during activation, suggesting that pathways enriched with such proteins, including histone demethylation, may be impaired by iron deficiency.
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > Using the Uniprot IDs of human iron interacting proteins provided by Andreini et al, corresponding standard human gene names were identified using the Uniprot mapping tool (https://www.uniprot.org/uploadlists/) (16). To curate an equivalent list of mouse iron interacting protein homologues, the list of human iron interacting genes was input into the Ensembl BioMart tool (http://useast.ensembl.org/biomart/ martview/893cea99357a57529ab65ce92c12e306) selecting for comparison to the Ensembl Genes 100 database, Human genes (GRCh38.p13) dataset (Supplementary File 1) (17). Filtering was completed by gene name using an external reference ID list and selecting for the attributes: gene stable ID, gene name, mouse gene stable ID, mouse gene name and gene description. This method was able to identify mouse homologues for the majority of human iron interacting proteins (349/398, 88%). In cases where gene matches were not identified by Ensembl, manual verification was completed and several more matches were identified (8 proteins). Some human iron interacting proteins were found to have no mouse homologues (23 proteins, ex//KDM4E, SCD5, NOX5, etc.) or poor gene annotation limited the identification of matches (18 proteins, ex//CYP2C, FADS2P1, DKFZp686G0638). To obtain further cofactor information regarding protein to iron atom stoichiometry, the Uniprot database was manually searched using the cofactor terms: 4Fe-4S, 3Fe-3S, 2Fe-2S, heme, Fe2+, Fe3+. Retrieved cofactor information was manually added to the list of iron interacting information Notably, the iron interacting protein list does not include proteins that indirectly interact with iron such as TFRC which interacts with iron via intermediate contact with Tf. The resulting list of mouse iron interacting proteins is relatively comprehensive but likely does not include the complete set of iron interacting proteins.

### [17] Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining
- Authors: Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al.
- Year: 2024
- Venue: Research Square
- URL: https://www.semanticscholar.org/paper/795b2985fdc3cf1cfbd5fda1b3c0502eb4dfe866
- DOI: 10.21203/rs.3.rs-5412515/v1
- PMID: 39649165
- PMCID: 11623766
- Citations: 3
- Summary: This study systematically assessed the Plasmodium falciparum genome for proteins amenable to target-based drug discovery, identifying 867 candidate targets with evidence of small molecule binding and blood stage essentiality and implements a generalizable framework for systematically evaluating and prioritizing novel pathogenic disease targets.
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > List of genes and genomic features (GFF) for Plasmodium falciparum 3D7 genome (PlasmoDB release 66) was downloaded and protein coding genes were extracted along with their gene annotations and genomic location. Additional genomic annotations were obtained by querying PlasmoDB to extract UniProt and Entrez ID(s), ortholog group (OrthoMCL), protein features (CDS and protein length, molecular weight, isoelectric point), domain annotations (InterPro, PFam, Superfamily), number of transmembrane (TM) domains, and enzyme commission (EC) numbers. Gene function (Gene Ontology; components, functions and processes) was extracted by either PlasmoDB or by querying the InterPro ID under InterPro2GO mapping tool from EMBL-EBI services. Gene essentiality data was obtained for P.
    > falciparum 29 and P. berghei 30,31 parasites that were mapped to their falciparum ortholog using OrthoMCL orthology group IDs. Protein Data Bank (PDB) IDs of crystal structures were obtained by searching either gene symbols, UniProt IDs associated with each gene, or by typing "Plasmodium" in the PDB website search box. A report with gene identi er, organism, accession number, method for structure determination and publication information was extracted for the search hits.
    > Mapping genes to associated literature publications A download from the NCBI FTP site was performed for gene2pubmed.gz (version 2024-02-21) containing taxonomy ID, gene ID (Entrez) and PubMed ID. Gene IDs were mapped to the P. falciparum 3D7 annotation set, and PMIDs matching the criteria were extracted. To include literature references associated with gene symbols, we queried each gene symbol in PubMed using the Eutils 81 efetch function from NCBI; additional information for each publication was obtained pragmatically using the same tool, retrieving title, authors and DOI (digital object identi er).

### [18] Telomere-to-telomere genome assembly of Phoxinus lagowskii
- Authors: Yanfeng Zhou, Chunhai Chen, Di’an Fang, Chenhe Wang, Yajuan Peng et al.
- Year: 2025
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/23f573aff23769df3b733d508b46f721cadb94ac
- DOI: 10.1038/s41597-025-05367-0
- PMID: 40533492
- PMCID: 12177035
- Citations: 1
- Summary: A T2T (Telomere-to-telomere) genome for P. lagowskii with chromosome-level is reported, serving as an invaluable resource for studies in evolution, comparative genomics, fish breeding applications, and ecological research.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > The gene set of 24,610 genes were functionally annotated using diamond v0.8.23
    > with an E-value threshold of 1E-5 based on the five databases including NR (NCBI nonredundant protein), TrEMB (http://www.uniprot.org), KOG 42 , KEEG (Kyoto Encyclopedia of Genes and Genomes, http://www. genome.jp/kegg/), Swiss-Prot (http://www.gpmaw.com/html/swiss-prot.html). The protein motifs and domains were identified using the InterProScan with InterPro 93.0 43 . The GO Ontology (GO) was classified from the results of InterProScan 44 . The annotation of 24,599 predicted genes (99.96%) out of the total 24,610 genes can be found by at least one database (Fig. 3b and Table 6). Of these functional proteins, 19,367 genes (~78.7%) were supported by five databases (Fig. 3a).

### [19] Identifying orthologs with OMA: A primer
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
  - Snippet 1 (score: 0.691)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [20] AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes
- Authors: D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al.
- Year: 2023
- Venue: Mammalian Genome
- URL: https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99
- DOI: 10.1007/s00335-023-10008-1
- PMID: 37460664
- PMCID: 10382368
- Citations: 5
- Summary: This work presents genome visualization and annotation tools to support seven livestock species, available in a new resource called AgAnimalGenomes, and describes the data and search methods available and how to use the provided tools to edit and create new gene models.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > As previously described (Triant et al. 2020), once a proteincoding gene annotation is complete, each new or modified isoform should be compared to a well-curated protein sequence database to check for congruency with known proteins. The sequence of an annotation is obtained by right clicking it and selecting Get Sequence. The first choice of database to search is the well-curated UniProtKB/Swissprot database using BLAST at either the UniProt (https:// www. unipr ot. org/ blast) or NCBI website (https:// blast. ncbi. nlm. nih. gov/ Blast. cgi) (Sayers et al. 2023a;UniProt Consortium 2023). If there is no match with a significant e-value (< 1e−05) in UniProtKB/Swissprot, the next database to try is the Model Organisms (landmark) database at NCBI. If that fails, select the RefSeq Proteins database and exclude your organism of interest from the search. Although RefSeq includes computationally predicted and hypothetical proteins, an alignment to a homologous protein from another organism provides support for the annotation. An alignment that covers the full length of both the annotated protein and the database protein sequence suggests the annotation is correct. An alignment that encompasses the full length of an annotated protein sequence but only part of a database protein suggests that the annotation is truncated. You may be able to correct the annotation with additional evidence, but if there is not sufficient evidence the issue can be noted in the Annotation Information Panel under the Comment tab. A partial alignment of an annotated protein to a database protein suggests the annotation has a reading frame shift or was extended incorrectly. Aligning the coding sequence (CDS) to the protein database will reveal whether the problem is due to a reading frame shift. Further annotation editing should be performed to correct the reading frame. If an incorrect extension was due to the merging of two genes, you should edit or redo the annotation. Any unresolved issues should be entered in the Comment section of the Annotation Information Panel.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
2. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
5. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
6. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
7. Xiaohua Jiang, Daren Zhao, Asim Ali, Bo Xu, Wei Liu et al. (2021). MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis. Frontiers in Cell and Developmental Biology. https://www.semanticscholar.org/paper/aeb08368a5540685473578345739bb569103bd46
8. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
9. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
10. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
11. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
12. J. Hirschman, T. Berardini, H. Drabkin, D. Howe (2010). A MOD(ern) perspective on literature curation. Molecular Genetics and Genomics. https://www.semanticscholar.org/paper/c98b7209b7106364e1a9b75cd45217efc63f6be5
13. Quan Wan, Hayley M Dingerdissen, Yu Fan, N. Gulzar, Yang Pan et al. (2015). BioXpress: an integrated RNA-seq-derived gene expression database for pan-cancer analysis. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/2852ba7d092a2814e304d9dfbe5a79fa4e0250f8
14. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
15. Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al. (2025). Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining. npj Drug Discovery. https://www.semanticscholar.org/paper/000083b7bd96cff5b3d1891b00ad332eed7d9add
16. Megan R. Teh, Joe N. Frost, A. Armitage, H. Drakesmith (2021). Analysis of Iron and Iron-Interacting Protein Dynamics During T-Cell Activation. Frontiers in Immunology. https://www.semanticscholar.org/paper/912bf84469a61cdc9db3bb47a2104a7bbbcfa4c5
17. Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al. (2024). Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining. Research Square. https://www.semanticscholar.org/paper/795b2985fdc3cf1cfbd5fda1b3c0502eb4dfe866
18. Yanfeng Zhou, Chunhai Chen, Di’an Fang, Chenhe Wang, Yajuan Peng et al. (2025). Telomere-to-telomere genome assembly of Phoxinus lagowskii. Scientific Data. https://www.semanticscholar.org/paper/23f573aff23769df3b733d508b46f721cadb94ac
19. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
20. D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al. (2023). AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes. Mammalian Genome. https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99