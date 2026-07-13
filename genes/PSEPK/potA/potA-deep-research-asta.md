---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T10:57:42.644972'
end_time: '2026-07-09T10:57:48.679030'
duration_seconds: 6.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: potA
  gene_symbol: potA
  uniprot_accession: Q88QS7
  protein_description: 'RecName: Full=Spermidine/putrescine import ATP-binding protein
    PotA {ECO:0000256|RuleBase:RU364083}; EC=7.6.2.11 {ECO:0000256|RuleBase:RU364083};'
  gene_info: Name=potA {ECO:0000256|RuleBase:RU364083}; OrderedLocusNames=PP_0411
    {ECO:0000313|EMBL:AAN66041.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ABC transporter superfamily.
  protein_domains: AAA+_ATPase. (IPR003593); ABC_SmlMolc_Importer. (IPR050093); ABC_transporter-like_ATP-bd.
    (IPR003439); ABC_transporter-like_CS. (IPR017871); Mo/tungstate-bd_C_term_dom.
    (IPR008995)
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
- **UniProt Accession:** Q88QS7
- **Protein Description:** RecName: Full=Spermidine/putrescine import ATP-binding protein PotA {ECO:0000256|RuleBase:RU364083}; EC=7.6.2.11 {ECO:0000256|RuleBase:RU364083};
- **Gene Information:** Name=potA {ECO:0000256|RuleBase:RU364083}; OrderedLocusNames=PP_0411 {ECO:0000313|EMBL:AAN66041.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC transporter superfamily.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_SmlMolc_Importer. (IPR050093); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); Mo/tungstate-bd_C_term_dom. (IPR008995)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "potA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'potA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **potA** (gene ID: potA, UniProt: Q88QS7) in PSEPK.

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
  - Snippet 1 (score: 0.745)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.669)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

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
  - Snippet 1 (score: 0.720)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [3] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.720)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

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
  - Snippet 1 (score: 0.711)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [5] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.710)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

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
  - Snippet 1 (score: 0.695)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [7] The quality of metabolic pathway resources depends on initial enzymatic function assignments: a case for maize
- Authors: Jesse R. Walsh, M. Schaeffer, Peifen Zhang, S. Rhee, J. Dickerson et al.
- Year: 2016
- Venue: BMC Systems Biology
- URL: https://www.semanticscholar.org/paper/c41be7766c80fddb3f81c57ced799b8562370cc8
- DOI: 10.1186/s12918-016-0369-x
- PMID: 27899149
- PMCID: 5129634
- Citations: 11
- Influential citations: 1
- Summary: CornCyc’s computational predictions are more accurate than those in MaizeCyc when compared to experimentally determined function assignments, demonstrating the relative strength of the enzymatic function assignment pipeline used to generate CornCyc.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > A gold standard set of protein functional annotations was generated by extracting data from UniProt [16] and BRENDA [17]. We extracted all protein sequence and annotation data from UniProt (release 2016_05) for the organism Zea mays, keeping the EC annotations only from the manually reviewed component of UniProt, while removing those annotations that had not undergone manual review. We also extracted experimentally verified protein annotations for Zea mays from BRENDA (release 2016.1). The UniProt and BRENDA annotations were then merged by matching proteins based on the database crosslinks provided by BRENDA, resulting in the union of the reviewed annotations from UniProt and the experimentally verified annotations of BRENDA with duplicates removed. The merged protein annotations were then matched to the B73 RefGen_v2 translated gene models using BLASTP based on a sequence identity cutoff of 96% and an e-value cutoff of 1e-20. We selected the top scoring hit for each protein which resulted in matches to 1,815 unique maize proteins. EC annotations for alternate isoforms were consolidated at the gene level, resulting in 1,475 experimentally verified or manually reviewed protein functional annotations across 1,450 maize genes.

### [8] Protein Localization Analysis of Essential Genes in Prokaryotes
- Authors: Chong Peng, Feng Gao
- Year: 2014
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
- DOI: 10.1038/srep06001
- PMID: 25105358
- PMCID: 4126397
- Citations: 28
- Summary: A comprehensive protein localization analysis of essential genes in 27 prokaryotes including 24 bacteria, 2 mycoplasmas and 1 archaeon has been performed and shows that proteins encoded by essential genes are enriched in internal location sites, while exist in cell envelope with a lower proportion compared with non-essential ones.
- Evidence snippets:
  - Snippet 1 (score: 0.680)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

