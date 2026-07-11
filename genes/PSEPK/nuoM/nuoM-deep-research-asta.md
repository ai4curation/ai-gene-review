---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T06:02:08.351035'
end_time: '2026-07-07T06:02:18.145851'
duration_seconds: 9.79
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nuoM
  gene_symbol: nuoM
  uniprot_accession: Q88FG6
  protein_description: 'RecName: Full=NADH-quinone oxidoreductase subunit M {ECO:0000256|ARBA:ARBA00019906};
    AltName: Full=NADH dehydrogenase I subunit M {ECO:0000256|ARBA:ARBA00031584};
    AltName: Full=NDH-1 subunit M {ECO:0000256|ARBA:ARBA00032798};'
  gene_info: Name=nuoM {ECO:0000313|EMBL:AAN69713.1}; OrderedLocusNames=PP_4130 {ECO:0000313|EMBL:AAN69713.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the complex I subunit 4 family.
  protein_domains: NADH_Q_OxRdtase_chainM/4. (IPR010227); NADH_UbQ_OxRdtase. (IPR003918);
    ND/Mrp_TM. (IPR001750); Proton_antipo_M (PF00361)
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
- **UniProt Accession:** Q88FG6
- **Protein Description:** RecName: Full=NADH-quinone oxidoreductase subunit M {ECO:0000256|ARBA:ARBA00019906}; AltName: Full=NADH dehydrogenase I subunit M {ECO:0000256|ARBA:ARBA00031584}; AltName: Full=NDH-1 subunit M {ECO:0000256|ARBA:ARBA00032798};
- **Gene Information:** Name=nuoM {ECO:0000313|EMBL:AAN69713.1}; OrderedLocusNames=PP_4130 {ECO:0000313|EMBL:AAN69713.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the complex I subunit 4 family.
- **Key Domains:** NADH_Q_OxRdtase_chainM/4. (IPR010227); NADH_UbQ_OxRdtase. (IPR003918); ND/Mrp_TM. (IPR001750); Proton_antipo_M (PF00361)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nuoM" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nuoM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nuoM** (gene ID: nuoM, UniProt: Q88FG6) in PSEPK.

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
  - Snippet 1 (score: 0.767)
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
  - Snippet 1 (score: 0.751)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

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
  - Snippet 1 (score: 0.744)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [4] Ten steps to get started in Genome Assembly and Annotation
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
  - Snippet 1 (score: 0.737)
    > The ultimate goal of the functional annotation process (Figure 4) is to assign biologically relevant information to predicted polypeptides, and to the features they derive from (e.g. gene, mRNA). This process is especially relevant nowadays in the context of the NGS era due to the capacity of sequencing, assembling, and annotating full genomes in short periods of time, e.g. less than a month. Functional elements could range from putative name and/or symbols for protein-coding genes, e.g. ADH to its putative biological function, e.g. alcohol dehydrogenase, associated gene ontology terms, e.g. GO:0004022, functional sites, e.g. METAL 47 47 Zinc 1, and domains, e.g. IPR002328, among other features. The function of predicted proteins can be computationally inferred based on the similarity between the sequence of interest and other sequences in different public repositories, e.g. BLASTP against Uniprot. Caution should be taken when assigning results merely based on sequence similarity as two evolutionary independent sequences which share some common domains could be considered homologs 62 . Thus, whenever possible, it is better to use orthologous sequences for annotation purposes rather than simply similar sequences 63 . With the growing number of sequences in those public repositories, it is possible to perform various searches and combine obtained results into a consensus annotation. The accurate assignment of the functional elements is a complex process, and the best annotation will involve manual curation.
    > There are two main outcomes of the functional annotation process. The first is the assignment of functional elements to genes. Downstream analysis of these elements allow further understanding of specific genome properties, e.g. metabolic pathways, and similarities compared with closely related species. The second result of the functional annotation is the additional quality check for the predicted gene set. It is possible to identify problematic and/or suspicious genes by the presence of specific domains, suspicious orthology assignment and/or absence of other functional elements, e.g. functional completeness. These Page 13 of 19

### [5] Role of the Gene ndufs8 Located in Respiratory Complex I from Monascus purpureus in the Cell Growth and Secondary Metabolites Biosynthesis
- Authors: Xinru Cai, Song Zhang, Jia Lin, Yaxu Wang, Fa-Bing Ye et al.
- Year: 2022
- Venue: Journal of Fungi
- URL: https://www.semanticscholar.org/paper/5211255ad6045e484b52456db63359041616fd33
- DOI: 10.3390/jof8070655
- PMID: 35887413
- PMCID: 9319538
- Citations: 11
- Summary: Investigation of the regulation mechanisms of respiratory complex I in response to the cell growth and secondary metabolite biosynthesis of M. purpureus revealed that complex I plays a vital role in regulating the cell grow and secondary metabolism of Monascus via changing the intracellular ROS and ATP levels.
- Evidence snippets:
  - Snippet 1 (score: 0.731)
    > From the genomic analysis of M. purpureus LQ-6, the gene monascus_4971 with the total number of length of 1180 bp, encoding a protein with the total number of length of 225 aa, which was identified as 23 kDa subunit of NADH-quinone oxidoreductase (22% Query Cover, 88.21% Identity) in Aspergillus terreus NIH2624 (accession: XM_001212139.1) by searching the NCBI-blastn, and NADH dehydrogenase Fe-S protein subunit 8 (ndufs8, 23 kDa subunit of the mitochondrial complex I) (100% Query Cover, 100% Identity) in M. purpureus HQ1 (accession: TQB76855.1) by searching the NCBI-blastp. The 23 kDa subunit of the human mitochondrial respiratory complex I is 72% identical to the Rhodobacter capsulatus nuoI counterpart [21]. Furthermore, the phyre2 web server predicted the spatial structure of the protein encoding by gene monascus_4971, and the result showed that it was almost same as the spatial structure of protein 6gcsI with 100% confidence and 80% coverage (Figure 1). In fact, the protein data bank showed that 6gcs (NADH: ubiquinone oxidoreductase) is the respiratory complex I from Yarrowia lipolytica (Candida lipolytica), and 6gcsI (229 aa, 25.68 kDa) is the NADH: ubiquinone oxidoreductase chain I (https: //www.ebi.ac.uk/pdbe/entry/pdb/6gcs/protein/9 (accessed on 10 October 2018)), and the domain homologous to the gene nuim (UniProtKB-Q9UUT8, 33-229 aa, coverage: 83%) encoding NADH: ubiquinone oxidoreductase 23 kDa subunit (https://www.uniprot.org/ uniprot/Q9UUT8 (accessed on 1 May 2020)).

### [6] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
- Authors: Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al.
- Year: 2020
- Venue: RNA
- URL: https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
- DOI: 10.1261/rna.075580.120
- PMID: 32669294
- PMCID: 7566566
- Citations: 3
- Summary: Gene ontology analysis reveals an enrichment of genes related to translation, including mRNAs of ribosomal proteins, tRNAs, tRNA ligases, and t RNA-modifying enzymes, consistent with a key role of Hera in ribosome and tRNA metabolism.
- Evidence snippets:
  - Snippet 1 (score: 0.724)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

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
  - Snippet 1 (score: 0.723)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [8] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.703)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [9] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
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
  - Snippet 1 (score: 0.703)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [10] Next Generation Sequencing and Transcriptome Analysis Predicts Biosynthetic Pathway of Sennosides from Senna (Cassia angustifolia Vahl.), a Non-Model Plant with Potent Laxative Properties
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
  - Snippet 1 (score: 0.698)
    > Further the assembled transcript contigs were validated using CLC Genomics workbench (CLC Bio, Boston, MA 02108 USA) by mapping high quality reads back to the assembled transcript contigs. ORF-Predictor [57], an online tool, was used on default parameters to identify the coding DNA sequences (CDS) from assembled transcript contigs. GC counts of transcripts was determined using a custom-made perl script.
    > Functional annotations. The functional annotation was performed by aligning coding DNA sequence (CDS) to NCBI 'green plant database (txid 33090)' database using basic local alignment search tool (BLASTX) [58] with an E-value threshold of 1e -06 and GO assignments were used to classify the functions of the predicted CDS. The GO mapping also provided ontology of defined terms representing gene product properties which were grouped into three main domains: biological process (BP), molecular function (MF) and cellular component (CC). GO mapping was carried out in order to retrieve GO terms for all the BLASTX functionally annotated CDS. The GO mapping used defined criteria to retrieve GO terms for annotated CDS which included use of BLASTX result accession IDs to retrieve gene names or symbols, UniProt IDs and direct search in the dbxref table of GO database. Identified gene names or symbols were then searched in the species specific entries of the gene-product tables of GO database. UniProt IDs made use of protein information resource (PIR) which includes protein sequence database (PSD), UniProt, SwissProt, TrEMBL, RefSeq, GenPept, and PDB databases. Gene Ontology analysis helps in specifying all the annotated nodes comprising of GO functional groups. CDS were compared against the COG (Clusters of Orthologous Groups) database for the analysis of phylogenetically widespread domain families. CDS were compared against Pfam database for higher-level groupings of related protein families, known as clans and the identification of domains that occurs within proteins. BLASTX was used against uniprot-swissprot database with cut-off e-value 1e-6 to annotate predicted CDS against protein.

### [11] MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data
- Authors: Anthony C. Smith, A. Robinson
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
  - Snippet 1 (score: 0.695)
    > Recorded for each protein of the mass spectrometry data sets were, where available, the original protein identifier, subcellular location, sequence of identified peptides, sequence coverage, and the experimental techniques that had been used for the purification, separation, and identification of the protein. If the original protein identifier could not be mapped to a UniProt primary accession number by PIR ID or MGI, then the protein was compared with proteins in UniProt by using BLASTP (14). If there was a significant match, then the UniProt primary accession number was assigned to the protein. Those proteins without a significant match were discarded. By using the PIR ID and the MGI identifier conversion tools, the evidence of mitochondrial localization for a protein was linked to many of the UniProt entries representing it. Identifiers of proteins encoded in the mitochondrial genome of organisms were taken from the Organelle database of the European Molecular Biology Laboratory-European Bioinformatics Institute and used to annotate the appropriate proteins in MitoMiner.
    > The source of protein sequences, related features, and annotation was UniProt (11). All UniProt entries were downloaded for the six species with mitochondrial localization data sets. The literature citations in each UniProt entry were retrieved from PubMed by using an InterMine parser. Additional Gene Ontology annotation on the biological process, metabolic function, and cellular component of each protein was taken from UniProt (15) and individual genome projects of M. musculus (12), Rattus norvegicus (16), Drosophila melanogaster (17), and Saccharomyces cerevisiae (18).
    > Finally lists of human genes and the descriptions of their associated disease phenotypes were taken from OMIM (19), the definitions of groups of homologous proteins were taken from HomoloGene (20), and data on the reactions, enzymes, and compounds of metabolic pathways were taken from KEGG (21). The EC numbers of proteins in UniProt were used to define the cross-reference between proteins and metabolic pathways.

### [12] Meta-Analysis of Studies Using Suppression Subtractive Hybridization and Microarrays to Investigate the Effects of Environmental Stress on Gene Transcription in Oysters
- Authors: K. Anderson, Daisy A. Taylor, E. Thompson, A. Melwani, S. Nair et al.
- Year: 2015
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/2e1f7fa1a93ee5206f397d90f45aefcdf8e0faff
- DOI: 10.1371/journal.pone.0118839
- PMID: 25768438
- PMCID: 4358831
- Citations: 45
- Influential citations: 1
- Summary: A meta-analysis of 14 studies that investigated the effects of different environmental stressors on gene expression in oysters found that the expression of over 400 genes in a range of oyster species changed significantly after exposure to environmental stress.
- Evidence snippets:
  - Snippet 1 (score: 0.684)
    > For instance, NADH dehydrogenase (EC 1.6.99.3) was deemed to be synonymous with cytochrome c reductase, NADH oxidoreductase and 13 other gene names; see http://enzyme.expasy.org/EC/1.6.99.3). In many cases, the alternative gene name was added to our database annotation to avoid redundancy. In addition, if two or more of the entries in our database of oyster genes encoded the same gene but had been allocated different names in the literature, those redundant sequences were consolidated into a single entry. In some additional cases, genes encoded in the mitochondrial (Mt) genome were allocated accession numbers in the primary literature that corresponded to the entire Mt genome. These were re-allocated gene-specific accessions.
    > After this filtering process, the final consolidated database was re-analyzed to verify the putative functions of the differentially expressed genes. These functional assignments were initially checked against searches of the literature cited in the GenBank registration file for each sequence. The functional category into which the gene fell was then confirmed by reference to the UniProtKB Protein Knowledgebase (http://www.uniprot.org/uniprot/) and the primary literature. The results from these searches were cross-referenced and hierarchically preferenced so that a single biological function could be assigned to each gene sequence in the database. Preference was given to ontologies that were based on experimentally defined functions in oysters, other bivalves, and mollusks in general.
    > As a result of these multiple filters, only sequences from published studies with definitive gene identifications and robust functional annotations were included in subsequent analyses.
    > At the time of this analysis, there were 97,811 nucleotide and 223,784 EST sequences listed in GenBank under the three oyster genera investigated (Table 1). Ninety-eight percent of the CoreNucleotide sequences that we searched against were from the genus Crassostrea, 0.6% were from Saccostrea, and 1.5% were from Ostrea. More than 99% of the dbEST sequences were from the genus Crassostrea.

### [13] A Semi-Quantitative, Synteny-Based Method to Improve Functional Predictions for Hypothetical and Poorly Annotated Bacterial and Archaeal Genes
- Authors: A. Yelton, B. Thomas, S. Simmons, P. Wilmes, A. Zemla et al.
- Year: 2011
- Venue: PLoS Computational Biology
- URL: https://www.semanticscholar.org/paper/88870437e2914eb4a8ed4914fe4f867e96372670
- DOI: 10.1371/journal.pcbi.1002230
- PMID: 22028637
- PMCID: 3197636
- Citations: 46
- Influential citations: 2
- Summary: A gene functional annotation method that weights evolutionary distance to estimate the probability of functional associations of syntenous proteins between genome pairs is developed, which is the first method to assign possible functions to poorly annotated genes through quantification of the probabilities of gene functional relationships at a significant evolutionary distance.
- Evidence snippets:
  - Snippet 1 (score: 0.683)
    > The synteny-based annotation of molybdopterin synthesis genes also differentiates the various AMD Archaea. Our synteny-based method improved annotations or provided annotations for seventeen genes in A-plasma, eleven genes in I-plasma, ten genes in Fer1, and six genes in Fer2 that were involved in molybdopterin synthesis, utilization or molybdate uptake (Figure 6 and Table S3). In silico protein structure modeling supported the functional Orthologs that are sometimes in predicted operons (operon genes) are compared separately from those that are never in operons (non-operon genes). The circled outliers come from comparisons of endosymbiont genomes, which have very small genomes and greater than expected conserved gene order in non-operon genes. doi:10.1371/journal.pcbi.1002230.g003 annotation of a number of these genes (Table S3). The A, I, Fer1, and Fer2 genomes have full pathways for the synthesis of molybdopterin guanine dinucleotide (MOB-DN), a molybdopterin cofactor that is used by proteins involved in anaerobic energy metabolism, while E and G-plasma have very few annotated molybdopterin synthesis genes of any kind. Formate dehydrogenase subunit genes are found in A-plasma, I-plasma, Fer1, and Fer2 genomes within molybdopterin synthesis gene clusters. Formate dehydrogenase is a MOB-DN-utilizing enzyme. In silico protein modeling provided additional evidence for the formate dehydrogenase annotation of these genes (Table S3).
    > Ether lipid biosynthesis genes were found in all of the AMD Thermoplasmatales Archaea, as expected. Synteny-based annotation improved or provided annotations for a number of genes involved  in ether lipid biosynthesis and its feeder pathway, the mevalonate pathway (Figure 7 and Table S4).

### [14] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.678)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

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
  - Snippet 1 (score: 0.676)
    > In an effort to engage the collective expertise of the scientific community, we have implemented a collaborative wiki (MediaWiki version 1.19.11) for the Mnemiopsis gene complement. The Mnemiopsis Gene Wiki is accessible from the left sidebar of most pages and is searchable either by selecting a Mnemiopsis gene identifier (e.g., ML00011a) from the drop-down menu or by manually entering an identifier in the appropriate search box. Users can also access these pages by clicking on a gene in the 2.2 track of the genome browser. Each record in the Gene Wiki represents a single Mnemiopsis gene and provides the following annotation: nucleotide and protein sequences, coding exonic genomic coordinates, pre-computed BLAST hits from numerous organisms displaying the top hits for each protein, the top non-self BLAST hit to Mnemiopsis, Pfam-A domains, Gene Ontology (GO) functional annotations, human disease genes from Online Mendelian Inheritance in Man (OMIM), and a table of ortholog clusters formed by phylogenetically informed clustering methods [4] (Figure 5). In addition, controlled editable sections have been included that permit (and encourage) the scientific community to provide further gene annotation for isoforms, in situ images, references, and other notes for each gene. Users interested in supplementing our gene model annotation at the Mnemiopsis Gene Wiki pages must first create an account and log in prior to submitting their contributions. In-house subject matter expert data curators are notified by e-mail following the creation of a new user account or an edit to an existing Gene Wiki record. Any content changes or additions to the Gene Wiki are thoroughly evaluated by these data curators and are made public subject to their approval.
    > Pre-compiled BLAST hits are enumerated in tabular form. Each Mnemiopsis protein was compared to the UniProt and NCBI non-redundant protein databases (nr) using BLASTP. The results display the hit number, the accession numbers, E-values, and brief descriptions of the top four hits (lowest E-values). Accession numbers are linked to relevant corresponding entries at UniProt and GenBank.

### [16] Transcriptomic responses of Microcystis aeruginosa under electromagnetic radiation exposure
- Authors: Chao Tang, Ziyan Zhang, Shen Tian, Peng Cai
- Year: 2021
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/bc965f1804c22c9b8b67454fa137e94208f752bf
- DOI: 10.1038/s41598-020-80830-z
- PMID: 33483577
- PMCID: 7822859
- Citations: 8
- Summary: The results suggest that the energy metabolism pathway may respond positively to electromagnetic radiation, and that electromagnetic radiation may inhibit protein synthesis and affect cyanobacterial energy metabolism and photosynthesis.
- Evidence snippets:
  - Snippet 1 (score: 0.675)
    > Differentially expressed genes analysis. Between the treatment and control groups, 306 differentially expressed genes were determined, 121 and 185 of which were upregulated and downregulated, respectively (Fig. 1). The full list of differentially expressed genes with the fold change and false discovery rate (FDR) detailed can be found as Supplementary Table S1.
    > Pathway enrichment analysis of differentially expressed genes. Exposure of M. aeruginosa to electromagnetic radiation caused significant differential gene expression and corresponding enrichment of the ribosome, oxidative phosphorylation and carbon fixation in photosynthetic pathways of organisms (Table 1).
    > Sixteen differentially expressed genes were present on the ribosome pathway under electromagnetic stress. The corresponding differentially expressed genes are listed in Table 2. The expression of genes regulating 30S ribosomal proteins S3, S8, S9, S10, S17, and S19 and 50S ribosomal proteins L2, L5, L6, L13, L14, L15, L16, L22, L24, and L29 was downregulated.
    > Fourteen differentially expressed genes were present on the oxidative phosphorylation pathway of M. aeruginosa under electromagnetic stress. Among them, 13 were downregulated, and 1 was upregulated. The corresponding differentially expressed genes are listed in Table 2. The expression of genes regulating NAD(P)H dehydrogenase, subunit NdhF3 family protein, proton-translocating NADH-quinone oxidoreductase, chain M family protein, NADH-ubiquinone/plastoquinone oxidoreductase chain 6 family protein, and NAD(P)H-quinone oxidoreductase subunit 1, 2, I was downregulated. Moreover, the expression of genes regulating ATP synthase subunit alpha, b' , b, beta, delta, gamma, and epsilon chains was downregulated. By contrast, the expression of genes regulating succinate dehydrogenase/fumarate reductase and flavoprotein subunit was upregulated. Seven differentially expressed genes were related to carbon fixation.

### [17] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2771
- Influential citations: 298
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [18] Single-Cell Genomics of Novel Actinobacteria With the Wood–Ljungdahl Pathway Discovered in a Serpentinizing System
- Authors: Nancy Merino, M. Kawai, E. Boyd, D. Colman, S. McGlynn et al.
- Year: 2020
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/5152e19ea06f6a82eff8f591579cdebed89552a3
- DOI: 10.3389/fmicb.2020.01031
- PMID: 32655506
- PMCID: 7325909
- Citations: 27
- Summary: This is the first report and detailed genome analysis of a bacterium within the Actinobacteria phylum capable of utilizing the Wood–Ljungdahl (WL) pathway, and proposes to name this bacterium ‘Candidatus Hakubanella thermoalkaliphilus’.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > The gene neighborhood was designed using Gene Graphics (Harrison et al., 2017). Abbreviations: apbE (Mg 2+ -dependent flavin transferase), apgM (2,3-bisphosphoglycerate-independent phosphoglycerate mutase), coo (carbon monoxide dehydrogenase), fdh (formate dehydrogenase), fix (electron transfer flavoprotein), gdhA (glutamate dehydrogenase), hdr (heterodisulfide reductase), hemE (uroporphyrinogen decarboxylase), hppA (K + -stimulated pyrophosphate-energized sodium pump), met (methylenetetrahydrofolate reductase), mvhD (F420-non-reducing hydrogenase iron-sulfur subunit), ndh (NAD(P)H-quinone oxidoreductase), nuo (NADH-quinone oxidoreductase), nosZ (nitrous oxide reductase), rnf (Na + -translocating ferredoxin:NAD + oxidoreductase), PF07992 (Pyridine nucleotide-disulphide oxidoreductase), por (pyruvate ferredoxin oxidoreductase), trk (Trk system potassium uptake protein), trmU (tRNA-uridine 2-sulfurtransferase).
    > Notably, the Hakuba co-assembly is the only genome amongst the three clades to harbor a hybrid CODH/ACS consisting of both archaeal-(cdhABC) and bacterial-type (acsCDE) subunits (Figure 2 and Supplementary Figure S7). Although the Hakuba co-assembly did not contain the entire gene cluster for the CODH/ACS complex on one contig, the Hakuba SAG S03 had the full operon of acsED-cdhABC-acsC, in addition to separate gene clusters containing another acsC, a split acsD, and a split acsE (Figure 2B).

### [19] Bioinformatics-Based Assessment of the Relevance of Candidate Genes for Mutation Discovery
- Authors: M. Slota, M. Maluszynski, I. Szarejko
- Year: 2017
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/1d07fbf9f7b1e87126e9de66cf91c6e68422ee79
- DOI: 10.1007/978-3-319-45021-6_17
- Citations: 3
- Summary: The bioinformatics resources provide a wide range of tools that can be applied in different areas of mutation screening and there are available tools enabling a proper design of oligonucleotide primers for the amplification of a gene fragment for the purpose of mutation screened.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > 1. Search for a specific GO annotation of a gene that is of interest using QuickGO browser for gene ontology [http://www.ebi.ac.uk/QuickGO/]. GO search can be conducted using a gene/protein name, symbol, accession number or description word as a query. 2. Obtained GO annotation data consists of three main aspects: molecular process involvement (P), molecular function (F) and localisation in specific component (C). 3. Analyse the QuickGO result table which contains a specific GO terms and identifiers, type of evidence and the affiliation to a database which created the annotation. 4. You can visualise and/or download annotation statistics in .xls format. Statistics reports contain the information on the frequency of covered ontology aspect: molecular process involvement/molecular function/localisation in specific component, the percentage of different types of evidence-experimental (EXP), direct Assay (IDA), physical interaction (IPI), mutant phenotype (IMP), genetic interaction (IGI), expression pattern (IEP) and the frequency of annotation to distinct taxon. 5. Additionally, a created gene list can be classified in terms of specific GO annotation for different ontology categories. 6. Perform a singular enrichment analysis (SEA) using an agriGO [http://bioinfo. cau.edu.cn/agriGO/] database. 7. Paste a gene symbols list compatible to an input format as well as the reference (user may choose between the genomic background and customised annotated reference which consist of a second group of GO annotation data).
    > 8. Browse a Detail information table to check the enrichment of input gene targets for different GO terms. GO term can be considered significantly enriched, if the parameter of false discovery rate (FDR) is <0.05 and p-value is <0.01 when compared to all the gene transcripts annotated in the selected genomic background or the set of genes applied as the background. 9. AgriGO tool uses a gene list input to create GO terms abundance chart for the provided accessions (Fig. 17.2). 10.

### [20] MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila
- Authors: Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al.
- Year: 2025
- Venue: Synthetic and Systems Biotechnology
- URL: https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
- DOI: 10.1016/j.synbio.2025.04.001
- PMID: 40276250
- PMCID: 12018684
- Summary: Shifts in metabolic allocation in a glucoamylase hyperproduction strain of M. thermophila are identified, highlighting changes in fatty acid biosynthesis and amino acids biosynthesis pathways, which provide new insights into the underlying phenotypic alterations.
- Evidence snippets:
  - Snippet 1 (score: 0.668)
    > Single-gene search: Gene annotation is essential for biologists to understand a gene's function. MTD's single-gene search interface allows researchers to obtain a comprehensive gene description by entering or selecting a gene ID. The results include sequence information, CAZy family, Pfam domains, GO/KEGG annotations, and phenotype information (Fig. 2D), along with sequence-based predictions such as optimal protein activity temperature, melting temperature (Tm), subcellular localization, and transcription factor scores. To enhance data accessibility, links to external databases such as NCBI, KEGG, FungiDB [4], UniProt, and JGI are also provided, facilitating cross-referencing of gene annotations across various resources.
    > Unlike the static genome, the transcriptome captures dynamic gene expression changes in response to developmental or environmental conditions, establishing a dynamic link between an organism's genome and its physical characteristics [63]. In the single-gene retrieval interface, the expression of the searched gene is visualized in the form of box plots and scatter plots across transcriptome datasets (Fig. 2E). When hovering over any data point, users can view the corresponding experimental details, such as mutant name, sample processing methods, and growth conditions. This interactive feature reveals gene expression responses to environmental factors, allowing researchers to quickly identify experimental conditions of interest and explore the gene's potential roles in diverse biological contexts. Moreover, clicking on the dataset title will direct users to the GEO browser for further detailed descriptions. KEGG Pathway or Gene List Search: In transcriptome studies, researchers typically adopt a "bottom-up" approach: first sequencing all mRNA in a cell, identifying differentially expressed genes between conditions, and then performing GO/KEGG enrichment analysis to interpret functional distributions. MTD, however, offers a complementary "top-down" search strategy, enabling users to examine the expression of genes within a specific KEGG pathway (Fig. 3A) or a user-defined gene set. A unique feature of MTD is its manually curated data categorization system, which organizes sample data with detailed annotations based on experimental conditions.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al. (2018). Ten steps to get started in Genome Assembly and Annotation. F1000Research. https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
5. Xinru Cai, Song Zhang, Jia Lin, Yaxu Wang, Fa-Bing Ye et al. (2022). Role of the Gene ndufs8 Located in Respiratory Complex I from Monascus purpureus in the Cell Growth and Secondary Metabolites Biosynthesis. Journal of Fungi. https://www.semanticscholar.org/paper/5211255ad6045e484b52456db63359041616fd33
6. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
7. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
8. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
9. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
10. Nagaraja Reddy Rama Reddy, Rucha Harishbhai Mehta, Palak Soni, Jayanti Makasana, N. Gajbhiye et al. (2015). Next Generation Sequencing and Transcriptome Analysis Predicts Biosynthetic Pathway of Sennosides from Senna (Cassia angustifolia Vahl.), a Non-Model Plant with Potent Laxative Properties. PLoS ONE. https://www.semanticscholar.org/paper/fec6263b90f9cd765752bdb1be3d162872f2e64e
11. Anthony C. Smith, A. Robinson (2009). MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data. Molecular & Cellular Proteomics : MCP. https://www.semanticscholar.org/paper/206a60d6d387688ce7f880e0dfe67af5a723c7b8
12. K. Anderson, Daisy A. Taylor, E. Thompson, A. Melwani, S. Nair et al. (2015). Meta-Analysis of Studies Using Suppression Subtractive Hybridization and Microarrays to Investigate the Effects of Environmental Stress on Gene Transcription in Oysters. PLoS ONE. https://www.semanticscholar.org/paper/2e1f7fa1a93ee5206f397d90f45aefcdf8e0faff
13. A. Yelton, B. Thomas, S. Simmons, P. Wilmes, A. Zemla et al. (2011). A Semi-Quantitative, Synteny-Based Method to Improve Functional Predictions for Hypothetical and Poorly Annotated Bacterial and Archaeal Genes. PLoS Computational Biology. https://www.semanticscholar.org/paper/88870437e2914eb4a8ed4914fe4f867e96372670
14. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
15. R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al. (2014). A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi. BMC Genomics. https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
16. Chao Tang, Ziyan Zhang, Shen Tian, Peng Cai (2021). Transcriptomic responses of Microcystis aeruginosa under electromagnetic radiation exposure. Scientific Reports. https://www.semanticscholar.org/paper/bc965f1804c22c9b8b67454fa137e94208f752bf
17. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
18. Nancy Merino, M. Kawai, E. Boyd, D. Colman, S. McGlynn et al. (2020). Single-Cell Genomics of Novel Actinobacteria With the Wood–Ljungdahl Pathway Discovered in a Serpentinizing System. Frontiers in Microbiology. https://www.semanticscholar.org/paper/5152e19ea06f6a82eff8f591579cdebed89552a3
19. M. Slota, M. Maluszynski, I. Szarejko (2017). Bioinformatics-Based Assessment of the Relevance of Candidate Genes for Mutation Discovery. https://www.semanticscholar.org/paper/1d07fbf9f7b1e87126e9de66cf91c6e68422ee79
20. Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al. (2025). MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila. Synthetic and Systems Biotechnology. https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba