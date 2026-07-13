---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T06:04:46.386510'
end_time: '2026-07-07T06:04:53.292371'
duration_seconds: 6.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: atpG
  gene_symbol: atpG
  uniprot_accession: Q88BX3
  protein_description: 'RecName: Full=ATP synthase gamma chain {ECO:0000255|HAMAP-Rule:MF_00815};
    AltName: Full=ATP synthase F1 sector gamma subunit {ECO:0000255|HAMAP-Rule:MF_00815};
    AltName: Full=F-ATPase gamma subunit {ECO:0000255|HAMAP-Rule:MF_00815};'
  gene_info: Name=atpG {ECO:0000255|HAMAP-Rule:MF_00815}; OrderedLocusNames=PP_5414;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATPase gamma chain family.
  protein_domains: ATP_synth_F1_ATPase_gsu. (IPR035968); ATP_synth_F1_gsu. (IPR000131);
    ATP_synth_F1_gsu_CS. (IPR023632); ATP-synt (PF00231)
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
- **UniProt Accession:** Q88BX3
- **Protein Description:** RecName: Full=ATP synthase gamma chain {ECO:0000255|HAMAP-Rule:MF_00815}; AltName: Full=ATP synthase F1 sector gamma subunit {ECO:0000255|HAMAP-Rule:MF_00815}; AltName: Full=F-ATPase gamma subunit {ECO:0000255|HAMAP-Rule:MF_00815};
- **Gene Information:** Name=atpG {ECO:0000255|HAMAP-Rule:MF_00815}; OrderedLocusNames=PP_5414;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATPase gamma chain family.
- **Key Domains:** ATP_synth_F1_ATPase_gsu. (IPR035968); ATP_synth_F1_gsu. (IPR000131); ATP_synth_F1_gsu_CS. (IPR023632); ATP-synt (PF00231)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atpG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atpG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atpG** (gene ID: atpG, UniProt: Q88BX3) in PSEPK.

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
  - Snippet 1 (score: 0.772)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.673)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.738)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [3] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.700)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [4] Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology
- Authors: Stefania D'Alessio, Katherine M. Buckley, I. Kraev, P. Hayes, S. Lange
- Year: 2021
- Venue: Biology
- URL: https://www.semanticscholar.org/paper/e2b33d9697175a6e724fdb85e3ac2ec169d92871
- DOI: 10.3390/biology10090866
- PMID: 34571743
- PMCID: 8464700
- Citations: 14
- Summary: This study assessed EVs present in the coelomic fluid of the purple sea urchin, and identified both total protein cargo as well as the deiminated protein cargo, adding to current understanding of how post-translational deimination may shape immunity across the phylogeny tree.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > For the detection of a putative PAD homologue from sea urchins, anti-human PAD2-specific antibody was used in Western blotting to assess any cross-reaction with a (B) KEGG pathways identified from STRING analysis for EV total protein cargo (annotated hits). (C) Gene Ontology (GO) Biological processes identified from STRING analysis for total EV protein cargo (annotated hits). (D) GO Molecular Function pathways identified from STRING analysis for total EV protein cargo (annotated hits; protein names of hits are presented in the figures; additional interacting proteins are: LOC579085 = ATP synthase subunit gamma, mitochondrial; LOC587430 = ATP synthase subunit O, mitochondrial; LOC373382 = ATP synthase subunit alpha; LOC576006 = ATP synthase subunit delta, mitochondrial; LOC579751 = ATP synthase F(0) complex subunit B1, mitochondrial).

### [5] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
- Authors: F. Pfeiffer, D. Oesterhelt
- Year: 2015
- Venue: Life
- URL: https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
- DOI: 10.3390/life5021427
- PMID: 26042526
- PMCID: 4500146
- Citations: 38
- Influential citations: 1
- Summary: A manual curation effort is described that attempts to produce high-quality genome annotations for a set of haloarchaeal genomes (Halobacterium salinarum and Hbt. hubeiense, Haloferax volcanii and Hfx. mediterranei).
- Evidence snippets:
  - Snippet 1 (score: 0.689)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [6] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2771
