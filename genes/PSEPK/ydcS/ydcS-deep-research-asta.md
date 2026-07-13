---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T10:58:34.899778'
end_time: '2026-07-09T10:58:40.010554'
duration_seconds: 5.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ydcS
  gene_symbol: ydcS
  uniprot_accession: Q88MT2
  protein_description: 'SubName: Full=Polyamine ABC transporter, periplasmic polyamine-binding
    protein {ECO:0000313|EMBL:AAN67108.1};'
  gene_info: Name=ydcS {ECO:0000313|EMBL:AAN67108.1}; OrderedLocusNames=PP_1486 {ECO:0000313|EMBL:AAN67108.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: SBP. (IPR006059); Sperm_putr-bd. (IPR001188); SBP_bac_8 (PF13416)
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
- **UniProt Accession:** Q88MT2
- **Protein Description:** SubName: Full=Polyamine ABC transporter, periplasmic polyamine-binding protein {ECO:0000313|EMBL:AAN67108.1};
- **Gene Information:** Name=ydcS {ECO:0000313|EMBL:AAN67108.1}; OrderedLocusNames=PP_1486 {ECO:0000313|EMBL:AAN67108.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** SBP. (IPR006059); Sperm_putr-bd. (IPR001188); SBP_bac_8 (PF13416)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ydcS" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ydcS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ydcS** (gene ID: ydcS, UniProt: Q88MT2) in PSEPK.

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
  - Snippet 1 (score: 0.762)
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
  - Snippet 1 (score: 0.752)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [3] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.749)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

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
  - Snippet 1 (score: 0.748)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [5] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
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
  - Snippet 1 (score: 0.748)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

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
  - Snippet 1 (score: 0.742)
    > To obtain comprehensive gene function information, we performed gene function annotation using eight major databases, including UniProt [23], KEGG [24] and KEGG Pathway, GO [25], Pfam [26], COG [27], TIGERfams [28], RefSeq, and NR. The predicted gene sequences were aligned against functional databases such as COG, KEGG, UniProt, and RefSeq using BLAST+ (Version: 2.11.0+), resulting in the gene function annotation outcomes. The statistical results of the annotations are shown in Table S2. Among the top 20 domains annotated based on Pfam, we observed that genes belonging to "ABC transporters" were the most abundant (Figure 2A). As we know, ABC transporters comprise a large superfamily of proteins that facilitate the translocation of a diverse array of substrates, including ions and macromolecules, across cellular membranes through ATP binding and hydrolysis. Furthermore, these transporters are also critically involved in the cellular uptake and efflux of numerous organic pollutants [29,30]. These results suggest that the abundance of ABC transporter genes provides Paracoccus sp. P-2 with a significant capacity for deltamethrin transport. As shown in Figure 2B, the genes annotated by KEGG are divided into 5 major categories and 23 minor subcategories. Among them, the subcategory with the largest number of genes is metabolic pathways, which include amino acid metabolism, carbohydrate metabolism, energy metabolism, metabolism of cofactors and vitamins, among others. The abundance of genes related to metabolic pathways provides the fundamental basis for the survival and deltamethrin degradation capability of Paracoccus sp. P-2. It is worth noting that a substantial number (254) of membrane transporter genes have been annotated in the genome of Paracoccus sp. P-2. Pollutants are often adsorbed onto the microbial membrane surface and subsequently internalized into the cells-a process in which membrane transporter proteins play a crucial role [31]. This abundance of transporter genes highlights the strain's strong capacity for pollutant transport.

### [7] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.740)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [8] Identifying orthologs with OMA: A primer
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
  - Snippet 1 (score: 0.737)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [9] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.726)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

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

