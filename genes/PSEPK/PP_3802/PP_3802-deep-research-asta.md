---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T21:06:49.944141'
end_time: '2026-07-08T21:06:54.836826'
duration_seconds: 4.89
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3802
  gene_symbol: PP_3802
  uniprot_accession: Q88GC2
  protein_description: 'SubName: Full=Cation ABC transporter, ATP-binding protein
    {ECO:0000313|EMBL:AAN69396.1};'
  gene_info: OrderedLocusNames=PP_3802 {ECO:0000313|EMBL:AAN69396.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439);
    ABC_transporter-like_CS. (IPR017871); Metal_Ion_Import_ABC. (IPR050153); P-loop_NTPase.
    (IPR027417)
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
- **UniProt Accession:** Q88GC2
- **Protein Description:** SubName: Full=Cation ABC transporter, ATP-binding protein {ECO:0000313|EMBL:AAN69396.1};
- **Gene Information:** OrderedLocusNames=PP_3802 {ECO:0000313|EMBL:AAN69396.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); Metal_Ion_Import_ABC. (IPR050153); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3802" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3802' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3802** (gene ID: PP_3802, UniProt: Q88GC2) in PSEPK.

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
  - Snippet 1 (score: 0.801)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [2] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.776)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [3] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.776)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [4] Phyletic Profiling with Cliques of Orthologs Is Enhanced by Signatures of Paralogy Relationships
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
  - Snippet 1 (score: 0.775)
    > In addition to the systematic experimental verification of novel annotations in three GO categories as described above, here we highlight individual predictions for which we found supporting evidence in the publicly available databases. This information was not available to the classifiers at the time when the models were constructed. The following examples are for E. coli K12, as this is by far the best-studied model prokaryote [21].
    > We predict genes hypC and hybG to have ''nickel cation binding.'' These genes had no GO terms assigned in the 07-02-2012 UniProt-GOA release (http://www.uniprot.org/uniprot/ P0AAM3 and http://www.uniprot.org/uniprot/P0AAM7), and we therefore considered them unannotated. In the meantime, hypC was annotated with ''metal ion binding'' using experimental evidence: this is a parent GO term of our prediction. Moreover, when examining the literature, we found evidence that these two genes are involved in the biosynthesis of the [NiFe] cluster [22].
    > Another prediction is for gltL: we predicted it is annotated with ''ATP-binding cassette (ABC) transporter complex.'' In line with our predictions, PortEco, a portal that includes information from 14 different E. coli data resources [23], labels the gene as ''ATPbinding component of ABC superfamily.'' Note that more general electronic GO annotations were available for this gene, e.g. ''ATP binding,'' ''ATPase activity,'' and ''ATP catabolic process'' (http://www.uniprot.org/uniprot/P0AAG3).
    > A similar prediction of a more detailed function is for ybgI, where we predict GO terms from both BP and MF ontologies. This gene is known to be a conserved metal-binding protein [24], having an electronic GO annotation ''metal ion binding''; we predict it is annotated with the BP GO term ''Mo-molybdopterin cofactor metabolic process.''

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
  - Snippet 1 (score: 0.763)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [6] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
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
  - Snippet 1 (score: 0.756)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [7] Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype
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
  - Snippet 1 (score: 0.756)
    > Protein identifications with 2 peptides and a confident protein score (P <0.05) from the HpH fractionation and IDA-MS were used to assign subcellular localization. Using the top score given by WoLF PSORT [10] (www.genscript.com/wolf-psort.html) proteins were categorized into 8 locations. Membrane proteins were predicted using transmembrane helical Markov model (TMHMM) [11] (www.cbs.dtu.dk/services/TMHMM/). Proteins in the solute carrier protein (SLC) and ATP-binding cassette (ABC) transporter families were identified according to gene and protein name. We also used website gene names (www.genenames.org/data) to characterise the subcellular location of the transporter and the type of substrate they transport.
    > For proteins annotated as 'uncharacterised' in figures and tables in the manuscript a BLAST protein homology search was carried out using the Ensembl or uniport accession code in uniprotKB (www.uniprot.org). The accession code page contains the sequence and a link to BLAST. BLASTp results against uniprotkb_Swissprot reference proteomes and an identity sequence match of >95.5% to human, bovine (cattle) or caprine (goat) proteome annotation was accepted as the protein name.

### [8] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.754)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [9] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.749)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [10] Genome-scale Model Constrained by Proteomics Reveals Metabolic Rearrangements in the Heterologous Host Streptomyces coelicolor
- Authors: Snorre Sulheim, T. Kumelj, Dino van Dissel, Ali Salehzadeh-Yazdi, Chao Du et al.
- Year: 2019
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/bee47d74917a677c792ed89d3d0d6496b790d5fb
- DOI: 10.1101/796722
- Citations: 1
- Summary: This study provides the first systems description of S. coelicolor M1152, an engineered heterologous expression host widely used for the production and discovery of natural products, and reconstructed the consensus model Sco-GEM in an open-science framework.
- Evidence snippets:
  - Snippet 1 (score: 0.744)
    > Gene annotations, substrate and transport class information were mostly extracted from Transport DB 2.0 (116) and TCDB (117). Then, transport proteins were extracted from IUBMB-approved Transporter Classification (TC) System and categorized into 9 main classes (Figure 1F): 1) ABC transporter; 2) PTS transporter; 3) Proton symporter; 4) Sodium symporter; 5) Other symporter; 6) Proton antiport; 7) Other antiport; 8) Facilitated diffusion; 9) Simple diffusion. For those transport proteins with an ambiguous substrate annotation in TCDB, the specific substrate annotation was obtain by extracting annotations from KEGG (51,52), UniProt (57) or through BLAST homology search (118) using a similarity threshold of 90% (see Supplemental Information 2 and Table S4 for details).

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
  - Snippet 1 (score: 0.742)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [12] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.736)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [13] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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

