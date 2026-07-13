---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T15:56:41.893375'
end_time: '2026-07-08T15:56:47.233091'
duration_seconds: 5.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3559
  gene_symbol: PP_3559
  uniprot_accession: Q88H06
  protein_description: 'SubName: Full=Glycine betaine ABC transporter (Permease) {ECO:0000313|EMBL:AAN69160.2};'
  gene_info: OrderedLocusNames=PP_3559 {ECO:0000313|EMBL:AAN69160.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the binding-protein-dependent transport system
  protein_domains: MetI-like. (IPR000515); MetI-like_sf. (IPR035906); BPD_transp_1
    (PF00528)
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
- **UniProt Accession:** Q88H06
- **Protein Description:** SubName: Full=Glycine betaine ABC transporter (Permease) {ECO:0000313|EMBL:AAN69160.2};
- **Gene Information:** OrderedLocusNames=PP_3559 {ECO:0000313|EMBL:AAN69160.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the binding-protein-dependent transport system
- **Key Domains:** MetI-like. (IPR000515); MetI-like_sf. (IPR035906); BPD_transp_1 (PF00528)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3559" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3559' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3559** (gene ID: PP_3559, UniProt: Q88H06) in PSEPK.

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
- Snippets retrieved: 19

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
  - Snippet 1 (score: 0.738)
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
  - Snippet 1 (score: 0.736)
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
  - Snippet 1 (score: 0.733)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [4] De novo transcriptome analysis of halotolerant bacterium Staphylococcus sp. strain P-TSB-70 isolated from East coast of India: In search of salt stress tolerant genes
- Authors: P. Das, B. Behera, S. Chatterjee, B. Das, T. Mohapatra
- Year: 2020
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/2bd5c9d398bf4af3553e03f2a6c145e16dfbbfaf
- DOI: 10.1371/journal.pone.0228199
- PMID: 32040520
- PMCID: 7010390
- Citations: 17
- Summary: The information acquired in the present study possibly used to recognize and clone the salt stress tolerant genes and support in developing the salt Stress-tolerant plant varieties to expand the agricultural productivity in the saline system.
- Evidence snippets:
  - Snippet 1 (score: 0.717)
    > Some of the genes are associated with osmoprotectant viz. glycine betaine, sodium potassium transporters, trehalose, while rest of the genes are associated with dass family protein, abc atp-binding protein, abc permease protein, abc solute binding protein, abc substrate binding family 3, abc-2 type transporter, neurotransmitter family, amino acid carrier protein, etc. (S7 Table ). In recent study, Xiong and co-workers [63] reported the genes responsible for membrane transport, abc transport, glycine betaine and proline in E. coli under salt stress which corroborates to our present study. A similar study has https://doi.org/10.1371/journal.pone.0228199.g007 been performed by Choi et al. [27] on a strain of Staphylococcus sp. as the genus tolerates high NaCl concentration. A number of researchers have investigated glycine betaine gene, trehalose gene, ectoine gene, sodium, and hydrogen antiporters from different bacteria viz.

### [5] Genomic and Proteomic Characterization of the Deltamethrin-Degrading Bacterium Paracoccus sp. P-2
- Authors: Qing Li, Yawei Zhang, Xianfeng Ren, Qingguo Meng, Baocheng Xu et al.
- Year: 2025
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/74c0d94a67b8f801f8322fe976457dfd4c3fd76c
- DOI: 10.3390/microorganisms13112481
- PMID: 41304166
- PMCID: 12654547
- Summary: This study elucidates the impact of deltamethrin on bacterial metabolism and its degradation mechanism by Paracoccus sp.
- Evidence snippets:
  - Snippet 1 (score: 0.715)
    > To obtain comprehensive gene function information, we performed gene function annotation using eight major databases, including UniProt [23], KEGG [24] and KEGG Pathway, GO [25], Pfam [26], COG [27], TIGERfams [28], RefSeq, and NR. The predicted gene sequences were aligned against functional databases such as COG, KEGG, UniProt, and RefSeq using BLAST+ (Version: 2.11.0+), resulting in the gene function annotation outcomes. The statistical results of the annotations are shown in Table S2. Among the top 20 domains annotated based on Pfam, we observed that genes belonging to "ABC transporters" were the most abundant (Figure 2A). As we know, ABC transporters comprise a large superfamily of proteins that facilitate the translocation of a diverse array of substrates, including ions and macromolecules, across cellular membranes through ATP binding and hydrolysis. Furthermore, these transporters are also critically involved in the cellular uptake and efflux of numerous organic pollutants [29,30]. These results suggest that the abundance of ABC transporter genes provides Paracoccus sp. P-2 with a significant capacity for deltamethrin transport. As shown in Figure 2B, the genes annotated by KEGG are divided into 5 major categories and 23 minor subcategories. Among them, the subcategory with the largest number of genes is metabolic pathways, which include amino acid metabolism, carbohydrate metabolism, energy metabolism, metabolism of cofactors and vitamins, among others. The abundance of genes related to metabolic pathways provides the fundamental basis for the survival and deltamethrin degradation capability of Paracoccus sp. P-2. It is worth noting that a substantial number (254) of membrane transporter genes have been annotated in the genome of Paracoccus sp. P-2. Pollutants are often adsorbed onto the microbial membrane surface and subsequently internalized into the cells-a process in which membrane transporter proteins play a crucial role [31]. This abundance of transporter genes highlights the strain's strong capacity for pollutant transport.

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
  - Snippet 1 (score: 0.713)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [7] The GbsR Family of Transcriptional Regulators: Functional Characterization of the OpuAR Repressor
- Authors: Stefanie Ronzheimer, Bianca Warmbold, C. Arnhold, E. Bremer
- Year: 2018
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/870efb61fecea60dee006daba32938f63e0197f6
- DOI: 10.3389/fmicb.2018.02536
- PMID: 30405586
- PMCID: 6207618
- Citations: 7
- Summary: GbsR-/OpuAR-type proteins are characterized as an extended sub-group within the MarR-superfamily of transcriptional regulators and a novel type of substrate-inducible import system for osmostress protectants is identified.
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > Representative genetic arrangements of opuA gene loci are shown, and the sub-unit composition of the encoded OpuA-type ABC transporters is depicted. In three opuA-type gene clusters (e.g., in P. larvae), a single gene encodes the permease (OpuAB) and the substrate-binding domain (OpuAC) of the transporter. All of these fused transporters (van der Heide and Poolman, 2002) were present in members of the genus Paenibacillus.
    > oriented gbsA-gbsB and gbsR-gbsU genes are transcribed as choline-responsive operons (Burkhardt et al., 2009). The H. halophilus GbsR protein exhibits a 52% amino acid sequence identity to its B. subtilis GbsR counterpart. Functional studies with similar genetically configured glycine betaine synthesis genes (gbsAB) from Halobacillus dabanensis have also been performed, and gbsR-gbsU-type genes have also been found in this halophile, although a different nomenclature (gbsI-gbsT) has been used to annotate them (Gu et al., 2008).
    > Physiological studies and gene disruption analysis have also been conducted with the glycine betaine synthesis genes (cudA-cudB) from S. xylosus (Rosenstein et al., 1999; Figure 4A). The corresponding gbsR-type gene was named cudC and its encoded protein is 52% identical to the GbsR protein from B. subtilis. Next to the cudC gene, a choline transporter gene (cudT) is present (Rosenstein et al., 1999) that encodes a member of the BCCT-type transporter family; many of its members, including the choline transporter BetT from E. coli (Lamark et al., 1991) serve for the uptake of osmostress protectants (Ziegler et al., 2010). Notably, transcription of the S. xylosus cudAB glycine betaine biosynthetic genes is inducible by both high salinity and choline (Rosenstein et al., 1999).

### [8] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.705)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [9] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.704)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [10] Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes
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
  - Snippet 1 (score: 0.703)
    > Background Although a large set of full-length transcripts was recently assembled in catfish, annotation of large gene families, especially those with duplications, is still a great challenge. Most often, complexities in annotation cause mis-identification and thereby much confusion in the scientific literature. As such, detailed phylogenetic analysis and/or orthology analysis are required for annotation of genes involved in gene families. The ATP-binding cassette (ABC) transporter gene superfamily is a large gene family that encodes membrane proteins that transport a diverse set of substrates across membranes, playing important roles in protecting organisms from diverse environment. Methodology/Principal Findings In this work, we identified a set of 50 ABC transporters in catfish genome. Phylogenetic analysis allowed their identification and annotation into seven subfamilies, including 9 ABCA genes, 12 ABCB genes, 12 ABCC genes, 5 ABCD genes, 2 ABCE genes, 4 ABCF genes and 6 ABCG genes. Most ABC transporters are conserved among vertebrates, though cases of recent gene duplications and gene losses do exist. Gene duplications in catfish were found for ABCA1, ABCB3, ABCB6, ABCC5, ABCD3, ABCE1, ABCF2 and ABCG2. Conclusion/Significance The whole set of catfish ABC transporters provide the essential genomic resources for future biochemical, toxicological and physiological studies of ABC drug efflux transporters. The establishment of orthologies should allow functional inferences with the information from model species, though the function of lineage-specific genes can be distinct because of specific living environment with different selection pressure.

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
  - Snippet 1 (score: 0.698)
    > Protein identifications with 2 peptides and a confident protein score (P <0.05) from the HpH fractionation and IDA-MS were used to assign subcellular localization. Using the top score given by WoLF PSORT [10] (www.genscript.com/wolf-psort.html) proteins were categorized into 8 locations. Membrane proteins were predicted using transmembrane helical Markov model (TMHMM) [11] (www.cbs.dtu.dk/services/TMHMM/). Proteins in the solute carrier protein (SLC) and ATP-binding cassette (ABC) transporter families were identified according to gene and protein name. We also used website gene names (www.genenames.org/data) to characterise the subcellular location of the transporter and the type of substrate they transport.
    > For proteins annotated as 'uncharacterised' in figures and tables in the manuscript a BLAST protein homology search was carried out using the Ensembl or uniport accession code in uniprotKB (www.uniprot.org). The accession code page contains the sequence and a link to BLAST. BLASTp results against uniprotkb_Swissprot reference proteomes and an identity sequence match of >95.5% to human, bovine (cattle) or caprine (goat) proteome annotation was accepted as the protein name.

### [12] Overexpression of Scr1 protein induces strong changes in the transcriptome and metabolome of Streptomyces coelicolor that affect antibiotic production
- Authors: C. Riascos, Gemma Fernández-García, Javier García-Martín, Ángel Manteca, R. Santamaría et al.
- Year: 2025
- Venue: Microbial Cell Factories
- URL: https://www.semanticscholar.org/paper/1459f4ce98f53d7b31337731f37caa2e8199a493
- DOI: 10.1186/s12934-025-02843-5
- PMID: 41077587
- PMCID: 12516864
- Summary: Xenobiotic response element (XRE) regulator proteins play an important role in gene regulation in Streptomyces. In these bacteria, they are often encoded together with a small protein containing a DUF397 domain. Previous work on 15 such pairs present in S. coelicolor has shown they act as pleiotropic regulators. They dependently affect antibiotic production and morphological differentiation on different culture media. Overexpression of the protein Scr1, which is encoded by gene SCO4441, induc...
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > In addition to the metabolic processes that were altered by Scr1 overexpression, the RNA-Seq assay also detected differential expression of several important genes involved in molecular transport and gene regulation, as detailed below.
    > ABC transporters: three types of ABC transporters were differentially expressed in the strain Sscr1: mineral and organic ion transporters; oligosaccharide, polyol and lipid transporters; and phosphate and amino acid transporters (Additional File 12). The expression pattern of these genes varied greatly from one type to another. For example, in the Sscr1 strain, genes for three molybdate transport-associated proteins (SCO3704, SCO3705, and SCO3706) were overexpressed only at 36 h. The same occurred for the betaine transporter (SCO4831), an osmoprotectant; except in this case, the gene for the substrate-binding protein (SCO2933) was not differentially expressed. Additionally, the genes for the three proteins responsible for the multiple sugar transporter were under-expressed. Thus, the gene encoding a putative sugar-binding protein (SCO2404) was under-expressed at 36 h, while those genes encoding the permease protein (SCO2406) and the ATP-binding protein (SCO2405) were under-expressed at 48 h. In the case of adenosine and the genes of four proteins associated with transport, the first, a lipoprotein (SCO4884), was under-expressed at 36 h, while the genes for the other three proteins, two permease proteins (SCO4887 and SCO4888) and an ATP-binding protein (SCO4886), were overexpressed at 48 h. As for orthophosphate transport, the genes for the three proteins responsible for its transport (SCO6814, SCO6415, and SCO6416) were overexpressed at 36 and 48 h and showed high FC values.

### [13] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.696)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [14] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.695)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [15] Identification of divergent botulinum neurotoxin homologs in Paeniclostridium ghonii
- Authors: Xin Wei, T. Wentz, B. Lobb, Michael J. Mansfield, William Zhen et al.
- Year: 2022
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/5f4f5db95227de16b06d3d95f4c151643dd1af07
- DOI: 10.1101/2022.08.17.504336
- Citations: 9
- Summary: The identification of two putative divergent BoNT-like homologs in the genomes of two strains of Paeniclostridium ghonii are reported, one of which is a divergent member of the lineage of BoNT that also includes BoNT/X, Bo NT/En and the insecticidal PMP1.
- Evidence snippets:
  - Snippet 1 (score: 0.693)
    > The PG-toxin1 locus from strain NCTR 3900 is similar but non-identical from that of the PG-toxin2 locus from strain DSM 15049. A notable unique feature of the PG-toxin locus is the presence of a nearby gene encoding an insecticidal Cry delta endotoxin (accession # WP_250673405.1). A cry toxin prediction was confirmed by the Conserved Domain Database, with matches to all three domains (N, M, and C-terminal region) with significant E-values all less than 1e-15. BLAST analysis of this protein also confirmed its relationship to a Cry8Ea1 family insecticidal delta endotoxin from Bacillus thuringiensis (accession # WP_172452114.1) with ~40% amino acid identity. The closest sequence of known structure is B. thuringiensis cry3Aa (PDB ID 4QX0_A) at 32% identity. In both P. ghonii genomes, this Cry toxin gene is encoded in the opposite direction to the PGT-LC genes, which suggests that it may be regulated differently.
    > In addition, The PG-toxin locus also encodes several genes shared with those found in other BoNT gene clusters. These include amiD (n-acetylmuramoyl-l-alanine amidase gene) and parA genes which are also present in the BoNT/En locus of E. faecium; and abc (ABC transporter ATPbinding protein) and fic (filamentation induced by cAMP protein) genes that are also found in the tent locus of C. tetani. Three nearby genes are also shared with the PMP1 locus of P.
    > bifermentans: an mpp gene encoding a putative metallophosphatase family protein, an abcpermease (ABC transporter ATP-binding protein/permease) and a radsam gene encoding a radical SAM domain containing protein. Interestingly, the orfx, ha and ntnh genes present in other BoNT gene clusters are absent.

### [16] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.687)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

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
  - Snippet 1 (score: 0.685)
    > Gene SSU_RS04755 has been predicted to encode a basic membrane family protein (BMP), a transmembrane component of specific ABC transporters. Growth curve experiments did not reveal a significant reduction in the growth rate of our ΔSSU_RS04755 mutant. The operon genes with SSU_RS04755 were predicted to encode an ATPbinding protein and a permease which are typical components of an ABC transporter. Both predicted ATPbinding protein and permease encoding genes appeared as CEGs in our Tn-seq results (Table 1). The protein sequence associated with SSU_RS04755 shares significant identity with lipoproteins that are components of nucleoside ABC transporters in Gram-positive bacteria (see above), suggesting that SSU_RS04755 and its operon genes may encode an ABC transporter complex involved in nucleoside transport. To investigate the possible functional equivalence of SSU_RS04755 operon genes with ABC transporters, we performed amino acid sequence alignments of SSU_RS04755 with PnrA and TmpC, which are homologous nucleoside binding lipoproteins from S. pneumoniae and Treponema pallidum (T. pallidum) respectively [49,50]. Using the crystal structure of PnrA binding to adenosine [49], we confirmed that all but one (T70) of the specific amino acids involved in adenosine binding by PnrA were conserved in SSU_RS04755 (Figure 5(c)).
    > To verify if the structural positions of these amino acids were conserved, we performed a structural prediction (see methods) of the predicted S. suis lipoprotein SSU_RS04755 and aligned it to the structure of PnrA (ID 6y9U in Protein Data Bank (PDB). We confirmed that all amino acids involved in the adenosine binding are located at the same position in both protein structures.

### [18] Reconstructing the functions of endosymbiotic Mollicutes in fungus-growing ants
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
  - Snippet 1 (score: 0.681)
    > gene targeted based on the RAST annotation, the target organism, the primer sequences from 5' to 3' and the annealing temperatures used for the qPCR. . Supplementary file 6. Correlation statistics for the association between the number of EntAcro1 cells and the expression of 10 MCT-like genes in the Ac. echinatior midgut and fat body tissues. From left to right we present for each gene examined: The protein ID in the Uniprot database (http://www.uniprot.org/), the gene name and the gene ID based on the Ac. echinatior annotation, the predicted protein size, and the results of statistical analyses examining the correlation between expression of the bacterial ftsZ gene in midgut/fat body tissues and the expression of MCT-like genes. The significance of each correlation was first evaluated using a non-parametric Spearman correlation test (see Methods), for which we give r values, p values and Bonferroni corrected p values.
    > The only significant correlation (marked in bold) was between the ftsZ and the MCT1 (F4WHWZ) transporter, for which previous functional experiments have demonstrated that it is actively involved in the import of acetate in eukaryotic cells (Kirat and Kato, 2006;Moschen et al., 2012).

### [19] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.680)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
4. P. Das, B. Behera, S. Chatterjee, B. Das, T. Mohapatra (2020). De novo transcriptome analysis of halotolerant bacterium Staphylococcus sp. strain P-TSB-70 isolated from East coast of India: In search of salt stress tolerant genes. PLoS ONE. https://www.semanticscholar.org/paper/2bd5c9d398bf4af3553e03f2a6c145e16dfbbfaf
5. Qing Li, Yawei Zhang, Xianfeng Ren, Qingguo Meng, Baocheng Xu et al. (2025). Genomic and Proteomic Characterization of the Deltamethrin-Degrading Bacterium Paracoccus sp. P-2. Microorganisms. https://www.semanticscholar.org/paper/74c0d94a67b8f801f8322fe976457dfd4c3fd76c
6. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
7. Stefanie Ronzheimer, Bianca Warmbold, C. Arnhold, E. Bremer (2018). The GbsR Family of Transcriptional Regulators: Functional Characterization of the OpuAR Repressor. Frontiers in Microbiology. https://www.semanticscholar.org/paper/870efb61fecea60dee006daba32938f63e0197f6
8. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
9. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
10. Shikai Liu, Qi Li, Zhanjiang Liu (2013). Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes. PLoS ONE. https://www.semanticscholar.org/paper/427dc24364271d57abe57d9efe0b1ebfc116d51c
11. J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al. (2022). Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype. PLoS ONE. https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
12. C. Riascos, Gemma Fernández-García, Javier García-Martín, Ángel Manteca, R. Santamaría et al. (2025). Overexpression of Scr1 protein induces strong changes in the transcriptome and metabolome of Streptomyces coelicolor that affect antibiotic production. Microbial Cell Factories. https://www.semanticscholar.org/paper/1459f4ce98f53d7b31337731f37caa2e8199a493
13. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
14. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
15. Xin Wei, T. Wentz, B. Lobb, Michael J. Mansfield, William Zhen et al. (2022). Identification of divergent botulinum neurotoxin homologs in Paeniclostridium ghonii. bioRxiv. https://www.semanticscholar.org/paper/5f4f5db95227de16b06d3d95f4c151643dd1af07
16. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
17. Maria Juanpere-Borràs, Tiantong Zhao, Jos Boekhorst, Blanca Fernandez-Ciruelos, Rajrita Sanyal et al. (2025). Genome-wide Identification of conditionally essential genes supporting Streptococcus suis growth in serum and cerebrospinal fluid. Virulence. https://www.semanticscholar.org/paper/400884affc80cbd5eef1e69b6961748a60a5b400
18. P. Sapountzis, M. Zhukova, J. Shik, M. Schiøtt, J. Boomsma (2018). Reconstructing the functions of endosymbiotic Mollicutes in fungus-growing ants. eLife. https://www.semanticscholar.org/paper/4c326d290732c1e42f47940b1cf7466fd19dcf2c
19. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c