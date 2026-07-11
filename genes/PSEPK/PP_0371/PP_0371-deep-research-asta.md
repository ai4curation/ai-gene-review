---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T18:28:25.184011'
end_time: '2026-07-10T18:28:30.457833'
duration_seconds: 5.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0371
  gene_symbol: PP_0371
  uniprot_accession: Q88QW3
  protein_description: 'SubName: Full=Transcriptional regulator, LysR family {ECO:0000313|EMBL:AAN66002.1};'
  gene_info: OrderedLocusNames=PP_0371 {ECO:0000313|EMBL:AAN66002.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the LysR transcriptional regulatory family.
  protein_domains: LysR_HTH_N. (IPR000847); LysR_subst-bd. (IPR005119); WH-like_DNA-bd_sf.
    (IPR036388); WH_DNA-bd_sf. (IPR036390); HTH_1 (PF00126)
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
- **UniProt Accession:** Q88QW3
- **Protein Description:** SubName: Full=Transcriptional regulator, LysR family {ECO:0000313|EMBL:AAN66002.1};
- **Gene Information:** OrderedLocusNames=PP_0371 {ECO:0000313|EMBL:AAN66002.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the LysR transcriptional regulatory family.
- **Key Domains:** LysR_HTH_N. (IPR000847); LysR_subst-bd. (IPR005119); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390); HTH_1 (PF00126)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0371" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0371' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0371** (gene ID: PP_0371, UniProt: Q88QW3) in PSEPK.

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
  - Snippet 1 (score: 0.766)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [2] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.758)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [3] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.745)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.743)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [5] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.732)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [6] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.725)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [7] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.725)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [8] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.713)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [9] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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

