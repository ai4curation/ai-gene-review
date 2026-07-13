---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T17:02:26.884991'
end_time: '2026-07-07T17:02:33.339161'
duration_seconds: 6.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: amgK
  gene_symbol: amgK
  uniprot_accession: Q88QT3
  protein_description: 'RecName: Full=N-acetylmuramate/N-acetylglucosamine kinase
    {ECO:0000305|PubMed:23831760}; Short=MurNAc/GlcNAc kinase {ECO:0000305|PubMed:23831760};
    EC=2.7.1.221 {ECO:0000269|PubMed:23831760}; AltName: Full=Anomeric sugar kinase
    {ECO:0000303|PubMed:23831760};'
  gene_info: Name=amgK {ECO:0000303|PubMed:23831760}; OrderedLocusNames=PP_0405 {ECO:0000312|EMBL:AAN66035.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the kinase AmgK family. .
  protein_domains: Aminoglycoside_PTrfase. (IPR002575); Kinase-like_dom_sf. (IPR011009);
    APH (PF01636)
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
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88QT3
- **Protein Description:** RecName: Full=N-acetylmuramate/N-acetylglucosamine kinase {ECO:0000305|PubMed:23831760}; Short=MurNAc/GlcNAc kinase {ECO:0000305|PubMed:23831760}; EC=2.7.1.221 {ECO:0000269|PubMed:23831760}; AltName: Full=Anomeric sugar kinase {ECO:0000303|PubMed:23831760};
- **Gene Information:** Name=amgK {ECO:0000303|PubMed:23831760}; OrderedLocusNames=PP_0405 {ECO:0000312|EMBL:AAN66035.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the kinase AmgK family. .
- **Key Domains:** Aminoglycoside_PTrfase. (IPR002575); Kinase-like_dom_sf. (IPR011009); APH (PF01636)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "amgK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'amgK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **amgK** (gene ID: amgK, UniProt: Q88QT3) in PSEPK.

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

- Papers retrieved: 18
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
  - Snippet 1 (score: 0.738)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [2] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
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
  - Snippet 1 (score: 0.718)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

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
  - Snippet 1 (score: 0.716)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [4] Centrality of drug targets in protein networks
- Authors: A. Follis
- Year: 2021
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/042dee46e3d0a0e64c02b21e1fb9e97e7bc403d8
- DOI: 10.1186/s12859-021-04342-x
- PMID: 34715787
- PMCID: 8555226
- Citations: 20
- Influential citations: 1
- Summary: These findings expand on previous reports of drug targets’ network centrality by suggesting some centrality metrics such as low topological coefficient as inherent characteristics of a ‘good’ target, relative to other exploratory targets and regardless of its functional class.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > org/) with the ChEMBL and Uniprot identifiers further retrieved the corresponding String identifiers. The functional classification of targets based on Gene Ontology [33] (GO) terms was performed using the StringDB GO-terms analysis tool applied to 'molecular function' annotations, pooling proteins by the following logical combinations of identifiers: channel or transporter (class 'channels and transporters); enzyme not kinase (class 'enzymes'); GPCR or G-protein coupled receptor (class 'GPCRs'); kinase (class 'kinases'); nuclear receptor (class 'nuclear receptors'). The complete set of GO annotations for the Uniprot reference human proteome (goa file) was downloaded from the Gene Ontology Consortium web page (http:// curre nt. geneo ntolo gy. org/ produ cts/ pages/ downl oads. html) The number of citations for each target protein was retrieved from automated Pub-Med searches (https:// pubmed. ncbi. nlm. nih. gov) using the proteins gene abbreviation as search term applying the filters: 'human' , 'journal article' and 'title-abstract' . Search automation was implemented using a Knime [49] 'GET Request' node workflow. Disease association annotations were downloaded from the DisGeNet web page (curated gene-disease associations) (https:// www. disge net. org/ downl oads#) and Genetic Association Database web page (https:// genet icass ociat iondb. nih. gov/).

### [5] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.708)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [6] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.707)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [7] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.707)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [8] HomoKinase: A Curated Database of Human Protein Kinases
- Authors: S. Subramani, Saranya Jayapalan, R. Kalpana, J. Natarajan
- Year: 2013
- Venue: International Scholarly Research Notices
- URL: https://www.semanticscholar.org/paper/81a21403fc772c6b9c00915e1124fad2cfb1894b
- DOI: 10.1155/2013/417634
- Citations: 18
- Summary: The present version of theomoKinase database contains 498 curated human protein kinases and links to other popular databases.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > The HGNC approved human genes, which satisfy all these three GO criteria, were classified as human protein kinases and used to build the database.
    > The predicted list of protein kinases were further divided into groups, families, subfamilies, and domains. The group classifications were done using the PhosphoSite database [13], whereas the superfamily, family, subfamily, and domain level classifications were retrieved from UniProt [14]. In addition, various biological information such as official symbol, full name, biological IDs, other known aliases, amino acid sequences, functional domain, gene ontology, pathway assignments, and drug compounds were extracted from various biological databases such as (i) NCBI, (ii) UniProt, (iii) Amigo Go, (iv) KEGG, and (v) DrugBank. Figure 2 depicts a schematic summary of the HomoKinase data warehouse creation process.
    > The curated human protein kinase names and their related information retrieved from other databases were used to develop the HomoKinase database. The HomoKinase database is implemented as client/server architecture with easy-to-use web interface. The server is made of MySQL database, and the web client and programs for the human protein kinase retrieval, annotation, and query interface were designed using PHP programming language. Entrez Gene stores information on 1,93,709 genes specific to Homo sapiens (as on October 2012). We retrieved 33,489 human genes/proteins specific to our query term "(Homo sapiens [Organism] AND HGNC). " On further comparison with HGNC database, only the 19,026 genes have official HGNC gene symbol, and the remaining were 8399 pseudogenes, 4230 noncoding RNAs, 707 phenotype, and 1127 other genes.
    > The 19,032 HGNC approved human genes were further classified into protein kinases by checking the presence of three GO annotation terms (i) ATP binding property, (ii) kinase activity, and (iii) protein phosphorylation property. The HGNC approved genes fulfilling the above three GO properties (e.g., CDK1, MARK1) were classified as protein kinases and included in the database.
  - Snippet 2 (score: 0.676)
    > The HomoKinase database creation involves several steps. First, human genes with their known aliases were downloaded from Entrez Gene (http://www.ncbi.nlm.nih.gov/ gene) using the query term "(Homo sapiens [Organism]) AND HGNC. " Next, the retrieved gene list was crosschecked with the HUGO Gene Nomenclature Committee (HGNC) (http://www.genenames.org/) database to include only the genes with HGNC approved gene name for building the database [7]. The other genes in the list such as pseudogenes, noncoding RNAs, and phenotype which have no HGNC approved name were eliminated.
    > Finally, gene ontology based refinement was performed to classify the protein kinase genes from the HGNC approved list of human protein-coding genes. In general, GO is mainly focused on three significant ontology terms such as molecular function, cellular component, and biological process. A single gene product may be annotated to multiple GO terms, detailing a range of functional attributes, using both manual and electronic annotation methods [8,9]. The conserved protein kinase core consists of two lobes: a smaller Nterminal lobe (N-lobe) with ATP binding site and a larger C-terminal lobe (C-lobe) with catalytic site responsible for kinase activity [3,10]. In addition, the biological processes correspond to protein phosphorylation. These three unique terms of gene ontology (GO) provide precise information about the annotated gene, gene products, and other terms which in turn provide a deep insight about kinases to the researchers. So, we classify the HGNC approved human genes which confirms these three GO terms: (i) ATP binding, (ii) kinase activity, and (iii) protein phosphorylation as true protein kinases. Gene ontology search was performed using two web tools, namely, Quick Go [11] and Amigo Go [12] with automated PHP scripts. The HGNC approved human genes, which satisfy all these three GO criteria, were classified as human protein kinases and used to build the database.

### [9] KinaseFusionDB: an integrative knowledge of kinase fusion proteins in multi-scales
- Authors: H. Kumar, Zikang Chen, Abayomi Adegunlehin, Loren Trowbridge, Leonardo Aguilar et al.
- Year: 2025
- Venue: Briefings in Bioinformatics
- URL: https://www.semanticscholar.org/paper/d212d0a2c8e4a7cedcd2c1e4fa11ed6de23345f7
- DOI: 10.1093/bib/bbaf259
- PMID: 40471992
- PMCID: 12140011
- Summary: A novel in silico pipeline for predicting 3D structures of kinase fusion proteins and performing structure-based virtual screening, which revealed that most predicted structures showed high pLDDT scores (pLDDT >70) within conserved kinase domains.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > To assign the functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases, and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', Figure 1. Overview of KinaseFusionDB and its role in understanding kinase fusion proteins. (a) I. The top section identifies therapeutic targets for oncogenic activation of kinases, including wild-type kinases activated by overexpression or genomic amplification, mutated kinases with gain-offunction mutations, and kinase fusion proteins resulting from chromosomal rearrangements. II. The middle section highlights the functionalities of KinaseFusionDB, such as providing functional annotations, mRNA/protein expression data, drug binding information, and relevant literature reviews. III. The third section addresses the current limitations in targeting kinase fusion proteins, particularly the lack of comprehensive 3D structures for these proteins. It emphasizes the partial knowledge of kinase fusion protein structures and the need for further drug screening. IV. The bottom section discusses how computational approaches, such as predicted 3D structures (e.g. from AlphaFold2), can fill these gaps, supporting drug screening and filtering based on consistent binding among multiple fusion protein isoforms. (b) Kinase domain-retained human kinase fusion proteins.
    > 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane', and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt [26] accessions from UniProt for 10 619 genes involved in 15 030 fusion genes [27]. UniProt provides the loci information of 39 protein features, including 6 molecule processing features, 13 region features, 4 site features, 6 amino acid modification features, 2 natural variation features, 5 experimental info features, and 3 secondary structure features.
  - Snippet 2 (score: 0.650)
    > KinaseFusionDB provides five functional annotations of 7680 kinase fusion genes and 23 functional annotations of ∼1399 kinase fusion proteins across 17 categories with user-friendly visualization. The main features of KinaseFusionDB annotation categories are summarized below.
    > i) The 'Kinase fusion gene summary' category shows a basic fusion gene summary following multiple annotations for each fusion partner gene. It provides an overview of the fusion gene with detailed annotations for each fusion partner, including gene symbol, chromosomal location, and UniProt [28]Accession IDs. It uses the University of California, Santa Cruz (UCSC) genome browser [47] to show the most frequently reported breakpoint information and all known breakpoints of individual partners in the gene structures. ii) The 'Kinase fusion gene sample information' category shows the sample or cell list that expressed the kinase fusion gene. It integrates data from multiple resources, such as the COSMIC and CCLE databases, displaying breakpoints for each kinase fusion partner gene with corresponding genomic coordinates. iii) The 'Kinase fusion ORF analysis' category provides the inframe fusion gene information after ORF annotation, such as gene isoform IDs, breakpoints, fusion mRNA sequence length, and fusion protein sequence length. iv) The 'Kinase fusion amino acid sequences' category provides the fusion amino acid sequences of all fusion isoforms. v) The 'Multiple sequence alignment of all fusion protein isoforms' category provides the multiple sequence alignment among all predicted fusion protein isoform sequences using CLUSTAL 2.1 [34]. This alignment helps compare the sequence similarity and identify conserved regions across all fusion isoforms. vi) The 'Kinase fusion protein functional features' category provides the retention information of 39 protein features due to the formation of fusion proteins with a link to an in-house visualization web tool for functional features of fusion genes, FGviewer [48]. This tool allows users to explore functional impacts at the DNA, mRNA, protein, and pathogenic levels. vii) The 'Kinase Fusion Protein Structures' category offers predicted 3D structures of kinase fusion proteins, available in PDB and CIF formats, with embedded Mol * visualization directly on the webpage for interactive exploration [49].

