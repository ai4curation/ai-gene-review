---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T13:30:43.418803'
end_time: '2026-07-10T13:30:48.377755'
duration_seconds: 4.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cmoB
  gene_symbol: cmoB
  uniprot_accession: Q88MX8
  protein_description: 'RecName: Full=tRNA U34 carboxymethyltransferase {ECO:0000255|HAMAP-Rule:MF_01590};
    EC=2.5.1.- {ECO:0000255|HAMAP-Rule:MF_01590};'
  gene_info: Name=cmoB {ECO:0000255|HAMAP-Rule:MF_01590}; OrderedLocusNames=PP_1440;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class I-like SAM-binding methyltransferase
  protein_domains: CmoB. (IPR010017); Mo5U34_MeTrfas-like. (IPR027555); SAM-dependent_MTases_sf.
    (IPR029063); Methyltransf_9 (PF08003)
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
- **UniProt Accession:** Q88MX8
- **Protein Description:** RecName: Full=tRNA U34 carboxymethyltransferase {ECO:0000255|HAMAP-Rule:MF_01590}; EC=2.5.1.- {ECO:0000255|HAMAP-Rule:MF_01590};
- **Gene Information:** Name=cmoB {ECO:0000255|HAMAP-Rule:MF_01590}; OrderedLocusNames=PP_1440;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class I-like SAM-binding methyltransferase
- **Key Domains:** CmoB. (IPR010017); Mo5U34_MeTrfas-like. (IPR027555); SAM-dependent_MTases_sf. (IPR029063); Methyltransf_9 (PF08003)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cmoB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cmoB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cmoB** (gene ID: cmoB, UniProt: Q88MX8) in PSEPK.

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
  - Snippet 1 (score: 0.760)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [2] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.729)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [3] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Citations: 1
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.726)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [4] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.725)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [5] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.701)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

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
  - Snippet 1 (score: 0.700)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [7] Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea
- Authors: A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al.
- Year: 2023
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
- DOI: 10.3389/fmicb.2023.1066096
- PMID: 36876067
- PMCID: 9981795
- Citations: 2
- Summary: The present study concludes that deciphering the whole genome of F. udum would be instrumental in understanding evolution, virulence determinants, host-pathogen interaction, possible control strategies, ecological behavior, and many other complexities of the pathogen.
- Evidence snippets:
  - Snippet 1 (score: 0.698)
    > The BLASTx homology search tool, a component of the standalone NCBI-blast-2.3.0+, was used to perform functional annotation of the F. udum genes (Altschul et al., 1990). With a cut-off E value of ≤1e−06 and a similarity of 34%, BLASTx identified the homologous sequences of the genes in the NCBI non-redundant protein database. Gene ontology (GO) analysis was carried out using Blast2GO PRO 4.1.5 (Conesa and Gotz, 2008). In three different mappings, B2G performed as follows: (1) Using two NCBI-provided mapping files, blast result accessions are used to get gene names (symbols; gene info, gene 2 accessions). (2) Blast result GI identifiers were used to retrieve UniProt IDs using a mapping file from PIR (non-redundant reference protein database), which includes PSD, Swiss-Prot, UniProt, TrEMBL, GenPept, RefSeq, and PDB. The names of the identified genes were searched in the species-specific entries of the gene product table of the GO database. With the aid of the KAAS-KEGG Automatic Annotation Server, pathway analyses were carried out. This database provides functional annotation of genes using other data servers (Moriya et al., 2007). Accessions from the blast results were looked for in the DBXRef table of the GO database.

### [8] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.695)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [9] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.693)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [10] The y-ome defines the thirty-four percent of Escherichia coli genes that lack experimental evidence of function
- Authors: S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson
- Year: 2018
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/b55c92ec2394bb9ebdff9d019f9afb7238e5c8ba
- DOI: 10.1101/328591
- Citations: 4
- Summary: This work identified the genes that lack direct experimental evidence of function (the “y-ome”) and discusses the value of the y-ome for systematic improvement of E. coli knowledge bases and its extension to other organisms.
- Evidence snippets:
  - Snippet 1 (score: 0.687)
    > Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et al. constructed a global functional atlas of E. coli proteins (18) . First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with "y", (ii) the gene does not have a known pathway within EcoCyc, and (iii) the gene does not have a functional description in GenProtEC (19) (any gene with a description containing the words "predicted", "hypothetical", or "conserved"). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were functionally unannotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (20) . This study also quantified the number of uncharacterized protein coding genes in E. coli . To assess functional annotation, they used the presence of experimentally supported "biological process" annotations in the Gene Ontology database (21) . They concluded that ~2000 protein coding genes in E. coli were functionally unannotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COMBREX) (22,23) . The COMBREX knowledge base currently contains information about 4182 protein coding genes in E. coli K-12 MG1655, of which 2378 (57%) have experimentally verified function, 1741 (42%) have predicted but not experimentally verified function, and 63 (2%) have no predicted function. These studies of unannotated genes in E. coli K-12 MG1655 provided inspiration for this work.

