---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T15:08:16.138055'
end_time: '2026-07-10T15:08:20.851653'
duration_seconds: 4.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ttgR
  gene_symbol: ttgR
  uniprot_accession: Q88N29
  protein_description: 'RecName: Full=Probable HTH-type transcriptional regulator
    TtgR; AltName: Full=Efflux pump ttgABC operon regulator;'
  gene_info: Name=ttgR; OrderedLocusNames=PP_1387;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DNA-bd_HTH_TetR-type_CS. (IPR023772); Homeodomain-like_sf. (IPR009057);
    HTH-type_TetR-like_transc_reg. (IPR050109); HTH_TetR. (IPR001647); Tet_transcr_reg_TetR-rel_C_sf.
    (IPR036271)
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
- **UniProt Accession:** Q88N29
- **Protein Description:** RecName: Full=Probable HTH-type transcriptional regulator TtgR; AltName: Full=Efflux pump ttgABC operon regulator;
- **Gene Information:** Name=ttgR; OrderedLocusNames=PP_1387;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DNA-bd_HTH_TetR-type_CS. (IPR023772); Homeodomain-like_sf. (IPR009057); HTH-type_TetR-like_transc_reg. (IPR050109); HTH_TetR. (IPR001647); Tet_transcr_reg_TetR-rel_C_sf. (IPR036271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ttgR" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ttgR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ttgR** (gene ID: ttgR, UniProt: Q88N29) in PSEPK.

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
  - Snippet 1 (score: 0.799)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.727)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.777)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

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
  - Snippet 1 (score: 0.752)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.736)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [5] PneumoWiki: a pan-genome-based database for the pathogen Streptococcus pneumoniae
- Authors: Henry Mehlan, Stephanie Hirschmann, L. M. Busch, André Hennig, K. Nieselt et al.
- Year: 2025
- Venue: Microbiology Spectrum
- URL: https://www.semanticscholar.org/paper/f50ca6bbbc06e7e98865757a669dc28515c71f9b
- DOI: 10.1128/spectrum.02957-25
- PMID: 41860230
- PMCID: 13055309
- Citations: 1
- Summary: A manually curated pan-genome database PneumoWiki is created that integrates genomic data of 43 S. pneumoniae strains with various aspects of functional annotation to provide researchers with curated, up-to-date information on a range of pneumococcal genomes.
- Evidence snippets:
  - Snippet 1 (score: 0.729)
    > The user can also choose between the two Gene pages via the register tabs specifying the strains (see Fig. 3). The next section of the Gene page contains detailed information about the gene (Gene section, Fig. 2A). This section covers the basic information from the Summary section as well as the gene coordinates, gene length, essentiality, DNA sequence, and accession numbers used by external databases with corresponding links, including BioCyc (40) and PneumoBrowse 2 (23). The largest section, the Protein section (Fig. 2B), is dedicated to the encoded protein. Here, users can find the protein length, molecular weight, isoelectric point, catalyzed reaction, protein function assignments based on TIGRFAMs, Pfam, and the SEED (see Materials and Methods), subcellular localization, and other information. If the selected gene encodes a transcriptional regulator, the corresponding regulon members are displayed, as shown in Fig. 2B. As for the Gene section, the Protein section is concluded with database links (NCBI and UniProt) and the protein sequence. Functional annotations based on complementary classification algorithms (TIGRFAMs, Pfam, and the SEED) can support the elucidation of protein functions in the case of proteins with poorly characterized or unknown function. For the sake of conciseness, by default, the lists of assigned predicted functions according to TIGRFAMs and Pfam are collapsed and show only the hit with the best HMM-score but can be expanded by clicking on the plus sign.
    > The following section of the Gene page (Expression and regulation, Fig. 2C) provides information related to regulation and gene expression. This includes the predicted operon structure obtained from MicrobesOnline (41), regulation by transcription factors (Table 1), and a link to the respective gene expression data in PneumoExpress (15). For the TIGR4 strain, additional data on transcription start sites and operon structures determined experimentally by Warrier et al. (42) are provided.
    > Data on transcription factor regulons are retrieved from the RegPrecise database (43) and from published literature (Table 1).

