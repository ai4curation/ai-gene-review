---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T11:42:21.966592'
end_time: '2026-07-10T11:42:26.946566'
duration_seconds: 4.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rsmB
  gene_symbol: rsmB
  uniprot_accession: Q88RR3
  protein_description: 'RecName: Full=Ribosomal RNA small subunit methyltransferase
    B; EC=2.1.1.176; AltName: Full=16S rRNA m5C967 methyltransferase; AltName: Full=rRNA
    (cytosine-C(5)-)-methyltransferase RsmB;'
  gene_info: Name=rsmB; Synonyms=rrmB, sun; OrderedLocusNames=PP_0066;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class I-like SAM-binding methyltransferase
  protein_domains: MeTrfase_RsmB-F_NOP2_cat. (IPR049560); MeTrfase_RsmB-F_NOP2_dom.
    (IPR001678); NusB-like_sf. (IPR035926); NusB_RsmB_TIM44. (IPR006027); RCMT. (IPR023267)
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
- **UniProt Accession:** Q88RR3
- **Protein Description:** RecName: Full=Ribosomal RNA small subunit methyltransferase B; EC=2.1.1.176; AltName: Full=16S rRNA m5C967 methyltransferase; AltName: Full=rRNA (cytosine-C(5)-)-methyltransferase RsmB;
- **Gene Information:** Name=rsmB; Synonyms=rrmB, sun; OrderedLocusNames=PP_0066;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class I-like SAM-binding methyltransferase
- **Key Domains:** MeTrfase_RsmB-F_NOP2_cat. (IPR049560); MeTrfase_RsmB-F_NOP2_dom. (IPR001678); NusB-like_sf. (IPR035926); NusB_RsmB_TIM44. (IPR006027); RCMT. (IPR023267)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rsmB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rsmB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rsmB** (gene ID: rsmB, UniProt: Q88RR3) in PSEPK.

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
  - Snippet 1 (score: 0.798)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.718)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.775)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

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
  - Snippet 1 (score: 0.771)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] Functional annotation and comparative genomics analysis of Balamuthia mandrillaris reveals potential virulence-related genes
- Authors: Alejandro Otero-Ruiz, L. Z. Rodriguez-Anaya, F. Lares-Villa, Luis Fernando Lozano Aguirre Beltrán, L. F. Lares-Jiménez et al.
- Year: 2023
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/2507f970e1c26a4be9a4aa77a62f685f36095593
- DOI: 10.1038/s41598-023-41657-6
- PMID: 37653073
- PMCID: 10471605
- Citations: 8
- Summary: The complete genome of B. mandrillaris isolated from a freshwater artificial lagoon was sequenced and assembled, obtaining an assembled genome with better assembly quality parameter values than the currently available genomes and helping prioritize which target genes could be used to develop new treatments.
- Evidence snippets:
  - Snippet 1 (score: 0.744)
    > For the ITSON01 strain, 67% of its genes were annotated as proteins with functional descriptions, 31% as proteins without functional descriptions (hypothetical proteins), and 2% as noncoding genes (rRNA and tRNA). In the case of the V039 strain, 63% of its genes were identified as proteins with functional descriptions, 35% as hypothetical proteins, and 2% as rRNA and tRNA. Finally, for the 2046 strain, 63% of its genes were described as proteins with functional descriptions, 35% as hypothetical proteins, and 2% as tRNA.
    > It should be noted that in the case of the 2046 strain, complete ribosomal RNAs could not be annotated due to the high fragmentation of the genome. A detailed summary of the annotation results for each strain    2. Regarding lncRNAs, in the ITSON01 strain, two were annotated as MESTIT1, one as NPPA-AS1, and one as TCL6, whereas in the V039 strain, three were annotated as CDKN2B-AS, NPPA-AS1, and Six3os1.
    > Regarding the length distribution of the rRNA structures, in the ITSON01 strain, the large subunit (LSU) varied from 3625 to 5239 bp, and the small subunit (SSU) varied from 2017 to 2022 bp. In the V039 strain, the LSU varied from 3487 to 3853 bp, and the SSU varied from 2010 to 2028 bp. Additionally, the length of 5S rRNA was 119 bp in both strains. Some examples of structures of such rRNA obtained with StructRNAfinder are presented below (Fig. 3).
    > The GO term annotation comparison revealed a similar profile for the 3 strains, except for some smaller gene families that represented less than 0.1% of the genes (Fig. 4).