### [11] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.710)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [12] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.700)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [13] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.700)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [14] Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining
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
  - Snippet 1 (score: 0.698)
    > List of genes and genomic features (GFF) for Plasmodium falciparum 3D7 genome (PlasmoDB release 66) was downloaded and protein coding genes were extracted along with their gene annotations and genomic location. Additional genomic annotations were obtained by querying PlasmoDB to extract UniProt and Entrez ID(s), ortholog group (OrthoMCL), protein features (CDS and protein length, molecular weight, isoelectric point), domain annotations (InterPro, PFam, Superfamily), number of transmembrane (TM) domains, and enzyme commission (EC) numbers. Gene function (Gene Ontology; components, functions and processes) was extracted by either PlasmoDB or by querying the InterPro ID under InterPro2GO mapping tool from EMBL-EBI services. Gene essentiality data was obtained for P.
    > falciparum 29 and P. berghei 30,31 parasites that were mapped to their falciparum ortholog using OrthoMCL orthology group IDs. Protein Data Bank (PDB) IDs of crystal structures were obtained by searching either gene symbols, UniProt IDs associated with each gene, or by typing "Plasmodium" in the PDB website search box. A report with gene identi er, organism, accession number, method for structure determination and publication information was extracted for the search hits.
    > Mapping genes to associated literature publications A download from the NCBI FTP site was performed for gene2pubmed.gz (version 2024-02-21) containing taxonomy ID, gene ID (Entrez) and PubMed ID. Gene IDs were mapped to the P. falciparum 3D7 annotation set, and PMIDs matching the criteria were extracted. To include literature references associated with gene symbols, we queried each gene symbol in PubMed using the Eutils 81 efetch function from NCBI; additional information for each publication was obtained pragmatically using the same tool, retrieving title, authors and DOI (digital object identi er).

### [15] Nanomolar Responsiveness of Marine Phaeobacter inhibens DSM 17395 toward Carbohydrates and Amino Acids
- Authors: Arne Weiten, K. Kalvelage, M. Neumann-Schaal, Ramona Buschen, Sabine Scheve et al.
- Year: 2022
- Venue: Microbial Physiology
- URL: https://www.semanticscholar.org/paper/203039f8389b30421070df4a8b7d42cdb98d2f1f
- DOI: 10.1159/000524702
- PMID: 35468615
- Citations: 3
- Summary: Results shed new light on the sensory/regulatory sensitivity of a well-studied roseobacter for recognizing potential substrates at low ambient concentrations and on the concentration threshold below which these might escape biodegradation (“emergent recalcitrance” concept of dissolved organic matter persistence).
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > Metabolic and genomic context of genes selected for quantitative transcript profiling of P. inhibens DSM 17395 in response to defined substrate pulses. a Periplasmic solute-binding proteins of ABC-transporters related to the uptake of the tested carbohydrates. b Degradation network and (c) coding genes for the degradation of the tested organic substrates; modified from Drüppel et al. [2014] and Wiegmann et al. [2014]. Accession numbers of targeted genes are as followed: nagK, PGA1_c27910; mtlK, PGA1_ c13160; xylA, PGA1_c14000; mccB, PGA1_c10320; paaA, PGA1_