- Influential citations: 298
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [7] Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control
- Authors: Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al.
- Year: 2023
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
- DOI: 10.3390/ijms241713058
- PMID: 37685862
- PMCID: 10488290
- Citations: 3
- Summary: Chilodonella hexasticha is a harmful parasitic ciliate that can cause severe damage to fish and high mortalities worldwide. Its congeneric species, C. uncinata, is a facultative parasite that not only can be free-living but also can parasitize on fish gills and fins. In this study, single-cell transcriptomes of these two species were assembled and characterized. Numerous enzymes related to energy metabolism and parasitic adaption were identified through annotation in the Non-Redundant (NR), C...
- Evidence snippets:
  - Snippet 1 (score: 0.681)
    > Some energy metabolism-related enzymes, such as isocitrate dehydrogenase (IDH), cytochrome c oxidase subunit 1 (Cox 1) and ATP synthase, were also up-regulated in C. hexasticha. for this study, while those of C. uncinata were adopted from [7]. The yellow boxes represent the upregulated genes, while the blue boxes represent down-expressed genes. The full names of protein products of these annotated genes are TUB: tubulin, ISCU: iron-sulfur cluster assembly scaffold protein IscU-like; ISCB: 2 iron, 2 sulfur cluster-binding protein, IDH: isocitrate dehydrogenase, Cox1: cytochrome c oxidase subunit 1, ATP5D: ATP synthase F1, delta subunit, OGC: 2oxoglutarate/malate carrier protein, ABC: ABC transporter family protein, ATPase: v-type ATPase subunit family protein, HSP: heat shock protein, ACP: acyl carrier protein, DNAH7: dynein heavy chain 7.

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
  - Snippet 1 (score: 0.673)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [9] Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains
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
  - Snippet 1 (score: 0.673)
    > Gene annotation was primarily derived from the S. clavuligerus reference genome in the NCBI database and was annotated using the NCBI Prokaryotic Genome Annotation Pipeline 59 . However, several CA biosynthetic genes were manually corrected based on published literature 9 . For instance, two loci were originally annotated as clavaminate synthase 1 (cas1), but one of these loci is located near the cephamycin C biosynthetic cluster, indicating it was actually cas2. Following this correction, the RefSeq accession numbers of all genes in the reference genome were cross-referenced with the UniProt database to obtain additional annotations 60 . For the mutated genes identified through ICA, protein existence levels were manually assigned based on the UniProt data, including protein existence status, annotation score, similar proteins, and relevant publications.

### [10] YeATSAM analysis of the walnut and chickpea transcriptome reveals key genes undetected by current annotation tools
- Authors: S. Chakraborty, P. Martínez-García, A. Dandekar
- Year: 2016
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/0b0afbfabeba7d3a90e11f6ce97418c3f8c7f71f
- DOI: 10.12688/f1000research.10040.1
- PMID: 28105312
- PMCID: 5200947
- Citations: 8
- Summary: An annotation method in the YeATS suite (YeATSAM) is presented, based on information encoded by the transcriptome, that demonstrates artifacts of the assembler, which must be addressed to achieve proper annotation.
- Evidence snippets:
  - Snippet 1 (score: 0.653)
    > The closest match of Uniprot:P30986 (with a low significance of 1E-07) to the MAKER-P annotation is 'WALNUT 00019959-RA', a 476 aa long cytokinin dehydrogenase. The sequence alignment of JrBBE genes to Uniprot (P30986) is shown (Figure 3a).
    > As with the walnut transcriptome, the chickpea transcriptome (transHybrid.fasta: n=34760) (Garg et al., 2011) was split into three ORFs, each of which was BLAST'ed to the subset of plant proteins created from the Ensembl database. Subsequently, the ORFs with significant homology to this database (n=29263) were BLAST'ed to the set of annotated chickpea proteins in the NCBI database (n=34198). Most of these annotations were done using Gnomon (Souvorov et al., 2010) (http://www.ncbi.nlm.nih.gov/ bioproject/PRJNA190909), which analyzed ~35000 transcripts.
    > There are ~1500 proteins identified by YeATSAM that are absent in the NCBI database (Evalue cutoff 1E-10). Some of these proteins and their corresponding genes in the TAIR database are shown (Table 4). TC00902 is an interesting example with two merged genes: a hydrogen ion-transporting ATP synthase (TAIR ID: ATMG00640.1) and a cytochrome C biogenesis (TAIR ID: ATMG00900.1). While Gnomon identified the cytochrome C  3). Here, there are four full length berberine bridge enzyme (BBE) genes (named JrBBE1-4) identified using the transcriptome. Some of the proteins are truncated (like C54286_ G1_I1), which might be an artifact of the Trinity assembler. Thus, this is not a complete enumeration of the JrBBE genes. biogenesis protein (Genbank: XP_004500083.1), it failed to identify the ATP synthase.

### [11] Plasma proteomics in septic shock and alcohol-related pancreatitis: a hyaluronan-centered approach
- Authors: Jaap van der Heijden, Asanda Mazubane, Marko Sallisalmi, E. Vorontsov, J. Tenhunen et al.
- Year: 2025
- Venue: Clinical Proteomics
- URL: https://www.semanticscholar.org/paper/ae917565de913693a2713b46c3eda672d9d01c7f
- DOI: 10.1186/s12014-025-09556-2
- PMID: 40885913
- PMCID: 12398169
- Summary: The altered proteomic profile of hyaluronan-related proteins as reflected by the GO terms indicates a complex dysregulation not only in hyaluronan metabolism and extracellular matrix, but also in the regulation of several proteolytic enzymes.
- Evidence snippets:
  - Snippet 1 (score: 0.650)
    > The identification of hyaluronan-associated genes was performed using Python 3.10.12. The UniProt REST Web Application Programming Interface (API) was used to query and retrieve gene annotations that met specific criteria (UniProt Consortium). A keyword-based query, utilizing the terms "hyaluronan, " "hyaluronic acid, " "hyaluronidase, " "hyaluronic acid synthase, " "hyaluronate binding protein, " "hyaluronan oligosaccharides, " "hyaluronan synthase, " and "hyaluronan receptor, " was executed across our dataset of 663 genes. Gene symbols were returned as "hits" when the query keywords were found in the annotations, including functional comments, Gene Ontology (GO) terms, and cross-referenced databases, formatted in JSON.

### [12] GeneTools – application for functional annotation and statistical hypothesis testing
- Authors: V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al.
- Year: 2006
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
- DOI: 10.1186/1471-2105-7-470
- PMID: 17062145
- PMCID: 1630634
- Citations: 105
- Influential citations: 11
- Summary: GeneTools is the first "all in one" annotation tool, providing users with a rapid extraction of highly relevant gene annotation data for e.g. thousands of genes or clones at once.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [13] An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México
- Authors: Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel
- Year: 2023
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
- DOI: 10.3390/microorganisms11071640
- PMID: 37512813
- PMCID: 10384328
- Citations: 8
- Summary: The quality obtained from the biogas suggests that this metabolism is not the main one in carbon use, possibly the sum of several conditions including growth conditions and the pollution present in these sediments.
- Evidence snippets:
  - Snippet 1 (score: 0.645)
    > When a genome is sequenced or a protein is characterized, databases classify the information in different ways using automatic identification or manual annotation. In the UniProt database, an annotation is possibly made using the formal representation proposed in Gene Ontology (GO) under three aspects related to biological knowledge of the proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively. An example of an ATP-binding protein is the subunit α of V-type ATP synthase (A0A8G2FW98) of Picrophilus oshimae DSM 9789. As expected, this protein has other three annotations related to proton transport. Besides that, the DNA helicase (A0A811T524) of Ca. Argoarchaeum ethanivorans has the MF of DNA binding and ATP binding. Interestingly, metal ion binding proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively.

