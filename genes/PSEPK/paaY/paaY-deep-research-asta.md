---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T02:50:17.534696'
end_time: '2026-07-10T02:50:22.453315'
duration_seconds: 4.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaY
  gene_symbol: paaY
  uniprot_accession: Q88HR8
  protein_description: 'SubName: Full=Detoxifying thioesterase of the phenylacetate
    degradation pathway {ECO:0000313|EMBL:AAN68892.1};'
  gene_info: Name=paaY {ECO:0000313|EMBL:AAN68892.1}; OrderedLocusNames=PP_3285 {ECO:0000313|EMBL:AAN68892.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Hexapep. (IPR001451); PaaY. (IPR011974); Transf_Hexapept/Carb_Anhydrase.
    (IPR050484); Trimer_LpxA-like_sf. (IPR011004); Hexapep (PF00132)
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
- **UniProt Accession:** Q88HR8
- **Protein Description:** SubName: Full=Detoxifying thioesterase of the phenylacetate degradation pathway {ECO:0000313|EMBL:AAN68892.1};
- **Gene Information:** Name=paaY {ECO:0000313|EMBL:AAN68892.1}; OrderedLocusNames=PP_3285 {ECO:0000313|EMBL:AAN68892.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Hexapep. (IPR001451); PaaY. (IPR011974); Transf_Hexapept/Carb_Anhydrase. (IPR050484); Trimer_LpxA-like_sf. (IPR011004); Hexapep (PF00132)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaY" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaY' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaY** (gene ID: paaY, UniProt: Q88HR8) in PSEPK.

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
  - Snippet 1 (score: 0.797)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.683)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] Ten steps to get started in Genome Assembly and Annotation
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
  - Snippet 1 (score: 0.760)
    > The ultimate goal of the functional annotation process (Figure 4) is to assign biologically relevant information to predicted polypeptides, and to the features they derive from (e.g. gene, mRNA). This process is especially relevant nowadays in the context of the NGS era due to the capacity of sequencing, assembling, and annotating full genomes in short periods of time, e.g. less than a month. Functional elements could range from putative name and/or symbols for protein-coding genes, e.g. ADH to its putative biological function, e.g. alcohol dehydrogenase, associated gene ontology terms, e.g. GO:0004022, functional sites, e.g. METAL 47 47 Zinc 1, and domains, e.g. IPR002328, among other features. The function of predicted proteins can be computationally inferred based on the similarity between the sequence of interest and other sequences in different public repositories, e.g. BLASTP against Uniprot. Caution should be taken when assigning results merely based on sequence similarity as two evolutionary independent sequences which share some common domains could be considered homologs 62 . Thus, whenever possible, it is better to use orthologous sequences for annotation purposes rather than simply similar sequences 63 . With the growing number of sequences in those public repositories, it is possible to perform various searches and combine obtained results into a consensus annotation. The accurate assignment of the functional elements is a complex process, and the best annotation will involve manual curation.
    > There are two main outcomes of the functional annotation process. The first is the assignment of functional elements to genes. Downstream analysis of these elements allow further understanding of specific genome properties, e.g. metabolic pathways, and similarities compared with closely related species. The second result of the functional annotation is the additional quality check for the predicted gene set. It is possible to identify problematic and/or suspicious genes by the presence of specific domains, suspicious orthology assignment and/or absence of other functional elements, e.g. functional completeness. These Page 13 of 19

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
  - Snippet 1 (score: 0.758)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [4] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.749)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [5] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.717)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [6] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.715)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [7] Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea
- Authors: A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al.
- Year: 2023
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
- DOI: 10.3389/fmicb.2023.1066096
- PMID: 36876067
- PMCID: 9981795
- Citations: 2
- Summary: The present study concludes that deciphering the whole genome of F. udum would be instrumental in understanding evolution, virulence determinants, host-pathogen interaction, possible control strategies, ecological behavior, and many other complexities of the pathogen.
- Evidence snippets:
  - Snippet 1 (score: 0.711)
    > The BLASTx homology search tool, a component of the standalone NCBI-blast-2.3.0+, was used to perform functional annotation of the F. udum genes (Altschul et al., 1990). With a cut-off E value of ≤1e−06 and a similarity of 34%, BLASTx identified the homologous sequences of the genes in the NCBI non-redundant protein database. Gene ontology (GO) analysis was carried out using Blast2GO PRO 4.1.5 (Conesa and Gotz, 2008). In three different mappings, B2G performed as follows: (1) Using two NCBI-provided mapping files, blast result accessions are used to get gene names (symbols; gene info, gene 2 accessions). (2) Blast result GI identifiers were used to retrieve UniProt IDs using a mapping file from PIR (non-redundant reference protein database), which includes PSD, Swiss-Prot, UniProt, TrEMBL, GenPept, RefSeq, and PDB. The names of the identified genes were searched in the species-specific entries of the gene product table of the GO database. With the aid of the KAAS-KEGG Automatic Annotation Server, pathway analyses were carried out. This database provides functional annotation of genes using other data servers (Moriya et al., 2007). Accessions from the blast results were looked for in the DBXRef table of the GO database.