### [10] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.686)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [11] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.683)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [12] Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser
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
  - Snippet 1 (score: 0.676)
    > Gene nomenclature contains current official symbols and various numbers of synonyms, which pose a challenge to integrating genomic data and increase the probability that different genes share the same symbol. Therefore, we retrieved identifiers assigned to all protein-coding genes in human, mouse, rat and pig genomes that are available in the Ensembl genome browser (release 113) to assess the number of genes, compare species and identify ambiguous symbols. Results: Our analysis revealed that the total number of symbols, both official symbols and synonyms, used to identify protein-coding genes ranges from 16,600 in pigs to 64,580 in mice. Furthermore, the gene nomenclature is not complete because there are also genes without an assigned symbol, which indicates gaps in understanding protein-coding genes, especially in pigs. We also found a large number of gene symbols that map to more than one gene. These symbols might complicate the identification of about 10% of rat and mouse genes and 18% of human protein-coding genes. A simple solution for this problem is the usage of stable gene IDs assigned by scientific institutions and committees (Ensembl, NCBI, RGD, HGNC and VGNC) provided that the genomic information associated with these IDs is retrieved directly from proprietary databases containing the most accurate data. Finally, although gene symbols may pose a problem with unequivocal identification of genes, there are instances when no other identifiers are available in the literature. Therefore, we have developed an R script performing search of the Ensembl database and integrating data to provide a single list of updated symbols with annotation about their ambiguity. Conclusions: Gene symbols are not always reliable and should be reported together with stable IDs to enable unequivocal identification of genes. Therefore, data containing only gene symbols should be used cautiously to avoid misidentification of genes. A solution for this problem is our R script REgeness that performs a gene symbol update to current official versions combined with identification of ambiguous symbols and retrieval of other IDs from the Ensembl database.

