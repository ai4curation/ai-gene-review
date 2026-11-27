---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-11-26T19:03:02.009125'
end_time: '2026-11-26T19:03:07.454609'
duration_seconds: 5.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: LDHD
  gene_symbol: LDHD
  uniprot_accession: Q86WU2
  protein_description: 'RecName: Full=D-lactate dehydrogenase, mitochondrial {ECO:0000305|PubMed:38373542};
    Short=DLD; Short=Lactate dehydrogenase D; EC=1.1.98.- {ECO:0000269|PubMed:38373542};
    Flags: Precursor;'
  gene_info: Name=LDHD {ECO:0000312|HGNC:HGNC:19708};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the FAD-binding oxidoreductase/transferase type
  protein_domains: FAD-bd_oxidored_4_C. (IPR004113); FAD-bd_PCMH. (IPR016166); FAD-bd_PCMH-like_sf.
    (IPR036318); FAD-bd_PCMH_sub1. (IPR016167); FAD-bd_PCMH_sub2. (IPR016169)
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
- **UniProt Accession:** Q86WU2
- **Protein Description:** RecName: Full=D-lactate dehydrogenase, mitochondrial {ECO:0000305|PubMed:38373542}; Short=DLD; Short=Lactate dehydrogenase D; EC=1.1.98.- {ECO:0000269|PubMed:38373542}; Flags: Precursor;
- **Gene Information:** Name=LDHD {ECO:0000312|HGNC:HGNC:19708};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the FAD-binding oxidoreductase/transferase type
- **Key Domains:** FAD-bd_oxidored_4_C. (IPR004113); FAD-bd_PCMH. (IPR016166); FAD-bd_PCMH-like_sf. (IPR036318); FAD-bd_PCMH_sub1. (IPR016167); FAD-bd_PCMH_sub2. (IPR016169)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LDHD" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LDHD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LDHD** (gene ID: LDHD, UniProt: Q86WU2) in human.

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

### [1] Acid tolerance of lactate-utilizing bacteria of the order Bacteroidales contributes to prevention of ruminal acidosis in goats adapted to a high-concentrate diet
- Authors: Zhongyan Lu, Lingmeng Kong, Shenhao Ren, J. Aschenbach, Hong Shen
- Year: 2023
- Venue: Animal Nutrition
- URL: https://www.semanticscholar.org/paper/b9b3a1ffa5d51c9225e5043f74473d80e3a94d8d
- DOI: 10.1016/j.aninu.2023.05.006
- PMID: 37397354
- PMCID: 10314236
- Citations: 9
- Summary: The rapid accumulation of organic acids, particularly lactate, has been suggested as the main cause of ruminal acidosis (RA) for ruminants fed high-concentrate diets. Previous research has shown that a gradual shift from low-to high-concentrate diets within 4 to 5 weeks effectively reduces the risk for RA. However, the mechanisms remain unknown. In this study, 20 goats were randomly allocated into four groups (n = 5) and fed with a diet containing a weekly increasing concentrate portion of 20...
- Evidence snippets:
  - Snippet 1 (score: 0.775)
    > Genes encoding nLDH, including NAD-depended L-lactate dehydrogenase gene (ldh, K00016) and NAD-depended D-lactate dehydrogenase gene (ldhA, K03778), and genes encoding iLDH, including cytochrome-dependent L-lactate dehydrogenase gene (lldD, K00101), quinone-dependent L-lactate dehydrogenase complex proteins genes (lldE, K18928; lldF, K18929; lldG, K00782), FADdependent D-lactate dehydrogenase gene (dldII, K18930), quinonedependent D-lactate dehydrogenase gene (dld, K03777), and cytochrome-dependent L-lactate dehydrogenase gene (dldH, K00102), were searched for within the metagenome data. Finally, ldh, ldhA, lldEFG and dldII were detected (GA > 0.1 in at least one group) in the data.
    > Available gene sequences of the above four types of LDH were downloaded from UniProt databases and subsequently aligned with corresponding gene sequences detected in this study by using MAFFT v7.486 (Katoh and Standley, 2013). Maximum likelihood trees of each investigated LDH were constructed by means of the GTR model in PhyML v3.0 (Guindon et al., 2010). Taxonomy classifications of these genes were retrieved according to the Kaiju annotation results of co-assembled contigs with these genes.

