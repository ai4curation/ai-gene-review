---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T16:21:07.657229'
end_time: '2026-07-10T16:21:12.708755'
duration_seconds: 5.05
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2333
  gene_symbol: PP_2333
  uniprot_accession: Q88KF7
  protein_description: 'SubName: Full=GntR family transcriptional regulator {ECO:0000313|EMBL:AAN67946.1};'
  gene_info: OrderedLocusNames=PP_2333 {ECO:0000313|EMBL:AAN67946.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: GntR_C. (IPR011711); TF_FadR/GntR_C. (IPR008920); Tscrpt_reg_HTH_GntR.
    (IPR000524); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390)
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
- **UniProt Accession:** Q88KF7
- **Protein Description:** SubName: Full=GntR family transcriptional regulator {ECO:0000313|EMBL:AAN67946.1};
- **Gene Information:** OrderedLocusNames=PP_2333 {ECO:0000313|EMBL:AAN67946.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** GntR_C. (IPR011711); TF_FadR/GntR_C. (IPR008920); Tscrpt_reg_HTH_GntR. (IPR000524); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2333" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2333' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2333** (gene ID: PP_2333, UniProt: Q88KF7) in PSEPK.

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
  - Snippet 1 (score: 0.773)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.760)
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
  - Snippet 1 (score: 0.751)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

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
  - Snippet 1 (score: 0.741)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.736)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [6] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.735)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [7] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.733)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [8] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.728)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [9] Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms
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
  - Snippet 1 (score: 0.718)
    > Examples are for illustrative purposes only and specific to each case, hence not all the entities are shown and highlighted. RED: Gene/Protein BLUE: Disease GREEN: Organism a. Biomedical concepts Gene/Protein: Annotations could be specific gene/protein names or classes/family names of gene/proteins. In particular, very broad concepts like "protein", "gene", "enzyme", "receptors", "kinase", "cytokine", "transcription regulators/factors" are out of the scope of annotations. However, family/subtype names of those concepts are considered for the annotations, such as "amylolytic enzyme", "antioxidant enzyme", "map kinase p38", because these terms narrow the concepts to specific families of gene/protein, enzyme.
    > Annotators can refer to Uniprot and Protein Ontology.

### [10] FusionPDB: a knowledgebase of human fusion proteins
- Authors: H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim
- Year: 2023
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
- DOI: 10.1093/nar/gkad920
- PMID: 37870473
- PMCID: 10767906
- Citations: 13
- Influential citations: 1
- Summary: FusionPDB is the only resource providing whole 3D structures of fusion proteins and comprehensive knowledge of human fusion proteins and it will be regularly updated until it covers all human fusion proteins in the future.
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > To assign functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt for 10 619 genes involved in 15 030 fusion genes ( 10 ). UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features and three secondary structure features. Since such feature loci information is based on amino acid sequences, the genomic breakpoint information was converted into the amino acid level while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE (v19) gene model of human reference genome ( 11 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported such fusion genes as having not retained that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.

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
  - Snippet 1 (score: 0.708)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [12] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.705)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [13] iPCD: A Comprehensive Data Resource of Regulatory Proteins in Programmed Cell Death
- Authors: Dachao Tang, Cheng Han, Shaofeng Lin, Xiaodan Tan, Weizhi Zhang et al.
- Year: 2022
- Venue: Cells
- URL: https://www.semanticscholar.org/paper/eb35030c62fa8e25fe91d3a4e48fef1de95e562c
- DOI: 10.3390/cells11132018
- PMID: 35805101
- PMCID: 9265749
- Citations: 7
- Summary: A comprehensive database, with integrated annotations for programmed cell death (iPCD), which contained 1,091,014 regulatory proteins involved in 30 PCD forms across 562 eukaryotic species and an in-depth annotation of PCD proteins in eight model organisms is developed.
- Evidence snippets:
  - Snippet 1 (score: 0.702)
    > The PCD regulators were collected and annotated. First, 1,091,014 PCD regulators were annotated with basic information, including 'iPCD ID', 'status', 'Ensembl Gene ID', 'Ensembl Protein ID', 'UniProt Accession', 'PDB structure', 'Function', 'Protein Sequence', 'Nucleotide Sequence', 'Key word' and 'Gene Ontology'. For each species, all regulatory proteins were alphabetically ordered based on their gene names. Then, each protein was automatically assigned a unique iPCD ID for convenient organization in the database. For example, the GPX4 protein in Homo sapiens was assigned with an ID of 'iPCD-Hsa-1522'. Subsequently, 102 additional public resources were integrated to annotate 17,768 regulators from 8 model organisms, including Homo sapiens, Mus musculus, Rattus norvegicus, Drosophila melanogaster, Caenorhabditis elegans, Saccharomyces cerevisiae, Arabidopsis thaliana and Danio rerio. These public resources covered 16 distinct aspects, which contained (i) genetic variation and mutation, (ii) functional annotation, (iii) structural annotation, (iv) physicochemical property, (v) functional domain, (vi) post-translational modification (PTM), (vii) disease-associated information, (viii) protein-protein interaction (PPI), (ix) drug-target relation, (x) orthologous information, (xi) biological pathway, (xii) transcriptional regulator, (xiii) mRNA expression, (xiv) protein expression/proteomics, (xv) subcellular localization and (xvi) DNA and RNA element. The detailed processing of 102 public resources is provided in Supplementary Methods. A brief flowchart of the study is shown in Figure 1A.