### [13] Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms
- Authors: Xiao Yang, Shyamasree Saha, Aravind Venkatesan, Santosh Tirunagari, Vid Vartak et al.
- Year: 2023
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
- DOI: 10.1101/2023.02.20.529292
- PMID: 37857688
- PMCID: 10587067
- Citations: 13
- Influential citations: 1
- Summary: A human-annotated full-text corpus for biomedical entities, comprising 300 full-text open-access research articles, is developed, describing the corpus and details how to access and reuse this open community resource.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > Examples are for illustrative purposes only and specific to each case, hence not all the entities are shown and highlighted. RED: Gene/Protein BLUE: Disease GREEN: Organism a. Biomedical concepts Gene/Protein: Annotations could be specific gene/protein names or classes/family names of gene/proteins. In particular, very broad concepts like "protein", "gene", "enzyme", "receptors", "kinase", "cytokine", "transcription regulators/factors" are out of the scope of annotations. However, family/subtype names of those concepts are considered for the annotations, such as "amylolytic enzyme", "antioxidant enzyme", "map kinase p38", because these terms narrow the concepts to specific families of gene/protein, enzyme.
    > Annotators can refer to Uniprot and Protein Ontology.

### [14] An Asymmetrically Balanced Organization of Kinases versus Phosphatases across Eukaryotes Determines Their Distinct Impacts
- Authors: Ilan Y. Smoly, N. Shemesh, Michal Ziv-Ukelson, Anat Ben-Zvi, Esti Yeger Lotem
- Year: 2017
- Venue: PLoS Computational Biology
- URL: https://www.semanticscholar.org/paper/4f13e00bf92fc0e75e910dd6a62d87286a816e6b
- DOI: 10.1371/journal.pcbi.1005221
- PMID: 28135269
- PMCID: 5279721
- Citations: 40
- Summary: Protein phosphorylation underlies cellular response pathways across eukaryotes and is governed by the opposing actions of phosphorylating kinases and de-phosphorylating phosphatases. While kinases and phosphatases have been extensively studied, their organization and the mechanisms by which they balance each other are not well understood. To address these questions we performed quantitative analyses of large-scale 'omics' datasets from yeast, fly, plant, mouse and human. We uncovered an asymm...
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > The annotations of genes to different molecular functions were obtained from the Gene Ontology (GO) Database [38]. We chose to work with GO annotations since they were in good agreement with other sources and provided a consistent framework across the different organisms. Kinases and phosphatases were defined as genes with molecular function annotation of 'protein kinase activity' (GO:0004672) or 'phosphoprotein phosphatase activity' (GO:0004721), respectively. Regulators of histone acetylation were defined as genes with 'histone acetyltransferase activity' (GO:0004402) or 'histone deacetylase activity' (GO:0004407) annotations. Regulators of protein ubiquitination were defined as genes with "ubiquitin-protein transferase activity" (GO:0004842) or "thiol-dependent ubiquitin-specific protease activity" (GO:0004843) annotations. For H. sapiens we considered only genes that were reviewed by UniProt database [39]. For A. thaliana we considered only genes with annotated TAIR accessions [40]. For D. melanogaster we considered only genes with annotated FlyBase accessions [41]. For M. musculus we considered only genes with annotated MGI accessions [42]. For C. elegans we considered all kinases and phosphatases annotated with multivulva or vulvaless phenotype according to WormBase [30]. To validate the trends we observed, we also analyzed curated kinases and phosphatases extracted from organism-specific databases, which showed similar results (S6 Fig).

