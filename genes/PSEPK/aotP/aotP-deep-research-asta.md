---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T16:26:22.675703'
end_time: '2026-07-08T16:27:02.806240'
duration_seconds: 40.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: aotP
  gene_symbol: aotP
  uniprot_accession: Q88R51
  protein_description: 'SubName: Full=Arginine/ornithine transport ATP-binding protein
    AotP {ECO:0000313|EMBL:AAN65914.1};'
  gene_info: Name=aotP {ECO:0000313|EMBL:AAN65914.1}; OrderedLocusNames=PP_0283 {ECO:0000313|EMBL:AAN65914.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ABC transporter superfamily.
  protein_domains: AAA+_ATPase. (IPR003593); ABC_ATPase_HisP-typ. (IPR030679); ABC_transporter-like_ATP-bd.
    (IPR003439); ABC_transporter-like_CS. (IPR017871); MetN_ABC_transporter-like.
    (IPR050086)
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
- **UniProt Accession:** Q88R51
- **Protein Description:** SubName: Full=Arginine/ornithine transport ATP-binding protein AotP {ECO:0000313|EMBL:AAN65914.1};
- **Gene Information:** Name=aotP {ECO:0000313|EMBL:AAN65914.1}; OrderedLocusNames=PP_0283 {ECO:0000313|EMBL:AAN65914.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC transporter superfamily.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_ATPase_HisP-typ. (IPR030679); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); MetN_ABC_transporter-like. (IPR050086)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aotP" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aotP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aotP** (gene ID: aotP, UniProt: Q88R51) in PSEPK.

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
  - Snippet 1 (score: 0.789)
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
  - Snippet 1 (score: 0.788)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.786)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [4] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.770)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [5] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.770)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

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
  - Snippet 1 (score: 0.761)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

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
  - Snippet 1 (score: 0.757)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

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
  - Snippet 1 (score: 0.747)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [9] A MOD(ern) perspective on literature curation
- Authors: J. Hirschman, T. Berardini, H. Drabkin, D. Howe
- Year: 2010
- Venue: Molecular Genetics and Genomics
- URL: https://www.semanticscholar.org/paper/c98b7209b7106364e1a9b75cd45217efc63f6be5
- DOI: 10.1007/s00438-010-0525-8
- PMID: 20221640
- PMCID: 2854346
- Citations: 27
- Influential citations: 2
- Summary: Four curators from different MODs describe the literature curation process and highlight approaches taken by the four MODs to address: (1) the decision process by which papers are selected, and (2) the identification and prioritization of the data contained in the paper.
- Evidence snippets:
  - Snippet 1 (score: 0.734)
    > The first step in curating a paper is the identification of the genes and proteins described as well as the organism to which they belong (Fig. 1). Surprisingly, one of the more difficult challenges a biocurator can face is unambiguously linking the gene or genes discussed in a paper to a record in their MOD, particularly when the gene nomenclature is unclear or the research organism is not identified. Inclusion of sequence or database identifiers for each gene in the paper ensures accurate linking between the results presented in that paper and the particular gene or genes described therein, no matter how the name of a gene may change over time. Papers that lack this information may be impossible to curate. Nomenclature standards and collaborative efforts often strive to give orthologous genes the same symbol and name in multiple species. For example, MGI, under the auspices of the International Committee on Standardized Genetic Nomenclature for Mice (Maltais et al. 2002), and the HUGO Gene Nomenclature Committee (HGNC, Bruford et al. 2008), works to co-ordinate nomenclature between mouse, human and rat genes. ZFIN attempts to name zebrafish genes after their human or mouse orthologs. Likewise, ArkDB (Hu et al. 2001) which maintains data on cat, chicken, cow, horse and sheep, adopts the HGNC nomenclature. Consequently, when a paper mentions a gene or protein symbol that is the same in several organisms (such as BRCA1, which is used in more than a dozen species) and it does not state the specific organism of origin or provide a sequence accession number for this particular gene, it is difficult, if not impossible, to determine whether the data in that paper belongs in a particular species-specific database or not. Another nomenclature conundrum for many model organisms is the case where the same symbol is used for more than one gene in a single species. For example, the symbol PAP1 in Arabidopsis thaliana is the primary symbol or alias for four different genes (PURPLE ACID PHOSPHATASE 1, PHOSPHATIDIC ACID PHOSPHATASE 1, PRODUC-TION OF ANTHOCYANIN PIGMENT 1, and PHY-TOCHROME-ASSOCIATED PROTEIN 1).

