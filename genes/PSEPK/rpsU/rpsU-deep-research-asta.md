---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T08:40:39.704672'
end_time: '2026-07-09T08:40:45.364650'
duration_seconds: 5.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rpsU
  gene_symbol: rpsU
  uniprot_accession: P0A165
  protein_description: 'RecName: Full=Small ribosomal subunit protein bS21 {ECO:0000305};
    AltName: Full=30S ribosomal protein S21;'
  gene_info: Name=rpsU; OrderedLocusNames=PP_0389;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial ribosomal protein bS21 family.
  protein_domains: Ribosomal_bS21. (IPR001911); Ribosomal_bS21_CS. (IPR018278); Ribosomal_bS21_sf.
    (IPR038380); Ribosomal_S21 (PF01165)
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
- **UniProt Accession:** P0A165
- **Protein Description:** RecName: Full=Small ribosomal subunit protein bS21 {ECO:0000305}; AltName: Full=30S ribosomal protein S21;
- **Gene Information:** Name=rpsU; OrderedLocusNames=PP_0389;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial ribosomal protein bS21 family.
- **Key Domains:** Ribosomal_bS21. (IPR001911); Ribosomal_bS21_CS. (IPR018278); Ribosomal_bS21_sf. (IPR038380); Ribosomal_S21 (PF01165)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rpsU" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rpsU' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rpsU** (gene ID: rpsU, UniProt: P0A165) in PSEPK.

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

### [1] Genomic analysis reveals the biotechnological and industrial potential of levan producing halophilic extremophile, Halomonas smyrnensis AAD6T
- Authors: Elif Diken, T. Ozer, M. Arıkan, Z. Emrence, E. Oner et al.
- Year: 2015
- Venue: SpringerPlus
- URL: https://www.semanticscholar.org/paper/b5e5ea11a592b4a5d4494e455c197add1a6ec2c2
- DOI: 10.1186/s40064-015-1184-3
- PMID: 26251777
- PMCID: 4523562
- Citations: 37
- Influential citations: 1
- Summary: The whole- Genome analysis was performed to gain more insight about the biological mechanisms, and the whole-genome organization of the bacterium, and Industrially crucial genes, including the levansucrase, were detected and the genome-scale metabolic model of H. smyrnensis AAD6T was reconstructed.
- Evidence snippets:
  - Snippet 1 (score: 0.879)
    > Gene prediction and genome annotation were carried out using the RAST auto-annotation server (Aziz et al. 2008). Protein-encoding and transfer RNA genes were predicted by RAST server, while the ribosomal RNA genes were identified with RNAmmer (v1.2) (Lagesen et al. 2007). The gene predictions of essential biosystems were manually verified using BLAST searches against protein databases, the Universal Protein Resource (UniProt) (http:// www.uniprot.org/) and National Center for Biotechnology Information (NCBI) (http://www.ncbi.nlm.nih.gov/). The gene functions and classifications were based on the subsystem annotation of the RAST server. Information on enzyme-encoding genes was taken from Kyoto Encyclopedia of Genes and Genomes (KEGG) (Kanehisa et al. 2012) and ExPaSy databases (Artimo et al. 2012). Transport protein coding genes were annotated using the similarity searches against the Transfer Classification Database (TCDB) (Saier et al. 2009).

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
  - Snippet 1 (score: 0.853)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

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
  - Snippet 1 (score: 0.831)
    > In transcriptomics and proteomics studies, one important step of data analysis is the functional annotation of obtained lists of differentially expressed genes (DEGs) or proteins (DEPs). With the increase in the number of organisms with sequenced and annotated genomes, such studies have been performed in many different species. However, the information about gene and protein functions, on which the annotation is based, is mainly derived from a limited number of model organisms or well-annotated species, such as mouse, humans and rat representing mammalian species or even from bacteria, yeast, worms or Drosophila. Based on the assumption that orthologous genes carry out identical or biologically equivalent functions in different organisms, functional annotation is transferred from wellstudied organisms to less well-annotated species (1). Whereas orthologous genes usually have maintained the same function during evolution (2) paralogous genes originated from gene duplication events and often evolved different functions (3,4). Orthologous genes usually have the same gene symbol and name for almost all corresponding species (5, 6). However, depending on the status of the gene annotation of a species, not all annotated genes have an official gene symbol (only locus number, e.g. LOC100152218 60S ribosomal protein L23a-like) and/or are assigned to functional annotation databases like their corresponding orthologs in the well-annotated model organisms. This leads to a substantial loss of information if the gene identifiers (IDs) of the respective species are used for functional annotation. To avoid this data loss and improve the results of functional annotation, one strategy is to transfer information from homologous genes (orthologs and paralogs) of well-annotated species (6).
    > In many situations with non-model species such as livestock species, experimentalists avoid the additional work to assign human ortholog genes for functional annotation analysis and are not aware of the information loss.

### [4] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.830)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

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
  - Snippet 1 (score: 0.829)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [6] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.823)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [7] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.819)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

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
  - Snippet 1 (score: 0.809)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

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
  - Snippet 1 (score: 0.799)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [10] De Novo Genome Assembly and Phylogenetic Analysis of Cirsium nipponicum
