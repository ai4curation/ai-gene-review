---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-06T16:30:48.485240'
end_time: '2026-07-06T16:30:53.680541'
duration_seconds: 5.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: alr
  gene_symbol: alr
  uniprot_accession: Q88GJ9
  protein_description: 'RecName: Full=Broad specificity amino-acid racemase {ECO:0000255|HAMAP-Rule:MF_02212,
    ECO:0000305|PubMed:30008699}; EC=5.1.1.10 {ECO:0000255|HAMAP-Rule:MF_02212, ECO:0000269|PubMed:23995642};
    AltName: Full=Broad spectrum racemase {ECO:0000303|PubMed:30008699}; Flags: Precursor;'
  gene_info: Name=alr {ECO:0000303|PubMed:23995642, ECO:0000312|EMBL:AAN69319.1};
    OrderedLocusNames=PP_3722 {ECO:0000312|EMBL:AAN69319.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the alanine racemase family. Bsr subfamily.
  protein_domains: Ala_racemase. (IPR000821); Ala_racemase/Decarboxylase_C. (IPR009006);
    Ala_racemase_C. (IPR011079); Ala_racemase_N. (IPR001608); Ala_racemase_pyridoxalP-BS.
    (IPR020622)
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
- **UniProt Accession:** Q88GJ9
- **Protein Description:** RecName: Full=Broad specificity amino-acid racemase {ECO:0000255|HAMAP-Rule:MF_02212, ECO:0000305|PubMed:30008699}; EC=5.1.1.10 {ECO:0000255|HAMAP-Rule:MF_02212, ECO:0000269|PubMed:23995642}; AltName: Full=Broad spectrum racemase {ECO:0000303|PubMed:30008699}; Flags: Precursor;
- **Gene Information:** Name=alr {ECO:0000303|PubMed:23995642, ECO:0000312|EMBL:AAN69319.1}; OrderedLocusNames=PP_3722 {ECO:0000312|EMBL:AAN69319.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the alanine racemase family. Bsr subfamily.
- **Key Domains:** Ala_racemase. (IPR000821); Ala_racemase/Decarboxylase_C. (IPR009006); Ala_racemase_C. (IPR011079); Ala_racemase_N. (IPR001608); Ala_racemase_pyridoxalP-BS. (IPR020622)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "alr" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'alr' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **alr** (gene ID: alr, UniProt: Q88GJ9) in PSEPK.

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
  - Snippet 1 (score: 0.763)
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
  - Snippet 1 (score: 0.726)
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
  - Snippet 1 (score: 0.717)
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
  - Snippet 1 (score: 0.705)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [5] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.703)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [6] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.688)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [7] Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B
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
  - Snippet 1 (score: 0.685)
    > 2.8.1. Annotation methods 2.8.1.1. Functional annotation. UniProt-GOA database was utilized to retrieve Gene Ontology (GO) annotation proteome. First, the identified protein identity was converted to UniProt identity and then mapped to GO identity based on the protein identity. When the identified protein was not annotated by UniProt-GOA, the functional annotation of that protein was conducted using the InterProScan software according to the amino acid sequence alignment approach. All proteins were then classified into 3 groups: molecular function, cellular component and biological process.

