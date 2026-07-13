---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T08:12:41.469849'
end_time: '2026-07-07T08:12:49.215532'
duration_seconds: 7.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: carB
  gene_symbol: carB
  uniprot_accession: Q88DU6
  protein_description: 'RecName: Full=Carbamoyl phosphate synthase large chain {ECO:0000255|HAMAP-Rule:MF_01210};
    EC=6.3.4.16 {ECO:0000255|HAMAP-Rule:MF_01210}; EC=6.3.5.5 {ECO:0000255|HAMAP-Rule:MF_01210};
    AltName: Full=Carbamoyl phosphate synthetase ammonia chain {ECO:0000255|HAMAP-Rule:MF_01210};'
  gene_info: Name=carB {ECO:0000255|HAMAP-Rule:MF_01210}; OrderedLocusNames=PP_4723;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the CarB family. {ECO:0000255|HAMAP-
  protein_domains: ATP-grasp. (IPR011761); CarbamoylP_synth_lsu_oligo_sf. (IPR036897);
    CPAse_ATP-bd. (IPR005479); CPSase_dom. (IPR005483); CPSase_lsu. (IPR006275)
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
- **UniProt Accession:** Q88DU6
- **Protein Description:** RecName: Full=Carbamoyl phosphate synthase large chain {ECO:0000255|HAMAP-Rule:MF_01210}; EC=6.3.4.16 {ECO:0000255|HAMAP-Rule:MF_01210}; EC=6.3.5.5 {ECO:0000255|HAMAP-Rule:MF_01210}; AltName: Full=Carbamoyl phosphate synthetase ammonia chain {ECO:0000255|HAMAP-Rule:MF_01210};
- **Gene Information:** Name=carB {ECO:0000255|HAMAP-Rule:MF_01210}; OrderedLocusNames=PP_4723;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the CarB family. {ECO:0000255|HAMAP-
- **Key Domains:** ATP-grasp. (IPR011761); CarbamoylP_synth_lsu_oligo_sf. (IPR036897); CPAse_ATP-bd. (IPR005479); CPSase_dom. (IPR005483); CPSase_lsu. (IPR006275)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "carB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'carB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **carB** (gene ID: carB, UniProt: Q88DU6) in PSEPK.

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
  - Snippet 1 (score: 0.761)
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
  - Snippet 1 (score: 0.745)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

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
  - Snippet 1 (score: 0.725)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.721)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [5] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Citations: 1
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.721)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

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
  - Snippet 1 (score: 0.703)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [7] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
