---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-10-18T18:01:55.925490'
end_time: '2026-10-18T18:02:00.901460'
duration_seconds: 4.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CDK5RAP1
  gene_symbol: CDK5RAP1
  uniprot_accession: Q96SZ6
  protein_description: 'RecName: Full=Mitochondrial tRNA methylthiotransferase CDK5RAP1
    {ECO:0000303|PubMed:22422838, ECO:0000303|PubMed:25738458}; EC=2.8.4.3 {ECO:0000269|PubMed:22422838,
    ECO:0000269|PubMed:25738458}; AltName: Full=CDK5 activator-binding protein C42;
    AltName: Full=CDK5 regulatory subunit-associated protein 1; AltName: Full=mt-tRNA-2-methylthio-N6-dimethylallyladenosine
    synthase; AltName: Full=mt-tRNA-N6-(dimethylallyl)adenosine(37) methylthiotransferase;
    Flags: Precursor;'
  gene_info: Name=CDK5RAP1 {ECO:0000312|HGNC:HGNC:15880}; Synonyms=C20orf34; ORFNames=CGI-05,
    HSPC167;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the methylthiotransferase family. MiaB
  protein_domains: Elp3/MiaA/NifB-like_rSAM. (IPR006638); Methylthiotransferase. (IPR005839);
    Methylthiotransferase_CS. (IPR020612); Methylthiotransferase_N. (IPR013848); Methylthiotransferase_N_sf.
    (IPR038135)
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
- **UniProt Accession:** Q96SZ6
- **Protein Description:** RecName: Full=Mitochondrial tRNA methylthiotransferase CDK5RAP1 {ECO:0000303|PubMed:22422838, ECO:0000303|PubMed:25738458}; EC=2.8.4.3 {ECO:0000269|PubMed:22422838, ECO:0000269|PubMed:25738458}; AltName: Full=CDK5 activator-binding protein C42; AltName: Full=CDK5 regulatory subunit-associated protein 1; AltName: Full=mt-tRNA-2-methylthio-N6-dimethylallyladenosine synthase; AltName: Full=mt-tRNA-N6-(dimethylallyl)adenosine(37) methylthiotransferase; Flags: Precursor;
- **Gene Information:** Name=CDK5RAP1 {ECO:0000312|HGNC:HGNC:15880}; Synonyms=C20orf34; ORFNames=CGI-05, HSPC167;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the methylthiotransferase family. MiaB
- **Key Domains:** Elp3/MiaA/NifB-like_rSAM. (IPR006638); Methylthiotransferase. (IPR005839); Methylthiotransferase_CS. (IPR020612); Methylthiotransferase_N. (IPR013848); Methylthiotransferase_N_sf. (IPR038135)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CDK5RAP1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CDK5RAP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CDK5RAP1** (gene ID: CDK5RAP1, UniProt: Q96SZ6) in human.

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
- Citations: 93
- Influential citations: 2
- Summary: The initial release of the LIPID MAPS Proteome Database contains 2959 records, representing human and mouse proteins involved in lipid metabolism, and this LMPD protein list was enhanced with annotations from UniProt, EntrezGene, ENZYME, GO, KEGG and other public resources.
- Evidence snippets:
  - Snippet 1 (score: 0.798)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [2] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
- Authors: Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al.
- Year: 2021
- Venue: mSystems
- URL: https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
- DOI: 10.1128/mSystems.00673-21
- PMID: 34726489
- PMCID: 8562490
- Citations: 17
- Summary: This work systematically updates the functional genome annotation of Mycobacterium tuberculosis virulent type strain H37Rv and identifies hundreds of high-confidence candidates for mechanisms of antibiotic resistance, virulence factors, and basic metabolism and other functions key in clinical and basic tuberculosis research.
- Evidence snippets:
  - Snippet 1 (score: 0.787)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [3] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