### [5] De Novo Genome Assembly and Phylogenetic Analysis of Cirsium nipponicum
- Authors: Bae Young Choi, Jaewook Kim, Hyeonseon Park, Jincheol Kim, Seahee Han et al.
- Year: 2024
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/658e8e30fac9b7c176a0e8e3f095d9f58b9c93a0
- DOI: 10.3390/genes15101269
- PMID: 39457393
- PMCID: 11507141
- Summary: This study provides a reference genome of C. nipponicum, enhancing the understanding of its genetic background and facilitating an exploration of genetic resources for beneficial phytochemicals.
- Evidence snippets:
  - Snippet 1 (score: 0.728)
    > accessed on 23 March 2016). GeneMarkS-T was employed to predict genes in the unique isoforms [31]. Finally, all predicted gene models were combined to produce non-redundant and consensus gene sets using TSEBRA [23].
    > Functional annotation of protein-coding genes were conducted using EnTAP v. 1.1.1 [32] with two methods. First, protein sequences of protein-coding genes were subjected to a BLASTp analysis against the NCBI RefSeq database [33] and Uniprot database using DI-AMOND [26,34]. Second, genes were annotated with KEGG terms and GO terms using eggNOG-mapper [35].
    > Transfer RNA (tRNA) genes were annotated using tRNAscan-SE v. 2.0.12 with eukaryote parameters [36]. Ribosomal RNA (rRNA) and its subunits were identified using Barrnap v. 0.9 in Eukaryotic mode [37]. To detect microRNA (miRNA) and small nuclear RNA (snRNA), sequence analysis was conducted by comparing against the Rfam database using Infernal's cmscan v. 1.1.5 [38,39].

### [6] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.726)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [7] A Frameshift Mutation in the Methyltransferase rlmN Is Associated with Increased Linezolid Resistance in Mycobacterium tuberculosis
- Authors: B. Reimer, A. G. Green
- Year: 2025
- Venue: Computational and Structural Biotechnology Journal
- URL: https://www.semanticscholar.org/paper/a260edff8f4ae0bcf9468eb43ed7c04ba9046560
- DOI: 10.34133/csbj.0090
- PMID: 42124926
- PMCID: 13158455
- Summary: An analysis of strains with paired whole-genome sequencing and linezolid minimum inhibitory concentration (MIC) phenotyping reveals that a relatively common frameshift mutation in MTB methyltransferase rlmN is significantly associated with increased linezolid MIC.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > To find all confirmed and putative methyltransferases in MTB, we combined several strategies. First, we searched the standard 2011 H37Rv annotation furnished by Mycobrowser [ 13 ] as well as a newly released reannotation of H37Rv [ 14 ] for "methyltransferase" and "RNA". We noted all genes and pseudogenes that were found in this manner (see the Supplementary Materials), whether or not they were included in the final list, and, if not, why.
    > Additionally, we searched UniProt [ 15 ] for methyltransferases thought to have RNA-binding ability. Because some methyltransferases have dual specificity for transfer RNA and rRNA, we searched for any RNA methyltransferase that either was in the methyltransferase class (Enzyme Commission number 2.1.1.*) [ 16 ] or was annotated with the Gene Ontology (GO) term for RNA methyltransferase activity (GO:0008173) [ 17 , 18 ]. Specifically, we used the following search terms:
    > Search 1: "ec:2.1.1.* H37Rv -H37Ra RNA". We then looked for evidence of ribosomal methylation in the protein annotation.
    > Search 2: "GO:0008173 H37Rv -H37Ra". Any protein that was found by these methods and that seemed likely to have RNA methyltransferase activity based on experimental evidence or homology was included in our catalog.