### [8] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.710)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [9] Protein modification characteristics of the malaria parasite Plasmodium falciparum and the infected erythrocytes.
- Authors: Jianhua Wang, Ning Jiang, Xiaoyu Sang, N. Yang, Ying Feng et al.
- Year: 2020
- Venue: Molecular & cellular proteomics : MCP
- URL: https://www.semanticscholar.org/paper/51e4f3979cfebff284dd479acc8890c973f7af52
- DOI: 10.1074/mcp.RA120.002375
- PMID: 33148788
- Citations: 19
- Influential citations: 1
- Summary: An extensive proteome-wide dissection revealed a fine PTM map of most proteins in both Plasmodium falciparum and its host cell and the infected red blood cells, providing a valuable resource for mining new antimalarial targets.
- Evidence snippets:
  - Snippet 1 (score: 0.706)
    > Gene Ontology (GO) annotation of proteins was derived from the UniProt-GOA database (www. http://www.ebi.ac.uk/GOA/). The protein accession was first converted to the GO ID, and then the protein function was annotated with Uniprot-GOA. If the proteins were not annotated by the Uniprot-GOA database, the annotation was produced by the InterProScan software based on the sequence alignment of proteins. The Kyoto Encyclopedia of Genes and Genomes (KEGG) database was used to annotate the pathways of proteins. The protein description from the KEGG pathway was annotated by the online service tools KAAS and KEGG mapper in the KEGG database. The functional enrichment was analyzed using Fisher's exact test.

### [10] Prediction of Horizontally and Widely Transferred Genes in Prokaryotes
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
  - Snippet 1 (score: 0.706)
    > Focusing on uncharacterized HT genes in the COG and KEGG databases, four gene groups (COG3209, COG1479, COG3291, and COG3791) were classified into "general function prediction only" (COG category code = R) or "function unknown" (S) according to the COG annotation. By adding two gene groups of "uncharacterized protein" (K08998 and K07062) from the KEGG annotation, a total of six were obtained as functionally ambiguous HT gene groups despite being distributed among more than 300 species. With reference to COG3209 (uncharacterized conserved protein RhaS, contains 28 RHS repeats), the genes encoded in E. coli have been suggested to be horizontally transferred from another organism. 43 Recently, RHS repeat-containing genes are reported to be involved in toxins against competitors 44 ; therefore, the genes in COG3209 could be considered as defense system genes. The functions of COG1479 (uncharacterized conserved protein, contains ParB-like and HNH nuclease domains), COG3291 (PKD repeat), and COG3791 (uncharacterized conserved protein) have yet to be examined. According to InterPro analysis, COG3791 genes have a domain of glutathione-dependent formaldehyde-activating enzyme (IPR006913); therefore, these genes might be related to formaldehyde detoxification. 45 The KO group, K08998, corresponds to COG0759 (membraneanchored protein YidD) of category M in the COG database that has previously been reported to be involved in the protein insertion process. 46 K07062 corresponds to COG1487 and is considered a toxic protein. 47 As a whole, it has to be said that the evolutionary significance of these six gene groups has not been fully realized. Conversely, these genes might be good targets for evolutionary studies in the context of HGT, providing an example of data-driven approaches from massive sequence data. 48

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
  - Snippet 1 (score: 0.705)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [12] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.702)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [13] Protein Localization Analysis of Essential Genes in Prokaryotes
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
  - Snippet 1 (score: 0.694)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