### [11] Antibodies to biotin enable large-scale detection of biotinylation sites on proteins
- Authors: N. Udeshi, Kayvon Pedram, Tanya Svinkina, Shaunt Fereshetian, S. Myers et al.
- Year: 2017
- Venue: Nature methods
- URL: https://www.semanticscholar.org/paper/f9e4f461ca61f4399a95875ea96fb075fa959901
- DOI: 10.1038/nmeth.4465
- PMID: 29039416
- PMCID: 8954634
- Citations: 124
- Influential citations: 3
- Summary: It is shown that anti-biotin antibodies enable unprecedented enrichment of biotinylated peptides from complex peptide mixtures.
- Evidence snippets:
  - Snippet 1 (score: 0.686)
    > All human IDs used for data annotation were downloaded from Uniprot 20 FTP (URL: ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledge-base/ idmapping/by_organism/, Version: 10/03/2016). The resulting data provided 133,996 unique identifications, which were in turn used to query the Uniprot database. This search returned HHMI Author Manuscript HHMI Author Manuscript HHMI Author Manuscript 109,961 records (including reviewed and unreviewed) along with their functional and structural annotations, including gene ontology features. The annotation table was used to search for mitochondrial evidence associated with a given Uniprot identification in our proximity-labeling anti-biotin-enriched data set by using a string match algorithm. A given protein was annotated as having mitochondrial evidence if any of the following were true: (i) the string 'mitoch' matched the above UniProt annotation table when queried by either gene name or accession number. (ii) The protein showed mitochondrial evidence from a list of mitochondrial proteins which was the same as our previous study (Rhee et al. 11 ) and a precursor to MitoCarta2.0 catalog 28 . (iii) The protein was present in the original mitochondrial true positive list used Rhee et al. 11 . Thebiotinylated peptide data were filtered such that reverse hits, nonhuman contaminants, nonfully localized biotinylation sites, sites identified in the SILAC light state, and redundant biotin site entries were removed. From this list, transmembrane proteins were annotated using the following criteria: (i) the UniProt transmembrane annotation contains the string "TRANSMEM" when matched by either gene name or accession number and/or (ii) evidence from of transmembrane domains after running the precursor MitoCarta2.0 catalog through TMHMM 29 . The UniProt topological domain annotation contained the string "TOPO" when matched by either gene name or accession number.

### [12] Ten steps to get started in Genome Assembly and Annotation
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
  - Snippet 1 (score: 0.682)
    > The ultimate goal of the functional annotation process (Figure 4) is to assign biologically relevant information to predicted polypeptides, and to the features they derive from (e.g. gene, mRNA). This process is especially relevant nowadays in the context of the NGS era due to the capacity of sequencing, assembling, and annotating full genomes in short periods of time, e.g. less than a month. Functional elements could range from putative name and/or symbols for protein-coding genes, e.g. ADH to its putative biological function, e.g. alcohol dehydrogenase, associated gene ontology terms, e.g. GO:0004022, functional sites, e.g. METAL 47 47 Zinc 1, and domains, e.g. IPR002328, among other features. The function of predicted proteins can be computationally inferred based on the similarity between the sequence of interest and other sequences in different public repositories, e.g. BLASTP against Uniprot. Caution should be taken when assigning results merely based on sequence similarity as two evolutionary independent sequences which share some common domains could be considered homologs 62 . Thus, whenever possible, it is better to use orthologous sequences for annotation purposes rather than simply similar sequences 63 . With the growing number of sequences in those public repositories, it is possible to perform various searches and combine obtained results into a consensus annotation. The accurate assignment of the functional elements is a complex process, and the best annotation will involve manual curation.
    > There are two main outcomes of the functional annotation process. The first is the assignment of functional elements to genes. Downstream analysis of these elements allow further understanding of specific genome properties, e.g. metabolic pathways, and similarities compared with closely related species. The second result of the functional annotation is the additional quality check for the predicted gene set. It is possible to identify problematic and/or suspicious genes by the presence of specific domains, suspicious orthology assignment and/or absence of other functional elements, e.g. functional completeness. These Page 13 of 19

### [13] Characterization of holins, the membrane proteins of coliphage ASEC2201: a genomewide in silico approach
- Authors: Humaira Saeed, Sudhaker Padmesh, Aditi Singh, S. Singh, Mohammed Haris Siddiqui et al.
- Year: 2025
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/a39392e12bf3bda67bdfe600053e8403deb3b887
- DOI: 10.3389/fmicb.2025.1550594
- PMID: 40703241
- PMCID: 12283622
- Citations: 4
- Summary: In silico identification of cell-penetrating peptide motifs within the holin sequences suggests potential for enhanced intracellular delivery in CPP-fusion therapeutic constructs and demonstrates the potential of integrative in silico approaches in developing a comprehensive foundation for future experimental validation for proteins with no prior functional annotation.
- Evidence snippets:
  - Snippet 1 (score: 0.679)
    > Protein-coding gene annotation is typically a two-step process. Initially, Prodigal is employed to identify open reading frames (ORFs) by locating gene coordinates, but it does not infer gene function. To assign putative functions, Prokka performs hierarchical annotation by comparing candidate genes to curated protein databases. It begins with a user-supplied, high-confidence protein set, using BLAST+ for sequence similarity searches. If no match is found, it progresses to UniProt's verified bacterial proteins, covering \~ 16,000 sequences, and then optionally to RefSeq proteins specific to the organism's genuscapturing nomenclature consistency. When sequence-based annotation fails, Prokka applies profile-based searches using HMMER's hmmscan to query against Pfam and TIGRFAMs databases. An e-value threshold of 10 −6 is consistently applied to ensure significance. If no reliable match is found across all levels, the gene is designated as a "hypothetical protein. " This layered strategy maximizes annotation accuracy and functional insight across diverse bacterial genomes (Seemann, 2014).
    > The genome of coliphage ASEC2201 has been analyzed and three holin protein coding genes were selected. The sequences of all three holin proteins were retrieved from NCBI using accession no. SRX17770782 in the FASTA format. The sequence similarity search was performed via BLAST against the non-redundant database (Altschul et al., 1990).

### [14] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.678)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [15] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.676)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [16] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
- Authors: Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al.
- Year: 2025
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
- DOI: 10.1093/nar/gkaf1206
- PMID: 41206768
- PMCID: 12807602
- Citations: 3
- Summary: The new RM2Target v2.0 will serve as a foundational resource for exploring RNA epitranscriptomic regulation, enabling investigations into cross-talk among modifications, underlying molecular mechanisms, and disease connections, thereby facilitating both basic research and translational applications in RNA epigenetics.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [17] Prediction of Horizontally and Widely Transferred Genes in Prokaryotes
- Authors: Yoji Nakamura
- Year: 2018
- Venue: Evolutionary Bioinformatics Online
- URL: https://www.semanticscholar.org/paper/af7bde229b96609907924d1c68ea463af656efb2
- DOI: 10.1177/1176934318810785
- PMID: 30546254
- PMCID: 6287321
- Citations: 5
- Influential citations: 1
- Summary: A data-driven approach using massive sequence data may contribute to a broader understanding of HGT in prokaryotes, and predicted that six as-yet-uncharacterized genes were widely distributed HT genes, and therefore, will be interesting targets for evolutionary studies.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > Focusing on uncharacterized HT genes in the COG and KEGG databases, four gene groups (COG3209, COG1479, COG3291, and COG3791) were classified into "general function prediction only" (COG category code = R) or "function unknown" (S) according to the COG annotation. By adding two gene groups of "uncharacterized protein" (K08998 and K07062) from the KEGG annotation, a total of six were obtained as functionally ambiguous HT gene groups despite being distributed among more than 300 species. With reference to COG3209 (uncharacterized conserved protein RhaS, contains 28 RHS repeats), the genes encoded in E. coli have been suggested to be horizontally transferred from another organism. 43 Recently, RHS repeat-containing genes are reported to be involved in toxins against competitors 44 ; therefore, the genes in COG3209 could be considered as defense system genes. The functions of COG1479 (uncharacterized conserved protein, contains ParB-like and HNH nuclease domains), COG3291 (PKD repeat), and COG3791 (uncharacterized conserved protein) have yet to be examined. According to InterPro analysis, COG3791 genes have a domain of glutathione-dependent formaldehyde-activating enzyme (IPR006913); therefore, these genes might be related to formaldehyde detoxification. 45 The KO group, K08998, corresponds to COG0759 (membraneanchored protein YidD) of category M in the COG database that has previously been reported to be involved in the protein insertion process. 46 K07062 corresponds to COG1487 and is considered a toxic protein. 47 As a whole, it has to be said that the evolutionary significance of these six gene groups has not been fully realized. Conversely, these genes might be good targets for evolutionary studies in the context of HGT, providing an example of data-driven approaches from massive sequence data. 48

