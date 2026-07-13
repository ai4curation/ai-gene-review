---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T08:45:42.981732'
end_time: '2026-07-08T08:45:50.305289'
duration_seconds: 7.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cobI
  gene_symbol: cobI
  uniprot_accession: Q88DJ8
  protein_description: 'RecName: Full=Precorrin-2 C(20)-methyltransferase {ECO:0000256|PIRNR:PIRNR036427};
    EC=2.1.1.130 {ECO:0000256|PIRNR:PIRNR036427};'
  gene_info: Name=cobI {ECO:0000313|EMBL:AAN70396.1}; OrderedLocusNames=PP_4827 {ECO:0000313|EMBL:AAN70396.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the precorrin methyltransferase family.
  protein_domains: 4pyrrol_Mease. (IPR000878); 4pyrrol_Methylase_sf. (IPR035996);
    4pyrrole_Mease_sub1. (IPR014777); 4pyrrole_Mease_sub2. (IPR014776); CobI/CbiL.
    (IPR012382)
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
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88DJ8
- **Protein Description:** RecName: Full=Precorrin-2 C(20)-methyltransferase {ECO:0000256|PIRNR:PIRNR036427}; EC=2.1.1.130 {ECO:0000256|PIRNR:PIRNR036427};
- **Gene Information:** Name=cobI {ECO:0000313|EMBL:AAN70396.1}; OrderedLocusNames=PP_4827 {ECO:0000313|EMBL:AAN70396.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the precorrin methyltransferase family.
- **Key Domains:** 4pyrrol_Mease. (IPR000878); 4pyrrol_Methylase_sf. (IPR035996); 4pyrrole_Mease_sub1. (IPR014777); 4pyrrole_Mease_sub2. (IPR014776); CobI/CbiL. (IPR012382)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cobI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cobI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cobI** (gene ID: cobI, UniProt: Q88DJ8) in PSEPK.

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

- Papers retrieved: 17
- Snippets retrieved: 20

## Relevant Papers

### [1] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.775)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

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
  - Snippet 1 (score: 0.763)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.
  - Snippet 2 (score: 0.694)
    > UniProt data were obtained from the UniProt website. For this purpose, a list of Ensids contained in Avimm was prepared. With this list, the UniProt web interface [46] was queried, and the resulting data were downloaded filtered by the following columns: "Entry (ID)", "Entry name", "Status (reviewed/unreviewed)", "Protein names", "Organism", "Gene names (primary)", "Gene names (synonym)", "Length", "Sequence", "Your list". As an initial step, only Entry IDs (UniProtKBs) were loaded into Avimm.
    > For the import of the B10K data, all gene symbols found in Avimm (including synonyms) were used. For each of these symbols, it was checked whether the gene symbol was found in the B10K genomes' annotations. If the gene symbol was found, the B10K ID (Unigene; B10K-internal identifier and not to be confused with NCBI's Unigene) was extracted and imported into Avimm.
    > To fill the feature tables, all obtained accession numbers from Ensembl, UniProt and B10K were then used to extract transcript information, amino acid sequences and nucleotide sequences, respectively, which were subsequently imported into Avimm (Fig. 3). Data were imported via a stored procedure (function in the database) which performs consistency checks before importing data.
    > Synonyms of gene symbols were handled in the following way: The primary gene symbol used in Ensembl was stored as a canonical name in Avimm and identified by a unique gene identifier (gene_id). The synonyms found in Ensembl were also imported into Avimm. Each gene symbol (primary or synonym) received an additional unique Fig. 3 Flow chart, loading of Avimm. Uncoloured boxes show preparatory steps. Yellow boxes describe imports into core tables and green boxes imports into feature tables. The initial set of immune genes in chicken is derived from "biological process/immune system process" in AmiGo 2 filtered for chicken.

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
  - Snippet 1 (score: 0.746)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

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
  - Snippet 1 (score: 0.740)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [5] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.722)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [6] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