### [10] MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis
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
  - Snippet 1 (score: 0.732)
    > Annotation information for each gene in MeiosisOnline contains "basic information, " "function annotation and classification, " "protein-protein interaction (PPI) and gene expression."
    > (1) Basic information: gene name/synonyms, nucleotide sequences, etc., were extracted from GenBank3 and UniProt Knowledgebase.4 (2) Function annotation and classification: detailed functional information is also manually collected from literature reports. (i) Which meiotic stage is the gene involved? (ii) Did the gene function in one sex or both sexes? (iii) Whether deletion or mutation of the gene in model organism has a phenotype in fertility? (iv) Which protein complex of the gene is involved? (v) The cellular location and expression pattern in tissues or cell lines.
    > (vi) Experimental methods used for functional analysis.
    > (vii) The information of related literature and figures for illustrating the function of protein/gene. (viii) Gene ontology annotation for collected genes.
    > (3) Protein-protein interaction and gene expression: both verified and predicted PPI information were provided. Gene expression pattern in reproductive system was also provided graphically.

### [11] Text-mining and information-retrieval services for molecular biology
- Authors: Martin Krallinger, A. Valencia
- Year: 2005
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/558a2745d6e1ac99f77dde88d62566237bd3cfad
- DOI: 10.1186/gb-2005-6-7-224
- PMID: 15998455
- PMCID: 1175978
- Citations: 237
- Influential citations: 1
- Summary: A range of text-mining applications have been developed recently that will improve access to knowledge for biologists and database annotators.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > Biological research is name-centered: proteins are referred to in free text by their names or symbols rather than using the unambiguous identifiers provided by annotation databases (such as SwissProt accession numbers [16]). Identifying mentions of proteins and genes unambiguously within free text is a fundamental step for the later extraction of functional attributes of these entities. Unfortunately this is a difficult process, partly because of the complex nature and usage of gene and protein names. Genes and proteins may be referred to in free text in a range of different ways: as full names (for example, porin), as symbols (the Saccharomyces cerevisiae gene POR1), and also through typographical variants (POR-1). Many genes also have several synonyms (such as OMP2 for POR1), or the gene name may be ambiguous [17] and refer to words that also have a different meanings depending on the context (for example, big brain, the full name for the Drosophila melanogaster gene bib, could also be an anatomical description). Furthermore, it has been suggested that errors in gene names might be introduced automatically by certain applications in bioinformatics [18].
    > In the NLP field, the identification of entities in free text is known as named-entity recognition (NER). To identify biological entities such as genes, proteins and drugs automatically and unambiguously within free text, over 50 information-extraction and text-mining tools have recently been implemented, and two community-wide evaluations have been carried out [19,20]. The top left of Figure 1 shows nine existing NER applications for biology that are provided via an online server or are directly downloadable. Note that the average recovery of biological entities from free text by 15 NER tools was 80%, and the results had an accuracy of 80% [21]; these figures are significantly lower than in the case of entities found in documents from fields such as economics, which demonstrates the complex nature of protein names.
    > Proteins and genes are characterized within biological databases through unique identifiers; each identifier is associated with its corresponding protein or nucleotide sequence and functional descriptions.

### [12] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2772
- Influential citations: 298
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.724)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

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
  - Snippet 1 (score: 0.722)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [14] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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

### [15] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [16] Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser
- Authors: Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała
- Year: 2025
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
- DOI: 10.1186/s12864-025-12329-8
- PMID: 41408139
- PMCID: 12822150
- Citations: 2
- Summary: An R script is developed that performs a gene symbol update to current official versions combined with identification of ambiguous symbols and retrieval of other IDs from the Ensembl database and provides a single list of updated symbols with annotation about their ambiguity.
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > Gene nomenclature contains current official symbols and various numbers of synonyms, which pose a challenge to integrating genomic data and increase the probability that different genes share the same symbol. Therefore, we retrieved identifiers assigned to all protein-coding genes in human, mouse, rat and pig genomes that are available in the Ensembl genome browser (release 113) to assess the number of genes, compare species and identify ambiguous symbols. Results: Our analysis revealed that the total number of symbols, both official symbols and synonyms, used to identify protein-coding genes ranges from 16,600 in pigs to 64,580 in mice. Furthermore, the gene nomenclature is not complete because there are also genes without an assigned symbol, which indicates gaps in understanding protein-coding genes, especially in pigs. We also found a large number of gene symbols that map to more than one gene. These symbols might complicate the identification of about 10% of rat and mouse genes and 18% of human protein-coding genes. A simple solution for this problem is the usage of stable gene IDs assigned by scientific institutions and committees (Ensembl, NCBI, RGD, HGNC and VGNC) provided that the genomic information associated with these IDs is retrieved directly from proprietary databases containing the most accurate data. Finally, although gene symbols may pose a problem with unequivocal identification of genes, there are instances when no other identifiers are available in the literature. Therefore, we have developed an R script performing search of the Ensembl database and integrating data to provide a single list of updated symbols with annotation about their ambiguity. Conclusions: Gene symbols are not always reliable and should be reported together with stable IDs to enable unequivocal identification of genes. Therefore, data containing only gene symbols should be used cautiously to avoid misidentification of genes. A solution for this problem is our R script REgeness that performs a gene symbol update to current official versions combined with identification of ambiguous symbols and retrieval of other IDs from the Ensembl database.

