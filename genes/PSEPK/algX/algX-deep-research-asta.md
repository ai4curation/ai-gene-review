---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T02:36:39.916043'
end_time: '2026-07-08T02:36:45.339287'
duration_seconds: 5.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: algX
  gene_symbol: algX
  uniprot_accession: Q88ND0
  protein_description: 'RecName: Full=Alginate biosynthesis protein AlgX; AltName:
    Full=Probable alginate O-acetyltransferase AlgX; EC=2.3.1.-; Flags: Precursor;'
  gene_info: Name=algX; OrderedLocusNames=PP_1282;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the AlgX family. .
  protein_domains: ALGX/ALGJ_SGNH-like. (IPR031811); AlgX_C. (IPR031798); AlgX_C_sf.
    (IPR038639); AlgX_N. (IPR034655); ALGX (PF16822)
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
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88ND0
- **Protein Description:** RecName: Full=Alginate biosynthesis protein AlgX; AltName: Full=Probable alginate O-acetyltransferase AlgX; EC=2.3.1.-; Flags: Precursor;
- **Gene Information:** Name=algX; OrderedLocusNames=PP_1282;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the AlgX family. .
- **Key Domains:** ALGX/ALGJ_SGNH-like. (IPR031811); AlgX_C. (IPR031798); AlgX_C_sf. (IPR038639); AlgX_N. (IPR034655); ALGX (PF16822)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "algX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'algX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **algX** (gene ID: algX, UniProt: Q88ND0) in PSEPK.

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

- Papers retrieved: 18
- Snippets retrieved: 20

## Relevant Papers

### [1] Discovery of a Novel Alginate Lyase from Nitratiruptor sp. SB155-2 Thriving at Deep-sea Hydrothermal Vents and Identification of the Residues Responsible for Its Heat Stability*
- Authors: A. Inoue, M. Anraku, S. Nakagawa, T. Ojima
- Year: 2016
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/1e78c9d41eb1053f2583a1342c3e2c52bb9ba647
- DOI: 10.1074/jbc.M115.713230
- PMID: 27231344
- Citations: 67
- Influential citations: 1
- Summary: NitAly is a functional alginate lyase, with its unique optimum conditions adapted to its environment, and insights into the heat stability of NitAly could be applied to improve that of other PL-7 alginates lyases.
- Evidence snippets:
  - Snippet 1 (score: 0.788)
    > SB155-2 against P. aeruginosa proteins located within the alginate biosynthesis operon revealed that seven genes encoding the Nitratiruptor sp. SB155-2 homologs were adjacent to one another in the Nitratiruptor sp. SB155-2 genome, namely the P. aeruginosa proteins AlgD (GDP-mannose dehydrogenase), Alg8 (glycosyltransferase), Alg44 (c-di-GMP binding), AlgE (outer membrane porin), AlgG (mannuronic acid C5-epimerase), AlgL (alginate lyase), and AlgA (phosphomannose isomerase/GDP-mannose pyrophosphatase). Thus, these genes may constitute an operon system in Nitratiruptor sp. SB155-2,  supporting that NitAly performs alginate biosynthesis in its natural habitat. Yet the candidate genes for AlgK and AlgX, which are involved in alginate polymerization, were not found. These proteins are needed to form the alginate biosynthesis machinery complex (46), whereby AlgK interacts with AlgE, Alg44, and AlgX. Furthermore, AlgX interacts with Alg44 and the specifically interacting serine protease MucD (47). In addition, AlgI, AlgJ, and AlgF were not found, despite being involved in the O-acetylation of alginate. Thus, proteins with these functions may have low homology with known proteins and may be the currently unidentified proteins encoded by genes such as nis_0180-nis_0184 and nis_0186 located near the nitaly (nis_0185) gene.