### [14] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Citations: 1
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.641)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [15] Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production
- Authors: Seth B Roberts, Christopher M. Gowen, J. Brooks, Stephen S. Fong
- Year: 2010
- Venue: BMC Systems Biology
- URL: https://www.semanticscholar.org/paper/dc66757785ecb9e1d1760f67f5410dddb5d3618c
- DOI: 10.1186/1752-0509-4-31
- PMID: 20307315
- PMCID: 2852388
- Citations: 129
- Influential citations: 15
- Summary: A genome-scale model of C. thermocellum metabolism is presented, i SR432, for the purpose of establishing a computational tool to study the metabolic network of the organism and establish a strong foundation for rational strain design.
- Evidence snippets:
  - Snippet 1 (score: 0.641)
    > GPR relationships specify the putative relationship between genes and enzymatic activities in an organism. Following previous work [52], we represented these relationships as Boolean statements. The simplest such statement was: gene A implies reaction X, i.e., gene A -> reaction X. Enzymatic activities associated with protein complexes required more complicated statements, e.g., (gene A or gene B) and (gene C) -> reaction X.
    > To develop the GPR relationships for C. thermocellum, we used the annotations described above and information on protein complexes from UniProt. For each EC number in the C. thermocellum annotations, we searched UniProt [23] to determine whether that EC is associated with protein complexes, and if so, what type of complex exists across different organisms (homodimer, heterotrimer, etc.). Based on this information, and the information in the annotations, we assigned putative GPR relationships for C. thermocellum, conforming to known enzyme complex architecture whenever possible. As a specific example of this process, consider the reaction corresponding to carbamoyl-phosphate synthase ('R_CBPS'), EC 6.3.5.5. Several UniProt entries (e.g., CARA_ECOLI) with this EC number are annotated as being members of a complex composed of two chains, a small glutamine-hydrolyzing chain and a large chain that synthesizes carbamoyl phosphate. We found two C. thermocellum genes annotated as "carbamoyl-phosphate synthase, small subunit" (Cthe_1867, Cthe_0950) and two genes annotated as "carbamoyl-phosphate synthase, large subunit" (Cthe_1868, Cthe_0949). Thus, we expressed the GPR relationship for this reaction as: (Cthe_1867 or Cthe_0950) and (Cthe_1868 or Cthe_0949) -> R_CBPS.

### [16] Proteome-wide Subcellular Topologies of E. coli Polypeptides Database (STEPdb)*
- Authors: Georgia Orfanoudaki, A. Economou
- Year: 2014
- Venue: Molecular & Cellular Proteomics
- URL: https://www.semanticscholar.org/paper/8e452aca415b30d995ba9f977086924c8fed8f19
- DOI: 10.1074/mcp.O114.041137
- PMID: 25210196
- Citations: 72
- Influential citations: 3
- Summary: The STEP database (STEPdb) is a comprehensive characterization of subcellular localization and topology of the complete proteome of Escherichia coli and is the first database that contains an extensive set of peripheral IM proteins (PIM proteins) and includes their graphical visualization into complexes, cellular functions, and interactions.
- Evidence snippets:
  - Snippet 1 (score: 0.641)
    > The E. coli K-12 Reference Proteome and Data Sources-Two databases Uniprot (29) and EcoLOCATION (32) and the proposed IM proteome (33) were the main initial starting points for the complete subcellular categorization of K-12 described here. The E. coli K-12/ MG1655 strain is one of the microbial proteomes whose comprehensive annotation is of the highest priority in Uniprot (29). This is the "reference proteome" for E. coli, contains 4303 proteins, and has been annotated here. Our annotation has been formulated in such a way that it can be easily incorporated in Uniprot.
    > EchoLOCATION has an easily accessible table that maps gene names to subcellular locations. However, mapping the gene names given by EchoLOCATION to the respective protein identifiers in Uniprot was not straightforward. Unfortunately, gene names cannot serve as unique identifiers of a protein sequence. In more than 100 cases the gene name of a predicted protein in EchoLOCATION when searched against Uniprot gave as a result more than one K-12 protein hits. That is because there are proteins that have common synonymous gene names with the primary gene name of others.
    > To retrieve updated Uniprot accession identifiers and to map Uniprot accessions identifiers to EchoLOCATION identifiers (termed: EchoBASE IDs) we used the "ID mapping" function of Uniprot. In cases where the only provided identifiers were the gene names, we used mySQL queries to compare with the primary and alternative gene names in Uniprot. In cases where multiple matches existed for the same gene name, we manually resolved the differences based on other information (e.g. protein description, mass etc.).
    > The annotation of pseudogenes, mobile elements, transposons, and insertion elements relied on EcoGene (34), Uniprot (29), and Ochman et al. (35). The list of E. coli K-12 complexes was retrieved from EcoCyc (31) and literature searches.