### [14] Does aberrant membrane transport contribute to poor outcome in adult acute myeloid leukemia?
- Authors: A. Chigaev
- Year: 2015
- Venue: Frontiers in Pharmacology
- URL: https://www.semanticscholar.org/paper/f9357a4a86ddce362e62083115f9ced89f8e617e
- DOI: 10.3389/fphar.2015.00134
- PMID: 26191006
- PMCID: 4489100
- Citations: 11
- Summary: Several ideas describing the possible relationship of membrane transport activity and leukemic cell biology, including the “Warburg effect,” the specific role of chloride ion transport, direct “import” of metabolic energy through uptake of creatine phosphate, and modification of the bone marrow niche microenvironment are discussed.
- Evidence snippets:
  - Snippet 1 (score: 0.726)
    > Previously, Wilson et al. (2006) reported that Clusters 7 and 8 of Valk et al. (2004) had a gene expression profile most similar to cluster B. It has been noted that one of genes overexpressed by these patients was ABCG2, a member of ATP-binding cassette (ABC) superfamily of membrane transporters, also termed breast cancer resistance protein (BCRP1), later dubbed as a stem cell marker and a target in cancer stem cell therapy (Ding et al., 2010). Moreover, ABCG2 protein overexpression in concurrence with FLT3-ITD mutation identifies a subgroup of AML patients with significantly worse prognosis (Tiribelli et al., 2011).
    > Our analysis of the top most significant discriminating genes from all three clusters revealed an unanticipated phenomenon: these clusters were enriched in genes functionally involved in membrane transport -transporters and channels (Table 1). Here protein functions are described according to UniprotKB1 and Gene Ontology2 databases. For gene function annotation from UniprotKB, reviewed (curator-evaluated) computational records (Swiss-Prot) were used. Below, a review of the specific gene functional roles is presented. This review is only intended to show data that are relevant for this particular context. For multiple genes listed below exhaustive literature reviews do exist.

### [15] Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes
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
  - Snippet 1 (score: 0.725)
    > Background Although a large set of full-length transcripts was recently assembled in catfish, annotation of large gene families, especially those with duplications, is still a great challenge. Most often, complexities in annotation cause mis-identification and thereby much confusion in the scientific literature. As such, detailed phylogenetic analysis and/or orthology analysis are required for annotation of genes involved in gene families. The ATP-binding cassette (ABC) transporter gene superfamily is a large gene family that encodes membrane proteins that transport a diverse set of substrates across membranes, playing important roles in protecting organisms from diverse environment. Methodology/Principal Findings In this work, we identified a set of 50 ABC transporters in catfish genome. Phylogenetic analysis allowed their identification and annotation into seven subfamilies, including 9 ABCA genes, 12 ABCB genes, 12 ABCC genes, 5 ABCD genes, 2 ABCE genes, 4 ABCF genes and 6 ABCG genes. Most ABC transporters are conserved among vertebrates, though cases of recent gene duplications and gene losses do exist. Gene duplications in catfish were found for ABCA1, ABCB3, ABCB6, ABCC5, ABCD3, ABCE1, ABCF2 and ABCG2. Conclusion/Significance The whole set of catfish ABC transporters provide the essential genomic resources for future biochemical, toxicological and physiological studies of ABC drug efflux transporters. The establishment of orthologies should allow functional inferences with the information from model species, though the function of lineage-specific genes can be distinct because of specific living environment with different selection pressure.

