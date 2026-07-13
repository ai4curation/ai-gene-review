---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T11:29:25.780512'
end_time: '2026-07-09T11:29:30.527006'
duration_seconds: 4.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: phoR
  gene_symbol: phoR
  uniprot_accession: Q88C62
  protein_description: 'RecName: Full=Phosphate regulon sensor protein PhoR {ECO:0000256|ARBA:ARBA00019665};
    EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};'
  gene_info: Name=phoR {ECO:0000313|EMBL:AAN70886.1}; OrderedLocusNames=PP_5321 {ECO:0000313|EMBL:AAN70886.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: BphY/WalK/GraS-like. (IPR050351); HATPase_C_sf. (IPR036890); HATPase_dom.
    (IPR003594); His_kinase_dom. (IPR005467); HisK_dim/P_dom. (IPR003661)
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
- **UniProt Accession:** Q88C62
- **Protein Description:** RecName: Full=Phosphate regulon sensor protein PhoR {ECO:0000256|ARBA:ARBA00019665}; EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};
- **Gene Information:** Name=phoR {ECO:0000313|EMBL:AAN70886.1}; OrderedLocusNames=PP_5321 {ECO:0000313|EMBL:AAN70886.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** BphY/WalK/GraS-like. (IPR050351); HATPase_C_sf. (IPR036890); HATPase_dom. (IPR003594); His_kinase_dom. (IPR005467); HisK_dim/P_dom. (IPR003661)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "phoR" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'phoR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **phoR** (gene ID: phoR, UniProt: Q88C62) in PSEPK.

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
  - Snippet 1 (score: 0.773)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.688)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.730)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.727)
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
  - Snippet 1 (score: 0.726)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

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
  - Snippet 1 (score: 0.726)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [6] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.700)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

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
  - Snippet 1 (score: 0.691)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [8] A Genome-Wide Association Study Identifying Novel Genetic Markers of Response to Treatment with Interleukin-23 Inhibitors in Psoriasis
- Authors: Sophia Zachari, K. Liadaki, Angeliki Planaki, E. Zafiriou, Olga Kouvarou et al.
- Year: 2025
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/d5f656311b54e222e7487ea32a061869b30178a1
- DOI: 10.3390/genes16101195
- PMID: 41153410
- PMCID: 12564705
- Summary: These findings provide promising pharmacogenetic markers which, upon validation in larger, independent cohorts, will enable the translation of a patient’s genotype into a response phenotype, thereby guiding clinical decisions and improving drug effectiveness.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > The UniProt knowledgebase (www.uniprot.org/uniprotkb/), (accessed on 20 June 2025), the central hub for the collection of functional information on proteins, with accurate and rich annotation [33], was used to retrieve the approved human gene and protein names and symbols.

### [9] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.684)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [10] Protein Localization Analysis of Essential Genes in Prokaryotes
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
  - Snippet 1 (score: 0.680)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

### [11] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.676)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [12] Recent advances in genome annotation and synthetic biology for the development of microbial chassis
- Authors: Saltiel Hamese, Kanganwiro Mugwanda, M. Takundwa, Earl Prinsloo, D. B. Thimiri Govinda Raj
- Year: 2023
- Venue: Journal of Genetic Engineering & Biotechnology
- URL: https://www.semanticscholar.org/paper/64c7c01c15495b3bf0ddb86c33e71d766b554517
- DOI: 10.1186/s43141-023-00598-3
- PMID: 38038785
- PMCID: 10692039
- Citations: 4
- Influential citations: 1
- Summary: The strategies for genome annotations of lactic acid bacteria provide insights into streamlining genome reduction without compromising the functionality of the chassis and the potential for minimal genome chassis development.
- Evidence snippets:
  - Snippet 1 (score: 0.670)
    > Genome annotation identifies functional elements of a genome sequence, indicating its significance. Annotating a genome entails following these steps: identifying genes (including protein-encoding genes and some RNA-encoding genes), predicting the functions of the identified genes, creating metabolic reconstructions and connecting them to genes, labeling phage insertion sequences and transposons, predicting frameshifts and pseudogenes, and identifying regulatory sites and operons, ultimately creating a list of regulons [51]. Regulons are a group of genes or operons that are upregulated or downregulated as a unit by the same protein in response to the same signal. Several genome annotation tools have been developed. These annotation tools may be automated or manual. Automated gene-annotation tools are often used because of the faster annotation and ease of use. However, it is highly recommended that beginners select automatic and semi-automatic annotation methods [31]. Moreover, automatic annotation algorithms, frequently based on orthologs from distantly related model organisms, cannot yet correctly identify all genes within a genome due to confidence and reliability of outcomes as results from different servers or databases are often dissimilar; obtaining accurate gene sets and model manual annotation is often required [21]. Several pipelines for the annotation of genomes have been developed; examples are in Table 1. The gene or protein sequences identified by structural annotation describing the gene structure (e.g., introns, exons, coding sequences, and start and end coordinates) are linked to biological data in a process known as functional annotation, which usually begins with gene identification or gene calling. The different tools for functional annotation are summarized in Table 2. With many genomes sequenced, computational annotation approaches to characterize genes and proteins from their sequences are essential for designing genome deletions.

