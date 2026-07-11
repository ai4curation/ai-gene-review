---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T22:42:08.392911'
end_time: '2026-07-10T22:42:13.252620'
duration_seconds: 4.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4428
  gene_symbol: PP_4428
  uniprot_accession: Q88EM6
  protein_description: 'SubName: Full=Amino acid ABC transporter, periplasmic amino
    acid-binding protein {ECO:0000313|EMBL:AAN70005.1};'
  gene_info: OrderedLocusNames=PP_4428 {ECO:0000313|EMBL:AAN70005.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial solute-binding protein 3 family.
  protein_domains: Ectoine_EhuB. (IPR014337); Solute-binding_3/MltF_N. (IPR001638);
    SBP_bac_3 (PF00497)
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
- **UniProt Accession:** Q88EM6
- **Protein Description:** SubName: Full=Amino acid ABC transporter, periplasmic amino acid-binding protein {ECO:0000313|EMBL:AAN70005.1};
- **Gene Information:** OrderedLocusNames=PP_4428 {ECO:0000313|EMBL:AAN70005.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial solute-binding protein 3 family.
- **Key Domains:** Ectoine_EhuB. (IPR014337); Solute-binding_3/MltF_N. (IPR001638); SBP_bac_3 (PF00497)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4428" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4428' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4428** (gene ID: PP_4428, UniProt: Q88EM6) in PSEPK.

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

### [1] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.778)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

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
  - Snippet 1 (score: 0.772)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [3] Cj1199 Affect the Development of Erythromycin Resistance in Campylobacter jejuni through Regulation of Leucine Biosynthesis
- Authors: H. Hao, Fei Li, Jing Han, S. Foley, Menghong Dai et al.
- Year: 2017
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/9152e27a908296795b4779c02d4aa02ffae2f388
- DOI: 10.3389/fmicb.2017.00016
- PMID: 28144238
- PMCID: 5239772
- Citations: 11
- Summary: The Cj1199 gene may directly regulate the leucine biosynthesis and transport and indirectly affect the development of erythromycin resistance in C. jejuni.
- Evidence snippets:
  - Snippet 1 (score: 0.764)
    > The 20 genes down-regulated in Cj1199 are shown in Table 2.
    > Five genes (leuA, leuB, leuC, leuD, and trpE) were involved in amino acid biosynthesis. The leuABCD genes participated in leucine biosynthesis pathway. Five genes (Cj0919c, Cj0920c, peb1A, pebC, and ceuC) encoded transporters or binding proteins. The permease protein (Cj0919c-Cj0920c), substratebinding protein (Peb1A), and ATP-binding protein (PebC) worked cooperatively in an ABC-type amino acid transport system. The ceuC encoded enterochelin uptake permease which was also transporters or binding protein. The Cj0246c was involved in signal transduction. Six genes (Cj0560, Cj1356c, Cj0423, Cj0424, Cj0425, and Cj0200c) encoded putative integral membrane or periplasmic proteins. Another three (Cj1025c, Cj1722c, and Cj1388) were hypothetical genes. Only Cj1241 gene encoding a putative major facilitator superfamily (MFS) transport protein was up-regulated in Cj1199. Using qRT-PCR to verify the microarray results, Cj1241 gene was confirmed to be up-regulated, while other four respective genes (Cj0920c, Cj1388, Cj0560, and Cj1717c) were confirmed to be down-regulated (Figure 1).

### [4] FusionPDB: a knowledgebase of human fusion proteins
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
  - Snippet 1 (score: 0.762)
    > To assign functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt for 10 619 genes involved in 15 030 fusion genes ( 10 ). UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features and three secondary structure features. Since such feature loci information is based on amino acid sequences, the genomic breakpoint information was converted into the amino acid level while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE (v19) gene model of human reference genome ( 11 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported such fusion genes as having not retained that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.

### [5] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
- Authors: Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al.
- Year: 2020
- Venue: RNA
- URL: https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
- DOI: 10.1261/rna.075580.120
- PMID: 32669294
- PMCID: 7566566
- Citations: 3
- Summary: Gene ontology analysis reveals an enrichment of genes related to translation, including mRNAs of ribosomal proteins, tRNAs, tRNA ligases, and t RNA-modifying enzymes, consistent with a key role of Hera in ribosome and tRNA metabolism.
- Evidence snippets:
  - Snippet 1 (score: 0.757)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [6] Genomic and Proteomic Characterization of the Deltamethrin-Degrading Bacterium Paracoccus sp. P-2
- Authors: Qing Li, Yawei Zhang, Xianfeng Ren, Qingguo Meng, Baocheng Xu et al.
- Year: 2025
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/74c0d94a67b8f801f8322fe976457dfd4c3fd76c
- DOI: 10.3390/microorganisms13112481
- PMID: 41304166
- PMCID: 12654547
- Summary: This study elucidates the impact of deltamethrin on bacterial metabolism and its degradation mechanism by Paracoccus sp.
- Evidence snippets:
  - Snippet 1 (score: 0.749)
    > To obtain comprehensive gene function information, we performed gene function annotation using eight major databases, including UniProt [23], KEGG [24] and KEGG Pathway, GO [25], Pfam [26], COG [27], TIGERfams [28], RefSeq, and NR. The predicted gene sequences were aligned against functional databases such as COG, KEGG, UniProt, and RefSeq using BLAST+ (Version: 2.11.0+), resulting in the gene function annotation outcomes. The statistical results of the annotations are shown in Table S2. Among the top 20 domains annotated based on Pfam, we observed that genes belonging to "ABC transporters" were the most abundant (Figure 2A). As we know, ABC transporters comprise a large superfamily of proteins that facilitate the translocation of a diverse array of substrates, including ions and macromolecules, across cellular membranes through ATP binding and hydrolysis. Furthermore, these transporters are also critically involved in the cellular uptake and efflux of numerous organic pollutants [29,30]. These results suggest that the abundance of ABC transporter genes provides Paracoccus sp. P-2 with a significant capacity for deltamethrin transport. As shown in Figure 2B, the genes annotated by KEGG are divided into 5 major categories and 23 minor subcategories. Among them, the subcategory with the largest number of genes is metabolic pathways, which include amino acid metabolism, carbohydrate metabolism, energy metabolism, metabolism of cofactors and vitamins, among others. The abundance of genes related to metabolic pathways provides the fundamental basis for the survival and deltamethrin degradation capability of Paracoccus sp. P-2. It is worth noting that a substantial number (254) of membrane transporter genes have been annotated in the genome of Paracoccus sp. P-2. Pollutants are often adsorbed onto the microbial membrane surface and subsequently internalized into the cells-a process in which membrane transporter proteins play a crucial role [31]. This abundance of transporter genes highlights the strain's strong capacity for pollutant transport.

### [7] Adaptation, Ecology, and Evolution of the Halophilic Stromatolite Archaeon Halococcus hamelinensis Inferred through Genome Analyses
- Authors: Reema K. Gudhka, B. Neilan, B. Burns
- Year: 2015
- Venue: Archaea
- URL: https://www.semanticscholar.org/paper/d650f910b391d57d43d94e5305e4902735d9f51f
- DOI: 10.1155/2015/241608
- PMID: 25709556
- PMCID: 4325475
- Citations: 29
- Summary: Characteristics reflecting its survival in its extreme environment were revealed, including putative genes/pathways involved in osmoprotection, oxidative stress response, and UV damage repair, and genome analyses indicated the presence of putative transposases as well as positive matches of genes of H. hamelinensis against various genomes of Bacteria, Archaea, and viruses, suggesting the potential for horizontal gene transfer.
- Evidence snippets:
  - Snippet 1 (score: 0.742)
    > H. hamelinensis whole cells indicated that the organism utilizes glucose, sucrose, xylose, maltose, trehalose, and glycerol as both single and complex carbon sources, in addition to  (gene ID: 2502301667) and NAD + synthetase (Gene ID: 2502298992, 2502299198, 2502299746). In addition to these enzymes, H. hamelinensis also possesses genes encoding three ABC transport proteins involving glutamine, namely, glutamine ABC transporter, periplasmic glutamine-binding protein (gene ID 2502298730), ABC-type glutamine/glutamate/polar amino acids transport system, permease protein (gene ID: 2502298731), and ABC-type glutamine/glutamate polar amino acids transport system, ATP-binding protein (gene ID: 2502298732).

### [8] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.739)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [9] Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype
- Authors: J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al.
- Year: 2022
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
- DOI: 10.1371/journal.pone.0273184
- PMID: 36256644
- PMCID: 9578583
- Citations: 4
- Influential citations: 1
- Summary: Background Ruminant livestock are a major contributor to Australian agricultural sector carbon emissions. Variation in methane (CH4) produced from enteric microbial fermentation of feed in the reticulo-rumen of sheep differs with different digestive functions. Method We isolated rumen epithelium enzymatically to extract membrane and cytosol proteins from sheep with high (H) and low (L) CH4 emission. Protein abundance was quantified using SWATH-mass spectrometry. Results The research found dif...
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > Protein identifications with 2 peptides and a confident protein score (P <0.05) from the HpH fractionation and IDA-MS were used to assign subcellular localization. Using the top score given by WoLF PSORT [10] (www.genscript.com/wolf-psort.html) proteins were categorized into 8 locations. Membrane proteins were predicted using transmembrane helical Markov model (TMHMM) [11] (www.cbs.dtu.dk/services/TMHMM/). Proteins in the solute carrier protein (SLC) and ATP-binding cassette (ABC) transporter families were identified according to gene and protein name. We also used website gene names (www.genenames.org/data) to characterise the subcellular location of the transporter and the type of substrate they transport.
    > For proteins annotated as 'uncharacterised' in figures and tables in the manuscript a BLAST protein homology search was carried out using the Ensembl or uniport accession code in uniprotKB (www.uniprot.org). The accession code page contains the sequence and a link to BLAST. BLASTp results against uniprotkb_Swissprot reference proteomes and an identity sequence match of >95.5% to human, bovine (cattle) or caprine (goat) proteome annotation was accepted as the protein name.

### [10] Syn Wiki: Functional annotation of the first artificial organism Mycoplasma mycoides JCVI‐syn3A
- Authors: Tiago Pedreira, Christoph Elfmann, Neil Singh, J. Stülke
- Year: 2021
- Venue: Protein Science : A Publication of the Protein Society
- URL: https://www.semanticscholar.org/paper/d9974c7fedefa8ec51f166d8546c8b0e819a7e14
- DOI: 10.1002/pro.4179
- PMID: 34515387
- PMCID: 8740822
- Citations: 11
- Summary: To gain a better understanding of the functions of the genes and proteins of the artificial bacteria, protein–protein interactions that may provide clues for the protein functions are included in an interactive manner.
- Evidence snippets:
  - Snippet 1 (score: 0.723)
    > Poorly characterized enzymes F I G U R E 4 Distribution of essentiality among all genes in SynWiki. While essential genes cannot be removed from the genome without loss of viability, the removal of quasi-essential genes results in an observable growth disadvantage 6 genes and 3 pseudogenes), making a total of 492 genes, resulting in better growth and improved stability.
    > In addition to the annotation in the original publications we also went through the literature, checked known functions of homologs, and searched for the availability of protein structures of the JCVI-syn3A proteins or their homologs from other organisms. All these results from manual data curation were added to the pages. Moreover, the curation of the pages is an ongoing process that will lead to ever-improved annotation and data presentation.
    > The success of a biological database strongly depends on the quality of annotation, and for those cases where there is poor or no annotation, we wanted to take a step forward and give our own contribution. With this in mind, and starting from the original annotation, we have also assigned each gene to one or more functional category. We took inspiration from GO term tree 14 and created a tree-like structure containing all functional categories. Currently, there are four major functional branches, "Cellular processes," "Group of genes," "Information processing" and "Metabolism," which then branch out into more specific categories (see here for an overview: http://synwiki.uni-goettingen.de/v1/category, and Table 1). For example, in "Cellular processes" it first branches out into "Cellular envelope and cell division," "Homeostasis," and "Transporters." Then, "Homeostasis" branches out into "Metal ion homeostasis" and "Coping with stress"; "Transporters" branch out into "ABC transporters," "ECF transporters," "Phosphotransferase system" and "Symporter." The "Group of genes" parent F I G U R E 5 Representation of protein homology analysis for PtsH. Results displayed in a table format for each organism used in this analysis with respective best potential homolog with UniProt link.

### [11] Exploration of the Potential of the ATP-Binding Cassette (ABC) Transporter Antigen as a Vaccine Candidate Against
- Authors: Salma Abdallah, Mervat A. Kassem, Nelly M. Mohamed, M. Bahey-El-Din
- Year: 2023
- Venue: Journal of Advanced Pharmacy Research
- URL: https://www.semanticscholar.org/paper/58d3fd58dae0a8e2caf8473c4f60be5dcea04c57
- DOI: 10.21608/aprh.2023.177396.1202
- Citations: 1
- Summary: The diversity of the virulence factors exhibited by A. baumannii including several iron acquisition mechanisms might necessitate the design of a multi-component vaccine to elicit effective protection.
- Evidence snippets:
  - Snippet 1 (score: 0.720)
    > Following the bioinformatic analysis of the gene encoding ABC transporter substrate-binding protein, the first 31 amino acids were recognized as signal peptide (SP) and their corresponding coding sequences were omitted during the forward primer design. The target gene was successfully PCR-amplified where agarose gel electrophoresis displayed the gene under investigation as a single band at its expected size (1728 bp) as shown in Figure 1 (lane 1). The gene was then cloned in pQE31 plasmid vector, and subsequently transformed into E. coli M15 (pREP4) expression host (Figure 1, lane 2). Sequencing analysis (Supplementary file S1) confirmed the sequence and identity of the gene encoding ABC transporter substrate-binding protein of A. baumannii. Following protein induction with IPTG, SDS-PAGE demonstrated successful protein expression in E. coli M15 (pREP4) host where the protein appeared as a pure band at its expected size (65 kDa) following Ni-NTA metal affinity chromatography (Figure 2).

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
  - Snippet 1 (score: 0.719)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [13] ‘Ca. Liberibacter asiaticus’ Proteins Orthologous with pSymA-Encoded Proteins of Sinorhizobium meliloti: Hypothetical Roles in Plant Host Interaction
- Authors: L. Kuykendall, J. Shao, J. Hartung
- Year: 2012
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/d1903bab3348459a5230cb86962e8df123d9be22
- DOI: 10.1371/journal.pone.0038725
- PMID: 22761700
- PMCID: 3382624
- Citations: 8
- Summary: The presence of multiple orthologs defies mutational analysis and is consistent with the hypothesis that these proteins may be of particular importance in host/microbe interaction and their duplication likely facilitates their ongoing evolution.
- Evidence snippets:
  - Snippet 1 (score: 0.715)
    > ATP Binding Cassette type amino acid transporters comprise the largest class of genes shared by 'Ca. Liberibacter asiaticus', pSymA and the S. meliloti chromosome (Table 2). For most ABCtype transporter proteins encoded by 'Ca. Liberibacter asiaticus' genes there are multiple homologs on pSymA, dispersed over the megaplasmid (Table S1). YP_003064586 is an example of an ABC-type transporter protein from 'Ca. Liberibacter asiaticus'. In addition to NP_435288.1 there are 10 more pSymA-encoded proteins homologous to YP_003064586 (E = 4e-67 up to 1e-14), and all are annotated as general amino acid transporters with an ATP binding site and other characteristics of an ABC type amino acid transporter. The corresponding genes are dispersed across the pSymA (Fig. 1A; Table 2).
    > YP_003064753 is a proline/glycine betaine ABC transporter protein with eight pSymA-encoded homologs (Table S1). YP_003064754, another proline/glycine betaine permease/ABC transporter permease protein, has two pSymA-encoded homologs. 'Ca. Liberibacter asiaticus' YP_003065117 and YP_003064552, both ATP-binding ABC-type transporter proteins, each have four homologs encoded by genes on pSymA. YP_003065525, a putative amino acid-binding periplasmic protein, is homologous to two pSymA-encoded predicted proteins. YP_003065526, an ABC-type amino acid transporter permease, has 7 homologs encoded by pSymA genes. These are examples of multiple, redundant shared homologs of ABC-type amino acid transport systems encoded by pSymA. 'Ca.

### [14] Environment sensing and response mediated by ABC transporters
- Authors: Sarah E. Giuliani, A. Frank, Danielle M. Corgliano, Catherine Seifert, L. Hauser et al.
- Year: 2011
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/cc4616ae2df0e74a413ae71b9560d956107ef0c5
- DOI: 10.1186/1471-2164-12-S1-S8
- PMID: 21810210
- PMCID: 3223731
- Citations: 65
- Influential citations: 2
- Summary: The functional screen identified specific ligands that bound to ABC transporter periplasmic binding subunits from R. palustris that provide unique insight for the metabolic capabilities of this organism and are consistent with the ecological niche of strain isolation.
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > Three proteins (RPA2499, RPA2628, and RPA3810) were identified as amino acid binding proteins via the FTS screening (Table 1). This observation is consistent with the assigned annotation and the general functional prediction of TransportDB (Table 2). The set of binding proteins specific for amino acids provide transport capabilities for seven of the individual amino acids. The genes encoding the RPA2628 (PBP), RPA2629 and RPA2630 (integral membrane subunits) (methionine/ cysteine/histidine) are orthologs of a verified amino acid transporter in Rhizobium leguminosarum [32]. They are also localized in a cluster of 10 ABC transporter proteins containing four periplasmic binding proteins (three screened by FTS assay, Additional file 1) and RPA2628 was the only protein with specific ligand binding. The characterized set of binding proteins reflects an emphasis on maintenance of sulfate and nitrogen stores. RPA2499, annotated as an arginine binding protein, is adjacent to an "amidase" gene. Asparagine has a N:C ratio of 2:4, which makes it an efficient molecule for the storage and transport of nitrogen.

### [15] Genomic and metabolomic insights into the antimicrobial compounds and plant growth-promoting potential of Bacillus velezensis Q-426
- Authors: Lulu Wang, Ruochen Fan, Haodi Ma, Yu Sun, Yang Huang et al.
- Year: 2023
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/dafda64a4e7dbdc0906aa66bc17fd6ee5856514c
- DOI: 10.1186/s12864-023-09662-1
- PMID: 37794314
- PMCID: 10548584
- Citations: 30
- Influential citations: 2
- Summary: This study laid the theoretical foundation for the development of secondary metabolites and the application of B. velezensis Q-426 as a plant growth-promoting strain in ecological agriculture.
- Evidence snippets:
  - Snippet 1 (score: 0.711)
    > These proteins accounted for 9.20% and 8.66% of the total protein sequences, respectively. The annotation results suggested that 119 genes participated in secondary metabolite biosynthesis, transport, and catabolism. As expected, the lipopeptides including surfactin, iturin, and fengycin gene clusters, were found in the genome sequence of Q-426.
    > In the present study, we used the InterProScan database [25] to predict all of the protein domains and functional sites of B. velezensis Q-426 and extract the information of GO [26,27]. Based on the GO functional annotation shown in Fig. 3, the identified proteins were classified into 3 large groups, including biological process, cellular components, and molecular functions. The results suggested that the proteins were annotated into 48 functional groups, including 26 biological processes, 12 cellular components, and 10 molecular functions (Fig. 3). In biological processes, the proteins were mainly involved in metabolic processes (1746 genes), cellular processes (1689 genes), and localization (624 genes). In cellular components, the proteins were mainly involved in cell (1135 genes), cell part (1135 genes), and organelle (225 genes). In molecular functions, the proteins were mainly involved in catalytic activity (1723 genes), binding (1391 genes), and transporter activity (286 genes).
    > The genes involved in the metabolic pathways were analyzed statistically using the KEGG analysis tool in the genome sequence of B. velezensis Q-426 [28]. The KEGG analysis results showed that the proteins were annotated to 36 KEGG pathways, classified into 6 large groups, including cellular processes (163 genes), environmental information processing (300 genes), genetic information processing (185 genes), human diseases (77 genes), metabolism (887 genes), and organismal systems (34 genes) (Fig. 4). Carbohydrate metabolism pathways (187 genes) and membrane transport (171 genes) were the primary enriched pathways, followed by amino acid metabolism (162 genes). The KEGG database analysis showed a great number of two-component systems (114 genes) and ABC transporters (135 genes).

### [16] MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data
- Authors: Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang
- Year: 2010
- Venue: Journal of Biomedicine and Biotechnology
- URL: https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
- DOI: 10.1155/2009/642524
- PMID: 20169000
- PMCID: 2822236
- Citations: 18
- Influential citations: 1
- Summary: By applying the MIClique algorithm to real gene expression data, some DEC gene subsets which correlated under one experimental condition but uncorrelated under another condition are detected from the graph of colon dataset and leukemia dataset.
- Evidence snippets:
  - Snippet 1 (score: 0.711)
    > Table 3 lists the Genbank accession number, the gene symbols, accession number in UniProtKB (UniProt Knowledgebase), and gene descriptions given by colon data. The UniProtKB is the central hub for the collection of information on proteins such as amino acid sequence, protein name or description, taxonomic data, and biological ontology [24]. Figure 6 depicts gene expression profiles of the eight genes in normal and disease samples. As shown in Figure 6, the profiles of these genes are highly coexpressed in normal samples (samples 1-22) while the coexpression pattern disappears in disease samples (samples 23-62).

### [17] The ultra-high affinity transport proteins of ubiquitous marine bacteria
- Authors: B. Clifton, Uria Alcolombri, Gen-Ichiro Uechi, C. Jackson, P. Laurino
- Year: 2024
- Venue: Nature
- URL: https://www.semanticscholar.org/paper/e261e726c69c86a4cf2bc4cd049a0931df48f585
- DOI: 10.1038/s41586-024-07924-w
- PMID: 39261732
- PMCID: 11485210
- Citations: 25
- Influential citations: 1
- Summary: Genome-wide characterization of solute-binding proteins in SAR11, a group of ubiquitous marine bacteria, reveals that they generally combine high binding affinities with narrow binding specificities, suggesting a molecular mechanism for the adaptation of SAR11 to diverse marine environments.
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > Nineteen candidate SBP genes in the genome of Ca. P. ubique strain HTCC1062 were identified through a search of the TransportDB 2.0 database 59 (http://membranetransport.org; accessed 22 January 2020). One of these genes, SAR11_0371, was annotated as a 'possible transmembrane receptor' in UniProt and showed a non-canonical predicted domain structure consisting of a short SBP-like domain (170 amino acids) followed by a coiled coil domain and unidentified C-terminal domain. Additionally, genome context analysis showed that, unlike the other ABC SBP genes in Ca. P. ubique HTCC1062, SAR11_0371 was not colocalized with genes encoding the membrane permease or ATP-binding cassette components of an ABC transport system. Thus, SAR11_0371 was considered not to represent the SBP component of an SBP-dependent transport system and was excluded from the analysis. We also attempted to identify additional SBP genes through a search of the UniProt database for proteins in Ca. P. ubique belonging to Pfam clans CL0177 (PBP; periplasmic binding protein) and CL0144 (Periplas_BP; periplasmic binding protein like); however, this search did not return any additional candidate genes.

### [18] Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B
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
  - Snippet 1 (score: 0.709)
    > 2.8.1. Annotation methods 2.8.1.1. Functional annotation. UniProt-GOA database was utilized to retrieve Gene Ontology (GO) annotation proteome. First, the identified protein identity was converted to UniProt identity and then mapped to GO identity based on the protein identity. When the identified protein was not annotated by UniProt-GOA, the functional annotation of that protein was conducted using the InterProScan software according to the amino acid sequence alignment approach. All proteins were then classified into 3 groups: molecular function, cellular component and biological process.

### [19] Genome-wide Identification of conditionally essential genes supporting Streptococcus suis growth in serum and cerebrospinal fluid
- Authors: Maria Juanpere-Borràs, Tiantong Zhao, Jos Boekhorst, Blanca Fernandez-Ciruelos, Rajrita Sanyal et al.
- Year: 2025
- Venue: Virulence
- URL: https://www.semanticscholar.org/paper/400884affc80cbd5eef1e69b6961748a60a5b400
- DOI: 10.1080/21505594.2025.2600145
- PMID: 41396007
- PMCID: 12707516
- Citations: 1
- Summary: Using Tn-Seq coupled with Nanopore sequencing to identify conditionally essential genes for growth of S. suis provides new insights into the genetic requirements for S. suis survival in host-like environments and a deeper understanding of its ability to adapt to distinct physiological niches.
- Evidence snippets:
  - Snippet 1 (score: 0.704)
    > Gene SSU_RS04755 has been predicted to encode a basic membrane family protein (BMP), a transmembrane component of specific ABC transporters. Growth curve experiments did not reveal a significant reduction in the growth rate of our ΔSSU_RS04755 mutant. The operon genes with SSU_RS04755 were predicted to encode an ATPbinding protein and a permease which are typical components of an ABC transporter. Both predicted ATPbinding protein and permease encoding genes appeared as CEGs in our Tn-seq results (Table 1). The protein sequence associated with SSU_RS04755 shares significant identity with lipoproteins that are components of nucleoside ABC transporters in Gram-positive bacteria (see above), suggesting that SSU_RS04755 and its operon genes may encode an ABC transporter complex involved in nucleoside transport. To investigate the possible functional equivalence of SSU_RS04755 operon genes with ABC transporters, we performed amino acid sequence alignments of SSU_RS04755 with PnrA and TmpC, which are homologous nucleoside binding lipoproteins from S. pneumoniae and Treponema pallidum (T. pallidum) respectively [49,50]. Using the crystal structure of PnrA binding to adenosine [49], we confirmed that all but one (T70) of the specific amino acids involved in adenosine binding by PnrA were conserved in SSU_RS04755 (Figure 5(c)).
    > To verify if the structural positions of these amino acids were conserved, we performed a structural prediction (see methods) of the predicted S. suis lipoprotein SSU_RS04755 and aligned it to the structure of PnrA (ID 6y9U in Protein Data Bank (PDB). We confirmed that all amino acids involved in the adenosine binding are located at the same position in both protein structures.

### [20] Evaluation of Proteins Released to Medium in Yeast-Bacteria Co-culture System
- Authors: Ayşegül Yanik, Ç. Tarhan
- Year: 2023
- Venue: Journal of Advanced Research in Natural and Applied Sciences
- URL: https://www.semanticscholar.org/paper/bf1e6e710a760d61cdce04ea82c683106fe2ad6d
- DOI: 10.28979/jarnas.1196962
- Summary: The wild strain of Schizosaccharomyces pombe and the DH5α strain of Escherichia coli were grown in their own specific media, then cultured for 48 hours and 72 hours by cultivating in media containing 0,1% glucose with different cell number, and finally the differentiation in the proteins released by the cells into the medium was observed in SDS polyacrylamide gels.
- Evidence snippets:
  - Snippet 1 (score: 0.704)
    > The proteins identified as a result of LC-MS/MS analysis were evaluated in UniProt and the names and functions of the proteins are given as an appendix. Here, 6 protein-coding genes in the bands of the proteins released into the medium by the co-culture were found in the S.pombe genome and were classified according to their biological functions and cellular locations using the online platform PANTHER (Figure 2). Other 257 protein-coding genes were found in the E. coli genome. These proteins were also classified according to their cellular location (Figure 3) and their cellular functions (Figure 4). Maltose/maltodextrin-binding periplasmic protein (malE) and D-galactose-binding periplasmic protein (mglB) found in E. coli cells are among the binding proteins found in LC-MS-MS results. The binding protein MglB has a high affinity for glucose (Ferenci, 1996), and at low glucose concentration, glucose is mainly taken up by cells in this way. In a study by Egli et al. (1993), giving 1.8 mg l−1 galactose to a low glucose-containing E. coli culture decreased the glucose utilization of the cells and led to glucose accumulation in continuous culture. In addition, Hua and., (2004) found that the expression of a series of genes encoding membrane transporter proteins was significantly induced in cultures of limited chemostats for various carbon sources, and that about half of these genes were maltose (all genes of malGFE and malK-lamB-malM operons), galactose. They showed that there are genes involved in a wide variety of high-affinity ABC transport systems that facilitate uptake (three genes of the mglBAC operon). In E. coli, the ABC transporter gene family covers approximately 5% of the entire genome (Linton and Higgins, 1998). This shows how important these genes are. Carbon-limited cultures have been proposed to investigate bacterial growth and behavior under environmental conditions (Matin, 1979;Moriarty, 1993;Morita, 1993).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. H. Hao, Fei Li, Jing Han, S. Foley, Menghong Dai et al. (2017). Cj1199 Affect the Development of Erythromycin Resistance in Campylobacter jejuni through Regulation of Leucine Biosynthesis. Frontiers in Microbiology. https://www.semanticscholar.org/paper/9152e27a908296795b4779c02d4aa02ffae2f388
4. H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim (2023). FusionPDB: a knowledgebase of human fusion proteins. Nucleic Acids Research. https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
5. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
6. Qing Li, Yawei Zhang, Xianfeng Ren, Qingguo Meng, Baocheng Xu et al. (2025). Genomic and Proteomic Characterization of the Deltamethrin-Degrading Bacterium Paracoccus sp. P-2. Microorganisms. https://www.semanticscholar.org/paper/74c0d94a67b8f801f8322fe976457dfd4c3fd76c
7. Reema K. Gudhka, B. Neilan, B. Burns (2015). Adaptation, Ecology, and Evolution of the Halophilic Stromatolite Archaeon Halococcus hamelinensis Inferred through Genome Analyses. Archaea. https://www.semanticscholar.org/paper/d650f910b391d57d43d94e5305e4902735d9f51f
8. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
9. J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al. (2022). Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype. PLoS ONE. https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
10. Tiago Pedreira, Christoph Elfmann, Neil Singh, J. Stülke (2021). Syn Wiki: Functional annotation of the first artificial organism Mycoplasma mycoides JCVI‐syn3A. Protein Science : A Publication of the Protein Society. https://www.semanticscholar.org/paper/d9974c7fedefa8ec51f166d8546c8b0e819a7e14
11. Salma Abdallah, Mervat A. Kassem, Nelly M. Mohamed, M. Bahey-El-Din (2023). Exploration of the Potential of the ATP-Binding Cassette (ABC) Transporter Antigen as a Vaccine Candidate Against. Journal of Advanced Pharmacy Research. https://www.semanticscholar.org/paper/58d3fd58dae0a8e2caf8473c4f60be5dcea04c57
12. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
13. L. Kuykendall, J. Shao, J. Hartung (2012). ‘Ca. Liberibacter asiaticus’ Proteins Orthologous with pSymA-Encoded Proteins of Sinorhizobium meliloti: Hypothetical Roles in Plant Host Interaction. PLoS ONE. https://www.semanticscholar.org/paper/d1903bab3348459a5230cb86962e8df123d9be22
14. Sarah E. Giuliani, A. Frank, Danielle M. Corgliano, Catherine Seifert, L. Hauser et al. (2011). Environment sensing and response mediated by ABC transporters. BMC Genomics. https://www.semanticscholar.org/paper/cc4616ae2df0e74a413ae71b9560d956107ef0c5
15. Lulu Wang, Ruochen Fan, Haodi Ma, Yu Sun, Yang Huang et al. (2023). Genomic and metabolomic insights into the antimicrobial compounds and plant growth-promoting potential of Bacillus velezensis Q-426. BMC Genomics. https://www.semanticscholar.org/paper/dafda64a4e7dbdc0906aa66bc17fd6ee5856514c
16. Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang (2010). MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data. Journal of Biomedicine and Biotechnology. https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
17. B. Clifton, Uria Alcolombri, Gen-Ichiro Uechi, C. Jackson, P. Laurino (2024). The ultra-high affinity transport proteins of ubiquitous marine bacteria. Nature. https://www.semanticscholar.org/paper/e261e726c69c86a4cf2bc4cd049a0931df48f585
18. Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al. (2022). Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B. Data in Brief. https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
19. Maria Juanpere-Borràs, Tiantong Zhao, Jos Boekhorst, Blanca Fernandez-Ciruelos, Rajrita Sanyal et al. (2025). Genome-wide Identification of conditionally essential genes supporting Streptococcus suis growth in serum and cerebrospinal fluid. Virulence. https://www.semanticscholar.org/paper/400884affc80cbd5eef1e69b6961748a60a5b400
20. Ayşegül Yanik, Ç. Tarhan (2023). Evaluation of Proteins Released to Medium in Yeast-Bacteria Co-culture System. Journal of Advanced Research in Natural and Applied Sciences. https://www.semanticscholar.org/paper/bf1e6e710a760d61cdce04ea82c683106fe2ad6d