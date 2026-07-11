---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T11:44:58.288819'
end_time: '2026-07-10T11:45:03.196248'
duration_seconds: 4.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rlmH
  gene_symbol: rlmH
  uniprot_accession: Q88DL7
  protein_description: 'RecName: Full=Ribosomal RNA large subunit methyltransferase
    H {ECO:0000255|HAMAP-Rule:MF_00658}; EC=2.1.1.177 {ECO:0000255|HAMAP-Rule:MF_00658};
    AltName: Full=23S rRNA (pseudouridine1915-N3)-methyltransferase {ECO:0000255|HAMAP-Rule:MF_00658};
    AltName: Full=23S rRNA m3Psi1915 methyltransferase {ECO:0000255|HAMAP-Rule:MF_00658};
    AltName: Full=rRNA (pseudouridine-N3-)-methyltransferase RlmH {ECO:0000255|HAMAP-Rule:MF_00658};'
  gene_info: Name=rlmH {ECO:0000255|HAMAP-Rule:MF_00658}; OrderedLocusNames=PP_4808;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the RNA methyltransferase RlmH family.
  protein_domains: Alpha/beta_knot_MTases. (IPR029028); RlmH-like. (IPR003742); tRNA_m1G_MTases_N.
    (IPR029026); SPOUT_MTase (PF02590)
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
- **UniProt Accession:** Q88DL7
- **Protein Description:** RecName: Full=Ribosomal RNA large subunit methyltransferase H {ECO:0000255|HAMAP-Rule:MF_00658}; EC=2.1.1.177 {ECO:0000255|HAMAP-Rule:MF_00658}; AltName: Full=23S rRNA (pseudouridine1915-N3)-methyltransferase {ECO:0000255|HAMAP-Rule:MF_00658}; AltName: Full=23S rRNA m3Psi1915 methyltransferase {ECO:0000255|HAMAP-Rule:MF_00658}; AltName: Full=rRNA (pseudouridine-N3-)-methyltransferase RlmH {ECO:0000255|HAMAP-Rule:MF_00658};
- **Gene Information:** Name=rlmH {ECO:0000255|HAMAP-Rule:MF_00658}; OrderedLocusNames=PP_4808;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the RNA methyltransferase RlmH family.
- **Key Domains:** Alpha/beta_knot_MTases. (IPR029028); RlmH-like. (IPR003742); tRNA_m1G_MTases_N. (IPR029026); SPOUT_MTase (PF02590)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rlmH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rlmH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rlmH** (gene ID: rlmH, UniProt: Q88DL7) in PSEPK.

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
  - Snippet 1 (score: 0.778)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.754)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [4] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
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
  - Snippet 1 (score: 0.742)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [5] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Citations: 1
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.737)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [6] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.734)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

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

### [8] CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts
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
  - Snippet 1 (score: 0.721)
    > Whole-genome sequencing has enabled investigations into the gene content of living many organisms and forms the foundation for further study of gene expression, proteomics and epigenetics. After assembly of a novel genome, gene annotation is often the first step in analysing the gene content of an organism. Accurate annotation of the exonic structure of genes is crucial to the success of all subsequent functional and comparative analyses.
    > Problems that can potentially be caused by incorrect gene annotation are numerous and can lead to incorrect assessments of the lifestyle and ecology of an organism. In comparative genomics where orthologous genes or conserved functional domains are compared between species/isolates, the estimated numbers of such genes/ domains can be distorted by less than perfect annotations (as described by Hane et al. [1], S Text 1). Prediction of extracellular secretion, which can be determined by a short signal peptide at the N-terminus, can miss secreted proteins if the start codon of a gene has been incorrectly annotated. Mis-annotating the start of protein translation could either cut off the signal peptide or bury it within the annotation. While a seemingly benign annotation error, the consequences for downstream research could be detrimental, particularly as the biotic interactions or industrial applications of microbes are largely determined by their secretomes. Additionally, translated protein sequences of novel species are often submitted to databases such as NCBI [2] and Uniprot [3]. It is commonplace to use these database entries to support the annotation of related species or isolates, meaning errors present in the pioneer annotation may be repeated. When these new annotations based on false assumptions are added to databases, there is not only a propagation of errors, but also a perceived strengthening of homology evidence for incorrect protein sequences.
    > In recent years, correction of in silico predicted gene annotations with RNA-seq derived transcripts and read alignments has enabled vastly improved genome annotations and corrections of annotated gene structures [4][5][6].

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
  - Snippet 1 (score: 0.716)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [10] Characterization of holins, the membrane proteins of coliphage ASEC2201: a genomewide in silico approach
