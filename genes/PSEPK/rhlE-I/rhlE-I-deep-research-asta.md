---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T03:19:42.866425'
end_time: '2026-07-09T03:19:49.873268'
duration_seconds: 7.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rhlE-I
  gene_symbol: rhlE-I
  uniprot_accession: Q88DQ7
  protein_description: 'RecName: Full=DEAD-box ATP-dependent RNA helicase RhpA {ECO:0000256|ARBA:ARBA00074363};
    EC=3.6.4.13 {ECO:0000256|ARBA:ARBA00012552};'
  gene_info: Name=rhlE-I {ECO:0000313|EMBL:AAN70336.1}; OrderedLocusNames=PP_4766
    {ECO:0000313|EMBL:AAN70336.1};
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
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88DQ7
- **Protein Description:** RecName: Full=DEAD-box ATP-dependent RNA helicase RhpA {ECO:0000256|ARBA:ARBA00074363}; EC=3.6.4.13 {ECO:0000256|ARBA:ARBA00012552};
- **Gene Information:** Name=rhlE-I {ECO:0000313|EMBL:AAN70336.1}; OrderedLocusNames=PP_4766 {ECO:0000313|EMBL:AAN70336.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DEAD box helicase family.
- **Key Domains:** DEAD/DEAH_box_helicase_dom. (IPR011545); DEAD/DEAH_RhlB. (IPR044742); DEAD_box_RNA_helicase. (IPR050079); Helicase_ATP-bd. (IPR014001); Helicase_C-like. (IPR001650)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rhlE-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rhlE-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rhlE-I** (gene ID: rhlE-I, UniProt: Q88DQ7) in PSEPK.

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

### [1] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.704)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.696)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.686)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [4] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.678)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [5] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.672)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [6] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.660)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [7] Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes
- Authors: Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer
- Year: 2023
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
- DOI: 10.1093/nar/gkad385
- PMID: 37216585
- PMCID: 10320097
- Citations: 8
- Summary: The new implementation of the CUPP-webserver, https://cupp.info/, now includes all published fungal and algal genomes from the Joint Genome Institute (JGI), genome resources My coCosm and PhycoCosm, dynamically subdivided into motif groups of CAZymes, allowing users to browse the JGI portals for specific predicted functions or specific protein families from genome sequences.
- Evidence snippets:
  - Snippet 1 (score: 0.659)
    > To inspect the transcriptomics result of individual genes, proteins originating from JGI have a hyperlink to a summary page which links to a 'Genome browser' page that displays the predicted gene splicing, including which regions have RNA support (Figure 1 D).
    > Hence, in the protein specific site in the JGI w e bsite under 'To Genome Browser', the current protein (GeneCatalog) can be seen together with se v eral other alternati v e predictions of the gene splicing, which is essential to have correct, for the protein to function naturally (Figure 2 ).
    > As the RNA coverage supports the exon / intron splicing, it is possible to infer whether a particular gene, in this case Table 1. Comparison between the dbCAN webserver, the eggNOG webserver for both family and functional annotation of CAZymes and the updated CUPP-w e bserver using the recommended significance cut-off at 5. The column 'CAZy -All characterized' encompasses all 10784 characterized proteins in the CAZy database used for the training, whereas the 'CAZy -Newly characterized '   a gene such as the one selected in Figure 2 , is more likely to work after heterologous gene expression.
    > To further improve the enzyme selection, all NCBI Genbank accessions were mapped to Uniprot ID to link to the specific Uniprot accession page including the predicted Al-phaFold structures, Go annotations and InterPro annotations and more ( 19 ).

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
  - Snippet 1 (score: 0.654)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [9] Stable Episomal Transfectant Leishmania infantum Promastigotes Over-Expressing the DEVH1 RNA Helicase Gene Down-Regulate Parasite Survival Genes
- Authors: A. Alonso, J. Larraga, F. J. Loayza, E. Martínez, B. Valladares et al.
- Year: 2022
- Venue: Pathogens
- URL: https://www.semanticscholar.org/paper/8416a769635c6a285345f6a47bfa38501246bf15
- DOI: 10.3390/pathogens11070761
- PMID: 35890006
- PMCID: 9323391
- Citations: 3
- Summary: Interestingly, genes related to parasite survival and virulence factors, such as the hydrophilic surface protein/small hydrophobic endoplasmic reticulum protein (HASP/SHERP) gene cluster, an amastin, and genesrelated to reactive oxygen species detoxification are down-regulated in DEVH1 transfectant promastigotes.
- Evidence snippets:
  - Snippet 1 (score: 0.654)
    > The compartmentalization of untranslated mRNA molecules in granules occurring in many eukaryotic organisms including trypanosomatids involves the formation of complexes between mRNA molecules and RNA-binding proteins (RBPs). The putative ATP-dependent DEAD/H RNA helicase (DEVH1) from Leishmania infantum (Kinetoplastida: Trypanosomatidae) is one such proteins. The objective of this research is finding differentially expressed genes in a stable episomal transfectant L. infantum promastigote line over-expressing DEVH1 in the stationary phase of growth in axenic culture to get insight into the biological roles of this RNA helicase in the parasite. Interestingly, genes related to parasite survival and virulence factors, such as the hydrophilic surface protein/small hydrophilic endoplasmic reticulum protein (HASP/SHERP) gene cluster, an amastin, and genes related to reactive oxygen species detoxification are down-regulated in DEVH1 transfectant promastigotes.

### [10] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.651)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [11] The alpha-ketoacid dehydrogenase complexes of Drosophila melanogaster.
- Authors: Steven J. Marygold
- Year: 2024
- Venue: microPublication Biology
- URL: https://www.semanticscholar.org/paper/50942e603e0e14ee9195c0d7cb52db11a521f964
- DOI: 10.17912/micropub.biology.001209
- PMID: 38741935
- PMCID: 11089389
- Citations: 2
- Summary: This work identifies and classify the genes encoding all Drosophila AKDHC subunits, update their functional annotations and integrate this work into the FlyBase database.
- Evidence snippets:
  - Snippet 1 (score: 0.651)
    > Symbol: gene symbol in FlyBase -asterisk (*) indicates a gene with testis-specific expression. CG#: gene annotation ID in FlyBase. Function: component and associated EC number (where available/applicable). Key reference(s) for initial identification or genetic characterization (in a metabolic context): 1. Gruntenko et al. 1998;2. Chen et al. 2008;3. Yoon et al. 2017;4. Yap et al. 2021a;5. Yap et al. 2021b;6. Whittle et al. 2023;7. González Morales et al. 2023;8. Homem et al. 2014;9. Bonnay et al. 2020;10. Ivanova et al. 2004;11. Boyko et al. 2020;12. Liu et al. 2017;13. Li et al. 2020;14. Devilliers et al. 2021;15. Goyal et al. 2022;16. Huang et al. 2022;17. Plaçais et al. 2017;18. Dung et al. 2018;19. Rabah et al. 2023;20. Klenz et al. 1995;21. Katsube et al. 1997;22. Gándara et al. 2019;23. Lambrechts et al. 2019;24. Lee et al. 2022;25. Chen et al. 2006;26. Kim et al. 2023;27. Tsai et al. 2020. Human ortholog: gene symbol at HGNC, with % amino acid identity between the encoded protein and the Drosophila protein. Human disease: OMIM symbol for disease(s) associated with the human gene (Amberger et al. 2019) -see Extended Data File 1 for details.

### [12] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
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
  - Snippet 1 (score: 0.648)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

### [13] Target gene selection for sprayable dsRNA‐based biopesticide against Tetranychus urticae Koch (Acari: Tetranychidae)
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
  - Snippet 1 (score: 0.647)
    > In this study, we assessed the toxicity of genes in the DEAD box gene family, proteasome subunits, and signal recognition particle. The DEAD box gene family is the largest subfamily of ATPase activity-dependent RNA helicase, 47 encoding RNA helicases genes that are highly conserved and widely expressed across prokaryotes and eukaryotes. They play essential roles in various aspects of RNA metabolism, including unwinding RNA and remodeling RNA-protein interactions through their ATP-dependent RNA helicase activity. 48 ATPHel-31B and Belle are members of the DEAD box ATP-dependent RNA helicase genes, which are known to modulate numerous biological processes, such as innate immunity and participation in the RNAi pathway. 29 Various approaches have shown that silencing DEAD box ATP-dependent RNA helicase genes can significantly compromise fitness and cause phenotypical changes in several arthropods, including migratory locust Locusta migratoria, 48 common fruit fly Drosophila melanogaster, 49 and A. viennensis. 39 In this study, knockdown of ATPHel-31B and Belle resulted in 60.9% and 37.9% mortality, respectively, with a >50% decrease in relative gene expression levels. No phenotypic changes were observed. Previous research been demonstrated that Belle is essential for both male and female fertility. 50,51 dsTuBelle treatment in T. urticae caused a numerical decrease in female fecundity. However, there were no significant differences compared with the controls, likely because of an insufficient concentration of the treatment. Eukaryotic initiation factor 4A-I (eIF-4A-1) belongs to the DEAD box superfamily 2 (SF2) and is critical for protein translation in eukaryotes. 28 It facilitates ribosome loading onto messenger RNA and is essential for cell growth and development. 52 eIF4A is regulated by the DREF pathway, which is involved in controlling protein synthesis in Drosophila. 53 Injecting dsTuelF4A in L. migratoria nymphs caused 100% mortality before molting, with appendages darkening and withering. 48

### [14] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
- Authors: E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al.
- Year: 2016
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/f3eda16f7a2760619a7727b38fc2fc6738858040
- DOI: 10.1186/s13059-016-1014-0
- PMID: 27381095
- PMCID: 4933991
- Citations: 93
- Influential citations: 5
- Summary: The results provide the most complete comparative genomics and experimental analysis of mRBPs in P. falciparum and identify and characterize mRNA-binding proteins (mRBPs) that encompass a relatively large proportion of the parasite proteome as compared to other eukaryotes.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

### [15] The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum
- Authors: E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al.
- Year: 2016
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
- DOI: 10.1186/s13059-016-1014-0
- Summary: The results provide the most complete comparative genomics and experimental analysis of mRBPs in P. falciparum and identify and characterize mRNA-binding proteins (mRBPs) that encompass a relatively large proportion of the parasite proteome as compared to other eukaryotes.
- Evidence snippets:
  - Snippet 1 (score: 0.646)
    > It is possible that the current gene annotation is incorrect and that these genes were mislabeled as "RNA binding." Out of all 64 manually added genes, nine genes contained weak to very weak RBDs (median E-value = 0.041), of which five were strongly related to the gene annotation. Diversification of these genes in P. falciparum may have precluded identification of these domains in our HMM search.
    > The type of molecule that the candidate RBP interacts with was determined based on existing annotations and known functions of homologs in other species. If this information was not available, the type of molecule was predicted based on the nature of the RNA-binding domain (RBD). Proteins for which no information was available were categorized as "non-RNA."
    > To calculate the percentage of sequences from groups of organisms in the HMM seed, the HMM seed file (Pfam version 27.0) was downloaded, filtered for the 372 mRNAbinding domains used in this study, and parsed for UniProt accession numbers. The source organism of each sequence was then retrieved using the retrieve/ID mapping tool on the UniProt website (http://www.uniprot.org/ uploadlists/) and matched to the corresponding Pfam domain. For each domain, the percentage of sequences derived from each group at the third level of the taxonomic lineage was determined.
    > In each organism, a variety of proteins that are unlikely to be involved in RNA metabolism were identified in the HMM search. However, manually curating these protein lists would introduce a bias, since not all genomes have been annotated to the same extent. Therefore, to make a fair comparison between organisms, we included all mRBD-containing proteins in our subsequent analysis, irrespective of their annotation. To correct for differences in genome size, RBD abundance was expressed as the number of RBDs per 10,000 genes. Pfam domains that were present in at least one out of 11 organisms (n = 353) were clustered based on their relative abundance across organisms using the k-means clustering algorithm with a maximum of 1000 iterations in R v2.7.0 [70].

### [16] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.646)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [17] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.644)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [18] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.644)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [19] Deltamethrin Selection Drives Transcriptomic Changes in Detoxification, Immune, and Cuticle Genes in Aedes aegypti
- Authors: Y. Contreras-Perera, L. Mackenzie-Impoinvil, Dieunel Derilus, Audrey Lenhart, I. Rodríguez-Sánchez et al.
- Year: 2025
- Venue: Tropical Medicine and Infectious Disease
- URL: https://www.semanticscholar.org/paper/21e5f9022b6c14afa8f193ff59151db6228bc141
- DOI: 10.3390/tropicalmed10060171
- PMID: 40559738
- PMCID: 12197768
- Citations: 5
- Summary: The overexpression of immune- and stress-related genes, including the RNA helicase MOV-10, indicates that insecticide selection may trigger broader physiological responses and highlight complex, multi-pathway transcriptomic changes associated with resistance development in Ae.
- Evidence snippets:
  - Snippet 1 (score: 0.642)
    > The AegL5 gene set contains over 19,804 predicted genes (14,718 protein-coding genes, 5086 non-protein-coding genes, and 382 pseudogenes). However, functional annotation is available for only 6319, and gene ontology (GO) annotation terms are assigned to 11,097 of the protein-coding genes. To enhance the interpretation of the data, the computational annotation of the AegL5 set was performed using Blast2GO (see Methods). This analysis assigned putative functional descriptions to 13,322 and GO terms to 11,680 of the protein-coding genes. All the annotation results from both Vector-Base and Blast2GO are provided in File S5.
    > Gene ontology enrichment analysis (GOEA) was performed on the DE genes (up and downregulated, separately) from each F S4 vs. F S0 (3 in total). The significantly enriched GO terms, including biological process, molecular function, and cellular component categories, are reported in File S6. GO molecular function terms that were significantly enriched in at least two out of the three comparisons are summarized in Figure S1.
    > For the upregulated genes, GO molecular function terms associated with binding activities (ATP, nucleic acid, RNA, Adenyl ribonucleotide/nucleotide small molecule, organic cyclic compounds), transferase activity (methyl, one-carbon group), helicase, and ATP-dependent activities were significantly enriched, suggesting the potential role of these key molecular functions following insecticide selection. Of note, GO terms associated with methyltransferase activity were significantly enriched in the upregulated genes. Among these, tRNA (cytosine34-C5)-methyltransferase (AAEL013968) was consistently detected among the top 10 DE genes from all three F S4 vs. F S0 comparisons. This may suggest the involvement of the RNA methylation process in response to insecticide selection; however, direct evidence for DNA or RNA methylation in Ae. aegypti under deltamethrin exposure is currently lacking.

### [20] Protocol for analysis of plasma proteomes from patients with hepatocellular carcinoma receiving combination therapy
- Authors: Z. Pan, Ling Du, Feng Liu
- Year: 2024
- Venue: STAR Protocols
- URL: https://www.semanticscholar.org/paper/1632ed4453801a085e45bc15fbeccd9d47313c04
- DOI: 10.1016/j.xpro.2024.103308
- PMID: 39321025
- PMCID: 11462194
- Summary: Plasma shows distinct metabolomic and proteomic signatures in response to combination therapy with lenvatinib and anti-programmed death-1 (PD-1) antibody in treating hepatocellular carcinoma (HCC) and a protocol for analyzing plasma proteomes from patients with HCC is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.642)
    > The above commands list the methods to retrieve gene symbols (like UniProt: MASP2), UniProt entry names (like UniProt: MASP2_HUMAN), and protein UniProt accession number (like UniProt: O00187). We use gene symbols for enrichment analysis.
    > 25. Enrichment analysis using R package UniprotR. Note: The functional enrichment analysis of the differential proteins is performed using R package UniprotR. 16 In our paper, we utilized the online functional enrichment analysis tool Metascape. 25 However, there is no R version of Metascape. Another R package, clusterProfiler, is commonly used in enrichment analysis. 10 Since clusterProfiler only supports ENTREZ ID, protein accession numbers or protein names must be converted into ENTREZ ID using ID transformation R packages, such as org.Hs.eg.db (https://bioconductor.org/packages/ release/data/annotation/html/org.Hs.eg.db.html), biomaRt, 26 or gconvert function in g:pro-filer2. 27 It is important to note, however, that not all protein accessions or protein names can be successfully connected to ENTREZ IDs using these tools. Interestingly, UniprotR is ideally suited for proteomics results due to its ability to use all accession numbers or protein names for enrichment analysis.
    > Note: The figures will write into a single PDF file in current directory.
    > Note: In some instances, functional enrichment analysis may not yield significant results. See problem 4.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
4. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
5. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
6. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
7. Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer (2023). Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes. Nucleic Acids Research. https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
8. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
9. A. Alonso, J. Larraga, F. J. Loayza, E. Martínez, B. Valladares et al. (2022). Stable Episomal Transfectant Leishmania infantum Promastigotes Over-Expressing the DEVH1 RNA Helicase Gene Down-Regulate Parasite Survival Genes. Pathogens. https://www.semanticscholar.org/paper/8416a769635c6a285345f6a47bfa38501246bf15
10. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
11. Steven J. Marygold (2024). The alpha-ketoacid dehydrogenase complexes of Drosophila melanogaster.. microPublication Biology. https://www.semanticscholar.org/paper/50942e603e0e14ee9195c0d7cb52db11a521f964
12. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
13. Yifei Wang, Yuanpeng Duan, Meibin Liu, Meifeng Ren, Yue Gao et al. (2025). Target gene selection for sprayable dsRNA‐based biopesticide against Tetranychus urticae Koch (Acari: Tetranychidae). Pest Management Science. https://www.semanticscholar.org/paper/199a962288bfd1b7f69c1136588cbac9e8f2c6dc
14. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/f3eda16f7a2760619a7727b38fc2fc6738858040
15. E. Bunnik, G. Batugedara, Anita Saraf, J. Prudhomme, L. Florens et al. (2016). The mRNA-bound proteome of the human malaria parasite Plasmodium falciparum. Genome Biology. https://www.semanticscholar.org/paper/fde442b2ed85f87ccd01e269ecce97ed9aea95d7
16. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
17. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
18. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
19. Y. Contreras-Perera, L. Mackenzie-Impoinvil, Dieunel Derilus, Audrey Lenhart, I. Rodríguez-Sánchez et al. (2025). Deltamethrin Selection Drives Transcriptomic Changes in Detoxification, Immune, and Cuticle Genes in Aedes aegypti. Tropical Medicine and Infectious Disease. https://www.semanticscholar.org/paper/21e5f9022b6c14afa8f193ff59151db6228bc141
20. Z. Pan, Ling Du, Feng Liu (2024). Protocol for analysis of plasma proteomes from patients with hepatocellular carcinoma receiving combination therapy. STAR Protocols. https://www.semanticscholar.org/paper/1632ed4453801a085e45bc15fbeccd9d47313c04