### [14] Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops
- Authors: Yi Zheng, Shan Wu, Yang Bai, Honghe Sun, C. Jiao et al.
- Year: 2018
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/a7bb1e82b8172252d79ee35170dfe038c4b17d78
- DOI: 10.1093/nar/gky944
- PMID: 30321383
- PMCID: 6324010
- Citations: 174
- Influential citations: 7
- Summary: The Cucurbit Genomics Database has been developed using the Tripal toolkit and two new tools have been developed, a ‘SyntenyViewer’ to view genome synteny between different cucurbit species and an ‘RNA-Seq’ module to analyze and visualize gene expression profiles.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > The submenu provides links to a pathway database, a genome browser, an FTP site for downloading genome and gene sequences and annotations, and bioinformatics tools such as BLAST, batch query and basic search functions.
    > A total of 265 334 protein-coding genes have been predicted from these 10 genomes and included in the database. A standard and unified procedure has been developed to comprehensively annotate predicted protein-coding genes. First, protein sequences of the predicted genes are compared against the GenBank non-redundant protein (nr), UniProt (TrEMBL and SwissProt), and Arabidopsis protein databases using the BLAST program with an E-value cutoff of 1e-4. The protein sequences are further compared against the InterPro database using InterProScan (21) to identify functional protein domains. The BLAST results D1130 Nucleic Acids Research, 2019, Vol. 47, Database issue against the nr database and the identified InterPro domains are fed to the Blast2GO program (22) for assigning gene ontology (GO) terms to protein-coding genes, and the BLAST results against the UniProt and Arabidopsis protein databases are loaded into the AHRD program (https: //github.com/groupschoof/AHRD) to assign concise, informative and precise functional descriptions of genes. The top BLAST hits (homologs), GO terms and InterPro domains assigned to each of the protein-coding genes have been imported into CuGenDB using Tripal Analysis Extension Modules (16). The functional descriptions generated by AHRD are loaded into the database using an inhouse Perl script. Each gene has a detailed feature page in the database that contains all the related sequence and annotation information; the gene feature page is divided into different sections based on the content types (Figure 1).

### [15] Identifying stress responsive genes using overlapping communities in co-expression networks
- Authors: Camila Riccio-Rengifo, J. Finke, Camilo Rocha
- Year: 2020
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/5410fad9d5b6c743bd156e67c9b7befc16deb5a3
- DOI: 10.1186/s12859-021-04462-4
- PMID: 34743699
- PMCID: 8574028
- Citations: 8
- Summary: A more effective framework to reduce the search-space for target genes that respond to a specific treatment is introduced, which facilitates experimental validation by restraining efforts to a smaller subset of genes of high potential relevance.
- Evidence snippets:
  - Snippet 1 (score: 0.687)
    > This is the final step of the workflow. Its goal is to annotate with additional information the genes identified in previous stages, helping to elucidate their possible behavior and role in the response to the treatment under study. A crucial step is to identify the differentially expressed genes in the set I. That is, to select the genes in I that have an absolute value of the Log Fold Change of at least 2 (| ij | ≥ 2) for at least one sample. This corresponds to genes whose expression level is quadrupled (up or down) from the control to treatment condition; they are the target genes.
    > Furthermore, functional category enrichment can be carried out by, e.g., searching for gene ontology annotations in databases such as QuickGO [5], UniProt [10], and the Rice Genome Annotation Project [21]. Such annotations can provide evidence of biological implications of the target genes in the treatment-tolerance mechanisms. Furthermore, those databases can be used to identify the protein products of genes, which can be used in turn to provide new insights on how target genes are involved in functional pathways related to treatment. Such analysis includes a review of reported protein-protein interactions in databases such as STRING [41]. The protein interactions include direct (physical) and indirect (functional) associations. They stem from computational prediction, knowledge transfer between organisms, and interactions aggregated from other (primary) databases. The search for unknown interactions would extend the workflow with additional steps.

### [16] Into the metabolic wild: Unveiling hidden pathways of microbial metabolism
- Authors: Özge Ata, D. Mattanovich
- Year: 2024
- Venue: Microbial Biotechnology
- URL: https://www.semanticscholar.org/paper/81ac8bfd05a0c52f8a5b6d058c5414b45bb5c1f9
- DOI: 10.1111/1751-7915.14548
- PMID: 39126421
- PMCID: 11316390
- Citations: 5
- Summary: The predictive power of metabolic modelling, well‐founded on biochemical knowledge and genomic information is discussed in the light of both discovery of yet unknown existing metabolic routes and the prediction of others, new to Nature.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > One major concern regarding genome data is the potential spread of false or inaccurate functional annotations iterating by sequence similarity-based gene annotations where functions are ascribed by analogy to other organisms' genes rather than being experimentally verified. As the source of information on a putative gene function is not always clearly indicated in databases, we advise researchers to always trace the original literature related to a gene function to verify its plausibility in a given non-model organism.
    > A special case is the genes with no known functional annotation in model organisms, like the y-genes in E. coli (so named because their gene names begin with the letter y). Ghatak et al. (2019) used multiple databases to define the y-ome of E. coli as the 35% genes that lack experimental evidence of their function, and highlight the differences between genes that lack any known function and those with attributed localization or computationally annotated functional domains. A similar situation is observed with eukaryotic genomes, where a consistent fraction of about 20% of the genes remains with unknown (or unstudied) gene products. Wood et al. (2019) compared unknown gene products of Schizosaccharomyces pombe, S. cerevisiae, and Homo sapiens, and concluded that these genes remained understudied even since genome sequences were published. They disprove the common assumption that unknown gene products are mostly orphaned, as the majority are conserved from yeasts to humans, and they conclude that the reasons for the lack of research on these proteins is two-fold. For many of these genes, no apparent knockout phenotype was observed in standard conditions. On the other hand, researchers still focus on a few well-studied proteins rather than exploring unknown territories, which the authors partly ascribe to risk-adverse strategies of funders and reviewers.
    > Although the primary use of metabolic models is the analysis of already known metabolic pathways, the potential of metabolic models extends far beyond these analyses. They can be used to uncover hidden pathways, unknown reactions, and to construct de novo pathways.

### [17] HomoKinase: A Curated Database of Human Protein Kinases
- Authors: S. Subramani, Saranya Jayapalan, R. Kalpana, J. Natarajan
- Year: 2013
- Venue: International Scholarly Research Notices
- URL: https://www.semanticscholar.org/paper/81a21403fc772c6b9c00915e1124fad2cfb1894b
- DOI: 10.1155/2013/417634
- Citations: 18
- Summary: The present version of theomoKinase database contains 498 curated human protein kinases and links to other popular databases.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > The HGNC approved human genes, which satisfy all these three GO criteria, were classified as human protein kinases and used to build the database.
    > The predicted list of protein kinases were further divided into groups, families, subfamilies, and domains. The group classifications were done using the PhosphoSite database [13], whereas the superfamily, family, subfamily, and domain level classifications were retrieved from UniProt [14]. In addition, various biological information such as official symbol, full name, biological IDs, other known aliases, amino acid sequences, functional domain, gene ontology, pathway assignments, and drug compounds were extracted from various biological databases such as (i) NCBI, (ii) UniProt, (iii) Amigo Go, (iv) KEGG, and (v) DrugBank. Figure 2 depicts a schematic summary of the HomoKinase data warehouse creation process.
    > The curated human protein kinase names and their related information retrieved from other databases were used to develop the HomoKinase database. The HomoKinase database is implemented as client/server architecture with easy-to-use web interface. The server is made of MySQL database, and the web client and programs for the human protein kinase retrieval, annotation, and query interface were designed using PHP programming language. Entrez Gene stores information on 1,93,709 genes specific to Homo sapiens (as on October 2012). We retrieved 33,489 human genes/proteins specific to our query term "(Homo sapiens [Organism] AND HGNC). " On further comparison with HGNC database, only the 19,026 genes have official HGNC gene symbol, and the remaining were 8399 pseudogenes, 4230 noncoding RNAs, 707 phenotype, and 1127 other genes.
    > The 19,032 HGNC approved human genes were further classified into protein kinases by checking the presence of three GO annotation terms (i) ATP binding property, (ii) kinase activity, and (iii) protein phosphorylation property. The HGNC approved genes fulfilling the above three GO properties (e.g., CDK1, MARK1) were classified as protein kinases and included in the database.

### [18] Prioritising genetic findings for drug target identification and validation.
- Authors: N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt
- Year: 2024
- Venue: Atherosclerosis
- URL: https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9
- DOI: 10.1016/j.atherosclerosis.2024.117462
- PMID: 38325120
- Citations: 11
- Summary: The current review provides an overview of genetic evidence for drug target identification, and how biomedical databases can be used to provide actionable prioritisation, fully informing downstream experimental validation.
- Evidence snippets:
  - Snippet 1 (score: 0.684)
    > Other gene identification systems include the Entrez Gene [43] database for gene-specific information, and the HUGO Gene Nomenclature Committee (HGNC) [44] which maintains unique symbols and names for human loci.An analogue for proteins is the UniProt Knowledgebase (UniProtKB) [45], which contains data on protein sequences and function, and each protein in the database is assigned a unique UniProt accession ID.UniProt provides functionality to map between different identifiers, including Ensembl IDs and UniProt accession IDs.
    > A common naming convention is also required to identify the diseases associated with the drug targets.Medical Subject Headings (MeSH) [46] are terms defined by the National Library of Medicine, and act as a standardised thesaurus for diseases and medical conditions which can be used to index PubMed.In some data sources, such as the Chemical Biology Database (ChEMBL) [23], diseases and outcomes will be identified by MeSH terms.However, in other cases, this will not be the case, and a metathesaurus such as the Unified Medical Language System (UMLS) [47] can be used to map synonymous disease terms.

### [19] Effects of 6-Hydroxykaempferol: A Potential Natural Product for Amelioration of Tendon Impairment
- Authors: T. Mok, Qiyu He, Xiaoxi Zhang, Tat-Hang Sin, Huajun Wang et al.
- Year: 2022
- Venue: Frontiers in Pharmacology
- URL: https://www.semanticscholar.org/paper/5051cd4b77d748a62d6efb4ca95e7bcac106c654
- DOI: 10.3389/fphar.2022.919104
- PMID: 35935848
- PMCID: 9354238
- Citations: 4
- Summary: 6-hydroxykaempferol, which reportedly promotes the proliferation of microvascular endothelial cells, is a molecule found in SHT and it is found that it promoted the proliferation and migration of tendon fibroblasts and elevated tendon repair-related gene expression.
- Evidence snippets:
  - Snippet 1 (score: 0.683)
    > The GeneCards (RRID:SCR_002773) database was used to search for reported tendinopathy-related genes by entering keywords of tendon injuries, tendon rupture, tendon healing, and tendon adhesion for target-based drug applications. The potential tendon-healing targets of the active components of SHT matched the potential gene targets of the active ingredients of SHT. According to the UniProt database (https://www.uniprot.org/), the full names of the target proteins were transformed into gene symbols based on the UniProt ID (The UniProt Consortium, 2017) (Figure 1). The database leverages the unique rich combinatorial annotations of GeneCards. The GeneCards database provides direct links to generelated research reagents, such as antibodies, recombinant proteins, DNA clones, and inhibitory RNAs, and lists of gene-related drugs and compounds. GeneCards was used to depict the GeneCards Inferred Functionality Score annotation landscape tool for scoring the functional status of genes (Fishilevich et al., 2016).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al. (2018). Ten steps to get started in Genome Assembly and Annotation. F1000Research. https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
3. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
5. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
6. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
7. A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al. (2023). Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea. Frontiers in Microbiology. https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
8. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
9. Jianhua Wang, Ning Jiang, Xiaoyu Sang, N. Yang, Ying Feng et al. (2020). Protein modification characteristics of the malaria parasite Plasmodium falciparum and the infected erythrocytes.. Molecular & cellular proteomics : MCP. https://www.semanticscholar.org/paper/51e4f3979cfebff284dd479acc8890c973f7af52
10. Yoji Nakamura (2018). Prediction of Horizontally and Widely Transferred Genes in Prokaryotes. Evolutionary Bioinformatics Online. https://www.semanticscholar.org/paper/af7bde229b96609907924d1c68ea463af656efb2
11. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
12. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
13. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
14. Yi Zheng, Shan Wu, Yang Bai, Honghe Sun, C. Jiao et al. (2018). Cucurbit Genomics Database (CuGenDB): a central portal for comparative and functional genomics of cucurbit crops. Nucleic Acids Research. https://www.semanticscholar.org/paper/a7bb1e82b8172252d79ee35170dfe038c4b17d78
15. Camila Riccio-Rengifo, J. Finke, Camilo Rocha (2020). Identifying stress responsive genes using overlapping communities in co-expression networks. BMC Bioinformatics. https://www.semanticscholar.org/paper/5410fad9d5b6c743bd156e67c9b7befc16deb5a3
16. Özge Ata, D. Mattanovich (2024). Into the metabolic wild: Unveiling hidden pathways of microbial metabolism. Microbial Biotechnology. https://www.semanticscholar.org/paper/81ac8bfd05a0c52f8a5b6d058c5414b45bb5c1f9
17. S. Subramani, Saranya Jayapalan, R. Kalpana, J. Natarajan (2013). HomoKinase: A Curated Database of Human Protein Kinases. International Scholarly Research Notices. https://www.semanticscholar.org/paper/81a21403fc772c6b9c00915e1124fad2cfb1894b
18. N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt (2024). Prioritising genetic findings for drug target identification and validation.. Atherosclerosis. https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9
19. T. Mok, Qiyu He, Xiaoxi Zhang, Tat-Hang Sin, Huajun Wang et al. (2022). Effects of 6-Hydroxykaempferol: A Potential Natural Product for Amelioration of Tendon Impairment. Frontiers in Pharmacology. https://www.semanticscholar.org/paper/5051cd4b77d748a62d6efb4ca95e7bcac106c654