- Authors: Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöery, R. Kuo et al.
- Year: 2020
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
- DOI: 10.1186/s12859-020-03764-3
- PMID: 33176685
- PMCID: 7661159
- Citations: 6
- Summary: The Avian Immunome DB (Avimm) for easy gene property extraction as exemplified by avian immune genes is presented and described, which contains 1170 distinct avian immune genes with canonical gene symbols and 612 synonyms across 363 bird species.
- Evidence snippets:
  - Snippet 1 (score: 0.756)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] Protocol for identifying and comparing molecular prognosis subtypes of IgAN using R
- Authors: Juan Wang, Yi Liu, Xi-Zhao Chen, Mansheng Li, Yunping Zhu
- Year: 2024
- Venue: STAR Protocols
- URL: https://www.semanticscholar.org/paper/6794ab2424155d4a65b28cd139731c21d4d37aa2
- DOI: 10.1016/j.xpro.2024.103138
- PMID: 38878284
- PMCID: 11234001
- Summary: A general workflow for identifying and comparing molecular subtypes of disease using proteomics data using R software is presented and steps for data preprocessing, feature selection, determination of subtypes, and functional interpretation of subtypes are described.
- Evidence snippets:
  - Snippet 1 (score: 0.749)
    > The UniProt database (https://www.uniprot.org/) can perform ID mapping on the UniProt ID of each protein to obtain corresponding annotation information, including Entry name, Protein name, Gene name, Organism, and Length.
    > Note: Considering the efficiency and readability of subsequent analysis, users need to convert the ID in the raw data. In this protocol, we choose to convert UniProt ID to Gene Symbol, and when multiple UniProt ID correspond to one Gene Symbol, we can use the make.unique() function to add a serial number to Gene Symbol to make it unique.
    > 7. Group samples by type.

### [5] A high-quality bread wheat genome unravels the adaptive evolution of wheat end-use quality
- Authors: Xin-You Cao, Ji-Jin Zhang, Ya-Fei Guo, Yuhong Huang, Lei Guo et al.
- Year: 2026
- Venue: Nature Plants
- URL: https://www.semanticscholar.org/paper/2e5e60b07b1b58e9b8258a63c57887e951fba19d
- DOI: 10.1038/s41477-026-02288-7
- PMID: 42098230
- Citations: 2
- Summary: A high-quality bread wheat genome reveals that prioritized selection on variable gluten genes and enhanced epistatic interactions drove the adaptive evolution of wheat end-use quality, offering a blueprint for future breeding.
- Evidence snippets:
  - Snippet 1 (score: 0.745)
    > EvidenceModeler (v2.1.0) 84 integrated the aforementioned prediction outcomes, while PASA software was used to predict variable cut annotations such as untranslated regions. All protein-coding genes were aligned to three integrated protein sequence databases: NR (https:// www.ncbi.nlm.nih.gov/protein/), SwissProt (https://ftp.uniprot.org/ pub/databases/uniprot/current_release/knowledgebase/complete/ uniprot_sprot.fasta.gz) and eggNOG (http://eggnog5.embl.de/#/app/ home). Protein domains were annotated by InterPro 85 , and the Gene Ontology 86,87 terms for each gene were obtained from the corresponding InterPro entry. The pathways in which the genes might be involved were assigned by BLAST (v.2.9.0) 88 against the KEGG databases (https:// www.genome.jp/kegg/brite.html). The protein-coding gene functional annotation results were merged from the above methods.
    > Noncoding RNAs were annotated using tRNAscan-SE (v.2.0) 89 for tRNAs and BLAST searches against the Rfam database for other noncoding RNAs. NLR gene signatures were identified using NLR-Annotator (v.2.0) 90 .

### [6] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, T. Lazar, P. Tompa, Bálint Mészáros, R. Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.740)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [7] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
- Authors: Xiaoqiong Bao, Qi Jiang, Wei-Xuan Chen, Hui-Qin Li, Xuan Li et al.
- Year: 2025
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
- DOI: 10.1093/nar/gkaf1206
- PMID: 41206768
- PMCID: 12807602
- Citations: 4
- Summary: The new RM2Target v2.0 will serve as a foundational resource for exploring RNA epitranscriptomic regulation, enabling investigations into cross-talk among modifications, underlying molecular mechanisms, and disease connections, thereby facilitating both basic research and translational applications in RNA epigenetics.
- Evidence snippets:
  - Snippet 1 (score: 0.736)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [8] AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes
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
  - Snippet 1 (score: 0.726)
    > As previously described (Triant et al. 2020), once a proteincoding gene annotation is complete, each new or modified isoform should be compared to a well-curated protein sequence database to check for congruency with known proteins. The sequence of an annotation is obtained by right clicking it and selecting Get Sequence. The first choice of database to search is the well-curated UniProtKB/Swissprot database using BLAST at either the UniProt (https:// www. unipr ot. org/ blast) or NCBI website (https:// blast. ncbi. nlm. nih. gov/ Blast. cgi) (Sayers et al. 2023a;UniProt Consortium 2023). If there is no match with a significant e-value (< 1e−05) in UniProtKB/Swissprot, the next database to try is the Model Organisms (landmark) database at NCBI. If that fails, select the RefSeq Proteins database and exclude your organism of interest from the search. Although RefSeq includes computationally predicted and hypothetical proteins, an alignment to a homologous protein from another organism provides support for the annotation. An alignment that covers the full length of both the annotated protein and the database protein sequence suggests the annotation is correct. An alignment that encompasses the full length of an annotated protein sequence but only part of a database protein suggests that the annotation is truncated. You may be able to correct the annotation with additional evidence, but if there is not sufficient evidence the issue can be noted in the Annotation Information Panel under the Comment tab. A partial alignment of an annotated protein to a database protein suggests the annotation has a reading frame shift or was extended incorrectly. Aligning the coding sequence (CDS) to the protein database will reveal whether the problem is due to a reading frame shift. Further annotation editing should be performed to correct the reading frame. If an incorrect extension was due to the merging of two genes, you should edit or redo the annotation. Any unresolved issues should be entered in the Comment section of the Annotation Information Panel.

### [9] Phase-separating fusion proteins drive cancer by upsetting transcription regulation
- Authors: Nazanin Farahi, T. Lazar, Peter Tompa, Bálint Mészáros, R. Pancsa
- Year: 2025
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/54d550a595352429b7ad7fdab681cd564170f566
- DOI: 10.1186/s13059-025-03787-0
- PMID: 41039633
- PMCID: 12492527
- Citations: 3
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and data shows that cancer-driving LLPS scaffolds tend to be potent oncogenes, giving rise to dominant phenotypes and lacking targeting options by current FDA-approved drugs.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations [55] in UniProt (GOA), UniProt annotations [61], the human transmembrane proteome (HTP) [130], MatrixDB [131], and MatrisomeDB [132]. We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2.
    > Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP) if it is assigned the "integral component of membrane (GO:0016021)" GO term in tier 1 GOA annotations, it is annotated as a TMP in HTP with a confidence score over 85, or it is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [10] MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila
- Authors: Jia-Cheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yu-Tao Wang et al.
- Year: 2025
- Venue: Synthetic and Systems Biotechnology
- URL: https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
- DOI: 10.1016/j.synbio.2025.04.001
- PMID: 40276250
- PMCID: 12018684
- Summary: Shifts in metabolic allocation in a glucoamylase hyperproduction strain of M. thermophila are identified, highlighting changes in fatty acid biosynthesis and amino acids biosynthesis pathways, which provide new insights into the underlying phenotypic alterations.
- Evidence snippets:
  - Snippet 1 (score: 0.721)
    > Single-gene search: Gene annotation is essential for biologists to understand a gene's function. MTD's single-gene search interface allows researchers to obtain a comprehensive gene description by entering or selecting a gene ID. The results include sequence information, CAZy family, Pfam domains, GO/KEGG annotations, and phenotype information (Fig. 2D), along with sequence-based predictions such as optimal protein activity temperature, melting temperature (Tm), subcellular localization, and transcription factor scores. To enhance data accessibility, links to external databases such as NCBI, KEGG, FungiDB [4], UniProt, and JGI are also provided, facilitating cross-referencing of gene annotations across various resources.
    > Unlike the static genome, the transcriptome captures dynamic gene expression changes in response to developmental or environmental conditions, establishing a dynamic link between an organism's genome and its physical characteristics [63]. In the single-gene retrieval interface, the expression of the searched gene is visualized in the form of box plots and scatter plots across transcriptome datasets (Fig. 2E). When hovering over any data point, users can view the corresponding experimental details, such as mutant name, sample processing methods, and growth conditions. This interactive feature reveals gene expression responses to environmental factors, allowing researchers to quickly identify experimental conditions of interest and explore the gene's potential roles in diverse biological contexts. Moreover, clicking on the dataset title will direct users to the GEO browser for further detailed descriptions. KEGG Pathway or Gene List Search: In transcriptome studies, researchers typically adopt a "bottom-up" approach: first sequencing all mRNA in a cell, identifying differentially expressed genes between conditions, and then performing GO/KEGG enrichment analysis to interpret functional distributions. MTD, however, offers a complementary "top-down" search strategy, enabling users to examine the expression of genes within a specific KEGG pathway (Fig. 3A) or a user-defined gene set. A unique feature of MTD is its manually curated data categorization system, which organizes sample data with detailed annotations based on experimental conditions.

### [11] VirProtRAG: Literature-grounded viral protein function annotation with retrieval-augmented generation
- Authors: Jiao-Jiao Guan, Jiayu Shang, Cheng Peng, Yan-Ni Sun
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/2f46f2b474600cdef3038432c50028f679298d36
- DOI: 10.64898/2026.07.03.736267
- Summary: VirProtRAG is a viral protein function annotation framework that integrates information retrieval with evidence-grounded knowledge generation and substantially improves recall and ranking of biologically relevant publications, helping ground LLM outputs in traceable literature evidence.
- Evidence snippets:
  - Snippet 1 (score: 0.717)
    > We downloaded all viral protein entries (taxonomy ID: 10239) from UniProtKB/Swiss-Prot. For each entry, we collected the following metadata fields: Entry ID, Protein Names, Gene Names, Gene names (primary), Gene names (synonym), Organism, and the corresponding Function [CC] annotation.
    > Each Function [CC] block consists of one or more free-text sentences, typically accompanied by bibliographic references and evidence codes that specify the provenance and reliability of each functional statement. These codes span a spectrum from direct experimental support (ECO:0000269), author-derived statements in literature without experimental validation (ECO:0000303), and curator inference based on scientific reasoning (ECO:0000305), to sequence-based functional propagation from a characterized homolog (ECO:0000250) or

### [12] MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data
- Authors: Anthony C. Smith, A. J. Robinson
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
  - Snippet 1 (score: 0.717)
    > Recorded for each protein of the mass spectrometry data sets were, where available, the original protein identifier, subcellular location, sequence of identified peptides, sequence coverage, and the experimental techniques that had been used for the purification, separation, and identification of the protein. If the original protein identifier could not be mapped to a UniProt primary accession number by PIR ID or MGI, then the protein was compared with proteins in UniProt by using BLASTP (14). If there was a significant match, then the UniProt primary accession number was assigned to the protein. Those proteins without a significant match were discarded. By using the PIR ID and the MGI identifier conversion tools, the evidence of mitochondrial localization for a protein was linked to many of the UniProt entries representing it. Identifiers of proteins encoded in the mitochondrial genome of organisms were taken from the Organelle database of the European Molecular Biology Laboratory-European Bioinformatics Institute and used to annotate the appropriate proteins in MitoMiner.
    > The source of protein sequences, related features, and annotation was UniProt (11). All UniProt entries were downloaded for the six species with mitochondrial localization data sets. The literature citations in each UniProt entry were retrieved from PubMed by using an InterMine parser. Additional Gene Ontology annotation on the biological process, metabolic function, and cellular component of each protein was taken from UniProt (15) and individual genome projects of M. musculus (12), Rattus norvegicus (16), Drosophila melanogaster (17), and Saccharomyces cerevisiae (18).
    > Finally lists of human genes and the descriptions of their associated disease phenotypes were taken from OMIM (19), the definitions of groups of homologous proteins were taken from HomoloGene (20), and data on the reactions, enzymes, and compounds of metabolic pathways were taken from KEGG (21). The EC numbers of proteins in UniProt were used to define the cross-reference between proteins and metabolic pathways.

### [13] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
- Authors: Christina M McCosker, E. Unal, Alayna K. Gigliotti, Wendy B. Puryear, Jonathan A. Runstadler et al.
- Year: 2025
- Venue: Molecular ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 4
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [14] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: Khairun Hisam Bin Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [15] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.707)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [16] An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models
- Authors: Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al.
- Year: 2026
- Venue: Nature Communications
- URL: https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
- DOI: 10.1038/s41467-026-75972-z
- PMID: 42669697
- PMCID: 13526818
- Summary: An embedding-based statistical framework is developed that transforms gene and function descriptions into vector representations, enabling statistical testing of gene-gene and gene-function relationships and quantitative prioritization of de novo functional hypotheses inferred by LLMs.
- Evidence snippets:
  - Snippet 1 (score: 0.707)
    > This study focused on human protein-coding genes because they represent the most well-annotated portion of the genome, with reliable functional summaries, and are typically the primary focus of functional annotation analyses. We obtained functional summaries of individual genes from three widely used databases: (1) NCBI Gene 32 , which curates descriptions from multiple sources such as RefSeq under the "Summary" field, (2) Alliance of Genome Resources 33 , where descriptions are generated from structured gene data such as ontology terms and ortholog sets under the "Automated Description" field, and (3) UniProt 34 , which focuses on protein-level functions under the "Function" field. The NCBI database was accessed using its API, Entrez Programming Utilities (E-utilities), while descriptions from Alliance of Genome Resources and UniProt were directly downloaded from their respective databases. The number of genes retrieved from each database was 18,753 from NCBI, 18,600 from Alliance of Genome Resources, and 16,343 from UniProt, with 16,329 genes shared across all three databases. We preprocessed the gene descriptions to remove irrelevant information, such as source attribution found in NCBI descriptions (e.g., "[provided by RefSeq, Jul 2008]"). After preprocessing, each gene name was combined with its corresponding functional summary and input into the embedding models to generate gene embeddings.
    > We also generated de novo gene descriptions using an RAG approach. For each gene, we first retrieved the 100 most relevant sentences from PubMed and PubMed Central via the LitSense 35 API using biological context-specific queries: "function of 'gene symbol'", "'gene symbol' pathway association", "'gene symbol' transcriptional response", "'gene symbol' disease association". The numbers of genes under each biological context were 18,723, 18,723, 18,288, and 18,548, respectively. To restrict the temporal scope of knowledge and ensure controlled evaluation, we filtered the retrieved sentences to retain only those from publications published in or before October 2023, consistent with the versions of curated gene databases used in this study.

### [17] CRONOS: the cross-reference navigation server
- Authors: B. Waegele, I. Dunger-Kaltenbach, G. Fobo, C. Montrone, H. Mewes et al.
- Year: 2008
- Venue: Bioinformatics
- URL: https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
- DOI: 10.1093/bioinformatics/btn590
- PMID: 19010804
- PMCID: 2638938
- Citations: 20
- Summary: CRONOS, a cross-reference server that contains entries from five mammalian organisms presented by major gene and protein information resources, is developed, which shows that the cross-references are highly accurate.
- Evidence snippets:
  - Snippet 1 (score: 0.706)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [18] Antibodies to biotin enable large-scale detection of biotinylation sites on proteins
- Authors: Namrata D. Udeshi, Kayvon Pedram, Tanya Svinkina, Shaunt Fereshetian, S. Myers et al.
- Year: 2017
- Venue: Nature methods
- URL: https://www.semanticscholar.org/paper/f9e4f461ca61f4399a95875ea96fb075fa959901
- DOI: 10.1038/nmeth.4465
- PMID: 29039416
- PMCID: 8954634
- Citations: 128
- Influential citations: 3
- Summary: It is shown that anti-biotin antibodies enable unprecedented enrichment of biotinylated peptides from complex peptide mixtures.
- Evidence snippets:
  - Snippet 1 (score: 0.701)
    > All human IDs used for data annotation were downloaded from Uniprot 20 FTP (URL: ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledge-base/ idmapping/by_organism/, Version: 10/03/2016). The resulting data provided 133,996 unique identifications, which were in turn used to query the Uniprot database. This search returned HHMI Author Manuscript HHMI Author Manuscript HHMI Author Manuscript 109,961 records (including reviewed and unreviewed) along with their functional and structural annotations, including gene ontology features. The annotation table was used to search for mitochondrial evidence associated with a given Uniprot identification in our proximity-labeling anti-biotin-enriched data set by using a string match algorithm. A given protein was annotated as having mitochondrial evidence if any of the following were true: (i) the string 'mitoch' matched the above UniProt annotation table when queried by either gene name or accession number. (ii) The protein showed mitochondrial evidence from a list of mitochondrial proteins which was the same as our previous study (Rhee et al. 11 ) and a precursor to MitoCarta2.0 catalog 28 . (iii) The protein was present in the original mitochondrial true positive list used Rhee et al. 11 . Thebiotinylated peptide data were filtered such that reverse hits, nonhuman contaminants, nonfully localized biotinylation sites, sites identified in the SILAC light state, and redundant biotin site entries were removed. From this list, transmembrane proteins were annotated using the following criteria: (i) the UniProt transmembrane annotation contains the string "TRANSMEM" when matched by either gene name or accession number and/or (ii) evidence from of transmembrane domains after running the precursor MitoCarta2.0 catalog through TMHMM 29 . The UniProt topological domain annotation contained the string "TOPO" when matched by either gene name or accession number.

### [19] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
- Authors: P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al.
- Year: 2025
- Venue: Animals : an Open Access Journal from MDPI
- URL: https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
- DOI: 10.3390/ani15040484
- PMID: 40002966
- PMCID: 11852025
- Citations: 3
- Summary: Differences in surface proteins between X- and Y-chromosome-bearing bovine spermatozoa are explored to identify potential targets for sperm sexing by LC-MS/MS analysis, with 5 transmembrane proteins showing promise as markers for X-sperm.
- Evidence snippets:
  - Snippet 1 (score: 0.700)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [20] A high-quality chromosome-level genome assembly of the Chinese medaka Oryzias sinensis
- Authors: Zhongdian Dong, Jiangman Wang, Guo-Zhu Chen, Yusong Guo, Na Zhao et al.
- Year: 2024
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/22e6bac57aff18bdef6ecc2240c145ad3758b9ee
- DOI: 10.1038/s41597-024-03173-8
- PMID: 38548787
- PMCID: 10978949
- Citations: 6
- Summary: A high-quality chromosome-level genome assembly of O. sinensis is generated using single-tube long fragment read (stLFR) reads, Nanopore long-reads, and Hi-C sequencing data and ATAC-seq is used to uncover chromosome transposase-accessibility as well as related genome area function enrichment for Oryzias sinensis.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > From inner to outer circles: Density of genes with 500 kbp windows, ranging from 0 to 50; Density of TE with 500 kbp windows, ranging from 0 to 600; Density of TRF with 500 kbp windows, ranging from 0 to 450; Distributions of GC content with 500 kbp windows. (B) Hi-C interaction heat map and scatter plot of genome assembly GC content and sequencing depth.
    > Trinity, before PASA was used to get a gene model. Finally, all evidence was merged to form a consensus gene structure annotation result using GLEAN 30 . A total of 22,461 protein-coding genes were successfully predicted. BUSCO 19 assessments reached 94.6% using the actinopterygii_odb9 database, indicating relatively complete gene annotation coverage (Table 3).
    > All predicted genes were compared with public biological function databases including KEGG 31 , Swissprot 32 , and TrEMBL 33 (https://www.uniprot.org/statistics/TrEMBL) using BLASTp 34 with an E-value cutoff of 1e-5 for functional annotation. Interpro was applied to provide functional analysis of protein sequences by classifying them into families and predicting the presence of domains and important sites, followed by Gene Ontology annotation [35][36][37] . Overall, 22,162 protein-coding genes (98.67%) were successfully functionally annotated (Table 5).
    > Non-coding RNAs (ncRNAs) are an important part of genome annotation as they can be active in transcriptional and translational regulation of gene expression as well as in the modulation of protein function 38 . Since ribosomal RNA (rRNA) was highly conservative, vertebrate rRNA data was used as a reference to map to the draft genome using BLASTn with an E-value of 1e-5. For the discovery of transfer RNA (tRNA), tRNAscan-SE v1.3.1 was applied with eukaryotic parameters according to the characteristics of tRNA 39 . Rfam database was applied to find microRNAs (miRNA) and small nuclear RNA (snRNA) 40,41 .

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöery, R. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Juan Wang, Yi Liu, Xi-Zhao Chen, Mansheng Li, Yunping Zhu (2024). Protocol for identifying and comparing molecular prognosis subtypes of IgAN using R. STAR Protocols. https://www.semanticscholar.org/paper/6794ab2424155d4a65b28cd139731c21d4d37aa2
5. Xin-You Cao, Ji-Jin Zhang, Ya-Fei Guo, Yuhong Huang, Lei Guo et al. (2026). A high-quality bread wheat genome unravels the adaptive evolution of wheat end-use quality. Nature Plants. https://www.semanticscholar.org/paper/2e5e60b07b1b58e9b8258a63c57887e951fba19d
6. Nazanin Farahi, T. Lazar, P. Tompa, Bálint Mészáros, R. Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
7. Xiaoqiong Bao, Qi Jiang, Wei-Xuan Chen, Hui-Qin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
8. D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al. (2023). AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes. Mammalian Genome. https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99
9. Nazanin Farahi, T. Lazar, Peter Tompa, Bálint Mészáros, R. Pancsa (2025). Phase-separating fusion proteins drive cancer by upsetting transcription regulation. Genome Biology. https://www.semanticscholar.org/paper/54d550a595352429b7ad7fdab681cd564170f566
10. Jia-Cheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yu-Tao Wang et al. (2025). MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila. Synthetic and Systems Biotechnology. https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
11. Jiao-Jiao Guan, Jiayu Shang, Cheng Peng, Yan-Ni Sun (2026). VirProtRAG: Literature-grounded viral protein function annotation with retrieval-augmented generation. bioRxiv. https://www.semanticscholar.org/paper/2f46f2b474600cdef3038432c50028f679298d36
12. Anthony C. Smith, A. J. Robinson (2009). MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data. Molecular & Cellular Proteomics : MCP. https://www.semanticscholar.org/paper/206a60d6d387688ce7f880e0dfe67af5a723c7b8
13. Christina M McCosker, E. Unal, Alayna K. Gigliotti, Wendy B. Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
14. Khairun Hisam Bin Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
15. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
16. Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al. (2026). An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models. Nature Communications. https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
17. B. Waegele, I. Dunger-Kaltenbach, G. Fobo, C. Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
18. Namrata D. Udeshi, Kayvon Pedram, Tanya Svinkina, Shaunt Fereshetian, S. Myers et al. (2017). Antibodies to biotin enable large-scale detection of biotinylation sites on proteins. Nature methods. https://www.semanticscholar.org/paper/f9e4f461ca61f4399a95875ea96fb075fa959901
19. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
20. Zhongdian Dong, Jiangman Wang, Guo-Zhu Chen, Yusong Guo, Na Zhao et al. (2024). A high-quality chromosome-level genome assembly of the Chinese medaka Oryzias sinensis. Scientific Data. https://www.semanticscholar.org/paper/22e6bac57aff18bdef6ecc2240c145ad3758b9ee