### [2] Alginate Polymerization and Modification Are Linked in Pseudomonas aeruginosa
- Authors: M. F. Moradali, I. Donati, I. Sims, S. Ghods, B. Rehm et al.
- Year: 2015
- Venue: mBio
- URL: https://www.semanticscholar.org/paper/19b9ccd0565a9b487a347f55de2934ded1cb95e3
- DOI: 10.1128/mBio.00453-15
- PMID: 25968647
- PMCID: 4436075
- Citations: 90
- Influential citations: 7
- Summary: Bacterial two-hybrid assays and pulldown experiments showed that the catalytic subunit Alg8 directly interacts with the proposed copolymerase Alg44 while embedded in the cytoplasmic membrane, providing new insights into the molecular mechanisms of the synthesis of the unique polysaccharide, alginate.
- Evidence snippets:
  - Snippet 1 (score: 0.765)
    > di-GMP binding to Alg44 (S1) which targets the catalytic site of Alg8 polymerase (S2) through an unknown mechanism. Then, translocation across the periplasmic scaffold is coupled with interactive functional performances of modification events and proteins (right side of model) for alginate length regulation and a series of associated modification events (S3 to S5). AlgL is responsible for degrading misguided alginate accumulating in periplasm (S6). MucD protein links the complex with the posttranslational alginate regulatory network via an interaction with AlgX. coding gentamicin acetyltransferase) flanked by two FRT sites (see the supplemental material).
    > In trans complementation of single-and double-gene-knockout mutants and chromosomal integrations. Relevant genes encoding Alg8, Alg44, AlgG, and AlgX (with and without the 6His tag) were individually or in combination transferred into generated mutants using the pBBR1MCS-5 plasmid and also incorporated into the genome using mini-CTX-lacZ plasmid (see the supplemental material). The pBBR1MCS-5 plasmid containing the various alginate genes was considered to study the impact on production of alginates and their characteristics in order to more sensitively detect changes in the alginates due to additional copy numbers of the respective alginate protein under investigation.
    > Site-specific mutations and deletions of alg44 and alg8. Site-specific mutations and deletions of alg44 and alg8 genes were performed using the QuikChange II site-directed mutagenesis kit (Stratagene) or by DNA synthesis (GenScript), resulting in genes encoding the Alg8(E322A/H323/ E326A) protein, Alg44(R17A/R21A/R21D) protein, and Alg44's N-and C-terminal truncation (see the supplemental material).
    > In vivo detection of the protein-protein interaction network. In vivo detection of protein-protein interaction was performed by employing pulling down
  - Snippet 2 (score: 0.761)
    > and except for algC, their encoding genes are clustered in the alginate biosynthesis operon (algD, alg8, alg44, algK, algE, algG, algX, algL, algI, algJ, algF, algA) (5,6). Except for soluble cytoplasmic proteins AlgA, AlgC, and AlgD, which are responsible for providing the activated nucleotide sugar precursor, GDPmannuronic acid, proteins encoded by the operon are proposed to constitute an envelope-spanning multiprotein complex. Two cytoplasmic membrane-anchored proteins, the glycosyltransferase, Alg8, and the proposed copolymerase, Alg44, are necessary for alginate polymerization (7)(8)(9). The MucR sensor protein, a diguanylate cyclase (DGC)/phosphodiesterase (PDE) embedded in the cytoplasmic membrane, was proposed to provide c-di-GMP for binding to the cytoplasmic PilZ domain of Alg44 by which alginate polymerization is activated (10). Translocation of nascent alginate across the periplasm is coupled with modification processes, including O-acetylation and epimerization. O-Acetylation is independently catalyzed by AlgJ and AlgX (11), while the acetyl group donor is provided by AlgI and AlgF (12,13). The AlgG epimerase converts M residues to G residues in the nascent alginate chain. AlgG, AlgX, and AlgK were suggested to form a periplasmic scaffold for guiding alginate through the periplasm for secretion via the outer membrane protein AlgE (14)(15)(16)(17)(18)(19). It was also suggested that if alginate is misguided into the periplasm, then degradation would be mediated by the periplasmic AlgL lyase (20). Previous studies on protein-protein interactions and mutual stabilities of proposed subunits of the multiprotein
  - Snippet 3 (score: 0.687)
    > 19). It was also suggested that if alginate is misguided into the periplasm, then degradation would be mediated by the periplasmic AlgL lyase (20). Previous studies on protein-protein interactions and mutual stabilities of proposed subunits of the multiprotein biosynthesis machinery provided evidence of binary protein interactions, including AlgE-AlgK, AlgX-AlgK, AlgX-MucD (a serine protease), Alg44-AlgX, and Alg8-AlgG (21,22). However, more experimental evidence is needed to map all protein-protein interactions within the multiprotein complex, in particular toward unraveling the molecular mechanisms of alginate polymerization, molecular mass control, and the relationship of modification events to polymerization.
    > In this study, protein-protein interactions within the multiprotein complex were investigated using the bacterial two-hybrid technique and pulldown assays. The proposed interacting protein surface of Alg44 was probed, and the molecular mechanism of c-di-GMP-mediated activation was studied (23,24). The role of Alg8, Alg44, AlgG, and AlgX with respect to polymerization and modification was studied by analyzing the composition and material properties of alginates produced by various strains. We employed a constitutively alginate-producing strain of P. aeruginosa, PDO300, to generate isogenic single-and double-gene knockouts of alg8, alg44, algG, and algX. This allowed studying the role of the respective proteins in alginate polymerization and/or modifications by introducing additional copy numbers of subunits or their variants in trans. The impact of various alginate structures on motility, biofilm formation, and architecture was investigated.

