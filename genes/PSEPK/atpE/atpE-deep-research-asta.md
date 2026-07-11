---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T06:05:20.744610'
end_time: '2026-07-07T06:05:26.871278'
duration_seconds: 6.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: atpE
  gene_symbol: atpE
  uniprot_accession: Q88BW9
  protein_description: 'RecName: Full=ATP synthase subunit c {ECO:0000255|HAMAP-Rule:MF_01396};
    AltName: Full=ATP synthase F(0) sector subunit c {ECO:0000255|HAMAP-Rule:MF_01396};
    AltName: Full=F-type ATPase subunit c {ECO:0000255|HAMAP-Rule:MF_01396}; Short=F-ATPase
    subunit c {ECO:0000255|HAMAP-Rule:MF_01396}; AltName: Full=Lipid-binding protein
    {ECO:0000255|HAMAP-Rule:MF_01396};'
  gene_info: Name=atpE {ECO:0000255|HAMAP-Rule:MF_01396}; OrderedLocusNames=PP_5418;
    ORFNames=PP5418;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATPase C chain family. {ECO:0000255|HAMAP-
  protein_domains: ATP_synth_csu_bac/chlpt. (IPR005953); ATP_synth_F0_csu. (IPR000454);
    ATP_synth_F0_csu_DDCD_BS. (IPR020537); ATP_synth_F0_csu_sf. (IPR038662); ATPase_proteolipid_c-like_dom.
    (IPR002379)
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
- **UniProt Accession:** Q88BW9
- **Protein Description:** RecName: Full=ATP synthase subunit c {ECO:0000255|HAMAP-Rule:MF_01396}; AltName: Full=ATP synthase F(0) sector subunit c {ECO:0000255|HAMAP-Rule:MF_01396}; AltName: Full=F-type ATPase subunit c {ECO:0000255|HAMAP-Rule:MF_01396}; Short=F-ATPase subunit c {ECO:0000255|HAMAP-Rule:MF_01396}; AltName: Full=Lipid-binding protein {ECO:0000255|HAMAP-Rule:MF_01396};
- **Gene Information:** Name=atpE {ECO:0000255|HAMAP-Rule:MF_01396}; OrderedLocusNames=PP_5418; ORFNames=PP5418;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATPase C chain family. {ECO:0000255|HAMAP-
- **Key Domains:** ATP_synth_csu_bac/chlpt. (IPR005953); ATP_synth_F0_csu. (IPR000454); ATP_synth_F0_csu_DDCD_BS. (IPR020537); ATP_synth_F0_csu_sf. (IPR038662); ATPase_proteolipid_c-like_dom. (IPR002379)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atpE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atpE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atpE** (gene ID: atpE, UniProt: Q88BW9) in PSEPK.

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
  - Snippet 1 (score: 0.787)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.667)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology
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
  - Snippet 1 (score: 0.743)
    > For the detection of a putative PAD homologue from sea urchins, anti-human PAD2-specific antibody was used in Western blotting to assess any cross-reaction with a (B) KEGG pathways identified from STRING analysis for EV total protein cargo (annotated hits). (C) Gene Ontology (GO) Biological processes identified from STRING analysis for total EV protein cargo (annotated hits). (D) GO Molecular Function pathways identified from STRING analysis for total EV protein cargo (annotated hits; protein names of hits are presented in the figures; additional interacting proteins are: LOC579085 = ATP synthase subunit gamma, mitochondrial; LOC587430 = ATP synthase subunit O, mitochondrial; LOC373382 = ATP synthase subunit alpha; LOC576006 = ATP synthase subunit delta, mitochondrial; LOC579751 = ATP synthase F(0) complex subunit B1, mitochondrial).

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
  - Snippet 1 (score: 0.731)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.688)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [6] Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control
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
  - Snippet 1 (score: 0.688)
    > Some energy metabolism-related enzymes, such as isocitrate dehydrogenase (IDH), cytochrome c oxidase subunit 1 (Cox 1) and ATP synthase, were also up-regulated in C. hexasticha. for this study, while those of C. uncinata were adopted from [7]. The yellow boxes represent the upregulated genes, while the blue boxes represent down-expressed genes. The full names of protein products of these annotated genes are TUB: tubulin, ISCU: iron-sulfur cluster assembly scaffold protein IscU-like; ISCB: 2 iron, 2 sulfur cluster-binding protein, IDH: isocitrate dehydrogenase, Cox1: cytochrome c oxidase subunit 1, ATP5D: ATP synthase F1, delta subunit, OGC: 2oxoglutarate/malate carrier protein, ABC: ABC transporter family protein, ATPase: v-type ATPase subunit family protein, HSP: heat shock protein, ACP: acyl carrier protein, DNAH7: dynein heavy chain 7.

