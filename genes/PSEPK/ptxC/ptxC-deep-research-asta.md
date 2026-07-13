---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T12:47:42.034363'
end_time: '2026-07-08T12:47:48.454272'
duration_seconds: 6.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ptxC
  gene_symbol: ptxC
  uniprot_accession: Q88PM3
  protein_description: 'SubName: Full=Phosphonate transport system permease protein
    PtxC {ECO:0000313|EMBL:AAN66452.1};'
  gene_info: Name=ptxC {ECO:0000313|EMBL:AAN66452.1}; OrderedLocusNames=PP_0827 {ECO:0000313|EMBL:AAN66452.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the binding-protein-dependent transport system
  protein_domains: MetI-like. (IPR000515); MetI-like_sf. (IPR035906); PhnE/PtxC. (IPR005769);
    BPD_transp_1 (PF00528)
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
- **UniProt Accession:** Q88PM3
- **Protein Description:** SubName: Full=Phosphonate transport system permease protein PtxC {ECO:0000313|EMBL:AAN66452.1};
- **Gene Information:** Name=ptxC {ECO:0000313|EMBL:AAN66452.1}; OrderedLocusNames=PP_0827 {ECO:0000313|EMBL:AAN66452.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the binding-protein-dependent transport system
- **Key Domains:** MetI-like. (IPR000515); MetI-like_sf. (IPR035906); PhnE/PtxC. (IPR005769); BPD_transp_1 (PF00528)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ptxC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ptxC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ptxC** (gene ID: ptxC, UniProt: Q88PM3) in PSEPK.

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
  - Snippet 1 (score: 0.801)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [2] MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis
- Authors: Xiaohua Jiang, Daren Zhao, Asim Ali, Bo Xu, Wei Liu et al.
- Year: 2021
- Venue: Frontiers in Cell and Developmental Biology
- URL: https://www.semanticscholar.org/paper/aeb08368a5540685473578345739bb569103bd46
- DOI: 10.3389/fcell.2021.673073
- PMID: 34485275
- PMCID: 8415030
- Citations: 6
- Summary: The developed MeiosisOnline provides the most updated and detailed information of experimental verified and predicted genes in meiosis, and will greatly help researchers in studying meiosis in an easy and efficient way.
- Evidence snippets:
  - Snippet 1 (score: 0.755)
    > Annotation information for each gene in MeiosisOnline contains "basic information, " "function annotation and classification, " "protein-protein interaction (PPI) and gene expression."
    > (1) Basic information: gene name/synonyms, nucleotide sequences, etc., were extracted from GenBank3 and UniProt Knowledgebase.4 (2) Function annotation and classification: detailed functional information is also manually collected from literature reports. (i) Which meiotic stage is the gene involved? (ii) Did the gene function in one sex or both sexes? (iii) Whether deletion or mutation of the gene in model organism has a phenotype in fertility? (iv) Which protein complex of the gene is involved? (v) The cellular location and expression pattern in tissues or cell lines.
    > (vi) Experimental methods used for functional analysis.
    > (vii) The information of related literature and figures for illustrating the function of protein/gene. (viii) Gene ontology annotation for collected genes.
    > (3) Protein-protein interaction and gene expression: both verified and predicted PPI information were provided. Gene expression pattern in reproductive system was also provided graphically.

### [3] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.748)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

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
  - Snippet 1 (score: 0.745)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

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
  - Snippet 1 (score: 0.743)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [6] Identifying orthologs with OMA: A primer
- Authors: Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover
- Year: 2020
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
- DOI: 10.12688/f1000research.21508.1
- PMID: 32089838
- PMCID: 7014581
- Citations: 41
- Summary: This Primer is organized in two parts and provides all the necessary background information to understand the concepts of orthology, how to infer them and the different subtypes of Orthology in OMA, as well as what types of analyses they should be used for.
- Evidence snippets:
  - Snippet 1 (score: 0.743)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

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
  - Snippet 1 (score: 0.729)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [8] SHIELD: an integrative gene expression database for inner ear research
- Authors: Jun Shen, D. Scheffer, Kelvin Y. Kwan, D. Corey
- Year: 2015
- Venue: Database: The Journal of Biological Databases and Curation
- URL: https://www.semanticscholar.org/paper/fc7704155cefd9f1c767dc2a03a5025c77d19437
- DOI: 10.1093/database/bav071
- PMID: 26209310
- PMCID: 4513695
- Citations: 130
- Influential citations: 9
- Summary: The Shared Harvard Inner Ear Laboratory Database (SHIELD), an integrated resource that seeks to compile, organize and analyse the genomic, transcriptomic and proteomic knowledge of the inner ear, is developed.
- Evidence snippets:
  - Snippet 1 (score: 0.723)
    > Many public databases of gene information are available (11)(12)(13)(14)(15)(16). However, different public databases often use different sets of unique identifiers (IDs) to describe the same genes or homologous genes in different species. One challenge of comparing large-scale biological datasets is the unification of gene names; otherwise, researchers spend a lot of effort in converting gene IDs when searching different databases. Another is the likelihood of missing some databases due to unfamiliarity; this is particularly true for clinicians and researchers who are specialized in inner ear research but are not necessarily familiar with genomics and bioinformatics. One goal of the SHIELD is to integrate relevant gene annotation information from various public databases in one centralized location.
    > For the SHIELD, annotations were derived from public databases and literature. Currently implemented annotations include official gene symbols, description of the gene name and synonyms, human and mouse chromosome cytogenetic banding, RefSeq RNA and protein (for protein coding genes) accession numbers, National Center for Biotechnology Information (NCBI) Entrez gene ID, genomic coordinates in both mouse reference genome assemblies mm9 and mm10, Ensembl, the Vertebrate Genome Annotation Database (VEGA) Mouse Genome Informatics, UniProt, Online Mendalian Inheritance in Man and gene ontology.
    > For each protein coding genes, we display all UniProt protein isoforms for that gene, the length in amino acid residues and the predicted number of transmembrane domains (TMs). We predicted TMs by running TMHMM2.0 run on all UniProt protein isoforms of each gene (17). The number of TMs is of special interest for research in sensory function, because many key proteins involved in signaling-such as the mechanotransduction ion channels-are integral membrane proteins. This information would help identify candidate genes for the components of the mechanotransduction apparatus of the inner ear.
    > We also performed manual curation of inner ear disorders including syndromic and non-syndromic hearing loss according to the Hereditary Hearing Loss Homepage (http://hereditaryhearingloss.org) and primary literature.

### [9] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.722)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.712)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [11] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.709)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

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
  - Snippet 1 (score: 0.704)
    > The UniProt knowledgebase (www.uniprot.org/uniprotkb/), (accessed on 20 June 2025), the central hub for the collection of functional information on proteins, with accurate and rich annotation [33], was used to retrieve the approved human gene and protein names and symbols.

### [13] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.694)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [14] The Autophagy Database: an all-inclusive information resource on autophagy that provides nourishment for research
- Authors: Keiichi Homma, Koji Suzuki, H. Sugawara
- Year: 2010
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/946ad0a62c6da7c1b288f58b48b6ce015835c176
- DOI: 10.1093/nar/gkq995
- PMID: 20972215
- PMCID: 3013813
- Citations: 106
- Influential citations: 4
- Summary: The Autophagy database is built to provide basics, up-to-date information on relevant literature, and a list of autophagy-related proteins and their homologs in 41 eukaryotes to give impetus to further research on autophagic by providing basic and specialized data on the subject.
- Evidence snippets:
  - Snippet 1 (score: 0.693)
    > The list of proteins of each species can be viewed in the 'Protein List section'. The user can get the cluster number, synonyms, the gene name, the Entrez gene ID, the GI number of National Center for Biotechnology Information (NCBI), the NCBI Protein Accession number together with the version, description and the PDB IDs. Clicking the symbol column opens a new window displaying detailed functions, UniProt accession number(s), UniGene ID of NCBI, related paper(s) and protein sequence as well as other information. Gene ID, GI, Protein Accession number, PDB IDs are also clickable and are linked to the relevant data.

### [15] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.691)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [16] LEGER: knowledge database and visualization tool for comparative genomics of pathogenic and non-pathogenic Listeria species
- Authors: Guido Dieterich, U. Kärst, Elmar Fischer, J. Wehland, L. Jänsch
- Year: 2005
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/45beb8854f24aefef4f88845858c82cd7c62cdf8
- DOI: 10.1093/nar/gkj071
- PMID: 16381897
- PMCID: 1347434
- Citations: 33
- Influential citations: 3
- Summary: The Proteome database LEGER was developed to support functional genome analyses by combining information obtained by applying bioinformatics methods and from public databases to improve the original annotations.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > The content of the result table can be defined by preselecting individual types of information that are grouped and presented by LEGER as part of four main topics, termed Annotation, Subcellular Localization, Protein Information and Comparative Genomics. The topic 'Annotation' refers to information for the functional assignment of genes or proteins. Whereas 'Description' and 'Classification' represent the original annotation, the UniProt-Swiss-Prot entries give access to the data of curated databases to reveal inconsistencies accumulated in the past 105 years. However, further powerful databases and services have to be considered for the generation of functional hypotheses and thus are included as part of this topic (e.g. Gene Ontology Annotation from UniProt and InterPro). With 'SPS-Annotation', the user receives information whether the selected genes/proteins were mentioned within a systematic post-genome study. This part requires manual updating and currently refers to the most important and comprehensive studies such as the investigation of PrfA-dependent gene expression (11), stress regulation and adaptation (12,13) and proteome studies aiming at subcellular reference maps derived from 2D-PAGE analyses (15,21). 'MineBlast' was recently published and can retrieve the most recent functional Nucleic Acids Research, 2006, Vol. 34, Database issue D403 information for listerial proteins and their orthologues from other organisms in literature (22). MineBlast often can complement missing functional assignments with data that were published following the first annotation of a genome and thus alleviates a still highly manual task. A genome-wide MineBlast query was already completed and adapted result pages shortcut the alternative processing using the public NCBI services (BLAST and PubMed queries). 'Genome View' and 'KEGG' generate links to graphical presentations for every gene/protein in the result table. Adapted KEGG pathway pages display the distribution of proteins along biochemical pathways (Figure 2). The Genome Viewer displays the experimental results at the level of genome organization. Genes are visualized according to their length, order and orientation in the genome (Figure 1). Rho-independent terminator sites and operon predictions help to recognize putative transcriptional units.

### [17] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2771
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.686)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [18] Genome information management and integrated data analysis with HaloLex
- Authors: F. Pfeiffer, A. Broicher, Thomas N Gillich, K. Klee, José Mejía et al.
- Year: 2008
- Venue: Archives of Microbiology
- URL: https://www.semanticscholar.org/paper/f1333d02086a84becaa054612dbb6316af6ba4c3
- DOI: 10.1007/s00203-008-0389-z
- PMID: 18592220
- PMCID: 2516542
- Citations: 91
- Influential citations: 4
- Summary: Application of homology-based methods to the published genome of Haloarcula marismortui allowed to detect 47 previously unidentified genes and to correct more than 300 start codon misassignments.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > The available information about an individual coding sequence is summarized by a central ''details page'' listing sequences (coding region and protein translation), functional information (e.g., protein name, gene name, EC number, functional classification), general gene and protein characteristics (e.g., sequence length, start and stop codons, GC content, theoretical pI value), and results from several bioinformatic tools, e.g., transmembrane and signal peptide prediction with ''Phobius'' (Kall et al. 2004), protein export signals with ''Tatfind'' (Rose et al. 2002), codon adaptation index (Sharp and Li 1987), etc. In addition, the details page shows homologous sequences as well as cross-references to entries of the same protein in major public sequence databases like GenBank, UniProt, Kegg, and also links to relevant PubMed abstracts.
    > Usually, the details page is reached by selecting an organism and directly specifying an identifier or name for the gene of interest. In addition, also less specific searches and browsing functionalities are supported, including the option to obtain complete lists of genes or proteins, which can optionally be filtered by various characteristics like pI value range, type of proteomic identification, etc. (cf. Fig. 1).
    > If the organism or gene of interest is not specified a priori, the user can alternatively start out with a blastbased search (Altschul et al. 1997) for all sequences in the HaloLex database, which are similar to a given query.
    > To reach the details page, one may also start from a graphical display of a particular region on the genome. The corresponding ''region viewer'' page provides standard genome browsing functionalities and allows to color-code genes according to a variety of characteristics like the annotation status, assigned function class, GC content, proteomic identification (see Fig. 2), and many more.

### [19] Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining
- Authors: Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al.
- Year: 2025
- Venue: npj Drug Discovery
- URL: https://www.semanticscholar.org/paper/000083b7bd96cff5b3d1891b00ad332eed7d9add
- DOI: 10.1038/s44386-025-00006-5
- PMID: 40066064
- PMCID: 11892419
- Citations: 4
- Summary: This study systematically assessed the Plasmodium falciparum genome and identified 867 candidate protein targets with evidence of small-molecule binding and blood-stage essentiality, providing a genome-wide data resource for P. falciparum and implements a generalizable framework for systematically evaluating and prioritizing novel pathogenic disease targets.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > List of genes and genomic features (GFF) for Plasmodium falciparum 3D7 genome (PlasmoDB release 66) was downloaded and protein-coding genes were extracted along with their gene annotations and genomic location. Additional genomic annotations were obtained by querying PlasmoDB to extract UniProt and Entrez ID(s), ortholog group (OrthoMCL), protein features (CDS and protein length, molecular weight, isoelectric point), domain annotations (InterPro, Pfam, and Superfamily), number of transmembrane (TM) domains, and enzyme commission (EC) numbers. Gene function (Gene Ontology components, functions, and processes) was extracted either from PlasmoDB or by querying the InterPro ID with the InterPro2GO mapping tool from EMBL-EBI. Gene essentiality data was obtained for P. falciparum 20 and P. berghei 21,22 parasites mapped to their falciparum orthologs using OrthoMCL orthology group IDs. Protein Data Bank (PDB) IDs of crystal structures were obtained by searching either gene symbols, UniProt IDs associated with each gene, or the term "Plasmodium". A report with gene identifier, organism, accession number, method for structure determination and publication information was extracted for the search hits.
    > Mapping genes to associated literature publications A download from the NCBI FTP site was performed for gene2pubmed.gz (version 2024-02-21) containing taxonomy ID, gene ID (Entrez) and PubMed ID information. Gene IDs were mapped to the P. falciparum 3D7 annotation set, and corresponding PMIDs were extracted. To include literature references associated with gene symbols, we queried each symbol in PubMed using the Eutils 77 efetch function from NCBI; additional information for each publication was obtained pragmatically using the same tool, namely title, authors and digital object identifier (DOI). Literature references from gene nomenclature extraction were manually reviewed and filtered for unrelated records (e.g., same name but different meaning across organisms/diseases).

### [20] iEKPD 2.0: an update with rich annotations for eukaryotic protein kinases, protein phosphatases and proteins containing phosphoprotein-binding domains
- Authors: Yaping Guo, D. Peng, Jiaqi Zhou, Shaofeng Lin, Chenwei Wang et al.
- Year: 2018
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/57e1c09ce999b88b08a7dea6ea4f6439d98dd4dc
- DOI: 10.1093/nar/gky1063
- PMID: 30380109
- PMCID: 6324023
- Citations: 34
- Influential citations: 1
- Summary: The updated database iEKPD 2.0 was described, which provided rich annotations for the regulators of eight model organisms, especially humans, by compiling and integrating the knowledge from 100 widely used public databases that cover 13 aspects.
- Evidence snippets:
  - Snippet 1 (score: 0.681)
    > As a gene-centered database, iEKPD 2.0 provided the classification and domain profile information for each phospho-regulator as well as a variety of basic annotations obtained from Ensembl (31) and UniProt (35) databases, such as protein/gene names/aliases, functional descriptions, Ensembl/UniProt/GeneBank/RefSeq accession numbers, protein/nucleotide sequences, Kyoto Encyclopedia of Genes and Genomes (KEGG) and Gene Ontology (GO) terms, and domain/motifs. From UniProt (35), we also obtained the annotations of active sites for 10 569 unique phospho-regulators. In addition, the primary references of known phospho-regulators were obtained.
    > By integrating the knowledge of 100 additional databases, we further annotated 15 717 phospho-regulators in eight model organisms, including H. sapiens, M. musculus, R. norvegicus, D. melanogaster, C. elegans, A. thaliana, S. pombe and S. cerevisiae (Supplementary Table S7). These resources contained rich annotations that covered 13 aspects, including cancer mutations, genetic variations, disease-associated information, mRNA expression, DNA & RNA elements, molecular interactions, drug-target relations, protein 3D structures, PTMs, protein expression/proteomics, subcellular localizations and protein functional annotations (Supplementary Table S7). The data in each resource were carefully processed, and the details are presented in Supplementary Methods.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Xiaohua Jiang, Daren Zhao, Asim Ali, Bo Xu, Wei Liu et al. (2021). MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis. Frontiers in Cell and Developmental Biology. https://www.semanticscholar.org/paper/aeb08368a5540685473578345739bb569103bd46
3. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
4. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
5. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
6. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
7. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
8. Jun Shen, D. Scheffer, Kelvin Y. Kwan, D. Corey (2015). SHIELD: an integrative gene expression database for inner ear research. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/fc7704155cefd9f1c767dc2a03a5025c77d19437
9. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
10. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
11. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
12. Sophia Zachari, K. Liadaki, Angeliki Planaki, E. Zafiriou, Olga Kouvarou et al. (2025). A Genome-Wide Association Study Identifying Novel Genetic Markers of Response to Treatment with Interleukin-23 Inhibitors in Psoriasis. Genes. https://www.semanticscholar.org/paper/d5f656311b54e222e7487ea32a061869b30178a1
13. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
14. Keiichi Homma, Koji Suzuki, H. Sugawara (2010). The Autophagy Database: an all-inclusive information resource on autophagy that provides nourishment for research. Nucleic Acids Research. https://www.semanticscholar.org/paper/946ad0a62c6da7c1b288f58b48b6ce015835c176
15. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
16. Guido Dieterich, U. Kärst, Elmar Fischer, J. Wehland, L. Jänsch (2005). LEGER: knowledge database and visualization tool for comparative genomics of pathogenic and non-pathogenic Listeria species. Nucleic Acids Research. https://www.semanticscholar.org/paper/45beb8854f24aefef4f88845858c82cd7c62cdf8
17. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
18. F. Pfeiffer, A. Broicher, Thomas N Gillich, K. Klee, José Mejía et al. (2008). Genome information management and integrated data analysis with HaloLex. Archives of Microbiology. https://www.semanticscholar.org/paper/f1333d02086a84becaa054612dbb6316af6ba4c3
19. Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al. (2025). Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining. npj Drug Discovery. https://www.semanticscholar.org/paper/000083b7bd96cff5b3d1891b00ad332eed7d9add
20. Yaping Guo, D. Peng, Jiaqi Zhou, Shaofeng Lin, Chenwei Wang et al. (2018). iEKPD 2.0: an update with rich annotations for eukaryotic protein kinases, protein phosphatases and proteins containing phosphoprotein-binding domains. Nucleic Acids Research. https://www.semanticscholar.org/paper/57e1c09ce999b88b08a7dea6ea4f6439d98dd4dc