- Authors: Bae Young Choi, Jaewook Kim, Hyeonseon Park, Jincheol Kim, Seahee Han et al.
- Year: 2024
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/658e8e30fac9b7c176a0e8e3f095d9f58b9c93a0
- DOI: 10.3390/genes15101269
- PMID: 39457393
- PMCID: 11507141
- Summary: This study provides a reference genome of C. nipponicum, enhancing the understanding of its genetic background and facilitating an exploration of genetic resources for beneficial phytochemicals.
- Evidence snippets:
  - Snippet 1 (score: 0.784)
    > accessed on 23 March 2016). GeneMarkS-T was employed to predict genes in the unique isoforms [31]. Finally, all predicted gene models were combined to produce non-redundant and consensus gene sets using TSEBRA [23].
    > Functional annotation of protein-coding genes were conducted using EnTAP v. 1.1.1 [32] with two methods. First, protein sequences of protein-coding genes were subjected to a BLASTp analysis against the NCBI RefSeq database [33] and Uniprot database using DI-AMOND [26,34]. Second, genes were annotated with KEGG terms and GO terms using eggNOG-mapper [35].
    > Transfer RNA (tRNA) genes were annotated using tRNAscan-SE v. 2.0.12 with eukaryote parameters [36]. Ribosomal RNA (rRNA) and its subunits were identified using Barrnap v. 0.9 in Eukaryotic mode [37]. To detect microRNA (miRNA) and small nuclear RNA (snRNA), sequence analysis was conducted by comparing against the Rfam database using Infernal's cmscan v. 1.1.5 [38,39].

