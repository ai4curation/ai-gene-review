---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T11:21:02.949169'
end_time: '2026-07-10T11:21:08.348211'
duration_seconds: 5.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: srmB
  gene_symbol: srmB
  uniprot_accession: Q88ED3
  protein_description: 'SubName: Full=ATP-dependent DEAD-box RNA helicase require
    for 50S ribosomal subunit biogenesis {ECO:0000313|EMBL:AAN70106.1}; EC=2.7.7.-
    {ECO:0000313|EMBL:AAN70106.1};'
  gene_info: Name=srmB {ECO:0000313|EMBL:AAN70106.1}; OrderedLocusNames=PP_4532 {ECO:0000313|EMBL:AAN70106.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DEAD box helicase family.
  protein_domains: DEAD/DEAH_box_helicase_dom. (IPR011545); DEAD/DEAH_RhlB. (IPR044742);
    DEAD_box_RNA_helicase. (IPR050079); Helicase_ATP-bd. (IPR014001); Helicase_C-like.
    (IPR001650)
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
- **UniProt Accession:** Q88ED3
- **Protein Description:** SubName: Full=ATP-dependent DEAD-box RNA helicase require for 50S ribosomal subunit biogenesis {ECO:0000313|EMBL:AAN70106.1}; EC=2.7.7.- {ECO:0000313|EMBL:AAN70106.1};
- **Gene Information:** Name=srmB {ECO:0000313|EMBL:AAN70106.1}; OrderedLocusNames=PP_4532 {ECO:0000313|EMBL:AAN70106.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DEAD box helicase family.
- **Key Domains:** DEAD/DEAH_box_helicase_dom. (IPR011545); DEAD/DEAH_RhlB. (IPR044742); DEAD_box_RNA_helicase. (IPR050079); Helicase_ATP-bd. (IPR014001); Helicase_C-like. (IPR001650)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "srmB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'srmB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **srmB** (gene ID: srmB, UniProt: Q88ED3) in PSEPK.

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

### [1] Plasmodium falciparum DDX31 is DNA helicase localized in nucleolus
- Authors: Rahena Yasmin, M. Chauhan, S. Sourabh, R. Tuteja
- Year: 2019
- Venue: Heliyon
- URL: https://www.semanticscholar.org/paper/693e52918e8f0574cbe3e5386ab130ace5cd107f
- DOI: 10.1016/j.heliyon.2019.e02905
- PMID: 31872112
- PMCID: 6911875
- Citations: 2
- Summary: Malaria is a major infectious disease and is responsible for millions of infections every year. As drug resistance strains of Plasmodium species are emerging, there is an urgent need to understand the parasite biology and identify new drug targets. Helicases are very important enzymes that participate in various nucleic acid metabolic processes. Previously we have reported several putative DEAD box helicases in the genome of Plasmodium falciparum 3D7 strain. In this study, we present biochemi...
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > The DEAD-box proteins belong to SF2 helicases and are involved in various aspects of RNA metabolism, including nuclear transcription, ribosomal biogenesis and nucleocytoplasmic transport in human and yeast (Bates et al., 2005;Cordin et al., 2006;Daugeron and Linder, 1998). Due to the presence of amino acid sequence DEAD (Aspartic Acid-Glutamic Acid--Alanine-Aspartic Acid) in conserved motif II; these proteins are designated as DEAD box proteins. The Has1 proteins are important members of DEAD-box family (Rocak et al., 2005). In yeast Has1 proteins are characterized as the ATP-dependent RNA helicases involved in the biogenesis of 40S and 60S ribosome subunits (Dembowski et al., 2013;Rocak et al., 2005). The genome wide analysis revealed that four members of Has1 family are present in P. falciparum (Tuteja, 2010). Previously we have biochemically characterized PfH69 (Plasmodium falciparum helicase 69 kDa; PF3D7_0630900, homologue of Has1p from P. falciparum) and reported the essentiality of N-terminal region for its enzymatic activities (Prakash and Tuteja, 2010).
    > PF3D7_0721300 is a homologue of Dbp7p (DEAD box protein 7p) in yeast and DDX31 in humans (Tuteja, 2010). In this study we report the biochemical characterization of DDX31 from P. falciparum 3D7 strain. The PfDDX31 gene is 2700 base pairs long and encodes a protein of ~100 kDa. The core region of PfDDX31 designated as PfDDX31C is from 170 to 789 amino acids (620 amino acids) and contains all the characteristic motifs. PfDDX31C has both ssDNA and RNA dependent ATPase activity. PfDDX31C also exhibits the DNA helicase activity but no RNA helicase activity was detectable in PfDDX31C.

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
  - Snippet 1 (score: 0.718)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.668)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [3] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.707)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [4] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.700)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [5] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.695)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [6] Computational Discovery of Transcriptional Regulatory Modules in Fungal Ribosome Biogenesis Genes Reveals Novel Sequence and Function Patterns
