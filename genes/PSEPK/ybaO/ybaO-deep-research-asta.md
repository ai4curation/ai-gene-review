---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T14:03:55.283032'
end_time: '2026-07-10T14:04:00.770544'
duration_seconds: 5.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ybaO
  gene_symbol: ybaO
  uniprot_accession: Q88E71
  protein_description: 'SubName: Full=LRP-like transcriptional regulator {ECO:0000313|EMBL:AAN70168.1};'
  gene_info: Name=ybaO {ECO:0000313|EMBL:AAN70168.1}; OrderedLocusNames=PP_4595 {ECO:0000313|EMBL:AAN70168.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ArsR-like_HTH. (IPR011991); AsnC-type_HTH_dom. (IPR000485); Dimeric_a/b-barrel.
    (IPR011008); Tscrpt_reg_AsnC-like. (IPR019888); Tscrpt_reg_AsnC/Lrp_C. (IPR019887)
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
- **UniProt Accession:** Q88E71
- **Protein Description:** SubName: Full=LRP-like transcriptional regulator {ECO:0000313|EMBL:AAN70168.1};
- **Gene Information:** Name=ybaO {ECO:0000313|EMBL:AAN70168.1}; OrderedLocusNames=PP_4595 {ECO:0000313|EMBL:AAN70168.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ArsR-like_HTH. (IPR011991); AsnC-type_HTH_dom. (IPR000485); Dimeric_a/b-barrel. (IPR011008); Tscrpt_reg_AsnC-like. (IPR019888); Tscrpt_reg_AsnC/Lrp_C. (IPR019887)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ybaO" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ybaO' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ybaO** (gene ID: ybaO, UniProt: Q88E71) in PSEPK.

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
  - Snippet 1 (score: 0.799)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [2] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.777)
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
  - Snippet 1 (score: 0.774)
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
  - Snippet 1 (score: 0.773)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [5] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.770)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

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
  - Snippet 1 (score: 0.753)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [7] FusionPDB: a knowledgebase of human fusion proteins
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
  - Snippet 1 (score: 0.746)
    > To assign functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt for 10 619 genes involved in 15 030 fusion genes ( 10 ). UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features and three secondary structure features. Since such feature loci information is based on amino acid sequences, the genomic breakpoint information was converted into the amino acid level while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE (v19) gene model of human reference genome ( 11 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported such fusion genes as having not retained that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.

### [8] Next Generation Sequencing and Transcriptome Analysis Predicts Biosynthetic Pathway of Sennosides from Senna (Cassia angustifolia Vahl.), a Non-Model Plant with Potent Laxative Properties
- Authors: Nagaraja Reddy Rama Reddy, Rucha Harishbhai Mehta, Palak Soni, Jayanti Makasana, N. Gajbhiye et al.
- Year: 2015
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/fec6263b90f9cd765752bdb1be3d162872f2e64e
- DOI: 10.1371/journal.pone.0129422
- PMID: 26098898
- PMCID: 4476680
- Citations: 81
- Influential citations: 3
- Summary: A set of putative genes involved in various secondary metabolite pathways, especially those related to the synthesis of sennosides are identified which will serve as an important platform for public information about gene expression, genomics, and functional genomics in senna.
- Evidence snippets:
  - Snippet 1 (score: 0.734)
    > Further the assembled transcript contigs were validated using CLC Genomics workbench (CLC Bio, Boston, MA 02108 USA) by mapping high quality reads back to the assembled transcript contigs. ORF-Predictor [57], an online tool, was used on default parameters to identify the coding DNA sequences (CDS) from assembled transcript contigs. GC counts of transcripts was determined using a custom-made perl script.
    > Functional annotations. The functional annotation was performed by aligning coding DNA sequence (CDS) to NCBI 'green plant database (txid 33090)' database using basic local alignment search tool (BLASTX) [58] with an E-value threshold of 1e -06 and GO assignments were used to classify the functions of the predicted CDS. The GO mapping also provided ontology of defined terms representing gene product properties which were grouped into three main domains: biological process (BP), molecular function (MF) and cellular component (CC). GO mapping was carried out in order to retrieve GO terms for all the BLASTX functionally annotated CDS. The GO mapping used defined criteria to retrieve GO terms for annotated CDS which included use of BLASTX result accession IDs to retrieve gene names or symbols, UniProt IDs and direct search in the dbxref table of GO database. Identified gene names or symbols were then searched in the species specific entries of the gene-product tables of GO database. UniProt IDs made use of protein information resource (PIR) which includes protein sequence database (PSD), UniProt, SwissProt, TrEMBL, RefSeq, GenPept, and PDB databases. Gene Ontology analysis helps in specifying all the annotated nodes comprising of GO functional groups. CDS were compared against the COG (Clusters of Orthologous Groups) database for the analysis of phylogenetically widespread domain families. CDS were compared against Pfam database for higher-level groupings of related protein families, known as clans and the identification of domains that occurs within proteins. BLASTX was used against uniprot-swissprot database with cut-off e-value 1e-6 to annotate predicted CDS against protein.

### [9] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.732)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

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
  - Snippet 1 (score: 0.732)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [11] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.730)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [12] MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila
- Authors: Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al.
- Year: 2025
- Venue: Synthetic and Systems Biotechnology
- URL: https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
- DOI: 10.1016/j.synbio.2025.04.001
- PMID: 40276250
- PMCID: 12018684
- Summary: Shifts in metabolic allocation in a glucoamylase hyperproduction strain of M. thermophila are identified, highlighting changes in fatty acid biosynthesis and amino acids biosynthesis pathways, which provide new insights into the underlying phenotypic alterations.
- Evidence snippets:
  - Snippet 1 (score: 0.715)
    > Single-gene search: Gene annotation is essential for biologists to understand a gene's function. MTD's single-gene search interface allows researchers to obtain a comprehensive gene description by entering or selecting a gene ID. The results include sequence information, CAZy family, Pfam domains, GO/KEGG annotations, and phenotype information (Fig. 2D), along with sequence-based predictions such as optimal protein activity temperature, melting temperature (Tm), subcellular localization, and transcription factor scores. To enhance data accessibility, links to external databases such as NCBI, KEGG, FungiDB [4], UniProt, and JGI are also provided, facilitating cross-referencing of gene annotations across various resources.
    > Unlike the static genome, the transcriptome captures dynamic gene expression changes in response to developmental or environmental conditions, establishing a dynamic link between an organism's genome and its physical characteristics [63]. In the single-gene retrieval interface, the expression of the searched gene is visualized in the form of box plots and scatter plots across transcriptome datasets (Fig. 2E). When hovering over any data point, users can view the corresponding experimental details, such as mutant name, sample processing methods, and growth conditions. This interactive feature reveals gene expression responses to environmental factors, allowing researchers to quickly identify experimental conditions of interest and explore the gene's potential roles in diverse biological contexts. Moreover, clicking on the dataset title will direct users to the GEO browser for further detailed descriptions. KEGG Pathway or Gene List Search: In transcriptome studies, researchers typically adopt a "bottom-up" approach: first sequencing all mRNA in a cell, identifying differentially expressed genes between conditions, and then performing GO/KEGG enrichment analysis to interpret functional distributions. MTD, however, offers a complementary "top-down" search strategy, enabling users to examine the expression of genes within a specific KEGG pathway (Fig. 3A) or a user-defined gene set. A unique feature of MTD is its manually curated data categorization system, which organizes sample data with detailed annotations based on experimental conditions.