- Authors: P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
- DOI: 10.1093/nar/gkr1122
- PMID: 22135298
- PMCID: 3245126
- Citations: 1605
- Influential citations: 155
- Summary: PhosphoSitePlus (http://www.phosphosite.org) is an open, comprehensive, manually curated and interactive resource for studying experimentally observed post-translational modifications, primarily of human and mouse proteins. It encompasses 1 30 000 non-redundant modification sites, primarily phosphorylation, ubiquitinylation and acetylation. The interface is designed for clarity and ease of navigation. From the home page, users can launch simple or complex searches and browse high-throughput d...
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [7] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.711)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [8] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.706)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [9] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.699)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [10] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.696)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [11] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.692)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

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
  - Snippet 1 (score: 0.687)
    > Gene nomenclature contains current official symbols and various numbers of synonyms, which pose a challenge to integrating genomic data and increase the probability that different genes share the same symbol. Therefore, we retrieved identifiers assigned to all protein-coding genes in human, mouse, rat and pig genomes that are available in the Ensembl genome browser (release 113) to assess the number of genes, compare species and identify ambiguous symbols. Results: Our analysis revealed that the total number of symbols, both official symbols and synonyms, used to identify protein-coding genes ranges from 16,600 in pigs to 64,580 in mice. Furthermore, the gene nomenclature is not complete because there are also genes without an assigned symbol, which indicates gaps in understanding protein-coding genes, especially in pigs. We also found a large number of gene symbols that map to more than one gene. These symbols might complicate the identification of about 10% of rat and mouse genes and 18% of human protein-coding genes. A simple solution for this problem is the usage of stable gene IDs assigned by scientific institutions and committees (Ensembl, NCBI, RGD, HGNC and VGNC) provided that the genomic information associated with these IDs is retrieved directly from proprietary databases containing the most accurate data. Finally, although gene symbols may pose a problem with unequivocal identification of genes, there are instances when no other identifiers are available in the literature. Therefore, we have developed an R script performing search of the Ensembl database and integrating data to provide a single list of updated symbols with annotation about their ambiguity. Conclusions: Gene symbols are not always reliable and should be reported together with stable IDs to enable unequivocal identification of genes. Therefore, data containing only gene symbols should be used cautiously to avoid misidentification of genes. A solution for this problem is our R script REgeness that performs a gene symbol update to current official versions combined with identification of ambiguous symbols and retrieval of other IDs from the Ensembl database.
  - Snippet 2 (score: 0.686)
    > The study provides a detailed overview of Ensembl protein-coding genes and explains relationships between various gene identifiers assigned by Ensembl, NCBI and specialized committees such as MGI, RGD, HGNC and VGNC (Table 2). The most important finding is that a large number of gene symbols in the most frequently studied species, laboratory rodents and humans, can map to more than one gene, either via the official gene symbol or via a synonym (Fig. 4). Symbols that map to more than one gene may lead to confusion in 10% of rat and mouse genes and 18% of human genes, as indicated by the estimate based on the protein-coding genes in the Ensembl database (Fig. 4).
    > Our results also indicated that the impact of the symbol ambiguity is even larger after inclusion of other types of genes. Therefore, it constitutes much more severe problem than previously reported transformations of some gene symbols caused by Excel [1][2][3][4]. The misidentifications caused by symbol ambiguity are most likely in case of literature data retrieved from older studies using past versions of gene nomenclature with a large number of obsolete symbols. A simple solution for this problem is to use stable gene IDs (Table 2) for unequivocal identification of genes. Gene symbols derived from abbreviated full gene names are convenient because they convey functional meaning and can be easily memorized while the stable IDs enable disambiguation of gene nomenclature. Therefore, reporting both gene symbols and stable IDs is a best solution combining advantages of different naming systems.
    > It is important, however, to retrieve genomic information associated with gene identifiers directly from proprietary databases hosted by organizations responsible for the assignment of these IDs. Such proprietary databases contain the most accurate data that are not affected by a delayed exchange of information between databases due to different time schedules of data updates. Furthermore, genomic databases are not fully compatible due to differences in genome annotation caused by the usage of different raw sequence data, different methodology and unusual complexity of some loci that cannot be easily fitted in the canonical view of a gene [36]. The existence of such discrepancies is another reason for using proprietary databases for each type of gene identifiers (Table 2).
  - Snippet 3 (score: 0.675)
    > In the mouse, rat and human genomes, there are approximately twice as many synonyms (aliases) as official symbols. This large number of obsolete gene symbols leads to the problem with unequivocal identification of genes in the literature data because some synonyms can be attributed to more than one current official symbol of protein-coding genes. The ambiguity of symbols may lead to misidentification of 10% of rodent genes and even 18% of human protein-coding genes. Such misidentifications are most likely in case of literature data retrieved from older studies using past versions of gene nomenclature with a large number of obsolete symbols. A simple solution for this problem is usage of stable gene IDs (Table 2) for the unequivocal identification of genes, provided that the genomic information associated with these IDs is retrieved directly from proprietary databases containing the most accurate data. The usage of stable identifiers is important not only for accurate interpretation of literature data but also for currently published datasets because neither the annotation of genomes nor the understanding of gene function are complete.
    > This incompleteness means that official gene symbols will change over time. Data based only on gene symbols should be used cautiously to avoid misidentification of genes. A solution for this problem is our R script that updates gene symbols and provides annotation about their unique or ambiguous character.