### [11] Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids
- Authors: G. Alama-Bermejo, E. Meyer, S. Atkinson, A. Holzer, Monika M. Wiśniewska et al.
- Year: 2020
- Venue: Genome Biology and Evolution
- URL: https://www.semanticscholar.org/paper/7d5e64908d9bea80accb9389be84679778625620
- DOI: 10.1093/gbe/evaa109
- PMID: 32467979
- PMCID: 7487138
- Citations: 18
- Summary: Host-free transcriptomes of a myxozoan model organism from strains that exhibited different degrees of virulence are developed, as a unique source of data that will foster functional gene analyses and serve as a base for the development of potential therapeutics for efficient control of these parasites.
- Evidence snippets:
  - Snippet 1 (score: 0.781)
    > We chose cell migration genes and proteases/inhibitors as candidate virulence factors, due to their relevance in hostpathogen interactions (e.g., Barragan and Sibley 2002;McKerrow et al. 2006;Bouzid et al. 2013). Given the low amount of functional (GO) annotation in our largest assembly, C. shasta þ NHP (see Results), we used BlastX to search for homologs of genes of interest in two custom concatenated databases that comprised the Cell Migration Knowledge Database (CMKB) which includes proteins, families, and complexes involved in cell migration (http://www.cellmigration. org/index.shtml, last accessed February 5, 2015; $7,600 protein sequences), and the MEROPS database, which consists of a nr library of full-length sequences of peptidases and peptidase inhibitors (http://merops.sanger.ac.uk/, last accessed December 2, 2014; $450,000 sequences; Rawlings et al. 2016). We searched using the longest representatives for each gene in the C. shasta þ NHP assembly (23,418 contigs; IIR-RBT6) then parsed matches (bit score > 100) and posteriorly classified homologs to proteases or motility genes matching the specific databases. We then selected only genes with the same annotation in UniProt (determined using the same standards: no ambiguous terms filtering, bit score > 100) to confirm gene identity. Due to disagreements between annotations (CMKB vs. UniProt, and MEROPS vs. UniProt), we curated gene lists manually, removing genes that matched one or more of the following criteria: 1) no genetic distances available (only available for reference); 2) disagreements between annotations from the different databases, after checking for synonyms or function similarity; 3) annotations that contained terms from UniProt "Uncharacterized protein" and "Predicted protein" (ambiguous terms), and whose identity could not be confirmed; and 4) annotations that contained nonspecific terms, such as "heat shock protein" or "ribosomal protein."

### [12] Draft genome sequence of type strain HBR26T and description of Rhizobium aethiopicum sp. nov.
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
  - Snippet 1 (score: 0.771)
    > Genes were predicted using Prodigal [46] and using the DOE JGJ annotation pipeline [47]. The identified protein-coding genes were translated and functionally annotated by comparing the sequences with the NCBI non-redundant database, UniProt, TIGRFam, Pfam, KEGG, COG, and InterPro databases. The tRNA genes were found using tRNAScanSE tool [48] and ribosomal RNA genes were identified by searches against models of the ribosomal RNA genes at the SILVA database [49].
    > Other non-coding RNAs such as the RNA components of the protein secretion complex and the RNase P were identified by searching the genome for the corresponding Rfam profiles using INFERNAL [50]. Additional analysis was accomplished using the IMG tool [51]. The same tool was also used for manual functional annotation of the predicted genes and for examining the genome sequence.

### [13] Soil properties and agricultural practices shape microbial communities in flooded and rainfed croplands
- Authors: Xiao-Yan Wang, Tianhua He, S. Gen, Xiao-qi Zhang, Xiao Wang et al.
- Year: 2020
- Venue: Applied Soil Ecology
- URL: https://www.semanticscholar.org/paper/39af2f84e27304c066c8a0da558194415f64dde5
- DOI: 10.1016/j.apsoil.2019.103449
- Citations: 34
- Summary: Abstract Understanding the dynamics of soil microbial communities and the factors that affect those dynamics is crucial for comprehending the processes affecting soil fertility in agricultural ecosystems. Here, we used shotgun DNA sequencing to characterise 29 soil microbial communities in flooded paddies in China's Yangtze River Basin, and comparatively analysed the composition and function of microbial communities with 132 communities from North and South America's rainfed cropland. We hypo...
- Evidence snippets:
  - Snippet 1 (score: 0.769)
    > To do so, sequence similarity was searched against several databases simultaneously--KEGG (Kyoto Encyclopedia of Genes and Genomes), NCBI (National Center for Biotechnology Information), RDP (Ribosomal Database Project), SEED (The SEED Project, Overbeek et al., 2005), UniProt (UniProt Knowledgebase), and eggNOG (evolutionary genealogy of genes Non-supervised Orthologous Groups) (Meyer et al., 2008). Genes were assigned to a subsystem by homology searches of protein sequences encoded by the reads. For both taxonomic assignment and function annotation, the match threshold was set at an expected value of < 1 × 10 −5 , similarity of > 50 bp, and a minimum identity of 65%. If no match was found in the relevant database, the sequence was classified as 'unclassified'. The taxonomic assignment and functional annotation results for each sample are deposited and retrievable from MG-RAST following the reference ID (Supplementary Table S1).

### [14] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2773
- Influential citations: 299
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.767)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [15] Identification of 12 New Yeast Mitochondrial Ribosomal Proteins Including 6 That Have No Prokaryotic Homologues*
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
  - Snippet 1 (score: 0.766)
    > However, this name does not allow one to discriminate between small and large subunit proteins and thus may be misleading. For example, Mrp2 is not the homologue of the prokaryotic S2 ribosomal proteins but belongs to the S14p family. Accordingly, we preferred to designate the newly identified genes RSMxx genes, where RSM stands for ribosomal small subunit of mitochondria, and xx is the number of the corresponding prokaryotic protein family (see Table II). The genes that encode proteins that are not significantly similar to prokaryotic proteins were named with the same prefix RSM followed by a number that begins with 22, because there are 21 prokaryotic small ribosomal subunit protein families. Thus, the proposed name of the YKL155c gene is RSM22 (Table II). The matched peptide has the sequence VT-PGSLYK. The differences between the masses of the marked peaks correspond to the masses of amino acid residues Gly, Pro, and Thr. D, the fragmentation spectrum for the peptide that is found within residues 400 -408 in the predicted sequence of Ygl129c shows a very good signal-to-noise ratio. Fragmentation spectra that were generated for other peptides show a signal-to-noise ratio between the two extremes shown in C and D.
    > A large amount of functional data was generated in the course of genetic screenings and functional genomic studies in yeast. Hence, for a number of the identified proteins, some cellular or functional data were already available in public data bases. In addition, for some of the less well characterized proteins, we analyzed the cellular localization of the GFP C-terminally tagged proteins and the respiratory competency of strains disrupted for the corresponding genes. These data are summarized in Table II and described below.
    > Functional Data on the New Proteins That Belong to Known Ribosomal Protein Families-Ribosomal protein families S7p and S10p are represented in yeast mitochondria by the corresponding homologues Yjr113c and Ydr041w. Mammalian homologues of S7 (19) and S10 (20) were also recently described as components of the bovine small mitochondrial ribosomal subunit.