### [13] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.714)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [14] A haplotype-resolved genome assembly of Malus domestica ‘Red Fuji’
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
  - Snippet 1 (score: 0.710)
    > For the functional annotation of the protein-coding genes, we employed a standardized workflow 30,31 .In summary, the protein sequences of the two haplotype genomes were compared against several protein databases using the DIAMOND program, with an E-value cutoff of 1E-4.The protein databases included the non-redundant protein database (NR), TrEMBL (http://www.uniprot.org/),SwissProt 32 , and the Arabidopsis protein database.The BLAST results from SwissProt, TrEMBL, and the Arabidopsis protein database were loaded into the AHRD (https://github.com/asishallab/AHRD)program to predict concise, informative, and accurate functional descriptions for each gene.
    > Furthermore, the protein sequences were compared against the InterPro database 33 using InterProScan to identify functional protein domains.The BLAST results from the NR database were combined with the identified InterPro protein domains to perform Gene Ontology (GO) annotation using the Blast2GO program 34 , and the GO terms were associated with the annotated protein sequences.To explore the protein-coding genes' connections to pathways, the 'Red Fuji' apple protein sequences were annotated using the online KAAS tool (https://www.genome.jp/tools/kaas/).This annotation provided information about the genes' associations with various metabolic pathways.Additionally, the iTAK software was used to predict transcription factors, transcription regulators, and protein kinases.
    > The protein-coding genes were compared separately with the NR, SwissProt, Arabidopsis protein database, and TrEMBL databases.Each database annotated 95,552, 77,453, 67,243, and 92,132 genes, respectively.A total of 52,073 genes were matched to 2,555 GO terms.Additionally, in the pathway annotation, 32,312 genes were annotated to 143 ko IDs.In the prediction of transcription factors (TFs) and transcription regulators (TRs), a total of 6,283 genes belong to 93 different gene families.Additionally, 3,119 genes were annotated to 127 different protein kinase (PK) families.

### [15] A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi
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
  - Snippet 1 (score: 0.707)
    > In an effort to engage the collective expertise of the scientific community, we have implemented a collaborative wiki (MediaWiki version 1.19.11) for the Mnemiopsis gene complement. The Mnemiopsis Gene Wiki is accessible from the left sidebar of most pages and is searchable either by selecting a Mnemiopsis gene identifier (e.g., ML00011a) from the drop-down menu or by manually entering an identifier in the appropriate search box. Users can also access these pages by clicking on a gene in the 2.2 track of the genome browser. Each record in the Gene Wiki represents a single Mnemiopsis gene and provides the following annotation: nucleotide and protein sequences, coding exonic genomic coordinates, pre-computed BLAST hits from numerous organisms displaying the top hits for each protein, the top non-self BLAST hit to Mnemiopsis, Pfam-A domains, Gene Ontology (GO) functional annotations, human disease genes from Online Mendelian Inheritance in Man (OMIM), and a table of ortholog clusters formed by phylogenetically informed clustering methods [4] (Figure 5). In addition, controlled editable sections have been included that permit (and encourage) the scientific community to provide further gene annotation for isoforms, in situ images, references, and other notes for each gene. Users interested in supplementing our gene model annotation at the Mnemiopsis Gene Wiki pages must first create an account and log in prior to submitting their contributions. In-house subject matter expert data curators are notified by e-mail following the creation of a new user account or an edit to an existing Gene Wiki record. Any content changes or additions to the Gene Wiki are thoroughly evaluated by these data curators and are made public subject to their approval.
    > Pre-compiled BLAST hits are enumerated in tabular form. Each Mnemiopsis protein was compared to the UniProt and NCBI non-redundant protein databases (nr) using BLASTP. The results display the hit number, the accession numbers, E-values, and brief descriptions of the top four hits (lowest E-values). Accession numbers are linked to relevant corresponding entries at UniProt and GenBank.

### [16] Text-mining and information-retrieval services for molecular biology
- Authors: Martin Krallinger, A. Valencia
- Year: 2005
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/558a2745d6e1ac99f77dde88d62566237bd3cfad
- DOI: 10.1186/gb-2005-6-7-224
- PMID: 15998455
- PMCID: 1175978
- Citations: 237
- Influential citations: 1
- Summary: A range of text-mining applications have been developed recently that will improve access to knowledge for biologists and database annotators.
- Evidence snippets:
  - Snippet 1 (score: 0.704)
    > Biological research is name-centered: proteins are referred to in free text by their names or symbols rather than using the unambiguous identifiers provided by annotation databases (such as SwissProt accession numbers [16]). Identifying mentions of proteins and genes unambiguously within free text is a fundamental step for the later extraction of functional attributes of these entities. Unfortunately this is a difficult process, partly because of the complex nature and usage of gene and protein names. Genes and proteins may be referred to in free text in a range of different ways: as full names (for example, porin), as symbols (the Saccharomyces cerevisiae gene POR1), and also through typographical variants (POR-1). Many genes also have several synonyms (such as OMP2 for POR1), or the gene name may be ambiguous [17] and refer to words that also have a different meanings depending on the context (for example, big brain, the full name for the Drosophila melanogaster gene bib, could also be an anatomical description). Furthermore, it has been suggested that errors in gene names might be introduced automatically by certain applications in bioinformatics [18].
    > In the NLP field, the identification of entities in free text is known as named-entity recognition (NER). To identify biological entities such as genes, proteins and drugs automatically and unambiguously within free text, over 50 information-extraction and text-mining tools have recently been implemented, and two community-wide evaluations have been carried out [19,20]. The top left of Figure 1 shows nine existing NER applications for biology that are provided via an online server or are directly downloadable. Note that the average recovery of biological entities from free text by 15 NER tools was 80%, and the results had an accuracy of 80% [21]; these figures are significantly lower than in the case of entities found in documents from fields such as economics, which demonstrates the complex nature of protein names.
    > Proteins and genes are characterized within biological databases through unique identifiers; each identifier is associated with its corresponding protein or nucleotide sequence and functional descriptions.

### [17] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.701)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [18] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.701)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [19] Integrative analysis of next generation sequencing for small non-coding RNAs and transcriptional regulation in Myelodysplastic Syndromes
- Authors: D. Beck, S. Ayers, J. Wen, Miriam Brandl, T. Pham et al.
- Year: 2011
- Venue: BMC Medical Genomics
- URL: https://www.semanticscholar.org/paper/de13a83fb5d84d8eb997c4dec2d73ed4be2efbd8
- DOI: 10.1186/1755-8794-4-19
- PMID: 21342535
- PMCID: 3060843
- Citations: 44
- Influential citations: 3
- Summary: Novel findings are provided that build a basis of further investigations of diagnostic biomarkers, targeted therapies and studies on MDS pathogenesis, and confirmed important regulatory roles for MDS linked miRNAs and TFs.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > The flat files FACTOR and GENE of the commercially available database TRANSFAC v2008_2 [26] were downloaded and parsed into a MySQL database. The FAC-TOR and GENE flat files contain information on transcription factor proteins and genes regulated by transcription factors, respectively. A total of 2362 regulating factors for the human species (Homo Sapiens) were extracted and 70 entries, that did not describe proteins, but other regulatory factors were omitted. A large fraction (about 77 percent) of the remaining 2292 transcription factor proteins were mapped to Uniprot [27], either by external database ID's, or exact matches between protein names. With these accessions the protein coding gene IDs, as well as other information was downloaded automatically via a MATLAB based data retrieval algorithm implemented for this study. The transcript and probeset annotation files for the Affymetrix GeneChip Human Exon 1.0 ST Array were downloaded from the manufacture's website http://www. affymetrix.com and parsed into MySQL tables. Transcript IDs for 98 percent of the human transcription factor coding genes were extracted based on direct matches between gene names.
    > Genes that can potentially be up regulated when the transcription factor protein binds to a specific site in its promoter region are called transcription factor target genes. We extracted all target genes for human transcription factor proteins by joining a number of database tables. This revealed 3296 gene targets for the 2292 transcription factor proteins. We used direct matches between the target gene names, as well as additional entries, to identify corresponding transcripts on the Affymetrix GeneChip. This resulted in matches for 83 percent of the target genes.

### [20] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.698)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
5. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
6. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
7. H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim (2023). FusionPDB: a knowledgebase of human fusion proteins. Nucleic Acids Research. https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
8. Nagaraja Reddy Rama Reddy, Rucha Harishbhai Mehta, Palak Soni, Jayanti Makasana, N. Gajbhiye et al. (2015). Next Generation Sequencing and Transcriptome Analysis Predicts Biosynthetic Pathway of Sennosides from Senna (Cassia angustifolia Vahl.), a Non-Model Plant with Potent Laxative Properties. PLoS ONE. https://www.semanticscholar.org/paper/fec6263b90f9cd765752bdb1be3d162872f2e64e
9. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
10. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
11. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
12. Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al. (2025). MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila. Synthetic and Systems Biotechnology. https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
13. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
14. Haixu Peng, Yating Yi, Jinrong Li, You Qing, Xuyang Zhai et al. (2024). A haplotype-resolved genome assembly of Malus domestica ‘Red Fuji’. Scientific Data. https://www.semanticscholar.org/paper/e5dc0e3046713c6ff2aed20631ab819fffd8b0c0
15. R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al. (2014). A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi. BMC Genomics. https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
16. Martin Krallinger, A. Valencia (2005). Text-mining and information-retrieval services for molecular biology. Genome Biology. https://www.semanticscholar.org/paper/558a2745d6e1ac99f77dde88d62566237bd3cfad
17. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
18. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
19. D. Beck, S. Ayers, J. Wen, Miriam Brandl, T. Pham et al. (2011). Integrative analysis of next generation sequencing for small non-coding RNAs and transcriptional regulation in Myelodysplastic Syndromes. BMC Medical Genomics. https://www.semanticscholar.org/paper/de13a83fb5d84d8eb997c4dec2d73ed4be2efbd8
20. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c