### [14] ExtraTrain: a database of Extragenic regions and Transcriptional information in prokaryotic organisms
- Authors: E. Pareja, Pablo Pareja-Tobes, Marina Manrique, Eduardo Pareja-Tobes, J. Bonal et al.
- Year: 2006
- Venue: BMC Microbiology
- URL: https://www.semanticscholar.org/paper/9a9a799ef8279d9e22f43371f59155458457fa51
- DOI: 10.1186/1471-2180-6-29
- PMID: 16539733
- PMCID: 1453763
- Citations: 57
- Influential citations: 3
- Summary: ExtraTrain is a new database for exploring Extra genic regions and Tra nscriptional in formation in bacteria and archaea and supplies a tool to explore extragenic regions, named Palinsight, oriented to detect and search palindromic patterns.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > An initial page about regulatory proteins displays information about the 16 families included in the database (Table 1) and a graphic illustration representing the distribution of families in the ExtraTrain database. By selecting a genome the user can obtain a graphical view displaying the distribution of the different families of regulatory proteins in the selected genome.
    > The ExtraTrain definition of entry for transcriptional regulatory proteins is identical to the UniProt definition of entry, which is based solely on the protein sequence.
    > Furthermore, the ExtraTrain regulator entry identifier is the UniProt identifier for this protein. We have chosen these unified criteria to reinforce invaluable initiatives of integration such as UniProt.
    > The web page corresponding to an ExtraTrain regulatory protein entry shows data automatically extracted from Uniprot, manually curated references extracted from Medline, a list of BLAST similar proteins and information about all extragenic regions upstream this regulator in the available genomes. The majority of regulatory proteins in the current ExtraTrain database are encoded by only one gene in one genome and hence, have only one upstream extragenic region. However, in the near future, with the availability of several strains for each species, it will be frequent to found several genes in several genomes encoding the same regulatory protein. It will allow the analysis of each protein in its different genetic contexts. This lack of one to one relationship between proteins and genes is solved in ExtraTrain by establishing the connexion between proteins and genes through extragenic regions without the loss of biologically relevant information. 3 is the copy of the complete content of this window.

### [15] MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila
- Authors: Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al.
- Year: 2025
- Venue: Synthetic and Systems Biotechnology
- URL: https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
- DOI: 10.1016/j.synbio.2025.04.001
- PMID: 40276250
- PMCID: 12018684
- Summary: Shifts in metabolic allocation in a glucoamylase hyperproduction strain of M. thermophila are identified, highlighting changes in fatty acid biosynthesis and amino acids biosynthesis pathways, which provide new insights into the underlying phenotypic alterations.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > Single-gene search: Gene annotation is essential for biologists to understand a gene's function. MTD's single-gene search interface allows researchers to obtain a comprehensive gene description by entering or selecting a gene ID. The results include sequence information, CAZy family, Pfam domains, GO/KEGG annotations, and phenotype information (Fig. 2D), along with sequence-based predictions such as optimal protein activity temperature, melting temperature (Tm), subcellular localization, and transcription factor scores. To enhance data accessibility, links to external databases such as NCBI, KEGG, FungiDB [4], UniProt, and JGI are also provided, facilitating cross-referencing of gene annotations across various resources.
    > Unlike the static genome, the transcriptome captures dynamic gene expression changes in response to developmental or environmental conditions, establishing a dynamic link between an organism's genome and its physical characteristics [63]. In the single-gene retrieval interface, the expression of the searched gene is visualized in the form of box plots and scatter plots across transcriptome datasets (Fig. 2E). When hovering over any data point, users can view the corresponding experimental details, such as mutant name, sample processing methods, and growth conditions. This interactive feature reveals gene expression responses to environmental factors, allowing researchers to quickly identify experimental conditions of interest and explore the gene's potential roles in diverse biological contexts. Moreover, clicking on the dataset title will direct users to the GEO browser for further detailed descriptions. KEGG Pathway or Gene List Search: In transcriptome studies, researchers typically adopt a "bottom-up" approach: first sequencing all mRNA in a cell, identifying differentially expressed genes between conditions, and then performing GO/KEGG enrichment analysis to interpret functional distributions. MTD, however, offers a complementary "top-down" search strategy, enabling users to examine the expression of genes within a specific KEGG pathway (Fig. 3A) or a user-defined gene set. A unique feature of MTD is its manually curated data categorization system, which organizes sample data with detailed annotations based on experimental conditions.