### [16] Reconstructing the functions of endosymbiotic Mollicutes in fungus-growing ants
- Authors: P. Sapountzis, M. Zhukova, J. Shik, M. Schiøtt, J. Boomsma
- Year: 2018
- Venue: eLife
- URL: https://www.semanticscholar.org/paper/4c326d290732c1e42f47940b1cf7466fd19dcf2c
- DOI: 10.7554/eLife.39209
- PMID: 30454555
- PMCID: 6245734
- Citations: 44
- Influential citations: 3
- Summary: Reconstructions of their functional significance showed that they are independently acquired symbionts, most likely to decompose excess arginine consistent with the farmed fungal cultivars providing this nitrogen-rich amino-acid in variable quantities.
- Evidence snippets:
  - Snippet 1 (score: 0.695)
    > gene targeted based on the RAST annotation, the target organism, the primer sequences from 5' to 3' and the annealing temperatures used for the qPCR. . Supplementary file 6. Correlation statistics for the association between the number of EntAcro1 cells and the expression of 10 MCT-like genes in the Ac. echinatior midgut and fat body tissues. From left to right we present for each gene examined: The protein ID in the Uniprot database (http://www.uniprot.org/), the gene name and the gene ID based on the Ac. echinatior annotation, the predicted protein size, and the results of statistical analyses examining the correlation between expression of the bacterial ftsZ gene in midgut/fat body tissues and the expression of MCT-like genes. The significance of each correlation was first evaluated using a non-parametric Spearman correlation test (see Methods), for which we give r values, p values and Bonferroni corrected p values.
    > The only significant correlation (marked in bold) was between the ftsZ and the MCT1 (F4WHWZ) transporter, for which previous functional experiments have demonstrated that it is actively involved in the import of acetate in eukaryotic cells (Kirat and Kato, 2006;Moschen et al., 2012).

### [17] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.694)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [18] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
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
  - Snippet 1 (score: 0.691)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

### [19] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2776
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [20] Syn Wiki: Functional annotation of the first artificial organism Mycoplasma mycoides JCVI‐syn3A
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
  - Snippet 1 (score: 0.690)
    > Poorly characterized enzymes F I G U R E 4 Distribution of essentiality among all genes in SynWiki. While essential genes cannot be removed from the genome without loss of viability, the removal of quasi-essential genes results in an observable growth disadvantage 6 genes and 3 pseudogenes), making a total of 492 genes, resulting in better growth and improved stability.
    > In addition to the annotation in the original publications we also went through the literature, checked known functions of homologs, and searched for the availability of protein structures of the JCVI-syn3A proteins or their homologs from other organisms. All these results from manual data curation were added to the pages. Moreover, the curation of the pages is an ongoing process that will lead to ever-improved annotation and data presentation.
    > The success of a biological database strongly depends on the quality of annotation, and for those cases where there is poor or no annotation, we wanted to take a step forward and give our own contribution. With this in mind, and starting from the original annotation, we have also assigned each gene to one or more functional category. We took inspiration from GO term tree 14 and created a tree-like structure containing all functional categories. Currently, there are four major functional branches, "Cellular processes," "Group of genes," "Information processing" and "Metabolism," which then branch out into more specific categories (see here for an overview: http://synwiki.uni-goettingen.de/v1/category, and Table 1). For example, in "Cellular processes" it first branches out into "Cellular envelope and cell division," "Homeostasis," and "Transporters." Then, "Homeostasis" branches out into "Metal ion homeostasis" and "Coping with stress"; "Transporters" branch out into "ABC transporters," "ECF transporters," "Phosphotransferase system" and "Symporter." The "Group of genes" parent F I G U R E 5 Representation of protein homology analysis for PtsH. Results displayed in a table format for each organism used in this analysis with respective best potential homolog with UniProt link.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
4. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
5. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
6. Qing Li, Yawei Zhang, Xianfeng Ren, Qingguo Meng, Baocheng Xu et al. (2025). Genomic and Proteomic Characterization of the Deltamethrin-Degrading Bacterium Paracoccus sp. P-2. Microorganisms. https://www.semanticscholar.org/paper/74c0d94a67b8f801f8322fe976457dfd4c3fd76c
7. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
8. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
9. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
10. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
11. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
12. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
13. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
14. Karla P. Godinez-Macias, Daisy Chen, J. L. Wallis, Miles G. Siegel, Anna Adam et al. (2024). Revisiting the Plasmodium falciparum druggable genome using predicted structures and data mining. Research Square. https://www.semanticscholar.org/paper/795b2985fdc3cf1cfbd5fda1b3c0502eb4dfe866
15. Arne Weiten, K. Kalvelage, M. Neumann-Schaal, Ramona Buschen, Sabine Scheve et al. (2022). Nanomolar Responsiveness of Marine Phaeobacter inhibens DSM 17395 toward Carbohydrates and Amino Acids. Microbial Physiology. https://www.semanticscholar.org/paper/203039f8389b30421070df4a8b7d42cdb98d2f1f
16. P. Sapountzis, M. Zhukova, J. Shik, M. Schiøtt, J. Boomsma (2018). Reconstructing the functions of endosymbiotic Mollicutes in fungus-growing ants. eLife. https://www.semanticscholar.org/paper/4c326d290732c1e42f47940b1cf7466fd19dcf2c
17. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
18. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
19. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
20. Tiago Pedreira, Christoph Elfmann, Neil Singh, J. Stülke (2021). Syn Wiki: Functional annotation of the first artificial organism Mycoplasma mycoides JCVI‐syn3A. Protein Science : A Publication of the Protein Society. https://www.semanticscholar.org/paper/d9974c7fedefa8ec51f166d8546c8b0e819a7e14