- Authors: P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
- DOI: 10.1093/nar/gkr1122
- PMID: 22135298
- PMCID: 3245126
- Citations: 1605
- Influential citations: 155
- Summary: PhosphoSitePlus (http://www.phosphosite.org) is an open, comprehensive, manually curated and interactive resource for studying experimentally observed post-translational modifications, primarily of human and mouse proteins. It encompasses 1 30 000 non-redundant modification sites, primarily phosphorylation, ubiquitinylation and acetylation. The interface is designed for clarity and ease of navigation. From the home page, users can launch simple or complex searches and browse high-throughput d...
- Evidence snippets:
  - Snippet 1 (score: 0.689)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

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
  - Snippet 1 (score: 0.678)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

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
  - Snippet 1 (score: 0.676)
    > Gene annotation was primarily derived from the S. clavuligerus reference genome in the NCBI database and was annotated using the NCBI Prokaryotic Genome Annotation Pipeline 59 . However, several CA biosynthetic genes were manually corrected based on published literature 9 . For instance, two loci were originally annotated as clavaminate synthase 1 (cas1), but one of these loci is located near the cephamycin C biosynthetic cluster, indicating it was actually cas2. Following this correction, the RefSeq accession numbers of all genes in the reference genome were cross-referenced with the UniProt database to obtain additional annotations 60 . For the mutated genes identified through ICA, protein existence levels were manually assigned based on the UniProt data, including protein existence status, annotation score, similar proteins, and relevant publications.

### [10] Protocol for gene annotation, prediction, and validation of genomic gene expansion
- Authors: Quanwei Zhang, Zhengdong D. Zhang
- Year: 2022
- Venue: STAR Protocols
- URL: https://www.semanticscholar.org/paper/af8e3a73daaa04214d43f4ec1d9b1c0fcd42b8e3
- DOI: 10.1016/j.xpro.2022.101692
- PMID: 36125934
- PMCID: 9494284
- Citations: 1
- Summary: A detailed step-by-step protocol for gene annotation, prediction of genomic gene expansion, and its computational and experimental validation is described and steps to discover functionality of each copy of replicated genes are detailed.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > 3. Gene annotation and functional annotation. a. Gene structure annotation.
    > In addition to gene prediction models, evidence from orthologous protein sequences and transcriptome assembly could be used to improve annotation quality. Protein sequences of orthologous genes can be obtained from UniProt (The UniProt, 2017). Ones from Swiss-Port have been reviewed and thus are of higher quality. Transcriptome assembly may be available from previous studies or can be assembled de novo from RNA-seq reads by Trinity (Haas et al., 2013). High quality transcriptome assembly can be selected as described in (Zhang et al., 2021). Note: Details about gene structure annotation (Holt and Yandell, 2011) can be found at http:// gmod.org/wiki/MAKER_Tutorial, https://darencard.net/blog/2017-05-16-maker-genomeannotation/, and the protocol (Campbell et al., 2014).
    > b. Quality measurement and functional annotation.
    > For each predicted gene, Maker2 provides the annotation edit distance (AED) score, which measures the goodness of fit between its predicted gene structure and its evidence support. The lower the score, the more accurate the prediction. If more than 90% genes with AED scores lower than 0.5, the genome can be considered well annotated. In addition to the AED score, a high proportion of recognizable domains contained in predicted protein -e.g., higher than 50% -also indicates a good annotation. Recognizable protein domains can by scanned by InterProScan (Jones et al., 2014), assigning potential function to predicted genes.
    > Note: Besides the aforementioned quality measurement, we strongly recommend measuring the completeness of the genome assembly and annotation by checking the existence of a set of Benchmarking Universal Single-Copy Orthologs (BUSCO) (Simao et al., 2015). A high-level completeness of genome assembly and annotation is imperative for a better identification of gene expansion. Based on the result of this analysis, researchers can decide whether they need to further improve the genome assembly before predicting gene expansion. A detailed protocol of BUSCO is available at

### [11] Ten steps to get started in Genome Assembly and Annotation
- Authors: Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al.
- Year: 2018
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
- DOI: 10.12688/f1000research.13598.1
- PMID: 29568489
- PMCID: 5850084
- Citations: 109
- Influential citations: 1
- Summary: Ten steps to facilitate researchers getting started in genome assembly and genome annotation are presented and the importance of data management is stressed, and advice on where to submit data and how to make results Findable, Accessible, Interoperable, and Reusable (FAIR).
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > The ultimate goal of the functional annotation process (Figure 4) is to assign biologically relevant information to predicted polypeptides, and to the features they derive from (e.g. gene, mRNA). This process is especially relevant nowadays in the context of the NGS era due to the capacity of sequencing, assembling, and annotating full genomes in short periods of time, e.g. less than a month. Functional elements could range from putative name and/or symbols for protein-coding genes, e.g. ADH to its putative biological function, e.g. alcohol dehydrogenase, associated gene ontology terms, e.g. GO:0004022, functional sites, e.g. METAL 47 47 Zinc 1, and domains, e.g. IPR002328, among other features. The function of predicted proteins can be computationally inferred based on the similarity between the sequence of interest and other sequences in different public repositories, e.g. BLASTP against Uniprot. Caution should be taken when assigning results merely based on sequence similarity as two evolutionary independent sequences which share some common domains could be considered homologs 62 . Thus, whenever possible, it is better to use orthologous sequences for annotation purposes rather than simply similar sequences 63 . With the growing number of sequences in those public repositories, it is possible to perform various searches and combine obtained results into a consensus annotation. The accurate assignment of the functional elements is a complex process, and the best annotation will involve manual curation.
    > There are two main outcomes of the functional annotation process. The first is the assignment of functional elements to genes. Downstream analysis of these elements allow further understanding of specific genome properties, e.g. metabolic pathways, and similarities compared with closely related species. The second result of the functional annotation is the additional quality check for the predicted gene set. It is possible to identify problematic and/or suspicious genes by the presence of specific domains, suspicious orthology assignment and/or absence of other functional elements, e.g. functional completeness. These Page 13 of 19

### [12] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.671)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [13] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [14] Protein Localization Analysis of Essential Genes in Prokaryotes
- Authors: Chong Peng, Feng Gao
- Year: 2014
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
- DOI: 10.1038/srep06001
- PMID: 25105358
- PMCID: 4126397
- Citations: 27
- Summary: A comprehensive protein localization analysis of essential genes in 27 prokaryotes including 24 bacteria, 2 mycoplasmas and 1 archaeon has been performed and shows that proteins encoded by essential genes are enriched in internal location sites, while exist in cell envelope with a lower proportion compared with non-essential ones.
- Evidence snippets:
  - Snippet 1 (score: 0.664)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

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
  - Snippet 1 (score: 0.664)
    > The available information about an individual coding sequence is summarized by a central ''details page'' listing sequences (coding region and protein translation), functional information (e.g., protein name, gene name, EC number, functional classification), general gene and protein characteristics (e.g., sequence length, start and stop codons, GC content, theoretical pI value), and results from several bioinformatic tools, e.g., transmembrane and signal peptide prediction with ''Phobius'' (Kall et al. 2004), protein export signals with ''Tatfind'' (Rose et al. 2002), codon adaptation index (Sharp and Li 1987), etc. In addition, the details page shows homologous sequences as well as cross-references to entries of the same protein in major public sequence databases like GenBank, UniProt, Kegg, and also links to relevant PubMed abstracts.
    > Usually, the details page is reached by selecting an organism and directly specifying an identifier or name for the gene of interest. In addition, also less specific searches and browsing functionalities are supported, including the option to obtain complete lists of genes or proteins, which can optionally be filtered by various characteristics like pI value range, type of proteomic identification, etc. (cf. Fig. 1).
    > If the organism or gene of interest is not specified a priori, the user can alternatively start out with a blastbased search (Altschul et al. 1997) for all sequences in the HaloLex database, which are similar to a given query.
    > To reach the details page, one may also start from a graphical display of a particular region on the genome. The corresponding ''region viewer'' page provides standard genome browsing functionalities and allows to color-code genes according to a variety of characteristics like the annotation status, assigned function class, GC content, proteomic identification (see Fig. 2), and many more.

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
  - Snippet 1 (score: 0.663)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [17] Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production
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
  - Snippet 1 (score: 0.661)
    > GPR relationships specify the putative relationship between genes and enzymatic activities in an organism. Following previous work [52], we represented these relationships as Boolean statements. The simplest such statement was: gene A implies reaction X, i.e., gene A -> reaction X. Enzymatic activities associated with protein complexes required more complicated statements, e.g., (gene A or gene B) and (gene C) -> reaction X.
    > To develop the GPR relationships for C. thermocellum, we used the annotations described above and information on protein complexes from UniProt. For each EC number in the C. thermocellum annotations, we searched UniProt [23] to determine whether that EC is associated with protein complexes, and if so, what type of complex exists across different organisms (homodimer, heterotrimer, etc.). Based on this information, and the information in the annotations, we assigned putative GPR relationships for C. thermocellum, conforming to known enzyme complex architecture whenever possible. As a specific example of this process, consider the reaction corresponding to carbamoyl-phosphate synthase ('R_CBPS'), EC 6.3.5.5. Several UniProt entries (e.g., CARA_ECOLI) with this EC number are annotated as being members of a complex composed of two chains, a small glutamine-hydrolyzing chain and a large chain that synthesizes carbamoyl phosphate. We found two C. thermocellum genes annotated as "carbamoyl-phosphate synthase, small subunit" (Cthe_1867, Cthe_0950) and two genes annotated as "carbamoyl-phosphate synthase, large subunit" (Cthe_1868, Cthe_0949). Thus, we expressed the GPR relationship for this reaction as: (Cthe_1867 or Cthe_0950) and (Cthe_1868 or Cthe_0949) -> R_CBPS.

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
  - Snippet 1 (score: 0.657)
    > In an effort to engage the collective expertise of the scientific community, we have implemented a collaborative wiki (MediaWiki version 1.19.11) for the Mnemiopsis gene complement. The Mnemiopsis Gene Wiki is accessible from the left sidebar of most pages and is searchable either by selecting a Mnemiopsis gene identifier (e.g., ML00011a) from the drop-down menu or by manually entering an identifier in the appropriate search box. Users can also access these pages by clicking on a gene in the 2.2 track of the genome browser. Each record in the Gene Wiki represents a single Mnemiopsis gene and provides the following annotation: nucleotide and protein sequences, coding exonic genomic coordinates, pre-computed BLAST hits from numerous organisms displaying the top hits for each protein, the top non-self BLAST hit to Mnemiopsis, Pfam-A domains, Gene Ontology (GO) functional annotations, human disease genes from Online Mendelian Inheritance in Man (OMIM), and a table of ortholog clusters formed by phylogenetically informed clustering methods [4] (Figure 5). In addition, controlled editable sections have been included that permit (and encourage) the scientific community to provide further gene annotation for isoforms, in situ images, references, and other notes for each gene. Users interested in supplementing our gene model annotation at the Mnemiopsis Gene Wiki pages must first create an account and log in prior to submitting their contributions. In-house subject matter expert data curators are notified by e-mail following the creation of a new user account or an edit to an existing Gene Wiki record. Any content changes or additions to the Gene Wiki are thoroughly evaluated by these data curators and are made public subject to their approval.
    > Pre-compiled BLAST hits are enumerated in tabular form. Each Mnemiopsis protein was compared to the UniProt and NCBI non-redundant protein databases (nr) using BLASTP. The results display the hit number, the accession numbers, E-values, and brief descriptions of the top four hits (lowest E-values). Accession numbers are linked to relevant corresponding entries at UniProt and GenBank.

### [19] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
- Authors: Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al.
- Year: 2025
- Venue: Molecular Ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 3
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.654)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
5. Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
6. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
7. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
8. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
9. J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al. (2025). Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains. Scientific Reports. https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
10. Quanwei Zhang, Zhengdong D. Zhang (2022). Protocol for gene annotation, prediction, and validation of genomic gene expansion. STAR Protocols. https://www.semanticscholar.org/paper/af8e3a73daaa04214d43f4ec1d9b1c0fcd42b8e3
11. Victoria Dominguez Del Angel, Erik Hjerde, L. Sterck, S. Capella-Gutiérrez, C. Notredame et al. (2018). Ten steps to get started in Genome Assembly and Annotation. F1000Research. https://www.semanticscholar.org/paper/1b1090dcbd0f6a609f0448957b7e464997879ea8
12. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
13. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
14. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
15. F. Pfeiffer, A. Broicher, Thomas N Gillich, K. Klee, José Mejía et al. (2008). Genome information management and integrated data analysis with HaloLex. Archives of Microbiology. https://www.semanticscholar.org/paper/f1333d02086a84becaa054612dbb6316af6ba4c3
16. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
17. Seth B Roberts, Christopher M. Gowen, J. Brooks, Stephen S. Fong (2010). Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production. BMC Systems Biology. https://www.semanticscholar.org/paper/dc66757785ecb9e1d1760f67f5410dddb5d3618c
18. R. Moreland, A. Nguyen, Joseph F. Ryan, Joseph F. Ryan, C. Schnitzler et al. (2014). A customized Web portal for the genome of the ctenophore Mnemiopsis leidyi. BMC Genomics. https://www.semanticscholar.org/paper/327b13b7b70d702a34b70b6ef01188d8167601d8
19. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21