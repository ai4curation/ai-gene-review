---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T20:53:08.917086'
end_time: '2026-07-08T20:53:15.793553'
duration_seconds: 6.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2750
  gene_symbol: PP_2750
  uniprot_accession: Q88J99
  protein_description: 'SubName: Full=Branched-chain amino acid ABC transporter, permease
    protein {ECO:0000313|EMBL:AAN68358.1};'
  gene_info: OrderedLocusNames=PP_2750 {ECO:0000313|EMBL:AAN68358.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ABC_transp_permease. (IPR001851); LivM-like. (IPR043428); BPD_transp_2
    (PF02653)
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
- **UniProt Accession:** Q88J99
- **Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, permease protein {ECO:0000313|EMBL:AAN68358.1};
- **Gene Information:** OrderedLocusNames=PP_2750 {ECO:0000313|EMBL:AAN68358.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ABC_transp_permease. (IPR001851); LivM-like. (IPR043428); BPD_transp_2 (PF02653)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2750" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2750' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2750** (gene ID: PP_2750, UniProt: Q88J99) in PSEPK.

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
  - Snippet 1 (score: 0.806)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

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

### [3] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.783)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [4] Proteomic profiling of regenerated urinary bladder tissue with stem cell seeded scaffold composites in a non-human primate bladder augmentation model
- Authors: Tiffany T. Sharma, S. Edassery, N. Rajinikanth, Vikram Karra, Matthew I. Bury et al.
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/6446e5bc8c0ec1aa0836a711b705ebafa66bd5c8
- DOI: 10.1101/2023.08.29.554824
- PMID: 37693577
- PMCID: 10491202
- Citations: 1
- Summary: Autologous, bone marrow derived mesenchymal stem cells along with primitive hematopoietic stem/progenitor cells can be used to regenerate bladder tissue in a large deficit, non-human primate bladder augmentation model and facilitates the promotion of a protein tissue landscape that is nearly identical to native bladder tissue.
- Evidence snippets:
  - Snippet 1 (score: 0.762)
    > Raw data were analyzed using Proteome Discoverer 2.5 (Thermo Fisher Scientific) using the "PWF Tribrid TMTpro Quan SPS MS3 SequestHT Percolator" and "CWF Comprehensive Enhanced Annotation Reporter
    > Quan" methods implemented in the PD2.For uncharacterized proteins or proteins with unknown function presented in the manuscript, the UniProt Accession number was search against UniProt database https://www.uniprot.org/and the NCBI Gene database https://www.ncbi.nlm.nih.gov/gene/.If required, more information was obtained with regards to protein identity by matching the amino acid sequence of the protein on the NCBI BLAST alignment program https://blast.ncbi.nlm.nih.gov/Blast.cgi .

### [5] MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data
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
  - Snippet 1 (score: 0.751)
    > Table 3 lists the Genbank accession number, the gene symbols, accession number in UniProtKB (UniProt Knowledgebase), and gene descriptions given by colon data. The UniProtKB is the central hub for the collection of information on proteins such as amino acid sequence, protein name or description, taxonomic data, and biological ontology [24]. Figure 6 depicts gene expression profiles of the eight genes in normal and disease samples. As shown in Figure 6, the profiles of these genes are highly coexpressed in normal samples (samples 1-22) while the coexpression pattern disappears in disease samples (samples 23-62).

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
  - Snippet 1 (score: 0.743)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [7] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
- Authors: Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al.
- Year: 2015
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
- DOI: 10.1186/s12864-015-2287-5
- PMID: 26692227
- PMCID: 4687164
- Citations: 69
- Influential citations: 2
- Summary: A revised manually curated full genome sequence for Clostridium autoethanogenum DSM10061 is presented, which provides reliable information for genome-scale models that rely heavily on the accuracy of annotation, and represents an important step towards the manipulation and metabolic modelling of this industrially relevant acetogen.
- Evidence snippets:
  - Snippet 1 (score: 0.740)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [8] Combining of transcriptome and metabolome analyses for understanding the utilization and metabolic pathways of Xylo‐oligosaccharide in Bifidobacterium adolescentis ATCC 15703
- Authors: Jian Yang, Qilong Tang, Lei Xu, Zhijiang Li, Yongqiang Ma et al.
- Year: 2019
- Venue: Food Science & Nutrition
- URL: https://www.semanticscholar.org/paper/a1dc16e9f5c2615024cf1c7cb6bc2e2d3a63a626
- DOI: 10.1002/fsn3.1194
- PMID: 31762999
- PMCID: 6848847
- Citations: 28
- Influential citations: 1
- Summary: The transcriptome analysis showed that XOS could enhance genes, including ABC transporters, galactosidase, xylosid enzyme, glucosidases, and amylase, which were involved in transport and metabolism of carbohydrate compared with xylose, which contributed to the optimization of XOS probiotic effects as a food additive.
- Evidence snippets:
  - Snippet 1 (score: 0.733)
    > From the RNA-seq analysis data, it can be seen that over 99% of the reads were aligned to encoding regions of the B. adolescentis.
    > Genes were assigned to 25 functional groups, which were annotated in COG database (Figure 2). Among these classifications, the largest group was amino acid transport and metabolism (191, 13.45%), followed by carbohydrate transport and metabolism (160, 11.27%) and general function prediction (151, 10.63%).
    > A total number of 302 DEGs were identified for B. adolescentis grown on xylose and XOS, including 158 upregulated genes and 144 downregulated genes (Figure 3). The top 10 upregulated genes and 10 downregulated genes of xylose and XOS treatments are presented in Table 2. Four genes of the top 10 upregulated genes encode ABC and MFS transporters. Among the remaining genes, two genes encode hsp20/alpha crystallin family protein and ATP-dependent chaperone ClpB, two genes encode RNA polymerase sigma factor and death-on-curing protein, other two genes encode enzyme proteins belonging to multiple sugar-binding transport system permease and shikimate kinase. Five genes of the top 10 downregulated genes encode structure protein, including penicillin-binding protein, von willebrand factor type A domain protein, fhiA protein, arginine repressor DUF4956, domain-containing protein, three genes are associated with membrane transport, including peptide ABC transporter ATP-binding protein, ABC transporter permease, and membrane spanning polysaccharide biosynthesis protein, while two genes encode O-antigen polymerase and hypothetical protein.

### [9] Establishing comprehensive quaternary structural proteomes from genome sequence
- Authors: Nathan Mih, M. Lu, B. Palsson, E. Catoiu
- Year: 2023
- Venue: Research Square
- URL: https://www.semanticscholar.org/paper/bf3821f3fcaef0b354e05b3332a155278a721316
- DOI: 10.21203/rs.3.rs-2923626/v1
- PMID: 37292890
- PMCID: 10246253
- Citations: 4
- Summary: A computational platform is developed that can resolve genome-scale structural proteomes to obtain an angstrom-level understanding of whole-cell functions and obtains a draft 3D visualization of the proteome in a functioning cell.
- Evidence snippets:
  - Snippet 1 (score: 0.727)
    > Blattner numbers were used to obtain gene-level subcellular information from UniProt topological annotation, EcoCyc compartment annotation, Gene Ontology (GO) terms relating to the membrane, and subcellular compartments in genome-scale model iML1515 36 .
    > Presence of annotated sequence features related to the membrane (TOPO_DOM, TRANSMEM, INTRAMEM) were used to identify potential membrane genes with UniProt. Genes containing membrane-related keywords ('membrane', 'transport', 'abc', 'wall' and 'periplasm') among their gene ontology (GO) terms were identified as potential membrane genes. These GO terms were scraped from the uniport text file for each gene. Genes containing membrane-related keywords ('membrane', 'periplas', 'transport', 'secretion', 'extracellular' and 'wall') found in the "Locations'' column of the EcoCyc public SmartTable "All genes of E. coli K-12 substr. MG1655" were tagged to the membrane. Membrane-related keywords ('membrane', 'transport', 'abc', 'wall', 'periplasm', 'envelope' and 'murein') in the gene-protein-reaction (GPR) relationships from genome-scale model iML1515 were used to identify potential membrane genes.
    > Once the complete set of all potential membrane genes was determined, a set of protein structures selected by QSPACE whose subunits consisted of at least one membrane gene were identified as potential membrane structures (Fig. 3a). This set of structures was analyzed further to confirm membrane embeddedness.
    > Identification of membrane-embedded and membrane-crossing residues.
    > Membrane-embedded residues are used to define amino acids in between the two membrane leaflets. Membrane-crossing residues are used to define amino acids that are at the surface of membrane leaflets.
    > The membrane-embedded and membrane-crossing residues were identified using the sequence-based topological annotation provided in UniProt, a sequence-based prediction using DeepTMHMM 40 , a structure-based prediction using OPM 41 .

### [10] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.726)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [11] Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype
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

### [12] Extensive Inter-Domain Lateral Gene Transfer in the Evolution of the Human Commensal Methanosphaera stadtmanae
- Authors: M. Lurie-Weinberger, Michael Peeri, T. Tuller, U. Gophna
- Year: 2012
- Venue: Frontiers in Genetics
- URL: https://www.semanticscholar.org/paper/d34372c95ea31abaa75d4248b82c50cace6acaa1
- DOI: 10.3389/fgene.2012.00182
- PMID: 23049536
- PMCID: 3445992
- Citations: 17
- Summary: Bacterial genes contributed to the adaptation of M. stadtmanae to a host-dependent lifestyle by allowing a larger variation in surface structures and increasing transport efficiency in the gut niche which is diverse and competitive.
- Evidence snippets:
  - Snippet 1 (score: 0.720)
    > Genes with low ENC (Values under 28.49, lower by more than 2 S.D) included the gene ThiM1, a nitroreductase, a nitrate/sulfonate/bicarbonate ABC transporter permease, a polar amino acid ABC transporter periplasmic substrate-binding protein, a transcriptional regulator, and two hypothetical proteins. On the other end of the spectrum, genes with high ENC values (values over 40.0, higher by more than two standard deviations) include a d-tyrosyl-tRNA (Tyr) deacylase, a putative secreted RNase (barnase), and three hypothetical proteins (see Table S2 in Supplementary Material).
    > Generally, CAI values showed the same trend as the ENC data (mean CAI of 0.72 for genes acquired from bacteria vs. a general CAI mean of 0.73), both implying that transferred genes are now highly ameliorated (see Table S2 in Supplementary Material). CAI values varied greatly among laterally transferred genes, ranging between 0.55 and 0.87. Genes with low CAI values (Values under 0.61, lower by more than 2 S.D) included an ATPase, a polar amino acid ABC transporter permease, an exopolysaccharide synthesis protein, a phosphohydrolase, and three hypothetical proteins (see Table S2 in Supplementary Material). Genes with high CAI values (values over 0.84, higher by more than 2 S.D) include a desulfoferrodoxin and ferredoxin, asn/thr-rich large protein family protein, glutamate dehydrogenase, a short chain dehydrogenase, the gene LeuD1 (a member of the Leucine biosynthetic process), ThiM1 (a member of the Thiamine biosynthesis process), and three hypothetical proteins (see Table S2 in Supplementary Material). Such high CAI values indicate high expression levels of these proteins, testifying to their functional importance.

### [13] Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes
- Authors: Shikai Liu, Qi Li, Zhanjiang Liu
- Year: 2013
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/427dc24364271d57abe57d9efe0b1ebfc116d51c
- DOI: 10.1371/journal.pone.0063895
- PMID: 23696857
- PMCID: 3655950
- Citations: 63
- Influential citations: 7
- Summary: A set of 50 ABC transporters in catfish genome is identified and identified into seven subfamilies, providing the essential genomic resources for future biochemical, toxicological and physiological studies of ABC drug effluxtransporters.
- Evidence snippets:
  - Snippet 1 (score: 0.718)
    > Background Although a large set of full-length transcripts was recently assembled in catfish, annotation of large gene families, especially those with duplications, is still a great challenge. Most often, complexities in annotation cause mis-identification and thereby much confusion in the scientific literature. As such, detailed phylogenetic analysis and/or orthology analysis are required for annotation of genes involved in gene families. The ATP-binding cassette (ABC) transporter gene superfamily is a large gene family that encodes membrane proteins that transport a diverse set of substrates across membranes, playing important roles in protecting organisms from diverse environment. Methodology/Principal Findings In this work, we identified a set of 50 ABC transporters in catfish genome. Phylogenetic analysis allowed their identification and annotation into seven subfamilies, including 9 ABCA genes, 12 ABCB genes, 12 ABCC genes, 5 ABCD genes, 2 ABCE genes, 4 ABCF genes and 6 ABCG genes. Most ABC transporters are conserved among vertebrates, though cases of recent gene duplications and gene losses do exist. Gene duplications in catfish were found for ABCA1, ABCB3, ABCB6, ABCC5, ABCD3, ABCE1, ABCF2 and ABCG2. Conclusion/Significance The whole set of catfish ABC transporters provide the essential genomic resources for future biochemical, toxicological and physiological studies of ABC drug efflux transporters. The establishment of orthologies should allow functional inferences with the information from model species, though the function of lineage-specific genes can be distinct because of specific living environment with different selection pressure.

### [14] Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae
- Authors: Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli
- Year: 2021
- Venue: BMC Research Notes
- URL: https://www.semanticscholar.org/paper/4f78acee7559d5e406bacad91d5982d9f3244ea3
- DOI: 10.1186/s13104-021-05856-6
- PMID: 34823574
- PMCID: 8620141
- Citations: 10
- Summary: To identify candidate genes likely involved in complementation of mef( A) deletion, the Mef(A) amino acid sequence was used as probe for database searching and identified 3 putative candidates in the S. pneumoniae R6 genome, namely spr0971, spr1023 and spr1932.
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > The 405-aa Mef(A) sequence (GenBank accession no. AAT72347) was used as a query to conduct a BLAST homology search of S. pneumoniae R6 genome. Homology analysis revealed the presence of three genes coding for proteins with a significant homology (e-value < 0.001) to Mef(A): (i) spr0971 (GenBank accession number NP_ 358565.1); (ii) spr1023 (GenBank accession number NP_ 358617.1); (iii) spr1932 (GenBank accession number NP_ 359523.1). The spr0971 gene, annotated as "ABC transporter membrane-spanning permease-macrolide efflux", codes for a 403 aa protein displaying 23% identity to Mef(A). The spr1023 gene, annotated as "macrolide ABC transporter permease", codes for a 392 aa protein with 24% identity to Mef(A). The spr1932 gene, annotated as "hypothetical protein", codes for a 415 aa protein with 21% identity to Mef(A). Analysis of the transmembrane domains of all deduced amino acid products predicted the presence of up to 12 transmembrane helices.

### [15] Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae
- Authors: Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli
- Year: 2021
- Venue: BMC Research Notes
- URL: https://www.semanticscholar.org/paper/f30df2b539544c70ac0c1f373b0235d4e92d7687
- DOI: 10.1186/s13104-021-05856-6
- Summary: In streptococci, the type M resistance to macrolides is due to the mef(A)–msr(D) efflux transport system of the ATP-Binding cassette (ABC) superfamily, where it is proposed that mef(A) codes for the transmembrane channel and msr(D) for the two ATP-binding domains. Phage ϕ1207.3 of Streptococcus pyogenes, carrying the mef(A)–msr(D) gene pair, is able to transfer the macrolide efflux phenotype to Streptococcus pneumoniae. Deletion of mef(A) in pneumococcal ϕ1207.3-carrying strains did not affec...
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > The 405-aa Mef(A) sequence (GenBank accession no. AAT72347) was used as a query to conduct a BLAST homology search of S. pneumoniae R6 genome. Homology analysis revealed the presence of three genes coding for proteins with a significant homology (e-value < 0.001) to Mef(A): (i) spr0971 (GenBank accession number NP_ 358565.1); (ii) spr1023 (GenBank accession number NP_ 358617.1); (iii) spr1932 (GenBank accession number NP_ 359523.1). The spr0971 gene, annotated as "ABC transporter membrane-spanning permease-macrolide efflux", codes for a 403 aa protein displaying 23% identity to Mef(A). The spr1023 gene, annotated as "macrolide ABC transporter permease", codes for a 392 aa protein with 24% identity to Mef(A). The spr1932 gene, annotated as "hypothetical protein", codes for a 415 aa protein with 21% identity to Mef(A). Analysis of the transmembrane domains of all deduced amino acid products predicted the presence of up to 12 transmembrane helices.

### [16] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.715)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [17] Genome-wide Identification of conditionally essential genes supporting Streptococcus suis growth in serum and cerebrospinal fluid
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
  - Snippet 1 (score: 0.713)
    > Gene SSU_RS04755 has been predicted to encode a basic membrane family protein (BMP), a transmembrane component of specific ABC transporters. Growth curve experiments did not reveal a significant reduction in the growth rate of our ΔSSU_RS04755 mutant. The operon genes with SSU_RS04755 were predicted to encode an ATPbinding protein and a permease which are typical components of an ABC transporter. Both predicted ATPbinding protein and permease encoding genes appeared as CEGs in our Tn-seq results (Table 1). The protein sequence associated with SSU_RS04755 shares significant identity with lipoproteins that are components of nucleoside ABC transporters in Gram-positive bacteria (see above), suggesting that SSU_RS04755 and its operon genes may encode an ABC transporter complex involved in nucleoside transport. To investigate the possible functional equivalence of SSU_RS04755 operon genes with ABC transporters, we performed amino acid sequence alignments of SSU_RS04755 with PnrA and TmpC, which are homologous nucleoside binding lipoproteins from S. pneumoniae and Treponema pallidum (T. pallidum) respectively [49,50]. Using the crystal structure of PnrA binding to adenosine [49], we confirmed that all but one (T70) of the specific amino acids involved in adenosine binding by PnrA were conserved in SSU_RS04755 (Figure 5(c)).
    > To verify if the structural positions of these amino acids were conserved, we performed a structural prediction (see methods) of the predicted S. suis lipoprotein SSU_RS04755 and aligned it to the structure of PnrA (ID 6y9U in Protein Data Bank (PDB). We confirmed that all amino acids involved in the adenosine binding are located at the same position in both protein structures.

### [18] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.712)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [19] Global transcriptional profiling reveals Streptococcus agalactiae genes controlled by the MtaR transcription factor
- Authors: J. Bryan, R. Liles, U. Cvek, M. Trutschl, D. Shelver
- Year: 2008
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/93b44d7dcdffa4a01e09ad914d1253b43d5a06ec
- DOI: 10.1186/1471-2164-9-607
- PMID: 19087320
- PMCID: 2627894
- Citations: 34
- Influential citations: 6
- Summary: This study implicates the metQ1NP genes as encoding the MtaR-regulated methionine transporter, which may provide a mechanistic explanation for the methamphetamineionine-dependent growth defect of the mtaR mutant.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > The expression of a gene cluster (metQ1NP) (Fig. 2A) that displayed strong similarity to established methionine transport gene clusters in other Gram-positive bacteria was downregulated in the mtaR mutant. RT-PCR analysis revealed that the gene cluster was cotranscribed (Fig. 2B). This cluster is predicted to encode products that are highly similar to components of bacterial ABC transporters. The The differentially-regulated genes are grouped into functional categories, based on experimental evidence, protein database searches, and genome annotation. Each GBS COH1 gene [14] is indicated by its Comprehensive Microbial Resources locus number (SAN number) available on the J. Craig Venter Institute website http://www.jcvi.org/cms/research/projects/cmr/ and gene symbol, when applicable. Fold changes in gene expression (mtaR mutant relative to wild-type) and Bayesian P values were derived using Cyber-T [38] analysis of data from three independent biological replicates. Criteria for inclusion in this table were the following: Bayesian P value < 0.001, greater than two-fold change, and confirmation of differential expression by qPCR (Table 2).
    > first component of typical bacterial ABC transporters consists of an ATP-binding cassette (ABC), which binds and hydrolyzes ATP. The second component is a permease, which forms a channel in the membrane. The third component, a substrate-binding protein, imparts specificity to the system. We identified genes predicted to encode the ABC component (MetN), the permease component (MetP), and the substrate-binding component (MetQ1) in the cluster and found that these genes were downregulated in the mtaR mutant. A gene in this cluster (pdsM) is predicted to encode a peptidase from the M20/M25/M40 family; the cotranscription of this gene in the metQ1 cluster may suggest the encoded protein is involved in the breakdown of peptides for nutritional purposes.

### [20] Characterization of the YCjN ABC Transporter in Escherichia coli: Role in Maltose and Ethidium Bromide Transport
- Authors: Yanhong Wang, Beibei Xu, Amro Abdelazez, Heba Abdel-motaal, Qingpeng Liu et al.
- Year: 2025
- Venue: Molecular Biotechnology
- URL: https://www.semanticscholar.org/paper/2d41c89bc66b446792c8cc4601cd5250173ccdef
- DOI: 10.1007/s12033-025-01475-9
- PMID: 40721696
- PMCID: 13053599
- Summary: The functional role of the ycjN gene in carbohydrate transport is established and a foundation for engineering applications involving ABC transporters is provided and provide a foundation for engineering applications involving ABC transporters.
- Evidence snippets:
  - Snippet 1 (score: 0.707)
    > The characterization of adenosine triphosphate-binding cassette (ABC) transporters commenced in the 1980s, driven by significant advancements in molecular biology techniques that facilitated the cloning of crucial genes. Notably, the histidine permease gene from Salmonella typhimurium and the maltose permease gene from Escherichia coli were among the first identified, providing foundational insights into the transport mechanisms employed by these proteins. These pioneering studies established a framework for understanding the intricate structure and functional dynamics of ABC transporters, which are vital for various biological processes [25]. Estevinho, Fernandes [26] underscore that a more profound understanding of ABC transporters' mechanisms could lead to innovative therapeutic strategies for hepatocellular carcinoma. This highlights the potential for translating current knowledge into practical applications, particularly in the context of personalized medicine. The findings support the idea that enhancing our understanding of ABC transporters may not only impact cancer treatment but also significantly influence other areas of drug development and delivery. Furthermore, the obtained findings of structural features of ABC transporters were in alignment with Ford, Kamis [27], including two nucleotidebinding domains (NBDs) and two transmembrane domains (TMDs), along with a substrate-binding protein (solutebinding protein, SBP).
    > The validation of predicted ABC superfamily genes, including ycjN, is essential for enhancing our understanding of this complex transporter family and could significantly influence future research and potential therapeutic applications. YcjN, an ABC family transporter protein found in Escherichia coli, is hypothesized to function as a lipoprotein residing in the periplasmic space. In this context, lipoproteins are characterized by N-acyl and S-diacylglycerol moieties attached to their amino-terminal cysteine residues, which is a hallmark feature of this class of proteins. In Gram-negative bacteria like E. coli, lipoproteins are primarily anchored to either the inner or outer membrane, thus playing a critical role in the lipid-water interface by facilitating various biological processes [28].
    > The domain analysis of the YcjN protein sheds light on its biochemical traits and possible roles.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
4. Tiffany T. Sharma, S. Edassery, N. Rajinikanth, Vikram Karra, Matthew I. Bury et al. (2023). Proteomic profiling of regenerated urinary bladder tissue with stem cell seeded scaffold composites in a non-human primate bladder augmentation model. bioRxiv. https://www.semanticscholar.org/paper/6446e5bc8c0ec1aa0836a711b705ebafa66bd5c8
5. Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang (2010). MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data. Journal of Biomedicine and Biotechnology. https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
6. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
7. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
8. Jian Yang, Qilong Tang, Lei Xu, Zhijiang Li, Yongqiang Ma et al. (2019). Combining of transcriptome and metabolome analyses for understanding the utilization and metabolic pathways of Xylo‐oligosaccharide in Bifidobacterium adolescentis ATCC 15703. Food Science & Nutrition. https://www.semanticscholar.org/paper/a1dc16e9f5c2615024cf1c7cb6bc2e2d3a63a626
9. Nathan Mih, M. Lu, B. Palsson, E. Catoiu (2023). Establishing comprehensive quaternary structural proteomes from genome sequence. Research Square. https://www.semanticscholar.org/paper/bf3821f3fcaef0b354e05b3332a155278a721316
10. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
11. J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al. (2022). Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype. PLoS ONE. https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
12. M. Lurie-Weinberger, Michael Peeri, T. Tuller, U. Gophna (2012). Extensive Inter-Domain Lateral Gene Transfer in the Evolution of the Human Commensal Methanosphaera stadtmanae. Frontiers in Genetics. https://www.semanticscholar.org/paper/d34372c95ea31abaa75d4248b82c50cace6acaa1
13. Shikai Liu, Qi Li, Zhanjiang Liu (2013). Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes. PLoS ONE. https://www.semanticscholar.org/paper/427dc24364271d57abe57d9efe0b1ebfc116d51c
14. Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli (2021). Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae. BMC Research Notes. https://www.semanticscholar.org/paper/4f78acee7559d5e406bacad91d5982d9f3244ea3
15. Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli (2021). Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae. BMC Research Notes. https://www.semanticscholar.org/paper/f30df2b539544c70ac0c1f373b0235d4e92d7687
16. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
17. Maria Juanpere-Borràs, Tiantong Zhao, Jos Boekhorst, Blanca Fernandez-Ciruelos, Rajrita Sanyal et al. (2025). Genome-wide Identification of conditionally essential genes supporting Streptococcus suis growth in serum and cerebrospinal fluid. Virulence. https://www.semanticscholar.org/paper/400884affc80cbd5eef1e69b6961748a60a5b400
18. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
19. J. Bryan, R. Liles, U. Cvek, M. Trutschl, D. Shelver (2008). Global transcriptional profiling reveals Streptococcus agalactiae genes controlled by the MtaR transcription factor. BMC Genomics. https://www.semanticscholar.org/paper/93b44d7dcdffa4a01e09ad914d1253b43d5a06ec
20. Yanhong Wang, Beibei Xu, Amro Abdelazez, Heba Abdel-motaal, Qingpeng Liu et al. (2025). Characterization of the YCjN ABC Transporter in Escherichia coli: Role in Maltose and Ethidium Bromide Transport. Molecular Biotechnology. https://www.semanticscholar.org/paper/2d41c89bc66b446792c8cc4601cd5250173ccdef