### [7] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
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
  - Snippet 1 (score: 0.684)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [8] A Na+ A1AO ATP synthase with a V‐type c subunit in a mesophilic bacterium
- Authors: Dennis Litty, V. Müller
- Year: 2019
- Venue: The FEBS Journal
- URL: https://www.semanticscholar.org/paper/0d8c321b4d6ef856523c256b1798b4c020a347ec
- DOI: 10.1111/febs.15193
- PMID: 31876375
- Citations: 9
- Summary: The Na+ A1AO ATP synthase from E. limosum is the first ATP synth enzyme with a V‐type c subunit from a mesophilic organism, and will enable future bioenergetic analysis of these unique ATP synthases.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > Eli_2187 (606 bp) is located 36 bp downstream of Eli_2186, and the deduced protein (22.6 kDa) is annotated as subunit E of V 1 V O ATPases. No significant homology to the corresponding protein sequence of subunit E in A 1 A O ATP synthases was found. Four base pair downstream of Eli_2187 is the 972-bp-long gene Eli_2188 which encodes for a subunit C with a molecular mass of 36.4 kDa. The identity/similarity of the deduced protein is 26/47% to subunit C of the A 1 A O ATP synthase from P. furiosus [12]. Ten base pair downstream of Eli_2188 is 318-bp-long Eli_2189 which encodes a polypeptide with a molecular mass of 11.3 kDa. 51/ 27% of the residues are similar/identical to subunit F of the A 1 A O ATPase from M. barkeri [20]. Eli_2190 (1806 bp) is located 26 bp downstream of Eli_2189 and encodes for subunit A with a molecular mass of 66.8 kDa. The deduced gene product is 59% identical to the corresponding subunit from M. jannaschii and T. onnurineus. Eli_2191 (1410 bp) encodes for subunit B with a molecular mass of 52.3 kDa. 71, 67, and 30% of the residues are identical to subunit B of the A 1 A O ATPase from P. furiosus, T. onnurineus, and M. barkeri, respectively. Four base pair downstream of Eli_2191 is Eli_2192 with a length of 636 bp. The protein has a molecular mass of 29.4 kDa. Sequence alignments showed 42% and 39% identity to subunit D of M. jannaschii and T. onnurineus, respectively. The next gene downstream of the putative ATP synthase operon Eli_2193 (138 bp) is located in 3 0 ? 5 0 direction. For this gene, no homologues were found.

### [9] Gene Nomenclature System for Rice
- Authors: S. McCouch
- Year: 2008
- Venue: Rice
- URL: https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
- DOI: 10.1007/s12284-008-9004-9
- Citations: 383
- Influential citations: 9
- Summary: A set of standard procedures for describing genes based on DNA, RNA, and protein sequence information that have been annotated and mapped on the sequenced genome assemblies, as well as those determined by biochemical characterization and/or phenotype characterization by way of forward genetics are outlined.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > The name of a protein encoded by a particular gene should be consistent with the gene full name in cases where the gene name is based on phenotype or molecular function (refer to the "Gene full name" section), except that the protein name is written using all upper case characters without italics. If, at a later stage, a gene and its corresponding protein product are determined to have a biochemically characterized molecular function, such as an enzyme or a structural component (subunit) of a macromolecular complex, the protein should be assigned a synonym consistent with the enzyme nomenclature recommended by the IUPAC Enzyme Commission or the macromolecule name adapted by the IUBMB [4]. Because there may be several functional assignments for a given protein (i.e., based on a phenotypic assay, a biochemical assay, or a molecular function), there may be several synonyms for the protein name (and similarly, for the gene full name). The protein symbol should always be consistent with the adopted gene symbol, with the exception that protein symbols are written using all upper case characters without italics, followed by a space and the numeric locus designator. For example, the GLUTINOUS ENDOSPERM 1 (WX1) gene encodes the granule-bound starch synthase enzyme (EC: 2.4.1.11). The protein name is GLUTINOUS ENDOSPERM 1 and the symbol is 'WX1'. The protein name(s), 'WAXY', 'WAXY 1', and GRANULE-BOUND STARCH SYNTHASE (GBSS) will be recorded as synonyms. If a name cannot be assigned based on phenotype, known biochemistry, or other experimental evidence supporting its function, a systematic locus identifier (described above) and a name consistent with the description in Table 1 must be used to describe the gene until its function can be confirmed.