### [8] GOnet: a tool for interactive Gene Ontology analysis
- Authors: M. Pomaznoy, Brendan Ha, Bjoern Peters
- Year: 2018
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/d984d075cb08f6c39a48bcf1f32e36f333a423d9
- DOI: 10.1186/s12859-018-2533-3
- PMID: 30526489
- PMCID: 6286514
- Citations: 247
- Influential citations: 17
- Summary: The open-source GOnet web-application is created, which takes a list of gene or protein entries from human or mouse data and performs GO term annotation analysis and provides insight into the functional interconnection of the submitted entries.
- Evidence snippets:
  - Snippet 1 (score: 0.677)
    > In a basic workflow, the GOnet application receives a list of gene symbols, protein symbols, or protein IDs (UniProt IDs) as an input, and outputs a graph (an example given in Fig. 1). There are various input parameters which will affect the actual structure of the graph visualized and its appearance. The first main user choice is which GO terms the genes are annotated against:
    > 1. GO terms statistically significantly over-represented in the gene list submitted. 2. A predefined subset (also known as 'GO slim'), or a user-supplied list of terms.
    > In the first case the analysis will be referred to as an 'enrichment' analysis, in the second as an 'annotation' analysis.
    > Input parameters 1) Gene list. A mandatory input parameter containing the genes/proteins of interest. Currently human and mouse data is supported. An example of a human gene list might look like this:
    > Fig. 1 Sample network output generated by GOnet application. Gene differentially expressed in CD4 Bulk Memory T cells in Latent TB patients compared to healthy controls were used as an example [22] The gene list can also be accompanied with a contrast value. For example, This contrast value can be any decimal number, such as the log-fold change of gene expression between two conditions. This is merely a visualization enhancement. If the value is supplied it can be used later to differentially color specific genes in the graph (note different colors of gene nodes in Fig. 1), and visually indicate up-or down-regulation of specific genes and gene clusters.
    > The application can process common gene symbols (like in the example above), UniProt IDs, and MGI Accession IDs (mouse only). The former type of ID (gene symbols), although is the most human friendly, can unfortunately be ambiguous. For example, AIM1 can mean 'absent in melanoma' (also called CRYBG1) or 'Aurora and Ipl1-like midbody-associated protein' (also known as AURKB). Due to this ambiguity UniProt IDs or MGI accession IDs (for mouse) are preferred.
    > 2) GO namespace. Can be any of 'biological process', 'molecular function' or 'cellular component'.

### [9] OntoGene in BioCreative II
- Authors: Fabio Rinaldi, T. Kappeler, K. Kaljurand, Gerold Schneider, Manfred Klenner et al.
- Year: 2007
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/ffcbf659129388203ce458ce1b25e5449e9594e7
- DOI: 10.1186/gb-2008-9-s2-s13
- PMID: 18834491
- PMCID: 2559984
- Citations: 78
- Influential citations: 1
- Summary: This report describes approaches taken within the scope of the second BioCreative competition in order to solve two aspects of this problem: detection of novel protein interactions reported in scientific articles, and detection of the experimental method that was used to confirm the interaction.
- Evidence snippets:
  - Snippet 1 (score: 0.675)
    > It is well known that protein names are highly ambiguous [45,46]. Researchers working in specific subcommunities tend to develop their own nomenclature, resulting in multiple names for the same protein. Acronyms and abbreviations further complicate the picture. Simply being able to recognize a protein name as such is just a starting point. The name needs then to be unambiguously qualified, by referring to an entry in a standard protein database, such as UniProt http:// www.expasy.org/sprot/ [47].
    > In order for that to happen, the disambiguation must occur at two levels: interspecies (to which specific organisms does the protein mention refer?) and intraspecies (within a given organism, which specific protein is meant?). For example, a protein mentioned in text as eIF4E could refer to a large number of different proteins. A search in the Swiss-Prot section of UniProt (the manually curated section) delivers 46 possible matches. However, if the term appears contextually with the mention of a specific organism, like in the sentence 'The Cap-binding protein eIF4E promotes folding of a functional domain of yeast translation initiation factor eIF4G1' (PubMed: 10409688), then it is reasonable to assume that the name refers to a specific organism (yeast), thus restricting the possible matches in UniProt to the following two: EAP1_YEAST (eIF4E-associated protein 1) and IF4E_YEAST (eukaryotic translation initiation factor 4E). For the task of protein annotation, we have adopted a high-recall, low-precision term annotation approach, followed by very strict disambiguation steps, which gradually increase precision (at some expense for recall).
    > UniProt contains for each protein a list of frequently used synonyms, as well as the name and synonyms of its encoding gene. We have built a database that maps the synonyms to the protein identifier. We have further enriched such a list using morpho-syntactic rules that generate variants of the synonyms. Starting from the subset of UniProt delivered by the BioCreative organizers (which contained 228,

### [10] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Citations: 1
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.671)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [11] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.668)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [12] Functional annotation of parasitic worm genomes, by assigning protein names and GO terms
- Authors: Avril Coghlan, M. Berriman
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
- DOI: 10.1038/protex.2018.055
- Citations: 1
- Summary: A computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and Go terms from orthologues in other species.
- Evidence snippets:
  - Snippet 1 (score: 0.667)
    > Given a set of predicted protein-coding genes for a newly sequenced genome, functional annotation involves assigning putative functions to the predicted genes. Two ways in which this can be done are assigning protein names and Gene Ontology (GO;Gene Ontology Consortium, 2010) terms to the predicted proteins. Here we describe a computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and GO terms from orthologues in other species.
    > When assigning protein names, UniProt protein naming rules (www.uniprot.org/docs/nameprot) are followed where possible. This recommends that a good and stable name for a protein is "as neutral as possible"; that a protein name "should be, as far as possible, unique and attributed to all orthologs"; and a protein name "should not contain a specific characteristic of the protein, and in particular it should not reflect the function or role of the protein, nor its subcellular location, its domain structure, its tissue specificity, its molecular weight or its species of origin".
    > In our protocol, a protein name is assigned to each predicted protein based on curated names in UniProt (Bairoch & Apweiler, 2000) for human, zebrafish, Drosophila melanogaster, Caenorhabditis elegans, and Schistosoma mansoni orthologues identified from a database of gene families (e.g. built using Ensembl Compara; Vilella et al. 2009), or (if no information is found from orthologues) based on InterPro (Hunter et al. 2012) domains. Figure 1 shows an example of using our protein naming pipeline for four Strongyloides ratti genes that belong to the tubulin polyglutamylase family (underlined in pink), where four different protein names were assigned to them (in pink), based on names of their C. elegans or human orthologues.
    > Since each of the S. ratti genes belonged to a different subfamily of the tubulin polyglutamylase family, they were assigned different names.

