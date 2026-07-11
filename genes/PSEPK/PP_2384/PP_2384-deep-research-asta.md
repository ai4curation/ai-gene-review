---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T22:41:24.141472'
end_time: '2026-07-10T22:41:28.811250'
duration_seconds: 4.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2384
  gene_symbol: PP_2384
  uniprot_accession: Q88KA6
  protein_description: 'RecName: Full=Branched-chain amino acid ABC transporter {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_2384 {ECO:0000313|EMBL:AAN67997.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Brnchd-chn_aa_trnsp_AzlD. (IPR008407); AzlD (PF05437)
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
- **UniProt Accession:** Q88KA6
- **Protein Description:** RecName: Full=Branched-chain amino acid ABC transporter {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_2384 {ECO:0000313|EMBL:AAN67997.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Brnchd-chn_aa_trnsp_AzlD. (IPR008407); AzlD (PF05437)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2384" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2384' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2384** (gene ID: PP_2384, UniProt: Q88KA6) in PSEPK.

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
  - Snippet 1 (score: 0.740)
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
  - Snippet 1 (score: 0.739)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.736)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.735)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

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
  - Snippet 1 (score: 0.729)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [6] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
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
  - Snippet 1 (score: 0.717)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [7] MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data
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
  - Snippet 1 (score: 0.716)
    > Table 3 lists the Genbank accession number, the gene symbols, accession number in UniProtKB (UniProt Knowledgebase), and gene descriptions given by colon data. The UniProtKB is the central hub for the collection of information on proteins such as amino acid sequence, protein name or description, taxonomic data, and biological ontology [24]. Figure 6 depicts gene expression profiles of the eight genes in normal and disease samples. As shown in Figure 6, the profiles of these genes are highly coexpressed in normal samples (samples 1-22) while the coexpression pattern disappears in disease samples (samples 23-62).

### [8] CRONOS: the cross-reference navigation server
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

### [9] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.700)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [10] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.699)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [11] Proteomic profiling of regenerated urinary bladder tissue with stem cell seeded scaffold composites in a non-human primate bladder augmentation model
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
  - Snippet 1 (score: 0.691)
    > Raw data were analyzed using Proteome Discoverer 2.5 (Thermo Fisher Scientific) using the "PWF Tribrid TMTpro Quan SPS MS3 SequestHT Percolator" and "CWF Comprehensive Enhanced Annotation Reporter
    > Quan" methods implemented in the PD2.For uncharacterized proteins or proteins with unknown function presented in the manuscript, the UniProt Accession number was search against UniProt database https://www.uniprot.org/and the NCBI Gene database https://www.ncbi.nlm.nih.gov/gene/.If required, more information was obtained with regards to protein identity by matching the amino acid sequence of the protein on the NCBI BLAST alignment program https://blast.ncbi.nlm.nih.gov/Blast.cgi .