### [17] Gene Nomenclature System for Rice
- Authors: S. McCouch
- Year: 2008
- Venue: Rice
- URL: https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
- DOI: 10.1007/s12284-008-9004-9
- Citations: 383
- Influential citations: 9
- Summary: A set of standard procedures for describing genes based on DNA, RNA, and protein sequence information that have been annotated and mapped on the sequenced genome assemblies, as well as those determined by biochemical characterization and/or phenotype characterization by way of forward genetics are outlined.
- Evidence snippets:
  - Snippet 1 (score: 0.639)
    > The name of a protein encoded by a particular gene should be consistent with the gene full name in cases where the gene name is based on phenotype or molecular function (refer to the "Gene full name" section), except that the protein name is written using all upper case characters without italics. If, at a later stage, a gene and its corresponding protein product are determined to have a biochemically characterized molecular function, such as an enzyme or a structural component (subunit) of a macromolecular complex, the protein should be assigned a synonym consistent with the enzyme nomenclature recommended by the IUPAC Enzyme Commission or the macromolecule name adapted by the IUBMB [4]. Because there may be several functional assignments for a given protein (i.e., based on a phenotypic assay, a biochemical assay, or a molecular function), there may be several synonyms for the protein name (and similarly, for the gene full name). The protein symbol should always be consistent with the adopted gene symbol, with the exception that protein symbols are written using all upper case characters without italics, followed by a space and the numeric locus designator. For example, the GLUTINOUS ENDOSPERM 1 (WX1) gene encodes the granule-bound starch synthase enzyme (EC: 2.4.1.11). The protein name is GLUTINOUS ENDOSPERM 1 and the symbol is 'WX1'. The protein name(s), 'WAXY', 'WAXY 1', and GRANULE-BOUND STARCH SYNTHASE (GBSS) will be recorded as synonyms. If a name cannot be assigned based on phenotype, known biochemistry, or other experimental evidence supporting its function, a systematic locus identifier (described above) and a name consistent with the description in Table 1 must be used to describe the gene until its function can be confirmed.

### [18] A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi
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
  - Snippet 1 (score: 0.638)
    > In an effort to engage the collective expertise of the scientific community, we have implemented a collaborative wiki (MediaWiki version 1.19.11) for the Mnemiopsis gene complement. The Mnemiopsis Gene Wiki is accessible from the left sidebar of most pages and is searchable either by selecting a Mnemiopsis gene identifier (e.g., ML00011a) from the drop-down menu or by manually entering an identifier in the appropriate search box. Users can also access these pages by clicking on a gene in the 2.2 track of the genome browser. Each record in the Gene Wiki represents a single Mnemiopsis gene and provides the following annotation: nucleotide and protein sequences, coding exonic genomic coordinates, pre-computed BLAST hits from numerous organisms displaying the top hits for each protein, the top non-self BLAST hit to Mnemiopsis, Pfam-A domains, Gene Ontology (GO) functional annotations, human disease genes from Online Mendelian Inheritance in Man (OMIM), and a table of ortholog clusters formed by phylogenetically informed clustering methods [4] (Figure 5). In addition, controlled editable sections have been included that permit (and encourage) the scientific community to provide further gene annotation for isoforms, in situ images, references, and other notes for each gene. Users interested in supplementing our gene model annotation at the Mnemiopsis Gene Wiki pages must first create an account and log in prior to submitting their contributions. In-house subject matter expert data curators are notified by e-mail following the creation of a new user account or an edit to an existing Gene Wiki record. Any content changes or additions to the Gene Wiki are thoroughly evaluated by these data curators and are made public subject to their approval.
    > Pre-compiled BLAST hits are enumerated in tabular form. Each Mnemiopsis protein was compared to the UniProt and NCBI non-redundant protein databases (nr) using BLASTP. The results display the hit number, the accession numbers, E-values, and brief descriptions of the top four hits (lowest E-values). Accession numbers are linked to relevant corresponding entries at UniProt and GenBank.