### [6] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
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
  - Snippet 1 (score: 0.718)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

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
  - Snippet 1 (score: 0.706)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [8] Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms
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
  - Snippet 1 (score: 0.705)
    > Examples are for illustrative purposes only and specific to each case, hence not all the entities are shown and highlighted. RED: Gene/Protein BLUE: Disease GREEN: Organism a. Biomedical concepts Gene/Protein: Annotations could be specific gene/protein names or classes/family names of gene/proteins. In particular, very broad concepts like "protein", "gene", "enzyme", "receptors", "kinase", "cytokine", "transcription regulators/factors" are out of the scope of annotations. However, family/subtype names of those concepts are considered for the annotations, such as "amylolytic enzyme", "antioxidant enzyme", "map kinase p38", because these terms narrow the concepts to specific families of gene/protein, enzyme.
    > Annotators can refer to Uniprot and Protein Ontology.

### [9] Analysis of solvent tolerance in Pseudomonas putida DOT‐T1E based on its genome sequence and a collection of mutants
- Authors: Zulema Udaondo, E. Duque, M. Fernández, Lázaro Molina, J. de la Torre et al.
- Year: 2012
- Venue: FEBS Letters
- URL: https://www.semanticscholar.org/paper/91edbfb569b866e6856db34f29273720f98a2fb7
- DOI: 10.1016/j.febslet.2012.07.031
- PMID: 22819823
- Citations: 45
- Influential citations: 3
- Summary: The genome of the solvent‐tolerant P. putida strain DOT‐T1E which thrives in the presence of high concentrations of monoaromatic hydrocarbons, contains a circular 6.3 Mbp chromosome and a 133 kbp plasmid.
- Evidence snippets:
  - Snippet 1 (score: 0.701)
    > The rpoT gene controls the expression of a number of membrane proteins, including components of the respiratory chains, porins, transporters, and multidrug efflux pumps. Hypersensitivity of the P. putida RpoT-deficient mutant to organic solvents can be attributed to the fact that in the DrpoT strain expression of the toluene efflux pump ttgGHI genes is several fold lower than in the parental strain.
    > Recently, extensive analyses of the regulation of the ttgABC, ttg-DEF and ttgGHI operons in T1E and SrpABC in S12 have been carried out. TtgR, which belongs to the TetR family of regulators, is the specific transcriptional repressor of the ttgABC. The basal expression of this pump is increased in the presence of antibiotics, flavonoids and alcohols but it does not vary in the presence of aromatic compounds [1,63,64]. The TtgR operator is a 36 bp sequence located in the ttgR-ttgA intergenic region and overlaps with the -10 and -35 regions of the ttgABC promoter, and the -10 region of the ttgR promoter. In the absence of effectors, the TtgR dimer is bound to its operator site repressing its own expression and that of the efflux pump. Effector binding to the protein-DNA complex induces the dissociation of TtgR, and allows transcription. The crystal structure of the TtgR protein in complex with effectors has been determined [65]. TtgR has a hydrophobic binding pocket, which explains TtgR's ability to bind different ligands. Within this pocket two binding sites were identified: one that binds ligands with high affinity and the second that binds molecules with low affinity.
    > TtgV belongs to the IclR family of transcriptional regulators and is the main regulator in the modulation of the expression of ttgDEF and ttgGHI (reviewed in [66]). The ttgDEF operon is silent in the absence of effectors, while a basal expression level of the ttgGHI operon has been reported [64,67]. Exposure of P. putida T1E to aromatic compounds (i.e.

### [10] Evidence-Based Annotation of Gene Function in Shewanella oneidensis MR-1 Using Genome-Wide Fitness Profiling across 121 Conditions
- Authors: A. Deutschbauer, M. Price, Kelly M. Wetmore, Wenjun Shao, Jason K. Baumohl et al.
- Year: 2011
- Venue: PLoS Genetics
- URL: https://www.semanticscholar.org/paper/2c45bfe12847d60d5d41ef832c10aef7b36882cd
- DOI: 10.1371/journal.pgen.1002385
- PMID: 22125499
- PMCID: 3219624
- Citations: 124
- Influential citations: 7
- Summary: Pools of tagged transposon mutants in the metal-reducing bacterium Shewanella oneidensis MR-1 are used to probe the mutant fitness of 3,355 genes in 121 diverse conditions including different growth substrates, alternative electron acceptors, stresses, and motility and it is found that genes in all functional categories have phenotypes, and that potentially redundant genes are likely to have distinct phenotypes.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > Evidence-based annotation of gene function using fitness profiles
    > One of the main aims of this study was to use mutant fitness to annotate gene function.Using the approaches described below, we predicted specific functional annotations for 40 genes/operons with either poor or incomplete annotations including 17 enzymes, 10 transporters/efflux pumps, 4 transcriptional regulators/signaling proteins, 4 electron transport proteins, and 5 other proteins (Table 1 for list; Text S2 for detailed rationale).Even in retrospect, few of these annotations could have been made by homology alone.First, we identified those genes with a strong fitness defect in only one or a few conditions, as an annotation of a specific function in these instances is often easier than if a gene has pleiotropic effects.Second, we identified groups of genes with high cofitness across the entire compendium.These genes are more likely to be functionally related and allow for functional annotation if one or more of the genes in the cofitness cluster are characterized [7].Given these genes and their phenotypes, we used comparative genomics and prior experimental data from MR-1 and other bacteria to predict specific functions.We split our evidence-based annotations into three categories, ''new'', ''expanded'', and ''confirmed'', to reflect prior knowledge and genes that have multiple functions.Selected examples of evidence-based annotations and their experimental validation are described below.
    > Some of our gene annotations reflect specific new functions for hypothetical genes.For example, the MR-1 genome does not have an annotated enzyme for synthesizing ornithine from N-acetylornithine, a necessary step in arginine biosynthesis.Given that MR-1 is capable of synthesizing arginine, we sought to identify the missing enzyme.The N-acetyl-ornithine to ornithine reaction is encoded in E. coli by argE, an N-acetyl-ornithine deacetylase, and in B. subtilis by argJ, an ornithine acetyltransferase.

### [11] FusionPDB: a knowledgebase of human fusion proteins
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
  - Snippet 1 (score: 0.690)
    > To assign functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt for 10 619 genes involved in 15 030 fusion genes ( 10 ). UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features and three secondary structure features. Since such feature loci information is based on amino acid sequences, the genomic breakpoint information was converted into the amino acid level while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE (v19) gene model of human reference genome ( 11 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported such fusion genes as having not retained that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.

### [12] iPCD: A Comprehensive Data Resource of Regulatory Proteins in Programmed Cell Death
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
  - Snippet 1 (score: 0.682)
    > The PCD regulators were collected and annotated. First, 1,091,014 PCD regulators were annotated with basic information, including 'iPCD ID', 'status', 'Ensembl Gene ID', 'Ensembl Protein ID', 'UniProt Accession', 'PDB structure', 'Function', 'Protein Sequence', 'Nucleotide Sequence', 'Key word' and 'Gene Ontology'. For each species, all regulatory proteins were alphabetically ordered based on their gene names. Then, each protein was automatically assigned a unique iPCD ID for convenient organization in the database. For example, the GPX4 protein in Homo sapiens was assigned with an ID of 'iPCD-Hsa-1522'. Subsequently, 102 additional public resources were integrated to annotate 17,768 regulators from 8 model organisms, including Homo sapiens, Mus musculus, Rattus norvegicus, Drosophila melanogaster, Caenorhabditis elegans, Saccharomyces cerevisiae, Arabidopsis thaliana and Danio rerio. These public resources covered 16 distinct aspects, which contained (i) genetic variation and mutation, (ii) functional annotation, (iii) structural annotation, (iv) physicochemical property, (v) functional domain, (vi) post-translational modification (PTM), (vii) disease-associated information, (viii) protein-protein interaction (PPI), (ix) drug-target relation, (x) orthologous information, (xi) biological pathway, (xii) transcriptional regulator, (xiii) mRNA expression, (xiv) protein expression/proteomics, (xv) subcellular localization and (xvi) DNA and RNA element. The detailed processing of 102 public resources is provided in Supplementary Methods. A brief flowchart of the study is shown in Figure 1A.

### [13] SubtiWiki—a comprehensive community resource for the model organism Bacillus subtilis
- Authors: U. Mäder, Arne G. Schmeisky, Lope A. Flórez, J. Stülke
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/2e731ca29bfb7bdedda983c425ccf151549b5ab7
- DOI: 10.1093/nar/gkr923
- PMID: 22096228
- PMCID: 3245094
- Citations: 92
- Influential citations: 9
- Summary: A Wiki-type database for the Gram-positive model bacterium Bacillus subtilis, SubtiWiki is generated and can be regarded as one of the most complete inventories of knowledge on a living organism in one single resource.
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > An example of a SubtiWiki gene page is shown in Figure 1. At the top of each page, the contents and a table with the most important information are shown. This table covers the gene name and synonym designations, the gene product and its function, the molecular weight and isoelectric point of the protein, the gene and protein lengths and the names of the adjacent genes. Moreover, the table contains links to the relevant representations of protein-protein interactions and to the pathway diagrams. Finally, the DNA and protein sequences can be downloaded and a diagram of the genomic context is shown. Below the table, the functional categories and regulons for the gene/protein are shown (see below). This allows immediate access to all related genes or proteins that are members of the same category or regulon. In the case of transcription regulators, a link to the page dedicated to the regulon controlled by the regulatory protein is provided.
    > The next section contains the information about the gene. It covers basic information as the unique identifier (locus tag), phenotypes of a mutant and gene-specific database entries. The largest section of each page is devoted to the encoded protein. It provides information on the biological activity of the protein, the protein family and possible paralogs. Moreover, kinetic data (if available), as well as information on protein domains, modifications, co-factors, effectors, interactions and the localization are presented. As for the gene section, the section for the protein is concluded with database links, such as structure databases (e. g. PDB), Uniprot or KEGG entries, as well as the E.C. numbers.
    > The following section of the page provides information on the expression of the gene and its regulation. This includes the operon structure, the sigma factor, transcription factors and their mode of action. At the bottom of the page, there is some community related information (biological materials, labs working on the gene/protein), as well as a collection of references on all aspects of the gene/protein.

### [14] Recent advances in genome annotation and synthetic biology for the development of microbial chassis
- Authors: Saltiel Hamese, Kanganwiro Mugwanda, M. Takundwa, Earl Prinsloo, D. B. Thimiri Govinda Raj
- Year: 2023
- Venue: Journal of Genetic Engineering & Biotechnology
- URL: https://www.semanticscholar.org/paper/64c7c01c15495b3bf0ddb86c33e71d766b554517
- DOI: 10.1186/s43141-023-00598-3
- PMID: 38038785
- PMCID: 10692039
- Citations: 4
- Influential citations: 1
- Summary: The strategies for genome annotations of lactic acid bacteria provide insights into streamlining genome reduction without compromising the functionality of the chassis and the potential for minimal genome chassis development.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > Genome annotation identifies functional elements of a genome sequence, indicating its significance. Annotating a genome entails following these steps: identifying genes (including protein-encoding genes and some RNA-encoding genes), predicting the functions of the identified genes, creating metabolic reconstructions and connecting them to genes, labeling phage insertion sequences and transposons, predicting frameshifts and pseudogenes, and identifying regulatory sites and operons, ultimately creating a list of regulons [51]. Regulons are a group of genes or operons that are upregulated or downregulated as a unit by the same protein in response to the same signal. Several genome annotation tools have been developed. These annotation tools may be automated or manual. Automated gene-annotation tools are often used because of the faster annotation and ease of use. However, it is highly recommended that beginners select automatic and semi-automatic annotation methods [31]. Moreover, automatic annotation algorithms, frequently based on orthologs from distantly related model organisms, cannot yet correctly identify all genes within a genome due to confidence and reliability of outcomes as results from different servers or databases are often dissimilar; obtaining accurate gene sets and model manual annotation is often required [21]. Several pipelines for the annotation of genomes have been developed; examples are in Table 1. The gene or protein sequences identified by structural annotation describing the gene structure (e.g., introns, exons, coding sequences, and start and end coordinates) are linked to biological data in a process known as functional annotation, which usually begins with gene identification or gene calling. The different tools for functional annotation are summarized in Table 2. With many genomes sequenced, computational annotation approaches to characterize genes and proteins from their sequences are essential for designing genome deletions.

### [15] An Asymmetrically Balanced Organization of Kinases versus Phosphatases across Eukaryotes Determines Their Distinct Impacts
- Authors: Ilan Y. Smoly, N. Shemesh, Michal Ziv-Ukelson, Anat Ben-Zvi, Esti Yeger Lotem
- Year: 2017
- Venue: PLoS Computational Biology
- URL: https://www.semanticscholar.org/paper/4f13e00bf92fc0e75e910dd6a62d87286a816e6b
- DOI: 10.1371/journal.pcbi.1005221
- PMID: 28135269
- PMCID: 5279721
- Citations: 40
- Summary: Protein phosphorylation underlies cellular response pathways across eukaryotes and is governed by the opposing actions of phosphorylating kinases and de-phosphorylating phosphatases. While kinases and phosphatases have been extensively studied, their organization and the mechanisms by which they balance each other are not well understood. To address these questions we performed quantitative analyses of large-scale 'omics' datasets from yeast, fly, plant, mouse and human. We uncovered an asymm...
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > The annotations of genes to different molecular functions were obtained from the Gene Ontology (GO) Database [38]. We chose to work with GO annotations since they were in good agreement with other sources and provided a consistent framework across the different organisms. Kinases and phosphatases were defined as genes with molecular function annotation of 'protein kinase activity' (GO:0004672) or 'phosphoprotein phosphatase activity' (GO:0004721), respectively. Regulators of histone acetylation were defined as genes with 'histone acetyltransferase activity' (GO:0004402) or 'histone deacetylase activity' (GO:0004407) annotations. Regulators of protein ubiquitination were defined as genes with "ubiquitin-protein transferase activity" (GO:0004842) or "thiol-dependent ubiquitin-specific protease activity" (GO:0004843) annotations. For H. sapiens we considered only genes that were reviewed by UniProt database [39]. For A. thaliana we considered only genes with annotated TAIR accessions [40]. For D. melanogaster we considered only genes with annotated FlyBase accessions [41]. For M. musculus we considered only genes with annotated MGI accessions [42]. For C. elegans we considered all kinases and phosphatases annotated with multivulva or vulvaless phenotype according to WormBase [30]. To validate the trends we observed, we also analyzed curated kinases and phosphatases extracted from organism-specific databases, which showed similar results (S6 Fig).

### [16] MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila
- Authors: Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al.
- Year: 2025
- Venue: Synthetic and Systems Biotechnology
- URL: https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
- DOI: 10.1016/j.synbio.2025.04.001
- PMID: 40276250
- PMCID: 12018684
- Summary: Shifts in metabolic allocation in a glucoamylase hyperproduction strain of M. thermophila are identified, highlighting changes in fatty acid biosynthesis and amino acids biosynthesis pathways, which provide new insights into the underlying phenotypic alterations.
- Evidence snippets:
  - Snippet 1 (score: 0.667)
    > Single-gene search: Gene annotation is essential for biologists to understand a gene's function. MTD's single-gene search interface allows researchers to obtain a comprehensive gene description by entering or selecting a gene ID. The results include sequence information, CAZy family, Pfam domains, GO/KEGG annotations, and phenotype information (Fig. 2D), along with sequence-based predictions such as optimal protein activity temperature, melting temperature (Tm), subcellular localization, and transcription factor scores. To enhance data accessibility, links to external databases such as NCBI, KEGG, FungiDB [4], UniProt, and JGI are also provided, facilitating cross-referencing of gene annotations across various resources.
    > Unlike the static genome, the transcriptome captures dynamic gene expression changes in response to developmental or environmental conditions, establishing a dynamic link between an organism's genome and its physical characteristics [63]. In the single-gene retrieval interface, the expression of the searched gene is visualized in the form of box plots and scatter plots across transcriptome datasets (Fig. 2E). When hovering over any data point, users can view the corresponding experimental details, such as mutant name, sample processing methods, and growth conditions. This interactive feature reveals gene expression responses to environmental factors, allowing researchers to quickly identify experimental conditions of interest and explore the gene's potential roles in diverse biological contexts. Moreover, clicking on the dataset title will direct users to the GEO browser for further detailed descriptions. KEGG Pathway or Gene List Search: In transcriptome studies, researchers typically adopt a "bottom-up" approach: first sequencing all mRNA in a cell, identifying differentially expressed genes between conditions, and then performing GO/KEGG enrichment analysis to interpret functional distributions. MTD, however, offers a complementary "top-down" search strategy, enabling users to examine the expression of genes within a specific KEGG pathway (Fig. 3A) or a user-defined gene set. A unique feature of MTD is its manually curated data categorization system, which organizes sample data with detailed annotations based on experimental conditions.

### [17] ResA3: A Web Tool for Resampling Analysis of Arbitrary Annotations
- Authors: A. Ruhs, F. Cemic, T. Braun, M. Krüger
- Year: 2013
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/81d8d1bc8cf5b02d9e7027a010f6dedc6be55b38
- DOI: 10.1371/journal.pone.0053743
- PMID: 23382850
- PMCID: 3557297
- Citations: 6
- Summary: ResA3 (Resampling Analysis of Arbitrary Annotations, short: ResA) is a novel tool to facilitate the analysis of enrichment and regulation of annotations deposited in various online resources such as KEGG, Gene Ontology and Pfam or any kind of classification.
- Evidence snippets:
  - Snippet 1 (score: 0.666)
    > Datasets can be inserted or uploaded to the web interface (Figure 2b). Data must be tab separated and formatted as shown in Figure 3A. They could include gene symbols and UniProt identifiers, which are used for the Gene Ontology annotation feature. To annotate a dataset which contains gene symbols and/ or UniProt identifiers, the appropriate organism can be set (Figure 2d) and the user can choose between full or slim GO annotation (Figure 2e) and full or experimental evidence (Figure 2f). The annotation is based on the gene and UniProt identifiers provided by UniProt-GOA and will be updated monthly.
    > It is essential that the first column contains the experimental value (log fold-change, isotope incorporation, intensity, etc.). Titles of the annotation columns are used to discriminate between different types of annotation in the results. If a pasted dataset already contains annotations such as KEGG and Pfam, these terms must reside in tab separated and titled columns (Figure 3A and online help). Annotations need to be located in the last columns. Importantly, semi-colons must separate multiple identifiers or terms in one column. For example, multiple identifiers are common for protein groups of mass spectrometric data and annotation will be done for all entries. Similarly, multiple terms are also common with Gene Ontology as one gene can be associated with several compartments at the same time and any of these terms will be treated independently. When columns of annotation are provided, the correct number of columns must be set in the respective spin-box in the web interface (Figure 2c). The dataset used in the example analysis already contains three annotation columns (KEGG, Pfam and InterPro) and is available on the web site of the tool as tab separated text file and Excel file (Figure 2a).
    > Regulation or the enrichment based on various statistics (estimators) can be tested depending on the focus of the analysis (Figure 2g). The number of resamplings R can be set in the range from 500 to 10,000 (Figure 2h).

### [18] Genomic and Functional Analyses of the 2-Aminophenol Catabolic Pathway and Partial Conversion of Its Substrate into Picolinic Acid in Burkholderia xenovorans LB400
- Authors: Bernardita Chirino, E. Strahsburger, Loreine Agulló, Myriam González, M. Seeger
- Year: 2013
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/6618487e3df8089c007d2ca22d810410762d163f
- DOI: 10.1371/journal.pone.0075746
- PMID: 24124510
- PMCID: 3790839
- Citations: 42
- Influential citations: 1
- Summary: It is shown that during LB400 growth on 2-AP this substrate was partially converted into picolinic acid (PA), a well-known antibiotic, which could lead to the production of picolinoic acid.
- Evidence snippets:
  - Snippet 1 (score: 0.665)
    > 93% identity), a MarR-type transcriptional regulator closely related to a MarRtype regulator protein from Acidovorax sp. JS42 (ABM43065.1; 77% identity), a LysR-type transcriptional regulator closely related to a LysR-type regulator protein from Bordetella petrii DSM 12804 (CAP41606.1; 81% identity), a XRE-type transcriptional regulator closely related to a XRE regulator protein from Alcaligenes sp. HPC1271 (EKU29625.1; 86% identity), and a LysR-type transcriptional regulator closely related to a LysR-type regulator protein from Acidovorax delafieldii 2AN (EER60975.1; 67% identity), respectively (Fig. 2). Three genes located downstream of the amn gene cluster encode membrane transporter proteins. The BxeA1155, BxeA1156 and BxeA1157 genes encode three components (an outer membrane protein, an inner membrane protein and a transmembrane protein, respectively) of a major facilitator superfamily (MFS) multidrug efflux system. This multidrug efflux system possesses high identity with a multidrug efflux transporter pump from Ralstonia solanacearum GMI1000 [27], including the channel-forming component (CAD17593.1; 54% identity), the inner membrane protein (CAD17592.1; 58% identity) and the transmembrane protein (CAD17591.1; 57% identity), respectively. The BxeA1154 gene encodes a TraG conjugal transfer coupling protein that has 33% identity with the TraG protein (accession number AFT71063.1) from Alcanivorax dieselolei B5 [28].

### [19] A haplotype-resolved genome assembly of Malus domestica ‘Red Fuji’
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
  - Snippet 1 (score: 0.665)
    > For the functional annotation of the protein-coding genes, we employed a standardized workflow 30,31 .In summary, the protein sequences of the two haplotype genomes were compared against several protein databases using the DIAMOND program, with an E-value cutoff of 1E-4.The protein databases included the non-redundant protein database (NR), TrEMBL (http://www.uniprot.org/),SwissProt 32 , and the Arabidopsis protein database.The BLAST results from SwissProt, TrEMBL, and the Arabidopsis protein database were loaded into the AHRD (https://github.com/asishallab/AHRD)program to predict concise, informative, and accurate functional descriptions for each gene.
    > Furthermore, the protein sequences were compared against the InterPro database 33 using InterProScan to identify functional protein domains.The BLAST results from the NR database were combined with the identified InterPro protein domains to perform Gene Ontology (GO) annotation using the Blast2GO program 34 , and the GO terms were associated with the annotated protein sequences.To explore the protein-coding genes' connections to pathways, the 'Red Fuji' apple protein sequences were annotated using the online KAAS tool (https://www.genome.jp/tools/kaas/).This annotation provided information about the genes' associations with various metabolic pathways.Additionally, the iTAK software was used to predict transcription factors, transcription regulators, and protein kinases.
    > The protein-coding genes were compared separately with the NR, SwissProt, Arabidopsis protein database, and TrEMBL databases.Each database annotated 95,552, 77,453, 67,243, and 92,132 genes, respectively.A total of 52,073 genes were matched to 2,555 GO terms.Additionally, in the pathway annotation, 32,312 genes were annotated to 143 ko IDs.In the prediction of transcription factors (TFs) and transcription regulators (TRs), a total of 6,283 genes belong to 93 different gene families.Additionally, 3,119 genes were annotated to 127 different protein kinase (PK) families.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
5. Henry Mehlan, Stephanie Hirschmann, L. M. Busch, André Hennig, K. Nieselt et al. (2025). PneumoWiki: a pan-genome-based database for the pathogen Streptococcus pneumoniae. Microbiology Spectrum. https://www.semanticscholar.org/paper/f50ca6bbbc06e7e98865757a669dc28515c71f9b
6. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
7. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
8. Xiao Yang, Shyamasree Saha, Aravind Venkatesan, Santosh Tirunagari, Vid Vartak et al. (2023). Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms. Scientific Data. https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
9. Zulema Udaondo, E. Duque, M. Fernández, Lázaro Molina, J. de la Torre et al. (2012). Analysis of solvent tolerance in Pseudomonas putida DOT‐T1E based on its genome sequence and a collection of mutants. FEBS Letters. https://www.semanticscholar.org/paper/91edbfb569b866e6856db34f29273720f98a2fb7
10. A. Deutschbauer, M. Price, Kelly M. Wetmore, Wenjun Shao, Jason K. Baumohl et al. (2011). Evidence-Based Annotation of Gene Function in Shewanella oneidensis MR-1 Using Genome-Wide Fitness Profiling across 121 Conditions. PLoS Genetics. https://www.semanticscholar.org/paper/2c45bfe12847d60d5d41ef832c10aef7b36882cd
11. H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim (2023). FusionPDB: a knowledgebase of human fusion proteins. Nucleic Acids Research. https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
12. Dachao Tang, Cheng Han, Shaofeng Lin, Xiaodan Tan, Weizhi Zhang et al. (2022). iPCD: A Comprehensive Data Resource of Regulatory Proteins in Programmed Cell Death. Cells. https://www.semanticscholar.org/paper/eb35030c62fa8e25fe91d3a4e48fef1de95e562c
13. U. Mäder, Arne G. Schmeisky, Lope A. Flórez, J. Stülke (2011). SubtiWiki—a comprehensive community resource for the model organism Bacillus subtilis. Nucleic Acids Research. https://www.semanticscholar.org/paper/2e731ca29bfb7bdedda983c425ccf151549b5ab7
14. Saltiel Hamese, Kanganwiro Mugwanda, M. Takundwa, Earl Prinsloo, D. B. Thimiri Govinda Raj (2023). Recent advances in genome annotation and synthetic biology for the development of microbial chassis. Journal of Genetic Engineering & Biotechnology. https://www.semanticscholar.org/paper/64c7c01c15495b3bf0ddb86c33e71d766b554517
15. Ilan Y. Smoly, N. Shemesh, Michal Ziv-Ukelson, Anat Ben-Zvi, Esti Yeger Lotem (2017). An Asymmetrically Balanced Organization of Kinases versus Phosphatases across Eukaryotes Determines Their Distinct Impacts. PLoS Computational Biology. https://www.semanticscholar.org/paper/4f13e00bf92fc0e75e910dd6a62d87286a816e6b
16. Jiacheng Dong, Zhitao Mao, Haoran Li, Ruoyu Wang, Yutao Wang et al. (2025). MTD: A cloud-based omics database and interactive platform for Myceliophthora thermophila. Synthetic and Systems Biotechnology. https://www.semanticscholar.org/paper/d3bb60ddd3eb08ddd4808324bbd432a4a0ae19ba
17. A. Ruhs, F. Cemic, T. Braun, M. Krüger (2013). ResA3: A Web Tool for Resampling Analysis of Arbitrary Annotations. PLoS ONE. https://www.semanticscholar.org/paper/81d8d1bc8cf5b02d9e7027a010f6dedc6be55b38
18. Bernardita Chirino, E. Strahsburger, Loreine Agulló, Myriam González, M. Seeger (2013). Genomic and Functional Analyses of the 2-Aminophenol Catabolic Pathway and Partial Conversion of Its Substrate into Picolinic Acid in Burkholderia xenovorans LB400. PLoS ONE. https://www.semanticscholar.org/paper/6618487e3df8089c007d2ca22d810410762d163f
19. Haixu Peng, Yating Yi, Jinrong Li, You Qing, Xuyang Zhai et al. (2024). A haplotype-resolved genome assembly of Malus domestica ‘Red Fuji’. Scientific Data. https://www.semanticscholar.org/paper/e5dc0e3046713c6ff2aed20631ab819fffd8b0c0