### [15] Synthesis, characterization, and computational evaluation of some synthesized xanthone derivatives: focus on kinase target network and biomedical properties
- Authors: Wisam Taher Muslim, L. J. Mohammad, Munaf M. Naji, Isaac Karimi, Matheel D. Al-Sabti et al.
- Year: 2025
- Venue: Frontiers in Pharmacology
- URL: https://www.semanticscholar.org/paper/659ab502877a1d6b5ab7ce45fa51f0f9a13dcf24
- DOI: 10.3389/fphar.2024.1511627
- PMID: 39830340
- PMCID: 11738930
- Summary: Acute leukemic T-cells were one of the top predicted tumor cell lines for these ligands and the possible antileukemic effects of synthesized xanthone derivatives are potentially very interesting and warrant further studies.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > The UniProt accession identification of target kinases was converted to gene symbols for humans using the SynGO gene set analysis tool (Koopmans et al., 2019), and pooled together, and submitted to GeneMANIA to construct target kinase network. GeneMANIA is a handy web interface for acquiring gene ontology, scrutinizing gene lists, and highlighting genes for functional assays (Warde-Farley et al., 2010). After choosing Homo sapiens from the list of optional organisms, the genes of interest in the previous step were entered into the search bar and the results were collated and high-scored genes were culled for further discussion. Moreover, the protein-protein network was also constructed in STRING ver. 12 launched at https://string-db.org, and submitted to Cytoscape ver. 3.10.2 for network analysis using a novel Cytoscape plugin cytoHubba and visualization (Shannon et al. , 2003).