### [16] The Plant Parasitic Nematodes Database: A Comprehensive Genomic Data Platform for Plant Parasitic Nematode Research
- Authors: Junhao Zhuge, Xiang Zhou, Lifeng Zhou, Jiafu Hu, Kai Guo
- Year: 2023
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/c62d6f382586d9dfd2e8e9d5b55dfc9215946ccc
- DOI: 10.3390/ijms242316841
- PMID: 38069165
- PMCID: 10706385
- Citations: 5
- Summary: The Plant Parasitic Nematodes Database (PPND) is developed, a platform to combine genomic, transcriptomic, protein, and functional annotation data, allowing users to conduct BLAST searches and genome browser analyses and download bioinformatics data for in-depth research.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > PPND integrates various sequences, annotations, and expression information to provide an efficient search tool for researchers, including the gene, gene family, transcription factor (TF), and protein kinase searches. In subsequent work, we added four additional tool modules: flanking sequence finder, TTL (Transthyretin-like) family [46] finder, pathway map, and miRNA search. Users can enter the gene ID obtained from BLAST or the genome browser into the gene search function to obtain more information. This includes information on the origin of the organism, gene family, KEGG ID, coding sequence, protein sequence, annotation information (site position and annotation source database), and expression data (Figure 4). This information will allow researchers to gain a basic understanding of the gene structure and function. Certain search functionalities, such as the protein kinase search, complement the gene search function. They provide more detailed assistance for researchers with varying levels of bioinformatics analysis expertise. Therefore, PPND provides Pfam links in the gene search function. By linking to InterPro, researchers can access additional information. Using this toolkit, users can also obtain information on the upstream and downstream sequences, functional components, signaling pathways, and miRNA sequences of the target gene. These data can help researchers conduct more in-depth investigations.
    > Gene families are groups of genes derived from a single ancestral gene due to gene duplication events. They usually have high similarity in structure and function and encode similar proteins with shared domains. For example, the MADS-box gene family [47] is involved in plant growth and development, especially flower reproductive development. In PPND, users can search for a gene family by entering the gene family name or Pfam ID and selecting a species. They can also click "↓" to make a selection. The "↓" button will display a random set of 50 members, including the family name and Pfam ID. The platform provides a list of genes from that family along with the option to obtain their sequences in FASTA format (Figure 5). Gene families are groups of genes derived from a single ancestral gene due to gene duplication events. They usually have high similarity in structure and function and encode similar proteins with shared domains.