### [13] Towards comprehensive annotation of Drosophila melanogaster enzymes in FlyBase
- Authors: Phani V. Garapati, Jingyao Zhang, Alix J. Rey, Steven J. Marygold
- Year: 2019
- Venue: Database: The Journal of Biological Databases and Curation
- URL: https://www.semanticscholar.org/paper/21a58bbde7dc287c6e30c17c08261f4bfca05629
- DOI: 10.1093/database/bay144
- PMID: 30689844
- PMCID: 6343044
- Citations: 11
- Influential citations: 1
- Summary: The review workflow, the improvement in the quality and coverage of enzyme annotations within FlyBase and the wider impact of the work on other related databases are described.
- Evidence snippets:
  - Snippet 1 (score: 0.658)
    > The first number corresponds to one of seven different classes according to the type of chemistry being carried out; the second and third numbers correspond to the chemical bond acted on (subclasses) and reaction (sub-subclasses), respectively; and the last number defines substrate specificity. For example, alanine racemase is an isomerase (EC 5), in particular a racemase (EC 5.1) that acts on the amino acid (EC 5.1.1) alanine (EC 5.1.1.1). EC annotations are prevalent in metabolic pathway-oriented databases such as MetaCyc/BioCyc (7) and KEGG (8) and are also used in UniProtKB (9), NCBI Gene (10) and some model organism databases (MODs).
    > The GO is the most widely used controlled vocabulary describing gene product function (11). GO annotations unify functional descriptions across all the major MODs, UniProtKB and other biological databases. Unlike EC codes, GO terms are assigned to genes/gene products as part of a fuller annotation that includes the source of the assertion and an 'evidence code' (12) to describe how the annotation to a particular term is supported. GO annotations may be made based on: i. experimental data, ii. computational analyses of gene/gene product sequences, iii. author statements or iv. inferences from electronic (automated) pipelines, such as the presence of protein domains via 'InterPro2GO' mapping (Table 1). Importantly, catalytic activity terms in the GO are crossreferenced to equivalent EC numbers. For example, EC 5.1.1.1 is a cross-reference for the GO term 'alanine racemase activity' (GO:0008784).
    > The fruit fly, Drosophila melanogaster, has been used as a model system to study enzyme function for over a century. Many classical eye color mutations were later found to disrupt enzymes (13) and experiments in the 1930s and 1940s by Beadle and colleagues helped establish the connection between genes, enzymes and metabolic pathways [reviewed in (14)].