### [13] The Protein Naming Utility: a rules database for protein nomenclature
- Authors: Johannes Goll, R. Montgomery, L. Brinkac, S. Schobel, D. Harkins et al.
- Year: 2009
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/dad2c69d04a5a3abdeda129612d52a7849531c09
- DOI: 10.1093/nar/gkp958
- PMID: 20007151
- PMCID: 2808875
- Citations: 8
- Summary: The Protein Naming Utility (PNU) is a web-based database for storing and applying naming rules to identify and correct syntactically incorrect protein names, or to replace synonyms with their preferred name.
- Evidence snippets:
  - Snippet 1 (score: 0.687)
    > During the annotation phase of a typical modern genomics project, functional names are assigned to identified genes and proteins in an automated or semiautomated fashion. Ideally, before such names are submitted to public sequence databases, they should be manually reviewed by experts to ensure that they are consistent, syntactically correct and unambiguous. However, with the scale of genomic data produced by next-generation sequencing technology and with increasingly automated functional annotation processes, the manual correction of names is no longer feasible. This issue is further complicated by the prevalence of ambiguous names resulting from the lack of interspecies naming conventions (1). New proteins are often named based on homology to existing proteins and many existing proteins have syntactically incorrect or ambiguous names, producing transitive annotation errors. Consequently, poor-quality names have proliferated in both public databases and the scientific literature.
    > The need for consistent and unambiguous names has led to the development of a number of conventions for naming genes and proteins [UniProt protein nomenclature (2), HUGO human gene name nomenclature (3) and various other model organism databases (4)(5)(6)(7)]. In addition, the biological text mining community has created dictionaries to resolve gene/protein synonyms to improve the identification of genes and proteins in scientific articles (1,8).
    > The Broad Institute has developed BioNames, a tool to resolve these difficulties using collections of hard-coded regular expressions (https://sourceforge.net/projects/ microbiomeutil). Here, we present our solution to this problem in the form of the Protein Naming Utility (PNU), a web-based database to store and apply customizable sets of naming rules to correct and standardize gene and protein names within an annotated genome or metagenome. The database provides an intuitive web interface that allows users to create and maintain their own naming rules and organize these rules in projects that can be shared with the community.

### [14] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
- Authors: Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al.
- Year: 2025
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
- DOI: 10.1093/nar/gkaf1206
- PMID: 41206768
- PMCID: 12807602
- Citations: 2
- Summary: The new RM2Target v2.0 will serve as a foundational resource for exploring RNA epitranscriptomic regulation, enabling investigations into cross-talk among modifications, underlying molecular mechanisms, and disease connections, thereby facilitating both basic research and translational applications in RNA epigenetics.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

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
  - Snippet 1 (score: 0.682)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [16] Antibodies to biotin enable large-scale detection of biotinylation sites on proteins
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
  - Snippet 1 (score: 0.680)
    > All human IDs used for data annotation were downloaded from Uniprot 20 FTP (URL: ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledge-base/ idmapping/by_organism/, Version: 10/03/2016). The resulting data provided 133,996 unique identifications, which were in turn used to query the Uniprot database. This search returned HHMI Author Manuscript HHMI Author Manuscript HHMI Author Manuscript 109,961 records (including reviewed and unreviewed) along with their functional and structural annotations, including gene ontology features. The annotation table was used to search for mitochondrial evidence associated with a given Uniprot identification in our proximity-labeling anti-biotin-enriched data set by using a string match algorithm. A given protein was annotated as having mitochondrial evidence if any of the following were true: (i) the string 'mitoch' matched the above UniProt annotation table when queried by either gene name or accession number. (ii) The protein showed mitochondrial evidence from a list of mitochondrial proteins which was the same as our previous study (Rhee et al. 11 ) and a precursor to MitoCarta2.0 catalog 28 . (iii) The protein was present in the original mitochondrial true positive list used Rhee et al. 11 . Thebiotinylated peptide data were filtered such that reverse hits, nonhuman contaminants, nonfully localized biotinylation sites, sites identified in the SILAC light state, and redundant biotin site entries were removed. From this list, transmembrane proteins were annotated using the following criteria: (i) the UniProt transmembrane annotation contains the string "TRANSMEM" when matched by either gene name or accession number and/or (ii) evidence from of transmembrane domains after running the precursor MitoCarta2.0 catalog through TMHMM 29 . The UniProt topological domain annotation contained the string "TOPO" when matched by either gene name or accession number.

### [17] Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale
- Authors: P. Kramer, Jack Treml
- Year: 2022
- Venue: Midwestern Journal of Undergraduate Sciences
- URL: https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27
- DOI: 10.17161/mjusc.v1i1.18565
- Summary: The following is a walkthrough of a project designed to overcome the lack of sense for proteins as real objects.
- Evidence snippets:
  - Snippet 1 (score: 0.680)
    > i. Click "See more" to view a bar chart containing data on where in the body's tissues the gene is expressed (as determined by RNA sequencing). Save and include this bar chart as the deliverable for this step.
    > II. Universal Protein Research Knowledgebase (UniProtKB) 8 6. UniProt Entry Number
    > i. Follow the UniProt link in the Resources then search for the protein using the NCBI Gene ID ii. Carefully select the result that best matches the gene and organism of interest by clicking on the blue entry number. iii. This page will be used later to gather further details about the protein.
    > III. RCSB Protein Data Bank (PDB) 9 7. RCSB PDB Solved Structure Identifi er i. Follow the RCSB PDB link in the Resources and search for the protein by either the common name or the NCBI Gene ID, making sure to select the organism of interest on the left. ii. You must ensure that your chosen protein has an existing solved structure in this data bank in order to do a mutational analysis in later parts of this exercise.
    > IV. NCBI GenBank 10 8. AA Protein Sequence i. From the NCBI Gene page, go to the "Genomic regions, transcripts, and products" section and then click "GenBank" on the right. Scroll down to the fi rst Coding Sequence "CDS" section and look directly after "/translation=" for the full protein sequence. ii. Sequence needs to be in FASTA Format consisting of '>' followed by a simple name, a return, and then the sequence in one continuous line of text. See "FASTA Formatting" link in Resources.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
5. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
6. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
7. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
8. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
9. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
10. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
11. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
12. Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała (2025). Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser. BMC Genomics. https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
13. Johannes Goll, R. Montgomery, L. Brinkac, S. Schobel, D. Harkins et al. (2009). The Protein Naming Utility: a rules database for protein nomenclature. Nucleic Acids Research. https://www.semanticscholar.org/paper/dad2c69d04a5a3abdeda129612d52a7849531c09
14. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
15. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
16. N. Udeshi, Kayvon Pedram, Tanya Svinkina, Shaunt Fereshetian, S. Myers et al. (2017). Antibodies to biotin enable large-scale detection of biotinylation sites on proteins. Nature methods. https://www.semanticscholar.org/paper/f9e4f461ca61f4399a95875ea96fb075fa959901
17. P. Kramer, Jack Treml (2022). Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale. Midwestern Journal of Undergraduate Sciences. https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27