### [16] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.658)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [17] A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi
- Authors: R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al.
- Year: 2014
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
- DOI: 10.1186/1471-2164-15-316
- PMID: 24773765
- PMCID: 4234515
- Citations: 41
- Summary: This sequencing effort has produced the first set of whole-genome sequencing data on any ctenophore species and is amongst the first wave of projects to sequence an animal genome de novo solely using next-generation sequencing technologies.
- Evidence snippets:
  - Snippet 1 (score: 0.657)
    > In an effort to engage the collective expertise of the scientific community, we have implemented a collaborative wiki (MediaWiki version 1.19.11) for the Mnemiopsis gene complement. The Mnemiopsis Gene Wiki is accessible from the left sidebar of most pages and is searchable either by selecting a Mnemiopsis gene identifier (e.g., ML00011a) from the drop-down menu or by manually entering an identifier in the appropriate search box. Users can also access these pages by clicking on a gene in the 2.2 track of the genome browser. Each record in the Gene Wiki represents a single Mnemiopsis gene and provides the following annotation: nucleotide and protein sequences, coding exonic genomic coordinates, pre-computed BLAST hits from numerous organisms displaying the top hits for each protein, the top non-self BLAST hit to Mnemiopsis, Pfam-A domains, Gene Ontology (GO) functional annotations, human disease genes from Online Mendelian Inheritance in Man (OMIM), and a table of ortholog clusters formed by phylogenetically informed clustering methods [4] (Figure 5). In addition, controlled editable sections have been included that permit (and encourage) the scientific community to provide further gene annotation for isoforms, in situ images, references, and other notes for each gene. Users interested in supplementing our gene model annotation at the Mnemiopsis Gene Wiki pages must first create an account and log in prior to submitting their contributions. In-house subject matter expert data curators are notified by e-mail following the creation of a new user account or an edit to an existing Gene Wiki record. Any content changes or additions to the Gene Wiki are thoroughly evaluated by these data curators and are made public subject to their approval.
    > Pre-compiled BLAST hits are enumerated in tabular form. Each Mnemiopsis protein was compared to the UniProt and NCBI non-redundant protein databases (nr) using BLASTP. The results display the hit number, the accession numbers, E-values, and brief descriptions of the top four hits (lowest E-values). Accession numbers are linked to relevant corresponding entries at UniProt and GenBank.