### [16] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.752)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

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
  - Snippet 1 (score: 0.748)
    > Table S20 Small ribosomal proteins. Gene identifiers are given as contig identifiers with a gene suffix beginning with ''g'' followed by a number (which is arbitrary in this context). Only proteins #100 aa with domains found in Pfam 26.0 with an Evalue,0.01 and with some homologs in UniProt that are #120 aa (to ensure that they are genuine small proteins) are listed. Where alternative fragmentation occurs, the nanochromosome length of the shortest putative isoform encoding the small protein is shown. Protein domains are taken from Pfam 26.0. Contig22302.0 is a multigene nanochromosome. a These proteins are incorrectly predicted as gene fusions on the longer ribosomal/nonribosomal protein-encoding nanochromosome. (RTF) Table S21 Small nonribosomal proteins. Gene identifiers are given as contig identifiers with a gene suffix beginning with ''g'' followed by a number (which is arbitrary in this context). All nanochromosomes in this table longer than 1 kb are predicted to be multigene nanochromosomes. Proteins 50-100 aa long with domains found in Pfam 26.0 (independent E-value,0.01) and with at least some homologs in UniProt that are #120 aa (to ensure that they are genuine small proteins) are listed. We excluded a few proteins that appeared to be truncated by incomplete assembly of their nanochromosomes. Nanochromosome lengths exclude telomeres. Where alternative fragmentation occurs, the nanochromosome length of the shortest putative isoform encoding the small protein is shown. Protein domain names are from Pfam 26.0. (RTF) Table S22 RNA-seq counts for transcription initiation factor II domain protein genes. RNA expression values are given in normalized read counts for vegetative (''Fed'') cells and cells developing during conjugation (see Text S1: RNA-seq mapping and read counting).

### [18] Functional annotation and comparative genomics analysis of Balamuthia mandrillaris reveals potential virulence-related genes
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
  - Snippet 1 (score: 0.747)
    > For the ITSON01 strain, 67% of its genes were annotated as proteins with functional descriptions, 31% as proteins without functional descriptions (hypothetical proteins), and 2% as noncoding genes (rRNA and tRNA). In the case of the V039 strain, 63% of its genes were identified as proteins with functional descriptions, 35% as hypothetical proteins, and 2% as rRNA and tRNA. Finally, for the 2046 strain, 63% of its genes were described as proteins with functional descriptions, 35% as hypothetical proteins, and 2% as tRNA.
    > It should be noted that in the case of the 2046 strain, complete ribosomal RNAs could not be annotated due to the high fragmentation of the genome. A detailed summary of the annotation results for each strain    2. Regarding lncRNAs, in the ITSON01 strain, two were annotated as MESTIT1, one as NPPA-AS1, and one as TCL6, whereas in the V039 strain, three were annotated as CDKN2B-AS, NPPA-AS1, and Six3os1.
    > Regarding the length distribution of the rRNA structures, in the ITSON01 strain, the large subunit (LSU) varied from 3625 to 5239 bp, and the small subunit (SSU) varied from 2017 to 2022 bp. In the V039 strain, the LSU varied from 3487 to 3853 bp, and the SSU varied from 2010 to 2028 bp. Additionally, the length of 5S rRNA was 119 bp in both strains. Some examples of structures of such rRNA obtained with StructRNAfinder are presented below (Fig. 3).
    > The GO term annotation comparison revealed a similar profile for the 3 strains, except for some smaller gene families that represented less than 0.1% of the genes (Fig. 4).