### [12] Genomic and Proteomic Characterization of the Deltamethrin-Degrading Bacterium Paracoccus sp. P-2
- Authors: Qing Li, Yawei Zhang, Xianfeng Ren, Qingguo Meng, Baocheng Xu et al.
- Year: 2025
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/74c0d94a67b8f801f8322fe976457dfd4c3fd76c
- DOI: 10.3390/microorganisms13112481
- PMID: 41304166
- PMCID: 12654547
- Summary: This study elucidates the impact of deltamethrin on bacterial metabolism and its degradation mechanism by Paracoccus sp.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > To obtain comprehensive gene function information, we performed gene function annotation using eight major databases, including UniProt [23], KEGG [24] and KEGG Pathway, GO [25], Pfam [26], COG [27], TIGERfams [28], RefSeq, and NR. The predicted gene sequences were aligned against functional databases such as COG, KEGG, UniProt, and RefSeq using BLAST+ (Version: 2.11.0+), resulting in the gene function annotation outcomes. The statistical results of the annotations are shown in Table S2. Among the top 20 domains annotated based on Pfam, we observed that genes belonging to "ABC transporters" were the most abundant (Figure 2A). As we know, ABC transporters comprise a large superfamily of proteins that facilitate the translocation of a diverse array of substrates, including ions and macromolecules, across cellular membranes through ATP binding and hydrolysis. Furthermore, these transporters are also critically involved in the cellular uptake and efflux of numerous organic pollutants [29,30]. These results suggest that the abundance of ABC transporter genes provides Paracoccus sp. P-2 with a significant capacity for deltamethrin transport. As shown in Figure 2B, the genes annotated by KEGG are divided into 5 major categories and 23 minor subcategories. Among them, the subcategory with the largest number of genes is metabolic pathways, which include amino acid metabolism, carbohydrate metabolism, energy metabolism, metabolism of cofactors and vitamins, among others. The abundance of genes related to metabolic pathways provides the fundamental basis for the survival and deltamethrin degradation capability of Paracoccus sp. P-2. It is worth noting that a substantial number (254) of membrane transporter genes have been annotated in the genome of Paracoccus sp. P-2. Pollutants are often adsorbed onto the microbial membrane surface and subsequently internalized into the cells-a process in which membrane transporter proteins play a crucial role [31]. This abundance of transporter genes highlights the strain's strong capacity for pollutant transport.