### [3] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
- Authors: P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
- DOI: 10.1093/nar/gkr1122
- PMID: 22135298
- PMCID: 3245126
- Citations: 1605
- Influential citations: 155
- Summary: PhosphoSitePlus (http://www.phosphosite.org) is an open, comprehensive, manually curated and interactive resource for studying experimentally observed post-translational modifications, primarily of human and mouse proteins. It encompasses 1 30 000 non-redundant modification sites, primarily phosphorylation, ubiquitinylation and acetylation. The interface is designed for clarity and ease of navigation. From the home page, users can launch simple or complex searches and browse high-throughput d...
- Evidence snippets:
  - Snippet 1 (score: 0.726)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [4] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.714)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [5] Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B
- Authors: Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al.
- Year: 2022
- Venue: Data in Brief
- URL: https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
- DOI: 10.1016/j.dib.2022.108592
- PMID: 36164296
- PMCID: 9508510
- Citations: 2
- Influential citations: 1
- Summary: Covering differential proteomes of three cell lines in a pairwise model, the data could be used to further screen the kinesins that play a vital role in regulating the growth of UM.
- Evidence snippets:
  - Snippet 1 (score: 0.706)
    > 2.8.1. Annotation methods 2.8.1.1. Functional annotation. UniProt-GOA database was utilized to retrieve Gene Ontology (GO) annotation proteome. First, the identified protein identity was converted to UniProt identity and then mapped to GO identity based on the protein identity. When the identified protein was not annotated by UniProt-GOA, the functional annotation of that protein was conducted using the InterProScan software according to the amino acid sequence alignment approach. All proteins were then classified into 3 groups: molecular function, cellular component and biological process.

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
  - Snippet 1 (score: 0.705)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [7] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
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
  - Snippet 1 (score: 0.704)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [8] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.703)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [9] Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea
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
  - Snippet 1 (score: 0.702)
    > The BLASTx homology search tool, a component of the standalone NCBI-blast-2.3.0+, was used to perform functional annotation of the F. udum genes (Altschul et al., 1990). With a cut-off E value of ≤1e−06 and a similarity of 34%, BLASTx identified the homologous sequences of the genes in the NCBI non-redundant protein database. Gene ontology (GO) analysis was carried out using Blast2GO PRO 4.1.5 (Conesa and Gotz, 2008). In three different mappings, B2G performed as follows: (1) Using two NCBI-provided mapping files, blast result accessions are used to get gene names (symbols; gene info, gene 2 accessions). (2) Blast result GI identifiers were used to retrieve UniProt IDs using a mapping file from PIR (non-redundant reference protein database), which includes PSD, Swiss-Prot, UniProt, TrEMBL, GenPept, RefSeq, and PDB. The names of the identified genes were searched in the species-specific entries of the gene product table of the GO database. With the aid of the KAAS-KEGG Automatic Annotation Server, pathway analyses were carried out. This database provides functional annotation of genes using other data servers (Moriya et al., 2007). Accessions from the blast results were looked for in the DBXRef table of the GO database.