### [14] Prioritising genetic findings for drug target identification and validation.
- Authors: N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt
- Year: 2024
- Venue: Atherosclerosis
- URL: https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9
- DOI: 10.1016/j.atherosclerosis.2024.117462
- PMID: 38325120
- Citations: 11
- Summary: The current review provides an overview of genetic evidence for drug target identification, and how biomedical databases can be used to provide actionable prioritisation, fully informing downstream experimental validation.
- Evidence snippets:
  - Snippet 1 (score: 0.648)
    > Other gene identification systems include the Entrez Gene [43] database for gene-specific information, and the HUGO Gene Nomenclature Committee (HGNC) [44] which maintains unique symbols and names for human loci.An analogue for proteins is the UniProt Knowledgebase (UniProtKB) [45], which contains data on protein sequences and function, and each protein in the database is assigned a unique UniProt accession ID.UniProt provides functionality to map between different identifiers, including Ensembl IDs and UniProt accession IDs.
    > A common naming convention is also required to identify the diseases associated with the drug targets.Medical Subject Headings (MeSH) [46] are terms defined by the National Library of Medicine, and act as a standardised thesaurus for diseases and medical conditions which can be used to index PubMed.In some data sources, such as the Chemical Biology Database (ChEMBL) [23], diseases and outcomes will be identified by MeSH terms.However, in other cases, this will not be the case, and a metathesaurus such as the Unified Medical Language System (UMLS) [47] can be used to map synonymous disease terms.

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
  - Snippet 1 (score: 0.648)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [16] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.644)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [17] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.643)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [18] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
- Authors: Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al.
- Year: 2025
- Venue: Molecular Ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 3
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.643)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [19] GRIMM: Genetic stRatification for Inference in Molecular Modeling
- Authors: Ashley Babjac, Adrienne Hoarfrost
- Year: 2026
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/a923e3c2800f1ce4cc937015594f74395af624a9
- Citations: 1
- Summary: GRIMM (Genetic stRatification for Inference in Molecular Modeling), a benchmark for enzyme function prediction that employs genetic stratification, enables more realistic evaluation of functional prediction models on both familiar and unseen classes and establishes a benchmark that more faithfully assesses model performance and generalizability.
- Evidence snippets:
  - Snippet 1 (score: 0.643)
    > We used amino acid sequence data from the Universal Protein Resource (UniProt) UniProt Consortium [2025] and associated gene DNA coding sequences in the European Nucleotide Archive (ENA) Leinonen et al. [2010]. The UniProt database is divided into two sections: (i) UniProt/TrEMBL (which includes more sequence diversity but more annotation errors owing to homology-based annotations and error propagation Schnoes et al. [2009]) and (ii) UniProt/SwissProt (which is carefully curated and provides high confidence accurate functional annotations). For this study, we limited the data retrieved to prokaryotic organisms in SwissProt (May 2025) UniProt Consortium [2025].
    > We mapped UniProt/SwissProt accession numbers to corresponding identifiers in UniRef (Universal Protein Resource Reference Clusters) UniRef50, UniRef90, and UniRef100, which define protein clusters based on amino acid sequence identity at 50, 90, and 100 percent amino acid identity respectively; and to their corresponding EMBL CDS IDs for gene coding sequences in the ENA database Leinonen et al. [2010] using ID mapping files uni [2021], Wang et al. [2021] from UniProtKB. Each EMBL CDS ID's corresponding DNA sequence was then obtained from ENA. EC numbers that were either incomplete or missing were removed from the dataset. Individual entries were created for UniProt records with more than one EMBL CDS ID in the nucleotide version of the dataset.

