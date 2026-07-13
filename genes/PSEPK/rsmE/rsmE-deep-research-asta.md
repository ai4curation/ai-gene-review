---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T11:45:19.575212'
end_time: '2026-07-10T11:45:24.673969'
duration_seconds: 5.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rsmE
  gene_symbol: rsmE
  uniprot_accession: Q88D43
  protein_description: 'RecName: Full=Ribosomal RNA small subunit methyltransferase
    E {ECO:0000256|ARBA:ARBA00013673, ECO:0000256|PIRNR:PIRNR015601}; EC=2.1.1.193
    {ECO:0000256|ARBA:ARBA00012328, ECO:0000256|PIRNR:PIRNR015601};'
  gene_info: Name=rsmE {ECO:0000313|EMBL:AAN70551.1}; OrderedLocusNames=PP_4985 {ECO:0000313|EMBL:AAN70551.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the RNA methyltransferase RsmE family.
  protein_domains: Alpha/beta_knot_MTases. (IPR029028); PUA-like_sf. (IPR015947);
    RsmE. (IPR006700); RsmE_MTase_dom. (IPR046886); RsmE_PUA-like. (IPR046887)
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
- **UniProt Accession:** Q88D43
- **Protein Description:** RecName: Full=Ribosomal RNA small subunit methyltransferase E {ECO:0000256|ARBA:ARBA00013673, ECO:0000256|PIRNR:PIRNR015601}; EC=2.1.1.193 {ECO:0000256|ARBA:ARBA00012328, ECO:0000256|PIRNR:PIRNR015601};
- **Gene Information:** Name=rsmE {ECO:0000313|EMBL:AAN70551.1}; OrderedLocusNames=PP_4985 {ECO:0000313|EMBL:AAN70551.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the RNA methyltransferase RsmE family.
- **Key Domains:** Alpha/beta_knot_MTases. (IPR029028); PUA-like_sf. (IPR015947); RsmE. (IPR006700); RsmE_MTase_dom. (IPR046886); RsmE_PUA-like. (IPR046887)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rsmE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rsmE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rsmE** (gene ID: rsmE, UniProt: Q88D43) in PSEPK.

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
  - Snippet 1 (score: 0.787)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

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
  - Snippet 1 (score: 0.775)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [3] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.750)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [4] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.746)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

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
  - Snippet 1 (score: 0.743)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [6] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2775
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.737)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [7] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.723)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [8] Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids
- Authors: G. Alama-Bermejo, E. Meyer, S. Atkinson, A. Holzer, Monika M. Wiśniewska et al.
- Year: 2020
- Venue: Genome Biology and Evolution
- URL: https://www.semanticscholar.org/paper/7d5e64908d9bea80accb9389be84679778625620
- DOI: 10.1093/gbe/evaa109
- PMID: 32467979
- PMCID: 7487138
- Citations: 18
- Summary: Host-free transcriptomes of a myxozoan model organism from strains that exhibited different degrees of virulence are developed, as a unique source of data that will foster functional gene analyses and serve as a base for the development of potential therapeutics for efficient control of these parasites.
- Evidence snippets:
  - Snippet 1 (score: 0.717)
    > We chose cell migration genes and proteases/inhibitors as candidate virulence factors, due to their relevance in hostpathogen interactions (e.g., Barragan and Sibley 2002;McKerrow et al. 2006;Bouzid et al. 2013). Given the low amount of functional (GO) annotation in our largest assembly, C. shasta þ NHP (see Results), we used BlastX to search for homologs of genes of interest in two custom concatenated databases that comprised the Cell Migration Knowledge Database (CMKB) which includes proteins, families, and complexes involved in cell migration (http://www.cellmigration. org/index.shtml, last accessed February 5, 2015; $7,600 protein sequences), and the MEROPS database, which consists of a nr library of full-length sequences of peptidases and peptidase inhibitors (http://merops.sanger.ac.uk/, last accessed December 2, 2014; $450,000 sequences; Rawlings et al. 2016). We searched using the longest representatives for each gene in the C. shasta þ NHP assembly (23,418 contigs; IIR-RBT6) then parsed matches (bit score > 100) and posteriorly classified homologs to proteases or motility genes matching the specific databases. We then selected only genes with the same annotation in UniProt (determined using the same standards: no ambiguous terms filtering, bit score > 100) to confirm gene identity. Due to disagreements between annotations (CMKB vs. UniProt, and MEROPS vs. UniProt), we curated gene lists manually, removing genes that matched one or more of the following criteria: 1) no genetic distances available (only available for reference); 2) disagreements between annotations from the different databases, after checking for synonyms or function similarity; 3) annotations that contained terms from UniProt "Uncharacterized protein" and "Predicted protein" (ambiguous terms), and whose identity could not be confirmed; and 4) annotations that contained nonspecific terms, such as "heat shock protein" or "ribosomal protein."

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

### [10] OntoGene in BioCreative II
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
  - Snippet 1 (score: 0.707)
    > It is well known that protein names are highly ambiguous [45,46]. Researchers working in specific subcommunities tend to develop their own nomenclature, resulting in multiple names for the same protein. Acronyms and abbreviations further complicate the picture. Simply being able to recognize a protein name as such is just a starting point. The name needs then to be unambiguously qualified, by referring to an entry in a standard protein database, such as UniProt http:// www.expasy.org/sprot/ [47].
    > In order for that to happen, the disambiguation must occur at two levels: interspecies (to which specific organisms does the protein mention refer?) and intraspecies (within a given organism, which specific protein is meant?). For example, a protein mentioned in text as eIF4E could refer to a large number of different proteins. A search in the Swiss-Prot section of UniProt (the manually curated section) delivers 46 possible matches. However, if the term appears contextually with the mention of a specific organism, like in the sentence 'The Cap-binding protein eIF4E promotes folding of a functional domain of yeast translation initiation factor eIF4G1' (PubMed: 10409688), then it is reasonable to assume that the name refers to a specific organism (yeast), thus restricting the possible matches in UniProt to the following two: EAP1_YEAST (eIF4E-associated protein 1) and IF4E_YEAST (eukaryotic translation initiation factor 4E). For the task of protein annotation, we have adopted a high-recall, low-precision term annotation approach, followed by very strict disambiguation steps, which gradually increase precision (at some expense for recall).
    > UniProt contains for each protein a list of frequently used synonyms, as well as the name and synonyms of its encoding gene. We have built a database that maps the synonyms to the protein identifier. We have further enriched such a list using morpho-syntactic rules that generate variants of the synonyms. Starting from the subset of UniProt delivered by the BioCreative organizers (which contained 228,

### [11] Metadata Standard and Data Exchange Specifications to Describe, Model, and Integrate Complex and Diverse High-Throughput Screening Data from the Library of Integrated Network-based Cellular Signatures (LINCS)
- Authors: U. Vempati, Caty Chung, Christopher Mader, Amar Koleti, Nakul Datar et al.
- Year: 2014
- Venue: Journal of Biomolecular Screening
- URL: https://www.semanticscholar.org/paper/91af493a67a83d599ad00f4da275e8eadd165b5e
- DOI: 10.1177/1087057114522514
- PMID: 24518066
- Citations: 83
- Influential citations: 3
- Summary: The National Institutes of Health Library of Integrated Network-based Cellular Signatures (LINCS) program is generating extensive multidimensional data sets, including biochemical, genome-wide transcriptional, and phenotypic cellular response signatures to a variety of small-molecule and genetic perturbations with the goal of creating a sustainable, widely applicable, and readily accessible systems biology knowledge resource. Integration and analysis of diverse LINCS data sets depend on the a...
- Evidence snippets:
  - Snippet 1 (score: 0.692)
    > Although this is a fairly obvious requirement, it is not trivial to implement because a protein reagent expressed recombinantly is typically not the exact same entity or in the same state as its corresponding assay participant in a living cell (e.g., kinase domain binding assay vs. corresponding kinase occurring in a specific cell line used for a growth inhibition assay). In this first version of metadata standards, we take a rudimentary approach. We use the UniProt accession and approved Gene symbol (NCBI Gene) and accession number to identify and reference proteins and their coding genes, respectively. Although we recognize limitations, for the purpose of our current simple use cases, this is sufficient. Linking protein and gene identifiers in addition is relevant to integrate RNAi reagent gene targets (see below). The recommended explicit fields for proteins include a standardized name, both for the protein and the gene that encodes it; source of protein (e.g., chemically synthesized, purified from natural source, recombinantly expressed); protein modifications (e.g., mutations, posttranslational modification); protein purity; subunit information for components of a protein complex; and isoform information (derived from either alternative promoter usage, alternative splicing, alternative translation initiation, or frame shifting). We are currently working on a formal description of proteins that will allow ambiguity (more-or less-specific definition of proteins), because in some cases, the exact entity and state of a protein reagent or model system participant is not definitively known (full length, functional domain, exact sequence, mutation, phosphorylation state, etc.).
    > Inhibitory RNAs (siRNA, shRNA). RNA interference is a standard methodology to transiently knock down gene expression in living cells. This can be achieved using different types of small RNA molecules, including siRNA, shRNA, and miRNA. Information that is relevant to identify and describe these perturbations include probe ID, name, source/provider, target gene symbol and accession number, sequence of the probe, and modifications to the probe (e.g., chemical modification) if any are specified.
    > Antibody Reagents.

### [12] A high-quality chromosome-level genome assembly of the Chinese medaka Oryzias sinensis
- Authors: Zhongdian Dong, Jiangman Wang, Guozhu Chen, Yusong Guo, Na Zhao et al.
- Year: 2024
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/22e6bac57aff18bdef6ecc2240c145ad3758b9ee
- DOI: 10.1038/s41597-024-03173-8
- PMID: 38548787
- PMCID: 10978949
- Citations: 5
- Summary: A high-quality chromosome-level genome assembly of O. sinensis is generated using single-tube long fragment read (stLFR) reads, Nanopore long-reads, and Hi-C sequencing data and ATAC-seq is used to uncover chromosome transposase-accessibility as well as related genome area function enrichment for Oryzias sinensis.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > From inner to outer circles: Density of genes with 500 kbp windows, ranging from 0 to 50; Density of TE with 500 kbp windows, ranging from 0 to 600; Density of TRF with 500 kbp windows, ranging from 0 to 450; Distributions of GC content with 500 kbp windows. (B) Hi-C interaction heat map and scatter plot of genome assembly GC content and sequencing depth.
    > Trinity, before PASA was used to get a gene model. Finally, all evidence was merged to form a consensus gene structure annotation result using GLEAN 30 . A total of 22,461 protein-coding genes were successfully predicted. BUSCO 19 assessments reached 94.6% using the actinopterygii_odb9 database, indicating relatively complete gene annotation coverage (Table 3).
    > All predicted genes were compared with public biological function databases including KEGG 31 , Swissprot 32 , and TrEMBL 33 (https://www.uniprot.org/statistics/TrEMBL) using BLASTp 34 with an E-value cutoff of 1e-5 for functional annotation. Interpro was applied to provide functional analysis of protein sequences by classifying them into families and predicting the presence of domains and important sites, followed by Gene Ontology annotation [35][36][37] . Overall, 22,162 protein-coding genes (98.67%) were successfully functionally annotated (Table 5).
    > Non-coding RNAs (ncRNAs) are an important part of genome annotation as they can be active in transcriptional and translational regulation of gene expression as well as in the modulation of protein function 38 . Since ribosomal RNA (rRNA) was highly conservative, vertebrate rRNA data was used as a reference to map to the draft genome using BLASTn with an E-value of 1e-5. For the discovery of transfer RNA (tRNA), tRNAscan-SE v1.3.1 was applied with eukaryotic parameters according to the characteristics of tRNA 39 . Rfam database was applied to find microRNAs (miRNA) and small nuclear RNA (snRNA) 40,41 .

### [13] Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes
- Authors: Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer
- Year: 2023
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
- DOI: 10.1093/nar/gkad385
- PMID: 37216585
- PMCID: 10320097
- Citations: 8
- Summary: The new implementation of the CUPP-webserver, https://cupp.info/, now includes all published fungal and algal genomes from the Joint Genome Institute (JGI), genome resources My coCosm and PhycoCosm, dynamically subdivided into motif groups of CAZymes, allowing users to browse the JGI portals for specific predicted functions or specific protein families from genome sequences.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > To inspect the transcriptomics result of individual genes, proteins originating from JGI have a hyperlink to a summary page which links to a 'Genome browser' page that displays the predicted gene splicing, including which regions have RNA support (Figure 1 D).
    > Hence, in the protein specific site in the JGI w e bsite under 'To Genome Browser', the current protein (GeneCatalog) can be seen together with se v eral other alternati v e predictions of the gene splicing, which is essential to have correct, for the protein to function naturally (Figure 2 ).
    > As the RNA coverage supports the exon / intron splicing, it is possible to infer whether a particular gene, in this case Table 1. Comparison between the dbCAN webserver, the eggNOG webserver for both family and functional annotation of CAZymes and the updated CUPP-w e bserver using the recommended significance cut-off at 5. The column 'CAZy -All characterized' encompasses all 10784 characterized proteins in the CAZy database used for the training, whereas the 'CAZy -Newly characterized '   a gene such as the one selected in Figure 2 , is more likely to work after heterologous gene expression.
    > To further improve the enzyme selection, all NCBI Genbank accessions were mapped to Uniprot ID to link to the specific Uniprot accession page including the predicted Al-phaFold structures, Go annotations and InterPro annotations and more ( 19 ).

### [14] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
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
  - Snippet 1 (score: 0.686)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

### [15] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
- Authors: E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al.
- Year: 2016
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
- DOI: 10.1186/s13059-016-1014-0
- Summary: The results provide the most complete comparative genomics and experimental analysis of mRBPs in P. falciparum and identify and characterize mRNA-binding proteins (mRBPs) that encompass a relatively large proportion of the parasite proteome as compared to other eukaryotes.
- Evidence snippets:
  - Snippet 1 (score: 0.686)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

### [16] A high-quality genome for the slender anole (Anolis apletophallus): an emerging model for field studies of tropical ecology and evolution
- Authors: Renata M. Pirani, Carlos F Arias, Kristin Charles, Albert K. Chung, J. D. Curlis et al.
- Year: 2023
- Venue: G3: Genes|Genomes|Genetics
- URL: https://www.semanticscholar.org/paper/3856bf1b43601b80987242d1858d505dd3167fd1
- DOI: 10.1093/g3journal/jkad248
- PMID: 37875105
- PMCID: 10755174
- Citations: 6
- Influential citations: 1
- Summary: This new reference genome for the slender anole is one of the most complete genomes of any anole assembled to date and should facilitate deeper studies of slender anole evolution, as well as broader scale comparative genomic studies of both mainland and island species.
- Evidence snippets:
  - Snippet 1 (score: 0.678)
    > MAKER, SNAP, and AUGUSTUS (with intron-exon boundary hints provided from RNA-seq) were then used to predict genes in the repeat-masked reference genome. To help guide the prediction process, Swiss-Prot peptide sequences from the UniProt database were downloaded and used in conjunction with the protein sequences from A. carolinensis, L. agilis, and Z. vivipara to generate peptide evidence in the MAKER pipeline. Only genes that were predicted by both SNAP and AUGUSTUS were retained in the final gene sets. To assess the quality of gene prediction, Annotation Edit Distance (AED) scores were generated for each of the predicted genes as part of the MAKER pipeline. Fourth, we curated the genome manually, during which we verified and corrected a preselected list of genes. We preselected genes that are biologically relevant for our focal species and our current research, such as arginyl-tRNA synthetase (RARS), heat shock protein family (HSP40), heat shock protein family A (HSP70), and the heat shock protein 90 (HSP90). Lastly, genes were further characterized for their putative function by performing a BLAST search of the peptide sequences against the UniProt database. tRNA were predicted using the software tRNAscan-SE (version 2.05).

### [17] Deltamethrin Selection Drives Transcriptomic Changes in Detoxification, Immune, and Cuticle Genes in Aedes aegypti
- Authors: Y. Contreras-Perera, L. Mackenzie-Impoinvil, Dieunel Derilus, Audrey Lenhart, I. Rodríguez-Sánchez et al.
- Year: 2025
- Venue: Tropical Medicine and Infectious Disease
- URL: https://www.semanticscholar.org/paper/21e5f9022b6c14afa8f193ff59151db6228bc141
- DOI: 10.3390/tropicalmed10060171
- PMID: 40559738
- PMCID: 12197768
- Citations: 5
- Summary: The overexpression of immune- and stress-related genes, including the RNA helicase MOV-10, indicates that insecticide selection may trigger broader physiological responses and highlight complex, multi-pathway transcriptomic changes associated with resistance development in Ae.
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > The AegL5 gene set contains over 19,804 predicted genes (14,718 protein-coding genes, 5086 non-protein-coding genes, and 382 pseudogenes). However, functional annotation is available for only 6319, and gene ontology (GO) annotation terms are assigned to 11,097 of the protein-coding genes. To enhance the interpretation of the data, the computational annotation of the AegL5 set was performed using Blast2GO (see Methods). This analysis assigned putative functional descriptions to 13,322 and GO terms to 11,680 of the protein-coding genes. All the annotation results from both Vector-Base and Blast2GO are provided in File S5.
    > Gene ontology enrichment analysis (GOEA) was performed on the DE genes (up and downregulated, separately) from each F S4 vs. F S0 (3 in total). The significantly enriched GO terms, including biological process, molecular function, and cellular component categories, are reported in File S6. GO molecular function terms that were significantly enriched in at least two out of the three comparisons are summarized in Figure S1.
    > For the upregulated genes, GO molecular function terms associated with binding activities (ATP, nucleic acid, RNA, Adenyl ribonucleotide/nucleotide small molecule, organic cyclic compounds), transferase activity (methyl, one-carbon group), helicase, and ATP-dependent activities were significantly enriched, suggesting the potential role of these key molecular functions following insecticide selection. Of note, GO terms associated with methyltransferase activity were significantly enriched in the upregulated genes. Among these, tRNA (cytosine34-C5)-methyltransferase (AAEL013968) was consistently detected among the top 10 DE genes from all three F S4 vs. F S0 comparisons. This may suggest the involvement of the RNA methylation process in response to insecticide selection; however, direct evidence for DNA or RNA methylation in Ae. aegypti under deltamethrin exposure is currently lacking.

### [18] Telomere-to-telomere genome assembly of asparaginase-producing Trichoderma simmonsii
- Authors: Dawoon Chung, Y. Kwon, Youngik Yang
- Year: 2021
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/c30991da2937d0cda82af9a6e04462da0aaf12be
- DOI: 10.1186/s12864-021-08162-4
- PMID: 34789157
- PMCID: 8600724
- Citations: 19
- Influential citations: 1
- Summary: The genome and transcriptome of T. simmonsii GH-Sj1 established in the current work represent valuable resources for future comparative studies on fungal genomes and asparaginase production.
- Evidence snippets:
  - Snippet 1 (score: 0.675)
    > Using the funannotate update command, UTRs were added to gene models. Various functional features were assigned, such as Phobius (v1.01) [75] results, anti-SMASH (v5) [32], eggnog-mapper (v2.0.1b) [76], Inter-ProScan (v5.50-84.0) [77], HMMer (v3.3) [78] search of PFAM (v33.1) [79], CAZymes (dbCAN v8.0) [31] using HMMer, and the Diamond blastp search of MEROPS (v12.0) [35].
    > Apart from the funannotate pipeline, protein functions (i.e., product field) were revised in the following manner. Protein sequences were aligned with BLASTP against all dikarya protein sequences in UniProt DB (v2021_03). Matching sequences were kept when the E-value was <= 1.0e-10, percent identity > = 50%, and query coverage in alignment > = 50%. Protein function was taken from the top hit. When more than one protein sequences from the same gene had a different functional description, we manually corrected them to have same functional description.

### [19] ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance
- Authors: FuGuo Liu, T. Lai, Wenxia Xu, Guodong Li
- Year: 2026
- Venue: PLOS One
- URL: https://www.semanticscholar.org/paper/7d7965ec223f5715675839cb57efdc776d25e216
- DOI: 10.1371/journal.pone.0349393
- PMID: 42234710
- PMCID: 13232823
- Citations: 1
- Summary: ViralMultiNet is a structure-aware multimodal framework that integrates multi-scale k-mer encodings with functional semantic embeddings derived from UniProt annotations that offers a scalable, interpretable solution for viral protein function prediction.
- Evidence snippets:
  - Snippet 1 (score: 0.675)
    > To reduce redundancy while preserving sequence diversity, the 235,441 validated ORFs were subjected to two-stage clustering using VSEARCH v2.21.1: first at 90% sequence identity, then refined at 95% identity. Cluster representatives were aligned against UniProt/Swiss-Prot (release 2024_01) using DIAMOND v2.0.15 in sensitive mode (--sensitive). The initial alignment yielded 62,689 ORFs with putative UniProt matches. For each match, protein names, functional descriptions, and Gene Ontology (GO) terms were extracted for downstream label assignment.
    > 2.1.4. Functional labeling. Functional labels (Enzymatic, Structural, Transport, Other) were assigned to the 62,689 UniProt-mapped ORFs using hierarchical keyword matching against a curated dictionary of 847 functional terms derived from UniProt protein descriptions and Gene Ontology annotations. The classification hierarchy prioritized primary molecular functions:
    > • Enzymatic: Proteins with catalytic activity (GO:0003824), including polymerases, proteases, methyltransferases, and helicases
    > • Structural: Proteins involved in virion assembly and structural maintenance (GO:0019012), including spike, envelope, membrane, and nucleocapsid proteins
    > • Transport: Proteins mediating membrane transport and ion channels (GO:0006810, GO:0015267)
    > • Other: All remaining ORFs, including regulatory proteins, accessory factors, and hypothetical proteins ORFs with ambiguous or conflicting annotations (e.g., proteins with both enzymatic and structural roles) were manually reviewed by two independent annotators, achieving 94.2% inter-annotator agreement (Cohen's κ = 0.92). After removing ambiguous cases, this resulted in 53,575 unique labeled ORF sequences with unambiguous functional assignments.The 'Other' category encompasses a functionally heterogeneous set of accessory proteins with distinct biological roles, as summarized in Table 1 Variants were filtered to retain only those with ≥2% sequence divergence from their corresponding base ORF to ensure meaningful diversity while maintaining functional annotation consistency.

### [20] Phylogenomics of 10,575 genomes reveals evolutionary proximity between domains Bacteria and Archaea
- Authors: Qiyun Zhu, U. Mai, W. Pfeiffer, Stefan Janssen, F. Asnicar et al.
- Year: 2019
- Venue: Nature Communications
- URL: https://www.semanticscholar.org/paper/7e3866b2d5d92fc28f91181a5393610760cba94d
- DOI: 10.1038/s41467-019-13443-4
- PMID: 31792218
- PMCID: 6889312
- Citations: 299
- Influential citations: 22
- Summary: A reference phylogeny of 10,575 evenly-sampled bacterial and archaeal genomes, based on a comprehensive set of 381 markers, is built, providing an updated view of domain-level relationships between Archaea and Bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > Each genome was given a unique identifier, which was derived from the NCBI accession of the corresponding assembly, but without version number. For example, a genome with assembly accession "GCF_000123456.1" was identified as "G000123456" in this study. In cases when the same genome was present in both GenBank (accession starting with "GCA_") and RefSeq (accession starting with "GCF_"), only the RefSeq version was kept.
    > Annotation and classification of marker genes. The functional annotation of the 400 PhyloPhlAn marker genes 25 was performed by aligning the protein sequences of the 400 marker genes (inferred from 2887 bacterial and archeal genomes as described in Segata et al. 25 ) against the UniRef50 database (March 2018 release) using BLASTp. The best hit for each gene was taken and queried against the UniProt database for gene and protein names. To categorize genes by function, the UniProt entries were translated into Gene Ontology (GO) terms 40 with the "sub-set_prokaryote" tag (March 2018 release). Because not all UniProt entries have corresponding GO terms, manual curation was involved to pick the most appropriate GO terms for those cases by examining the BLAST hit table. GO terms were further translated into GO slim terms to obtain higher-level functional categories.
    > Note that this analysis is independent from the phylogenetic analysis of the current genome data set, and the result can be used as a reference for PhyloPhlAn users.
    > Analyses of genome sequences and identification of marker genes. The DNA sequences of the 86,200 bacterial and archaeal genomes were subjected to the following analyses:
    > 1. The quality scores for DNA, protein, tRNA, and rRNA were calculated following Land et al. 41 . 2. A MinHash sketch was built for each genome using Mash 1.1.1 42 , with default settings (sketch size = 1000, k-mer size = 21), based on which a pairwise distance matrix was built for the entire genome pool. In brief, MinHash is a k-mer hashing technique that enables the quantification of genome-to-genome distance.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
5. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
6. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
7. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
8. G. Alama-Bermejo, E. Meyer, S. Atkinson, A. Holzer, Monika M. Wiśniewska et al. (2020). Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids. Genome Biology and Evolution. https://www.semanticscholar.org/paper/7d5e64908d9bea80accb9389be84679778625620
9. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
10. Fabio Rinaldi, T. Kappeler, K. Kaljurand, Gerold Schneider, Manfred Klenner et al. (2007). OntoGene in BioCreative II. Genome Biology. https://www.semanticscholar.org/paper/ffcbf659129388203ce458ce1b25e5449e9594e7
11. U. Vempati, Caty Chung, Christopher Mader, Amar Koleti, Nakul Datar et al. (2014). Metadata Standard and Data Exchange Specifications to Describe, Model, and Integrate Complex and Diverse High-Throughput Screening Data from the Library of Integrated Network-based Cellular Signatures (LINCS). Journal of Biomolecular Screening. https://www.semanticscholar.org/paper/91af493a67a83d599ad00f4da275e8eadd165b5e
12. Zhongdian Dong, Jiangman Wang, Guozhu Chen, Yusong Guo, Na Zhao et al. (2024). A high-quality chromosome-level genome assembly of the Chinese medaka Oryzias sinensis. Scientific Data. https://www.semanticscholar.org/paper/22e6bac57aff18bdef6ecc2240c145ad3758b9ee
13. Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer (2023). Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes. Nucleic Acids Research. https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
14. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/f3eda16f7a2760619a7727b38fc2fc6738858040
15. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
16. Renata M. Pirani, Carlos F Arias, Kristin Charles, Albert K. Chung, J. D. Curlis et al. (2023). A high-quality genome for the slender anole (Anolis apletophallus): an emerging model for field studies of tropical ecology and evolution. G3: Genes|Genomes|Genetics. https://www.semanticscholar.org/paper/3856bf1b43601b80987242d1858d505dd3167fd1
17. Y. Contreras-Perera, L. Mackenzie-Impoinvil, Dieunel Derilus, Audrey Lenhart, I. Rodríguez-Sánchez et al. (2025). Deltamethrin Selection Drives Transcriptomic Changes in Detoxification, Immune, and Cuticle Genes in Aedes aegypti. Tropical Medicine and Infectious Disease. https://www.semanticscholar.org/paper/21e5f9022b6c14afa8f193ff59151db6228bc141
18. Dawoon Chung, Y. Kwon, Youngik Yang (2021). Telomere-to-telomere genome assembly of asparaginase-producing Trichoderma simmonsii. BMC Genomics. https://www.semanticscholar.org/paper/c30991da2937d0cda82af9a6e04462da0aaf12be
19. FuGuo Liu, T. Lai, Wenxia Xu, Guodong Li (2026). ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance. PLOS One. https://www.semanticscholar.org/paper/7d7965ec223f5715675839cb57efdc776d25e216
20. Qiyun Zhu, U. Mai, W. Pfeiffer, Stefan Janssen, F. Asnicar et al. (2019). Phylogenomics of 10,575 genomes reveals evolutionary proximity between domains Bacteria and Archaea. Nature Communications. https://www.semanticscholar.org/paper/7e3866b2d5d92fc28f91181a5393610760cba94d