### [2] LMPD: LIPID MAPS proteome database
- Authors: Dawn Cotter, Andreia Maer, C. Guda, Brian Saunders, S. Subramaniam
- Year: 2005
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
- DOI: 10.1093/nar/gkj122
- PMID: 16381922
- PMCID: 1347484
- Citations: 94
- Influential citations: 2
- Summary: The initial release of the LIPID MAPS Proteome Database contains 2959 records, representing human and mouse proteins involved in lipid metabolism, and this LMPD protein list was enhanced with annotations from UniProt, EntrezGene, ENZYME, GO, KEGG and other public resources.
- Evidence snippets:
  - Snippet 1 (score: 0.749)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [3] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
- Authors: Ralf C. Mueller, Nicolai Mallig, J. Smith, Lél Eöery, R. Kuo et al.
- Year: 2020
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
- DOI: 10.1186/s12859-020-03764-3
- PMID: 33176685
- PMCID: 7661159
- Citations: 7
- Summary: The Avian Immunome DB (Avimm) for easy gene property extraction as exemplified by avian immune genes is presented and described, which contains 1170 distinct avian immune genes with canonical gene symbols and 612 synonyms across 363 bird species.
- Evidence snippets:
  - Snippet 1 (score: 0.723)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
- Authors: P. Hornbeck, J. Kornhauser, Sasha L. Tkachev, Bin Zhang, E. Skrzypek et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
- DOI: 10.1093/nar/gkr1122
- PMID: 22135298
- PMCID: 3245126
- Citations: 1660
- Influential citations: 161
- Summary: PhosphoSitePlus (http://www.phosphosite.org) is an open, comprehensive, manually curated and interactive resource for studying experimentally observed post-translational modifications, primarily of human and mouse proteins. It encompasses 1 30 000 non-redundant modification sites, primarily phosphorylation, ubiquitinylation and acetylation. The interface is designed for clarity and ease of navigation. From the home page, users can launch simple or complex searches and browse high-throughput d...
- Evidence snippets:
  - Snippet 1 (score: 0.706)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [5] CRONOS: the cross-reference navigation server
- Authors: B. Waegele, I. Dunger-Kaltenbach, G. Fobo, Corinna Montrone, H. Mewes et al.
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

### [6] Antibodies to biotin enable large-scale detection of biotinylation sites on proteins
- Authors: N. Udeshi, Kayvon Pedram, Tanya Svinkina, Shaunt Fereshetian, S. Myers et al.
- Year: 2017
- Venue: Nature methods
- URL: https://www.semanticscholar.org/paper/f9e4f461ca61f4399a95875ea96fb075fa959901
- DOI: 10.1038/nmeth.4465
- PMID: 29039416
- PMCID: 8954634
- Citations: 130
- Influential citations: 3
- Summary: It is shown that anti-biotin antibodies enable unprecedented enrichment of biotinylated peptides from complex peptide mixtures.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > All human IDs used for data annotation were downloaded from Uniprot 20 FTP (URL: ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledge-base/ idmapping/by_organism/, Version: 10/03/2016). The resulting data provided 133,996 unique identifications, which were in turn used to query the Uniprot database. This search returned HHMI Author Manuscript HHMI Author Manuscript HHMI Author Manuscript 109,961 records (including reviewed and unreviewed) along with their functional and structural annotations, including gene ontology features. The annotation table was used to search for mitochondrial evidence associated with a given Uniprot identification in our proximity-labeling anti-biotin-enriched data set by using a string match algorithm. A given protein was annotated as having mitochondrial evidence if any of the following were true: (i) the string 'mitoch' matched the above UniProt annotation table when queried by either gene name or accession number. (ii) The protein showed mitochondrial evidence from a list of mitochondrial proteins which was the same as our previous study (Rhee et al. 11 ) and a precursor to MitoCarta2.0 catalog 28 . (iii) The protein was present in the original mitochondrial true positive list used Rhee et al. 11 . Thebiotinylated peptide data were filtered such that reverse hits, nonhuman contaminants, nonfully localized biotinylation sites, sites identified in the SILAC light state, and redundant biotin site entries were removed. From this list, transmembrane proteins were annotated using the following criteria: (i) the UniProt transmembrane annotation contains the string "TRANSMEM" when matched by either gene name or accession number and/or (ii) evidence from of transmembrane domains after running the precursor MitoCarta2.0 catalog through TMHMM 29 . The UniProt topological domain annotation contained the string "TOPO" when matched by either gene name or accession number.

### [7] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
- Authors: L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Si-Qian He, Sunghwan Kim et al.
- Year: 2021
- Venue: Frontiers in Research Metrics and Analytics
- URL: https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
- DOI: 10.3389/frma.2021.689059
- PMID: 34322655
- PMCID: 8311438
- Citations: 25
- Summary: The literature knowledge panels developed and implemented in PubChem help to uncover and summarize important relationships between chemicals, genes, proteins, and diseases by analyzing co-occurrences of terms in biomedical literature abstracts.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [8] Telomere-to-telomere assembly and haplotype analysis of tetraploid Dendrobium officinale illuminate Orchidaceae polyploid evolution and mycorrhizal symbiosis genes
- Authors: Enlian Chen, Jialu Xu, Yuan-Sheng Liu, Yong-Liang Li, Yiping Feng et al.
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/b1df798188e8a8909532f07343a1c167e46291b8
- DOI: 10.64898/2026.03.04.709700
- Summary: The telomere-to-telomere (T2T) genome assembly for D. officinale is reported, representing the first T2T reference genome within the Orchidaceae family, and a systematic analysis of the SWEET gene family across the genus Dendrobium revealed that the gene family size is shaped primarily by epiphytic types and environmental factors.
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > Protein sequences with less than 90% identity were filtered out. The remaining aligned sequences were used for transcript and coding region prediction with miniprot v0.12(68).
    > For de novo prediction, Augustus v3.5(69), Helixer v0.3.4(70), and GeneMark v4.7.1(71) were used to annotate genes based on the repeat-masked D. officinale genome. Augustus was trained using models generated from BUSCO results, Helixer performed cross-species gene prediction using deep learning, and GeneMark employed an unsupervised algorithm that does not require a training set.
    > The results from transcriptome-based, homology-based, and de novo prediction were integrated using EVM v2.1.0. Subsequently, PASA v2.5.3 (72) was utilized to refine the gene models by incorporating transcriptome evidence, correcting exon-intron boundaries, adding UTRs, and modeling alternative splicing events, followed by the removal of extremely short genes and those containing premature stop codons to improve annotation quality. The final gene set was evaluated using BUSCO to assess completeness.
    > Gene function annotation is the process of predicting the function of target proteins by aligning their sequences with known functional protein sequences in databases. The methods for gene function annotation can be divided into two main approaches: the first is based on sequence homology, where the protein sequences of D. officinale are aligned with the UniProt, Nr, GO, and KEGG databases using BLASTP to obtain related functional information and potential involvement in metabolic pathways; The second is based on domain similarity, where the protein sequences of D. officinale were analyzed using InterProScan v5.51 (73) to identify conserved domains, assign protein families, and predict functional site.
    > Non-coding RNAs annotation Non-coding RNAs are RNA molecules that do not encode proteins, including rRNA, tRNA, snRNA, snoRNA, and miRNA, among others. These RNAs perform their biological functions directly after transcription, without the need for translation into proteins.

### [9] MitoFates: Improved Prediction of Mitochondrial Targeting Sequences and Their Cleavage Sites
- Authors: Y. Fukasawa, J. Tsuji, Szu-Chin Fu, K. Tomii, P. Horton et al.
- Year: 2015
- Venue: Molecular & Cellular Proteomics : MCP
- URL: https://www.semanticscholar.org/paper/9d6a56f3096a15e53bb433a4cfd9ad7109211639
- DOI: 10.1074/mcp.M114.043083
- PMID: 25670805
- PMCID: 4390256
- Citations: 539
- Influential citations: 76
- Summary: MitoFates is described, an improved prediction method for cleavable N-terminal mitochondrial targeting signals (presequences) and their cleavage sites and it is used to look for undiscovered mitochondrial proteins from 42,217 human proteins.
- Evidence snippets:
  - Snippet 1 (score: 0.675)
    > In MitoCarta, the most comprehensive animal mitochondria proteomics study to date, Pagliarini et al. (3) identified 1098 mouse mitochondrial proteins with an estimated false positive rate of 10%. Thus, hundreds of mitochondrial proteins may remain undiscovered. Under its default threshold (0.385 corresponding to an estimated 79% precision and 80% recall), MitoFates predicts 1847 human proteins (from 1167 genes) to contain mitochondrial targeting presequences (supplemental Table S5), including 580 predicted presequence genes (851 proteins) without annotation as mitochondrial proteins in either UniProt or Gene Ontology (supplemental Table S6). We hope that this list of predicted mitochondrial presequence proteins (including isoforms) will be a useful resource for prioritizing experimental investigation of novel candidates.
    > Candidate Mitochondrial Proteins with Differentially Localized Isoforms-In humans and many other eukaryotic organisms, most protein genes produce multiple isoforms via mechanisms such as alternative splicing and alternative translation initiation. Many cases are known in which isoforms of the same gene exhibit differential subcellular localization. For example, aldehyde dehydrogenase 7A1 (ALDH7A1), which plays an important role in protecting cells and tissues from hyperosmotic stress, has both mitochondrial and nonmitochondrial isoforms that are differentially expressed in a tissuespecific manner. Mitochondrial ALDH7A1 is thought to utilize an alternate upstream start codon, resulting in the addition of a presequence (58). Several genes like ALDH7A1, possessing both mitochondrial and nonmitochondrial targeted isoforms have been identified, but a comprehensive list of such proteins is not available. Thus, we applied MitoFates to search for candidate differentially localized isoforms, obtaining 517 candidate genes (supplemental Table S7), a sizable (44%) percentage of predicted mitochondrial genes. In about 90% of these candidates, the maximum score difference between isoforms is larger than 0.4, reflecting major changes in the N-termini of those sequences (supplemental Fig. S7).

### [10] Genomic Analysis of Rhodococcus sp. Br-6, a Bromate Reducing Bacterium Isolated From Soil in Chiba, Japan
- Authors: Kohei Ito, Masafumi Harada, N. Nakajima, Shigeki Yamamura, M. Tomita et al.
- Year: 2018
- Venue: Journal of Genomics
- URL: https://www.semanticscholar.org/paper/5a46aff9e42e4f79784e2e878938ba507b8bdf2b
- DOI: 10.7150/jgen.27741
- PMID: 30510597
- PMCID: 6275400
- Summary: The draft genome sequence of Rhodococcus sp.
- Evidence snippets:
  - Snippet 1 (score: 0.670)
    > As expected by the fact that Rhodococcus is non-motile, the Br-6 genome did not contain any genes involved in motility. Tamai et al. (2016) suggested that diaphorase is involved in bromate reduction by strain Br-6, and that strain Br-6 has multiple isoforms of diaphorase [3]. Some dihydrolipoyl dehydrogenase (DLD) enzymes have NADH-dependent diaphorase activity [19]. The Br-6 genome contains the lpdC gene, which encodes DLD (locus_tag: Br6_03586; UniProt: E4W8R5). The DLD protein sequence was used as a query in a BLASTP search (E-value < 1e-5) against all the strain Br-6 predicted protein sequences to identify DLD homologues. The lpdC protein has low percentage identity (ranging from 25% to 31%) with all 10 reductase encoding homologs (Table 2), including the lpdA gene, annotated as "NAD(P)H dehydrogenase" (locus_tag: Br6_00169) or "flavoprotein disulfide reductase" (UniProt: E9T344), and the merA gene, annotated as "mercuric reductase" (Br6_01549) or "putative dihydrolipoyl dehydrogenase" (UniProt: E4WE66). The lpdC, lpdA, and merA genes were also annotated as "dihydrolipoamide dehydrogenase [EC:1.8.1.4]" (KEGG: K00382). These results suggest that these homologous genes encode multiple diaphorase isoforms. The genes identified here could be effective targets for future experimental studies.

### [11] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
- Authors: Mary Kate Bonner, Daniel S. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al.
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
  - Snippet 1 (score: 0.670)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [12] Possible Novel Sulfolipid Utilization Pathway in Giant Clams and Other Aquatic Invertebrates: Implications for Photosymbiosis and Sulfur Cycling
- Authors: Taiga Uchida, H. Yamashita, Go Shimada, E. Shoguchi, C. Shinzato
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/fc2752dcc39243be40916b466681cc4f02dc7927
- DOI: 10.64898/2026.02.11.705467
- Summary: Results suggest that in aquatic invertebrates, SQase functions as a digestive enzyme for algal-derived sulfolipids and that photosymbiotic bivalves have expanded its deployment to tissues specialized for symbiosis.
- Evidence snippets:
  - Snippet 1 (score: 0.667)
    > In the search of gene models, several sequences showed similarity to Pseudomonas putida sulfoquinovose 1-dehydrogenase (UniProt accession: P0DOV5). However, all of these sequences were annotated as dehydrogenases/reductases, distinct from sulfoquinovose 1dehydrogenase, based on SwissProt BLAST annotations (Table S3). In the search against the genome sequence, all significant hits corresponded to protein-coding regions. With the exception of one gene annotated as an ADP-ribosylation factor, all other hits were annotated as dehydrogenases/reductases distinct from sulfoquinovose 1-dehydrogenase, based on SwissProt BLAST annotations (Table S4).

### [13] An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models
- Authors: Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al.
- Year: 2026
- Venue: Nature Communications
- URL: https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
- DOI: 10.1038/s41467-026-75972-z
- PMID: 42669697
- PMCID: 13526818
- Citations: 1
- Summary: An embedding-based statistical framework is developed that transforms gene and function descriptions into vector representations, enabling statistical testing of gene-gene and gene-function relationships and quantitative prioritization of de novo functional hypotheses inferred by LLMs.
- Evidence snippets:
  - Snippet 1 (score: 0.664)
    > This study focused on human protein-coding genes because they represent the most well-annotated portion of the genome, with reliable functional summaries, and are typically the primary focus of functional annotation analyses. We obtained functional summaries of individual genes from three widely used databases: (1) NCBI Gene 32 , which curates descriptions from multiple sources such as RefSeq under the "Summary" field, (2) Alliance of Genome Resources 33 , where descriptions are generated from structured gene data such as ontology terms and ortholog sets under the "Automated Description" field, and (3) UniProt 34 , which focuses on protein-level functions under the "Function" field. The NCBI database was accessed using its API, Entrez Programming Utilities (E-utilities), while descriptions from Alliance of Genome Resources and UniProt were directly downloaded from their respective databases. The number of genes retrieved from each database was 18,753 from NCBI, 18,600 from Alliance of Genome Resources, and 16,343 from UniProt, with 16,329 genes shared across all three databases. We preprocessed the gene descriptions to remove irrelevant information, such as source attribution found in NCBI descriptions (e.g., "[provided by RefSeq, Jul 2008]"). After preprocessing, each gene name was combined with its corresponding functional summary and input into the embedding models to generate gene embeddings.
    > We also generated de novo gene descriptions using an RAG approach. For each gene, we first retrieved the 100 most relevant sentences from PubMed and PubMed Central via the LitSense 35 API using biological context-specific queries: "function of 'gene symbol'", "'gene symbol' pathway association", "'gene symbol' transcriptional response", "'gene symbol' disease association". The numbers of genes under each biological context were 18,723, 18,723, 18,288, and 18,548, respectively. To restrict the temporal scope of knowledge and ensure controlled evaluation, we filtered the retrieved sentences to retain only those from publications published in or before October 2023, consistent with the versions of curated gene databases used in this study.

### [14] Gene and protein nomenclature in public databases
- Authors: Katrin Fundel, Ralf Zimmer
- Year: 2006
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/75e725b9aa79f1b6943b32164778e5b52f715852
- DOI: 10.1186/1471-2105-7-372
- PMID: 16899134
- PMCID: 1560172
- Citations: 59
- Influential citations: 2
- Summary: The combination of data contained in different databases allows the generation of gene and protein name dictionaries that contain significantly more used names than dictionaries obtained from individual data sources, and curation of combined dictionaries considerably increases size and decreases ambiguity.
- Evidence snippets:
  - Snippet 1 (score: 0.659)
    > The results presented above clearly indicate that, when aiming at construction of a broad coverage gene name dictionary, it is important to combine information from different data sources. Such a gene name dictionary is relevant for several scenarios: (1) The researcher, who is starting to work on a gene/protein so far unknown to him should consider several databases for obtaining information. Especially, he should use all available gene names when doing literature search. Otherwise he risks missing information on the gene/protein, e.g. previously published results on certain experiments, which may lead him to inappropriate planning of studies.
    > (2) Automated approaches like systems for information retrieval or information extraction that focus on genes and/or proteins benefit from comprehensive and specific input data. A gene name dictionary allows to create specific queries, integrate information on individual genes/proteins, and also to directly link information from several information sources (database mapping).
    > (3) Approaches for named entity recognition and identification frequently apply gene name dictionaries. Depending on the recognition methodology, they depend more or less on the dictionary, but generally they produce better results with better dictionaries. Our results in BioCreAtIvE have shown a significant influence of the dictionary on recall and precision of gene name identification when applying a simple exact text matching approach [8], but also a significant influence when applying a more involved search strategy [9].
    > This study shows that the ambiguity within gene names and also between gene names and common English words and domain-related terms is significant. The degree of ambiguity varies between different organisms. Some of the aspects that we analyzed here have been previously analyzed in a slightly different way (e.g. different thesaurus of common English words, different data sources for the generation of gene name dictionary) [29,30]. The results are similar and thus show a good agreement of the studies. The ambiguity is in part due to the rules of gene and protein nomenclature for the corresponding model organisms. It is evident that a descriptive and free nomenclature as it is used for Drosophila makes automated identification of gene names very difficult, while a stringent nomenclature as it is used for yeast allows for easy means of gene name identification.

### [15] WormBase 2024: status and transitioning to Alliance infrastructure
- Authors: P. Sternberg, K. V. Van Auken, Qing-Hua Wang, Adam J. Wright, K. Yook et al.
- Year: 2024
- Venue: Genetics
- URL: https://www.semanticscholar.org/paper/dcfce02a58655b0872a8265f5c85dbbd94957294
- DOI: 10.1093/genetics/iyae050
- PMID: 38573366
- PMCID: 11075546
- Citations: 227
- Influential citations: 12
- Summary: The current state of WormBase as well as progress and plans for moving core WormBase infrastructure to the Alliance of Genome Resources (the Alliance) are discussed.
- Evidence snippets:
  - Snippet 1 (score: 0.658)
    > Of the 19,984 protein-coding genes in C. elegans, 10,838 have a name/gene symbol (e.g. lin-12). Gene naming is largely investigator-initiated, with a request to WormBase through genenames@wormbase.org ; this will continue with C. elegans content in the Alliance. The gene symbol, which is formatted in lowercase and italics, communicates information about the gene based on mutant phenotype, functional criteria, orthology, or homology. To make genes easily recognizable to non-elegans researchers, the current preference is to name genes with human orthologs after the human gene if characterized. Gene name stability and formatting are important to avoid confusion in the literature and to facilitate searches of other databases that use the C. elegans gene symbols (e.g. UniProt) and text mining. However, occasionally names have been changed because of incorrect orthology or not supported by functional studies from the community. Names have also been changed based on requests from multiple community members (e.g. daf-21 renamed as hsp-90). To avoid name changes and to have the published name used in databases, researchers should contact WormBase prior to manuscript submission; the most common issue is that the requested name is already in use in C. elegans or another model organism for a nonhomologous gene product. Over the past 10 years, the community has averaged 180 new gene names per year, often with a corresponding publication, increasing knowledge about our favorite organism. More information about C. elegans-specific nomenclature can be found at https://wormbase.org/about/ userguide/nomenclature.

### [16] Identifying orthologs with OMA: A primer
- Authors: Monique Zahn-Zabal, C. Dessimoz, N. Glover
- Year: 2020
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
- DOI: 10.12688/f1000research.21508.1
- PMID: 32089838
- PMCID: 7014581
- Citations: 41
- Summary: This Primer is organized in two parts and provides all the necessary background information to understand the concepts of orthology, how to infer them and the different subtypes of Orthology in OMA, as well as what types of analyses they should be used for.
- Evidence snippets:
  - Snippet 1 (score: 0.658)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [17] Meta-Analysis of Studies Using Suppression Subtractive Hybridization and Microarrays to Investigate the Effects of Environmental Stress on Gene Transcription in Oysters
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
  - Snippet 1 (score: 0.657)
    > For instance, NADH dehydrogenase (EC 1.6.99.3) was deemed to be synonymous with cytochrome c reductase, NADH oxidoreductase and 13 other gene names; see http://enzyme.expasy.org/EC/1.6.99.3). In many cases, the alternative gene name was added to our database annotation to avoid redundancy. In addition, if two or more of the entries in our database of oyster genes encoded the same gene but had been allocated different names in the literature, those redundant sequences were consolidated into a single entry. In some additional cases, genes encoded in the mitochondrial (Mt) genome were allocated accession numbers in the primary literature that corresponded to the entire Mt genome. These were re-allocated gene-specific accessions.
    > After this filtering process, the final consolidated database was re-analyzed to verify the putative functions of the differentially expressed genes. These functional assignments were initially checked against searches of the literature cited in the GenBank registration file for each sequence. The functional category into which the gene fell was then confirmed by reference to the UniProtKB Protein Knowledgebase (http://www.uniprot.org/uniprot/) and the primary literature. The results from these searches were cross-referenced and hierarchically preferenced so that a single biological function could be assigned to each gene sequence in the database. Preference was given to ontologies that were based on experimentally defined functions in oysters, other bivalves, and mollusks in general.
    > As a result of these multiple filters, only sequences from published studies with definitive gene identifications and robust functional annotations were included in subsequent analyses.
    > At the time of this analysis, there were 97,811 nucleotide and 223,784 EST sequences listed in GenBank under the three oyster genera investigated (Table 1). Ninety-eight percent of the CoreNucleotide sequences that we searched against were from the genus Crassostrea, 0.6% were from Saccostrea, and 1.5% were from Ostrea. More than 99% of the dbEST sequences were from the genus Crassostrea.

### [18] Mass spectrometry‐based mitochondrial proteomics for cancer biomarker discovery
- Authors: Zheng Cao, Zikun Song, Wei-Jie Zhou, Xiao-Hui Liu, Yanling Liu et al.
- Year: 2026
- Venue: View
- URL: https://www.semanticscholar.org/paper/2356a7008d3eae0e112f8ac17c84c805a2fbeff7
- DOI: 10.1002/VIW.20250171
- Citations: 2
- Summary: Qualitative advances in MS‐based mitochondrial proteomics, including sample preparation, MS techniques, and data analysis strategies are summarized, and insights into the application of mitochondrial proteomics in the discovery of tumor markers for various cancer types are provided.
- Evidence snippets:
  - Snippet 1 (score: 0.656)
    > Annotations are further enriched with cross-references from Gene Ontology (GO), UniProt, OMIM, and the Human Protein Atlas. 91 itoMiner enhances biological interpretation by linking genes to phenotypes, diseases, and functional pathways, thereby reinforcing the credibility of disease-associated candidate genes. Another notable resource is MitoP2, a platform designed to correlate mitochondrial protein data with molecular functions and disease phenotypes. 92 Especially valuable for researchers delving into the pathological underpinnings of mitochondrial dysfunction, MitoP2 facilitates the identification of potential therapeutic targets by mapping protein anomalies to specific clinical manifestations.

### [19] ReCap enables deep, copy number-scaled cysteine redox proteomics with minimal exogenous oxidation
- Authors: J. Cobley, Hao Jiang, J. El-sayed Moustafa, Melpomeni Platani, Zixin Kang et al.
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/818785cfb75c131aa35027738333aa91fd095b9d
- DOI: 10.64898/2026.06.16.731536
- Summary: ‘ReCap’, a Redox Capture workflow combining Oxi-DIA, an enrichment-free isotope-encoded DIA workflow, with Oxi-Stop, a simple oxygen-exclusion strategy for cryopreserved tissue, reveals cysteine oxidation as a sparse, ordered and quantitatively concentrated signal.
- Evidence snippets:
  - Snippet 1 (score: 0.650)
    > Annotation counts were aggregated at both the protein level and the global proteome level. Third, a site-level cysteine functional resource was generated by extracting positional annotations for selected UniProt feature classes and retaining only annotated cysteine residues. For each annotated cysteine site, accession, gene symbol, protein name, organism, review status, cysteine position, feature type, feature span, ligand metadata, and evidence fields were recorded where available.
    > A protein-level annotation resource was generated from the cysteine summary table. Proteins containing at least one cysteine residue were retained and annotated using UniProtKB JSON records retrieved through the UniProt REST API. For each protein, accession, primary gene name, recommended protein name, organism, and review status were extracted. UniProt cross-references were parsed to collect Gene Ontology (GO), KEGG, and STRING annotations. GO terms were classified into Cellular Component, Biological Process, and Molecular Function categories based on UniProt GO term prefixes. A protein-level master table was generated containing cysteine content, counts of annotated functional cysteines, and the number of associated GO, KEGG, and STRING annotations. A companion long-format annotation table was also produced containing one row per protein-annotation pair.

### [20] Prioritising genetic findings for drug target identification and validation.
- Authors: N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt
- Year: 2024
- Venue: Atherosclerosis
- URL: https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9
- DOI: 10.1016/j.atherosclerosis.2024.117462
- PMID: 38325120
- Citations: 17
- Summary: The current review provides an overview of genetic evidence for drug target identification, and how biomedical databases can be used to provide actionable prioritisation, fully informing downstream experimental validation.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > Other gene identification systems include the Entrez Gene [43] database for gene-specific information, and the HUGO Gene Nomenclature Committee (HGNC) [44] which maintains unique symbols and names for human loci.An analogue for proteins is the UniProt Knowledgebase (UniProtKB) [45], which contains data on protein sequences and function, and each protein in the database is assigned a unique UniProt accession ID.UniProt provides functionality to map between different identifiers, including Ensembl IDs and UniProt accession IDs.
    > A common naming convention is also required to identify the diseases associated with the drug targets.Medical Subject Headings (MeSH) [46] are terms defined by the National Library of Medicine, and act as a standardised thesaurus for diseases and medical conditions which can be used to index PubMed.In some data sources, such as the Chemical Biology Database (ChEMBL) [23], diseases and outcomes will be identified by MeSH terms.However, in other cases, this will not be the case, and a metathesaurus such as the Unified Medical Language System (UMLS) [47] can be used to map synonymous disease terms.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Zhongyan Lu, Lingmeng Kong, Shenhao Ren, J. Aschenbach, Hong Shen (2023). Acid tolerance of lactate-utilizing bacteria of the order Bacteroidales contributes to prevention of ruminal acidosis in goats adapted to a high-concentrate diet. Animal Nutrition. https://www.semanticscholar.org/paper/b9b3a1ffa5d51c9225e5043f74473d80e3a94d8d
2. Dawn Cotter, Andreia Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Ralf C. Mueller, Nicolai Mallig, J. Smith, Lél Eöery, R. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. P. Hornbeck, J. Kornhauser, Sasha L. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
5. B. Waegele, I. Dunger-Kaltenbach, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
6. N. Udeshi, Kayvon Pedram, Tanya Svinkina, Shaunt Fereshetian, S. Myers et al. (2017). Antibodies to biotin enable large-scale detection of biotinylation sites on proteins. Nature methods. https://www.semanticscholar.org/paper/f9e4f461ca61f4399a95875ea96fb075fa959901
7. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Si-Qian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
8. Enlian Chen, Jialu Xu, Yuan-Sheng Liu, Yong-Liang Li, Yiping Feng et al. (2026). Telomere-to-telomere assembly and haplotype analysis of tetraploid Dendrobium officinale illuminate Orchidaceae polyploid evolution and mycorrhizal symbiosis genes. bioRxiv. https://www.semanticscholar.org/paper/b1df798188e8a8909532f07343a1c167e46291b8
9. Y. Fukasawa, J. Tsuji, Szu-Chin Fu, K. Tomii, P. Horton et al. (2015). MitoFates: Improved Prediction of Mitochondrial Targeting Sequences and Their Cleavage Sites. Molecular & Cellular Proteomics : MCP. https://www.semanticscholar.org/paper/9d6a56f3096a15e53bb433a4cfd9ad7109211639
10. Kohei Ito, Masafumi Harada, N. Nakajima, Shigeki Yamamura, M. Tomita et al. (2018). Genomic Analysis of Rhodococcus sp. Br-6, a Bromate Reducing Bacterium Isolated From Soil in Chiba, Japan. Journal of Genomics. https://www.semanticscholar.org/paper/5a46aff9e42e4f79784e2e878938ba507b8bdf2b
11. Mary Kate Bonner, Daniel S. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
12. Taiga Uchida, H. Yamashita, Go Shimada, E. Shoguchi, C. Shinzato (2026). Possible Novel Sulfolipid Utilization Pathway in Giant Clams and Other Aquatic Invertebrates: Implications for Photosymbiosis and Sulfur Cycling. bioRxiv. https://www.semanticscholar.org/paper/fc2752dcc39243be40916b466681cc4f02dc7927
13. Yanhao Tan, Li-Ju Wang, Tianyuzhou Liang, Ying-Ju Lai, Chien-Hung Shih et al. (2026). An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models. Nature Communications. https://www.semanticscholar.org/paper/4ee3e30c14f90463927180ad11f99b48d0a234f4
14. Katrin Fundel, Ralf Zimmer (2006). Gene and protein nomenclature in public databases. BMC Bioinformatics. https://www.semanticscholar.org/paper/75e725b9aa79f1b6943b32164778e5b52f715852
15. P. Sternberg, K. V. Van Auken, Qing-Hua Wang, Adam J. Wright, K. Yook et al. (2024). WormBase 2024: status and transitioning to Alliance infrastructure. Genetics. https://www.semanticscholar.org/paper/dcfce02a58655b0872a8265f5c85dbbd94957294
16. Monique Zahn-Zabal, C. Dessimoz, N. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
17. K. Anderson, Daisy A. Taylor, E. Thompson, A. Melwani, S. Nair et al. (2015). Meta-Analysis of Studies Using Suppression Subtractive Hybridization and Microarrays to Investigate the Effects of Environmental Stress on Gene Transcription in Oysters. PLoS ONE. https://www.semanticscholar.org/paper/2e1f7fa1a93ee5206f397d90f45aefcdf8e0faff
18. Zheng Cao, Zikun Song, Wei-Jie Zhou, Xiao-Hui Liu, Yanling Liu et al. (2026). Mass spectrometry‐based mitochondrial proteomics for cancer biomarker discovery. View. https://www.semanticscholar.org/paper/2356a7008d3eae0e112f8ac17c84c805a2fbeff7
19. J. Cobley, Hao Jiang, J. El-sayed Moustafa, Melpomeni Platani, Zixin Kang et al. (2026). ReCap enables deep, copy number-scaled cysteine redox proteomics with minimal exogenous oxidation. bioRxiv. https://www.semanticscholar.org/paper/818785cfb75c131aa35027738333aa91fd095b9d
20. N. Hukerikar, A. Hingorani, F. Asselbergs, C. Finan, A. Schmidt (2024). Prioritising genetic findings for drug target identification and validation.. Atherosclerosis. https://www.semanticscholar.org/paper/80ee965ca8d81196a8281ab055ff7ff79eda31d9