### [13] Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B
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
  - Snippet 1 (score: 0.670)
    > 2.8.1. Annotation methods 2.8.1.1. Functional annotation. UniProt-GOA database was utilized to retrieve Gene Ontology (GO) annotation proteome. First, the identified protein identity was converted to UniProt identity and then mapped to GO identity based on the protein identity. When the identified protein was not annotated by UniProt-GOA, the functional annotation of that protein was conducted using the InterProScan software according to the amino acid sequence alignment approach. All proteins were then classified into 3 groups: molecular function, cellular component and biological process.

### [14] The quality of metabolic pathway resources depends on initial enzymatic function assignments: a case for maize
- Authors: Jesse R. Walsh, M. Schaeffer, Peifen Zhang, S. Rhee, J. Dickerson et al.
- Year: 2016
- Venue: BMC Systems Biology
- URL: https://www.semanticscholar.org/paper/c41be7766c80fddb3f81c57ced799b8562370cc8
- DOI: 10.1186/s12918-016-0369-x
- PMID: 27899149
- PMCID: 5129634
- Citations: 11
- Influential citations: 1
- Summary: CornCyc’s computational predictions are more accurate than those in MaizeCyc when compared to experimentally determined function assignments, demonstrating the relative strength of the enzymatic function assignment pipeline used to generate CornCyc.
- Evidence snippets:
  - Snippet 1 (score: 0.668)
    > A gold standard set of protein functional annotations was generated by extracting data from UniProt [16] and BRENDA [17]. We extracted all protein sequence and annotation data from UniProt (release 2016_05) for the organism Zea mays, keeping the EC annotations only from the manually reviewed component of UniProt, while removing those annotations that had not undergone manual review. We also extracted experimentally verified protein annotations for Zea mays from BRENDA (release 2016.1). The UniProt and BRENDA annotations were then merged by matching proteins based on the database crosslinks provided by BRENDA, resulting in the union of the reviewed annotations from UniProt and the experimentally verified annotations of BRENDA with duplicates removed. The merged protein annotations were then matched to the B73 RefGen_v2 translated gene models using BLASTP based on a sequence identity cutoff of 96% and an e-value cutoff of 1e-20. We selected the top scoring hit for each protein which resulted in matches to 1,815 unique maize proteins. EC annotations for alternate isoforms were consolidated at the gene level, resulting in 1,475 experimentally verified or manually reviewed protein functional annotations across 1,450 maize genes.

### [15] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
- Authors: Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al.
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
  - Snippet 1 (score: 0.666)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [16] Ten steps to get started in Genome Assembly and Annotation
- Authors: Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al.
- Year: 2018
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
- DOI: 10.12688/f1000research.13598.1
- PMID: 29568489
- PMCID: 5850084
- Citations: 109
- Influential citations: 1
- Summary: Ten steps to facilitate researchers getting started in genome assembly and genome annotation are presented and the importance of data management is stressed, and advice on where to submit data and how to make results Findable, Accessible, Interoperable, and Reusable (FAIR).
- Evidence snippets:
  - Snippet 1 (score: 0.666)
    > The ultimate goal of the functional annotation process (Figure 4) is to assign biologically relevant information to predicted polypeptides, and to the features they derive from (e.g. gene, mRNA). This process is especially relevant nowadays in the context of the NGS era due to the capacity of sequencing, assembling, and annotating full genomes in short periods of time, e.g. less than a month. Functional elements could range from putative name and/or symbols for protein-coding genes, e.g. ADH to its putative biological function, e.g. alcohol dehydrogenase, associated gene ontology terms, e.g. GO:0004022, functional sites, e.g. METAL 47 47 Zinc 1, and domains, e.g. IPR002328, among other features. The function of predicted proteins can be computationally inferred based on the similarity between the sequence of interest and other sequences in different public repositories, e.g. BLASTP against Uniprot. Caution should be taken when assigning results merely based on sequence similarity as two evolutionary independent sequences which share some common domains could be considered homologs 62 . Thus, whenever possible, it is better to use orthologous sequences for annotation purposes rather than simply similar sequences 63 . With the growing number of sequences in those public repositories, it is possible to perform various searches and combine obtained results into a consensus annotation. The accurate assignment of the functional elements is a complex process, and the best annotation will involve manual curation.
    > There are two main outcomes of the functional annotation process. The first is the assignment of functional elements to genes. Downstream analysis of these elements allow further understanding of specific genome properties, e.g. metabolic pathways, and similarities compared with closely related species. The second result of the functional annotation is the additional quality check for the predicted gene set. It is possible to identify problematic and/or suspicious genes by the presence of specific domains, suspicious orthology assignment and/or absence of other functional elements, e.g. functional completeness. These Page 13 of 19