- Authors: V. Martyanov, R. H. Gross
- Year: 2013
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/986fb7b3472c53c1891d806144874429471d3d13
- DOI: 10.1371/journal.pone.0059851
- PMID: 23555806
- PMCID: 3612091
- Summary: Several likely new candidates for a role in ribosome biogenesis in S. cerevisiae are identified based on the combined evidence of RBA module presence in the upstream regions, functional annotation information and microarray expression profiles.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > For S. cerevisiae, we used the extra gene feature of SCOPE and identified 12 previously unreported genes containing RBA modules (8 with RRPE-PAC and 4 with PAC-RRPE). By utilizing functional annotation and microarray expression data (see Materials and Methods), we were able to find evidence from at least one other source for 8 genes and from two sources for 4 genes. Based on these analyses, we can hypothesize about several new candidates for a role in ribosome biogenesis in S. cerevisiae.
    > The 4 candidate genes that are most likely involved in RBA (supported as such by SCOPE motif and module data, SGD functional description information and SPELL expression data) are as follows. YDR465C is an arginine methyltransferase that methylates ribosomal protein RPL12. YGR272C is an essential protein required for maturation of 18S rRNA. YPR010C is the second largest subunit of RNA polymerase I. YNL061W is a probable RNA methyltransferase essential for large ribosomal subunit biogenesis. Table 5 describes which genes are supported by which analyses and Table S4 contains more information about all 12 predicted genes.

### [7] Different Metabolic Pathways Are Involved in Response of Saccharomyces cerevisiae to L-A and M Viruses
- Authors: Juliana Lukša, B. Ravoitytė, A. Konovalovas, L. Aitmanaitė, A. Butenko et al.
- Year: 2017
- Venue: Toxins
- URL: https://www.semanticscholar.org/paper/347e98c21490a16073f34d46ef429d508b7f6822
- DOI: 10.3390/toxins9080233
- PMID: 28757599
- PMCID: 5577567
- Citations: 23
- Summary: It is reported that most of the transcriptional responses induced by viral dsRNAs are moderate and insight into the virus–host and virus–virus interplays is provided.
- Evidence snippets:
  - Snippet 1 (score: 0.684)
    > The physical and/or functional interaction of gene products identified in RNA-Seq. analysis was addressed next. For this, a STRING database of known and predicted protein interactions was used to analyze gene products involved in processes altered by elimination of M-2 (Figure 4) and both L-A-lus and M-2 viral dsRNAs (Figure 5).
    > Products of genes with altered expression level in M-2-free cells and related to ribosome biogenesis, oxidation-reduction and lipid metabolism were shown to be highly interconnected (Figure 4). Interconnections formed highly-reliable hub between members of ribosome biogenesis group. Most of the genes encoding these proteins are essential. They are related to ribosomal RNA processing (Rrp1, -5, -12, and -14); ATP-dependent RNA helicases of the DEAD-box protein family (Dbp2, -8, and -10); components of the Rix1 complex and pre-replicative complexes Ipi1 and Ipi3; components of RNA polymerases (Rpb8, and Rpc10 and -19); many nucleolar proteins (e.g., Nop1, -4, -7, -8, and -10); and others. In terms of fold change, NSR1, RRS1 and ALB1 were the most (almost three-fold) upregulated genes in this group. Among the closely interconnected gene products involved in ribosome biogenesis, we noted those that are also required for maintenance of M-1 dsRNA (Mak5, Mak11, Mak16) [38][39][40] and involved in susceptibility to K1 (Kre33) [21] or both K1 and K2 killer toxins (Fyv7) [23].
    > The products of downregulated genes in M437 [L+M−] cells showed interconnections of high confidence level between members related to cellular energetic processes (Figure 4B).