### [17] A haplotype-resolved genome assembly of Malus domestica ‘Red Fuji’
- Authors: Haixu Peng, Yating Yi, Jinrong Li, You Qing, Xuyang Zhai et al.
- Year: 2024
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/e5dc0e3046713c6ff2aed20631ab819fffd8b0c0
- DOI: 10.1038/s41597-024-03401-1
- PMID: 38844753
- PMCID: 11156929
- Citations: 7
- Summary: The haplotype-resolved genome of ‘Red Fuji’ apple stands as a precise benchmark for an array of analyses, such as comparative genomics, transcriptomics, and allelic expression studies.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > For the functional annotation of the protein-coding genes, we employed a standardized workflow 30,31 .In summary, the protein sequences of the two haplotype genomes were compared against several protein databases using the DIAMOND program, with an E-value cutoff of 1E-4.The protein databases included the non-redundant protein database (NR), TrEMBL (http://www.uniprot.org/),SwissProt 32 , and the Arabidopsis protein database.The BLAST results from SwissProt, TrEMBL, and the Arabidopsis protein database were loaded into the AHRD (https://github.com/asishallab/AHRD)program to predict concise, informative, and accurate functional descriptions for each gene.
    > Furthermore, the protein sequences were compared against the InterPro database 33 using InterProScan to identify functional protein domains.The BLAST results from the NR database were combined with the identified InterPro protein domains to perform Gene Ontology (GO) annotation using the Blast2GO program 34 , and the GO terms were associated with the annotated protein sequences.To explore the protein-coding genes' connections to pathways, the 'Red Fuji' apple protein sequences were annotated using the online KAAS tool (https://www.genome.jp/tools/kaas/).This annotation provided information about the genes' associations with various metabolic pathways.Additionally, the iTAK software was used to predict transcription factors, transcription regulators, and protein kinases.
    > The protein-coding genes were compared separately with the NR, SwissProt, Arabidopsis protein database, and TrEMBL databases.Each database annotated 95,552, 77,453, 67,243, and 92,132 genes, respectively.A total of 52,073 genes were matched to 2,555 GO terms.Additionally, in the pathway annotation, 32,312 genes were annotated to 143 ko IDs.In the prediction of transcription factors (TFs) and transcription regulators (TRs), a total of 6,283 genes belong to 93 different gene families.Additionally, 3,119 genes were annotated to 127 different protein kinase (PK) families.

### [18] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.689)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [19] Into the metabolic wild: Unveiling hidden pathways of microbial metabolism
- Authors: Özge Ata, D. Mattanovich
- Year: 2024
- Venue: Microbial Biotechnology
- URL: https://www.semanticscholar.org/paper/81ac8bfd05a0c52f8a5b6d058c5414b45bb5c1f9
- DOI: 10.1111/1751-7915.14548
- PMID: 39126421
- PMCID: 11316390
- Citations: 5
- Summary: The predictive power of metabolic modelling, well‐founded on biochemical knowledge and genomic information is discussed in the light of both discovery of yet unknown existing metabolic routes and the prediction of others, new to Nature.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > One major concern regarding genome data is the potential spread of false or inaccurate functional annotations iterating by sequence similarity-based gene annotations where functions are ascribed by analogy to other organisms' genes rather than being experimentally verified. As the source of information on a putative gene function is not always clearly indicated in databases, we advise researchers to always trace the original literature related to a gene function to verify its plausibility in a given non-model organism.
    > A special case is the genes with no known functional annotation in model organisms, like the y-genes in E. coli (so named because their gene names begin with the letter y). Ghatak et al. (2019) used multiple databases to define the y-ome of E. coli as the 35% genes that lack experimental evidence of their function, and highlight the differences between genes that lack any known function and those with attributed localization or computationally annotated functional domains. A similar situation is observed with eukaryotic genomes, where a consistent fraction of about 20% of the genes remains with unknown (or unstudied) gene products. Wood et al. (2019) compared unknown gene products of Schizosaccharomyces pombe, S. cerevisiae, and Homo sapiens, and concluded that these genes remained understudied even since genome sequences were published. They disprove the common assumption that unknown gene products are mostly orphaned, as the majority are conserved from yeasts to humans, and they conclude that the reasons for the lack of research on these proteins is two-fold. For many of these genes, no apparent knockout phenotype was observed in standard conditions. On the other hand, researchers still focus on a few well-studied proteins rather than exploring unknown territories, which the authors partly ascribe to risk-adverse strategies of funders and reviewers.
    > Although the primary use of metabolic models is the analysis of already known metabolic pathways, the potential of metabolic models extends far beyond these analyses. They can be used to uncover hidden pathways, unknown reactions, and to construct de novo pathways.

### [20] Experimental validation of novel genes predicted in the un-annotated regions of the Arabidopsis genome
- Authors: William A. Moskal, Hank Wu, Beverly A. Underwood, Wei Wang, C. Town et al.
- Year: 2007
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/4ce1de531b1c484ff37cebc7a4d18811d3425ab9
- DOI: 10.1186/1471-2164-8-18
- PMID: 17229318
- PMCID: 1783852
- Citations: 14
- Influential citations: 3
- Summary: The accuracy of the Twinscan and EuGene gene prediction programs are found to be reliable predictors of gene structure in Arabidopsis and several hundred previously un-annotated genes were validated by this work.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > we observed reporter gene expression from lines tagging 2 of 3 genes. The lack of expression observed with five of our promoter-reporter lines as well as a gene trap line obtained from CSHL's collection is likely due to either a very low level of expression directed by those promoters, or a very specific pattern, timing, or condition for expression that was not tested by our assays. The pools of cDNA which served as our RACE template originated from several biotic and abiotic treatments that we did not examine in relation to our promoter-reporter constructs.
    > Overall, we verified the expression and structure of 378 un-annotated genes, 27% of which do not display similarity to any annotated proteins. Furthermore, nearly 50% of the genes described herein are most similar to hypothetical proteins or other proteins of unknown function.
    > Examining the putative functional roles of the remaining un-annotated genes, we can begin to speculate the reasons that many were overlooked by previous annotation efforts. Single copy, lowly expressed genes such as the putative alpha 1,-6, mannosyltransferase corresponding to Twinscan prediction At.chr1.1.117, which does not have similarity with other Arabidopsis genes was likely overlooked due to the lack of support from conserved EST sequences. On the other hand, At.chr1.6.385, which encodes a CLAVATA3/ESR related protein and is a member of a divergent multi-gene family, was likely overlooked due to a combination of lack of EST support [30], and a relatively small coding size. Similarly, we have identified members of a large and divergent gene family encoding Cysteine Rich Peptides. The small size and divergent sequences of this family have contributed to their under-representation in the genome annotation [12]. Additionally, approximately 50% of the top protein hits for the newly verified genes are to hypothetical proteins, or other poorly characterized proteins having unknown function and low expression levels. These examples underscore the limitations of gene prediction programs that still rely to a large extent on training sets derived from relatively abundantly expressed proteins.
    > The incorporation of genomic sequence data from related organisms allows for the easier identification of such genes.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
5. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
6. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
7. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
8. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
9. Xiao Yang, Shyamasree Saha, Aravind Venkatesan, Santosh Tirunagari, Vid Vartak et al. (2023). Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms. Scientific Data. https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
10. H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim (2023). FusionPDB: a knowledgebase of human fusion proteins. Nucleic Acids Research. https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
11. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
12. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
13. Dachao Tang, Cheng Han, Shaofeng Lin, Xiaodan Tan, Weizhi Zhang et al. (2022). iPCD: A Comprehensive Data Resource of Regulatory Proteins in Programmed Cell Death. Cells. https://www.semanticscholar.org/paper/eb35030c62fa8e25fe91d3a4e48fef1de95e562c
14. E. Pareja, Pablo Pareja-Tobes, Marina Manrique, Eduardo Pareja-Tobes, J. Bonal et al. (2006). ExtraTrain: a database of Extragenic regions and Transcriptional information in prokaryotic organisms. BMC Microbiology. https://www.semanticscholar.org/paper/9a9a799ef8279d9e22f43371f59155458457fa51
15. Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al. (2025). MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila. Synthetic and Systems Biotechnology. https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
16. Junhao Zhuge, Xiang Zhou, Lifeng Zhou, Jiafu Hu, Kai Guo (2023). The Plant Parasitic Nematodes Database: A Comprehensive Genomic Data Platform for Plant Parasitic Nematode Research. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/c62d6f382586d9dfd2e8e9d5b55dfc9215946ccc
17. Haixu Peng, Yating Yi, Jinrong Li, You Qing, Xuyang Zhai et al. (2024). A haplotype-resolved genome assembly of Malus domestica ‘Red Fuji’. Scientific Data. https://www.semanticscholar.org/paper/e5dc0e3046713c6ff2aed20631ab819fffd8b0c0
18. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
19. Özge Ata, D. Mattanovich (2024). Into the metabolic wild: Unveiling hidden pathways of microbial metabolism. Microbial Biotechnology. https://www.semanticscholar.org/paper/81ac8bfd05a0c52f8a5b6d058c5414b45bb5c1f9
20. William A. Moskal, Hank Wu, Beverly A. Underwood, Wei Wang, C. Town et al. (2007). Experimental validation of novel genes predicted in the un-annotated regions of the Arabidopsis genome. BMC Genomics. https://www.semanticscholar.org/paper/4ce1de531b1c484ff37cebc7a4d18811d3425ab9