### [10] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.698)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [11] Transcriptional Response of Mucoid Pseudomonas aeruginosa to Human Respiratory Mucus
- Authors: V. Cattoir, V. Cattoir, G. Narasimhan, D. Skurnik, H. Aschard et al.
- Year: 2012
- Venue: mBio
- URL: https://www.semanticscholar.org/paper/1ad4f5c18a5217d47a3a9291429b3d103fb031ba
- DOI: 10.1128/mBio.00410-12
- PMID: 23143799
- PMCID: 3509433
- Citations: 41
- Influential citations: 1
- Summary: A snapshot of responses in a pathogen adapted to a human host through assimilation of regulatory signals from tissues, optimizing its long-term survival potential is provided.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > Among these 656 genes, approximately 20% coded for hypothetical proteins of unknown function, equally represented in RNA samples obtained under both sets of conditions (see Fig. S2 and Table S3 in the supplemental material). In the presence of mucus, expression of genes coding for proteins involved in motility/attachment and the protein secretion/export apparatus and related to phage, transposons, or plasmids was induced whereas expression of genes coding for proteins involved in energy metabolism and transport of small molecules as well as genes coding for putative enzymes, secreted factors (toxins, enzymes, alginate), and two-component regulatory systems was repressed.
    > Repression of alginate production by mucus. The overexpression of alginate in mucoid P. aeruginosa isolates from CF patients is due to mutations in regulatory genes, primarily in mucA, encoding the antagonist of the alternative sigma factor AlgU (15).
    > Stable derepression of the alginate biosynthetic pathways provides a mechanism for producing copious amounts of this polysaccharide without environmental influences. The results of the RNAseq analysis showed that the entire group of genes encoding proteins involved in the synthesis, modification, and export of alginate were highly expressed in the mucoid strain 2192 grown in minimal media but that the levels of the corresponding transcripts were reduced in media containing human mucus compared to media lacking this supplement. Specifically, the mRNA levels for each gene within the 12-gene cluster (algD, alg8, alg44, algK, algE, algG, algX, algL, algI, algJ, algF, and algA) were reduced, with fold changes between Ϫ4.8 and Ϫ9.4 (Fig. 2). No effect of the composition of media was observed for the moderately to highly expressed genes in the alginate regulatory operon (algU, mucABC, and D), and none of the other known regulatory genes (algQ, algP, algZ, algR, and algW) had a significant fold change in expression (see Table S4A in the supplemental material).

### [12] Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains
- Authors: J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al.
- Year: 2025
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
- DOI: 10.1038/s41598-025-29509-x
- PMID: 41310174
- PMCID: 12749726
- Citations: 1
- Summary: Findings include large plasmid deletions, an enrichment of mutations in secondary metabolite biosynthesis and regulatory genes, and metabolic shifts redirecting amino acid and carbon flux toward CA biosynthetic pathways.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > Gene annotation was primarily derived from the S. clavuligerus reference genome in the NCBI database and was annotated using the NCBI Prokaryotic Genome Annotation Pipeline 59 . However, several CA biosynthetic genes were manually corrected based on published literature 9 . For instance, two loci were originally annotated as clavaminate synthase 1 (cas1), but one of these loci is located near the cephamycin C biosynthetic cluster, indicating it was actually cas2. Following this correction, the RefSeq accession numbers of all genes in the reference genome were cross-referenced with the UniProt database to obtain additional annotations 60 . For the mutated genes identified through ICA, protein existence levels were manually assigned based on the UniProt data, including protein existence status, annotation score, similar proteins, and relevant publications.