### [8] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2775
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.683)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [9] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.683)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [10] Permanent draft genome of Thermithiobaclillus tepidarius DSM 3134T, a moderately thermophilic, obligately chemolithoautotrophic member of the Acidithiobacillia
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
  - Snippet 1 (score: 0.677)
    > Genes were identified using Prodigal [18] as part of the DOE-JGI genome annotation pipeline [19]. The predicted CDSs were translated and used to search the National Center for Biotechnology Information non-redundant database, UniProt, TIGR-Fam, Pfam, KEGG, COG, and InterPro database. These data sources were combined to assert a product description for each predicted protein. tRNAScanSE was used to find tRNA genes and rRNA genes were found using searches against models of the ribosomal RNA genes built from SIVLA [20,21].
    > Additional gene prediction analysis and functional annotation was performed within the IMG-ER platform [22,23]. For each gene discussed in this publication, the annotation was manually checked against the Gen-Bank® databased manual searches using the BLASTn and BLASTp algorithms -both of the gene from T. tepidarius and using the equivalent gene from members of the Acidithiobacillia or Escherichia coli.

### [11] Silencing of RNA Helicase II/Guα Inhibits Mammalian Ribosomal RNA Production*
- Authors: D. Henning, Rolando B. So, Runyan Jin, L. Lau, B. Valdez
- Year: 2003
- Venue: Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/9be7b042a6a61f36ad5a60279b1f88ffbbe044c2
- DOI: 10.1074/jbc.M310846200
- Citations: 68
- Influential citations: 1
- Summary: Short interfering RNA was used to search for functions for RH-II/Guα and its paralogue RH- II/Guβ in rRNA production and found the opposite effects of the two paralogues suggest antagonistic functions.
- Evidence snippets:
  - Snippet 1 (score: 0.677)
    > The use of short interfering RNA (siRNA) 1 has revolutionized the way in which the functions and interactions of multiple genes and their encoded proteins are deciphered. Short doublestranded RNA mediates the recognition and degradation of its homologous RNA, leading to the down-regulation of expression of the target gene; the mechanism involves a multiprotein complex (1)(2)(3). The application of siRNA facilitates the study of complex cellular processes including the biogenesis of ribosomal RNA (rRNA).
    > Synthesis and processing of pre-rRNA, maturation of the final products, and formation of ribosomes occur in the nucleolus. The identification of ϳ350 nucleolar proteins (4,5) and the use of siRNA to silence each encoding gene provide the genetic and biochemical screenings that are necessary to elucidate the mechanism of rRNA production in mammalian cells, a process that is more defined in yeast (6 -8). A number of nucleolar proteins have been functionally associated with mammalian rRNA production mostly based on in vitro experiments and indirect in vivo observations (9 -13). More direct lines of evidence are limited to Bop1 (14), p19 arf (15), and the DKC1 gene product dyskerin (16,17). Although our laboratory recently showed that antisense-mediated down-regulation of RNA helicase II/Gu␣ in Xenopus laevis oocytes resulted in inhibition of production of 18 S rRNA and degradation of 28 S rRNA (18), we have not reported that this enzyme has a similar function in mammalian cells.
    > RNA helicase II/Gu␣ (RH-II/Gu␣ or DDX21) is a DEAD box nucleolar protein that we previously cloned and characterized (19,20). The cDNA-derived amino acid sequence shows RNA helicase motifs at the middle region, which is responsible for its 5Ј to 3Ј RNA unwinding activity, and a functionally distinct domain at its C terminus that is able to introduce secondary structure to single-stranded RNA (21).

