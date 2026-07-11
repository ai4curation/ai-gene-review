---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T09:27:11.468641'
end_time: '2026-07-09T09:27:16.199640'
duration_seconds: 4.73
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rpmF
  gene_symbol: rpmF
  uniprot_accession: Q88LL9
  protein_description: 'RecName: Full=Large ribosomal subunit protein bL32 {ECO:0000255|HAMAP-Rule:MF_00340};
    AltName: Full=50S ribosomal protein L32 {ECO:0000305};'
  gene_info: Name=rpmF {ECO:0000255|HAMAP-Rule:MF_00340}; OrderedLocusNames=PP_1911;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial ribosomal protein bL32 family.
  protein_domains: Ribosomal_bL32. (IPR002677); Ribosomal_bL32_bact. (IPR044957);
    Ribosomal_zn-bd. (IPR011332); Ribosomal_L32p (PF01783)
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
- **UniProt Accession:** Q88LL9
- **Protein Description:** RecName: Full=Large ribosomal subunit protein bL32 {ECO:0000255|HAMAP-Rule:MF_00340}; AltName: Full=50S ribosomal protein L32 {ECO:0000305};
- **Gene Information:** Name=rpmF {ECO:0000255|HAMAP-Rule:MF_00340}; OrderedLocusNames=PP_1911;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial ribosomal protein bL32 family.
- **Key Domains:** Ribosomal_bL32. (IPR002677); Ribosomal_bL32_bact. (IPR044957); Ribosomal_zn-bd. (IPR011332); Ribosomal_L32p (PF01783)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rpmF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rpmF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rpmF** (gene ID: rpmF, UniProt: Q88LL9) in PSEPK.

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

### [1] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.829)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).
  - Snippet 2 (score: 0.727)
    > (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b). Under normal-growth conditions, the most enriched cluster (enrichment score 11.4) comprised genes related to ribonucleoproteins, ribosomes, ribosomal proteins, and translation. The second-most enriched cluster (enrichment score 3.8) comprised genes belonging to protein biosynthesis and tRNA metabolism, including aminoacyl-tRNA synthetases. A third cluster (enrichment score 2.2) comprised genes related to nucleotide-binding proteins. Among the genes with peaks under cold-shock conditions, the same three annotation clusters were identified, with enrichment scores 6.5, 4.1, and 2.5, respectively.
    > We also analyzed the genes identified under both normal-growth and cold-shock conditions, only under normal-growth conditions, or only under cold-shock conditions. (Supplemental Table 4c-e). The same three annotation clusters (ribosome and translation, tRNA metabolism, and nucleotide binding, enrichment scores 6.4, 3.8, and 2.7, respectively) were reported for genes that contained peaks under both normal-growth and cold-shock conditions. Genes with peaks only under normal-growth conditions were enriched for genes related to ribosomes and translation, genes with peaks only under cold-shock conditions showed no specific enrichment. Genes that neither contained a peak under normal-growth nor under coldshock conditions also showed no significant enrichment of a particular family of proteins (Supplemental Table 4f).
    > As an example for genes related to annotation cluster 1, 18 out of the 22 genes (82%) for proteins of the 30S ribosomal subunit were identified under normal-growth conditions, 12 (55%) after cold shock (11 common genes, three without peaks). For the proteins of the 50S ribosomal subunit, the picture was similar: Out of 34 genes, 31 (91%) were identified under normal-growth, 22 (65%) under coldshock conditions (20 common genes, one without peaks).

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
  - Snippet 1 (score: 0.785)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.706)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [3] Mammalian Annotation Database for improved annotation and functional classification of Omics datasets from less well-annotated organisms
- Authors: Jochen T. Bick, Shuqin Zeng, M. Robinson, S. Ulbrich, S. Bauersachs
- Year: 2019
- Venue: Database: The Journal of Biological Databases and Curation
- URL: https://www.semanticscholar.org/paper/e0716471510abb041c775418ffa9cea283a8c47c
- DOI: 10.1093/database/baz086
- PMID: 31353404
- PMCID: 6661403
- Citations: 16
- Summary: The developed Mammalian Annotation Database tool (MAdb) showed clearly improved overrepresentation analysis results based on the assigned human homologous gene identifiers and a new tool (AnnOverlappeR) for the reliable assignment of the National Center for Biotechnology Information and Ensembl gene IDs.
- Evidence snippets:
  - Snippet 1 (score: 0.759)
    > In transcriptomics and proteomics studies, one important step of data analysis is the functional annotation of obtained lists of differentially expressed genes (DEGs) or proteins (DEPs). With the increase in the number of organisms with sequenced and annotated genomes, such studies have been performed in many different species. However, the information about gene and protein functions, on which the annotation is based, is mainly derived from a limited number of model organisms or well-annotated species, such as mouse, humans and rat representing mammalian species or even from bacteria, yeast, worms or Drosophila. Based on the assumption that orthologous genes carry out identical or biologically equivalent functions in different organisms, functional annotation is transferred from wellstudied organisms to less well-annotated species (1). Whereas orthologous genes usually have maintained the same function during evolution (2) paralogous genes originated from gene duplication events and often evolved different functions (3,4). Orthologous genes usually have the same gene symbol and name for almost all corresponding species (5, 6). However, depending on the status of the gene annotation of a species, not all annotated genes have an official gene symbol (only locus number, e.g. LOC100152218 60S ribosomal protein L23a-like) and/or are assigned to functional annotation databases like their corresponding orthologs in the well-annotated model organisms. This leads to a substantial loss of information if the gene identifiers (IDs) of the respective species are used for functional annotation. To avoid this data loss and improve the results of functional annotation, one strategy is to transfer information from homologous genes (orthologs and paralogs) of well-annotated species (6).
    > In many situations with non-model species such as livestock species, experimentalists avoid the additional work to assign human ortholog genes for functional annotation analysis and are not aware of the information loss.

### [4] GISMO—gene identification using a support vector machine for ORF classification
- Authors: L. Krause, A. Mchardy, T. Nattkemper, A. Pühler, J. Stoye et al.
- Year: 2006
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/cb81798928519b6ed28762411cd7e201dd9e10fe
- DOI: 10.1093/nar/gkl1083
- PMID: 17175534
- PMCID: 1802617
- Citations: 62
- Influential citations: 4
- Summary: Using GISMO, the novel prokaryotic gene finder, several thousand new predictions for the published genomes that are supported by extrinsic evidence are found, which strongly suggest that these are very likely biologically active genes.
- Evidence snippets:
  - Snippet 1 (score: 0.757)
    > GISMO also predicted 99 genes encoding ribosomal proteins that are currently missing from the genome annotations. For example, two novel GISMO predictions for E.coli CFT073 and Wolinella succinogenes DSM 1740 are very similar to the ribosomal protein L32 in E.coli K12 and Helicobacter pylori 26695. The homologs of the two novel predictions and their adjacent genes appear in a conserved order in various organisms (Figure 5). Many of the probably-coding genes are as short as the ribosomal protein-encoding genes, a situation that explains why they were missed before. In summary, our results indicate that a considerable percentage of our additional predictions are novel and currently unknown protein-encoding genes that are missing from the annotations.

### [5] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.740)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [6] Identification of 12 New Yeast Mitochondrial Ribosomal Proteins Including 6 That Have No Prokaryotic Homologues*
- Authors: Cosmin Saveanu, M. Fromont‐Racine, A. Harington, Florence Ricard, A. Namane et al.
- Year: 2001
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/19c21c6d297e524358a1809bfb53fc458763c293
- DOI: 10.1074/JBC.M010864200
- PMID: 11278769
- Citations: 81
- Influential citations: 4
- Summary: It is shown that a subset of the newly described ribosomal proteins are localized in mitochondria and are required for the respiratory competency of the yeast cells, bringing to 26 the total number of proteins described as components of the mitochondrial small Ribosomal subunit.
- Evidence snippets:
  - Snippet 1 (score: 0.739)
    > However, this name does not allow one to discriminate between small and large subunit proteins and thus may be misleading. For example, Mrp2 is not the homologue of the prokaryotic S2 ribosomal proteins but belongs to the S14p family. Accordingly, we preferred to designate the newly identified genes RSMxx genes, where RSM stands for ribosomal small subunit of mitochondria, and xx is the number of the corresponding prokaryotic protein family (see Table II). The genes that encode proteins that are not significantly similar to prokaryotic proteins were named with the same prefix RSM followed by a number that begins with 22, because there are 21 prokaryotic small ribosomal subunit protein families. Thus, the proposed name of the YKL155c gene is RSM22 (Table II). The matched peptide has the sequence VT-PGSLYK. The differences between the masses of the marked peaks correspond to the masses of amino acid residues Gly, Pro, and Thr. D, the fragmentation spectrum for the peptide that is found within residues 400 -408 in the predicted sequence of Ygl129c shows a very good signal-to-noise ratio. Fragmentation spectra that were generated for other peptides show a signal-to-noise ratio between the two extremes shown in C and D.
    > A large amount of functional data was generated in the course of genetic screenings and functional genomic studies in yeast. Hence, for a number of the identified proteins, some cellular or functional data were already available in public data bases. In addition, for some of the less well characterized proteins, we analyzed the cellular localization of the GFP C-terminally tagged proteins and the respiratory competency of strains disrupted for the corresponding genes. These data are summarized in Table II and described below.
    > Functional Data on the New Proteins That Belong to Known Ribosomal Protein Families-Ribosomal protein families S7p and S10p are represented in yeast mitochondria by the corresponding homologues Yjr113c and Ydr041w. Mammalian homologues of S7 (19) and S10 (20) were also recently described as components of the bovine small mitochondrial ribosomal subunit.

### [7] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2774
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.733)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [8] Unaltered maximal power and submaximal performance correlates with an oxidative vastus lateralis proteome phenotype during tapering in male cyclists
- Authors: Pieter de Lange, Giuseppe Petito, H. Notbohm, Antonia Giacco, G. Renzone et al.
- Year: 2025
- Venue: Physiological Reports
- URL: https://www.semanticscholar.org/paper/a0b1b7299cc744296872bad1e07b102cc644c3c1
- DOI: 10.14814/phy2.70302
- PMID: 40265526
- PMCID: 12015642
- Summary: The data indicate that transient 50% training volume reductions may be beneficial for oxidative metabolism in muscle and may be beneficial for oxidative metabolism in muscle.
- Evidence snippets:
  - Snippet 1 (score: 0.726)
    > Reported are UniProtKB accessions, proteins and corresponding gene names, protein abundances at t9 + 2 (Ab t9+2 ) and t11 (Ab t11 ), abundance ratios Ab t9+2 /Ab t11 (9 + 2/11) and corresponding ratio p-values. Proteins belonging to the clusters (C1 and C2) detected by MCODE algorithm (Figure 6a,b 7d), this analysis identified the GO-terms "cytosolic ribosome", "amide biosynthetic process", "ribosome", "cytoplasmic translation", and "translation" as the five (out of a total of seventeen) statistically most significant decreased (p « 0.01), originating from ATP-binding cassette sub-family E member 1 (ABCE1), large ribosomal subunit protein uL15m (RPL15), large ribosomal subunit protein eL22 (RPL22), large ribosomal subunit protein eL14 (RPL14), small ribosomal subunit protein RACK1 (RACK1) and
    > T A B L E 1 0 Pathway and process enrichment (GO-enrichment) analysis applied to the PPI network identified for the over-represented proteins at t9 + 2 in the comparison "t9 + 2 vs. t11". Reported are the four most significantly enriched Gene Ontology terms (including GO-Category, GO-term identifier, description, involved genes, and p-value). long-chain-fatty-acid--CoA ligase (ACSL3). Table S6 reports all information here not included for the comparison "t9 + 2 vs. t11", related to DRPs identification and functional enrichment/PPI network/MCODE analyses.

### [9] Draft genome sequence of type strain HBR26T and description of Rhizobium aethiopicum sp. nov.
- Authors: A. A. Aserse, T. Woyke, N. Kyrpides, W. Whitman, K. Lindström
- Year: 2017
- Venue: Standards in Genomic Sciences
- URL: https://www.semanticscholar.org/paper/e1bdbb37e1c501cbf7bf61678c972e140a80414f
- DOI: 10.1186/s40793-017-0220-z
- PMID: 28163823
- PMCID: 5278577
- Citations: 20
- Summary: The genome of type strain HBR26T of R. aethiopicum sp.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > Genes were predicted using Prodigal [46] and using the DOE JGJ annotation pipeline [47]. The identified protein-coding genes were translated and functionally annotated by comparing the sequences with the NCBI non-redundant database, UniProt, TIGRFam, Pfam, KEGG, COG, and InterPro databases. The tRNA genes were found using tRNAScanSE tool [48] and ribosomal RNA genes were identified by searches against models of the ribosomal RNA genes at the SILVA database [49].
    > Other non-coding RNAs such as the RNA components of the protein secretion complex and the RNase P were identified by searching the genome for the corresponding Rfam profiles using INFERNAL [50]. Additional analysis was accomplished using the IMG tool [51]. The same tool was also used for manual functional annotation of the predicted genes and for examining the genome sequence.

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
  - Snippet 1 (score: 0.723)
    > (ii). Annotation of Protein-Coding Genes Among the 33 ORFs encoding proteins with predicted functions were: nine encoding NADH dehydrogenase subunits, one encoding cytochrome b, three encoding cytochrome C oxidase subunits, five encoding ATP synthase subunits, four responsible for cytochrome C maturation, nine encoding ribosomal proteins, and two with other functions (matR and mttB; Table 1, Figure 2). Among these, the cox2, rps3, nad1, nad5, and rpl2 genes were characterized with potential mutations due to single nucleotide polymorphisms (SNPs). The rpl2 sequence from the VIK32, line MlS-1 mtDNA showed identity with exon 2 of the chloroplast gene encoding ribosomal protein L2. For example, it showed identity with an exon of the line MlS-1 chloroplast gene rplB (OR674883.1; coordinates 78,587-79,084; Cover 69%, Identity 98.3%) (Figure 3), as well as with exon 2 of the chloroplast gene rpl2 from M. lupulina (OM681370.1; Cover 72%, Identity 98.4%) and M. truncatula cultivar Jemalong A17 (MT965675.1; Cover 72%, Identity 97.5%). This sequence also showed high similarity to sequences from the chloroplast genomes of phylogenetically distant plants from the genera Trigonella, Melilotus, Lathyrus, and Pisum (Cover 97%, Identity 95.6-96.2%). The 45 protein-coding genes were characterized as genes encoding hypothetical proteins (Figure 2).

### [11] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.718)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [12] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.717)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [13] Permanent draft genome of Thermithiobaclillus tepidarius DSM 3134T, a moderately thermophilic, obligately chemolithoautotrophic member of the Acidithiobacillia
- Authors: R. Boden, L. Hutt, Marcel Huntemann, Alicia Clum, Manoj Pillay et al.
- Year: 2016
- Venue: Standards in Genomic Sciences
- URL: https://www.semanticscholar.org/paper/f2117c6922312a227e69b8448f807915356842c9
- DOI: 10.1186/s40793-016-0188-0
- PMID: 27708749
- PMCID: 5037610
- Citations: 20
- Influential citations: 1
- Summary: It is speculated that DUF302 and sox genes may have a role in periplasmic trithionate oxidation, as the Kelly-Friedrich pathway of thiosulfate oxidation is not used in Thermithiobacillus spp.
- Evidence snippets:
  - Snippet 1 (score: 0.716)
    > Genes were identified using Prodigal [18] as part of the DOE-JGI genome annotation pipeline [19]. The predicted CDSs were translated and used to search the National Center for Biotechnology Information non-redundant database, UniProt, TIGR-Fam, Pfam, KEGG, COG, and InterPro database. These data sources were combined to assert a product description for each predicted protein. tRNAScanSE was used to find tRNA genes and rRNA genes were found using searches against models of the ribosomal RNA genes built from SIVLA [20,21].
    > Additional gene prediction analysis and functional annotation was performed within the IMG-ER platform [22,23]. For each gene discussed in this publication, the annotation was manually checked against the Gen-Bank® databased manual searches using the BLASTn and BLASTp algorithms -both of the gene from T. tepidarius and using the equivalent gene from members of the Acidithiobacillia or Escherichia coli.

### [14] De Novo Genome Assembly and Phylogenetic Analysis of Cirsium nipponicum
- Authors: Bae Young Choi, Jaewook Kim, Hyeonseon Park, Jincheol Kim, Seahee Han et al.
- Year: 2024
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/658e8e30fac9b7c176a0e8e3f095d9f58b9c93a0
- DOI: 10.3390/genes15101269
- PMID: 39457393
- PMCID: 11507141
- Summary: This study provides a reference genome of C. nipponicum, enhancing the understanding of its genetic background and facilitating an exploration of genetic resources for beneficial phytochemicals.
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > accessed on 23 March 2016). GeneMarkS-T was employed to predict genes in the unique isoforms [31]. Finally, all predicted gene models were combined to produce non-redundant and consensus gene sets using TSEBRA [23].
    > Functional annotation of protein-coding genes were conducted using EnTAP v. 1.1.1 [32] with two methods. First, protein sequences of protein-coding genes were subjected to a BLASTp analysis against the NCBI RefSeq database [33] and Uniprot database using DI-AMOND [26,34]. Second, genes were annotated with KEGG terms and GO terms using eggNOG-mapper [35].
    > Transfer RNA (tRNA) genes were annotated using tRNAscan-SE v. 2.0.12 with eukaryote parameters [36]. Ribosomal RNA (rRNA) and its subunits were identified using Barrnap v. 0.9 in Eukaryotic mode [37]. To detect microRNA (miRNA) and small nuclear RNA (snRNA), sequence analysis was conducted by comparing against the Rfam database using Infernal's cmscan v. 1.1.5 [38,39].

### [15] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.713)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [16] Basidioascus undulatus: genome, origins, and sexuality
- Authors: Hai D. T. Nguyen, D. Chabot, Y. Hirooka, R. Roberson, K. Seifert
- Year: 2015
- Venue: IMA Fungus
- URL: https://www.semanticscholar.org/paper/a5deb29da5109780b4d55dfa35ea0d9fe13216d5
- DOI: 10.5598/imafungus.2015.06.01.14
- PMID: 26203425
- PMCID: 4500085
- Citations: 12
- Influential citations: 1
- Summary: Nuclear staining and confocal microscopy showed meiosis occurring in basidia and genome analysis confirmed the existence of genes involved in meiosis and mating, leading to a move out of the Wallemiomycetes and into the new class Geminibasidiales cl. nov.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > run on the scaffolds to detect the percentage of conserved eukaryotic genes (CEGs).
    > Genome annotation was performed following established guidelines (Haas et al. 2011 (Slater & Birney 2005). Predicted gene models exhibiting strong evidence by exon alignment were exported as protein sequences and coding nucleotide sequences (CDS). Predicted gene models lacking evidence from exon alignment were discarded in downstream analyses. To determine function, the protein sequences were used as input for InterProScan 5RC6 (Jones et al. 2014) (parameters: -dp -f -t p -iprlookup -pa -goterms) and were also compared to the manually curated protein data set from UniProt/Swiss-Prot by blastp v. 2.2.28+. The results in XML format from blastp v. 2.2.28+ and InterProScan were loaded into Blast2GO v. 2.7.1 (Conesa et al. 2005) and merged to create an annotation table (available from the first author on request). The gene models with BLAST hits having e-value of less than 1.0E -100 and mean similarity hit of ≥ 70% were assumed to be orthologs and they were given names following recommended conventions (http:// www.uniprot.org/docs/proknameprot). Ribosomal RNA's were predicted by RNAmmer v. 1.2 (Lagesen et al. 2007). Data files are publicly available at NCBI (Genome Accession No. JTLS00000000 version JTLS01000000; BioProject Accession No. PRJNA247992) and JGI MycoCosm portal (Grigoriev et al. 2014).

### [17] The Oxytricha trifallax Macronuclear Genome: A Complex Eukaryotic Genome with 16,000 Tiny Chromosomes
- Authors: E. Swart, J. Bracht, V. Magrini, P. Minx, Xiao Chen et al.
- Year: 2013
- Venue: PLoS Biology
- URL: https://www.semanticscholar.org/paper/757a5557a078925a0e54425d7e2f0dc265f1e92f
- DOI: 10.1371/journal.pbio.1001473
- PMID: 23382650
- PMCID: 3558436
- Citations: 226
- Influential citations: 20
- Summary: With more chromosomes than any other sequenced genome, the macronuclear genome of Oxytricha trifallax has a unique and complex architecture, including alternative fragmentation and predominantly single-gene chromosomes.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > Table S20 Small ribosomal proteins. Gene identifiers are given as contig identifiers with a gene suffix beginning with ''g'' followed by a number (which is arbitrary in this context). Only proteins #100 aa with domains found in Pfam 26.0 with an Evalue,0.01 and with some homologs in UniProt that are #120 aa (to ensure that they are genuine small proteins) are listed. Where alternative fragmentation occurs, the nanochromosome length of the shortest putative isoform encoding the small protein is shown. Protein domains are taken from Pfam 26.0. Contig22302.0 is a multigene nanochromosome. a These proteins are incorrectly predicted as gene fusions on the longer ribosomal/nonribosomal protein-encoding nanochromosome. (RTF) Table S21 Small nonribosomal proteins. Gene identifiers are given as contig identifiers with a gene suffix beginning with ''g'' followed by a number (which is arbitrary in this context). All nanochromosomes in this table longer than 1 kb are predicted to be multigene nanochromosomes. Proteins 50-100 aa long with domains found in Pfam 26.0 (independent E-value,0.01) and with at least some homologs in UniProt that are #120 aa (to ensure that they are genuine small proteins) are listed. We excluded a few proteins that appeared to be truncated by incomplete assembly of their nanochromosomes. Nanochromosome lengths exclude telomeres. Where alternative fragmentation occurs, the nanochromosome length of the shortest putative isoform encoding the small protein is shown. Protein domain names are from Pfam 26.0. (RTF) Table S22 RNA-seq counts for transcription initiation factor II domain protein genes. RNA expression values are given in normalized read counts for vegetative (''Fed'') cells and cells developing during conjugation (see Text S1: RNA-seq mapping and read counting).

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
  - Snippet 1 (score: 0.708)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. Jochen T. Bick, Shuqin Zeng, M. Robinson, S. Ulbrich, S. Bauersachs (2019). Mammalian Annotation Database for improved annotation and functional classification of Omics datasets from less well-annotated organisms. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/e0716471510abb041c775418ffa9cea283a8c47c
4. L. Krause, A. Mchardy, T. Nattkemper, A. Pühler, J. Stoye et al. (2006). GISMO—gene identification using a support vector machine for ORF classification. Nucleic Acids Research. https://www.semanticscholar.org/paper/cb81798928519b6ed28762411cd7e201dd9e10fe
5. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
6. Cosmin Saveanu, M. Fromont‐Racine, A. Harington, Florence Ricard, A. Namane et al. (2001). Identification of 12 New Yeast Mitochondrial Ribosomal Proteins Including 6 That Have No Prokaryotic Homologues*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/19c21c6d297e524358a1809bfb53fc458763c293
7. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
8. Pieter de Lange, Giuseppe Petito, H. Notbohm, Antonia Giacco, G. Renzone et al. (2025). Unaltered maximal power and submaximal performance correlates with an oxidative vastus lateralis proteome phenotype during tapering in male cyclists. Physiological Reports. https://www.semanticscholar.org/paper/a0b1b7299cc744296872bad1e07b102cc644c3c1
9. A. A. Aserse, T. Woyke, N. Kyrpides, W. Whitman, K. Lindström (2017). Draft genome sequence of type strain HBR26T and description of Rhizobium aethiopicum sp. nov.. Standards in Genomic Sciences. https://www.semanticscholar.org/paper/e1bdbb37e1c501cbf7bf61678c972e140a80414f
10. M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al. (2025). Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
11. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
12. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
13. R. Boden, L. Hutt, Marcel Huntemann, Alicia Clum, Manoj Pillay et al. (2016). Permanent draft genome of Thermithiobaclillus tepidarius DSM 3134T, a moderately thermophilic, obligately chemolithoautotrophic member of the Acidithiobacillia. Standards in Genomic Sciences. https://www.semanticscholar.org/paper/f2117c6922312a227e69b8448f807915356842c9
14. Bae Young Choi, Jaewook Kim, Hyeonseon Park, Jincheol Kim, Seahee Han et al. (2024). De Novo Genome Assembly and Phylogenetic Analysis of Cirsium nipponicum. Genes. https://www.semanticscholar.org/paper/658e8e30fac9b7c176a0e8e3f095d9f58b9c93a0
15. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
16. Hai D. T. Nguyen, D. Chabot, Y. Hirooka, R. Roberson, K. Seifert (2015). Basidioascus undulatus: genome, origins, and sexuality. IMA Fungus. https://www.semanticscholar.org/paper/a5deb29da5109780b4d55dfa35ea0d9fe13216d5
17. E. Swart, J. Bracht, V. Magrini, P. Minx, Xiao Chen et al. (2013). The Oxytricha trifallax Macronuclear Genome: A Complex Eukaryotic Genome with 16,000 Tiny Chromosomes. PLoS Biology. https://www.semanticscholar.org/paper/757a5557a078925a0e54425d7e2f0dc265f1e92f
18. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211