### [19] Whole-Genome Analysis of Starmerella bacillaris CC-PT4 against MRSA, a Non-Saccharomyces Yeast Isolated from Grape
- Authors: Yong Shen, Xue Bai, Xiran Zhou, Jiaxi Wang, Na Guo et al.
- Year: 2022
- Venue: Journal of Fungi
- URL: https://www.semanticscholar.org/paper/a01fbbcc789c5485c2835438124908ecab8d568a
- DOI: 10.3390/jof8121255
- PMID: 36547588
- PMCID: 9784136
- Citations: 5
- Influential citations: 1
- Summary: The whole genome sequencing and analysis of S. bacillaris CC-PT4 in this study provide valuable information for understanding the biological characteristics and further development of this strain.
- Evidence snippets:
  - Snippet 1 (score: 0.746)
    > In this study, protein-coding genes were annotated using several databases. Among protein-coding genes, 4056 (97.73%) genes were annotated in the P450 database, followed by the NCBI nr database (3538, 5.25%), eggNOG database (3185, 76.45%), KEGG database (2610, 62.89%), Swiss-Prot database (3363, 81.04%), Go database annotations (2888, 69.59%), and TCDB database (670, 16.14%).
    > The NCBI nr database is a non-redundant protein database. The goal is to provide a comprehensive dataset representing complete sequence information of any species [37]. Annotation results of this database contain species information. In this study, the species information of 3538 genes annotated by S. bacillaris CC-PT4 in NCBI nr was counted, and the top 25 species involved 3074 genes (Figure 2). However, ten genes whose sequence identity was not less than 97% among the annotated genes belong to the genus Starmerella, and nine genes are S. bacillaris, of which four genes had 100% sequence identity (Table 1). Note: Hit_species, the species corresponding to the annotated gene.
    > Further, eggNOG was used to annotate the function of S. bacillaris CC-PT4 annotated protein, and cluster analysis was carried out. The classification results of 3185 genes annotated by eggNOG on S. bacillaris CC-PT4 were shown in Figure 3. There were 499 genes with no clear function, which may be related to the lack of research on S. bacillaris and the lack of reference genes. The most abundant annotated genes with clear functional classification were translation, ribosomal structure, and biogenesis (321 genes); and genes related to carbohydrate transport and metabolism, lipid transport and metabolism, and amino acid transport and metabolism are 146, 108, 145, respectively. However, the information annotated by extracellular structures and nuclear structures was less (four genes).