### [16] Integrated pan-cancer analysis revealed therapeutic targets in the ABC transporter protein family
- Authors: M. B. E. Masood, Iqra Shafique, M. Rafique, Ayesha Iman, Ariba Abbasi et al.
- Year: 2025
- Venue: PLOS One
- URL: https://www.semanticscholar.org/paper/75f1be3a2286bbe9d4105e8c1625c6913bc7d7bf
- DOI: 10.1371/journal.pone.0308585
- PMID: 40445912
- PMCID: 12124511
- Citations: 1
- Summary: It is demonstrated that ABCA10 shows reduced expression, while ABCB5 displays variable expression patterns across tumors, indicating their opposing roles and flexible functions in pan-cancer.
- Evidence snippets:
  - Snippet 1 (score: 0.715)
    > WGCNA is a useful algorithm for discovering modules of co-expressed genes, module is a collection of genes with matching expression patterns across various biological mechanisms or sample types [10,51]. After module identification, the association among gene modules and tumor state (primary, recurring, and metastatic) was calculated. 43 modules were identified in present study, correlation analysis reveals that turquoise and paleturquoise modules are the modules of interest, exhibiting strong relationships with different tumor states. Subsequently, we identified genes that were common between DEGs and genes in selected modules. This process ensures that every gene exhibits the greatest degree of differential expression accompanied by highest correlation with tumor state. Ultimately, ABCA10 and ABCB5 were selected for further analysis.
    > ABC transporters have been extensively investigated in the context of cancer, where they play pivotal roles in immune regulation and treatment resistance. Their functions are welldocumented, particularly in the context of multidrug resistance, where these proteins actively pump chemotherapeutic agents out of cancer cells, diminishing drug efficacy. Comprehensive studies have detailed the structural and functional complexity of ABC transporters and their involvement in various biological processes. However, research has predominantly focused on well-known members, such as multidrug resistance protein 1 (MDR1, also known as ATP-binding cassette subfamily B member 1, ABCB1), breast cancer resistance protein (BCRP, also known as ATP-binding cassette subfamily G member 2, ABCG2), and multidrug resistance-associated protein 1 (MRP1, also known as ATP-binding cassette subfamily C member 1, ABCC1) [52][53][54] leaving other transporters relatively underexplored. While emerging research is beginning to uncover roles of ABC transporters apart from drug efflux, including their influence on tumor biology and immune interactions, these studies typically focus on a limited number of cancer types. Consequently, a comprehensive understanding of the broader roles of less-studied transporters, such as ABCA10 and ABCB5, remains an important area for further exploration. We utilized an innovative bioinformatics approach to bridge this significant gap by simultaneously examining ABCA10 and ABCB5 across multiple cancer types.

### [17] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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

### [18] The Protein Interactome of Glycolysis in Escherichia coli
- Authors: Shomeek Chowdhury, Stephen Hepper, M. Lodi, M. Saier, P. Uetz
- Year: 2021
- Venue: Proteomes
- URL: https://www.semanticscholar.org/paper/ab9b1aae1d278887ece0a69b5e7725e8d494c0ee
- DOI: 10.3390/proteomes9020016
- PMID: 33917325
- PMCID: 8167557
- Citations: 8
- Summary: This work investigates which of these interactions may affect glycolysis in E. coli and possibly across numerous other bacteria, based on the stoichiometry of interacting protein pairs (from proteomic studies) and their conservation across bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.711)
    > In order to identify enzymes among glycolytic interactors, we used the EC number in the Uniprot reference proteome [34]. Similarly, we used the Uniprot GO (Gene Ontology) terms to map proteins to biological processes, including "metabolic process" to find metabolic proteins or proteins not known to be involved in any metabolic pathway. This information was verified using annotations from KEGG [35] to identify proteins involved in carbohydrate metabolism or other processes, such as environmental information processing. Lastly, we identified essential genes/proteins using the Database of Essential Genes (DEG version 15.2) [36].