### [13] Computational screening of phytochemicals targeting mutant KRAS in colorectal cancer
- Authors: Muskan Arooj, R. Mateen, M. Javed, Muhammad Ali, Muhammad Irfan Fareed et al.
- Year: 2025
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/2e47ff33fc8e4bd8a85a3cd322f3441bb45db205
- DOI: 10.1038/s41598-025-14229-z
- PMID: 40770256
- PMCID: 12329011
- Citations: 2
- Summary: This study focused on the identification of potential phytochemicals that can inhibit the KRAS protein from being overexpressed in CRC using the anticancer medication fruquintinib, which has been authorized by the FDA.
- Evidence snippets:
  - Snippet 1 (score: 0.683)
    > For the structure retrieval of the KRAS gene, which is overexpressed in CRC, the Universal Protein Resource (UniProt) (https://www.uniprot.org/) database was first consulted for detailed functional information. UniProt provides extensive data on proteins and their functional annotations 19 . The KRAS gene encoding GTPase protein consisting of 189 amino acids with a molecular weight of approximately 21.6 kDa was recovered from the Protein Data Bank (PDB) using the RCSB-PDB ID: 7SCW, which has a resolution of 1.98 Å. The Protein Data Bank (PDB) ( https://doi.org/10.2210/pdb7SCW/pdb) is a crucial resource for studying the 3D structures, aiding research and education in many fields 20 .

### [14] Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes
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
  - Snippet 1 (score: 0.681)
    > Background Although a large set of full-length transcripts was recently assembled in catfish, annotation of large gene families, especially those with duplications, is still a great challenge. Most often, complexities in annotation cause mis-identification and thereby much confusion in the scientific literature. As such, detailed phylogenetic analysis and/or orthology analysis are required for annotation of genes involved in gene families. The ATP-binding cassette (ABC) transporter gene superfamily is a large gene family that encodes membrane proteins that transport a diverse set of substrates across membranes, playing important roles in protecting organisms from diverse environment. Methodology/Principal Findings In this work, we identified a set of 50 ABC transporters in catfish genome. Phylogenetic analysis allowed their identification and annotation into seven subfamilies, including 9 ABCA genes, 12 ABCB genes, 12 ABCC genes, 5 ABCD genes, 2 ABCE genes, 4 ABCF genes and 6 ABCG genes. Most ABC transporters are conserved among vertebrates, though cases of recent gene duplications and gene losses do exist. Gene duplications in catfish were found for ABCA1, ABCB3, ABCB6, ABCC5, ABCD3, ABCE1, ABCF2 and ABCG2. Conclusion/Significance The whole set of catfish ABC transporters provide the essential genomic resources for future biochemical, toxicological and physiological studies of ABC drug efflux transporters. The establishment of orthologies should allow functional inferences with the information from model species, though the function of lineage-specific genes can be distinct because of specific living environment with different selection pressure.

### [15] Phyletic Profiling with Cliques of Orthologs Is Enhanced by Signatures of Paralogy Relationships
- Authors: N. Skunca, Matko Bosnjak, A. Kriško, P. Panov, S. Džeroski et al.
- Year: 2013
- Venue: PLoS Computational Biology
- URL: https://www.semanticscholar.org/paper/1510cd0e087650323cdf75ea132e6fcbc4d7e852
- DOI: 10.1371/journal.pcbi.1002852
- PMID: 23308060
- PMCID: 3536626
- Citations: 41
- Influential citations: 2
- Summary: A novel model for computational annotation that refines two established concepts: annotation based on homology and annotations based on phyletic profiling is introduced, which will contribute to making experimental validation of computational predictions more approachable, both in cost and time.
- Evidence snippets:
  - Snippet 1 (score: 0.680)
    > In addition to the systematic experimental verification of novel annotations in three GO categories as described above, here we highlight individual predictions for which we found supporting evidence in the publicly available databases. This information was not available to the classifiers at the time when the models were constructed. The following examples are for E. coli K12, as this is by far the best-studied model prokaryote [21].
    > We predict genes hypC and hybG to have ''nickel cation binding.'' These genes had no GO terms assigned in the 07-02-2012 UniProt-GOA release (http://www.uniprot.org/uniprot/ P0AAM3 and http://www.uniprot.org/uniprot/P0AAM7), and we therefore considered them unannotated. In the meantime, hypC was annotated with ''metal ion binding'' using experimental evidence: this is a parent GO term of our prediction. Moreover, when examining the literature, we found evidence that these two genes are involved in the biosynthesis of the [NiFe] cluster [22].
    > Another prediction is for gltL: we predicted it is annotated with ''ATP-binding cassette (ABC) transporter complex.'' In line with our predictions, PortEco, a portal that includes information from 14 different E. coli data resources [23], labels the gene as ''ATPbinding component of ABC superfamily.'' Note that more general electronic GO annotations were available for this gene, e.g. ''ATP binding,'' ''ATPase activity,'' and ''ATP catabolic process'' (http://www.uniprot.org/uniprot/P0AAG3).
    > A similar prediction of a more detailed function is for ybgI, where we predict GO terms from both BP and MF ontologies. This gene is known to be a conserved metal-binding protein [24], having an electronic GO annotation ''metal ion binding''; we predict it is annotated with the BP GO term ''Mo-molybdopterin cofactor metabolic process.''

### [16] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.677)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [17] Genomic and metabolomic insights into the antimicrobial compounds and plant growth-promoting potential of Bacillus velezensis Q-426
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
  - Snippet 1 (score: 0.677)
    > These proteins accounted for 9.20% and 8.66% of the total protein sequences, respectively. The annotation results suggested that 119 genes participated in secondary metabolite biosynthesis, transport, and catabolism. As expected, the lipopeptides including surfactin, iturin, and fengycin gene clusters, were found in the genome sequence of Q-426.
    > In the present study, we used the InterProScan database [25] to predict all of the protein domains and functional sites of B. velezensis Q-426 and extract the information of GO [26,27]. Based on the GO functional annotation shown in Fig. 3, the identified proteins were classified into 3 large groups, including biological process, cellular components, and molecular functions. The results suggested that the proteins were annotated into 48 functional groups, including 26 biological processes, 12 cellular components, and 10 molecular functions (Fig. 3). In biological processes, the proteins were mainly involved in metabolic processes (1746 genes), cellular processes (1689 genes), and localization (624 genes). In cellular components, the proteins were mainly involved in cell (1135 genes), cell part (1135 genes), and organelle (225 genes). In molecular functions, the proteins were mainly involved in catalytic activity (1723 genes), binding (1391 genes), and transporter activity (286 genes).
    > The genes involved in the metabolic pathways were analyzed statistically using the KEGG analysis tool in the genome sequence of B. velezensis Q-426 [28]. The KEGG analysis results showed that the proteins were annotated to 36 KEGG pathways, classified into 6 large groups, including cellular processes (163 genes), environmental information processing (300 genes), genetic information processing (185 genes), human diseases (77 genes), metabolism (887 genes), and organismal systems (34 genes) (Fig. 4). Carbohydrate metabolism pathways (187 genes) and membrane transport (171 genes) were the primary enriched pathways, followed by amino acid metabolism (162 genes). The KEGG database analysis showed a great number of two-component systems (114 genes) and ABC transporters (135 genes).

### [18] Unraveling genomic features and phylogenomics through the analysis of three Mexican endemic Myotis genomes
- Authors: Edgar G. Gutiérrez, J. E. Maldonado, Gabriela Castellanos‐Morales, Luis E. Eguiarte, Norberto Martínez‐Méndez et al.
- Year: 2024
- Venue: PeerJ
- URL: https://www.semanticscholar.org/paper/051ff7f79c8f5cce0e73f8c350d6c442cb75fc12
- DOI: 10.7717/peerj.17651
- PMID: 38993980
- PMCID: 11238727
- Citations: 4
- Summary: Background Genomic resource development for non-model organisms is rapidly progressing, seeking to uncover molecular mechanisms and evolutionary adaptations enabling thriving in diverse environments. Limited genomic data for bat species hinder insights into their evolutionary processes, particularly within the diverse Myotis genus of the Vespertilionidae family. In Mexico, 15 Myotis species exist, with three—M. vivesi, M. findleyi, and M. planiceps—being endemic and of conservation concern. M...
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > (Jones et al., 2014) and each of the gene predictions were compared against gene annotations available in the InterPro database (Blum et al., 2021).The InterPro database integrates predictive information about protein function from many resources providing a description of the protein function (Blum et al., 2021).The second approach is based on protein homology through BLASTp v. 2.13.0+ (Camacho et al., 2009).This package requires a database to compare and detect the best match for each gene analyzed.The functional inference analysis was generated using the protein sequence databases UniProtKB/Swiss-Prot (UniProt Consortium, 2023) and NCBI RefSeq (O'Leary et al., 2016).The third approach corresponds to the search for putative biological functions of the structural predicted genes were assigned by compared against the Kyoto Encyclopedia of Genes and Genomes (KEGG; Kanehisa et al., 2023).Low quality genes of less than 50 amino acids and/or exhibiting premature termination were removed.

### [19] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.673)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [20] Potential role of multiple carbon fixation pathways during lipid accumulation in Phaeodactylum tricornutum
- Authors: Jacob J. Valenzuela, Aurélien Mazurie, R. Carlson, R. Gerlach, K. Cooksey et al.
- Year: 2012
- Venue: Biotechnology for Biofuels
- URL: https://www.semanticscholar.org/paper/5f205021fe6a9b10aba8237bdac8ceada97adde0
- DOI: 10.1186/1754-6834-5-40
- PMID: 22672912
- PMCID: 3457861
- Citations: 206
- Influential citations: 10
- Summary: The results indicate that P. tricornutum continued carbon dioxide reduction when population growth was arrested and different carbon-concentrating mechanisms were used dependent upon exogenous DIC levels, and suggest that the build-up of precursors to the acetyl-CoA carboxylases may play a more significant role in TAG synthesis rather than the actual enzyme levels of acetyl
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > Cufflinks output files had transcripts identified by uniprot accessions. Using the DAVID (Database for Annotation, Visualization, and Integrated Discovery) [67] Gene ID conversion tool, uniprot accessions were converted to Locus Tag IDs and Protein IDs. Once all accessions were converted, the DAVID Functional Annotation tool was used to retrieve gene names as well as KEGG (Kyoto Encyclopedia of Genes and Genomes) Pathway information. For genes that were identified as hypothetical proteins, searches were performed on the JGI Phaeodactylum tricornutum v2.0 genome website (http://genome.jgi-psf. org/Phatr2/Phatr2.home.html) and based on best hits, % ID, score, and consistency of the top hits, genes were either identified or remained as hypothetical. Genes were also searched on NCBI and ENSEMBL genome browsers for cross-referencing. To assign genes into pathways, we used KEGG maps for P. tricornutum as a backbone. Genes for major pathways were searched manually to find genes not directly annotated in the P. tricornutum KEGG maps. Gene lists were compiled for the major pathways and developed into network maps.
    > Organelle targeting for transcript products was done based on annotations from the databases of JGI, NCBI, and ENSEMBL. If no localization was found, eukaryotic organelle localizations were predicted with TargetP 1.1. server [68] in both plant and non-plant mode. Amino acid sequences were also checked for a peroxisomal targeting sequence (SKL, serine-lysine-leucine). If potential targeting was not identified, we assumed that the gene product occurred in the cytoplasm. If the gene was an integral membrane protein we again checked JGI, NCBI, and ENSEMBL, and if targeting could not be determined we located the gene in the most biologically relevant membrane (e.g., light harvesting complex in the plastid).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
5. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
6. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
7. Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang (2010). MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data. Journal of Biomedicine and Biotechnology. https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
8. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
9. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
10. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
11. Tiffany T. Sharma, S. Edassery, N. Rajinikanth, Vikram Karra, Matthew I. Bury et al. (2023). Proteomic profiling of regenerated urinary bladder tissue with stem cell seeded scaffold composites in a non-human primate bladder augmentation model. bioRxiv. https://www.semanticscholar.org/paper/6446e5bc8c0ec1aa0836a711b705ebafa66bd5c8
12. Qing Li, Yawei Zhang, Xianfeng Ren, Qingguo Meng, Baocheng Xu et al. (2025). Genomic and Proteomic Characterization of the Deltamethrin-Degrading Bacterium Paracoccus sp. P-2. Microorganisms. https://www.semanticscholar.org/paper/74c0d94a67b8f801f8322fe976457dfd4c3fd76c
13. Muskan Arooj, R. Mateen, M. Javed, Muhammad Ali, Muhammad Irfan Fareed et al. (2025). Computational screening of phytochemicals targeting mutant KRAS in colorectal cancer. Scientific Reports. https://www.semanticscholar.org/paper/2e47ff33fc8e4bd8a85a3cd322f3441bb45db205
14. Shikai Liu, Qi Li, Zhanjiang Liu (2013). Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes. PLoS ONE. https://www.semanticscholar.org/paper/427dc24364271d57abe57d9efe0b1ebfc116d51c
15. N. Skunca, Matko Bosnjak, A. Kriško, P. Panov, S. Džeroski et al. (2013). Phyletic Profiling with Cliques of Orthologs Is Enhanced by Signatures of Paralogy Relationships. PLoS Computational Biology. https://www.semanticscholar.org/paper/1510cd0e087650323cdf75ea132e6fcbc4d7e852
16. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
17. Lulu Wang, Ruochen Fan, Haodi Ma, Yu Sun, Yang Huang et al. (2023). Genomic and metabolomic insights into the antimicrobial compounds and plant growth-promoting potential of Bacillus velezensis Q-426. BMC Genomics. https://www.semanticscholar.org/paper/dafda64a4e7dbdc0906aa66bc17fd6ee5856514c
18. Edgar G. Gutiérrez, J. E. Maldonado, Gabriela Castellanos‐Morales, Luis E. Eguiarte, Norberto Martínez‐Méndez et al. (2024). Unraveling genomic features and phylogenomics through the analysis of three Mexican endemic Myotis genomes. PeerJ. https://www.semanticscholar.org/paper/051ff7f79c8f5cce0e73f8c350d6c442cb75fc12
19. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
20. Jacob J. Valenzuela, Aurélien Mazurie, R. Carlson, R. Gerlach, K. Cooksey et al. (2012). Potential role of multiple carbon fixation pathways during lipid accumulation in Phaeodactylum tricornutum. Biotechnology for Biofuels. https://www.semanticscholar.org/paper/5f205021fe6a9b10aba8237bdac8ceada97adde0