### [20] The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function
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
  - Snippet 1 (score: 0.743)
    > There are several knowledge bases that represent the collected knowledge of the E. coli K-12 MG1655 genome: EcoCyc (11), EcoGene (12), UniProt (13) and RefSeq (14). Other useful knowledge bases cater to specific classes of gene products, such as the RegulonDB, which contains manually curated functional information about transcription factors in E. coli (15). Our initial review of these knowledge bases yielded conflicting information on gene function and level of annotation for many E. coli genes. Any attempt to systematically assess the function of unannotated genes must therefore draw from multiple knowledge bases and resolve these conflicts.
    > Many research groups have categorized E. coli genes and proteins by annotation quality as a part of their studies. In 2009, Hu et (16). First, they identified all unannotated proteins in the K-12 W3110 and MG1655 genomes. In order for a protein-encoding gene to be considered functionally uncharacterized in their analysis, it had to meet the following criteria: (i) The gene name begins with 'y', (ii) the gene does not have a known pathway within EcoCyc and (iii) the gene does not have a functional description in Gen-ProtEC (17) (any gene with a description containing the words 'predicted', 'hypothetical', or 'conserved'). Based on these criteria, it was determined that 1431 of 4225 protein coding sequences were not functionally annotated. In 2015, Kim et al. published a database called EcoliNet that curated and predicted cofunctional gene networks for every protein coding gene in the E. coli genome (18). This study also quantified the number of uncharacterized protein coding genes in E. coli. To assess functional annotation, they used the presence of experimentally supported 'biological process' annotations in the Gene Ontology database (19). They concluded that ∼2000 protein coding genes in E. coli were not functionally annotated. The most comprehensive effort to assess the level of annotation in bacterial genomes has been Computational Bridges to Experiments (COM-BREX) (20,21).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Elif Diken, T. Ozer, M. Arıkan, Z. Emrence, E. Oner et al. (2015). Genomic analysis reveals the biotechnological and industrial potential of levan producing halophilic extremophile, Halomonas smyrnensis AAD6T. SpringerPlus. https://www.semanticscholar.org/paper/b5e5ea11a592b4a5d4494e455c197add1a6ec2c2
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. Jochen T. Bick, Shuqin Zeng, M. Robinson, S. Ulbrich, S. Bauersachs (2019). Mammalian Annotation Database for improved annotation and functional classification of Omics datasets from less well-annotated organisms. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/e0716471510abb041c775418ffa9cea283a8c47c
4. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
5. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
6. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
7. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
8. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
9. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
10. Bae Young Choi, Jaewook Kim, Hyeonseon Park, Jincheol Kim, Seahee Han et al. (2024). De Novo Genome Assembly and Phylogenetic Analysis of Cirsium nipponicum. Genes. https://www.semanticscholar.org/paper/658e8e30fac9b7c176a0e8e3f095d9f58b9c93a0
11. G. Alama-Bermejo, E. Meyer, S. Atkinson, A. Holzer, Monika M. Wiśniewska et al. (2020). Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids. Genome Biology and Evolution. https://www.semanticscholar.org/paper/7d5e64908d9bea80accb9389be84679778625620
12. A. A. Aserse, T. Woyke, N. Kyrpides, W. Whitman, K. Lindström (2017). Draft genome sequence of type strain HBR26T and description of Rhizobium aethiopicum sp. nov.. Standards in Genomic Sciences. https://www.semanticscholar.org/paper/e1bdbb37e1c501cbf7bf61678c972e140a80414f
13. Xiao-Yan Wang, Tianhua He, S. Gen, Xiao-qi Zhang, Xiao Wang et al. (2020). Soil properties and agricultural practices shape microbial communities in flooded and rainfed croplands. Applied Soil Ecology. https://www.semanticscholar.org/paper/39af2f84e27304c066c8a0da558194415f64dde5
14. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
15. Cosmin Saveanu, M. Fromont‐Racine, A. Harington, Florence Ricard, A. Namane et al. (2001). Identification of 12 New Yeast Mitochondrial Ribosomal Proteins Including 6 That Have No Prokaryotic Homologues*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/19c21c6d297e524358a1809bfb53fc458763c293
16. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
17. E. Swart, J. Bracht, V. Magrini, P. Minx, Xiao Chen et al. (2013). The Oxytricha trifallax Macronuclear Genome: A Complex Eukaryotic Genome with 16,000 Tiny Chromosomes. PLoS Biology. https://www.semanticscholar.org/paper/757a5557a078925a0e54425d7e2f0dc265f1e92f
18. Alejandro Otero-Ruiz, L. Z. Rodriguez-Anaya, F. Lares-Villa, Luis Fernando Lozano Aguirre Beltrán, L. F. Lares-Jiménez et al. (2023). Functional annotation and comparative genomics analysis of Balamuthia mandrillaris reveals potential virulence-related genes. Scientific Reports. https://www.semanticscholar.org/paper/2507f970e1c26a4be9a4aa77a62f685f36095593
19. Yong Shen, Xue Bai, Xiran Zhou, Jiaxi Wang, Na Guo et al. (2022). Whole-Genome Analysis of Starmerella bacillaris CC-PT4 against MRSA, a Non-Saccharomyces Yeast Isolated from Grape. Journal of Fungi. https://www.semanticscholar.org/paper/a01fbbcc789c5485c2835438124908ecab8d568a
20. S. Ghatak, Zachary A. King, Anand V. Sastry, B. Palsson (2019). The y-ome defines the 35% of Escherichia coli genes that lack experimental evidence of function. Nucleic Acids Research. https://www.semanticscholar.org/paper/c0336e0a70554304893a9e2d010ee30bd6872b10