### [19] The automatic annotation of bacterial genomes
- Authors: Emily J. Richardson, M. Watson
- Year: 2012
- Venue: Briefings in Bioinformatics
- URL: https://www.semanticscholar.org/paper/4cdc5583359a37c93782f34ad5cf9dbd83359fd6
- DOI: 10.1093/bib/bbs007
- PMID: 22408191
- PMCID: 3548604
- Citations: 151
- Influential citations: 8
- Summary: The automatic and manual annotation of bacterial genomes is discussed, common problems introduced by the current genome annotation process are identified and potential solutions are suggested.
- Evidence snippets:
  - Snippet 1 (score: 0.638)
    > There are 128 proteins in UniProt that contain the word 'syntase', an incorrect spelling of the word 'synthase'. To put this into context, the RefSeq entry for Rhizobium etli CFN 42 (accession NC_007761) assigns the function 'dihydrofolate syntase' to gene folC. This has propagated into other databases such as UniProt (accession: Q2KE79), KEGG (accession: RHE_CH00024), and xBASE (accession: RHE_CH00024). If a user was to visit any of these databases and search for 'dihydrofolate synthase' the misspelled entries would be omitted from the search results. Large scale detection and correction of spelling mistakes in public databases is a difficult task, and so there is a reliance on the submitter to correct these. Automatic annotation pipelines simply copy and propagate what is there already. Spelling mistakes may be highlighted by the validation software provided by the public databases during submission, however, an alternative correct spelling isn't offered, making it difficult to amend the mistakes without manual intervention.
    > This can be solved by writing rules to find spelling mistakes [16]. However, this approach is limited to spelling mistakes which are explicitly written in the code. A solution may exist beyond biological science. The search engine Google upon receiving the input 'syntase' automatically states 'Did you mean: synthase'. There are programming languages which have classes or plugins to produce such 'did you mean' results [50,51]. 'Same gene name, different product name'
    > This issue occurs when two features, either within or between genomes, are assigned the same short gene name yet different product names. The NCBI validation software specifically highlights when this occurs intra-genomically with the description 'Same gene name, different product name' [9,10]. In the current set of 2696 microbial genome and plasmid sequences in RefSeq, we detected 23,843 genes with at least two different product names (see http:// www.ark-genomics.org/genomeannotation.html for the full list).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
4. Stefania D'Alessio, Katherine M. Buckley, I. Kraev, P. Hayes, S. Lange (2021). Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology. Biology. https://www.semanticscholar.org/paper/e2b33d9697175a6e724fdb85e3ac2ec169d92871
5. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
6. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
7. Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al. (2023). Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
8. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
9. J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al. (2025). Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains. Scientific Reports. https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
10. S. Chakraborty, P. Martínez-García, A. Dandekar (2016). YeATSAM analysis of the walnut and chickpea transcriptome reveals key genes undetected by current annotation tools. F1000Research. https://www.semanticscholar.org/paper/0b0afbfabeba7d3a90e11f6ce97418c3f8c7f71f
11. Jaap van der Heijden, Asanda Mazubane, Marko Sallisalmi, E. Vorontsov, J. Tenhunen et al. (2025). Plasma proteomics in septic shock and alcohol-related pancreatitis: a hyaluronan-centered approach. Clinical Proteomics. https://www.semanticscholar.org/paper/ae917565de913693a2713b46c3eda672d9d01c7f
12. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
13. Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel (2023). An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México. Microorganisms. https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
14. Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
15. Seth B Roberts, Christopher M. Gowen, J. Brooks, Stephen S. Fong (2010). Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production. BMC Systems Biology. https://www.semanticscholar.org/paper/dc66757785ecb9e1d1760f67f5410dddb5d3618c
16. Georgia Orfanoudaki, A. Economou (2014). Proteome-wide Subcellular Topologies of E. coli Polypeptides Database (STEPdb)*. Molecular & Cellular Proteomics. https://www.semanticscholar.org/paper/8e452aca415b30d995ba9f977086924c8fed8f19
17. S. McCouch (2008). Gene Nomenclature System for Rice. Rice. https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
18. R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al. (2014). A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi. BMC Genomics. https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
19. Emily J. Richardson, M. Watson (2012). The automatic annotation of bacterial genomes. Briefings in Bioinformatics. https://www.semanticscholar.org/paper/4cdc5583359a37c93782f34ad5cf9dbd83359fd6