### [10] Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences
- Authors: M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al.
- Year: 2025
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
- DOI: 10.3390/ijms262411830
- PMID: 41465260
- PMCID: 12733082
- Summary: This work establishes a foundation for investigating the role of mitochondrial genome variation in key plant’s phenotypic traits, such as the enhanced responsiveness to arbuscular mycorrhiza observed in this agronomically valuable line of Medicago lupulina L. vulgaris Koch.
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > (ii). Annotation of Protein-Coding Genes Among the 33 ORFs encoding proteins with predicted functions were: nine encoding NADH dehydrogenase subunits, one encoding cytochrome b, three encoding cytochrome C oxidase subunits, five encoding ATP synthase subunits, four responsible for cytochrome C maturation, nine encoding ribosomal proteins, and two with other functions (matR and mttB; Table 1, Figure 2). Among these, the cox2, rps3, nad1, nad5, and rpl2 genes were characterized with potential mutations due to single nucleotide polymorphisms (SNPs). The rpl2 sequence from the VIK32, line MlS-1 mtDNA showed identity with exon 2 of the chloroplast gene encoding ribosomal protein L2. For example, it showed identity with an exon of the line MlS-1 chloroplast gene rplB (OR674883.1; coordinates 78,587-79,084; Cover 69%, Identity 98.3%) (Figure 3), as well as with exon 2 of the chloroplast gene rpl2 from M. lupulina (OM681370.1; Cover 72%, Identity 98.4%) and M. truncatula cultivar Jemalong A17 (MT965675.1; Cover 72%, Identity 97.5%). This sequence also showed high similarity to sequences from the chloroplast genomes of phylogenetically distant plants from the genera Trigonella, Melilotus, Lathyrus, and Pisum (Cover 97%, Identity 95.6-96.2%). The 45 protein-coding genes were characterized as genes encoding hypothetical proteins (Figure 2).

### [11] Evaluation of 6-Hydroxydopamine and Rotenone In Vitro Neurotoxicity on Differentiated SH-SY5Y Cells Using Applied Computational Statistics
- Authors: Rui F. Simões, Paulo J. Oliveira, Teresa Cunha-Oliveira, F. Pereira
- Year: 2022
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/59030907c78858d46692b09591ebb5bdc3eecf65
- DOI: 10.3390/ijms23063009
- PMID: 35328430
- PMCID: 8953223
- Citations: 9
- Summary: Both biochemical and computational analyses resulted in an evident distinction between the neurotoxic effects of 6-hydroxydopamine and rotenone, specifically for the highest concentrations of both compounds.
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > 3.0; Bio-Rad, Hercules, CA, USA).
    > Table 2. List of forward (Fwd) and reverse (Rev) primers used for real time-PCR, respective gene, accession number, and annealing temperature (Ta) for genes used in the calculation of mtDNA copy number and for genes encoding electron transport chain complex and ATP synthase subunits, proteins involved in mitochondrial fission and fusion, antioxidant enzymes, mitochondrial biogenesisrelated gene transcripts, and mitochondrial biogenesis-related gene transcripts. CYB: cytochrome b; B2M: β2 microglobulin; ATP5G1: ATP synthase membrane subunit c locus 1; ATP6: ATP synthase membrane subunit 6; COX1: cytochrome c oxidase I; COX4I1: cytochrome c oxidase subunit 4I1; CYB: cytochrome b; ND5: NADH: Ubiquinone oxidoreductase core subunit 5; NDUFA9: NADH: Ubiquinone oxidoreductase subunit A9; SDHA: succinate dehydrogenase complex flavoprotein subunit A; UQCRC2: ubiquinol-cytochrome c reductase core protein 2; DRP1: dynamin-related protein 1; FIS1: mitochondrial fission 1 protein; MFF: mitochondrial fission factor; MFN1: mitofusin 1; MFN2: mitofusin 2; MIEF2: mitochondrial elongation factor 2; OPA1: optic atrophy 1 protein; CAT: catalase; GPX1: glutathione peroxidase 1; GPX4: glutathione peroxidase 4; SOD1: superoxide dismutase 1; SOD2: superoxide dismutase 2; AMPK: adenosine monophosphate-activated protein kinase; GABPB1: GA binding protein transcription factor subunit beta 1; NRF1: nuclear respiratory factor 1; SIRT1: sirtuin 1; TFAM: mitochondrial transcription factor A.