- Authors: Humaira Saeed, Sudhaker Padmesh, Aditi Singh, S. Singh, Mohammed Haris Siddiqui et al.
- Year: 2025
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/a39392e12bf3bda67bdfe600053e8403deb3b887
- DOI: 10.3389/fmicb.2025.1550594
- PMID: 40703241
- PMCID: 12283622
- Citations: 4
- Summary: In silico identification of cell-penetrating peptide motifs within the holin sequences suggests potential for enhanced intracellular delivery in CPP-fusion therapeutic constructs and demonstrates the potential of integrative in silico approaches in developing a comprehensive foundation for future experimental validation for proteins with no prior functional annotation.
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > Protein-coding gene annotation is typically a two-step process. Initially, Prodigal is employed to identify open reading frames (ORFs) by locating gene coordinates, but it does not infer gene function. To assign putative functions, Prokka performs hierarchical annotation by comparing candidate genes to curated protein databases. It begins with a user-supplied, high-confidence protein set, using BLAST+ for sequence similarity searches. If no match is found, it progresses to UniProt's verified bacterial proteins, covering \~ 16,000 sequences, and then optionally to RefSeq proteins specific to the organism's genuscapturing nomenclature consistency. When sequence-based annotation fails, Prokka applies profile-based searches using HMMER's hmmscan to query against Pfam and TIGRFAMs databases. An e-value threshold of 10 −6 is consistently applied to ensure significance. If no reliable match is found across all levels, the gene is designated as a "hypothetical protein. " This layered strategy maximizes annotation accuracy and functional insight across diverse bacterial genomes (Seemann, 2014).
    > The genome of coliphage ASEC2201 has been analyzed and three holin protein coding genes were selected. The sequences of all three holin proteins were retrieved from NCBI using accession no. SRX17770782 in the FASTA format. The sequence similarity search was performed via BLAST against the non-redundant database (Altschul et al., 1990).

