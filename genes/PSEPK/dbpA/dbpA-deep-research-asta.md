---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T11:21:26.729364'
end_time: '2026-07-10T11:21:31.893912'
duration_seconds: 5.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dbpA
  gene_symbol: dbpA
  uniprot_accession: Q88D75
  protein_description: 'SubName: Full=ATP-dependent RNA helicase, specific for 23S
    rRNA {ECO:0000313|EMBL:AAN70519.1}; EC=3.6.4.13 {ECO:0000313|EMBL:AAN70519.1};'
  gene_info: Name=dbpA {ECO:0000313|EMBL:AAN70519.1}; OrderedLocusNames=PP_4952 {ECO:0000313|EMBL:AAN70519.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DEAD box helicase family.
  protein_domains: DbpA/CsdA_RNA-bd_dom. (IPR005580); DEAD/DEAH_box_helicase_dom.
    (IPR011545); DEAD/DEAH_RhlB. (IPR044742); DEAD_box_RNA_helicase. (IPR050079);
    Helicase_ATP-bd. (IPR014001)
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
- **UniProt Accession:** Q88D75
- **Protein Description:** SubName: Full=ATP-dependent RNA helicase, specific for 23S rRNA {ECO:0000313|EMBL:AAN70519.1}; EC=3.6.4.13 {ECO:0000313|EMBL:AAN70519.1};
- **Gene Information:** Name=dbpA {ECO:0000313|EMBL:AAN70519.1}; OrderedLocusNames=PP_4952 {ECO:0000313|EMBL:AAN70519.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DEAD box helicase family.
- **Key Domains:** DbpA/CsdA_RNA-bd_dom. (IPR005580); DEAD/DEAH_box_helicase_dom. (IPR011545); DEAD/DEAH_RhlB. (IPR044742); DEAD_box_RNA_helicase. (IPR050079); Helicase_ATP-bd. (IPR014001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dbpA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dbpA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dbpA** (gene ID: dbpA, UniProt: Q88D75) in PSEPK.

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
  - Snippet 1 (score: 0.723)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [2] Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes
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
  - Snippet 1 (score: 0.716)
    > To inspect the transcriptomics result of individual genes, proteins originating from JGI have a hyperlink to a summary page which links to a 'Genome browser' page that displays the predicted gene splicing, including which regions have RNA support (Figure 1 D).
    > Hence, in the protein specific site in the JGI w e bsite under 'To Genome Browser', the current protein (GeneCatalog) can be seen together with se v eral other alternati v e predictions of the gene splicing, which is essential to have correct, for the protein to function naturally (Figure 2 ).
    > As the RNA coverage supports the exon / intron splicing, it is possible to infer whether a particular gene, in this case Table 1. Comparison between the dbCAN webserver, the eggNOG webserver for both family and functional annotation of CAZymes and the updated CUPP-w e bserver using the recommended significance cut-off at 5. The column 'CAZy -All characterized' encompasses all 10784 characterized proteins in the CAZy database used for the training, whereas the 'CAZy -Newly characterized '   a gene such as the one selected in Figure 2 , is more likely to work after heterologous gene expression.
    > To further improve the enzyme selection, all NCBI Genbank accessions were mapped to Uniprot ID to link to the specific Uniprot accession page including the predicted Al-phaFold structures, Go annotations and InterPro annotations and more ( 19 ).

### [3] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.709)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [4] Misannotations of rRNA can now generate 90% false positive protein matches in metatranscriptomic studies
- Authors: H. J. Tripp, I. Hewson, Sam Boyarsky, Joshua M. Stuart, J. Zehr
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/7fb83902c01e43ed76adfdd93530e28355d7b954
- DOI: 10.1093/nar/gkr576
- PMID: 21771858
- PMCID: 3203614
- Citations: 52
- Influential citations: 2
- Summary: Recommendations are offered that workers in the field of metatranscriptomics take extra care to avoid including false positive matches in their datasets, and other issues relating to the curation practices of those managing public databases such as GenBank and SwissProt are offered.
- Evidence snippets:
  - Snippet 1 (score: 0.706)
    > We clicked on the link to 'Group II intron-associated genes', but there was no diagram of a subsystem and no literature listed in the 'Functional Roles' tab. We visually inspected the 30 gene contexts and found additional embedded and overlapping ORFs in the 23S rRNA sequences displayed. Of the 30 contexts, 12 also showed a conserved hypothetical protein that also completely overlapped the 23S rRNA, just down-stream of the misannotated 'Retron-type reverse transcriptase'. Three of the 30 contexts also showed a different conserved hypothetical protein that also completely overlapped the 23S rRNA sequence, and three more contexts showed from one to three very small (<53 amino acids) conserved hypothetical proteins completely overlapping a 23S rRNA sequence. By 'completely overlapping' we mean 'coding for rRNA and protein at the same time'. This confirmed that there are errors in the SEED, despite the care taken by the current Rapid Annotations using Subsystems Technology (RAST) pipeline not to add any more errors. The RAST pipeline begins by calling tRNA and rRNA genes and 'the server will not consider retaining any protein-encoding genes that are embedded in rRNAs. These gene calls are almost certainly artefacts of the period in which groups were learning how to develop proper annotations, and RAST attempts to avoid propagating these errors'. Still, we assert that existing misannotations should be found and corrected.

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
  - Snippet 1 (score: 0.703)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.672)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [6] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.680)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [7] A short guide to long non-coding RNA gene nomenclature
- Authors: M. Wright
- Year: 2014
- Venue: Human Genomics
- URL: https://www.semanticscholar.org/paper/5603656d27ad714cebcb661e6d4089e9c7f34e37
- DOI: 10.1186/1479-7364-8-7
- Citations: 3
- Influential citations: 1
- Summary: A short guide is presented herein to help authors when developing novel gene symbols for lncRNAs with characterised function, and to provide unique and, wherever possible, meaningful gene symbols to all lncRNA genes.
- Evidence snippets:
  - Snippet 1 (score: 0.677)
    > The HUGO Gene Nomenclature Committee (HGNC) is the only organisation authorised to assign standardised nomenclature to human genes. Of the 38,000 approved gene symbols in our database (http://www.genenames.org), the majority represent protein-coding (pc) genes; however, we also name pseudogenes, phenotypic loci, some genomic features, and to date have named more than 8,500 human non-protein coding RNA (ncRNA) genes and ncRNA pseudogenes. We have already established unique names for most of the small ncRNA genes by working with experts for each class. Small ncRNAs can be defined into their respective classes by their shared homology and common function. In contrast, long non-coding RNA (lncRNA) genes represent a disparate set of loci related only by their size, more than 200 bases in length, share no conserved sequence homology, and have variable functions. As with pc genes, wherever possible, lncRNAs are named based on the known function of their product; a short guide is presented herein to help authors when developing novel gene symbols for lncRNAs with characterised function. Researchers must contact the HGNC with their suggestions prior to publication, to check whether the proposed gene symbol can be approved. Although thousands of lncRNAs have been predicted in the human genome, for the vast majority their function remains unresolved. lncRNA genes with no known function are named based on their genomic context. Working with lncRNA researchers, the HGNC aims to provide unique and, wherever possible, meaningful gene symbols to all lncRNA genes.

### [8] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.674)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [9] CRONOS: the cross-reference navigation server
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

### [10] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
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
  - Snippet 1 (score: 0.672)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

### [11] Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation
- Authors: Eugenio L Mangas, Alejandro Rubio, R. Álvarez-Marín, Gema Labrador-Herrera, J. Pachón et al.
- Year: 2019
- Venue: Microbial Genomics
- URL: https://www.semanticscholar.org/paper/ccdc06e24b4cff1ddca5e537c65e5f14c5f017b3
- DOI: 10.1099/mgen.0.000309
- PMID: 31626589
- PMCID: 6927304
- Citations: 64
- Influential citations: 2
- Summary: A genomics analysis of almost 2500 strains found two different groups of genomes found based on the number of shared genes, one of which rarely has plasmids, and bears clustered regularly interspaced short palindromic repeat (CRISPR) sequences, in addition to CRISPR-associated genes (cas genes) or restriction-modification system genes.
- Evidence snippets:
  - Snippet 1 (score: 0.668)
    > To homogenize the genome annotation, the sequences of all genomes were analysed using the same protocol. The proteinencoding genes were predicted using Prokka version 1.13 [24], and the predicted protein sequences were functionally annotated using Sma3s v2 and UniProt taxonomic division bacteria 2019_01 as a reference database [25,55].
    > To annotate specific genes, GO (gene ontology) terms and UniProt keywords assigned by Sma3s were used. To find genes associated with CRISPR systems, protein sequences coming

### [12] Metagenomics reveals the genetic diversity between sublineages of UCYN-A and their algal host plastids
- Authors: E. J. H. Kantor, Brent M Robicheau, J. Tolman, John M. Archibald, Julie LaRoche
- Year: 2024
- Venue: ISME Communications
- URL: https://www.semanticscholar.org/paper/7d08a26029e51ce59a2a68d12b83e4855b6ae4fc
- DOI: 10.1093/ismeco/ycae150
- PMID: 39670058
- PMCID: 11637426
- Citations: 4
- Summary: Comparison of the initial genome sequenced from this sublineage showed that UCYN-A4 is sufficiently genetically distinct from both UCYN-A1 and UCYN-A2 to be considered its own sublineage, but more similar to UCYN-A2 than -A1, supporting its possible classification as a nitroplast.
- Evidence snippets:
  - Snippet 1 (score: 0.667)
    > BLAST results of the UCYN-A1 NWA against the UCYN-A1 ALOHA reference genome showed high percent identity of over 98% in most regions except for missing rRNA genes (Fig. 3C).
    > Of the 30 gene clusters unique to the UCYN-A4 NWA, only four were annotated by Anvi'o. Of the rest, three have BLAST matches to known proteins in public databases, 11 were annotated as hypothetical proteins, and 12 had no annotations beyond their original identification as ORFs (Table S9). Three of the genes with annotations are adjacent at the ends of two contigs: a MalK maltose/maltodextrin ATP-binding protein, a 23S rRNA-intervening sequence protein with BLASTx match to a four-helix bundle protein of unknown function from Gracilimonas sp., and a gene with a BLASTx match to a HlyD family eff lux transporter from Balneola sp. The MalK has 93% identity in BLASTn with a portion of the same gene in the UCYN-A2 CPSB-1 genome, while the other two had no BLASTn results and do not align with UCYN-A2 CPSB-1. Other annotated genes encode an RNA polymerase sigma factor with BLASTx match to Crocosphaera sp., a glycosyltransferase BscA, a partial ferredoxin gene which partially aligns to the same gene in UCYN-A2 CPSB-1, and DUF3086 domain-containing protein of unknown function with a weak BLASTx match to the same protein in UCYN-A2 CPSB-1 (45% amino acid identity). Five hypothetical protein genes and one unannotated gene were found to align with regions in UCYN-A2 CPSB-1 with no annotations. A BLASTn of UCYN-A4 NWA against UCYN-A2 CPSB-1 showed an average identity in the low 80% range and was also missing rRNA genes (Fig. 3C).

### [13] Telomere-to-telomere and haplotype-resolved genome assembly of the Chinese cork oak (Quercus variabilis)
- Authors: Longxin Wang, Lei-Lei Li, Li Chen, Rengang Zhang, Shilei Zhao et al.
- Year: 2023
- Venue: Frontiers in Plant Science
- URL: https://www.semanticscholar.org/paper/0dcf50ebbfe0e1527238aa4758df72784d064667
- DOI: 10.3389/fpls.2023.1290913
- PMID: 38023918
- PMCID: 10652414
- Citations: 10
- Influential citations: 1
- Summary: This study presents a nearly complete comprehensive telomere-to-telomere (T2T) and haplotype-resolved reference genome for Q. variabilis, and predicts 36,830 and 36,370 protein-coding genes, with 95.9% and 96.0% functional annotation for each haplotype genome.
- Evidence snippets:
  - Snippet 1 (score: 0.662)
    > exons per gene. We predicted non-coding RNA sequences, which resulted in the prediction of 641 ribosomal RNA (rRNA), 1,282 transfer RNA (tRNA) and 1,764 other non-coding RNA (ncRNA). By integrating the functional annotations from three methods, we successfully annotated 95.90% and 96.00% of the protein-coding genes on haplotypes A and B, respectively, leaving 4.1% and 4.0% of the protein-coding genes unannotated for their functions. These gene function annotations will provide a valuable resource for breeders and researchers, who can query the data and analyze their gene of interest through https://doi.org/ 10.6084/m9.figshare.22313569.v2.

### [14] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.660)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [15] Genome information management and integrated data analysis with HaloLex
- Authors: F. Pfeiffer, A. Broicher, Thomas N Gillich, K. Klee, José Mejía et al.
- Year: 2008
- Venue: Archives of Microbiology
- URL: https://www.semanticscholar.org/paper/f1333d02086a84becaa054612dbb6316af6ba4c3
- DOI: 10.1007/s00203-008-0389-z
- PMID: 18592220
- PMCID: 2516542
- Citations: 91
- Influential citations: 4
- Summary: Application of homology-based methods to the published genome of Haloarcula marismortui allowed to detect 47 previously unidentified genes and to correct more than 300 start codon misassignments.
- Evidence snippets:
  - Snippet 1 (score: 0.658)
    > The available information about an individual coding sequence is summarized by a central ''details page'' listing sequences (coding region and protein translation), functional information (e.g., protein name, gene name, EC number, functional classification), general gene and protein characteristics (e.g., sequence length, start and stop codons, GC content, theoretical pI value), and results from several bioinformatic tools, e.g., transmembrane and signal peptide prediction with ''Phobius'' (Kall et al. 2004), protein export signals with ''Tatfind'' (Rose et al. 2002), codon adaptation index (Sharp and Li 1987), etc. In addition, the details page shows homologous sequences as well as cross-references to entries of the same protein in major public sequence databases like GenBank, UniProt, Kegg, and also links to relevant PubMed abstracts.
    > Usually, the details page is reached by selecting an organism and directly specifying an identifier or name for the gene of interest. In addition, also less specific searches and browsing functionalities are supported, including the option to obtain complete lists of genes or proteins, which can optionally be filtered by various characteristics like pI value range, type of proteomic identification, etc. (cf. Fig. 1).
    > If the organism or gene of interest is not specified a priori, the user can alternatively start out with a blastbased search (Altschul et al. 1997) for all sequences in the HaloLex database, which are similar to a given query.
    > To reach the details page, one may also start from a graphical display of a particular region on the genome. The corresponding ''region viewer'' page provides standard genome browsing functionalities and allows to color-code genes according to a variety of characteristics like the annotation status, assigned function class, GC content, proteomic identification (see Fig. 2), and many more.

### [16] Next Generation Sequencing and Transcriptome Analysis Predicts Biosynthetic Pathway of Sennosides from Senna (Cassia angustifolia Vahl.), a Non-Model Plant with Potent Laxative Properties
- Authors: Nagaraja Reddy Rama Reddy, Rucha Harishbhai Mehta, Palak Soni, Jayanti Makasana, N. Gajbhiye et al.
- Year: 2015
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/fec6263b90f9cd765752bdb1be3d162872f2e64e
- DOI: 10.1371/journal.pone.0129422
- PMID: 26098898
- PMCID: 4476680
- Citations: 81
- Influential citations: 3
- Summary: A set of putative genes involved in various secondary metabolite pathways, especially those related to the synthesis of sennosides are identified which will serve as an important platform for public information about gene expression, genomics, and functional genomics in senna.
- Evidence snippets:
  - Snippet 1 (score: 0.656)
    > Further the assembled transcript contigs were validated using CLC Genomics workbench (CLC Bio, Boston, MA 02108 USA) by mapping high quality reads back to the assembled transcript contigs. ORF-Predictor [57], an online tool, was used on default parameters to identify the coding DNA sequences (CDS) from assembled transcript contigs. GC counts of transcripts was determined using a custom-made perl script.
    > Functional annotations. The functional annotation was performed by aligning coding DNA sequence (CDS) to NCBI 'green plant database (txid 33090)' database using basic local alignment search tool (BLASTX) [58] with an E-value threshold of 1e -06 and GO assignments were used to classify the functions of the predicted CDS. The GO mapping also provided ontology of defined terms representing gene product properties which were grouped into three main domains: biological process (BP), molecular function (MF) and cellular component (CC). GO mapping was carried out in order to retrieve GO terms for all the BLASTX functionally annotated CDS. The GO mapping used defined criteria to retrieve GO terms for annotated CDS which included use of BLASTX result accession IDs to retrieve gene names or symbols, UniProt IDs and direct search in the dbxref table of GO database. Identified gene names or symbols were then searched in the species specific entries of the gene-product tables of GO database. UniProt IDs made use of protein information resource (PIR) which includes protein sequence database (PSD), UniProt, SwissProt, TrEMBL, RefSeq, GenPept, and PDB databases. Gene Ontology analysis helps in specifying all the annotated nodes comprising of GO functional groups. CDS were compared against the COG (Clusters of Orthologous Groups) database for the analysis of phylogenetically widespread domain families. CDS were compared against Pfam database for higher-level groupings of related protein families, known as clans and the identification of domains that occurs within proteins. BLASTX was used against uniprot-swissprot database with cut-off e-value 1e-6 to annotate predicted CDS against protein.

### [17] Complete Genome Sequencing of the Attenuated Strain Mycoplasma synoviae 5-9
- Authors: Xiaorong Zhang, Yang Chen, Zehua Wei, Shuang Ma, Mengjiao Guo et al.
- Year: 2021
- Venue: Microbiology Resource Announcements
- URL: https://www.semanticscholar.org/paper/7b6f0a2b5ca6ca23de3f49b578b0f1eb9d7dd8ab
- DOI: 10.1128/MRA.00981-21
- PMID: 34881981
- PMCID: 8656387
- Summary: The complete genome sequence of Mycoplasma synoviae strain 5-9, which was attenuated by chemical mutagenesis from a field strain isolated from egg breeders in Ningxia, China, is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.650)
    > Gene models were identified using GeneMark. Then, all gene models were searched using blastp against the NCBI nonredundant (NR), Swiss-Prot (http://uniprot.org), KEGG (http://www.genome.jp/kegg/), and COG (http://www.ncbi.nlm.nih.gov/COG) databases. Additionally, tRNAs were identified using tRNAscan-SE v1.23 (13) (http://lowelab .ucsc.edu/tRNAscan-SE), and rRNAs were determined using RNAmmer v1.2 (14) (https:// services.healthtech.dtu.dk/service.php?RNAmmer-1.2). There were 652 protein-coding genes and 44 RNA genes (34 tRNAs, 3 5S rRNAs, 2 16S rRNAs, 2 23S rRNAs, and 3 noncoding RNA [ncRNA] genes).
    > Data availability. The complete genome sequence and annotation of M. synoviae strain 5-9 have been deposited at GenBank under accession number CP083748. The raw data were deposited in the Sequence Read Archive (SRA) database under the accession numbers SRR16005423 (Oxford Nanopore) and SRR16005422 (Illumina). The BioProject accession number is PRJNA763075. The BioSample accession number is SAMN21422653.

### [18] OntoGene in BioCreative II
- Authors: Fabio Rinaldi, T. Kappeler, K. Kaljurand, Gerold Schneider, Manfred Klenner et al.
- Year: 2007
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/ffcbf659129388203ce458ce1b25e5449e9594e7
- DOI: 10.1186/gb-2008-9-s2-s13
- PMID: 18834491
- PMCID: 2559984
- Citations: 78
- Influential citations: 1
- Summary: This report describes approaches taken within the scope of the second BioCreative competition in order to solve two aspects of this problem: detection of novel protein interactions reported in scientific articles, and detection of the experimental method that was used to confirm the interaction.
- Evidence snippets:
  - Snippet 1 (score: 0.650)
    > It is well known that protein names are highly ambiguous [45,46]. Researchers working in specific subcommunities tend to develop their own nomenclature, resulting in multiple names for the same protein. Acronyms and abbreviations further complicate the picture. Simply being able to recognize a protein name as such is just a starting point. The name needs then to be unambiguously qualified, by referring to an entry in a standard protein database, such as UniProt http:// www.expasy.org/sprot/ [47].
    > In order for that to happen, the disambiguation must occur at two levels: interspecies (to which specific organisms does the protein mention refer?) and intraspecies (within a given organism, which specific protein is meant?). For example, a protein mentioned in text as eIF4E could refer to a large number of different proteins. A search in the Swiss-Prot section of UniProt (the manually curated section) delivers 46 possible matches. However, if the term appears contextually with the mention of a specific organism, like in the sentence 'The Cap-binding protein eIF4E promotes folding of a functional domain of yeast translation initiation factor eIF4G1' (PubMed: 10409688), then it is reasonable to assume that the name refers to a specific organism (yeast), thus restricting the possible matches in UniProt to the following two: EAP1_YEAST (eIF4E-associated protein 1) and IF4E_YEAST (eukaryotic translation initiation factor 4E). For the task of protein annotation, we have adopted a high-recall, low-precision term annotation approach, followed by very strict disambiguation steps, which gradually increase precision (at some expense for recall).
    > UniProt contains for each protein a list of frequently used synonyms, as well as the name and synonyms of its encoding gene. We have built a database that maps the synonyms to the protein identifier. We have further enriched such a list using morpho-syntactic rules that generate variants of the synonyms. Starting from the subset of UniProt delivered by the BioCreative organizers (which contained 228,

### [19] miRNAs Predicted to Regulate Host Anti-viral Gene Pathways in IPNV-Challenged Atlantic Salmon Fry Are Affected by Viral Load, and Associated With the Major IPN Resistance QTL Genotypes in Late Infection
- Authors: N. T. Woldemariam, O. Agafonov, H. Sindre, B. Høyheim, R. Houston et al.
- Year: 2020
- Venue: Frontiers in Immunology
- URL: https://www.semanticscholar.org/paper/b2d7a6eaa8ad2899b5f575d7f9dce8e85079e9c1
- DOI: 10.3389/fimmu.2020.02113
- PMID: 33013890
- PMCID: 7516080
- Citations: 25
- Summary: The absence of differences between QTL groups in controls, 1 and 7 dpc indicates that the QTL genotype does not affect miRNA expression in healthy fish or their first response to viral infections, and shows that miRNAs are sensitive to VL and disease progression, and may act as fine-tuners of both immediate immune response activation and the later inflammatory processes.
- Evidence snippets:
  - Snippet 1 (score: 0.650)
    > Target gene prediction (in silico analysis) was carried out with RNAhybrid (41). The mature sequences from the DE miRNAs [mature sequences given in Woldemariam et al. (33)] were tested against 3'UTRs from all Atlantic salmon mRNA transcripts in the NCBI Reference Sequence database (Refseq) (42). The following parameters were applied in the RNA hybrid analysis: helix constraint 2-8, no G: U in seed and minimum free energy threshold−18 kcal/mol. Gene functions of predicted target genes were retrieved from the Universal Protein Resource (UniProt) database https://www.uniprot.org/ (43). Based on the GO annotations, the subsets of target genes relevant to immune response were identified. Cross-reference links for these genes in Uniprot were used to retrieve organism-specific gene pathways from the online resource Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway database (https:// www.genome.jp/kegg/pathway.html) (44). These genes were also used as input in gene pathway enrichment analyses applying the Enrichr tool (http://amp.pharm.mssm.edu/Enrichr/). Results were then filtered by organism to rank gene pathways present in Atlantic salmon by their adjusted P-values (Q-values) and combined score.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer (2023). Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes. Nucleic Acids Research. https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
3. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
4. H. J. Tripp, I. Hewson, Sam Boyarsky, Joshua M. Stuart, J. Zehr (2011). Misannotations of rRNA can now generate 90% false positive protein matches in metatranscriptomic studies. Nucleic Acids Research. https://www.semanticscholar.org/paper/7fb83902c01e43ed76adfdd93530e28355d7b954
5. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
6. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
7. M. Wright (2014). A short guide to long non-coding RNA gene nomenclature. Human Genomics. https://www.semanticscholar.org/paper/5603656d27ad714cebcb661e6d4089e9c7f34e37
8. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
9. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
10. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10
11. Eugenio L Mangas, Alejandro Rubio, R. Álvarez-Marín, Gema Labrador-Herrera, J. Pachón et al. (2019). Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation. Microbial Genomics. https://www.semanticscholar.org/paper/ccdc06e24b4cff1ddca5e537c65e5f14c5f017b3
12. E. J. H. Kantor, Brent M Robicheau, J. Tolman, John M. Archibald, Julie LaRoche (2024). Metagenomics reveals the genetic diversity between sublineages of UCYN-A and their algal host plastids. ISME Communications. https://www.semanticscholar.org/paper/7d08a26029e51ce59a2a68d12b83e4855b6ae4fc
13. Longxin Wang, Lei-Lei Li, Li Chen, Rengang Zhang, Shilei Zhao et al. (2023). Telomere-to-telomere and haplotype-resolved genome assembly of the Chinese cork oak (Quercus variabilis). Frontiers in Plant Science. https://www.semanticscholar.org/paper/0dcf50ebbfe0e1527238aa4758df72784d064667
14. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
15. F. Pfeiffer, A. Broicher, Thomas N Gillich, K. Klee, José Mejía et al. (2008). Genome information management and integrated data analysis with HaloLex. Archives of Microbiology. https://www.semanticscholar.org/paper/f1333d02086a84becaa054612dbb6316af6ba4c3
16. Nagaraja Reddy Rama Reddy, Rucha Harishbhai Mehta, Palak Soni, Jayanti Makasana, N. Gajbhiye et al. (2015). Next Generation Sequencing and Transcriptome Analysis Predicts Biosynthetic Pathway of Sennosides from Senna (Cassia angustifolia Vahl.), a Non-Model Plant with Potent Laxative Properties. PLoS ONE. https://www.semanticscholar.org/paper/fec6263b90f9cd765752bdb1be3d162872f2e64e
17. Xiaorong Zhang, Yang Chen, Zehua Wei, Shuang Ma, Mengjiao Guo et al. (2021). Complete Genome Sequencing of the Attenuated Strain Mycoplasma synoviae 5-9. Microbiology Resource Announcements. https://www.semanticscholar.org/paper/7b6f0a2b5ca6ca23de3f49b578b0f1eb9d7dd8ab
18. Fabio Rinaldi, T. Kappeler, K. Kaljurand, Gerold Schneider, Manfred Klenner et al. (2007). OntoGene in BioCreative II. Genome Biology. https://www.semanticscholar.org/paper/ffcbf659129388203ce458ce1b25e5449e9594e7
19. N. T. Woldemariam, O. Agafonov, H. Sindre, B. Høyheim, R. Houston et al. (2020). miRNAs Predicted to Regulate Host Anti-viral Gene Pathways in IPNV-Challenged Atlantic Salmon Fry Are Affected by Viral Load, and Associated With the Major IPN Resistance QTL Genotypes in Late Infection. Frontiers in Immunology. https://www.semanticscholar.org/paper/b2d7a6eaa8ad2899b5f575d7f9dce8e85079e9c1