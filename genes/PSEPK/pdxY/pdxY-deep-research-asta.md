---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T03:27:44.875176'
end_time: '2026-07-07T03:27:56.054842'
duration_seconds: 11.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pdxY
  gene_symbol: pdxY
  uniprot_accession: Q88C26
  protein_description: 'RecName: Full=Pyridoxal kinase PdxY {ECO:0000255|HAMAP-Rule:MF_01639};
    Short=PL kinase {ECO:0000255|HAMAP-Rule:MF_01639}; EC=2.7.1.35 {ECO:0000255|HAMAP-Rule:MF_01639};'
  gene_info: Name=pdxY {ECO:0000255|HAMAP-Rule:MF_01639}; OrderedLocusNames=PP_5357;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the pyridoxine kinase family. PdxY subfamily.
  protein_domains: PM/HMP-P_kinase-1. (IPR013749); PyrdxlKinase. (IPR004625); Pyridoxal_kinase_PdxY.
    (IPR023685); Ribokinase-like. (IPR029056); Phos_pyr_kin (PF08543)
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
- **UniProt Accession:** Q88C26
- **Protein Description:** RecName: Full=Pyridoxal kinase PdxY {ECO:0000255|HAMAP-Rule:MF_01639}; Short=PL kinase {ECO:0000255|HAMAP-Rule:MF_01639}; EC=2.7.1.35 {ECO:0000255|HAMAP-Rule:MF_01639};
- **Gene Information:** Name=pdxY {ECO:0000255|HAMAP-Rule:MF_01639}; OrderedLocusNames=PP_5357;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the pyridoxine kinase family. PdxY subfamily.
- **Key Domains:** PM/HMP-P_kinase-1. (IPR013749); PyrdxlKinase. (IPR004625); Pyridoxal_kinase_PdxY. (IPR023685); Ribokinase-like. (IPR029056); Phos_pyr_kin (PF08543)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pdxY" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pdxY' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pdxY** (gene ID: pdxY, UniProt: Q88C26) in PSEPK.

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

### [1] Synthesis, characterization, and computational evaluation of some synthesized xanthone derivatives: focus on kinase target network and biomedical properties
- Authors: Wisam Taher Muslim, L. J. Mohammad, Munaf M. Naji, Isaac Karimi, Matheel D. Al-Sabti et al.
- Year: 2025
- Venue: Frontiers in Pharmacology
- URL: https://www.semanticscholar.org/paper/659ab502877a1d6b5ab7ce45fa51f0f9a13dcf24
- DOI: 10.3389/fphar.2024.1511627
- PMID: 39830340
- PMCID: 11738930
- Summary: Acute leukemic T-cells were one of the top predicted tumor cell lines for these ligands and the possible antileukemic effects of synthesized xanthone derivatives are potentially very interesting and warrant further studies.
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > The UniProt accession identification of target kinases was converted to gene symbols for humans using the SynGO gene set analysis tool (Koopmans et al., 2019), and pooled together, and submitted to GeneMANIA to construct target kinase network. GeneMANIA is a handy web interface for acquiring gene ontology, scrutinizing gene lists, and highlighting genes for functional assays (Warde-Farley et al., 2010). After choosing Homo sapiens from the list of optional organisms, the genes of interest in the previous step were entered into the search bar and the results were collated and high-scored genes were culled for further discussion. Moreover, the protein-protein network was also constructed in STRING ver. 12 launched at https://string-db.org, and submitted to Cytoscape ver. 3.10.2 for network analysis using a novel Cytoscape plugin cytoHubba and visualization (Shannon et al. , 2003).

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
  - Snippet 1 (score: 0.701)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

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
  - Snippet 1 (score: 0.699)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [4] HomoKinase: A Curated Database of Human Protein Kinases