### [11] Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids
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
  - Snippet 1 (score: 0.707)
    > We chose cell migration genes and proteases/inhibitors as candidate virulence factors, due to their relevance in hostpathogen interactions (e.g., Barragan and Sibley 2002;McKerrow et al. 2006;Bouzid et al. 2013). Given the low amount of functional (GO) annotation in our largest assembly, C. shasta þ NHP (see Results), we used BlastX to search for homologs of genes of interest in two custom concatenated databases that comprised the Cell Migration Knowledge Database (CMKB) which includes proteins, families, and complexes involved in cell migration (http://www.cellmigration. org/index.shtml, last accessed February 5, 2015; $7,600 protein sequences), and the MEROPS database, which consists of a nr library of full-length sequences of peptidases and peptidase inhibitors (http://merops.sanger.ac.uk/, last accessed December 2, 2014; $450,000 sequences; Rawlings et al. 2016). We searched using the longest representatives for each gene in the C. shasta þ NHP assembly (23,418 contigs; IIR-RBT6) then parsed matches (bit score > 100) and posteriorly classified homologs to proteases or motility genes matching the specific databases. We then selected only genes with the same annotation in UniProt (determined using the same standards: no ambiguous terms filtering, bit score > 100) to confirm gene identity. Due to disagreements between annotations (CMKB vs. UniProt, and MEROPS vs. UniProt), we curated gene lists manually, removing genes that matched one or more of the following criteria: 1) no genetic distances available (only available for reference); 2) disagreements between annotations from the different databases, after checking for synonyms or function similarity; 3) annotations that contained terms from UniProt "Uncharacterized protein" and "Predicted protein" (ambiguous terms), and whose identity could not be confirmed; and 4) annotations that contained nonspecific terms, such as "heat shock protein" or "ribosomal protein."

### [12] A high-quality genome for the slender anole (Anolis apletophallus): an emerging model for field studies of tropical ecology and evolution
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
  - Snippet 1 (score: 0.705)
    > MAKER, SNAP, and AUGUSTUS (with intron-exon boundary hints provided from RNA-seq) were then used to predict genes in the repeat-masked reference genome. To help guide the prediction process, Swiss-Prot peptide sequences from the UniProt database were downloaded and used in conjunction with the protein sequences from A. carolinensis, L. agilis, and Z. vivipara to generate peptide evidence in the MAKER pipeline. Only genes that were predicted by both SNAP and AUGUSTUS were retained in the final gene sets. To assess the quality of gene prediction, Annotation Edit Distance (AED) scores were generated for each of the predicted genes as part of the MAKER pipeline. Fourth, we curated the genome manually, during which we verified and corrected a preselected list of genes. We preselected genes that are biologically relevant for our focal species and our current research, such as arginyl-tRNA synthetase (RARS), heat shock protein family (HSP40), heat shock protein family A (HSP70), and the heat shock protein 90 (HSP90). Lastly, genes were further characterized for their putative function by performing a BLAST search of the peptide sequences against the UniProt database. tRNA were predicted using the software tRNAscan-SE (version 2.05).

### [13] OntoGene in BioCreative II
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
  - Snippet 1 (score: 0.703)
    > It is well known that protein names are highly ambiguous [45,46]. Researchers working in specific subcommunities tend to develop their own nomenclature, resulting in multiple names for the same protein. Acronyms and abbreviations further complicate the picture. Simply being able to recognize a protein name as such is just a starting point. The name needs then to be unambiguously qualified, by referring to an entry in a standard protein database, such as UniProt http:// www.expasy.org/sprot/ [47].
    > In order for that to happen, the disambiguation must occur at two levels: interspecies (to which specific organisms does the protein mention refer?) and intraspecies (within a given organism, which specific protein is meant?). For example, a protein mentioned in text as eIF4E could refer to a large number of different proteins. A search in the Swiss-Prot section of UniProt (the manually curated section) delivers 46 possible matches. However, if the term appears contextually with the mention of a specific organism, like in the sentence 'The Cap-binding protein eIF4E promotes folding of a functional domain of yeast translation initiation factor eIF4G1' (PubMed: 10409688), then it is reasonable to assume that the name refers to a specific organism (yeast), thus restricting the possible matches in UniProt to the following two: EAP1_YEAST (eIF4E-associated protein 1) and IF4E_YEAST (eukaryotic translation initiation factor 4E). For the task of protein annotation, we have adopted a high-recall, low-precision term annotation approach, followed by very strict disambiguation steps, which gradually increase precision (at some expense for recall).
    > UniProt contains for each protein a list of frequently used synonyms, as well as the name and synonyms of its encoding gene. We have built a database that maps the synonyms to the protein identifier. We have further enriched such a list using morpho-syntactic rules that generate variants of the synonyms. Starting from the subset of UniProt delivered by the BioCreative organizers (which contained 228,

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
  - Snippet 1 (score: 0.700)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [15] ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance
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
  - Snippet 1 (score: 0.699)
    > To reduce redundancy while preserving sequence diversity, the 235,441 validated ORFs were subjected to two-stage clustering using VSEARCH v2.21.1: first at 90% sequence identity, then refined at 95% identity. Cluster representatives were aligned against UniProt/Swiss-Prot (release 2024_01) using DIAMOND v2.0.15 in sensitive mode (--sensitive). The initial alignment yielded 62,689 ORFs with putative UniProt matches. For each match, protein names, functional descriptions, and Gene Ontology (GO) terms were extracted for downstream label assignment.
    > 2.1.4. Functional labeling. Functional labels (Enzymatic, Structural, Transport, Other) were assigned to the 62,689 UniProt-mapped ORFs using hierarchical keyword matching against a curated dictionary of 847 functional terms derived from UniProt protein descriptions and Gene Ontology annotations. The classification hierarchy prioritized primary molecular functions:
    > • Enzymatic: Proteins with catalytic activity (GO:0003824), including polymerases, proteases, methyltransferases, and helicases
    > • Structural: Proteins involved in virion assembly and structural maintenance (GO:0019012), including spike, envelope, membrane, and nucleocapsid proteins
    > • Transport: Proteins mediating membrane transport and ion channels (GO:0006810, GO:0015267)
    > • Other: All remaining ORFs, including regulatory proteins, accessory factors, and hypothetical proteins ORFs with ambiguous or conflicting annotations (e.g., proteins with both enzymatic and structural roles) were manually reviewed by two independent annotators, achieving 94.2% inter-annotator agreement (Cohen's κ = 0.92). After removing ambiguous cases, this resulted in 53,575 unique labeled ORF sequences with unambiguous functional assignments.The 'Other' category encompasses a functionally heterogeneous set of accessory proteins with distinct biological roles, as summarized in Table 1 Variants were filtered to retain only those with ≥2% sequence divergence from their corresponding base ORF to ensure meaningful diversity while maintaining functional annotation consistency.

### [16] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.695)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [17] Ten steps to get started in Genome Assembly and Annotation
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
  - Snippet 1 (score: 0.691)
    > The ultimate goal of the functional annotation process (Figure 4) is to assign biologically relevant information to predicted polypeptides, and to the features they derive from (e.g. gene, mRNA). This process is especially relevant nowadays in the context of the NGS era due to the capacity of sequencing, assembling, and annotating full genomes in short periods of time, e.g. less than a month. Functional elements could range from putative name and/or symbols for protein-coding genes, e.g. ADH to its putative biological function, e.g. alcohol dehydrogenase, associated gene ontology terms, e.g. GO:0004022, functional sites, e.g. METAL 47 47 Zinc 1, and domains, e.g. IPR002328, among other features. The function of predicted proteins can be computationally inferred based on the similarity between the sequence of interest and other sequences in different public repositories, e.g. BLASTP against Uniprot. Caution should be taken when assigning results merely based on sequence similarity as two evolutionary independent sequences which share some common domains could be considered homologs 62 . Thus, whenever possible, it is better to use orthologous sequences for annotation purposes rather than simply similar sequences 63 . With the growing number of sequences in those public repositories, it is possible to perform various searches and combine obtained results into a consensus annotation. The accurate assignment of the functional elements is a complex process, and the best annotation will involve manual curation.
    > There are two main outcomes of the functional annotation process. The first is the assignment of functional elements to genes. Downstream analysis of these elements allow further understanding of specific genome properties, e.g. metabolic pathways, and similarities compared with closely related species. The second result of the functional annotation is the additional quality check for the predicted gene set. It is possible to identify problematic and/or suspicious genes by the presence of specific domains, suspicious orthology assignment and/or absence of other functional elements, e.g. functional completeness. These Page 13 of 19

### [18] Prediction of Horizontally and Widely Transferred Genes in Prokaryotes
- Authors: Yoji Nakamura
- Year: 2018
- Venue: Evolutionary Bioinformatics Online
- URL: https://www.semanticscholar.org/paper/af7bde229b96609907924d1c68ea463af656efb2
- DOI: 10.1177/1176934318810785
- PMID: 30546254
- PMCID: 6287321
- Citations: 5
- Influential citations: 1
- Summary: A data-driven approach using massive sequence data may contribute to a broader understanding of HGT in prokaryotes, and predicted that six as-yet-uncharacterized genes were widely distributed HT genes, and therefore, will be interesting targets for evolutionary studies.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > Focusing on uncharacterized HT genes in the COG and KEGG databases, four gene groups (COG3209, COG1479, COG3291, and COG3791) were classified into "general function prediction only" (COG category code = R) or "function unknown" (S) according to the COG annotation. By adding two gene groups of "uncharacterized protein" (K08998 and K07062) from the KEGG annotation, a total of six were obtained as functionally ambiguous HT gene groups despite being distributed among more than 300 species. With reference to COG3209 (uncharacterized conserved protein RhaS, contains 28 RHS repeats), the genes encoded in E. coli have been suggested to be horizontally transferred from another organism. 43 Recently, RHS repeat-containing genes are reported to be involved in toxins against competitors 44 ; therefore, the genes in COG3209 could be considered as defense system genes. The functions of COG1479 (uncharacterized conserved protein, contains ParB-like and HNH nuclease domains), COG3291 (PKD repeat), and COG3791 (uncharacterized conserved protein) have yet to be examined. According to InterPro analysis, COG3791 genes have a domain of glutathione-dependent formaldehyde-activating enzyme (IPR006913); therefore, these genes might be related to formaldehyde detoxification. 45 The KO group, K08998, corresponds to COG0759 (membraneanchored protein YidD) of category M in the COG database that has previously been reported to be involved in the protein insertion process. 46 K07062 corresponds to COG1487 and is considered a toxic protein. 47 As a whole, it has to be said that the evolutionary significance of these six gene groups has not been fully realized. Conversely, these genes might be good targets for evolutionary studies in the context of HGT, providing an example of data-driven approaches from massive sequence data. 48

### [19] Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes
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
  - Snippet 1 (score: 0.688)
    > To inspect the transcriptomics result of individual genes, proteins originating from JGI have a hyperlink to a summary page which links to a 'Genome browser' page that displays the predicted gene splicing, including which regions have RNA support (Figure 1 D).
    > Hence, in the protein specific site in the JGI w e bsite under 'To Genome Browser', the current protein (GeneCatalog) can be seen together with se v eral other alternati v e predictions of the gene splicing, which is essential to have correct, for the protein to function naturally (Figure 2 ).
    > As the RNA coverage supports the exon / intron splicing, it is possible to infer whether a particular gene, in this case Table 1. Comparison between the dbCAN webserver, the eggNOG webserver for both family and functional annotation of CAZymes and the updated CUPP-w e bserver using the recommended significance cut-off at 5. The column 'CAZy -All characterized' encompasses all 10784 characterized proteins in the CAZy database used for the training, whereas the 'CAZy -Newly characterized '   a gene such as the one selected in Figure 2 , is more likely to work after heterologous gene expression.
    > To further improve the enzyme selection, all NCBI Genbank accessions were mapped to Uniprot ID to link to the specific Uniprot accession page including the predicted Al-phaFold structures, Go annotations and InterPro annotations and more ( 19 ).

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
  - Snippet 1 (score: 0.687)
    > Each genome was given a unique identifier, which was derived from the NCBI accession of the corresponding assembly, but without version number. For example, a genome with assembly accession "GCF_000123456.1" was identified as "G000123456" in this study. In cases when the same genome was present in both GenBank (accession starting with "GCA_") and RefSeq (accession starting with "GCF_"), only the RefSeq version was kept.
    > Annotation and classification of marker genes. The functional annotation of the 400 PhyloPhlAn marker genes 25 was performed by aligning the protein sequences of the 400 marker genes (inferred from 2887 bacterial and archeal genomes as described in Segata et al. 25 ) against the UniRef50 database (March 2018 release) using BLASTp. The best hit for each gene was taken and queried against the UniProt database for gene and protein names. To categorize genes by function, the UniProt entries were translated into Gene Ontology (GO) terms 40 with the "sub-set_prokaryote" tag (March 2018 release). Because not all UniProt entries have corresponding GO terms, manual curation was involved to pick the most appropriate GO terms for those cases by examining the BLAST hit table. GO terms were further translated into GO slim terms to obtain higher-level functional categories.
    > Note that this analysis is independent from the phylogenetic analysis of the current genome data set, and the result can be used as a reference for PhyloPhlAn users.
    > Analyses of genome sequences and identification of marker genes. The DNA sequences of the 86,200 bacterial and archaeal genomes were subjected to the following analyses:
    > 1. The quality scores for DNA, protein, tRNA, and rRNA were calculated following Land et al. 41 . 2. A MinHash sketch was built for each genome using Mash 1.1.1 42 , with default settings (sketch size = 1000, k-mer size = 21), based on which a pairwise distance matrix was built for the entire genome pool. In brief, MinHash is a k-mer hashing technique that enables the quantification of genome-to-genome distance.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
5. Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
6. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
7. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
8. Alison C. Testa, James K. Hane, S. Ellwood, R. Oliver (2015). CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts. BMC Genomics. https://www.semanticscholar.org/paper/06704917bf44cd62eef0bb5cb944b97484056e21
9. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
10. Humaira Saeed, Sudhaker Padmesh, Aditi Singh, S. Singh, Mohammed Haris Siddiqui et al. (2025). Characterization of holins, the membrane proteins of coliphage ASEC2201: a genomewide in silico approach. Frontiers in Microbiology. https://www.semanticscholar.org/paper/a39392e12bf3bda67bdfe600053e8403deb3b887
11. G. Alama-Bermejo, E. Meyer, S. Atkinson, A. Holzer, Monika M. Wiśniewska et al. (2020). Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids. Genome Biology and Evolution. https://www.semanticscholar.org/paper/7d5e64908d9bea80accb9389be84679778625620
12. Renata M. Pirani, Carlos F Arias, Kristin Charles, Albert K. Chung, J. D. Curlis et al. (2023). A high-quality genome for the slender anole (Anolis apletophallus): an emerging model for field studies of tropical ecology and evolution. G3: Genes|Genomes|Genetics. https://www.semanticscholar.org/paper/3856bf1b43601b80987242d1858d505dd3167fd1
13. Fabio Rinaldi, T. Kappeler, K. Kaljurand, Gerold Schneider, Manfred Klenner et al. (2007). OntoGene in BioCreative II. Genome Biology. https://www.semanticscholar.org/paper/ffcbf659129388203ce458ce1b25e5449e9594e7
14. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
15. FuGuo Liu, T. Lai, Wenxia Xu, Guodong Li (2026). ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance. PLOS One. https://www.semanticscholar.org/paper/7d7965ec223f5715675839cb57efdc776d25e216
16. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
17. Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al. (2018). Ten steps to get started in Genome Assembly and Annotation. F1000Research. https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
18. Yoji Nakamura (2018). Prediction of Horizontally and Widely Transferred Genes in Prokaryotes. Evolutionary Bioinformatics Online. https://www.semanticscholar.org/paper/af7bde229b96609907924d1c68ea463af656efb2
19. Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer (2023). Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes. Nucleic Acids Research. https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
20. Qiyun Zhu, U. Mai, W. Pfeiffer, Stefan Janssen, F. Asnicar et al. (2019). Phylogenomics of 10,575 genomes reveals evolutionary proximity between domains Bacteria and Archaea. Nature Communications. https://www.semanticscholar.org/paper/7e3866b2d5d92fc28f91181a5393610760cba94d