### [18] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [19] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.671)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [20] CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts
- Authors: Alison C. Testa, James K. Hane, S. Ellwood, R. Oliver
- Year: 2015
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/06704917bf44cd62eef0bb5cb944b97484056e21
- DOI: 10.1186/s12864-015-1344-4
- PMID: 25887563
- PMCID: 4363200
- Citations: 164
- Influential citations: 20
- Summary: CodingQuarry is a highly accurate, self-training GHMM fungal gene predictor designed to work with assembled, aligned RNA-seq transcripts, which capitalises on the high quality of fungal transcript assemblies by incorporating predictions made directly from transcript sequences.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > Whole-genome sequencing has enabled investigations into the gene content of living many organisms and forms the foundation for further study of gene expression, proteomics and epigenetics. After assembly of a novel genome, gene annotation is often the first step in analysing the gene content of an organism. Accurate annotation of the exonic structure of genes is crucial to the success of all subsequent functional and comparative analyses.
    > Problems that can potentially be caused by incorrect gene annotation are numerous and can lead to incorrect assessments of the lifestyle and ecology of an organism. In comparative genomics where orthologous genes or conserved functional domains are compared between species/isolates, the estimated numbers of such genes/ domains can be distorted by less than perfect annotations (as described by Hane et al. [1], S Text 1). Prediction of extracellular secretion, which can be determined by a short signal peptide at the N-terminus, can miss secreted proteins if the start codon of a gene has been incorrectly annotated. Mis-annotating the start of protein translation could either cut off the signal peptide or bury it within the annotation. While a seemingly benign annotation error, the consequences for downstream research could be detrimental, particularly as the biotic interactions or industrial applications of microbes are largely determined by their secretomes. Additionally, translated protein sequences of novel species are often submitted to databases such as NCBI [2] and Uniprot [3]. It is commonplace to use these database entries to support the annotation of related species or isolates, meaning errors present in the pioneer annotation may be repeated. When these new annotations based on false assumptions are added to databases, there is not only a propagation of errors, but also a perceived strengthening of homology evidence for incorrect protein sequences.
    > In recent years, correction of in silico predicted gene annotations with RNA-seq derived transcripts and read alignments has enabled vastly improved genome annotations and corrections of annotated gene structures [4][5][6].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
4. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
5. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
6. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
7. A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al. (2023). Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea. Frontiers in Microbiology. https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
8. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
9. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
10. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2018). The y-ome defines the thirty-four percent of Escherichia coli genes that lack experimental evidence of function. bioRxiv. https://www.semanticscholar.org/paper/b55c92ec2394bb9ebdff9d019f9afb7238e5c8ba
11. N. Udeshi, Kayvon Pedram, Tanya Svinkina, Shaunt Fereshetian, S. Myers et al. (2017). Antibodies to biotin enable large-scale detection of biotinylation sites on proteins. Nature methods. https://www.semanticscholar.org/paper/f9e4f461ca61f4399a95875ea96fb075fa959901
12. Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al. (2018). Ten steps to get started in Genome Assembly and Annotation. F1000Research. https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
13. Humaira Saeed, Sudhaker Padmesh, Aditi Singh, S. Singh, Mohammed Haris Siddiqui et al. (2025). Characterization of holins, the membrane proteins of coliphage ASEC2201: a genomewide in silico approach. Frontiers in Microbiology. https://www.semanticscholar.org/paper/a39392e12bf3bda67bdfe600053e8403deb3b887
14. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
15. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
16. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
17. Yoji Nakamura (2018). Prediction of Horizontally and Widely Transferred Genes in Prokaryotes. Evolutionary Bioinformatics Online. https://www.semanticscholar.org/paper/af7bde229b96609907924d1c68ea463af656efb2
18. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
19. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
20. Alison C. Testa, James K. Hane, S. Ellwood, R. Oliver (2015). CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts. BMC Genomics. https://www.semanticscholar.org/paper/06704917bf44cd62eef0bb5cb944b97484056e21