### [10] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.705)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [11] A short guide to long non-coding RNA gene nomenclature
- Authors: M. Wright
- Year: 2014
- Venue: Human Genomics
- URL: https://www.semanticscholar.org/paper/5603656d27ad714cebcb661e6d4089e9c7f34e37
- DOI: 10.1186/1479-7364-8-7
- Citations: 3
- Influential citations: 1
- Summary: A short guide is presented herein to help authors when developing novel gene symbols for lncRNAs with characterised function, and to provide unique and, wherever possible, meaningful gene symbols to all lncRNA genes.
- Evidence snippets:
  - Snippet 1 (score: 0.705)
    > The HUGO Gene Nomenclature Committee (HGNC) is the only organisation authorised to assign standardised nomenclature to human genes. Of the 38,000 approved gene symbols in our database (http://www.genenames.org), the majority represent protein-coding (pc) genes; however, we also name pseudogenes, phenotypic loci, some genomic features, and to date have named more than 8,500 human non-protein coding RNA (ncRNA) genes and ncRNA pseudogenes. We have already established unique names for most of the small ncRNA genes by working with experts for each class. Small ncRNAs can be defined into their respective classes by their shared homology and common function. In contrast, long non-coding RNA (lncRNA) genes represent a disparate set of loci related only by their size, more than 200 bases in length, share no conserved sequence homology, and have variable functions. As with pc genes, wherever possible, lncRNAs are named based on the known function of their product; a short guide is presented herein to help authors when developing novel gene symbols for lncRNAs with characterised function. Researchers must contact the HGNC with their suggestions prior to publication, to check whether the proposed gene symbol can be approved. Although thousands of lncRNAs have been predicted in the human genome, for the vast majority their function remains unresolved. lncRNA genes with no known function are named based on their genomic context. Working with lncRNA researchers, the HGNC aims to provide unique and, wherever possible, meaningful gene symbols to all lncRNA genes.

### [12] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.702)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [13] Genenames.org: the HGNC and PGNC resources in 2026
- Authors: Ruth L. Seal, Bryony Braschi, Kristian A. Gray, James C. McClay, Susan Tweedie et al.
- Year: 2025
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/730580471233ae0456a420c386bf72758e999faa
- DOI: 10.1093/nar/gkaf1229
- PMID: 41287213
- PMCID: 12807706
- Citations: 9
- Summary: The PGNC project, which has been approving gene symbols and names for the tree species Populus trichocarpa, is introduced and all approved plant gene nomenclature is displayed on the new website plant.genenames.org.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > The HGNC approves symbols for genes of several different biotypes, the main categories of which are proteincoding, non-coding RNA, and pseudogenes. See https://www. genenames.org/ download/ statistics-and-files for a full list of our biotypes and the associated numbers of genes with approved symbols. As of September 3, 2025, the HGNC website contains 44 476 genes in total with 19 294 protein coding genes, 14 603 pseudogenes and 9574 ncRNA genes-of which the largest sub-categories are long non-coding RNA (6236 genes), microRNA (1912 genes), transfer RNA (591 genes), and small nucleolar RNA (568 genes), see Fig. 1 for a chart displaying the proportion of named genes for these locus types.
    > The set of protein-coding genes with HGNC symbols, based on current manual gene annotation guidelines, is relatively complete. Most HGNC work on protein-coding genes focuses on renaming genes with placeholder symbols and evaluating the stability of existing gene symbols, as described later in this paper. There are some examples of "novel" proteincoding genes that have been recently described in publications and subsequently assigned approved nomenclature by the HGNC, including MLDHR (HGNC:55 481), which was identified by [ 14 ] as located within the 5 UTR of the PTEN (HGNC:9588) gene. The authors published this gene as "MP31" for "micropeptide of 31 amino acids," which does not fulfill HGNC guidelines due to the mention of the number of amino acid residues. Based on the functional information in [ 14 ], the HGNC approved the unique, searchable gene symbol MLDHR with the corresponding gene name "mitochondrial lactate dehydrogenase regulator." A second example is SMIM10L3 (HGNC:56 768), which was identi- fied in [ 15 ] and is also an example of a protein-coding gene nested within the 5 UTR of a separate, characterized proteincoding gene, FAM220A (HGNC:22 422).

### [14] WormBase 2024: status and transitioning to Alliance infrastructure
- Authors: Paul W. Sternberg, K. V. Van Auken, Qinghua Wang, Adam J. Wright, K. Yook et al.
- Year: 2024
- Venue: Genetics
- URL: https://www.semanticscholar.org/paper/dcfce02a58655b0872a8265f5c85dbbd94957294
- DOI: 10.1093/genetics/iyae050
- PMID: 38573366
- PMCID: 11075546
- Citations: 199
- Influential citations: 9
- Summary: The current state of WormBase as well as progress and plans for moving core WormBase infrastructure to the Alliance of Genome Resources (the Alliance) are discussed.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > Of the 19,984 protein-coding genes in C. elegans, 10,838 have a name/gene symbol (e.g. lin-12). Gene naming is largely investigator-initiated, with a request to WormBase through genenames@wormbase.org ; this will continue with C. elegans content in the Alliance. The gene symbol, which is formatted in lowercase and italics, communicates information about the gene based on mutant phenotype, functional criteria, orthology, or homology. To make genes easily recognizable to non-elegans researchers, the current preference is to name genes with human orthologs after the human gene if characterized. Gene name stability and formatting are important to avoid confusion in the literature and to facilitate searches of other databases that use the C. elegans gene symbols (e.g. UniProt) and text mining. However, occasionally names have been changed because of incorrect orthology or not supported by functional studies from the community. Names have also been changed based on requests from multiple community members (e.g. daf-21 renamed as hsp-90). To avoid name changes and to have the published name used in databases, researchers should contact WormBase prior to manuscript submission; the most common issue is that the requested name is already in use in C. elegans or another model organism for a nonhomologous gene product. Over the past 10 years, the community has averaged 180 new gene names per year, often with a corresponding publication, increasing knowledge about our favorite organism. More information about C. elegans-specific nomenclature can be found at https://wormbase.org/about/ userguide/nomenclature.

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
  - Snippet 1 (score: 0.695)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [16] Functional annotation of parasitic worm genomes, by assigning protein names and GO terms
- Authors: Avril Coghlan, M. Berriman
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
- DOI: 10.1038/protex.2018.055
- Citations: 1
- Summary: A computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and Go terms from orthologues in other species.
- Evidence snippets:
  - Snippet 1 (score: 0.695)
    > Given a set of predicted protein-coding genes for a newly sequenced genome, functional annotation involves assigning putative functions to the predicted genes. Two ways in which this can be done are assigning protein names and Gene Ontology (GO;Gene Ontology Consortium, 2010) terms to the predicted proteins. Here we describe a computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and GO terms from orthologues in other species.
    > When assigning protein names, UniProt protein naming rules (www.uniprot.org/docs/nameprot) are followed where possible. This recommends that a good and stable name for a protein is "as neutral as possible"; that a protein name "should be, as far as possible, unique and attributed to all orthologs"; and a protein name "should not contain a specific characteristic of the protein, and in particular it should not reflect the function or role of the protein, nor its subcellular location, its domain structure, its tissue specificity, its molecular weight or its species of origin".
    > In our protocol, a protein name is assigned to each predicted protein based on curated names in UniProt (Bairoch & Apweiler, 2000) for human, zebrafish, Drosophila melanogaster, Caenorhabditis elegans, and Schistosoma mansoni orthologues identified from a database of gene families (e.g. built using Ensembl Compara; Vilella et al. 2009), or (if no information is found from orthologues) based on InterPro (Hunter et al. 2012) domains. Figure 1 shows an example of using our protein naming pipeline for four Strongyloides ratti genes that belong to the tubulin polyglutamylase family (underlined in pink), where four different protein names were assigned to them (in pink), based on names of their C. elegans or human orthologues.
    > Since each of the S. ratti genes belonged to a different subfamily of the tubulin polyglutamylase family, they were assigned different names.

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
  - Snippet 1 (score: 0.693)
    > In an effort to engage the collective expertise of the scientific community, we have implemented a collaborative wiki (MediaWiki version 1.19.11) for the Mnemiopsis gene complement. The Mnemiopsis Gene Wiki is accessible from the left sidebar of most pages and is searchable either by selecting a Mnemiopsis gene identifier (e.g., ML00011a) from the drop-down menu or by manually entering an identifier in the appropriate search box. Users can also access these pages by clicking on a gene in the 2.2 track of the genome browser. Each record in the Gene Wiki represents a single Mnemiopsis gene and provides the following annotation: nucleotide and protein sequences, coding exonic genomic coordinates, pre-computed BLAST hits from numerous organisms displaying the top hits for each protein, the top non-self BLAST hit to Mnemiopsis, Pfam-A domains, Gene Ontology (GO) functional annotations, human disease genes from Online Mendelian Inheritance in Man (OMIM), and a table of ortholog clusters formed by phylogenetically informed clustering methods [4] (Figure 5). In addition, controlled editable sections have been included that permit (and encourage) the scientific community to provide further gene annotation for isoforms, in situ images, references, and other notes for each gene. Users interested in supplementing our gene model annotation at the Mnemiopsis Gene Wiki pages must first create an account and log in prior to submitting their contributions. In-house subject matter expert data curators are notified by e-mail following the creation of a new user account or an edit to an existing Gene Wiki record. Any content changes or additions to the Gene Wiki are thoroughly evaluated by these data curators and are made public subject to their approval.
    > Pre-compiled BLAST hits are enumerated in tabular form. Each Mnemiopsis protein was compared to the UniProt and NCBI non-redundant protein databases (nr) using BLASTP. The results display the hit number, the accession numbers, E-values, and brief descriptions of the top four hits (lowest E-values). Accession numbers are linked to relevant corresponding entries at UniProt and GenBank.

### [18] Hymenoptera Genome Database: integrating genome annotations in HymenopteraMine
- Authors: C. Elsik, A. Tayal, Colin M. Diesh, Deepak R. Unni, Marianne L. Emery et al.
- Year: 2015
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/f3050b6d6a0a45db7ad78d972e5c014195a3abf0
- DOI: 10.1093/nar/gkv1208
- PMID: 26578564
- PMCID: 4702858
- Citations: 112
- Influential citations: 6
- Summary: An update of the HGD, a model organism database for insect species of the order Hymenoptera (ants, bees and wasps), which maintains genomic data for 9 bee species, 10 ant species and 1 wasp, including the versions of genome and annotation data sets published by the genome sequencing consortiums and those provided by NCBI.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > HymenopteraMine provides a report for each entity in the database. Each report is divided into sections including 'Summary', 'Gene', 'Gene Expression', 'Protein', 'Function', 'Homology', 'Others' or a subset of those categories, depending on the identifier searched. For example, searching a protein identifier would provide sections relevant to proteins. Each section of the report provides information in the form of a table that can be customized and downloaded in various formats. The Summary section of a Gene Report provides gene identifiers, symbols, description, organism, chromosome, strand and other identifiers such as aliases (identifiers from previous OGS versions) and database cross references. The Transcripts section provides information about the gene model (transcripts, exons, coding sequences) and gives a visual representation of the gene model highlighting the structure of the gene. Users can download FASTA-formatted sequences for each type of feature provided in the gene model section. Links are provided to JBrowse and to NCBI gene pages, when applicable. Transcript identifiers are linked to Transcript Reports, which include a Gene Expression section that provides raw read counts, normalized read counts, FPKM and RPKM values for RNAseq data with SRA metadata. The Protein section of the Gene Report includes protein name, accession and length. The protein name/accession numbers are linked to Protein Reports, with more information including protein family, GO annotations, InterPro domains, related publications, protein features, and curated notes from UniProt describing tissue specificity, function and developmental stages. The Function section provides GO annotation with evidence codes from the Biological Process, Molecular Function and Cellular Component ontologies. Clicking on the symbols to the right of each GO term leads to the directed acyclic graph showing all parents and children of the term, developed using the BioJS DAG Viewer (50). Clicking on a GO term provides a report for that term, a list of genes annotated with that term and tables showing relationships to other GO terms. The Homologue sec-tion lists homologues in other hymenopteran species and Drosophila melanogaster. The 'Other' section provides publications and a list of overlapping features.

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

### [20] A MOD(ern) perspective on literature curation
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
  - Snippet 1 (score: 0.685)
    > For example, the symbol PAP1 in Arabidopsis thaliana is the primary symbol or alias for four different genes (PURPLE ACID PHOSPHATASE 1, PHOSPHATIDIC ACID PHOSPHATASE 1, PRODUC-TION OF ANTHOCYANIN PIGMENT 1, and PHY-TOCHROME-ASSOCIATED PROTEIN 1). There are currently 216 similar examples for zebrafish, where a gene has a primary symbol that is the same as an alias for at least one other zebrafish gene. As a result, use of these symbols in the literature is ambiguous, and more information is required to resolve which specific gene is actually described in a particular paper. Additionally, many species have gene duplicates which share a root symbol but are appended with an 'a' or 'b' suffix. For example, when a publication discusses the zebrafish gene 'wnt8', it is unclear which specific gene is meant as zebrafish have both a wnt8a and a wnt8b gene. There is no way to resolve such a case without a sequence accession number, or communication directly with the authors.
    > Curators of each MOD have tried to formalize the process of naming genes according to the wishes of their respective research communities (Table 3). Not all researchers are aware that such processes exist, and that
    > a Limited allele and orthology information are curated as part of phenotype and general literature curation b Interaction data is provided in collaboration with the BioGRID database (http://www.thebiogrid.org/, Breitkreutz et al. 2008) they differ among organisms. In general, validation of gene names is not required as part of the publication process. Consequently, gene names or mutant alleles used in publications sometimes conflict when a gene or mutant already exists with an approved name in the database, or the author-given name is already in use for another gene or mutant. In all such cases, a biocurator must tease out the pertinent information for the appropriate gene by searching through earlier literature cited in the paper or by direct communication with authors. This slows the curation process and unnecessarily increases the risk of data association errors during curation.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
5. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
6. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
7. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
8. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
9. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
10. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
11. M. Wright (2014). A short guide to long non-coding RNA gene nomenclature. Human Genomics. https://www.semanticscholar.org/paper/5603656d27ad714cebcb661e6d4089e9c7f34e37
12. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
13. Ruth L. Seal, Bryony Braschi, Kristian A. Gray, James C. McClay, Susan Tweedie et al. (2025). Genenames.org: the HGNC and PGNC resources in 2026. Nucleic Acids Research. https://www.semanticscholar.org/paper/730580471233ae0456a420c386bf72758e999faa
14. Paul W. Sternberg, K. V. Van Auken, Qinghua Wang, Adam J. Wright, K. Yook et al. (2024). WormBase 2024: status and transitioning to Alliance infrastructure. Genetics. https://www.semanticscholar.org/paper/dcfce02a58655b0872a8265f5c85dbbd94957294
15. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
16. Avril Coghlan, M. Berriman (2018). Functional annotation of parasitic worm genomes, by assigning protein names and GO terms. https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
17. R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al. (2014). A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi. BMC Genomics. https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
18. C. Elsik, A. Tayal, Colin M. Diesh, Deepak R. Unni, Marianne L. Emery et al. (2015). Hymenoptera Genome Database: integrating genome annotations in HymenopteraMine. Nucleic Acids Research. https://www.semanticscholar.org/paper/f3050b6d6a0a45db7ad78d972e5c014195a3abf0
19. Özge Ata, D. Mattanovich (2024). Into the metabolic wild: Unveiling hidden pathways of microbial metabolism. Microbial Biotechnology. https://www.semanticscholar.org/paper/81ac8bfd05a0c52f8a5b6d058c5414b45bb5c1f9
20. J. Hirschman, T. Berardini, H. Drabkin, D. Howe (2010). A MOD(ern) perspective on literature curation. Molecular Genetics and Genomics. https://www.semanticscholar.org/paper/c98b7209b7106364e1a9b75cd45217efc63f6be5