### [13] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.689)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [14] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.688)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [15] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.687)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [16] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.685)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [17] Pseudomonas aeruginosa AlgF is a protein–protein interaction mediator required for acetylation of the alginate exopolysaccharide
- Authors: Kristin E. Low, Andreea A. Gheorghita, S. Tammam, Gregory B. Whit ﬁ eld, Yancheng E. Li et al.
- Year: 2023
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/6b9a22cb9c15b2c7a9e47966866582c22648573b
- DOI: 10.1016/j.jbc.2023.105314
- PMID: 37797696
- PMCID: 10641220
- Citations: 6
- Summary: It is proposed that AlgF functions to mediate protein-protein interactions between alginate acetylation enzymes, forming the periplasmic AlgJFXK (AlgJ-AlgF- AlgX-AlGK) acetylations and export complex required for robust biofilm formation.
- Evidence snippets:
  - Snippet 1 (score: 0.684)
    > After modification, alginate is exported from the cell by AlgX, AlgK, and AlgE (24). Belonging to the membrane-bound O-acetyltransferase family of proteins (19,22), AlgI is hypothesized to receive an acetyl group from an unknown donor in the cytoplasm and transfer it to AlgJ in the periplasm (25). Although AlgJ exhibits acetylesterase activity in vitro, AlgJ is unable to bind or acetylate poly-mannuronate oligomers in vitro, suggesting that it is an intermediary in alginate acetylation (21). AlgX is a periplasmic acetyltransferase that can remove an acetyl group from an artificial donor and transfer it onto mannuronate polymer in vitro. In addition, chromosomal mutation of AlgX residues required for its acetyltransferase activity led to production of nonacetylated alginate (20,21). Thus, it has been hypothesized that a relay takes place to transfer an acetyl group from the cytoplasm to the polysaccharide chain via AlgI, AlgJ, and finally AlgX (19)(20)(21). AlgF is also localized to the periplasm and is required for alginate acetylation in vivo but little is known about its structure or function to date (19,23).
    > Here, we describe the structure of AlgF determined by CS-Rosetta from chemical shifts data (26) and supported by interproton nuclear Overhauser effect (NOE) analysis. We demonstrate protein-protein interactions in vitro between AlgF and AlgJ, as well as AlgF and AlgX, by isothermal titration calorimetry (ITC) and an interaction between AlgF and AlgX identified by co-immunoprecipitation (co-IP) in P. aeruginosa.

### [18] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.679)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. A. Inoue, M. Anraku, S. Nakagawa, T. Ojima (2016). Discovery of a Novel Alginate Lyase from Nitratiruptor sp. SB155-2 Thriving at Deep-sea Hydrothermal Vents and Identification of the Residues Responsible for Its Heat Stability*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/1e78c9d41eb1053f2583a1342c3e2c52bb9ba647
2. M. F. Moradali, I. Donati, I. Sims, S. Ghods, B. Rehm et al. (2015). Alginate Polymerization and Modification Are Linked in Pseudomonas aeruginosa. mBio. https://www.semanticscholar.org/paper/19b9ccd0565a9b487a347f55de2934ded1cb95e3
3. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
4. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
5. Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al. (2022). Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B. Data in Brief. https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
6. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
7. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
8. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
9. A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al. (2023). Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea. Frontiers in Microbiology. https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
10. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
11. V. Cattoir, V. Cattoir, G. Narasimhan, D. Skurnik, H. Aschard et al. (2012). Transcriptional Response of Mucoid Pseudomonas aeruginosa to Human Respiratory Mucus. mBio. https://www.semanticscholar.org/paper/1ad4f5c18a5217d47a3a9291429b3d103fb031ba
12. J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al. (2025). Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains. Scientific Reports. https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
13. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
14. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
15. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
16. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
17. Kristin E. Low, Andreea A. Gheorghita, S. Tammam, Gregory B. Whit ﬁ eld, Yancheng E. Li et al. (2023). Pseudomonas aeruginosa AlgF is a protein–protein interaction mediator required for acetylation of the alginate exopolysaccharide. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/6b9a22cb9c15b2c7a9e47966866582c22648573b
18. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508