### [12] Basidioascus undulatus: genome, origins, and sexuality
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
  - Snippet 1 (score: 0.675)
    > run on the scaffolds to detect the percentage of conserved eukaryotic genes (CEGs).
    > Genome annotation was performed following established guidelines (Haas et al. 2011 (Slater & Birney 2005). Predicted gene models exhibiting strong evidence by exon alignment were exported as protein sequences and coding nucleotide sequences (CDS). Predicted gene models lacking evidence from exon alignment were discarded in downstream analyses. To determine function, the protein sequences were used as input for InterProScan 5RC6 (Jones et al. 2014) (parameters: -dp -f -t p -iprlookup -pa -goterms) and were also compared to the manually curated protein data set from UniProt/Swiss-Prot by blastp v. 2.2.28+. The results in XML format from blastp v. 2.2.28+ and InterProScan were loaded into Blast2GO v. 2.7.1 (Conesa et al. 2005) and merged to create an annotation table (available from the first author on request). The gene models with BLAST hits having e-value of less than 1.0E -100 and mean similarity hit of ≥ 70% were assumed to be orthologs and they were given names following recommended conventions (http:// www.uniprot.org/docs/proknameprot). Ribosomal RNA's were predicted by RNAmmer v. 1.2 (Lagesen et al. 2007). Data files are publicly available at NCBI (Genome Accession No. JTLS00000000 version JTLS01000000; BioProject Accession No. PRJNA247992) and JGI MycoCosm portal (Grigoriev et al. 2014).

### [13] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.674)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [14] ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance
- Authors: FuGuo Liu, T. Lai, Wenxia Xu, Guodong Li
- Year: 2026
- Venue: PLOS One
- URL: https://www.semanticscholar.org/paper/7d7965ec223f5715675839cb57efdc776d25e216
- DOI: 10.1371/journal.pone.0349393
- PMID: 42234710
- PMCID: 13232823
- Citations: 1
- Summary: ViralMultiNet is a structure-aware multimodal framework that integrates multi-scale k-mer encodings with functional semantic embeddings derived from UniProt annotations that offers a scalable, interpretable solution for viral protein function prediction.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > To reduce redundancy while preserving sequence diversity, the 235,441 validated ORFs were subjected to two-stage clustering using VSEARCH v2.21.1: first at 90% sequence identity, then refined at 95% identity. Cluster representatives were aligned against UniProt/Swiss-Prot (release 2024_01) using DIAMOND v2.0.15 in sensitive mode (--sensitive). The initial alignment yielded 62,689 ORFs with putative UniProt matches. For each match, protein names, functional descriptions, and Gene Ontology (GO) terms were extracted for downstream label assignment.
    > 2.1.4. Functional labeling. Functional labels (Enzymatic, Structural, Transport, Other) were assigned to the 62,689 UniProt-mapped ORFs using hierarchical keyword matching against a curated dictionary of 847 functional terms derived from UniProt protein descriptions and Gene Ontology annotations. The classification hierarchy prioritized primary molecular functions:
    > • Enzymatic: Proteins with catalytic activity (GO:0003824), including polymerases, proteases, methyltransferases, and helicases
    > • Structural: Proteins involved in virion assembly and structural maintenance (GO:0019012), including spike, envelope, membrane, and nucleocapsid proteins
    > • Transport: Proteins mediating membrane transport and ion channels (GO:0006810, GO:0015267)
    > • Other: All remaining ORFs, including regulatory proteins, accessory factors, and hypothetical proteins ORFs with ambiguous or conflicting annotations (e.g., proteins with both enzymatic and structural roles) were manually reviewed by two independent annotators, achieving 94.2% inter-annotator agreement (Cohen's κ = 0.92). After removing ambiguous cases, this resulted in 53,575 unique labeled ORF sequences with unambiguous functional assignments.The 'Other' category encompasses a functionally heterogeneous set of accessory proteins with distinct biological roles, as summarized in Table 1 Variants were filtered to retain only those with ≥2% sequence divergence from their corresponding base ORF to ensure meaningful diversity while maintaining functional annotation consistency.

### [15] Comprehensive Bioinformatics Analysis of the Biodiversity of Lsm Proteins in the Archaea Domain
- Authors: Gloria Payá, V. Bautista, M. Camacho, J. Esclapez, M. Bonete
- Year: 2023
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/62674578b27cda57cafc83c112afaa020f5ab651
- DOI: 10.3390/microorganisms11051196
- PMID: 37317170
- PMCID: 10221803
- Citations: 7
- Summary: It is proposed that most archaeal Lsm proteins are related to the RNA metabolism, and the larger L sm proteins could perform different functions and/or act through other mechanisms of action.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > The STRING 11.0 bioinformatics tool [25] predicts gene-gene or protein-protein associations derived from experimental and bibliographic information, i.e., the interactome. For this purpose, all Lsm proteins in Table S1 were searched, of which 74 were deposited in this database. Figure 7 shows 11 genes that appear in the vast majority of the species analyzed: rpl7ae and rpl37e, which encode 50S ribosomal proteins; fusA, which encodes elongation factor 2; flpA, which encodes fibrillin-like pre-rRNA processing protein; purF, which encodes amidophosphoribosyltransferase; rrp4 and rrp41, which encode RNA-binding proteins of the exosome complex; hel308, which encodes a helicase; and rpoD, rpoH, and rpoN, which encode different RNA polymerase subunits (Figure 7A). All these genes encode proteins closely related to the RNA metabolism.
    > The ribosomal protein L7Ae is a multifunctional RNA-binding protein that recognizes the K-turn motif of the ribosome and the H/ACA and C/D boxes of sRNAs, generating conformational changes in sRNAs [60]. As mentioned above, the ribosomal protein L37e is found adjacent to the lsm gene in many archaea species. Its primary function is stabilizing interactions between the domains to maintain the structural integrity of the 50S subunit through interactions with RNA [54]. The fusA gene encodes translational elongation factor 2, which has homologs in all three domains of life, EF-G in bacteria, eEF-2 in eukaryotes, and aEF-2 in archaea; it is composed of five domains, a GTPase domain, and domains II to V; and mediates the hydrolysis of a GTP molecule during translocation [61,62].

### [16] Sexual and Apogamous Species of Woodferns Show Different Protein and Phytohormone Profiles
- Authors: H. Fernández, Jonas Grossmann, V. Gagliardini, I. Feito, Alejandro Rivera et al.
- Year: 2021
- Venue: Frontiers in Plant Science
- URL: https://www.semanticscholar.org/paper/31e7e9e486fe7ed4411184372cd9324d4fc2c25c
- DOI: 10.3389/fpls.2021.718932
- PMID: 34868105
- PMCID: 8633544
- Citations: 9
- Summary: The results point to the existence of large metabolic differences between apogamous and sexual gametophytes, and invite to consider the ferngametophyte as a good experimental system to deepen the understanding of plant reproduction.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > Besides, it promotes, in a dose-and auxindependent manner, organ growth by stimulating both cell proliferation and expansion, via the regulation of RBR1 levels (Horváth et al., 2006). The list also included an emb3010 or 40S ribosomal protein S6-2, which may play an important role in controlling cell growth and proliferation through the selective translation of particular classes of mRNAs (Zhou et al., 2015).
    > Ribosome assembly and function are correlated with the activity of RNA binding proteins, often associated to ribonucleoprotein complexes of RNA as well as helicases (Schmidt, 2020). The former includes proteins like the phosphoprotein AtLa1, required for normal ribosome biogenesis and embryogenesis (Fleurdépine et al., 2007), and the latter, a 50S ribosomal protein L13 or embryo defective 1473, involved in translation and biological processes such as embryo development ending in seed dormancy or stress tolerance (Moin et al., 2016).
    > RNA helicases are considered of crucial importance for gene regulation of developmental processes, exerting an epigenetic control. In the apogamous species, two helicases, to unwind nucleic acids, were reported: the emb1138, member of the DEAD-box ATP-dependent RNA helicase 3, and At3G62310, a probable pre-mRNA-splicing factor ATP-dependent RNA helicase DEAH2, which might be involved in pre-mRNA splicing. The DEAD-box helicases are involved in various aspects of RNA metabolism, including nuclear transcription, pre-mRNA splicing, ribosome biogenesis, nucleocytoplasmic transport, translation, RNA decay and organellar gene expression. Different studies provided evidence of RNA helicases to be likely involved in regulating apomictic development (Schmidt, 2020). In A. thaliana, mutants for the RNA helicase MNEME form unreduced gametophytes, resembling apospory (Schmidt et al., 2011).

### [17] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.668)
    > (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b). Under normal-growth conditions, the most enriched cluster (enrichment score 11.4) comprised genes related to ribonucleoproteins, ribosomes, ribosomal proteins, and translation. The second-most enriched cluster (enrichment score 3.8) comprised genes belonging to protein biosynthesis and tRNA metabolism, including aminoacyl-tRNA synthetases. A third cluster (enrichment score 2.2) comprised genes related to nucleotide-binding proteins. Among the genes with peaks under cold-shock conditions, the same three annotation clusters were identified, with enrichment scores 6.5, 4.1, and 2.5, respectively.
    > We also analyzed the genes identified under both normal-growth and cold-shock conditions, only under normal-growth conditions, or only under cold-shock conditions. (Supplemental Table 4c-e). The same three annotation clusters (ribosome and translation, tRNA metabolism, and nucleotide binding, enrichment scores 6.4, 3.8, and 2.7, respectively) were reported for genes that contained peaks under both normal-growth and cold-shock conditions. Genes with peaks only under normal-growth conditions were enriched for genes related to ribosomes and translation, genes with peaks only under cold-shock conditions showed no specific enrichment. Genes that neither contained a peak under normal-growth nor under coldshock conditions also showed no significant enrichment of a particular family of proteins (Supplemental Table 4f).
    > As an example for genes related to annotation cluster 1, 18 out of the 22 genes (82%) for proteins of the 30S ribosomal subunit were identified under normal-growth conditions, 12 (55%) after cold shock (11 common genes, three without peaks). For the proteins of the 50S ribosomal subunit, the picture was similar: Out of 34 genes, 31 (91%) were identified under normal-growth, 22 (65%) under coldshock conditions (20 common genes, one without peaks).

### [18] Target gene selection for sprayable dsRNA‐based biopesticide against Tetranychus urticae Koch (Acari: Tetranychidae)
- Authors: Yifei Wang, Yuanpeng Duan, Meibin Liu, Meifeng Ren, Yue Gao et al.
- Year: 2025
- Venue: Pest Management Science
- URL: https://www.semanticscholar.org/paper/199a962288bfd1b7f69c1136588cbac9e8f2c6dc
- DOI: 10.1002/ps.8675
- PMID: 39887845
- PMCID: 12074632
- Citations: 8
- Summary: A project to develop double‐stranded RNA (dsRNA)‐based biopesticides against T. urticae, aiming for a species‐specific and sustainable pest management alternative, is initiated.
- Evidence snippets:
  - Snippet 1 (score: 0.667)
    > In this study, we assessed the toxicity of genes in the DEAD box gene family, proteasome subunits, and signal recognition particle. The DEAD box gene family is the largest subfamily of ATPase activity-dependent RNA helicase, 47 encoding RNA helicases genes that are highly conserved and widely expressed across prokaryotes and eukaryotes. They play essential roles in various aspects of RNA metabolism, including unwinding RNA and remodeling RNA-protein interactions through their ATP-dependent RNA helicase activity. 48 ATPHel-31B and Belle are members of the DEAD box ATP-dependent RNA helicase genes, which are known to modulate numerous biological processes, such as innate immunity and participation in the RNAi pathway. 29 Various approaches have shown that silencing DEAD box ATP-dependent RNA helicase genes can significantly compromise fitness and cause phenotypical changes in several arthropods, including migratory locust Locusta migratoria, 48 common fruit fly Drosophila melanogaster, 49 and A. viennensis. 39 In this study, knockdown of ATPHel-31B and Belle resulted in 60.9% and 37.9% mortality, respectively, with a >50% decrease in relative gene expression levels. No phenotypic changes were observed. Previous research been demonstrated that Belle is essential for both male and female fertility. 50,51 dsTuBelle treatment in T. urticae caused a numerical decrease in female fecundity. However, there were no significant differences compared with the controls, likely because of an insufficient concentration of the treatment. Eukaryotic initiation factor 4A-I (eIF-4A-1) belongs to the DEAD box superfamily 2 (SF2) and is critical for protein translation in eukaryotes. 28 It facilitates ribosome loading onto messenger RNA and is essential for cell growth and development. 52 eIF4A is regulated by the DREF pathway, which is involved in controlling protein synthesis in Drosophila. 53 Injecting dsTuelF4A in L. migratoria nymphs caused 100% mortality before molting, with appendages darkening and withering. 48

### [19] Role of DEAD-box RNA helicases in low-temperature adapted growth of Antarctic Pseudomonas syringae Lz4W
- Authors: Ashaq Hussain, M. K. Ray
- Year: 2023
- Venue: Microbiology Spectrum
- URL: https://www.semanticscholar.org/paper/3760a722f12fd4b62ed86cf4925ef91174806c4e
- DOI: 10.1128/spectrum.04335-22
- PMID: 38014988
- PMCID: 10783127
- Citations: 5
- Summary: The role of DEAD-box RNA helicases in low-temperature adapted growth of P. syringae is investigated, as this group of enzymes play an essential role in modulation of RNA secondary structures, and the requisite role of dbpA and the indispensable requirement of csdA for low- temperature adapted growth are a novel finding.
- Evidence snippets:
  - Snippet 1 (score: 0.666)
    > R NA helicases regulate cellular processes by modulating different aspects of RNA biology, from its synthesis to degradation, structural maturation (RNA processing) to the stability, and for interaction with metabolites to cellular proteins (RNA protein complexes) for sensing and responding to the cellular milieu (1,2). The DEAD-box RNA helicases constitute a specific group of RNA helicases that derives its name from the highly conserved amino acid sequence in one of the motifs that reads as DEAD in single-letter amino acid code (3). The DEAD-box proteins belong to the SF2 superfamily of RNA helicases which bind to ATP and RNA by two RecA-like domains located on 350to 400-residues-long "helicase core" and perform ATP (ATPase)dependent functions (4,5). These functions include canonical RNA duplex unwinding, RNA strand annealing, RNA folding (RNA chaperone), strand exchange, and protein displacement activity (1,6,7). The conserved helicase core of the RNA helicases is generally flanked by variable regions which are important for determining the specificity of the enzyme (2). The cellular ability to perform these functions at low temperature is critical for cold-adapted organisms, as RNA secondary structures are stabilized at lower temperatures (8).
    > In bacteria, only a small number of genes (four to six) code for DEAD-box proteins (9). Gram-negative bacterium, such as Escherichia coli, contains five genes for different DEAD-box RNA helicases, while the Gram-positive bacterium, such as Bacillus subtilis, contains four DEAD-box RNA helicase genes in the genome (7,10,11). These helicases are involved in ribosome biogenesis, mRNA processing, and translation. Many of these proteins are non-essential in the organisms at optimum temperature of growth but are variably important for growth at low temperature. In E. coli, none of the five DEADbox proteins (RhlE, SrmB, CsdA, DbpA, and RhlB) are essential for growth at 37°C (12). However, SrmB and CsdA are critical at low temperature (15°C-20°C).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Rahena Yasmin, M. Chauhan, S. Sourabh, R. Tuteja (2019). Plasmodium falciparum DDX31 is DNA helicase localized in nucleolus. Heliyon. https://www.semanticscholar.org/paper/693e52918e8f0574cbe3e5386ab130ace5cd107f
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
4. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
5. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
6. V. Martyanov, R. H. Gross (2013). Computational Discovery of Transcriptional Regulatory Modules in Fungal Ribosome Biogenesis Genes Reveals Novel Sequence and Function Patterns. PLoS ONE. https://www.semanticscholar.org/paper/986fb7b3472c53c1891d806144874429471d3d13
7. Juliana Lukša, B. Ravoitytė, A. Konovalovas, L. Aitmanaitė, A. Butenko et al. (2017). Different Metabolic Pathways Are Involved in Response of Saccharomyces cerevisiae to L-A and M Viruses. Toxins. https://www.semanticscholar.org/paper/347e98c21490a16073f34d46ef429d508b7f6822
8. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
9. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
10. R. Boden, L. Hutt, Marcel Huntemann, Alicia Clum, Manoj Pillay et al. (2016). Permanent draft genome of Thermithiobaclillus tepidarius DSM 3134T, a moderately thermophilic, obligately chemolithoautotrophic member of the Acidithiobacillia. Standards in Genomic Sciences. https://www.semanticscholar.org/paper/f2117c6922312a227e69b8448f807915356842c9
11. D. Henning, Rolando B. So, Runyan Jin, L. Lau, B. Valdez (2003). Silencing of RNA Helicase II/Guα Inhibits Mammalian Ribosomal RNA Production*. Journal of Biological Chemistry. https://www.semanticscholar.org/paper/9be7b042a6a61f36ad5a60279b1f88ffbbe044c2
12. Hai D. T. Nguyen, D. Chabot, Y. Hirooka, R. Roberson, K. Seifert (2015). Basidioascus undulatus: genome, origins, and sexuality. IMA Fungus. https://www.semanticscholar.org/paper/a5deb29da5109780b4d55dfa35ea0d9fe13216d5
13. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
14. FuGuo Liu, T. Lai, Wenxia Xu, Guodong Li (2026). ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance. PLOS One. https://www.semanticscholar.org/paper/7d7965ec223f5715675839cb57efdc776d25e216
15. Gloria Payá, V. Bautista, M. Camacho, J. Esclapez, M. Bonete (2023). Comprehensive Bioinformatics Analysis of the Biodiversity of Lsm Proteins in the Archaea Domain. Microorganisms. https://www.semanticscholar.org/paper/62674578b27cda57cafc83c112afaa020f5ab651
16. H. Fernández, Jonas Grossmann, V. Gagliardini, I. Feito, Alejandro Rivera et al. (2021). Sexual and Apogamous Species of Woodferns Show Different Protein and Phytohormone Profiles. Frontiers in Plant Science. https://www.semanticscholar.org/paper/31e7e9e486fe7ed4411184372cd9324d4fc2c25c
17. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
18. Yifei Wang, Yuanpeng Duan, Meibin Liu, Meifeng Ren, Yue Gao et al. (2025). Target gene selection for sprayable dsRNA‐based biopesticide against Tetranychus urticae Koch (Acari: Tetranychidae). Pest Management Science. https://www.semanticscholar.org/paper/199a962288bfd1b7f69c1136588cbac9e8f2c6dc
19. Ashaq Hussain, M. K. Ray (2023). Role of DEAD-box RNA helicases in low-temperature adapted growth of Antarctic Pseudomonas syringae Lz4W. Microbiology Spectrum. https://www.semanticscholar.org/paper/3760a722f12fd4b62ed86cf4925ef91174806c4e