### [19] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.711)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [20] Topology based identification and comprehensive classification of four-transmembrane helix containing proteins (4TMs) in the human genome
- Authors: Misty M. Attwood, Arunkumar Krishnan, Valentina Pivotti, Samira Yazdi, M. S. Almén et al.
- Year: 2016
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/268e83d5e00c4b7b210ab19c9bd873e0e50ba87e
- DOI: 10.1186/s12864-016-2592-7
- PMID: 27030248
- PMCID: 4815072
- Citations: 10
- Summary: This study identifies the complete 4TM complement from the latest release of the human genome and assess the 4TM structure group as a whole and functionally characterize this dataset and evaluates the resulting groups and ubiquitous functions, and furthermore describe disease and drug target involvement.
- Evidence snippets:
  - Snippet 1 (score: 0.708)
    > The manual classification process included four steps, which are highlighted in Fig. 1B. Universal protein resource (Uniprot) [28] was used to access annotation information on the dataset by using the unique Ensembl protein identification associated with each protein. Uniprot is a large comprehensive repository of protein sequences with manually curated as well as automatically generated associated annotations. For each protein, the associated UniProt annotations were used in the curation process: gene name, sequence status, review status, Consensus Coding Sequence identifier, Transporter Classification number, Enzyme Commission number, Pfam domain information, Gene Ontology annotation terms, and protein family information.
    > The Uniprot sequence information is derived from translated sequences that have been submitted to the International Nucleotide Sequence Database Collaboration (INSDC), which is EMBL-bank, GenBank, and DDBJ. The canonical sequence is determined from either the most prevalent, the most similar to orthologous sequences, the properties of the amino acid composition, or in lieu of nothing else, then the longest sequence. The sequence status is defined as either complete or fragment, in which the canonical sequence is missing amino acid residues, often in the initial or terminal ends. Those protein sequences identified as fragments were considered invalid proteins and culled from the dataset. To reduce falsepositive predictions from TOPCONS-single, proteins that were identified in literature or database sources as having less than or greater than four-transmembrane segments were also removed from the dataset.
    > The initial gene annotation source, GenCode, has ~1050 more protein-coding gene entries than the most conservative annotation resource, the Consensus Coding Sequence dataset (CCDS) [64]. Therefore the CCDS identifier was used to assess the validity of each protein, i.e. that each has acceptable transcriptional support and recognized protein-coding annotation. Additionally, the sequence status, CCDS identifier, and sequence length were used to ensure that the predicted protein was the main (or canonical) protein product of the gene and not an isoform. There are eight predicted proteins in the dataset that do not have a CCDS identifier associated with them.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
3. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. N. Skunca, Matko Bosnjak, A. Kriško, P. Panov, S. Džeroski et al. (2013). Phyletic Profiling with Cliques of Orthologs Is Enhanced by Signatures of Paralogy Relationships. PLoS Computational Biology. https://www.semanticscholar.org/paper/1510cd0e087650323cdf75ea132e6fcbc4d7e852
5. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
6. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
7. J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al. (2022). Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype. PLoS ONE. https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
8. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
9. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
10. Snorre Sulheim, T. Kumelj, Dino van Dissel, Ali Salehzadeh-Yazdi, Chao Du et al. (2019). Genome-scale Model Constrained by Proteomics Reveals Metabolic Rearrangements in the Heterologous Host Streptomyces coelicolor. bioRxiv. https://www.semanticscholar.org/paper/bee47d74917a677c792ed89d3d0d6496b790d5fb
11. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
12. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
13. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
14. A. Chigaev (2015). Does aberrant membrane transport contribute to poor outcome in adult acute myeloid leukemia?. Frontiers in Pharmacology. https://www.semanticscholar.org/paper/f9357a4a86ddce362e62083115f9ced89f8e617e
15. Shikai Liu, Qi Li, Zhanjiang Liu (2013). Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes. PLoS ONE. https://www.semanticscholar.org/paper/427dc24364271d57abe57d9efe0b1ebfc116d51c
16. M. B. E. Masood, Iqra Shafique, M. Rafique, Ayesha Iman, Ariba Abbasi et al. (2025). Integrated pan-cancer analysis revealed therapeutic targets in the ABC transporter protein family. PLOS One. https://www.semanticscholar.org/paper/75f1be3a2286bbe9d4105e8c1625c6913bc7d7bf
17. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
18. Shomeek Chowdhury, Stephen Hepper, M. Lodi, M. Saier, P. Uetz (2021). The Protein Interactome of Glycolysis in Escherichia coli. Proteomes. https://www.semanticscholar.org/paper/ab9b1aae1d278887ece0a69b5e7725e8d494c0ee
19. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
20. Misty M. Attwood, Arunkumar Krishnan, Valentina Pivotti, Samira Yazdi, M. S. Almén et al. (2016). Topology based identification and comprehensive classification of four-transmembrane helix containing proteins (4TMs) in the human genome. BMC Genomics. https://www.semanticscholar.org/paper/268e83d5e00c4b7b210ab19c9bd873e0e50ba87e