- Authors: S. Subramani, Saranya Jayapalan, R. Kalpana, J. Natarajan
- Year: 2013
- Venue: International Scholarly Research Notices
- URL: https://www.semanticscholar.org/paper/81a21403fc772c6b9c00915e1124fad2cfb1894b
- DOI: 10.1155/2013/417634
- Citations: 18
- Summary: The present version of theomoKinase database contains 498 curated human protein kinases and links to other popular databases.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > The HomoKinase database creation involves several steps. First, human genes with their known aliases were downloaded from Entrez Gene (http://www.ncbi.nlm.nih.gov/ gene) using the query term "(Homo sapiens [Organism]) AND HGNC. " Next, the retrieved gene list was crosschecked with the HUGO Gene Nomenclature Committee (HGNC) (http://www.genenames.org/) database to include only the genes with HGNC approved gene name for building the database [7]. The other genes in the list such as pseudogenes, noncoding RNAs, and phenotype which have no HGNC approved name were eliminated.
    > Finally, gene ontology based refinement was performed to classify the protein kinase genes from the HGNC approved list of human protein-coding genes. In general, GO is mainly focused on three significant ontology terms such as molecular function, cellular component, and biological process. A single gene product may be annotated to multiple GO terms, detailing a range of functional attributes, using both manual and electronic annotation methods [8,9]. The conserved protein kinase core consists of two lobes: a smaller Nterminal lobe (N-lobe) with ATP binding site and a larger C-terminal lobe (C-lobe) with catalytic site responsible for kinase activity [3,10]. In addition, the biological processes correspond to protein phosphorylation. These three unique terms of gene ontology (GO) provide precise information about the annotated gene, gene products, and other terms which in turn provide a deep insight about kinases to the researchers. So, we classify the HGNC approved human genes which confirms these three GO terms: (i) ATP binding, (ii) kinase activity, and (iii) protein phosphorylation as true protein kinases. Gene ontology search was performed using two web tools, namely, Quick Go [11] and Amigo Go [12] with automated PHP scripts. The HGNC approved human genes, which satisfy all these three GO criteria, were classified as human protein kinases and used to build the database.
  - Snippet 2 (score: 0.688)
    > The HGNC approved human genes, which satisfy all these three GO criteria, were classified as human protein kinases and used to build the database.
    > The predicted list of protein kinases were further divided into groups, families, subfamilies, and domains. The group classifications were done using the PhosphoSite database [13], whereas the superfamily, family, subfamily, and domain level classifications were retrieved from UniProt [14]. In addition, various biological information such as official symbol, full name, biological IDs, other known aliases, amino acid sequences, functional domain, gene ontology, pathway assignments, and drug compounds were extracted from various biological databases such as (i) NCBI, (ii) UniProt, (iii) Amigo Go, (iv) KEGG, and (v) DrugBank. Figure 2 depicts a schematic summary of the HomoKinase data warehouse creation process.
    > The curated human protein kinase names and their related information retrieved from other databases were used to develop the HomoKinase database. The HomoKinase database is implemented as client/server architecture with easy-to-use web interface. The server is made of MySQL database, and the web client and programs for the human protein kinase retrieval, annotation, and query interface were designed using PHP programming language. Entrez Gene stores information on 1,93,709 genes specific to Homo sapiens (as on October 2012). We retrieved 33,489 human genes/proteins specific to our query term "(Homo sapiens [Organism] AND HGNC). " On further comparison with HGNC database, only the 19,026 genes have official HGNC gene symbol, and the remaining were 8399 pseudogenes, 4230 noncoding RNAs, 707 phenotype, and 1127 other genes.
    > The 19,032 HGNC approved human genes were further classified into protein kinases by checking the presence of three GO annotation terms (i) ATP binding property, (ii) kinase activity, and (iii) protein phosphorylation property. The HGNC approved genes fulfilling the above three GO properties (e.g., CDK1, MARK1) were classified as protein kinases and included in the database.

### [5] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.692)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [6] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.688)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [7] KinaseFusionDB: an integrative knowledge of kinase fusion proteins in multi-scales
- Authors: H. Kumar, Zikang Chen, Abayomi Adegunlehin, Loren Trowbridge, Leonardo Aguilar et al.
- Year: 2025
- Venue: Briefings in Bioinformatics
- URL: https://www.semanticscholar.org/paper/d212d0a2c8e4a7cedcd2c1e4fa11ed6de23345f7
- DOI: 10.1093/bib/bbaf259
- PMID: 40471992
- PMCID: 12140011
- Summary: A novel in silico pipeline for predicting 3D structures of kinase fusion proteins and performing structure-based virtual screening, which revealed that most predicted structures showed high pLDDT scores (pLDDT >70) within conserved kinase domains.
- Evidence snippets:
  - Snippet 1 (score: 0.679)
    > To assign the functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases, and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', Figure 1. Overview of KinaseFusionDB and its role in understanding kinase fusion proteins. (a) I. The top section identifies therapeutic targets for oncogenic activation of kinases, including wild-type kinases activated by overexpression or genomic amplification, mutated kinases with gain-offunction mutations, and kinase fusion proteins resulting from chromosomal rearrangements. II. The middle section highlights the functionalities of KinaseFusionDB, such as providing functional annotations, mRNA/protein expression data, drug binding information, and relevant literature reviews. III. The third section addresses the current limitations in targeting kinase fusion proteins, particularly the lack of comprehensive 3D structures for these proteins. It emphasizes the partial knowledge of kinase fusion protein structures and the need for further drug screening. IV. The bottom section discusses how computational approaches, such as predicted 3D structures (e.g. from AlphaFold2), can fill these gaps, supporting drug screening and filtering based on consistent binding among multiple fusion protein isoforms. (b) Kinase domain-retained human kinase fusion proteins.
    > 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane', and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt [26] accessions from UniProt for 10 619 genes involved in 15 030 fusion genes [27]. UniProt provides the loci information of 39 protein features, including 6 molecule processing features, 13 region features, 4 site features, 6 amino acid modification features, 2 natural variation features, 5 experimental info features, and 3 secondary structure features.

### [8] An Asymmetrically Balanced Organization of Kinases versus Phosphatases across Eukaryotes Determines Their Distinct Impacts
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
  - Snippet 1 (score: 0.676)
    > The annotations of genes to different molecular functions were obtained from the Gene Ontology (GO) Database [38]. We chose to work with GO annotations since they were in good agreement with other sources and provided a consistent framework across the different organisms. Kinases and phosphatases were defined as genes with molecular function annotation of 'protein kinase activity' (GO:0004672) or 'phosphoprotein phosphatase activity' (GO:0004721), respectively. Regulators of histone acetylation were defined as genes with 'histone acetyltransferase activity' (GO:0004402) or 'histone deacetylase activity' (GO:0004407) annotations. Regulators of protein ubiquitination were defined as genes with "ubiquitin-protein transferase activity" (GO:0004842) or "thiol-dependent ubiquitin-specific protease activity" (GO:0004843) annotations. For H. sapiens we considered only genes that were reviewed by UniProt database [39]. For A. thaliana we considered only genes with annotated TAIR accessions [40]. For D. melanogaster we considered only genes with annotated FlyBase accessions [41]. For M. musculus we considered only genes with annotated MGI accessions [42]. For C. elegans we considered all kinases and phosphatases annotated with multivulva or vulvaless phenotype according to WormBase [30]. To validate the trends we observed, we also analyzed curated kinases and phosphatases extracted from organism-specific databases, which showed similar results (S6 Fig).

### [9] Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale
- Authors: P. Kramer, Jack Treml
- Year: 2022
- Venue: Midwestern Journal of Undergraduate Sciences
- URL: https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27
- DOI: 10.17161/mjusc.v1i1.18565
- Summary: The following is a walkthrough of a project designed to overcome the lack of sense for proteins as real objects.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > i. Click "See more" to view a bar chart containing data on where in the body's tissues the gene is expressed (as determined by RNA sequencing). Save and include this bar chart as the deliverable for this step.
    > II. Universal Protein Research Knowledgebase (UniProtKB) 8 6. UniProt Entry Number
    > i. Follow the UniProt link in the Resources then search for the protein using the NCBI Gene ID ii. Carefully select the result that best matches the gene and organism of interest by clicking on the blue entry number. iii. This page will be used later to gather further details about the protein.
    > III. RCSB Protein Data Bank (PDB) 9 7. RCSB PDB Solved Structure Identifi er i. Follow the RCSB PDB link in the Resources and search for the protein by either the common name or the NCBI Gene ID, making sure to select the organism of interest on the left. ii. You must ensure that your chosen protein has an existing solved structure in this data bank in order to do a mutational analysis in later parts of this exercise.
    > IV. NCBI GenBank 10 8. AA Protein Sequence i. From the NCBI Gene page, go to the "Genomic regions, transcripts, and products" section and then click "GenBank" on the right. Scroll down to the fi rst Coding Sequence "CDS" section and look directly after "/translation=" for the full protein sequence. ii. Sequence needs to be in FASTA Format consisting of '>' followed by a simple name, a return, and then the sequence in one continuous line of text. See "FASTA Formatting" link in Resources.

### [10] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.670)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [11] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Citations: 1
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [12] drawProteins: a Bioconductor/R package for reproducible and programmatic generation of protein schematics
- Authors: P. Brennan
- Year: 2018
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/9bf4dc397d29f68a9f271c47b02bb17aeca65fb6
- DOI: 10.12688/f1000research.14541.1
- PMID: 30210791
- PMCID: 6107989
- Citations: 55
- Influential citations: 7
- Summary: The drawProteins package is to enable the generation of schematics of proteins in an automated fashion that can integrate with the Bioconductor/R suite of tools for bioinformatics and statistical analysis.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > It is possible to use bioMart 11,12 to pull out the UniProt accession numbers for a Gene Ontology (GO) term. For example, the GO term for "MAP kinase activity". This has a GO number of GO:0004707. This example script borrows heavily on the biomaRt users guide written by Steffen Durinck, Wolfgang Huber and Mike Smith 13 . The script below generates a visualization containing 14 protein schematics (Figure 5).
    > # install bioMart if you haven't used it before # remove the hash tags... # source("http://www.bioconductor.org/biocLite.R ") # biocLite() # biocLite("biomaRt") library(biomaRt) # chosing a database = MART and a dataset -gets more focussed each step... ensembl = useMart("ensembl", dataset="hsapiens_gene_ensembl")
    > # Retrieve all entrezgene identifiers and HUGO gene symbols of genes which have # a "MAP kinase activity" GO term associated with it. # this is the GO:0004707 # this gives 14 proteins.... # create output in a dataframe and add uniprotswissprot # which is the UniProt ID output <-getBM(attributes = c('uniprotswissprot', 'hgnc_symbol'), filters = 'go', values = 'GO:0004707', mart = ensembl) # returns a dataframe... pull out uniprotIDs for drawing... uniprotIDs <-output$uniprotswissprot # get rid of blank entries -turn into NA uniprotIDs[uniprotIDs==""] <-NA # remove NA uniprotIDs <-na.omit(uniprotIDs) # make the IDs characters uniprotIDs <-as.character(uniprotIDs)

### [13] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.665)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [14] Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms
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
  - Snippet 1 (score: 0.662)
    > Examples are for illustrative purposes only and specific to each case, hence not all the entities are shown and highlighted. RED: Gene/Protein BLUE: Disease GREEN: Organism a. Biomedical concepts Gene/Protein: Annotations could be specific gene/protein names or classes/family names of gene/proteins. In particular, very broad concepts like "protein", "gene", "enzyme", "receptors", "kinase", "cytokine", "transcription regulators/factors" are out of the scope of annotations. However, family/subtype names of those concepts are considered for the annotations, such as "amylolytic enzyme", "antioxidant enzyme", "map kinase p38", because these terms narrow the concepts to specific families of gene/protein, enzyme.
    > Annotators can refer to Uniprot and Protein Ontology.

### [15] FusionPDB: a knowledgebase of human fusion proteins
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
  - Snippet 1 (score: 0.657)
    > To assign functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt for 10 619 genes involved in 15 030 fusion genes ( 10 ). UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features and three secondary structure features. Since such feature loci information is based on amino acid sequences, the genomic breakpoint information was converted into the amino acid level while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE (v19) gene model of human reference genome ( 11 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported such fusion genes as having not retained that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.

### [16] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
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
  - Snippet 1 (score: 0.657)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [17] The Annotation of Both Human and Mouse Kinomes in UniProtKB/Swiss-Prot
- Authors: S. Quintaje, S. Orchard
- Year: 2008
- Venue: Molecular & Cellular Proteomics
- URL: https://www.semanticscholar.org/paper/75cfc927e8d88cecfe132572301b7d6a97172a80
- DOI: 10.1074/mcp.R700001-MCP200
- PMID: 18436524
- Citations: 42
- Summary: This review will detail the state-of-the-art human and mouse kinomes as provided in the UniProtKB/Swiss-Prot protein knowledgebase as well as providing a central portal to a wealth of further detail via extensive cross-referencing.
- Evidence snippets:
  - Snippet 1 (score: 0.652)
    > As part of the annotation process, UniProtKB strives to provide a unified name for both gene and protein product that describes the function of the enzyme while retaining a unique identification that is recognizable by the scientific community; it is most commonly based on the gene name (Fig. 2). The primary name follows a series of rules, which have been made public by the UniProtKB consortium, that enable a protein to be assigned a recommended name providing the maximal amount of information about that gene product while still enabling its propagation across orthologues in other organisms. The database works closely with other nomenclature groups, such as the Human Genome Nomenclature Committee (10) and the Mouse Genome Informatics (11), which are cross-referenced from within the appropriate entries. However, many kinases are already known by more than one well accepted name, and where it proves impossible to include these within the primary name, they are retained within the entry as a synonym to allow ease of searching. All entries have a stable accession number and a human readable identification. The latter, however, should not be regarded as stable because these are occasionally updated, for example with change of gene name. The activity of the kinase, as described by the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology, is captured within the protein description as the Enzyme Classification (EC) number (12).

### [18] Centrality of drug targets in protein networks
- Authors: A. Follis
- Year: 2021
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/042dee46e3d0a0e64c02b21e1fb9e97e7bc403d8
- DOI: 10.1186/s12859-021-04342-x
- PMID: 34715787
- PMCID: 8555226
- Citations: 20
- Influential citations: 1
- Summary: These findings expand on previous reports of drug targets’ network centrality by suggesting some centrality metrics such as low topological coefficient as inherent characteristics of a ‘good’ target, relative to other exploratory targets and regardless of its functional class.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > org/) with the ChEMBL and Uniprot identifiers further retrieved the corresponding String identifiers. The functional classification of targets based on Gene Ontology [33] (GO) terms was performed using the StringDB GO-terms analysis tool applied to 'molecular function' annotations, pooling proteins by the following logical combinations of identifiers: channel or transporter (class 'channels and transporters); enzyme not kinase (class 'enzymes'); GPCR or G-protein coupled receptor (class 'GPCRs'); kinase (class 'kinases'); nuclear receptor (class 'nuclear receptors'). The complete set of GO annotations for the Uniprot reference human proteome (goa file) was downloaded from the Gene Ontology Consortium web page (http:// curre nt. geneo ntolo gy. org/ produ cts/ pages/ downl oads. html) The number of citations for each target protein was retrieved from automated Pub-Med searches (https:// pubmed. ncbi. nlm. nih. gov) using the proteins gene abbreviation as search term applying the filters: 'human' , 'journal article' and 'title-abstract' . Search automation was implemented using a Knime [49] 'GET Request' node workflow. Disease association annotations were downloaded from the DisGeNet web page (curated gene-disease associations) (https:// www. disge net. org/ downl oads#) and Genetic Association Database web page (https:// genet icass ociat iondb. nih. gov/).

### [19] AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes
- Authors: D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al.
- Year: 2023
- Venue: Mammalian Genome
- URL: https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99
- DOI: 10.1007/s00335-023-10008-1
- PMID: 37460664
- PMCID: 10382368
- Citations: 5
- Summary: This work presents genome visualization and annotation tools to support seven livestock species, available in a new resource called AgAnimalGenomes, and describes the data and search methods available and how to use the provided tools to edit and create new gene models.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > As previously described (Triant et al. 2020), once a proteincoding gene annotation is complete, each new or modified isoform should be compared to a well-curated protein sequence database to check for congruency with known proteins. The sequence of an annotation is obtained by right clicking it and selecting Get Sequence. The first choice of database to search is the well-curated UniProtKB/Swissprot database using BLAST at either the UniProt (https:// www. unipr ot. org/ blast) or NCBI website (https:// blast. ncbi. nlm. nih. gov/ Blast. cgi) (Sayers et al. 2023a;UniProt Consortium 2023). If there is no match with a significant e-value (< 1e−05) in UniProtKB/Swissprot, the next database to try is the Model Organisms (landmark) database at NCBI. If that fails, select the RefSeq Proteins database and exclude your organism of interest from the search. Although RefSeq includes computationally predicted and hypothetical proteins, an alignment to a homologous protein from another organism provides support for the annotation. An alignment that covers the full length of both the annotated protein and the database protein sequence suggests the annotation is correct. An alignment that encompasses the full length of an annotated protein sequence but only part of a database protein suggests that the annotation is truncated. You may be able to correct the annotation with additional evidence, but if there is not sufficient evidence the issue can be noted in the Annotation Information Panel under the Comment tab. A partial alignment of an annotated protein to a database protein suggests the annotation has a reading frame shift or was extended incorrectly. Aligning the coding sequence (CDS) to the protein database will reveal whether the problem is due to a reading frame shift. Further annotation editing should be performed to correct the reading frame. If an incorrect extension was due to the merging of two genes, you should edit or redo the annotation. Any unresolved issues should be entered in the Comment section of the Annotation Information Panel.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Wisam Taher Muslim, L. J. Mohammad, Munaf M. Naji, Isaac Karimi, Matheel D. Al-Sabti et al. (2025). Synthesis, characterization, and computational evaluation of some synthesized xanthone derivatives: focus on kinase target network and biomedical properties. Frontiers in Pharmacology. https://www.semanticscholar.org/paper/659ab502877a1d6b5ab7ce45fa51f0f9a13dcf24
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
4. S. Subramani, Saranya Jayapalan, R. Kalpana, J. Natarajan (2013). HomoKinase: A Curated Database of Human Protein Kinases. International Scholarly Research Notices. https://www.semanticscholar.org/paper/81a21403fc772c6b9c00915e1124fad2cfb1894b
5. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
6. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
7. H. Kumar, Zikang Chen, Abayomi Adegunlehin, Loren Trowbridge, Leonardo Aguilar et al. (2025). KinaseFusionDB: an integrative knowledge of kinase fusion proteins in multi-scales. Briefings in Bioinformatics. https://www.semanticscholar.org/paper/d212d0a2c8e4a7cedcd2c1e4fa11ed6de23345f7
8. Ilan Y. Smoly, N. Shemesh, Michal Ziv-Ukelson, Anat Ben-Zvi, Esti Yeger Lotem (2017). An Asymmetrically Balanced Organization of Kinases versus Phosphatases across Eukaryotes Determines Their Distinct Impacts. PLoS Computational Biology. https://www.semanticscholar.org/paper/4f13e00bf92fc0e75e910dd6a62d87286a816e6b
9. P. Kramer, Jack Treml (2022). Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale. Midwestern Journal of Undergraduate Sciences. https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27
10. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
11. Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
12. P. Brennan (2018). drawProteins: a Bioconductor/R package for reproducible and programmatic generation of protein schematics. F1000Research. https://www.semanticscholar.org/paper/9bf4dc397d29f68a9f271c47b02bb17aeca65fb6
13. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
14. Xiao Yang, Shyamasree Saha, Aravind Venkatesan, Santosh Tirunagari, Vid Vartak et al. (2023). Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms. Scientific Data. https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
15. H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim (2023). FusionPDB: a knowledgebase of human fusion proteins. Nucleic Acids Research. https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
16. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
17. S. Quintaje, S. Orchard (2008). The Annotation of Both Human and Mouse Kinomes in UniProtKB/Swiss-Prot. Molecular & Cellular Proteomics. https://www.semanticscholar.org/paper/75cfc927e8d88cecfe132572301b7d6a97172a80
18. A. Follis (2021). Centrality of drug targets in protein networks. BMC Bioinformatics. https://www.semanticscholar.org/paper/042dee46e3d0a0e64c02b21e1fb9e97e7bc403d8
19. D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al. (2023). AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes. Mammalian Genome. https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99