---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T04:21:38.093009'
end_time: '2026-07-10T04:21:42.326775'
duration_seconds: 4.23
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_5086
  gene_symbol: PP_5086
  uniprot_accession: Q88CU4
  protein_description: 'SubName: Full=Nuclease (SNase domain protein) {ECO:0000313|EMBL:AAN70651.1};
    EC=3.1.-.- {ECO:0000313|EMBL:AAN70651.1};'
  gene_info: OrderedLocusNames=PP_5086 {ECO:0000313|EMBL:AAN70651.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: SNase_OB-fold_sf. (IPR035437); Staphylococal_nuclease_OB-fold.
    (IPR016071); Thermonucl_AS. (IPR002071); SNase (PF00565)
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
- **UniProt Accession:** Q88CU4
- **Protein Description:** SubName: Full=Nuclease (SNase domain protein) {ECO:0000313|EMBL:AAN70651.1}; EC=3.1.-.- {ECO:0000313|EMBL:AAN70651.1};
- **Gene Information:** OrderedLocusNames=PP_5086 {ECO:0000313|EMBL:AAN70651.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** SNase_OB-fold_sf. (IPR035437); Staphylococal_nuclease_OB-fold. (IPR016071); Thermonucl_AS. (IPR002071); SNase (PF00565)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_5086" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_5086' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_5086** (gene ID: PP_5086, UniProt: Q88CU4) in PSEPK.

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
  - Snippet 1 (score: 0.876)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [2] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.808)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

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
  - Snippet 1 (score: 0.805)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.805)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [5] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.787)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [6] The Protein Naming Utility: a rules database for protein nomenclature
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
  - Snippet 1 (score: 0.767)
    > During the annotation phase of a typical modern genomics project, functional names are assigned to identified genes and proteins in an automated or semiautomated fashion. Ideally, before such names are submitted to public sequence databases, they should be manually reviewed by experts to ensure that they are consistent, syntactically correct and unambiguous. However, with the scale of genomic data produced by next-generation sequencing technology and with increasingly automated functional annotation processes, the manual correction of names is no longer feasible. This issue is further complicated by the prevalence of ambiguous names resulting from the lack of interspecies naming conventions (1). New proteins are often named based on homology to existing proteins and many existing proteins have syntactically incorrect or ambiguous names, producing transitive annotation errors. Consequently, poor-quality names have proliferated in both public databases and the scientific literature.
    > The need for consistent and unambiguous names has led to the development of a number of conventions for naming genes and proteins [UniProt protein nomenclature (2), HUGO human gene name nomenclature (3) and various other model organism databases (4)(5)(6)(7)]. In addition, the biological text mining community has created dictionaries to resolve gene/protein synonyms to improve the identification of genes and proteins in scientific articles (1,8).
    > The Broad Institute has developed BioNames, a tool to resolve these difficulties using collections of hard-coded regular expressions (https://sourceforge.net/projects/ microbiomeutil). Here, we present our solution to this problem in the form of the Protein Naming Utility (PNU), a web-based database to store and apply customizable sets of naming rules to correct and standardize gene and protein names within an annotated genome or metagenome. The database provides an intuitive web interface that allows users to create and maintain their own naming rules and organize these rules in projects that can be shared with the community.

### [7] FlyBase: establishing a Gene Group resource for Drosophila melanogaster
- Authors: H. Attrill, K. Falls, J. Goodman, G. Millburn, Giulia Antonazzo et al.
- Year: 2015
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/0d58fdc5f1dfcb2910f7cc003338a82ef827f85c
- DOI: 10.1093/nar/gkv1046
- PMID: 26467478
- PMCID: 4702782
- Citations: 326
- Influential citations: 28
- Summary: FlyBase (flybase.org), the MOD for Drosophila melanogaster, has established a ‘Gene Group’ resource: high-quality sets of genes derived from the published literature and organized into individual report pages, to enable researchers with diverse backgrounds and interests to easily view and analyse acknowledged D. melanogsaster gene sets and compare them with those of other species.
- Evidence snippets:
  - Snippet 1 (score: 0.767)
    > Given the wealth of post-genomic data, it should be straightforward to query a biological database and obtain a robust list of genes related by the shared attributes of their products, such as actins, protein kinases or subunits of the proteasome. However, this is often not the case. For evolutionary-related genes, BLAST (1) or domain-based searches may yield a good preliminary list, but without further analysis, particularly when inferring function from se-quence, it is hard to distinguish false positives. Additionally, there may be false negatives because a gene may be somewhat atypical or fails to score above a given threshold. Gene Ontology (GO) annotations can be used to search for gene products that are related by common biological attributes, but annotation is not exhaustive and expressing features that pertain to sequence does not fall within its scope (2,3).
    > An alternative approach to finding related genes (at least in species with well-characterized genomes such as humans and model organisms) can be to search for gene symbols that share a common prefix. This can be effective for databases such as WormBase (4) or the HUGO Gene Nomenclature Committee (HGNC) (5) that assign unifying and systematic gene symbols to nematode and human genes, respectively, based on shared structures, functions or phenotypes. However, this strategy is not generally applicable to Drosophila melanogaster genes in FlyBase (6) as these are traditionally named on a gene-by-gene basis by the authors who first publish on the gene, often reflecting a specific mutant phenotype.
    > A third method for acquiring a set of related genes is to directly consult relevant research or review articles. The advantage of this approach is that the list is compiled directly from an expert and peer-reviewed source, and as such will be robust and clearly attributable. However, it can be time-consuming to seek out and then extract a set of genes from individual publications (or, often, their supplementary data) and lists obtained in this manner are inherently uncoupled from the relevant species database, meaning that the listed gene symbols/IDs may become stale over time.
    > Several databases have addressed these issues by providing explicit sets of related genes.

### [8] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.767)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [9] Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes
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
  - Snippet 1 (score: 0.761)
    > To inspect the transcriptomics result of individual genes, proteins originating from JGI have a hyperlink to a summary page which links to a 'Genome browser' page that displays the predicted gene splicing, including which regions have RNA support (Figure 1 D).
    > Hence, in the protein specific site in the JGI w e bsite under 'To Genome Browser', the current protein (GeneCatalog) can be seen together with se v eral other alternati v e predictions of the gene splicing, which is essential to have correct, for the protein to function naturally (Figure 2 ).
    > As the RNA coverage supports the exon / intron splicing, it is possible to infer whether a particular gene, in this case Table 1. Comparison between the dbCAN webserver, the eggNOG webserver for both family and functional annotation of CAZymes and the updated CUPP-w e bserver using the recommended significance cut-off at 5. The column 'CAZy -All characterized' encompasses all 10784 characterized proteins in the CAZy database used for the training, whereas the 'CAZy -Newly characterized '   a gene such as the one selected in Figure 2 , is more likely to work after heterologous gene expression.
    > To further improve the enzyme selection, all NCBI Genbank accessions were mapped to Uniprot ID to link to the specific Uniprot accession page including the predicted Al-phaFold structures, Go annotations and InterPro annotations and more ( 19 ).

### [10] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.759)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [11] Functional annotation of parasitic worm genomes, by assigning protein names and GO terms
- Authors: Avril Coghlan, M. Berriman
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
- DOI: 10.1038/protex.2018.055
- Citations: 1
- Summary: A computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and Go terms from orthologues in other species.
- Evidence snippets:
  - Snippet 1 (score: 0.754)
    > Given a set of predicted protein-coding genes for a newly sequenced genome, functional annotation involves assigning putative functions to the predicted genes. Two ways in which this can be done are assigning protein names and Gene Ontology (GO;Gene Ontology Consortium, 2010) terms to the predicted proteins. Here we describe a computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and GO terms from orthologues in other species.
    > When assigning protein names, UniProt protein naming rules (www.uniprot.org/docs/nameprot) are followed where possible. This recommends that a good and stable name for a protein is "as neutral as possible"; that a protein name "should be, as far as possible, unique and attributed to all orthologs"; and a protein name "should not contain a specific characteristic of the protein, and in particular it should not reflect the function or role of the protein, nor its subcellular location, its domain structure, its tissue specificity, its molecular weight or its species of origin".
    > In our protocol, a protein name is assigned to each predicted protein based on curated names in UniProt (Bairoch & Apweiler, 2000) for human, zebrafish, Drosophila melanogaster, Caenorhabditis elegans, and Schistosoma mansoni orthologues identified from a database of gene families (e.g. built using Ensembl Compara; Vilella et al. 2009), or (if no information is found from orthologues) based on InterPro (Hunter et al. 2012) domains. Figure 1 shows an example of using our protein naming pipeline for four Strongyloides ratti genes that belong to the tubulin polyglutamylase family (underlined in pink), where four different protein names were assigned to them (in pink), based on names of their C. elegans or human orthologues.
    > Since each of the S. ratti genes belonged to a different subfamily of the tubulin polyglutamylase family, they were assigned different names.

### [12] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.752)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [13] BioGPS: an extensible and customizable portal for querying and organizing gene annotation resources
- Authors: Chunlei Wu, C. Orozco, J. Boyer, Marc Leglise, James Goodale et al.
- Year: 2009
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/2e9d9f0d6f9f72c76482bcfc2a93abb890fd560f
- DOI: 10.1186/gb-2009-10-11-r130
- PMID: 19919682
- PMCID: 3091323
- Citations: 1446
- Influential citations: 85
- Summary: BioGPS http://biogps.gnf.org is introduced, a centralized gene portal for aggregating distributed gene annotation resources, and embraces the principle of community intelligence, enabling any user to easily and directly contribute to the BioGPS platform.
- Evidence snippets:
  - Snippet 1 (score: 0.751)
    > In the past decade, many technology platforms have been developed that allow researchers to generate data on a genome scale. For example, profiling technologies have been developed for highly parallel measurements of gene expression, copy number, genotype, and epigenetic state. The data derived from these high-throughput approaches can then be used to generate new hypotheses or inferences of gene function. In contrast to experiments focusing on a specific gene or gene family, these genome-scale experiments typically result in the identification of a list of candidate genes that are relatively unfamiliar to any single researcher. Hit lists identified by these methods can often span many protein classes and signaling pathways. In many cases, these genes may also have little or no previous functional characterization.
    > Researchers are then faced with the daunting task of prioritizing these candidate genes for detailed functional and mechanistic studies. Dozens of gene annotation resources and model organism databases serve prominent roles in the genetics and genomics communities. Take, for example, the instance where a researcher has identified hundreds or even thousands of differentially expressed genes between a cancer sample and a matched control. In prioritizing this gene list, many researchers would commonly search Entrez Gene [1] and Ensembl [2] as a first stop for many descriptions of critical gene annotation information, including primary sequence data, genome position, associated Gene Ontology terms, gene structure, and genetic variation. Other researchers may then consult the Mouse Genome Database (MGD) [3] and Rat Genome Database (RGD) [4] for annotation focused on these model organisms, including knockout phenotypes and quantitative trait loci. Molecular and cellular biologists may then visit the STRING database for protein interaction data [5]. Other researchers may query reference Gene Atlas expression data using the SymAtlas web site [6]. In addition, there are a wide variety of gene annotation sites targeting more specific communities, including a database describing the targets of the transcription factor CREB [7], the Allen Brain Atlas showing high-resolution expression information by in situ hybridization in the mouse brain [8], and the TargetScan database for microRNA target prediction [9]. Hundreds of such online resources for mammalian gene annotation currently exist [10,11].

### [14] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.751)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [15] The quality of metabolic pathway resources depends on initial enzymatic function assignments: a case for maize
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
  - Snippet 1 (score: 0.750)
    > A gold standard set of protein functional annotations was generated by extracting data from UniProt [16] and BRENDA [17]. We extracted all protein sequence and annotation data from UniProt (release 2016_05) for the organism Zea mays, keeping the EC annotations only from the manually reviewed component of UniProt, while removing those annotations that had not undergone manual review. We also extracted experimentally verified protein annotations for Zea mays from BRENDA (release 2016.1). The UniProt and BRENDA annotations were then merged by matching proteins based on the database crosslinks provided by BRENDA, resulting in the union of the reviewed annotations from UniProt and the experimentally verified annotations of BRENDA with duplicates removed. The merged protein annotations were then matched to the B73 RefGen_v2 translated gene models using BLASTP based on a sequence identity cutoff of 96% and an e-value cutoff of 1e-20. We selected the top scoring hit for each protein which resulted in matches to 1,815 unique maize proteins. EC annotations for alternate isoforms were consolidated at the gene level, resulting in 1,475 experimentally verified or manually reviewed protein functional annotations across 1,450 maize genes.

### [16] Role of histone-lysine N-methyltransferase 2D (KMT2D) in MEK-ERK signaling-mediated epigenetic regulation: a phosphoproteomics perspective
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
  - Snippet 1 (score: 0.749)
    > Each protein was mapped to its corresponding gene symbol based on the HGNC (downloaded on 30.05.2023) and to its corresponding UniProt (13.04.2023) (UniProt, 2023) accessions using our in-built mapping tool to ensure consistent and standardized annotation. We conducted the analysis using the methodologies outlined in (Sanjeev et al., 2024). The overall workflow used in this study is outlined in Figure 1.

### [17] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.746)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [18] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.745)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [19] Where in the genome are we? A cautionary tale of database use in genomics research
- Authors: L. Vaughan, V. Srinivasasainagendra
- Year: 2013
- Venue: Frontiers in Genetics
- URL: https://www.semanticscholar.org/paper/385827fa8325d3417572365f0ac7777d2e4f8a08
- DOI: 10.3389/fgene.2013.00038
- PMID: 23519237
- PMCID: 3604632
- Citations: 4
- Summary: This manuscript provides selected case studies illustrating issues that may arise while working with genes and genetic polymorphisms, and highlights that resources are constantly evolving, and in order to provide reproducible results research should be aware of and connected to the correct release of the data.
- Evidence snippets:
  - Snippet 1 (score: 0.744)
    > The steps in identifying SNPs from a list of candidate genes can be described as (1) determining the candidate gene pool,
    > (2) annotating, or retrieving information about those genes, (3) determining the location (and boundaries) of those genes, and (4) identifying molecular markers (e.g., single nucleotide polymorphisms, SNPs) within those boundaries. Similar steps are involved in identifying genes that are related to SNPs found to be significant from a GWAS.
    > In a collaborative research setting investigators will often provide a list of gene names that they are interested in to their bioinformatic collaborators who then retrieve information related to these genes for further analysis. The naming of these genes is the first point of ambiguity. Often, these names are common names or synonyms instead of the official names or gene symbols [see HUGO Gene Names Committee HGNC (Seal et al., 2011)]. Due to the structure of most bioinformatic data sources, it can be difficult to correctly identify the gene that an investigator is interested in when the official name is not provided. An example of this is described in Table 1. In this example the original list of TOSO, PIGR, FCAMR, ADRA1A, ADRA1B, and ADRA1D was provided by a collaborator. When searching the UCSC Genome Browser or Entrez Gene databases (accessed July 2011), we see that TOSO is not an HGNC official gene symbol, but is instead a synonym for the gene Fas apoptotic inhibitory molecule 3 (official symbol FAIM3, geneID 9214), and searching earlier versions of UCSC Genome Browser or into the Gene Accession Conversion tool in DAVID, TOSO would not produce any results.
    > The second source of ambiguity, gene annotation, is also illustrated in Table 1. In general, capturing gene level annotations (HGNC id, geneID, synonyms, chromosome, description, etc.), not only provides more information, but also allows investigators to perform quality checks.

### [20] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.742)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
5. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
6. Johannes Goll, R. Montgomery, L. Brinkac, S. Schobel, D. Harkins et al. (2009). The Protein Naming Utility: a rules database for protein nomenclature. Nucleic Acids Research. https://www.semanticscholar.org/paper/dad2c69d04a5a3abdeda129612d52a7849531c09
7. H. Attrill, K. Falls, J. Goodman, G. Millburn, Giulia Antonazzo et al. (2015). FlyBase: establishing a Gene Group resource for Drosophila melanogaster. Nucleic Acids Research. https://www.semanticscholar.org/paper/0d58fdc5f1dfcb2910f7cc003338a82ef827f85c
8. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
9. Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer (2023). Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes. Nucleic Acids Research. https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
10. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
11. Avril Coghlan, M. Berriman (2018). Functional annotation of parasitic worm genomes, by assigning protein names and GO terms. https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
12. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
13. Chunlei Wu, C. Orozco, J. Boyer, Marc Leglise, James Goodale et al. (2009). BioGPS: an extensible and customizable portal for querying and organizing gene annotation resources. Genome Biology. https://www.semanticscholar.org/paper/2e9d9f0d6f9f72c76482bcfc2a93abb890fd560f
14. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
15. Jesse R. Walsh, M. Schaeffer, Peifen Zhang, S. Rhee, J. Dickerson et al. (2016). The quality of metabolic pathway resources depends on initial enzymatic function assignments: a case for maize. BMC Systems Biology. https://www.semanticscholar.org/paper/c41be7766c80fddb3f81c57ced799b8562370cc8
16. Sreeshma Ravindran Kammarambath, Leona Dcunha, Athira Perunelly Gopalakrishnan, Amal Fahma, N. Krishna et al. (2025). Role of histone-lysine N-methyltransferase 2D (KMT2D) in MEK-ERK signaling-mediated epigenetic regulation: a phosphoproteomics perspective. Frontiers in Bioinformatics. https://www.semanticscholar.org/paper/0ac0729148aff3d839e6a15984e11532e9e740f9
17. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
18. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
19. L. Vaughan, V. Srinivasasainagendra (2013). Where in the genome are we? A cautionary tale of database use in genomics research. Frontiers in Genetics. https://www.semanticscholar.org/paper/385827fa8325d3417572365f0ac7777d2e4f8a08
20. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f