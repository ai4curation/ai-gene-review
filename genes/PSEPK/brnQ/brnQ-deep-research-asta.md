---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-11T02:15:10.552407'
end_time: '2026-07-11T02:15:15.818030'
duration_seconds: 5.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: brnQ
  gene_symbol: brnQ
  uniprot_accession: Q88FB4
  protein_description: 'RecName: Full=Branched-chain amino acid transport system carrier
    protein {ECO:0000256|RuleBase:RU362122};'
  gene_info: Name=brnQ {ECO:0000313|EMBL:AAN69765.1}; OrderedLocusNames=PP_4184 {ECO:0000313|EMBL:AAN69765.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the branched chain amino acid transporter
  protein_domains: Brnchd-chn_aa_trnsp_Livcs. (IPR004685); Branch_AA_trans (PF05525)
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
- **UniProt Accession:** Q88FB4
- **Protein Description:** RecName: Full=Branched-chain amino acid transport system carrier protein {ECO:0000256|RuleBase:RU362122};
- **Gene Information:** Name=brnQ {ECO:0000313|EMBL:AAN69765.1}; OrderedLocusNames=PP_4184 {ECO:0000313|EMBL:AAN69765.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the branched chain amino acid transporter
- **Key Domains:** Brnchd-chn_aa_trnsp_Livcs. (IPR004685); Branch_AA_trans (PF05525)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "brnQ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'brnQ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **brnQ** (gene ID: brnQ, UniProt: Q88FB4) in PSEPK.

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
  - Snippet 1 (score: 0.752)
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
  - Snippet 1 (score: 0.752)
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
  - Snippet 1 (score: 0.747)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [4] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.743)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [5] A computational genomics pipeline for prokaryotic sequencing projects
- Authors: A. Kislyuk, L. Katz, Sonia Agrawal, Matthew S. Hagen, Andrew B. Conley et al.
- Year: 2010
- Venue: Bioinformatics
- URL: https://www.semanticscholar.org/paper/17027b44117f371e335aada5f1a518a7ed2c7d66
- DOI: 10.1093/bioinformatics/btq284
- PMID: 20519285
- PMCID: 2905547
- Citations: 71
- Influential citations: 2
- Summary: The pipeline is capable of enhanced or manually assisted reference-based assembly using multiple assemblers and modes; gene predictor combining; and functional annotation of genes and gene products, which makes it suitable for projects of a sensitive nature.
- Evidence snippets:
  - Snippet 1 (score: 0.735)
    > Functional annotation of genome features was also performed using a combination of tools. Annotation of protein coding genes was based on an integrated platform that makes use of six distinct annotation tools, four of which employ intrinsic sequence characteristics for annotation and two that use extrinsic homology-based approaches to compare sequences against databases of sequences and structures with known functions. Information on Gene Ontology (GO) terms, domain architecture and identity, subcellular localization, signal peptides, transmembrane helices and lipoprotein motifs is provided for each protein-coding gene (Fig. 4). BLASTp alignment of predicted proteins was performed against the UniProt database (Uniprot, 2009). Homology-based searches were also made across thirteen sequence and protein domain databases with the InterProScan suite (Mulder and Apweiler, 2007). Parsing of the results was carried out against the corresponding InterPro database. The pipeline also stores the top five hits for each gene against the NCBI non-redundant protein  database, to provide potentially useful information. All homology searches were run locally. Signal peptides were annotated using the SignalP package (Bendtsen et al., 2004) and transmembrane domains were annotated with the TMHMM package (Krogh et al., 2001). State of the art in subcellular localization algorithms was examined to ensure the best performance given our operational requirements. Insertion sequences (transposases) and proteins reported as virulence factors by VFDB (Chen et al., 2005;Yang et al., 2008) were also annotated. These annotations of virulence-related features make the pipeline particularly useful for projects working with pathogenic prokaryotes. Results of this analysis are summarized in Table 4.
    > After the functional annotations were determined, a naming scheme was employed for each locus to conform to standard annotation terminology. Specific gene names were assigned according to homology-based results. For genes that had a Uniprot result with a best hit at >91% amino acid sequence identity and an e-value <1e-9, the gene assumed the best hit's name.

### [6] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.720)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [7] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.719)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [8] MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data
- Authors: Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang
- Year: 2010
- Venue: Journal of Biomedicine and Biotechnology
- URL: https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
- DOI: 10.1155/2009/642524
- PMID: 20169000
- PMCID: 2822236
- Citations: 18
- Influential citations: 1
- Summary: By applying the MIClique algorithm to real gene expression data, some DEC gene subsets which correlated under one experimental condition but uncorrelated under another condition are detected from the graph of colon dataset and leukemia dataset.
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > Table 3 lists the Genbank accession number, the gene symbols, accession number in UniProtKB (UniProt Knowledgebase), and gene descriptions given by colon data. The UniProtKB is the central hub for the collection of information on proteins such as amino acid sequence, protein name or description, taxonomic data, and biological ontology [24]. Figure 6 depicts gene expression profiles of the eight genes in normal and disease samples. As shown in Figure 6, the profiles of these genes are highly coexpressed in normal samples (samples 1-22) while the coexpression pattern disappears in disease samples (samples 23-62).

### [9] Proteomic profiling of regenerated urinary bladder tissue with stem cell seeded scaffold composites in a non-human primate bladder augmentation model
- Authors: Tiffany T. Sharma, S. Edassery, N. Rajinikanth, Vikram Karra, Matthew I. Bury et al.
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/6446e5bc8c0ec1aa0836a711b705ebafa66bd5c8
- DOI: 10.1101/2023.08.29.554824
- PMID: 37693577
- PMCID: 10491202
- Citations: 1
- Summary: Autologous, bone marrow derived mesenchymal stem cells along with primitive hematopoietic stem/progenitor cells can be used to regenerate bladder tissue in a large deficit, non-human primate bladder augmentation model and facilitates the promotion of a protein tissue landscape that is nearly identical to native bladder tissue.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > Raw data were analyzed using Proteome Discoverer 2.5 (Thermo Fisher Scientific) using the "PWF Tribrid TMTpro Quan SPS MS3 SequestHT Percolator" and "CWF Comprehensive Enhanced Annotation Reporter
    > Quan" methods implemented in the PD2.For uncharacterized proteins or proteins with unknown function presented in the manuscript, the UniProt Accession number was search against UniProt database https://www.uniprot.org/and the NCBI Gene database https://www.ncbi.nlm.nih.gov/gene/.If required, more information was obtained with regards to protein identity by matching the amino acid sequence of the protein on the NCBI BLAST alignment program https://blast.ncbi.nlm.nih.gov/Blast.cgi .

### [10] Potential role of multiple carbon fixation pathways during lipid accumulation in Phaeodactylum tricornutum
- Authors: Jacob J. Valenzuela, Aurélien Mazurie, R. Carlson, R. Gerlach, K. Cooksey et al.
- Year: 2012
- Venue: Biotechnology for Biofuels
- URL: https://www.semanticscholar.org/paper/5f205021fe6a9b10aba8237bdac8ceada97adde0
- DOI: 10.1186/1754-6834-5-40
- PMID: 22672912
- PMCID: 3457861
- Citations: 206
- Influential citations: 10
- Summary: The results indicate that P. tricornutum continued carbon dioxide reduction when population growth was arrested and different carbon-concentrating mechanisms were used dependent upon exogenous DIC levels, and suggest that the build-up of precursors to the acetyl-CoA carboxylases may play a more significant role in TAG synthesis rather than the actual enzyme levels of acetyl
- Evidence snippets:
  - Snippet 1 (score: 0.689)
    > Cufflinks output files had transcripts identified by uniprot accessions. Using the DAVID (Database for Annotation, Visualization, and Integrated Discovery) [67] Gene ID conversion tool, uniprot accessions were converted to Locus Tag IDs and Protein IDs. Once all accessions were converted, the DAVID Functional Annotation tool was used to retrieve gene names as well as KEGG (Kyoto Encyclopedia of Genes and Genomes) Pathway information. For genes that were identified as hypothetical proteins, searches were performed on the JGI Phaeodactylum tricornutum v2.0 genome website (http://genome.jgi-psf. org/Phatr2/Phatr2.home.html) and based on best hits, % ID, score, and consistency of the top hits, genes were either identified or remained as hypothetical. Genes were also searched on NCBI and ENSEMBL genome browsers for cross-referencing. To assign genes into pathways, we used KEGG maps for P. tricornutum as a backbone. Genes for major pathways were searched manually to find genes not directly annotated in the P. tricornutum KEGG maps. Gene lists were compiled for the major pathways and developed into network maps.
    > Organelle targeting for transcript products was done based on annotations from the databases of JGI, NCBI, and ENSEMBL. If no localization was found, eukaryotic organelle localizations were predicted with TargetP 1.1. server [68] in both plant and non-plant mode. Amino acid sequences were also checked for a peroxisomal targeting sequence (SKL, serine-lysine-leucine). If potential targeting was not identified, we assumed that the gene product occurred in the cytoplasm. If the gene was an integral membrane protein we again checked JGI, NCBI, and ENSEMBL, and if targeting could not be determined we located the gene in the most biologically relevant membrane (e.g., light harvesting complex in the plastid).

### [11] Prioritising genetic findings for drug target identification and validation.
- Authors: N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt
- Year: 2024
- Venue: Atherosclerosis
- URL: https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9
- DOI: 10.1016/j.atherosclerosis.2024.117462
- PMID: 38325120
- Citations: 11
- Summary: The current review provides an overview of genetic evidence for drug target identification, and how biomedical databases can be used to provide actionable prioritisation, fully informing downstream experimental validation.
- Evidence snippets:
  - Snippet 1 (score: 0.686)
    > Other gene identification systems include the Entrez Gene [43] database for gene-specific information, and the HUGO Gene Nomenclature Committee (HGNC) [44] which maintains unique symbols and names for human loci.An analogue for proteins is the UniProt Knowledgebase (UniProtKB) [45], which contains data on protein sequences and function, and each protein in the database is assigned a unique UniProt accession ID.UniProt provides functionality to map between different identifiers, including Ensembl IDs and UniProt accession IDs.
    > A common naming convention is also required to identify the diseases associated with the drug targets.Medical Subject Headings (MeSH) [46] are terms defined by the National Library of Medicine, and act as a standardised thesaurus for diseases and medical conditions which can be used to index PubMed.In some data sources, such as the Chemical Biology Database (ChEMBL) [23], diseases and outcomes will be identified by MeSH terms.However, in other cases, this will not be the case, and a metathesaurus such as the Unified Medical Language System (UMLS) [47] can be used to map synonymous disease terms.

### [12] ProteoSushi: a software tool to biologically annotate and quantify modification-specific, peptide-centric proteomics datasets
- Authors: Robert W Seymour, S. van der Post, A. Mooradian, Jason M. Held
- Year: 2020
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/9bdbfae251dfa48820f40c01f12a1ee25fcdf57e
- DOI: 10.1101/2020.11.24.395921
- PMID: 34056901
- Citations: 6
- Summary: ProteoSushi is a software tool tailored to the analysis of each modified site in peptide-centric proteomic datasets that is compatible with any post-translational modification or chemical label, and streamlines peptides-centric data processing and knowledge mining of large modification-specific proteomics datasets.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > ProteoSushi assigns each peptide to all proteins with a matching sequence in the userprovided FASTA proteome using the amino acid sequence of each modified peptide. Leucines and isoleucines, which are isobaric and can't be distinguished through mass spectrometry, are considered equivalent. Proteins in UniProt reference proteome are not equally likely studied and characterized resulting in a wide range of annotation quality and depth. Therefore, ProteoSushi compares the UniProt annotation scores of all matched proteins and annotates the peptide with the available information of those with the highest score (Supp. Fig. S1). This approach minimizes over-annotation and prioritizes assignment to better characterized proteins. This is especially useful for species that are not annotated well. The primary gene name assigned to the UniProt ID is used to assign the gene, and the modified residue(s) of the peptide are assigned to the amino acid number in the UniProt amino acid sequence.
    > ProteoSushi provides an option for a user-input list of gene names to prioritize identification to a specific subset of candidate proteins. Potential applications of this include organelle or protein complex enrichment prior to PTM enrichment, such as mitochondrial fractionation followed by enrichment for lysine acetylation 4 . In this case, the user can input a list of mitochondrial genes and ProteoSushi will prioritize assignment of peptides to these genes instead of cytoplasmic proteins that may have sequence homology. The ProteoSushi output indicates that the assigned proteins are in the target list to simplify follow-up analysis.
    > To compare how proteins and genes are assigned by ProteoSushi versus typical proteincentric database search software, the data output from MaxQuant were compared before and after ProteoSushi processing. A publicly available proteomic dataset that enriched and quantified the reversible oxidation of ~4,000 cysteines 29 was used for evaluation.

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
  - Snippet 1 (score: 0.679)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [14] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
- Authors: S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson
- Year: 2019
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
- DOI: 10.1093/nar/gkz030
- PMID: 30698741
- PMCID: 6412132
- Citations: 133
- Influential citations: 4
- Summary: The misconception that a gene in E. coli whose primary name starts with ‘y’ is unannotated is resolved, and the value of the y-ome is discussed for systematic improvement ofE.
- Evidence snippets:
  - Snippet 1 (score: 0.679)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

### [15] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.678)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [16] Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B
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
  - Snippet 1 (score: 0.677)
    > 2.8.1. Annotation methods 2.8.1.1. Functional annotation. UniProt-GOA database was utilized to retrieve Gene Ontology (GO) annotation proteome. First, the identified protein identity was converted to UniProt identity and then mapped to GO identity based on the protein identity. When the identified protein was not annotated by UniProt-GOA, the functional annotation of that protein was conducted using the InterProScan software according to the amino acid sequence alignment approach. All proteins were then classified into 3 groups: molecular function, cellular component and biological process.

### [17] MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila
- Authors: Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al.
- Year: 2025
- Venue: Synthetic and Systems Biotechnology
- URL: https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
- DOI: 10.1016/j.synbio.2025.04.001
- PMID: 40276250
- PMCID: 12018684
- Summary: Shifts in metabolic allocation in a glucoamylase hyperproduction strain of M. thermophila are identified, highlighting changes in fatty acid biosynthesis and amino acids biosynthesis pathways, which provide new insights into the underlying phenotypic alterations.
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > Single-gene search: Gene annotation is essential for biologists to understand a gene's function. MTD's single-gene search interface allows researchers to obtain a comprehensive gene description by entering or selecting a gene ID. The results include sequence information, CAZy family, Pfam domains, GO/KEGG annotations, and phenotype information (Fig. 2D), along with sequence-based predictions such as optimal protein activity temperature, melting temperature (Tm), subcellular localization, and transcription factor scores. To enhance data accessibility, links to external databases such as NCBI, KEGG, FungiDB [4], UniProt, and JGI are also provided, facilitating cross-referencing of gene annotations across various resources.
    > Unlike the static genome, the transcriptome captures dynamic gene expression changes in response to developmental or environmental conditions, establishing a dynamic link between an organism's genome and its physical characteristics [63]. In the single-gene retrieval interface, the expression of the searched gene is visualized in the form of box plots and scatter plots across transcriptome datasets (Fig. 2E). When hovering over any data point, users can view the corresponding experimental details, such as mutant name, sample processing methods, and growth conditions. This interactive feature reveals gene expression responses to environmental factors, allowing researchers to quickly identify experimental conditions of interest and explore the gene's potential roles in diverse biological contexts. Moreover, clicking on the dataset title will direct users to the GEO browser for further detailed descriptions. KEGG Pathway or Gene List Search: In transcriptome studies, researchers typically adopt a "bottom-up" approach: first sequencing all mRNA in a cell, identifying differentially expressed genes between conditions, and then performing GO/KEGG enrichment analysis to interpret functional distributions. MTD, however, offers a complementary "top-down" search strategy, enabling users to examine the expression of genes within a specific KEGG pathway (Fig. 3A) or a user-defined gene set. A unique feature of MTD is its manually curated data categorization system, which organizes sample data with detailed annotations based on experimental conditions.

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
  - Snippet 1 (score: 0.672)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [19] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.670)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

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
  - Snippet 1 (score: 0.669)
    > We used NGS-SNP [25] for functional annotation of identified SNPs and indels. The details of the resulting annotation fields have been described by Grant et al. [25]. Briefly, NGS-SNP provides rich annotations for genome-wide SNP and indels in organisms for which reference sequences are available in the Ensembl database. It reports a "Model_Annotations" field with detailed comparisons of SNP/indel to an orthologous gene typically in a well-characterized species. NGS-SNP also classifies whether or not the amino acid change is deleterious based on SIFT [56] prediction. Other important fields include overlapping protein features or domains, gene ontology information, and the conservation of both the SNP site and flanking sequence compared to a well-characterized species. NGS-SNP also reports NCBI, Ensembl, and UniProt IDs for genes, transcripts, and proteins when applicable. A gene description, phenotypes linked to the gene and whether the SNP/indel is novel or known is also supplemented in the annotated field. In our analysis, NGS-SNP utilized information from Ensembl release 72 [57], dbSNP Build 133 [58], Entrez Gene [58] and UniProt release 2013_09 [59]. We incorporated Homo sapiens as the model species for sequence conservation during annotation because most of the eukaryotic genes are well characterized in human.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
5. A. Kislyuk, L. Katz, Sonia Agrawal, Matthew S. Hagen, Andrew B. Conley et al. (2010). A computational genomics pipeline for prokaryotic sequencing projects. Bioinformatics. https://www.semanticscholar.org/paper/17027b44117f371e335aada5f1a518a7ed2c7d66
6. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
7. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
8. Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang (2010). MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data. Journal of Biomedicine and Biotechnology. https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
9. Tiffany T. Sharma, S. Edassery, N. Rajinikanth, Vikram Karra, Matthew I. Bury et al. (2023). Proteomic profiling of regenerated urinary bladder tissue with stem cell seeded scaffold composites in a non-human primate bladder augmentation model. bioRxiv. https://www.semanticscholar.org/paper/6446e5bc8c0ec1aa0836a711b705ebafa66bd5c8
10. Jacob J. Valenzuela, Aurélien Mazurie, R. Carlson, R. Gerlach, K. Cooksey et al. (2012). Potential role of multiple carbon fixation pathways during lipid accumulation in Phaeodactylum tricornutum. Biotechnology for Biofuels. https://www.semanticscholar.org/paper/5f205021fe6a9b10aba8237bdac8ceada97adde0
11. N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt (2024). Prioritising genetic findings for drug target identification and validation.. Atherosclerosis. https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9
12. Robert W Seymour, S. van der Post, A. Mooradian, Jason M. Held (2020). ProteoSushi: a software tool to biologically annotate and quantify modification-specific, peptide-centric proteomics datasets. bioRxiv. https://www.semanticscholar.org/paper/9bdbfae251dfa48820f40c01f12a1ee25fcdf57e
13. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
14. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
15. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
16. Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al. (2022). Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B. Data in Brief. https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
17. Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al. (2025). MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila. Synthetic and Systems Biotechnology. https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
18. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
19. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
20. Ashutosh Das, F. Panitz, V. R. Gregersen, C. Bendixen, L. Holm (2015). Deep sequencing of Danish Holstein dairy cattle for variant detection and insight into potential loss-of-function variants in protein coding genes. BMC Genomics. https://www.semanticscholar.org/paper/b96532e082a2c5b0f3f0fc51afc47ac2426b4904