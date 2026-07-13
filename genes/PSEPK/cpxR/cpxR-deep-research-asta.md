---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T12:23:21.125754'
end_time: '2026-07-08T12:23:27.386514'
duration_seconds: 6.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cpxR
  gene_symbol: cpxR
  uniprot_accession: Q88HI5
  protein_description: 'SubName: Full=CpxR-Pasp DNA-binding transcriptional two-component
    system regulator {ECO:0000313|EMBL:AAN68976.1};'
  gene_info: Name=cpxR {ECO:0000313|EMBL:AAN68976.1}; OrderedLocusNames=PP_3372 {ECO:0000313|EMBL:AAN68976.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: CheY-like_superfamily. (IPR011006); OmpR/PhoB-type_DNA-bd. (IPR001867);
    Sig_transdc_resp-reg_C-effctor. (IPR016032); Sig_transdc_resp-reg_receiver. (IPR001789);
    WalR-like. (IPR039420)
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
- **UniProt Accession:** Q88HI5
- **Protein Description:** SubName: Full=CpxR-Pasp DNA-binding transcriptional two-component system regulator {ECO:0000313|EMBL:AAN68976.1};
- **Gene Information:** Name=cpxR {ECO:0000313|EMBL:AAN68976.1}; OrderedLocusNames=PP_3372 {ECO:0000313|EMBL:AAN68976.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CheY-like_superfamily. (IPR011006); OmpR/PhoB-type_DNA-bd. (IPR001867); Sig_transdc_resp-reg_C-effctor. (IPR016032); Sig_transdc_resp-reg_receiver. (IPR001789); WalR-like. (IPR039420)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cpxR" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cpxR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cpxR** (gene ID: cpxR, UniProt: Q88HI5) in PSEPK.

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

### [1] FusionPDB: a knowledgebase of human fusion proteins
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
  - Snippet 1 (score: 0.742)
    > To assign functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt for 10 619 genes involved in 15 030 fusion genes ( 10 ). UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features and three secondary structure features. Since such feature loci information is based on amino acid sequences, the genomic breakpoint information was converted into the amino acid level while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE (v19) gene model of human reference genome ( 11 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported such fusion genes as having not retained that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.
  - Snippet 2 (score: 0.642)
    > There are multiple representative functional mechanisms of fusion genes as shown in Figure 3 A. Suppose a partner gene, with the active promoter and dimerization functional domains, is fused with a kinase domain. This will constitutively drive the activated expression of the kinase, leading to uncontrolled cell proliferation (3)(4)(5). If a partner gene with a protooncogene or transactivation domain is fused with a transcription factor with a DNA-binding domain, it will result in target gene activation ( 6 ). Through fusion, one protein can lose its interactions with important cellular regulators (i.e. MLL fusion genes) ( 7 ). If the 3 -UTR region of a fusion gene is truncated, such a fusion transcript can avoid the regulation by miRNAs ( 8 ). Other mechanisms include the loss of function of tumor suppressors and DNA damage repairs through the deletion or frameshift open reading frame (ORF) of fusion transcripts ( 10 ,11 ). Targeting the downstream effectors of fusion genes is a noteworthy recent approach ( 12 ,13 ). Cellular essential complexes or machinery can lose their original function due to the formation of a fusion gene of one of their subunits ( 15 ). Investigation of the retention of the fusion protein functional features can utilize diverse functional mechanisms in therapeutics for patients.
    > For this aim, we investigated domain retention at the given breakpoints of ∼43K fusion proteins from FusionGDB2.0 and 1267 fusion proteins of 266 manually curated fusion genes from ChimerKB4. In the 'Fusion Protein Functional Features' category, we provide a detailed annotation of fusion protein functions through the retention search of 39 protein features from UniProt based on the fusion protein sequence. In this category, we specifically provide the results of the retention studies of 13 features belonging to the 'region' subsection, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger', to focus on the major functional components.

### [2] FusionNeoAntigen: a resource of fusion gene-specific neoantigens
- Authors: H. Kumar, Ruihan Luo, Jianguo Wen, Chengyuan Yang, Xiaobo Zhou et al.
- Year: 2023
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/f3d4fd48edb74b21b90f5df9f57c3fbb214aba95
- DOI: 10.1093/nar/gkad922
- PMID: 37870454
- PMCID: 10767944
- Citations: 13
- Summary: FusionNeoAntigen will help to develop fusion gene-based immunotherapies and provide fusion gene information, corresponding fusion protein sequences, fusion breakpoint peptide sequences, fusion gene-derived neoantigens prediction, virtual screening between fusion breakpoint peptides having potential fusion neoantigens and human leucocyte antigens and human leucocyte antigens, and literature curation.
- Evidence snippets:
  - Snippet 1 (score: 0.742)
    > To assign functional or genetic categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt ( 14 ) for 10 619 genes involved in 15 030 fusion genes. UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features, and three secondary structure features. Since such feature loci information was based on amino acid sequence, the genomic breakpoint information was converted into amino acid sequences while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE gene model of human reference genome v19 ( 15 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported that such fusion genes did not retain that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.

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
  - Snippet 1 (score: 0.732)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.727)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [5] Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea
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
  - Snippet 1 (score: 0.719)
    > The BLASTx homology search tool, a component of the standalone NCBI-blast-2.3.0+, was used to perform functional annotation of the F. udum genes (Altschul et al., 1990). With a cut-off E value of ≤1e−06 and a similarity of 34%, BLASTx identified the homologous sequences of the genes in the NCBI non-redundant protein database. Gene ontology (GO) analysis was carried out using Blast2GO PRO 4.1.5 (Conesa and Gotz, 2008). In three different mappings, B2G performed as follows: (1) Using two NCBI-provided mapping files, blast result accessions are used to get gene names (symbols; gene info, gene 2 accessions). (2) Blast result GI identifiers were used to retrieve UniProt IDs using a mapping file from PIR (non-redundant reference protein database), which includes PSD, Swiss-Prot, UniProt, TrEMBL, GenPept, RefSeq, and PDB. The names of the identified genes were searched in the species-specific entries of the gene product table of the GO database. With the aid of the KAAS-KEGG Automatic Annotation Server, pathway analyses were carried out. This database provides functional annotation of genes using other data servers (Moriya et al., 2007). Accessions from the blast results were looked for in the DBXRef table of the GO database.

### [6] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.706)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [7] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.701)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [8] KinaseFusionDB: an integrative knowledge of kinase fusion proteins in multi-scales
- Authors: H. Kumar, Zikang Chen, Abayomi Adegunlehin, Loren Trowbridge, Leonardo Aguilar et al.
- Year: 2025
- Venue: Briefings in Bioinformatics
- URL: https://www.semanticscholar.org/paper/d212d0a2c8e4a7cedcd2c1e4fa11ed6de23345f7
- DOI: 10.1093/bib/bbaf259
- PMID: 40471992
- PMCID: 12140011
- Summary: A novel in silico pipeline for predicting 3D structures of kinase fusion proteins and performing structure-based virtual screening, which revealed that most predicted structures showed high pLDDT scores (pLDDT >70) within conserved kinase domains.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > To assign the functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases, and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', Figure 1. Overview of KinaseFusionDB and its role in understanding kinase fusion proteins. (a) I. The top section identifies therapeutic targets for oncogenic activation of kinases, including wild-type kinases activated by overexpression or genomic amplification, mutated kinases with gain-offunction mutations, and kinase fusion proteins resulting from chromosomal rearrangements. II. The middle section highlights the functionalities of KinaseFusionDB, such as providing functional annotations, mRNA/protein expression data, drug binding information, and relevant literature reviews. III. The third section addresses the current limitations in targeting kinase fusion proteins, particularly the lack of comprehensive 3D structures for these proteins. It emphasizes the partial knowledge of kinase fusion protein structures and the need for further drug screening. IV. The bottom section discusses how computational approaches, such as predicted 3D structures (e.g. from AlphaFold2), can fill these gaps, supporting drug screening and filtering based on consistent binding among multiple fusion protein isoforms. (b) Kinase domain-retained human kinase fusion proteins.
    > 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane', and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt [26] accessions from UniProt for 10 619 genes involved in 15 030 fusion genes [27]. UniProt provides the loci information of 39 protein features, including 6 molecule processing features, 13 region features, 4 site features, 6 amino acid modification features, 2 natural variation features, 5 experimental info features, and 3 secondary structure features.

### [9] A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi
- Authors: R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al.
- Year: 2014
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
- DOI: 10.1186/1471-2164-15-316
- PMID: 24773765
- PMCID: 4234515
- Citations: 41
- Summary: This sequencing effort has produced the first set of whole-genome sequencing data on any ctenophore species and is amongst the first wave of projects to sequence an animal genome de novo solely using next-generation sequencing technologies.
- Evidence snippets:
  - Snippet 1 (score: 0.687)
    > In an effort to engage the collective expertise of the scientific community, we have implemented a collaborative wiki (MediaWiki version 1.19.11) for the Mnemiopsis gene complement. The Mnemiopsis Gene Wiki is accessible from the left sidebar of most pages and is searchable either by selecting a Mnemiopsis gene identifier (e.g., ML00011a) from the drop-down menu or by manually entering an identifier in the appropriate search box. Users can also access these pages by clicking on a gene in the 2.2 track of the genome browser. Each record in the Gene Wiki represents a single Mnemiopsis gene and provides the following annotation: nucleotide and protein sequences, coding exonic genomic coordinates, pre-computed BLAST hits from numerous organisms displaying the top hits for each protein, the top non-self BLAST hit to Mnemiopsis, Pfam-A domains, Gene Ontology (GO) functional annotations, human disease genes from Online Mendelian Inheritance in Man (OMIM), and a table of ortholog clusters formed by phylogenetically informed clustering methods [4] (Figure 5). In addition, controlled editable sections have been included that permit (and encourage) the scientific community to provide further gene annotation for isoforms, in situ images, references, and other notes for each gene. Users interested in supplementing our gene model annotation at the Mnemiopsis Gene Wiki pages must first create an account and log in prior to submitting their contributions. In-house subject matter expert data curators are notified by e-mail following the creation of a new user account or an edit to an existing Gene Wiki record. Any content changes or additions to the Gene Wiki are thoroughly evaluated by these data curators and are made public subject to their approval.
    > Pre-compiled BLAST hits are enumerated in tabular form. Each Mnemiopsis protein was compared to the UniProt and NCBI non-redundant protein databases (nr) using BLASTP. The results display the hit number, the accession numbers, E-values, and brief descriptions of the top four hits (lowest E-values). Accession numbers are linked to relevant corresponding entries at UniProt and GenBank.

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
  - Snippet 1 (score: 0.685)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.665)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [12] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
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
  - Snippet 1 (score: 0.664)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

### [13] Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms
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
  - Snippet 1 (score: 0.664)
    > Examples are for illustrative purposes only and specific to each case, hence not all the entities are shown and highlighted. RED: Gene/Protein BLUE: Disease GREEN: Organism a. Biomedical concepts Gene/Protein: Annotations could be specific gene/protein names or classes/family names of gene/proteins. In particular, very broad concepts like "protein", "gene", "enzyme", "receptors", "kinase", "cytokine", "transcription regulators/factors" are out of the scope of annotations. However, family/subtype names of those concepts are considered for the annotations, such as "amylolytic enzyme", "antioxidant enzyme", "map kinase p38", because these terms narrow the concepts to specific families of gene/protein, enzyme.
    > Annotators can refer to Uniprot and Protein Ontology.

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
  - Snippet 1 (score: 0.661)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [15] Spore Germination of the Obligate Biotroph Spongospora subterranea: Transcriptome Analysis Reveals Germination Associated Genes
- Authors: Sadegh Balotf, R. Tegg, D. Nichols, C. Wilson
- Year: 2021
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/d6fe7c793bbd642b3cf0b2c098589c5c5b8f7eef
- DOI: 10.3389/fmicb.2021.691877
- PMID: 34234764
- PMCID: 8256667
- Citations: 10
- Summary: The datasets generated in this study provide a basic knowledge of the physiological processes associated with spore germination and will facilitate functional predictions of novel genes in S. subterranea and other plasmodiophorids.
- Evidence snippets:
  - Snippet 1 (score: 0.659)
    > Of 679 differentially expressed transcripts, 570 transcripts were annotated in protein databases. Gene ontology (GO) enrichment analysis of differentially expressed genes (DEGs) was conducted to identify the functional categories of the annotated genes. These DEGs were assigned to GO-terms for biological processes and molecular functions (David annotation). The significantly (Pvalue <0.05) enriched biological processes (top 25 only) and molecular functions are presented in Figure 3. The complete list of GO categories of DEGs is listed in Supplementary Table 3.
    > The major functional categories of biological processes were as follows: cellular metabolic process, organic substance metabolic process and metabolic process (n = 38 each); primary metabolic process (n = 36); macromolecule metabolic process (n = 32); cellular macromolecule metabolic process (n = 30); protein metabolic process (n = 24); response to stimulus (n = 23) and cellular protein metabolic process (n = 21) (Figure 3A). Among the various categories, binding (n = 35), protein binding and transferase activity (n = 16 each) were dominantly represented within the molecular function category. Other significantly represented categories include kinase activity (n = 8) and macromolecular complex binding (n = 4) (Figure 3B).
    > The functional annotation of DEGs was also retrieved from UniProt (Figure 4). Transport (n = 34), transcription regulation (n = 27), Ubl conjugation pathway (n = 18), DNA repair (n = 11) and mRNA processing (n = 11) were the most represented functions in the DEGs.
    > After obtaining the functional annotation of the identified transcripts from the gene and protein databases, we generated a list of selected DEGs with the possible role in the germination of resting spores in S. subterranea (Table 2). Among the upregulated group, the majority of genes were related to the initiation and regulation of transcription such as heat shock protein, transcription initiation factor and proteasome. The DNA repair genes such as DNA repair factor IIH helicase (Table 2 and Supplementary Table 2) were also found in the upregulated transcript.

### [16] iPCD: A Comprehensive Data Resource of Regulatory Proteins in Programmed Cell Death
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
  - Snippet 1 (score: 0.650)
    > The PCD regulators were collected and annotated. First, 1,091,014 PCD regulators were annotated with basic information, including 'iPCD ID', 'status', 'Ensembl Gene ID', 'Ensembl Protein ID', 'UniProt Accession', 'PDB structure', 'Function', 'Protein Sequence', 'Nucleotide Sequence', 'Key word' and 'Gene Ontology'. For each species, all regulatory proteins were alphabetically ordered based on their gene names. Then, each protein was automatically assigned a unique iPCD ID for convenient organization in the database. For example, the GPX4 protein in Homo sapiens was assigned with an ID of 'iPCD-Hsa-1522'. Subsequently, 102 additional public resources were integrated to annotate 17,768 regulators from 8 model organisms, including Homo sapiens, Mus musculus, Rattus norvegicus, Drosophila melanogaster, Caenorhabditis elegans, Saccharomyces cerevisiae, Arabidopsis thaliana and Danio rerio. These public resources covered 16 distinct aspects, which contained (i) genetic variation and mutation, (ii) functional annotation, (iii) structural annotation, (iv) physicochemical property, (v) functional domain, (vi) post-translational modification (PTM), (vii) disease-associated information, (viii) protein-protein interaction (PPI), (ix) drug-target relation, (x) orthologous information, (xi) biological pathway, (xii) transcriptional regulator, (xiii) mRNA expression, (xiv) protein expression/proteomics, (xv) subcellular localization and (xvi) DNA and RNA element. The detailed processing of 102 public resources is provided in Supplementary Methods. A brief flowchart of the study is shown in Figure 1A.

### [17] Integrative analysis of next generation sequencing for small non-coding RNAs and transcriptional regulation in Myelodysplastic Syndromes
- Authors: D. Beck, S. Ayers, J. Wen, Miriam Brandl, T. Pham et al.
- Year: 2011
- Venue: BMC Medical Genomics
- URL: https://www.semanticscholar.org/paper/de13a83fb5d84d8eb997c4dec2d73ed4be2efbd8
- DOI: 10.1186/1755-8794-4-19
- PMID: 21342535
- PMCID: 3060843
- Citations: 44
- Influential citations: 3
- Summary: Novel findings are provided that build a basis of further investigations of diagnostic biomarkers, targeted therapies and studies on MDS pathogenesis, and confirmed important regulatory roles for MDS linked miRNAs and TFs.
- Evidence snippets:
  - Snippet 1 (score: 0.648)
    > The flat files FACTOR and GENE of the commercially available database TRANSFAC v2008_2 [26] were downloaded and parsed into a MySQL database. The FAC-TOR and GENE flat files contain information on transcription factor proteins and genes regulated by transcription factors, respectively. A total of 2362 regulating factors for the human species (Homo Sapiens) were extracted and 70 entries, that did not describe proteins, but other regulatory factors were omitted. A large fraction (about 77 percent) of the remaining 2292 transcription factor proteins were mapped to Uniprot [27], either by external database ID's, or exact matches between protein names. With these accessions the protein coding gene IDs, as well as other information was downloaded automatically via a MATLAB based data retrieval algorithm implemented for this study. The transcript and probeset annotation files for the Affymetrix GeneChip Human Exon 1.0 ST Array were downloaded from the manufacture's website http://www. affymetrix.com and parsed into MySQL tables. Transcript IDs for 98 percent of the human transcription factor coding genes were extracted based on direct matches between gene names.
    > Genes that can potentially be up regulated when the transcription factor protein binds to a specific site in its promoter region are called transcription factor target genes. We extracted all target genes for human transcription factor proteins by joining a number of database tables. This revealed 3296 gene targets for the 2292 transcription factor proteins. We used direct matches between the target gene names, as well as additional entries, to identify corresponding transcripts on the Affymetrix GeneChip. This resulted in matches for 83 percent of the target genes.

### [18] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.645)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [19] Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation
- Authors: Eugenio L Mangas, Alejandro Rubio, R. Álvarez-Marín, Gema Labrador-Herrera, J. Pachón et al.
- Year: 2019
- Venue: Microbial Genomics
- URL: https://www.semanticscholar.org/paper/ccdc06e24b4cff1ddca5e537c65e5f14c5f017b3
- DOI: 10.1099/mgen.0.000309
- PMID: 31626589
- PMCID: 6927304
- Citations: 64
- Influential citations: 2
- Summary: A genomics analysis of almost 2500 strains found two different groups of genomes found based on the number of shared genes, one of which rarely has plasmids, and bears clustered regularly interspaced short palindromic repeat (CRISPR) sequences, in addition to CRISPR-associated genes (cas genes) or restriction-modification system genes.
- Evidence snippets:
  - Snippet 1 (score: 0.640)
    > To homogenize the genome annotation, the sequences of all genomes were analysed using the same protocol. The proteinencoding genes were predicted using Prokka version 1.13 [24], and the predicted protein sequences were functionally annotated using Sma3s v2 and UniProt taxonomic division bacteria 2019_01 as a reference database [25,55].
    > To annotate specific genes, GO (gene ontology) terms and UniProt keywords assigned by Sma3s were used. To find genes associated with CRISPR systems, protein sequences coming

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim (2023). FusionPDB: a knowledgebase of human fusion proteins. Nucleic Acids Research. https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
2. H. Kumar, Ruihan Luo, Jianguo Wen, Chengyuan Yang, Xiaobo Zhou et al. (2023). FusionNeoAntigen: a resource of fusion gene-specific neoantigens. Nucleic Acids Research. https://www.semanticscholar.org/paper/f3d4fd48edb74b21b90f5df9f57c3fbb214aba95
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
5. A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al. (2023). Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea. Frontiers in Microbiology. https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
6. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
7. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
8. H. Kumar, Zikang Chen, Abayomi Adegunlehin, Loren Trowbridge, Leonardo Aguilar et al. (2025). KinaseFusionDB: an integrative knowledge of kinase fusion proteins in multi-scales. Briefings in Bioinformatics. https://www.semanticscholar.org/paper/d212d0a2c8e4a7cedcd2c1e4fa11ed6de23345f7
9. R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al. (2014). A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi. BMC Genomics. https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
10. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
11. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
12. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
13. Xiao Yang, Shyamasree Saha, Aravind Venkatesan, Santosh Tirunagari, Vid Vartak et al. (2023). Europe PMC annotated full-text corpus for gene/proteins, diseases and organisms. Scientific Data. https://www.semanticscholar.org/paper/fcd1d26d443a982ea79e1351bfaf791209e7c74d
14. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
15. Sadegh Balotf, R. Tegg, D. Nichols, C. Wilson (2021). Spore Germination of the Obligate Biotroph Spongospora subterranea: Transcriptome Analysis Reveals Germination Associated Genes. Frontiers in Microbiology. https://www.semanticscholar.org/paper/d6fe7c793bbd642b3cf0b2c098589c5c5b8f7eef
16. Dachao Tang, Cheng Han, Shaofeng Lin, Xiaodan Tan, Weizhi Zhang et al. (2022). iPCD: A Comprehensive Data Resource of Regulatory Proteins in Programmed Cell Death. Cells. https://www.semanticscholar.org/paper/eb35030c62fa8e25fe91d3a4e48fef1de95e562c
17. D. Beck, S. Ayers, J. Wen, Miriam Brandl, T. Pham et al. (2011). Integrative analysis of next generation sequencing for small non-coding RNAs and transcriptional regulation in Myelodysplastic Syndromes. BMC Medical Genomics. https://www.semanticscholar.org/paper/de13a83fb5d84d8eb997c4dec2d73ed4be2efbd8
18. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
19. Eugenio L Mangas, Alejandro Rubio, R. Álvarez-Marín, Gema Labrador-Herrera, J. Pachón et al. (2019). Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation. Microbial Genomics. https://www.semanticscholar.org/paper/ccdc06e24b4cff1ddca5e537c65e5f14c5f017b3