### [17] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.711)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [18] CharProtDB: a database of experimentally characterized protein annotations
- Authors: R. Madupu, Alexander R. Richter, R. Dodson, L. Brinkac, D. Harkins et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/998f9623b739aaf1099dd2de48b1d86bff6cba78
- DOI: 10.1093/nar/gkr1133
- PMID: 22140108
- PMCID: 3245046
- Citations: 27
- Influential citations: 1
- Summary: The CharProtDB has been expanded by import of selected records from publicly available protein collections whose biocuration indicated direct rather than homology-based assignment of function.
- Evidence snippets:
  - Snippet 1 (score: 0.711)
    > The central unit of CharProtDB is the protein record. Each protein record in CharProtDB (Figure 1) must have an assigned organism (by taxon ID), and at least one public accession, protein name and GO annotation complete with an experimental evidence code and an associated reference. The protein may also have one or more gene symbols assigned. Additional synonymous accessions are added to proteins, either automatically as the proteins are entered, or manually by curators. These synonymous accessions, in the context of CharProtDB, are limited to public accessions with both identical sequence and taxon ID.
    > Annotating using the GO system is of importance for several reasons; the GO system captures defined concepts (the GO terms) with unique ids, which can be attached to specific genes and the three controlled vocabularies of the GO allow for the capture of much more annotation information than is traditionally captured in protein common names, including, for example, not just the function of the protein, but its location as well. GO evidence codes implemented in CHAR directly correlate with the GO consortium definitions of experimental evidence codes (6).
    > Beyond GO annotations, the protein may be assigned one or more controlled vocabulary terms for enzyme functional classification, as Enzyme Commission (EC) numbers (http://www.chem.qmul.ac.uk/iubmb/) (7), or transporter functional classification, as Transport Classification (TC) numbers (8). Except for GO assignments, which must have a reference, any or all of these annotations may be linked to a reference. If a record was imported from an external database, the annotations coming from that database will be referenced back to the original source. Any additional references found, including those not directly linked to an annotation, will be attached to the applicable protein(s).
    > For leveraging CharProtDB in automated annotation, one protein name, one gene symbol and one or more GO terms, EC or TC annotations are marked as 'primary'. This represents the preferred choice for assignment to a predicted gene being automatically annotated. Apart from the primary annotation, CharProtDB also stores alternate protein names or synonyms and alternate gene symbol.

### [19] Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining
- Authors: Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al.
- Year: 2024
- Venue: Research Square
- URL: https://www.semanticscholar.org/paper/795b2985fdc3cf1cfbd5fda1b3c0502eb4dfe866
- DOI: 10.21203/rs.3.rs-5412515/v1
- PMID: 39649165
- PMCID: 11623766
- Citations: 3
- Summary: This study systematically assessed the Plasmodium falciparum genome for proteins amenable to target-based drug discovery, identifying 867 candidate targets with evidence of small molecule binding and blood stage essentiality and implements a generalizable framework for systematically evaluating and prioritizing novel pathogenic disease targets.
- Evidence snippets:
  - Snippet 1 (score: 0.711)
    > List of genes and genomic features (GFF) for Plasmodium falciparum 3D7 genome (PlasmoDB release 66) was downloaded and protein coding genes were extracted along with their gene annotations and genomic location. Additional genomic annotations were obtained by querying PlasmoDB to extract UniProt and Entrez ID(s), ortholog group (OrthoMCL), protein features (CDS and protein length, molecular weight, isoelectric point), domain annotations (InterPro, PFam, Superfamily), number of transmembrane (TM) domains, and enzyme commission (EC) numbers. Gene function (Gene Ontology; components, functions and processes) was extracted by either PlasmoDB or by querying the InterPro ID under InterPro2GO mapping tool from EMBL-EBI services. Gene essentiality data was obtained for P.
    > falciparum 29 and P. berghei 30,31 parasites that were mapped to their falciparum ortholog using OrthoMCL orthology group IDs. Protein Data Bank (PDB) IDs of crystal structures were obtained by searching either gene symbols, UniProt IDs associated with each gene, or by typing "Plasmodium" in the PDB website search box. A report with gene identi er, organism, accession number, method for structure determination and publication information was extracted for the search hits.
    > Mapping genes to associated literature publications A download from the NCBI FTP site was performed for gene2pubmed.gz (version 2024-02-21) containing taxonomy ID, gene ID (Entrez) and PubMed ID. Gene IDs were mapped to the P. falciparum 3D7 annotation set, and PMIDs matching the criteria were extracted. To include literature references associated with gene symbols, we queried each gene symbol in PubMed using the Eutils 81 efetch function from NCBI; additional information for each publication was obtained pragmatically using the same tool, retrieving title, authors and DOI (digital object identi er).

### [20] GeneSet2miRNA: finding the signature of cooperative miRNA activities in the gene lists
- Authors: A. Antonov, S. Dietmann, Philip Wong, D. Lutter, H. Mewes
- Year: 2009
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/90ebadc70236638e9499c1200097725327469ea3
- DOI: 10.1093/nar/gkp313
- PMID: 19420064
- PMCID: 2703952
- Citations: 52
- Influential citations: 5
- Summary: GeneSet2miRNA is the first web-based tool which is able to identify whether or not a gene list has a signature of miRNA-regulatory activity.
- Evidence snippets:
  - Snippet 1 (score: 0.708)
    > As input GeneSet2miRNA accepts several types of gene or protein identifiers. For example, for the human genome GeneSet2miRNA supports identifiers from 'Entrez Gene' (24), 'UniProt/Swiss-Prot', 'Gene Symbol' (24,25), 'UniGene' (24), 'Ensembl' (26), 'RefSeq Protein ID', 'RefSeq Transcript ID' ( 27) and 'Affymetrix probe codes' (28). Additionally a mixture of several identifier types is possible. In the first step user supplied gene Ids are mapped to 'Entrez Gene' identifiers. For this purpose files from NCBI and Affymetrix web sites are used. Detailed information on data sources used by GeneSet2miRNA is in Table 1.
    > The user gets full information on the mapping of the supplied gene ids. We would like to point out that protein and gene identifiers can be highly ambiguous (29) with multiple synonymous variants. For this reason the quality of the retrieved annotation can be different for different types of identifiers. To escape multiple mapping issues we recommend submitting 'Entrez Gene' identifies to GeneSet2miRNA.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
5. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
6. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
7. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
8. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
9. J. Hirschman, T. Berardini, H. Drabkin, D. Howe (2010). A MOD(ern) perspective on literature curation. Molecular Genetics and Genomics. https://www.semanticscholar.org/paper/c98b7209b7106364e1a9b75cd45217efc63f6be5
10. Xiaohua Jiang, Daren Zhao, Asim Ali, Bo Xu, Wei Liu et al. (2021). MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis. Frontiers in Cell and Developmental Biology. https://www.semanticscholar.org/paper/aeb08368a5540685473578345739bb569103bd46
11. Martin Krallinger, A. Valencia (2005). Text-mining and information-retrieval services for molecular biology. Genome Biology. https://www.semanticscholar.org/paper/558a2745d6e1ac99f77dde88d62566237bd3cfad
12. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
13. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
14. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
15. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
16. Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała (2025). Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser. BMC Genomics. https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
17. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
18. R. Madupu, Alexander R. Richter, R. Dodson, L. Brinkac, D. Harkins et al. (2011). CharProtDB: a database of experimentally characterized protein annotations. Nucleic Acids Research. https://www.semanticscholar.org/paper/998f9623b739aaf1099dd2de48b1d86bff6cba78
19. Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al. (2024). Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining. Research Square. https://www.semanticscholar.org/paper/795b2985fdc3cf1cfbd5fda1b3c0502eb4dfe866
20. A. Antonov, S. Dietmann, Philip Wong, D. Lutter, H. Mewes (2009). GeneSet2miRNA: finding the signature of cooperative miRNA activities in the gene lists. Nucleic Acids Research. https://www.semanticscholar.org/paper/90ebadc70236638e9499c1200097725327469ea3