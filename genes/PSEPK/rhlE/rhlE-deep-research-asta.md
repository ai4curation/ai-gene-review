---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T03:20:08.650935'
end_time: '2026-07-09T03:20:14.162949'
duration_seconds: 5.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rhlE
  gene_symbol: rhlE
  uniprot_accession: Q88D48
  protein_description: 'RecName: Full=ATP-dependent RNA helicase RhlE {ECO:0000256|HAMAP-Rule:MF_00968};
    EC=3.6.4.13 {ECO:0000256|HAMAP-Rule:MF_00968};'
  gene_info: Name=rhlE {ECO:0000256|HAMAP-Rule:MF_00968}; Synonyms=rhlE-II {ECO:0000313|EMBL:AAN70546.1};
    OrderedLocusNames=PP_4980 {ECO:0000313|EMBL:AAN70546.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DEAD box helicase family. RhlE subfamily.
  protein_domains: DEAD/DEAH_box_helicase_dom. (IPR011545); DEAD/DEAH_RhlB. (IPR044742);
    DEAD_box_RNA_helicase. (IPR050079); DEAD_helicase_RhlE. (IPR028622); Helicase_ATP-bd.
    (IPR014001)
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
- **UniProt Accession:** Q88D48
- **Protein Description:** RecName: Full=ATP-dependent RNA helicase RhlE {ECO:0000256|HAMAP-Rule:MF_00968}; EC=3.6.4.13 {ECO:0000256|HAMAP-Rule:MF_00968};
- **Gene Information:** Name=rhlE {ECO:0000256|HAMAP-Rule:MF_00968}; Synonyms=rhlE-II {ECO:0000313|EMBL:AAN70546.1}; OrderedLocusNames=PP_4980 {ECO:0000313|EMBL:AAN70546.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DEAD box helicase family. RhlE subfamily.
- **Key Domains:** DEAD/DEAH_box_helicase_dom. (IPR011545); DEAD/DEAH_RhlB. (IPR044742); DEAD_box_RNA_helicase. (IPR050079); DEAD_helicase_RhlE. (IPR028622); Helicase_ATP-bd. (IPR014001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rhlE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rhlE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rhlE** (gene ID: rhlE, UniProt: Q88D48) in PSEPK.

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
  - Snippet 1 (score: 0.711)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [2] Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes
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
  - Snippet 1 (score: 0.695)
    > To inspect the transcriptomics result of individual genes, proteins originating from JGI have a hyperlink to a summary page which links to a 'Genome browser' page that displays the predicted gene splicing, including which regions have RNA support (Figure 1 D).
    > Hence, in the protein specific site in the JGI w e bsite under 'To Genome Browser', the current protein (GeneCatalog) can be seen together with se v eral other alternati v e predictions of the gene splicing, which is essential to have correct, for the protein to function naturally (Figure 2 ).
    > As the RNA coverage supports the exon / intron splicing, it is possible to infer whether a particular gene, in this case Table 1. Comparison between the dbCAN webserver, the eggNOG webserver for both family and functional annotation of CAZymes and the updated CUPP-w e bserver using the recommended significance cut-off at 5. The column 'CAZy -All characterized' encompasses all 10784 characterized proteins in the CAZy database used for the training, whereas the 'CAZy -Newly characterized '   a gene such as the one selected in Figure 2 , is more likely to work after heterologous gene expression.
    > To further improve the enzyme selection, all NCBI Genbank accessions were mapped to Uniprot ID to link to the specific Uniprot accession page including the predicted Al-phaFold structures, Go annotations and InterPro annotations and more ( 19 ).

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
  - Snippet 1 (score: 0.690)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.680)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.636)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

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
  - Snippet 1 (score: 0.667)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [6] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
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

### [7] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.657)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [8] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.654)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

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
  - Snippet 1 (score: 0.653)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [10] ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance
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
  - Snippet 1 (score: 0.647)
    > To reduce redundancy while preserving sequence diversity, the 235,441 validated ORFs were subjected to two-stage clustering using VSEARCH v2.21.1: first at 90% sequence identity, then refined at 95% identity. Cluster representatives were aligned against UniProt/Swiss-Prot (release 2024_01) using DIAMOND v2.0.15 in sensitive mode (--sensitive). The initial alignment yielded 62,689 ORFs with putative UniProt matches. For each match, protein names, functional descriptions, and Gene Ontology (GO) terms were extracted for downstream label assignment.
    > 2.1.4. Functional labeling. Functional labels (Enzymatic, Structural, Transport, Other) were assigned to the 62,689 UniProt-mapped ORFs using hierarchical keyword matching against a curated dictionary of 847 functional terms derived from UniProt protein descriptions and Gene Ontology annotations. The classification hierarchy prioritized primary molecular functions:
    > • Enzymatic: Proteins with catalytic activity (GO:0003824), including polymerases, proteases, methyltransferases, and helicases
    > • Structural: Proteins involved in virion assembly and structural maintenance (GO:0019012), including spike, envelope, membrane, and nucleocapsid proteins
    > • Transport: Proteins mediating membrane transport and ion channels (GO:0006810, GO:0015267)
    > • Other: All remaining ORFs, including regulatory proteins, accessory factors, and hypothetical proteins ORFs with ambiguous or conflicting annotations (e.g., proteins with both enzymatic and structural roles) were manually reviewed by two independent annotators, achieving 94.2% inter-annotator agreement (Cohen's κ = 0.92). After removing ambiguous cases, this resulted in 53,575 unique labeled ORF sequences with unambiguous functional assignments.The 'Other' category encompasses a functionally heterogeneous set of accessory proteins with distinct biological roles, as summarized in Table 1 Variants were filtered to retain only those with ≥2% sequence divergence from their corresponding base ORF to ensure meaningful diversity while maintaining functional annotation consistency.

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
  - Snippet 1 (score: 0.645)
    > Although this is a fairly obvious requirement, it is not trivial to implement because a protein reagent expressed recombinantly is typically not the exact same entity or in the same state as its corresponding assay participant in a living cell (e.g., kinase domain binding assay vs. corresponding kinase occurring in a specific cell line used for a growth inhibition assay). In this first version of metadata standards, we take a rudimentary approach. We use the UniProt accession and approved Gene symbol (NCBI Gene) and accession number to identify and reference proteins and their coding genes, respectively. Although we recognize limitations, for the purpose of our current simple use cases, this is sufficient. Linking protein and gene identifiers in addition is relevant to integrate RNAi reagent gene targets (see below). The recommended explicit fields for proteins include a standardized name, both for the protein and the gene that encodes it; source of protein (e.g., chemically synthesized, purified from natural source, recombinantly expressed); protein modifications (e.g., mutations, posttranslational modification); protein purity; subunit information for components of a protein complex; and isoform information (derived from either alternative promoter usage, alternative splicing, alternative translation initiation, or frame shifting). We are currently working on a formal description of proteins that will allow ambiguity (more-or less-specific definition of proteins), because in some cases, the exact entity and state of a protein reagent or model system participant is not definitively known (full length, functional domain, exact sequence, mutation, phosphorylation state, etc.).
    > Inhibitory RNAs (siRNA, shRNA). RNA interference is a standard methodology to transiently knock down gene expression in living cells. This can be achieved using different types of small RNA molecules, including siRNA, shRNA, and miRNA. Information that is relevant to identify and describe these perturbations include probe ID, name, source/provider, target gene symbol and accession number, sequence of the probe, and modifications to the probe (e.g., chemical modification) if any are specified.
    > Antibody Reagents.

### [12] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.645)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [13] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
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
  - Snippet 1 (score: 0.644)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

### [14] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
- Authors: E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al.
- Year: 2016
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
- DOI: 10.1186/s13059-016-1014-0
- Summary: The results provide the most complete comparative genomics and experimental analysis of mRBPs in P. falciparum and identify and characterize mRNA-binding proteins (mRBPs) that encompass a relatively large proportion of the parasite proteome as compared to other eukaryotes.
- Evidence snippets:
  - Snippet 1 (score: 0.643)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

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
  - Snippet 1 (score: 0.638)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [16] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
- Authors: F. Pfeiffer, D. Oesterhelt
- Year: 2015
- Venue: Life
- URL: https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
- DOI: 10.3390/life5021427
- PMID: 26042526
- PMCID: 4500146
- Citations: 38
- Influential citations: 1
- Summary: A manual curation effort is described that attempts to produce high-quality genome annotations for a set of haloarchaeal genomes (Halobacterium salinarum and Hbt. hubeiense, Haloferax volcanii and Hfx. mediterranei).
- Evidence snippets:
  - Snippet 1 (score: 0.634)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [17] CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts
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
  - Snippet 1 (score: 0.631)
    > Whole-genome sequencing has enabled investigations into the gene content of living many organisms and forms the foundation for further study of gene expression, proteomics and epigenetics. After assembly of a novel genome, gene annotation is often the first step in analysing the gene content of an organism. Accurate annotation of the exonic structure of genes is crucial to the success of all subsequent functional and comparative analyses.
    > Problems that can potentially be caused by incorrect gene annotation are numerous and can lead to incorrect assessments of the lifestyle and ecology of an organism. In comparative genomics where orthologous genes or conserved functional domains are compared between species/isolates, the estimated numbers of such genes/ domains can be distorted by less than perfect annotations (as described by Hane et al. [1], S Text 1). Prediction of extracellular secretion, which can be determined by a short signal peptide at the N-terminus, can miss secreted proteins if the start codon of a gene has been incorrectly annotated. Mis-annotating the start of protein translation could either cut off the signal peptide or bury it within the annotation. While a seemingly benign annotation error, the consequences for downstream research could be detrimental, particularly as the biotic interactions or industrial applications of microbes are largely determined by their secretomes. Additionally, translated protein sequences of novel species are often submitted to databases such as NCBI [2] and Uniprot [3]. It is commonplace to use these database entries to support the annotation of related species or isolates, meaning errors present in the pioneer annotation may be repeated. When these new annotations based on false assumptions are added to databases, there is not only a propagation of errors, but also a perceived strengthening of homology evidence for incorrect protein sequences.
    > In recent years, correction of in silico predicted gene annotations with RNA-seq derived transcripts and read alignments has enabled vastly improved genome annotations and corrections of annotated gene structures [4][5][6].

### [18] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.630)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [19] Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation
- Authors: Eugenio L Mangas, Alejandro Rubio, R. Álvarez-Marín, Gema Labrador-Herrera, J. Pachón et al.
- Year: 2019
- Venue: Microbial Genomics
- URL: https://www.semanticscholar.org/paper/ccdc06e24b4cff1ddca5e537c65e5f14c5f017b3
- DOI: 10.1099/mgen.0.000309
- PMID: 31626589
- PMCID: 6927304
- Citations: 64
- Influential citations: 2
- Summary: A genomics analysis of almost 2500 strains found two different groups of genomes found based on the number of shared genes, one of which rarely has plasmids, and bears clustered regularly interspaced short palindromic repeat (CRISPR) sequences, in addition to CRISPR-associated genes (cas genes) or restriction-modification system genes.
- Evidence snippets:
  - Snippet 1 (score: 0.625)
    > To homogenize the genome annotation, the sequences of all genomes were analysed using the same protocol. The proteinencoding genes were predicted using Prokka version 1.13 [24], and the predicted protein sequences were functionally annotated using Sma3s v2 and UniProt taxonomic division bacteria 2019_01 as a reference database [25,55].
    > To annotate specific genes, GO (gene ontology) terms and UniProt keywords assigned by Sma3s were used. To find genes associated with CRISPR systems, protein sequences coming

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer (2023). Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes. Nucleic Acids Research. https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
3. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
5. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
6. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
7. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
8. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
9. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
10. FuGuo Liu, T. Lai, Wenxia Xu, Guodong Li (2026). ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance. PLOS One. https://www.semanticscholar.org/paper/7d7965ec223f5715675839cb57efdc776d25e216
11. U. Vempati, Caty Chung, Christopher Mader, Amar Koleti, Nakul Datar et al. (2014). Metadata Standard and Data Exchange Specifications to Describe, Model, and Integrate Complex and Diverse High-Throughput Screening Data from the Library of Integrated Network-based Cellular Signatures (LINCS). Journal of Biomolecular Screening. https://www.semanticscholar.org/paper/91af493a67a83d599ad00f4da275e8eadd165b5e
12. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
13. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/f3eda16f7a2760619a7727b38fc2fc6738858040
14. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
15. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
16. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
17. Alison C. Testa, James K. Hane, S. Ellwood, R. Oliver (2015). CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts. BMC Genomics. https://www.semanticscholar.org/paper/06704917bf44cd62eef0bb5cb944b97484056e21
18. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
19. Eugenio L Mangas, Alejandro Rubio, R. Álvarez-Marín, Gema Labrador-Herrera, J. Pachón et al. (2019). Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation. Microbial Genomics. https://www.semanticscholar.org/paper/ccdc06e24b4cff1ddca5e537c65e5f14c5f017b3