### [9] Network pharmacology- and molecular docking-based exploration of the molecular mechanism underlying Jianpi Yiwei Recipe treatment of gastric cancer
- Authors: Peng Chen, Huan-Yu Wu
- Year: 2024
- Venue: World Journal of Gastrointestinal Oncology
- URL: https://www.semanticscholar.org/paper/e443646ac4c9b1279858936d666dcd66993fe816
- DOI: 10.4251/wjgo.v16.i7.2988
- PMID: 39072163
- PMCID: 11271781
- Citations: 3
- Influential citations: 1
- Summary: Jianpi Yiwei Recipe plays a therapeutic role in GC through multiple components, targets, and pathways and form a basis for follow-up exploration of Jianpi Yiwei Recipe in the treatment of GC.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > After obtaining effective active components from relevant TCMs, we used TCMSP to obtain their corresponding targets, sorted the data, and deleted repetitive and unidentified components. The targets were imported into the UniProt database (https://www.uniprot.org/) one by one. Target protein names (official symbol) and UniProt ID numbers were retrieved, with retrieval condition Organism: Homo sapiens (Human). Unverified target genes were removed during the research.

### [10] Haplotype-resolved genome assembly of the tetraploid potato cultivar Désirée
- Authors: Tim Godec, Sebastian Beier, Natalia Yaneth Rodriguez-Granados, R. Sasidharan, L. Abdelhakim et al.
- Year: 2025
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/23a46e4cee0fdfcb5eec69a77ad783893a46d924
- DOI: 10.1038/s41597-025-05372-3
- PMID: 40541992
- PMCID: 12181383
- Citations: 4
- Influential citations: 1
- Summary: A haplotype-resolved genome assembly of Désirée is presented, achieved by assembling PacBio HiFi reads and Hi-C scaffolding, resulting in a high-contiguity chromosome-level assembly and a genome-wide DNA methylation profile using Oxford Nanopore reads, enabling insights into potato epigenetics.
- Evidence snippets:
  - Snippet 1 (score: 0.659)
    > plabipd.de/helixer_main.html). Gene models from the S. tuberosum reference genome (DM v6.1, UniTato annotation) were transferred to the Désirée assembly using Liftoff (v1.6.3) 51   were consolidated using Mikado (v2.3.4) 52 and UniProt plants database (review version 2024_04_22) 53 to generate a non-redundant set of transcripts. Protein-coding gene completeness was assessed using BUSCO (Tables 2, v5.4.7, solanales_odb10 dataset) and OMArk (v0.3.0, omamer v2.0.2) 54 . The quality of protein-coding gene annotations was assessed using PSAURON (v 1.0.4) 55 and results were added to the GFF3 annotation file. Transcriptomic data used for gene annotation was downloaded from public repositories: SRA under accessions SRP548344 34 , SRP545376 35 , SRP315827 41 , SRP358130 33 , SRP556848 36 and SRP547875 37 ; the Gene Expression Omnibus (GEO) under accession GSE232028 39 ; and the National Genomics Data Center (NGDC) under accession CRA006012 38 . Existing gene models used in the gene annotation pipeline were downloaded from https://unitato.nib.si and https://spuddb.uga.edu.
    > The predicted protein-coding genes were functionally annotated using EggNOG Mapper (v2.1.11) 56 with the EggNOG database (version 5.0.2) 57 for the Viridiplantae subset. This included categories such as gene names, Gene Ontologies (GOs), enzyme functions (EC), and KEGG pathways, reactions, and modules, along with CAZy families, PFAM domains, and more.

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
  - Snippet 1 (score: 0.656)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [12] A Genome-Wide Association Study Identifying Novel Genetic Markers of Response to Treatment with Interleukin-23 Inhibitors in Psoriasis
- Authors: Sophia Zachari, K. Liadaki, Angeliki Planaki, E. Zafiriou, Olga Kouvarou et al.
- Year: 2025
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/d5f656311b54e222e7487ea32a061869b30178a1
- DOI: 10.3390/genes16101195
- PMID: 41153410
- PMCID: 12564705
- Summary: These findings provide promising pharmacogenetic markers which, upon validation in larger, independent cohorts, will enable the translation of a patient’s genotype into a response phenotype, thereby guiding clinical decisions and improving drug effectiveness.
- Evidence snippets:
  - Snippet 1 (score: 0.656)
    > The UniProt knowledgebase (www.uniprot.org/uniprotkb/), (accessed on 20 June 2025), the central hub for the collection of functional information on proteins, with accurate and rich annotation [33], was used to retrieve the approved human gene and protein names and symbols.