### [12] Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production
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
  - Snippet 1 (score: 0.669)
    > GPR relationships specify the putative relationship between genes and enzymatic activities in an organism. Following previous work [52], we represented these relationships as Boolean statements. The simplest such statement was: gene A implies reaction X, i.e., gene A -> reaction X. Enzymatic activities associated with protein complexes required more complicated statements, e.g., (gene A or gene B) and (gene C) -> reaction X.
    > To develop the GPR relationships for C. thermocellum, we used the annotations described above and information on protein complexes from UniProt. For each EC number in the C. thermocellum annotations, we searched UniProt [23] to determine whether that EC is associated with protein complexes, and if so, what type of complex exists across different organisms (homodimer, heterotrimer, etc.). Based on this information, and the information in the annotations, we assigned putative GPR relationships for C. thermocellum, conforming to known enzyme complex architecture whenever possible. As a specific example of this process, consider the reaction corresponding to carbamoyl-phosphate synthase ('R_CBPS'), EC 6.3.5.5. Several UniProt entries (e.g., CARA_ECOLI) with this EC number are annotated as being members of a complex composed of two chains, a small glutamine-hydrolyzing chain and a large chain that synthesizes carbamoyl phosphate. We found two C. thermocellum genes annotated as "carbamoyl-phosphate synthase, small subunit" (Cthe_1867, Cthe_0950) and two genes annotated as "carbamoyl-phosphate synthase, large subunit" (Cthe_1868, Cthe_0949). Thus, we expressed the GPR relationship for this reaction as: (Cthe_1867 or Cthe_0950) and (Cthe_1868 or Cthe_0949) -> R_CBPS.

### [13] Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains
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
  - Snippet 1 (score: 0.664)
    > Gene annotation was primarily derived from the S. clavuligerus reference genome in the NCBI database and was annotated using the NCBI Prokaryotic Genome Annotation Pipeline 59 . However, several CA biosynthetic genes were manually corrected based on published literature 9 . For instance, two loci were originally annotated as clavaminate synthase 1 (cas1), but one of these loci is located near the cephamycin C biosynthetic cluster, indicating it was actually cas2. Following this correction, the RefSeq accession numbers of all genes in the reference genome were cross-referenced with the UniProt database to obtain additional annotations 60 . For the mutated genes identified through ICA, protein existence levels were manually assigned based on the UniProt data, including protein existence status, annotation score, similar proteins, and relevant publications.

### [14] An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México
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
  - Snippet 1 (score: 0.655)
    > When a genome is sequenced or a protein is characterized, databases classify the information in different ways using automatic identification or manual annotation. In the UniProt database, an annotation is possibly made using the formal representation proposed in Gene Ontology (GO) under three aspects related to biological knowledge of the proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively. An example of an ATP-binding protein is the subunit α of V-type ATP synthase (A0A8G2FW98) of Picrophilus oshimae DSM 9789. As expected, this protein has other three annotations related to proton transport. Besides that, the DNA helicase (A0A811T524) of Ca. Argoarchaeum ethanivorans has the MF of DNA binding and ATP binding. Interestingly, metal ion binding proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively.

### [15] Isolation and Identification of miRNAs in Jatropha curcas
- Authors: Chun Ming Wang, F. Sun, Lei Li, Peng Liu, Jian Ye et al.
- Year: 2012
- Venue: International Journal of Biological Sciences
- URL: https://www.semanticscholar.org/paper/89362a3bf150081c8260f785de9299194d5e2d22
- DOI: 10.7150/ijbs.3676
- PMID: 22419887
- PMCID: 3303143
- Citations: 29
- Influential citations: 2
- Summary: To identify miRNAs in Jatropha curcas L, a bioenergy crop, cDNA clones from two small RNA libraries of leaves and seeds were sequenced and analyzed using bioinformatic tools, indicating diverse functions of JcumiR004.
- Evidence snippets:
  - Snippet 1 (score: 0.654)
    > The 28 ESTs of putative targets were used to search for similar protein sequences in the Uniprot database (BLASTX). The functional information is presented in Additional file 2: Supplementary Table 1. Using the best hits found by BLASTX, an inferred gene ontology annotation was found for 16 of the sequences through QuickGO. Using GO Slimmer in AmiGO database, of the 16 known functional ESTs, one was associated with genes belonging to biological process, 7 with cellular component, and 8 with molecular function. The result showed that the miRNA target genes encoded a broad range of proteins, with majority (15/16) of the predicted protein products involved in molecular function and cellular compo-nent ontologies. The predicted protein description of the target EST sequences were listed in Additional file 2: Supplementary Table 1, with some interesting proteins such as DNA cross-link repair protein, vacuolar ATP synthase proteolipid, elongation factor 1-alpha, Cytochrome c-type biogenesis protein, 14-3-3 protein, heat stress transcription factor A-5, etc. Thus, the miRNA target genes encode a broad range of proteins.

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
  - Snippet 1 (score: 0.654)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [17] Escherichia coli F1Fo-ATP Synthase with a b/δ Fusion Protein Allows Analysis of the Function of the Individual b Subunits*
- Authors: C. Gajadeera, J. Weber
- Year: 2013
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/d6e7ac8b54142570af6f71a319c1c47c7df37428
- DOI: 10.1074/jbc.M113.503722
- PMID: 23893411
- Citations: 13
- Influential citations: 1
- Summary: It is shown that it is possible to generate a functional E. coli ATP synthase containing a b/δ fusion protein, which allowed the analysis of the roles of the individual b subunits.
- Evidence snippets:
  - Snippet 1 (score: 0.653)
    > The Function of Each of the b Subunits-The finding that in E. coli dimerization of b is required for binding to F 1 (31) certainly suggests that both b subunits are contributing to this function. On the other hand, in chloroplasts and some bacteria the C-terminal helix of b, which appears to be most directly involved in the contacts to ␦ (10, 15-17), is missing, indicating that at least in those organisms one of the b subunits might play a less prominent role in binding of ␦ and F 1 . Similarly, it is not known whether both b subunits are required for binding to a.
    > To answer the question of the role of each b subunit, we first generated strain pCG12/DK8 which contains the gene for the hybrid b/␦ fusion protein (but not that for the additional b subunit), with the DNA sequence encoding the transmembrane helix of the fusion protein deleted. As expected, without the possibility to anchor the fusion protein (independent whether monomeric or dimeric) to a, (b ⌬N /␦) ATP synthase fails to assemble. Neither membrane-bound F 1 nor any ATP synthase activity could be detected. In contrast, activity could be restored when the b gene was added to pCG12, to give pCG13. Strain pCG13/DK8 expressed a functional b(b ⌬N /␦) ATP synthase, which showed a level of expression (and/or stability) and activity very similar to the b(b/␦) enzyme (Table 2), demonstrating that a single transmembrane helix is sufficient to anchor the stator stalk to the a subunit and F o .
    > As mentioned above, in mycobacteria the b subunit contained in the fusion protein is of the full-length b type, whereas the additional b subunit is of the shorter bЈ variety. To test whether it is possible to omit the C-terminal helix in the additional b subunit in E. coli ATP synthase containing the b/␦ fusion protein, thereby essentially generating a bЈ subunit, we engineered plasmid pCG16.

### [18] Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale
- Authors: P. Kramer, Jack Treml
- Year: 2022
- Venue: Midwestern Journal of Undergraduate Sciences
- URL: https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27
- DOI: 10.17161/mjusc.v1i1.18565
- Summary: The following is a walkthrough of a project designed to overcome the lack of sense for proteins as real objects.
- Evidence snippets:
  - Snippet 1 (score: 0.649)
    > i. Click "See more" to view a bar chart containing data on where in the body's tissues the gene is expressed (as determined by RNA sequencing). Save and include this bar chart as the deliverable for this step.
    > II. Universal Protein Research Knowledgebase (UniProtKB) 8 6. UniProt Entry Number
    > i. Follow the UniProt link in the Resources then search for the protein using the NCBI Gene ID ii. Carefully select the result that best matches the gene and organism of interest by clicking on the blue entry number. iii. This page will be used later to gather further details about the protein.
    > III. RCSB Protein Data Bank (PDB) 9 7. RCSB PDB Solved Structure Identifi er i. Follow the RCSB PDB link in the Resources and search for the protein by either the common name or the NCBI Gene ID, making sure to select the organism of interest on the left. ii. You must ensure that your chosen protein has an existing solved structure in this data bank in order to do a mutational analysis in later parts of this exercise.
    > IV. NCBI GenBank 10 8. AA Protein Sequence i. From the NCBI Gene page, go to the "Genomic regions, transcripts, and products" section and then click "GenBank" on the right. Scroll down to the fi rst Coding Sequence "CDS" section and look directly after "/translation=" for the full protein sequence. ii. Sequence needs to be in FASTA Format consisting of '>' followed by a simple name, a return, and then the sequence in one continuous line of text. See "FASTA Formatting" link in Resources.

### [19] Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts
- Authors: J. Doolittle, S. Gomez
- Year: 2011
- Venue: PLoS Neglected Tropical Diseases
- URL: https://www.semanticscholar.org/paper/baff9e82a73e77a021118c0910a5874568cd60b3
- DOI: 10.1371/journal.pntd.0000954
- PMID: 21358811
- PMCID: 3039688
- Citations: 97
- Influential citations: 2
- Summary: Dengue virus manipulates cellular processes to its advantage through specific interactions with the host's protein interaction network, and the interaction networks presented here provide a set of hypothesis for further experimental investigation into the DENV life cycle as well as potential therapeutic targets.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > Figure S1 GO term enrichment of A. aegypti proteins based on data from Guo et al. [13]. (A) Enriched GO biological process terms. (B) Enriched GO molecular function terms. Light blue bars represent terms for A. aegypti targets, and pink is for terms from DENV-similar proteins. When more than ten terms were enriched for a set of proteins, only the ten most signicant terms are shown. Bonferroni corrected p-values were transformed by -log10. The following abbreviations are used: "translation factor nucleic acid bind" is "translation factor activity nucleic acid binding," and "macromolecular subunit organiz" is "macromolecular complex subunit organization." Found at: doi:10.1371/journal.pntd.0000954.s001 (1.39 MB TIF)  Table S3 Predicted interactions between DENV2 and human after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the target protein's Uniprot accession, Entrez Gene ID, and Symbol; if the target is a known host factor; and if the predicted interaction was already known in the literature. Found at: doi:10.1371/journal.pntd.0000954.s005 (3.01 MB TXT) Table S4 Predicted interactions between DENV2 and A. aegypti after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the D. melanogaster target protein's FlyBase gene number, and Symbol; the A. aegypti target protein's VectorBase protein ID, and Uniprot accession; and if the target is a known host factor. Found at: doi:10.1371/journal.pntd.0000954.s006

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Stefania D'Alessio, Katherine M. Buckley, I. Kraev, P. Hayes, S. Lange (2021). Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology. Biology. https://www.semanticscholar.org/paper/e2b33d9697175a6e724fdb85e3ac2ec169d92871
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
5. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
6. Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al. (2023). Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
7. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
8. Dennis Litty, V. Müller (2019). A Na+ A1AO ATP synthase with a V‐type c subunit in a mesophilic bacterium. The FEBS Journal. https://www.semanticscholar.org/paper/0d8c321b4d6ef856523c256b1798b4c020a347ec
9. S. McCouch (2008). Gene Nomenclature System for Rice. Rice. https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
10. M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al. (2025). Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
11. Rui F. Simões, Paulo J. Oliveira, Teresa Cunha-Oliveira, F. Pereira (2022). Evaluation of 6-Hydroxydopamine and Rotenone In Vitro Neurotoxicity on Differentiated SH-SY5Y Cells Using Applied Computational Statistics. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/59030907c78858d46692b09591ebb5bdc3eecf65
12. Seth B Roberts, Christopher M. Gowen, J. Brooks, Stephen S. Fong (2010). Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production. BMC Systems Biology. https://www.semanticscholar.org/paper/dc66757785ecb9e1d1760f67f5410dddb5d3618c
13. J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al. (2025). Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains. Scientific Reports. https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
14. Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel (2023). An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México. Microorganisms. https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
15. Chun Ming Wang, F. Sun, Lei Li, Peng Liu, Jian Ye et al. (2012). Isolation and Identification of miRNAs in Jatropha curcas. International Journal of Biological Sciences. https://www.semanticscholar.org/paper/89362a3bf150081c8260f785de9299194d5e2d22
16. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
17. C. Gajadeera, J. Weber (2013). Escherichia coli F1Fo-ATP Synthase with a b/δ Fusion Protein Allows Analysis of the Function of the Individual b Subunits*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/d6e7ac8b54142570af6f71a319c1c47c7df37428
18. P. Kramer, Jack Treml (2022). Undergraduate Bioinformatics Conceptualizing Form and Function on a Molecular Scale. Midwestern Journal of Undergraduate Sciences. https://www.semanticscholar.org/paper/58a6af68fc2fd768735d429724ffdd52e16dfb27
19. J. Doolittle, S. Gomez (2011). Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts. PLoS Neglected Tropical Diseases. https://www.semanticscholar.org/paper/baff9e82a73e77a021118c0910a5874568cd60b3