### [18] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.655)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. A. Follis (2021). Centrality of drug targets in protein networks. BMC Bioinformatics. https://www.semanticscholar.org/paper/042dee46e3d0a0e64c02b21e1fb9e97e7bc403d8
5. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
6. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
7. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
8. S. Subramani, Saranya Jayapalan, R. Kalpana, J. Natarajan (2013). HomoKinase: A Curated Database of Human Protein Kinases. International Scholarly Research Notices. https://www.semanticscholar.org/paper/81a21403fc772c6b9c00915e1124fad2cfb1894b
9. H. Kumar, Zikang Chen, Abayomi Adegunlehin, Loren Trowbridge, Leonardo Aguilar et al. (2025). KinaseFusionDB: an integrative knowledge of kinase fusion proteins in multi-scales. Briefings in Bioinformatics. https://www.semanticscholar.org/paper/d212d0a2c8e4a7cedcd2c1e4fa11ed6de23345f7
10. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
11. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
12. Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała (2025). Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser. BMC Genomics. https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
13. Xiao Yang, Shyamasree Saha, Aravind Venkatesan, Santosh Tirunagari, Vid Vartak et al. (2023). Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms. Scientific Data. https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
14. Ilan Y. Smoly, N. Shemesh, Michal Ziv-Ukelson, Anat Ben-Zvi, Esti Yeger Lotem (2017). An Asymmetrically Balanced Organization of Kinases versus Phosphatases across Eukaryotes Determines Their Distinct Impacts. PLoS Computational Biology. https://www.semanticscholar.org/paper/4f13e00bf92fc0e75e910dd6a62d87286a816e6b
15. Wisam Taher Muslim, L. J. Mohammad, Munaf M. Naji, Isaac Karimi, Matheel D. Al-Sabti et al. (2025). Synthesis, characterization, and computational evaluation of some synthesized xanthone derivatives: focus on kinase target network and biomedical properties. Frontiers in Pharmacology. https://www.semanticscholar.org/paper/659ab502877a1d6b5ab7ce45fa51f0f9a13dcf24
16. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
17. R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al. (2014). A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi. BMC Genomics. https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
18. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508