### [13] Identifier Mapping in Cytoscape
- Authors: Adam Treister, Alexander R. Pico
- Year: 2018
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/c97ebea942d97f5336dd1a1a189c665ae83753ec
- DOI: 10.12688/f1000research.14807.2
- PMID: 30079244
- PMCID: 6053696
- Citations: 8
- Influential citations: 2
- Summary: The idmapper app for Cytoscape simplifies identifier mapping for genes and proteins in the context of common biological networks by providing a unified interface to different identifier resources accessible through a right-click on the table's column header.
- Evidence snippets:
  - Snippet 1 (score: 0.648)
    > (RCy3): mapTableColumn(column="name", species="Yeast", map.from="Ensembl", map.to="Entrez Gene") (py2cytoscape): cyclient.idmapper.map_column(source_column="name", species="Yeast", source_selection="Ensembl", target_selection="Entrez Gene")
    > Case 2: From proteins to genes When working with protein interaction networks, for example those from the STRING database (see http:// apps.cytoscape.org/apps/stringapp), you may want to translate protein identifiers (e.g., Uniprot-TrEMBL) to gene identifiers. The idmapper app supports this case as well, but one should be aware of the assumptions involved when making this translation. Since most genes encode for many proteins, you may have many-to-one mappings in your results. For all human networks imported from STRING using the StringApp 5 , the following commands will perform an ID mapping from Uniprot-TrEMBL (proteins) to Ensembl (genes):
    > (RCy3): mapTableColumn(column="canonical name", species="Human", map.from="Uniprot-TrEMBL", map.to="Ensembl") (py2cytoscape): cyclient.idmapper.map_column(source_column="canonical name", species="Human", source_selection="Uniprot-TrEMBL", target_selection="Ensembl")
    > Case 3: Identifiers and symbols In contrast to gene names and symbols, identifiers provide a more reliable means of specifying a particular gene.
    > All data integration should be performed using identifiers as keys. Nevertheless, names and symbols play an important role in making results easier to read and understand. The idmapper app is primarily concerned with identifiers. However, relying on a subset of commonly used sources from BridgeDb (Table 1) it does provide one exception.

### [14] Proteome-wide Subcellular Topologies of E. coli Polypeptides Database (STEPdb)*
- Authors: Georgia Orfanoudaki, A. Economou
- Year: 2014
- Venue: Molecular & Cellular Proteomics
- URL: https://www.semanticscholar.org/paper/8e452aca415b30d995ba9f977086924c8fed8f19
- DOI: 10.1074/mcp.O114.041137
- PMID: 25210196
- Citations: 72
- Influential citations: 3
- Summary: The STEP database (STEPdb) is a comprehensive characterization of subcellular localization and topology of the complete proteome of Escherichia coli and is the first database that contains an extensive set of peripheral IM proteins (PIM proteins) and includes their graphical visualization into complexes, cellular functions, and interactions.
- Evidence snippets:
  - Snippet 1 (score: 0.648)
    > The E. coli K-12 Reference Proteome and Data Sources-Two databases Uniprot (29) and EcoLOCATION (32) and the proposed IM proteome (33) were the main initial starting points for the complete subcellular categorization of K-12 described here. The E. coli K-12/ MG1655 strain is one of the microbial proteomes whose comprehensive annotation is of the highest priority in Uniprot (29). This is the "reference proteome" for E. coli, contains 4303 proteins, and has been annotated here. Our annotation has been formulated in such a way that it can be easily incorporated in Uniprot.
    > EchoLOCATION has an easily accessible table that maps gene names to subcellular locations. However, mapping the gene names given by EchoLOCATION to the respective protein identifiers in Uniprot was not straightforward. Unfortunately, gene names cannot serve as unique identifiers of a protein sequence. In more than 100 cases the gene name of a predicted protein in EchoLOCATION when searched against Uniprot gave as a result more than one K-12 protein hits. That is because there are proteins that have common synonymous gene names with the primary gene name of others.
    > To retrieve updated Uniprot accession identifiers and to map Uniprot accessions identifiers to EchoLOCATION identifiers (termed: EchoBASE IDs) we used the "ID mapping" function of Uniprot. In cases where the only provided identifiers were the gene names, we used mySQL queries to compare with the primary and alternative gene names in Uniprot. In cases where multiple matches existed for the same gene name, we manually resolved the differences based on other information (e.g. protein description, mass etc.).
    > The annotation of pseudogenes, mobile elements, transposons, and insertion elements relied on EcoGene (34), Uniprot (29), and Ochman et al. (35). The list of E. coli K-12 complexes was retrieved from EcoCyc (31) and literature searches.

### [15] Role of histone-lysine N-methyltransferase 2D (KMT2D) in MEK-ERK signaling-mediated epigenetic regulation: a phosphoproteomics perspective
- Authors: Sreeshma Ravindran Kammarambath, Leona Dcunha, Athira Perunelly Gopalakrishnan, Amal Fahma, N. Krishna et al.
- Year: 2025
- Venue: Frontiers in Bioinformatics
- URL: https://www.semanticscholar.org/paper/0ac0729148aff3d839e6a15984e11532e9e740f9
- DOI: 10.3389/fbinf.2025.1683469
- PMID: 41341998
- PMCID: 12669113
- Citations: 5
- Summary: The phosphoregulatory network of Histone-lysine N-methyltransferase 2D is delineated, positioning it as a dynamic epigenetic effector modulated by MEK-ERK signaling, with broader implications for cancer and developmental disorders.
- Evidence snippets:
  - Snippet 1 (score: 0.648)
    > Each protein was mapped to its corresponding gene symbol based on the HGNC (downloaded on 30.05.2023) and to its corresponding UniProt (13.04.2023) (UniProt, 2023) accessions using our in-built mapping tool to ensure consistent and standardized annotation. We conducted the analysis using the methodologies outlined in (Sanjeev et al., 2024). The overall workflow used in this study is outlined in Figure 1.

### [16] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.645)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [17] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
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
  - Snippet 1 (score: 0.644)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

### [18] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.644)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [19] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.643)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
4. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
5. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
6. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
7. Jesse R. Walsh, M. Schaeffer, Peifen Zhang, S. Rhee, J. Dickerson et al. (2016). The quality of metabolic pathway resources depends on initial enzymatic function assignments: a case for maize. BMC Systems Biology. https://www.semanticscholar.org/paper/c41be7766c80fddb3f81c57ced799b8562370cc8
8. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
9. Peng Chen, Huan-Yu Wu (2024). Network pharmacology- and molecular docking-based exploration of the molecular mechanism underlying Jianpi Yiwei Recipe treatment of gastric cancer. World Journal of Gastrointestinal Oncology. https://www.semanticscholar.org/paper/e443646ac4c9b1279858936d666dcd66993fe816
10. Tim Godec, Sebastian Beier, Natalia Yaneth Rodriguez-Granados, R. Sasidharan, L. Abdelhakim et al. (2025). Haplotype-resolved genome assembly of the tetraploid potato cultivar Désirée. Scientific Data. https://www.semanticscholar.org/paper/23a46e4cee0fdfcb5eec69a77ad783893a46d924
11. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
12. Sophia Zachari, K. Liadaki, Angeliki Planaki, E. Zafiriou, Olga Kouvarou et al. (2025). A Genome-Wide Association Study Identifying Novel Genetic Markers of Response to Treatment with Interleukin-23 Inhibitors in Psoriasis. Genes. https://www.semanticscholar.org/paper/d5f656311b54e222e7487ea32a061869b30178a1
13. Adam Treister, Alexander R. Pico (2018). Identifier Mapping in Cytoscape. F1000Research. https://www.semanticscholar.org/paper/c97ebea942d97f5336dd1a1a189c665ae83753ec
14. Georgia Orfanoudaki, A. Economou (2014). Proteome-wide Subcellular Topologies of E. coli Polypeptides Database (STEPdb)*. Molecular & Cellular Proteomics. https://www.semanticscholar.org/paper/8e452aca415b30d995ba9f977086924c8fed8f19
15. Sreeshma Ravindran Kammarambath, Leona Dcunha, Athira Perunelly Gopalakrishnan, Amal Fahma, N. Krishna et al. (2025). Role of histone-lysine N-methyltransferase 2D (KMT2D) in MEK-ERK signaling-mediated epigenetic regulation: a phosphoproteomics perspective. Frontiers in Bioinformatics. https://www.semanticscholar.org/paper/0ac0729148aff3d839e6a15984e11532e9e740f9
16. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
17. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
18. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
19. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c