### [17] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.665)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [18] AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes
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
  - Snippet 1 (score: 0.665)
    > As previously described (Triant et al. 2020), once a proteincoding gene annotation is complete, each new or modified isoform should be compared to a well-curated protein sequence database to check for congruency with known proteins. The sequence of an annotation is obtained by right clicking it and selecting Get Sequence. The first choice of database to search is the well-curated UniProtKB/Swissprot database using BLAST at either the UniProt (https:// www. unipr ot. org/ blast) or NCBI website (https:// blast. ncbi. nlm. nih. gov/ Blast. cgi) (Sayers et al. 2023a;UniProt Consortium 2023). If there is no match with a significant e-value (< 1e−05) in UniProtKB/Swissprot, the next database to try is the Model Organisms (landmark) database at NCBI. If that fails, select the RefSeq Proteins database and exclude your organism of interest from the search. Although RefSeq includes computationally predicted and hypothetical proteins, an alignment to a homologous protein from another organism provides support for the annotation. An alignment that covers the full length of both the annotated protein and the database protein sequence suggests the annotation is correct. An alignment that encompasses the full length of an annotated protein sequence but only part of a database protein suggests that the annotation is truncated. You may be able to correct the annotation with additional evidence, but if there is not sufficient evidence the issue can be noted in the Annotation Information Panel under the Comment tab. A partial alignment of an annotated protein to a database protein suggests the annotation has a reading frame shift or was extended incorrectly. Aligning the coding sequence (CDS) to the protein database will reveal whether the problem is due to a reading frame shift. Further annotation editing should be performed to correct the reading frame. If an incorrect extension was due to the merging of two genes, you should edit or redo the annotation. Any unresolved issues should be entered in the Comment section of the Annotation Information Panel.

### [19] Functional annotation of parasitic worm genomes, by assigning protein names and GO terms
- Authors: Avril Coghlan, M. Berriman
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
- DOI: 10.1038/protex.2018.055
- Citations: 1
- Summary: A computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and Go terms from orthologues in other species.
- Evidence snippets:
  - Snippet 1 (score: 0.660)
    > Given a set of predicted protein-coding genes for a newly sequenced genome, functional annotation involves assigning putative functions to the predicted genes. Two ways in which this can be done are assigning protein names and Gene Ontology (GO;Gene Ontology Consortium, 2010) terms to the predicted proteins. Here we describe a computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and GO terms from orthologues in other species.
    > When assigning protein names, UniProt protein naming rules (www.uniprot.org/docs/nameprot) are followed where possible. This recommends that a good and stable name for a protein is "as neutral as possible"; that a protein name "should be, as far as possible, unique and attributed to all orthologs"; and a protein name "should not contain a specific characteristic of the protein, and in particular it should not reflect the function or role of the protein, nor its subcellular location, its domain structure, its tissue specificity, its molecular weight or its species of origin".
    > In our protocol, a protein name is assigned to each predicted protein based on curated names in UniProt (Bairoch & Apweiler, 2000) for human, zebrafish, Drosophila melanogaster, Caenorhabditis elegans, and Schistosoma mansoni orthologues identified from a database of gene families (e.g. built using Ensembl Compara; Vilella et al. 2009), or (if no information is found from orthologues) based on InterPro (Hunter et al. 2012) domains. Figure 1 shows an example of using our protein naming pipeline for four Strongyloides ratti genes that belong to the tubulin polyglutamylase family (underlined in pink), where four different protein names were assigned to them (in pink), based on names of their C. elegans or human orthologues.
    > Since each of the S. ratti genes belonged to a different subfamily of the tubulin polyglutamylase family, they were assigned different names.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
5. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
6. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
7. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
8. Sophia Zachari, K. Liadaki, Angeliki Planaki, E. Zafiriou, Olga Kouvarou et al. (2025). A Genome-Wide Association Study Identifying Novel Genetic Markers of Response to Treatment with Interleukin-23 Inhibitors in Psoriasis. Genes. https://www.semanticscholar.org/paper/d5f656311b54e222e7487ea32a061869b30178a1
9. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
10. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
11. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
12. Saltiel Hamese, Kanganwiro Mugwanda, M. Takundwa, Earl Prinsloo, D. B. Thimiri Govinda Raj (2023). Recent advances in genome annotation and synthetic biology for the development of microbial chassis. Journal of Genetic Engineering & Biotechnology. https://www.semanticscholar.org/paper/64c7c01c15495b3bf0ddb86c33e71d766b554517
13. Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al. (2022). Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B. Data in Brief. https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
14. Jesse R. Walsh, M. Schaeffer, Peifen Zhang, S. Rhee, J. Dickerson et al. (2016). The quality of metabolic pathway resources depends on initial enzymatic function assignments: a case for maize. BMC Systems Biology. https://www.semanticscholar.org/paper/c41be7766c80fddb3f81c57ced799b8562370cc8
15. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
16. Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al. (2018). Ten steps to get started in Genome Assembly and Annotation. F1000Research. https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
17. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
18. D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al. (2023). AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes. Mammalian Genome. https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99
19. Avril Coghlan, M. Berriman (2018). Functional annotation of parasitic worm genomes, by assigning protein names and GO terms. https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82