### [8] High-quality chromosome-level genome assembly of the Northern Pacific sea star Asterias amurensis
- Authors: Zhichao Huang, Qi Liu, Xiaoqi Zeng, Gang Ni
- Year: 2024
- Venue: DNA Research: An International Journal for Rapid Publication of Reports on Genes and Genomes
- URL: https://www.semanticscholar.org/paper/fdf7285020b4962ffe6c8225e147eb17725e2fa8
- DOI: 10.1093/dnares/dsae007
- PMID: 38416146
- PMCID: 11090083
- Citations: 2
- Summary: The significantly enriched pathways and Gene Ontology terms related to the amplified gene family were mainly associated with immune response and energy metabolism, suggesting that these factors might have contributed to the adaptability of A. amurensis to its environment.
- Evidence snippets:
  - Snippet 1 (score: 0.712)
    > Genome annotation mainly includes three aspects: repetitive recognition, non-coding RNA prediction, gene structure prediction, and functional annotation.
    > Homology prediction using RepeatMasker (vopen-4.0.9) and RepeatProteinMask based on RepBase (http:// www.girinst.org/repbase) and de novo prediction using RepeatModeler (v open-1.0.11), ][35][36] Combined with homologous prediction, de novo prediction (software: Augustus, Genscan, GlimmerHMM), cDNA/ EST prediction to make structural prediction of coding genes. 37,38 Meanwhile, RNA-seq data (accession numbers: SRR26104401, BioProject ID: PRJNA1016059) were compiled by Tophat alignment and Cufflinks assembled transcripts. 39 By using the MAKER, the predicted gene sets can be integrated into a non-redundant and more comprehensive gene set. Additionally, by incorporating the CEGMA results and implementing the HiCESAP workflow, a final reliable gene set can be obtained. 40 Finally, the proteins in the gene set will be functionally annotated using external protein databases such as SwissProt, TrEMBL, Kyoto Encyclopedia of Genes and Genomes (KEGG), InterPro, and Gene Ontology (GO). 41,42 he tRNAscan-SE software was used to find tRNA sequences in the genome. The reference sequence for rRNA from Invertebrates is selected, and BLASTN alignment is performed to identify rRNA sequences within the genome. By utilizing the covariance models from the Rfam database and employing the INFERNAL software provided by Rfam, it is possible to predict the miRNA and snRNA sequences present in the genome. 43,44

### [9] A high-quality chromosome-level genome assembly of the Chinese medaka Oryzias sinensis
- Authors: Zhongdian Dong, Jiangman Wang, Guozhu Chen, Yusong Guo, Na Zhao et al.
- Year: 2024
- Venue: Scientific Data
- URL: https://www.semanticscholar.org/paper/22e6bac57aff18bdef6ecc2240c145ad3758b9ee
- DOI: 10.1038/s41597-024-03173-8
- PMID: 38548787
- PMCID: 10978949
- Citations: 5
- Summary: A high-quality chromosome-level genome assembly of O. sinensis is generated using single-tube long fragment read (stLFR) reads, Nanopore long-reads, and Hi-C sequencing data and ATAC-seq is used to uncover chromosome transposase-accessibility as well as related genome area function enrichment for Oryzias sinensis.
- Evidence snippets:
  - Snippet 1 (score: 0.712)
    > From inner to outer circles: Density of genes with 500 kbp windows, ranging from 0 to 50; Density of TE with 500 kbp windows, ranging from 0 to 600; Density of TRF with 500 kbp windows, ranging from 0 to 450; Distributions of GC content with 500 kbp windows. (B) Hi-C interaction heat map and scatter plot of genome assembly GC content and sequencing depth.
    > Trinity, before PASA was used to get a gene model. Finally, all evidence was merged to form a consensus gene structure annotation result using GLEAN 30 . A total of 22,461 protein-coding genes were successfully predicted. BUSCO 19 assessments reached 94.6% using the actinopterygii_odb9 database, indicating relatively complete gene annotation coverage (Table 3).
    > All predicted genes were compared with public biological function databases including KEGG 31 , Swissprot 32 , and TrEMBL 33 (https://www.uniprot.org/statistics/TrEMBL) using BLASTp 34 with an E-value cutoff of 1e-5 for functional annotation. Interpro was applied to provide functional analysis of protein sequences by classifying them into families and predicting the presence of domains and important sites, followed by Gene Ontology annotation [35][36][37] . Overall, 22,162 protein-coding genes (98.67%) were successfully functionally annotated (Table 5).
    > Non-coding RNAs (ncRNAs) are an important part of genome annotation as they can be active in transcriptional and translational regulation of gene expression as well as in the modulation of protein function 38 . Since ribosomal RNA (rRNA) was highly conservative, vertebrate rRNA data was used as a reference to map to the draft genome using BLASTn with an E-value of 1e-5. For the discovery of transfer RNA (tRNA), tRNAscan-SE v1.3.1 was applied with eukaryotic parameters according to the characteristics of tRNA 39 . Rfam database was applied to find microRNAs (miRNA) and small nuclear RNA (snRNA) 40,41 .

### [10] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.711)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [11] ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance
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
  - Snippet 1 (score: 0.710)
    > To reduce redundancy while preserving sequence diversity, the 235,441 validated ORFs were subjected to two-stage clustering using VSEARCH v2.21.1: first at 90% sequence identity, then refined at 95% identity. Cluster representatives were aligned against UniProt/Swiss-Prot (release 2024_01) using DIAMOND v2.0.15 in sensitive mode (--sensitive). The initial alignment yielded 62,689 ORFs with putative UniProt matches. For each match, protein names, functional descriptions, and Gene Ontology (GO) terms were extracted for downstream label assignment.
    > 2.1.4. Functional labeling. Functional labels (Enzymatic, Structural, Transport, Other) were assigned to the 62,689 UniProt-mapped ORFs using hierarchical keyword matching against a curated dictionary of 847 functional terms derived from UniProt protein descriptions and Gene Ontology annotations. The classification hierarchy prioritized primary molecular functions:
    > • Enzymatic: Proteins with catalytic activity (GO:0003824), including polymerases, proteases, methyltransferases, and helicases
    > • Structural: Proteins involved in virion assembly and structural maintenance (GO:0019012), including spike, envelope, membrane, and nucleocapsid proteins
    > • Transport: Proteins mediating membrane transport and ion channels (GO:0006810, GO:0015267)
    > • Other: All remaining ORFs, including regulatory proteins, accessory factors, and hypothetical proteins ORFs with ambiguous or conflicting annotations (e.g., proteins with both enzymatic and structural roles) were manually reviewed by two independent annotators, achieving 94.2% inter-annotator agreement (Cohen's κ = 0.92). After removing ambiguous cases, this resulted in 53,575 unique labeled ORF sequences with unambiguous functional assignments.The 'Other' category encompasses a functionally heterogeneous set of accessory proteins with distinct biological roles, as summarized in Table 1 Variants were filtered to retain only those with ≥2% sequence divergence from their corresponding base ORF to ensure meaningful diversity while maintaining functional annotation consistency.

### [12] Phylogenomics of 10,575 genomes reveals evolutionary proximity between domains Bacteria and Archaea
- Authors: Qiyun Zhu, U. Mai, W. Pfeiffer, Stefan Janssen, F. Asnicar et al.
- Year: 2019
- Venue: Nature Communications
- URL: https://www.semanticscholar.org/paper/7e3866b2d5d92fc28f91181a5393610760cba94d
- DOI: 10.1038/s41467-019-13443-4
- PMID: 31792218
- PMCID: 6889312
- Citations: 299
- Influential citations: 22
- Summary: A reference phylogeny of 10,575 evenly-sampled bacterial and archaeal genomes, based on a comprehensive set of 381 markers, is built, providing an updated view of domain-level relationships between Archaea and Bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > Each genome was given a unique identifier, which was derived from the NCBI accession of the corresponding assembly, but without version number. For example, a genome with assembly accession "GCF_000123456.1" was identified as "G000123456" in this study. In cases when the same genome was present in both GenBank (accession starting with "GCA_") and RefSeq (accession starting with "GCF_"), only the RefSeq version was kept.
    > Annotation and classification of marker genes. The functional annotation of the 400 PhyloPhlAn marker genes 25 was performed by aligning the protein sequences of the 400 marker genes (inferred from 2887 bacterial and archeal genomes as described in Segata et al. 25 ) against the UniRef50 database (March 2018 release) using BLASTp. The best hit for each gene was taken and queried against the UniProt database for gene and protein names. To categorize genes by function, the UniProt entries were translated into Gene Ontology (GO) terms 40 with the "sub-set_prokaryote" tag (March 2018 release). Because not all UniProt entries have corresponding GO terms, manual curation was involved to pick the most appropriate GO terms for those cases by examining the BLAST hit table. GO terms were further translated into GO slim terms to obtain higher-level functional categories.
    > Note that this analysis is independent from the phylogenetic analysis of the current genome data set, and the result can be used as a reference for PhyloPhlAn users.
    > Analyses of genome sequences and identification of marker genes. The DNA sequences of the 86,200 bacterial and archaeal genomes were subjected to the following analyses:
    > 1. The quality scores for DNA, protein, tRNA, and rRNA were calculated following Land et al. 41 . 2. A MinHash sketch was built for each genome using Mash 1.1.1 42 , with default settings (sketch size = 1000, k-mer size = 21), based on which a pairwise distance matrix was built for the entire genome pool. In brief, MinHash is a k-mer hashing technique that enables the quantification of genome-to-genome distance.

### [13] Methyltransferase That Modifies Guanine 966 of the 16 S rRNA
- Authors: Dmitry V. Lesnyak, J. Osipiuk, T. Skarina, P. Sergiev, A. Bogdanov et al.
- Year: 2007
- Venue: Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/6694f459f1c71e750efbebd82897ab61a57e7f75
- DOI: 10.1074/jbc.M608214200
- PMID: 17189261
- Citations: 87
- Influential citations: 4
- Summary: Structural comparisons and analysis of the enzyme active site suggest modes for binding AdoMet and rRNA to m2G966 methyltransferase, and the protein expressed from the yhhF gene was renamed to RsmD, a model for interaction of RSMD with ribosome has been proposed.
- Evidence snippets:
  - Snippet 1 (score: 0.703)
    > N 2 -Methylguanine 966 is located in the loop of Escherichia coli 16 S rRNA helix 31, forming a part of the P-site tRNA-binding pocket. We found yhhF to be a gene encoding for m 2 G966 specific 16 S rRNA methyltransferase. Disruption of the yhhF gene by kanamycin resistance marker leads to a loss of modification at G966. The modification could be rescued by expression of recombinant protein from the plasmid carrying the yhhF gene. Moreover, purified m 2 G966 methyltransferase, in the presence of S-adenosylomethionine (AdoMet), is able to methylate 30 S ribosomal subunits that were purified from yhhF knock-out strain in vitro. The methylation is specific for G966 base of the 16 S rRNA. The m 2 G966 methyltransferase was crystallized, and its structure has been determined and refined to 2.05 A ˚. The structure closely resembles RsmC rRNA methyltransferase, specific for m 2 G1207 of the 16 S rRNA. Structural comparisons and analysis of the enzyme active site suggest modes for binding AdoMet and rRNA to m 2 G966 methyltransferase. Based on the experimental data and current nomenclature the protein expressed from the yhhF gene was renamed to RsmD. A model for interaction of RsmD with ribosome has been proposed.
    > Ribosomal RNAs form the main functional core of the ribosome, a universal molecular machine for protein synthesis. It is believed that primordial ribosome was initially composed entirely of RNA (1) and proteins were added later in evolution.
    > A set of four ribonucleotides used in rRNA is rather limited for the full range and fine tuning of ribosomal functions especially when compared with 20 amino acids the proteins are composed of. The diversity in RNA could be increased through the usage of a set of modified nucleotides (2). A number of such nucleotides have been found in functional ribosomal RNA molecules (as well as other RNA).

### [14] Computational Discovery of Transcriptional Regulatory Modules in Fungal Ribosome Biogenesis Genes Reveals Novel Sequence and Function Patterns
- Authors: V. Martyanov, R. H. Gross
- Year: 2013
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/986fb7b3472c53c1891d806144874429471d3d13
- DOI: 10.1371/journal.pone.0059851
- PMID: 23555806
- PMCID: 3612091
- Summary: Several likely new candidates for a role in ribosome biogenesis in S. cerevisiae are identified based on the combined evidence of RBA module presence in the upstream regions, functional annotation information and microarray expression profiles.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > For S. cerevisiae, we used the extra gene feature of SCOPE and identified 12 previously unreported genes containing RBA modules (8 with RRPE-PAC and 4 with PAC-RRPE). By utilizing functional annotation and microarray expression data (see Materials and Methods), we were able to find evidence from at least one other source for 8 genes and from two sources for 4 genes. Based on these analyses, we can hypothesize about several new candidates for a role in ribosome biogenesis in S. cerevisiae.
    > The 4 candidate genes that are most likely involved in RBA (supported as such by SCOPE motif and module data, SGD functional description information and SPELL expression data) are as follows. YDR465C is an arginine methyltransferase that methylates ribosomal protein RPL12. YGR272C is an essential protein required for maturation of 18S rRNA. YPR010C is the second largest subunit of RNA polymerase I. YNL061W is a probable RNA methyltransferase essential for large ribosomal subunit biogenesis. Table 5 describes which genes are supported by which analyses and Table S4 contains more information about all 12 predicted genes.

### [15] Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation
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
  - Snippet 1 (score: 0.698)
    > To homogenize the genome annotation, the sequences of all genomes were analysed using the same protocol. The proteinencoding genes were predicted using Prokka version 1.13 [24], and the predicted protein sequences were functionally annotated using Sma3s v2 and UniProt taxonomic division bacteria 2019_01 as a reference database [25,55].
    > To annotate specific genes, GO (gene ontology) terms and UniProt keywords assigned by Sma3s were used. To find genes associated with CRISPR systems, protein sequences coming

### [16] Deltamethrin Selection Drives Transcriptomic Changes in Detoxification, Immune, and Cuticle Genes in Aedes aegypti
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
  - Snippet 1 (score: 0.696)
    > The AegL5 gene set contains over 19,804 predicted genes (14,718 protein-coding genes, 5086 non-protein-coding genes, and 382 pseudogenes). However, functional annotation is available for only 6319, and gene ontology (GO) annotation terms are assigned to 11,097 of the protein-coding genes. To enhance the interpretation of the data, the computational annotation of the AegL5 set was performed using Blast2GO (see Methods). This analysis assigned putative functional descriptions to 13,322 and GO terms to 11,680 of the protein-coding genes. All the annotation results from both Vector-Base and Blast2GO are provided in File S5.
    > Gene ontology enrichment analysis (GOEA) was performed on the DE genes (up and downregulated, separately) from each F S4 vs. F S0 (3 in total). The significantly enriched GO terms, including biological process, molecular function, and cellular component categories, are reported in File S6. GO molecular function terms that were significantly enriched in at least two out of the three comparisons are summarized in Figure S1.
    > For the upregulated genes, GO molecular function terms associated with binding activities (ATP, nucleic acid, RNA, Adenyl ribonucleotide/nucleotide small molecule, organic cyclic compounds), transferase activity (methyl, one-carbon group), helicase, and ATP-dependent activities were significantly enriched, suggesting the potential role of these key molecular functions following insecticide selection. Of note, GO terms associated with methyltransferase activity were significantly enriched in the upregulated genes. Among these, tRNA (cytosine34-C5)-methyltransferase (AAEL013968) was consistently detected among the top 10 DE genes from all three F S4 vs. F S0 comparisons. This may suggest the involvement of the RNA methylation process in response to insecticide selection; however, direct evidence for DNA or RNA methylation in Ae. aegypti under deltamethrin exposure is currently lacking.

### [17] CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts
- Authors: Alison C. Testa, James K. Hane, S. Ellwood, R. Oliver
- Year: 2015
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/06704917bf44cd62eef0bb5cb944b97484056e21
- DOI: 10.1186/s12864-015-1344-4
- PMID: 25887563
- PMCID: 4363200
- Citations: 164
- Influential citations: 20
- Summary: CodingQuarry is a highly accurate, self-training GHMM fungal gene predictor designed to work with assembled, aligned RNA-seq transcripts, which capitalises on the high quality of fungal transcript assemblies by incorporating predictions made directly from transcript sequences.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > Whole-genome sequencing has enabled investigations into the gene content of living many organisms and forms the foundation for further study of gene expression, proteomics and epigenetics. After assembly of a novel genome, gene annotation is often the first step in analysing the gene content of an organism. Accurate annotation of the exonic structure of genes is crucial to the success of all subsequent functional and comparative analyses.
    > Problems that can potentially be caused by incorrect gene annotation are numerous and can lead to incorrect assessments of the lifestyle and ecology of an organism. In comparative genomics where orthologous genes or conserved functional domains are compared between species/isolates, the estimated numbers of such genes/ domains can be distorted by less than perfect annotations (as described by Hane et al. [1], S Text 1). Prediction of extracellular secretion, which can be determined by a short signal peptide at the N-terminus, can miss secreted proteins if the start codon of a gene has been incorrectly annotated. Mis-annotating the start of protein translation could either cut off the signal peptide or bury it within the annotation. While a seemingly benign annotation error, the consequences for downstream research could be detrimental, particularly as the biotic interactions or industrial applications of microbes are largely determined by their secretomes. Additionally, translated protein sequences of novel species are often submitted to databases such as NCBI [2] and Uniprot [3]. It is commonplace to use these database entries to support the annotation of related species or isolates, meaning errors present in the pioneer annotation may be repeated. When these new annotations based on false assumptions are added to databases, there is not only a propagation of errors, but also a perceived strengthening of homology evidence for incorrect protein sequences.
    > In recent years, correction of in silico predicted gene annotations with RNA-seq derived transcripts and read alignments has enabled vastly improved genome annotations and corrections of annotated gene structures [4][5][6].

### [18] A Literature-Derived Knowledge Graph Augments the Interpretation of Single Cell RNA-seq Datasets
- Authors: D. Doddahonnaiah, P. Lenehan, T. Hughes, D. Zemmour, E. Garcia-Rivera et al.
- Year: 2021
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/f078685c8e996b4e80f3f872f296e1c14b17e01a
- DOI: 10.3390/genes12060898
- PMID: 34200671
- PMCID: 8229796
- Citations: 10
- Summary: An NLP framework is deployed to objectively quantify associations between a comprehensive set of over 20,000 human protein-coding genes and over 500 cell type terms across over 26 million biomedical documents and illustrates for the first time how the systematic application of a literature derived knowledge graph can expedite and enhance the annotation and interpretation of scRNA-seq data.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > We obtained the full set of human protein-coding genes from HGNC [24] and curated potential gene synonyms from various sources including ENTREZ, UniProt, Ensembl, and Wikipedia. For specific gene families, we also manually added family-level synonyms which are not captured by synonyms curated at the single gene level. This included genes encoding the following proteins: T cell receptor subunits, immunoglobulin subunits, class II MHC molecules, hemoglobin subunits, surfactant proteins, chymotrypsinogen subunits, CD8 subunits (CD8A, CD8B), and CD3 subunits (CD3E, CD3G, CD3D, and CD247). The complete gene vocabulary is given in File S4.
    > For the cell type annotation algorithm described subsequently, we only considered protein-coding genes which were strongly associated with at least one cell type in the literature (local score ≥ 3; see description of local scores below). Further, we excluded mitochondrially encoded genes (gene names starting with "MT-"), genes encoding ribosomal proteins (gene names starting with "RPS", "RPL", "MRPS", or "MRPL"), and MHC class I genes except for HLA-G (HLA-A, HLA-B, HLA-C, HLA-E, HLA-F). These filtering steps yielded a final set of 5113 "eligible genes" for consideration during the cell type annotation steps (indicated in File S4).

### [19] Metadata Standard and Data Exchange Specifications to Describe, Model, and Integrate Complex and Diverse High-Throughput Screening Data from the Library of Integrated Network-based Cellular Signatures (LINCS)
- Authors: U. Vempati, Caty Chung, Christopher Mader, Amar Koleti, Nakul Datar et al.
- Year: 2014
- Venue: Journal of Biomolecular Screening
- URL: https://www.semanticscholar.org/paper/91af493a67a83d599ad00f4da275e8eadd165b5e
- DOI: 10.1177/1087057114522514
- PMID: 24518066
- Citations: 83
- Influential citations: 3
- Summary: The National Institutes of Health Library of Integrated Network-based Cellular Signatures (LINCS) program is generating extensive multidimensional data sets, including biochemical, genome-wide transcriptional, and phenotypic cellular response signatures to a variety of small-molecule and genetic perturbations with the goal of creating a sustainable, widely applicable, and readily accessible systems biology knowledge resource. Integration and analysis of diverse LINCS data sets depend on the a...
- Evidence snippets:
  - Snippet 1 (score: 0.680)
    > Although this is a fairly obvious requirement, it is not trivial to implement because a protein reagent expressed recombinantly is typically not the exact same entity or in the same state as its corresponding assay participant in a living cell (e.g., kinase domain binding assay vs. corresponding kinase occurring in a specific cell line used for a growth inhibition assay). In this first version of metadata standards, we take a rudimentary approach. We use the UniProt accession and approved Gene symbol (NCBI Gene) and accession number to identify and reference proteins and their coding genes, respectively. Although we recognize limitations, for the purpose of our current simple use cases, this is sufficient. Linking protein and gene identifiers in addition is relevant to integrate RNAi reagent gene targets (see below). The recommended explicit fields for proteins include a standardized name, both for the protein and the gene that encodes it; source of protein (e.g., chemically synthesized, purified from natural source, recombinantly expressed); protein modifications (e.g., mutations, posttranslational modification); protein purity; subunit information for components of a protein complex; and isoform information (derived from either alternative promoter usage, alternative splicing, alternative translation initiation, or frame shifting). We are currently working on a formal description of proteins that will allow ambiguity (more-or less-specific definition of proteins), because in some cases, the exact entity and state of a protein reagent or model system participant is not definitively known (full length, functional domain, exact sequence, mutation, phosphorylation state, etc.).
    > Inhibitory RNAs (siRNA, shRNA). RNA interference is a standard methodology to transiently knock down gene expression in living cells. This can be achieved using different types of small RNA molecules, including siRNA, shRNA, and miRNA. Information that is relevant to identify and describe these perturbations include probe ID, name, source/provider, target gene symbol and accession number, sequence of the probe, and modifications to the probe (e.g., chemical modification) if any are specified.
    > Antibody Reagents.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Alejandro Otero-Ruiz, L. Z. Rodriguez-Anaya, F. Lares-Villa, Luis Fernando Lozano Aguirre Beltrán, L. F. Lares-Jiménez et al. (2023). Functional annotation and comparative genomics analysis of Balamuthia mandrillaris reveals potential virulence-related genes. Scientific Reports. https://www.semanticscholar.org/paper/2507f970e1c26a4be9a4aa77a62f685f36095593
5. Bae Young Choi, Jaewook Kim, Hyeonseon Park, Jincheol Kim, Seahee Han et al. (2024). De Novo Genome Assembly and Phylogenetic Analysis of Cirsium nipponicum. Genes. https://www.semanticscholar.org/paper/658e8e30fac9b7c176a0e8e3f095d9f58b9c93a0
6. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
7. B. Reimer, A. G. Green (2025). A Frameshift Mutation in the Methyltransferase rlmN Is Associated with Increased Linezolid Resistance in Mycobacterium tuberculosis. Computational and Structural Biotechnology Journal. https://www.semanticscholar.org/paper/a260edff8f4ae0bcf9468eb43ed7c04ba9046560
8. Zhichao Huang, Qi Liu, Xiaoqi Zeng, Gang Ni (2024). High-quality chromosome-level genome assembly of the Northern Pacific sea star Asterias amurensis. DNA Research: An International Journal for Rapid Publication of Reports on Genes and Genomes. https://www.semanticscholar.org/paper/fdf7285020b4962ffe6c8225e147eb17725e2fa8
9. Zhongdian Dong, Jiangman Wang, Guozhu Chen, Yusong Guo, Na Zhao et al. (2024). A high-quality chromosome-level genome assembly of the Chinese medaka Oryzias sinensis. Scientific Data. https://www.semanticscholar.org/paper/22e6bac57aff18bdef6ecc2240c145ad3758b9ee
10. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
11. FuGuo Liu, T. Lai, Wenxia Xu, Guodong Li (2026). ViralMultiNet: A structure-aware multimodal framework for viral protein function prediction in wastewater surveillance. PLOS One. https://www.semanticscholar.org/paper/7d7965ec223f5715675839cb57efdc776d25e216
12. Qiyun Zhu, U. Mai, W. Pfeiffer, Stefan Janssen, F. Asnicar et al. (2019). Phylogenomics of 10,575 genomes reveals evolutionary proximity between domains Bacteria and Archaea. Nature Communications. https://www.semanticscholar.org/paper/7e3866b2d5d92fc28f91181a5393610760cba94d
13. Dmitry V. Lesnyak, J. Osipiuk, T. Skarina, P. Sergiev, A. Bogdanov et al. (2007). Methyltransferase That Modifies Guanine 966 of the 16 S rRNA. Journal of Biological Chemistry. https://www.semanticscholar.org/paper/6694f459f1c71e750efbebd82897ab61a57e7f75
14. V. Martyanov, R. H. Gross (2013). Computational Discovery of Transcriptional Regulatory Modules in Fungal Ribosome Biogenesis Genes Reveals Novel Sequence and Function Patterns. PLoS ONE. https://www.semanticscholar.org/paper/986fb7b3472c53c1891d806144874429471d3d13
15. Eugenio L Mangas, Alejandro Rubio, R. Álvarez-Marín, Gema Labrador-Herrera, J. Pachón et al. (2019). Pangenome of Acinetobacter baumannii uncovers two groups of genomes, one of them with genes involved in CRISPR/Cas defence systems associated with the absence of plasmids and exclusive genes for biofilm formation. Microbial Genomics. https://www.semanticscholar.org/paper/ccdc06e24b4cff1ddca5e537c65e5f14c5f017b3
16. Y. Contreras-Perera, L. Mackenzie-Impoinvil, Dieunel Derilus, Audrey Lenhart, I. Rodríguez-Sánchez et al. (2025). Deltamethrin Selection Drives Transcriptomic Changes in Detoxification, Immune, and Cuticle Genes in Aedes aegypti. Tropical Medicine and Infectious Disease. https://www.semanticscholar.org/paper/21e5f9022b6c14afa8f193ff59151db6228bc141
17. Alison C. Testa, James K. Hane, S. Ellwood, R. Oliver (2015). CodingQuarry: highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts. BMC Genomics. https://www.semanticscholar.org/paper/06704917bf44cd62eef0bb5cb944b97484056e21
18. D. Doddahonnaiah, P. Lenehan, T. Hughes, D. Zemmour, E. Garcia-Rivera et al. (2021). A Literature-Derived Knowledge Graph Augments the Interpretation of Single Cell RNA-seq Datasets. Genes. https://www.semanticscholar.org/paper/f078685c8e996b4e80f3f872f296e1c14b17e01a
19. U. Vempati, Caty Chung, Christopher Mader, Amar Koleti, Nakul Datar et al. (2014). Metadata Standard and Data Exchange Specifications to Describe, Model, and Integrate Complex and Diverse High-Throughput Screening Data from the Library of Integrated Network-based Cellular Signatures (LINCS). Journal of Biomolecular Screening. https://www.semanticscholar.org/paper/91af493a67a83d599ad00f4da275e8eadd165b5e