### [20] Deep sequencing of Danish Holstein dairy cattle for variant detection and insight into potential loss-of-function variants in protein coding genes
- Authors: Ashutosh Das, F. Panitz, V. R. Gregersen, C. Bendixen, L. Holm
- Year: 2015
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/b96532e082a2c5b0f3f0fc51afc47ac2426b4904
- DOI: 10.1186/s12864-015-2249-y
- PMID: 26645365
- PMCID: 4673847
- Citations: 36
- Influential citations: 3
- Summary: Deep sequencing of Danish Holstein genomes enabled us to identify 12.1 million variants, a catalog of variants that will be a resource for future studies to understand variation underlying important phenotypes, particularly recessively inherited lethal phenotypes.
- Evidence snippets:
  - Snippet 1 (score: 0.642)
    > We used NGS-SNP [25] for functional annotation of identified SNPs and indels. The details of the resulting annotation fields have been described by Grant et al. [25]. Briefly, NGS-SNP provides rich annotations for genome-wide SNP and indels in organisms for which reference sequences are available in the Ensembl database. It reports a "Model_Annotations" field with detailed comparisons of SNP/indel to an orthologous gene typically in a well-characterized species. NGS-SNP also classifies whether or not the amino acid change is deleterious based on SIFT [56] prediction. Other important fields include overlapping protein features or domains, gene ontology information, and the conservation of both the SNP site and flanking sequence compared to a well-characterized species. NGS-SNP also reports NCBI, Ensembl, and UniProt IDs for genes, transcripts, and proteins when applicable. A gene description, phenotypes linked to the gene and whether the SNP/indel is novel or known is also supplemented in the annotated field. In our analysis, NGS-SNP utilized information from Ensembl release 72 [57], dbSNP Build 133 [58], Entrez Gene [58] and UniProt release 2013_09 [59]. We incorporated Homo sapiens as the model species for sequence conservation during annotation because most of the eukaryotic genes are well characterized in human.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
5. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
6. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
7. Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al. (2022). Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B. Data in Brief. https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
8. M. Pomaznoy, Brendan Ha, Bjoern Peters (2018). GOnet: a tool for interactive Gene Ontology analysis. BMC Bioinformatics. https://www.semanticscholar.org/paper/d984d075cb08f6c39a48bcf1f32e36f333a423d9
9. Fabio Rinaldi, T. Kappeler, K. Kaljurand, Gerold Schneider, Manfred Klenner et al. (2007). OntoGene in BioCreative II. Genome Biology. https://www.semanticscholar.org/paper/ffcbf659129388203ce458ce1b25e5449e9594e7
10. Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
11. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
12. Avril Coghlan, M. Berriman (2018). Functional annotation of parasitic worm genomes, by assigning protein names and GO terms. https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
13. Phani V. Garapati, Jingyao Zhang, Alix J. Rey, Steven J. Marygold (2019). Towards comprehensive annotation of Drosophila melanogaster enzymes in FlyBase. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/21a58bbde7dc287c6e30c17c08261f4bfca05629
14. N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt (2024). Prioritising genetic findings for drug target identification and validation.. Atherosclerosis. https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9
15. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
16. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
17. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
18. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
19. Ashley Babjac, Adrienne Hoarfrost (2026). GRIMM: Genetic stRatification for Inference in Molecular Modeling. https://www.semanticscholar.org/paper/a923e3c2800f1ce4cc937015594f74395af624a9
20. Ashutosh Das, F. Panitz, V. R. Gregersen, C. Bendixen, L. Holm (2015). Deep sequencing of Danish Holstein dairy cattle for variant detection and insight into potential loss-of-function variants in protein coding genes. BMC Genomics. https://www.semanticscholar.org/paper/b96532e082a2c5b0f3f0fc51afc47ac2426b4904