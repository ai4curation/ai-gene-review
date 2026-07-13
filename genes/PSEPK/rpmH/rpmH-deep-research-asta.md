---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T09:23:56.968629'
end_time: '2026-07-09T09:24:04.489638'
duration_seconds: 7.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rpmH
  gene_symbol: rpmH
  uniprot_accession: P0A161
  protein_description: 'RecName: Full=Large ribosomal subunit protein bL34 {ECO:0000305};
    AltName: Full=50S ribosomal protein L34;'
  gene_info: Name=rpmH; OrderedLocusNames=PP_0009;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial ribosomal protein bL34 family.
  protein_domains: Ribosomal_bL34. (IPR000271); Ribosomal_bL34_CS. (IPR020939); Ribosomal_L34
    (PF00468)
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
- **UniProt Accession:** P0A161
- **Protein Description:** RecName: Full=Large ribosomal subunit protein bL34 {ECO:0000305}; AltName: Full=50S ribosomal protein L34;
- **Gene Information:** Name=rpmH; OrderedLocusNames=PP_0009;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial ribosomal protein bL34 family.
- **Key Domains:** Ribosomal_bL34. (IPR000271); Ribosomal_bL34_CS. (IPR020939); Ribosomal_L34 (PF00468)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rpmH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rpmH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rpmH** (gene ID: rpmH, UniProt: P0A161) in PSEPK.

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

### [1] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.866)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [2] Genomic analysis reveals the biotechnological and industrial potential of levan producing halophilic extremophile, Halomonas smyrnensis AAD6T
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
  - Snippet 1 (score: 0.855)
    > Gene prediction and genome annotation were carried out using the RAST auto-annotation server (Aziz et al. 2008). Protein-encoding and transfer RNA genes were predicted by RAST server, while the ribosomal RNA genes were identified with RNAmmer (v1.2) (Lagesen et al. 2007). The gene predictions of essential biosystems were manually verified using BLAST searches against protein databases, the Universal Protein Resource (UniProt) (http:// www.uniprot.org/) and National Center for Biotechnology Information (NCBI) (http://www.ncbi.nlm.nih.gov/). The gene functions and classifications were based on the subsystem annotation of the RAST server. Information on enzyme-encoding genes was taken from Kyoto Encyclopedia of Genes and Genomes (KEGG) (Kanehisa et al. 2012) and ExPaSy databases (Artimo et al. 2012). Transport protein coding genes were annotated using the similarity searches against the Transfer Classification Database (TCDB) (Saier et al. 2009).

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
  - Snippet 1 (score: 0.852)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.851)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).
  - Snippet 2 (score: 0.776)
    > (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b). Under normal-growth conditions, the most enriched cluster (enrichment score 11.4) comprised genes related to ribonucleoproteins, ribosomes, ribosomal proteins, and translation. The second-most enriched cluster (enrichment score 3.8) comprised genes belonging to protein biosynthesis and tRNA metabolism, including aminoacyl-tRNA synthetases. A third cluster (enrichment score 2.2) comprised genes related to nucleotide-binding proteins. Among the genes with peaks under cold-shock conditions, the same three annotation clusters were identified, with enrichment scores 6.5, 4.1, and 2.5, respectively.
    > We also analyzed the genes identified under both normal-growth and cold-shock conditions, only under normal-growth conditions, or only under cold-shock conditions. (Supplemental Table 4c-e). The same three annotation clusters (ribosome and translation, tRNA metabolism, and nucleotide binding, enrichment scores 6.4, 3.8, and 2.7, respectively) were reported for genes that contained peaks under both normal-growth and cold-shock conditions. Genes with peaks only under normal-growth conditions were enriched for genes related to ribosomes and translation, genes with peaks only under cold-shock conditions showed no specific enrichment. Genes that neither contained a peak under normal-growth nor under coldshock conditions also showed no significant enrichment of a particular family of proteins (Supplemental Table 4f).
    > As an example for genes related to annotation cluster 1, 18 out of the 22 genes (82%) for proteins of the 30S ribosomal subunit were identified under normal-growth conditions, 12 (55%) after cold shock (11 common genes, three without peaks). For the proteins of the 50S ribosomal subunit, the picture was similar: Out of 34 genes, 31 (91%) were identified under normal-growth, 22 (65%) under coldshock conditions (20 common genes, one without peaks).

### [5] Mammalian Annotation Database for improved annotation and functional classification of Omics datasets from less well-annotated organisms
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
  - Snippet 1 (score: 0.848)
    > In transcriptomics and proteomics studies, one important step of data analysis is the functional annotation of obtained lists of differentially expressed genes (DEGs) or proteins (DEPs). With the increase in the number of organisms with sequenced and annotated genomes, such studies have been performed in many different species. However, the information about gene and protein functions, on which the annotation is based, is mainly derived from a limited number of model organisms or well-annotated species, such as mouse, humans and rat representing mammalian species or even from bacteria, yeast, worms or Drosophila. Based on the assumption that orthologous genes carry out identical or biologically equivalent functions in different organisms, functional annotation is transferred from wellstudied organisms to less well-annotated species (1). Whereas orthologous genes usually have maintained the same function during evolution (2) paralogous genes originated from gene duplication events and often evolved different functions (3,4). Orthologous genes usually have the same gene symbol and name for almost all corresponding species (5, 6). However, depending on the status of the gene annotation of a species, not all annotated genes have an official gene symbol (only locus number, e.g. LOC100152218 60S ribosomal protein L23a-like) and/or are assigned to functional annotation databases like their corresponding orthologs in the well-annotated model organisms. This leads to a substantial loss of information if the gene identifiers (IDs) of the respective species are used for functional annotation. To avoid this data loss and improve the results of functional annotation, one strategy is to transfer information from homologous genes (orthologs and paralogs) of well-annotated species (6).
    > In many situations with non-model species such as livestock species, experimentalists avoid the additional work to assign human ortholog genes for functional annotation analysis and are not aware of the information loss.

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
  - Snippet 1 (score: 0.837)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [7] Toward Spectral Library-Free Matrix-Assisted Laser Desorption/Ionization Time-of-Flight Mass Spectrometry Bacterial Identification
- Authors: Ding Cheng, Liang Qiao, P. Horvatovich
- Year: 2018
- Venue: Journal of Proteome Research
- URL: https://www.semanticscholar.org/paper/49e3162fb738e88a6c6816c88e0855e645c1d43a
- DOI: 10.1021/acs.jproteome.8b00065
- PMID: 29749232
- PMCID: 5989274
- Citations: 21
- Summary: A strategy for bacterial typing by MALDI-TOF using protein sequences from public database, that is, UniProt, so that bacteria can be identified at the genus level by searching against a database containing the protein sequences of 42 genera of bacteria from UniProt.
- Evidence snippets:
  - Snippet 1 (score: 0.812)
    > This work employed a double cross-validation 24 method to obtain the optimal gene weight table W for spectral matching. In the model, the outer test group was independent from the data used in the inner loop for the optimization of parameters, and therefore overfitting of model parameters can be avoided when assessing the statistical validity of the library-free MALDI-TOF bacterial identification. 25 Ten genes were identified as the most informative genes to annotate peaks on MALDI-TOF spectra for bacterial identification (Figure S1 in section S3 of the Supporting Information). The 10 genes together with their gene weights are shown on Figure 3. The obtained genes corresponded to ribosomal subunit proteins and DNA-binding proteins. Ribosomal proteins in conjunction with rRNA form the ribosomal subunits and are involved in protein translation. 26 DNA-binding proteins are responsible for binding to DNA regions essential for DNA replication, recombination, and repair. 27 Ribosomal proteins are highly abundant in bacteria. By statistics, 28 the weight of ribosomal proteins accounts for onefifth of the total weight of all proteins in a bacterial cell. Figure 3 shows that three genes, rpmC, rpmJ, and rpmH, have relative much higher gene weights compared to the other genes, which correspond to 50S ribosomal protein L34, 50S ribosomal protein L36, and 50S ribosomal protein L29, respectively. The expression levels of the three proteins in microorganism are high and their molecular weights are ranging from 4000 to 8000 Da. Mass spectra of bacteria by MALDI-TOF MS normally show strongest peaks within the mass range of 2000 to 20000 Da. 14 The ribosomal proteins are conserved proteins but specific to bacteria at genera level, which make them as potential markers for bacterial identification. By only considering ribosomal protein sequences for spectral matching, we have obtained another gene weight table as shown in the S6 part of Supporting Information. The top eight genes are the same as the ones in Figure 3 and with similar gene weights.
    > A previous study on bacterial identification by MALDI-TOF also supports the results in Figure 3. 29 Arnold and Reilly characterized the proteins isolated from Escherichia coli ribosomes by MALDI-TOF.

### [8] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.811)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [9] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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

### [10] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.784)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [11] Functional annotation of parasitic worm genomes, by assigning protein names and GO terms
- Authors: Avril Coghlan, M. Berriman
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
- DOI: 10.1038/protex.2018.055
- Citations: 1
- Summary: A computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and Go terms from orthologues in other species.
- Evidence snippets:
  - Snippet 1 (score: 0.772)
    > Given a set of predicted protein-coding genes for a newly sequenced genome, functional annotation involves assigning putative functions to the predicted genes. Two ways in which this can be done are assigning protein names and Gene Ontology (GO;Gene Ontology Consortium, 2010) terms to the predicted proteins. Here we describe a computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and GO terms from orthologues in other species.
    > When assigning protein names, UniProt protein naming rules (www.uniprot.org/docs/nameprot) are followed where possible. This recommends that a good and stable name for a protein is "as neutral as possible"; that a protein name "should be, as far as possible, unique and attributed to all orthologs"; and a protein name "should not contain a specific characteristic of the protein, and in particular it should not reflect the function or role of the protein, nor its subcellular location, its domain structure, its tissue specificity, its molecular weight or its species of origin".
    > In our protocol, a protein name is assigned to each predicted protein based on curated names in UniProt (Bairoch & Apweiler, 2000) for human, zebrafish, Drosophila melanogaster, Caenorhabditis elegans, and Schistosoma mansoni orthologues identified from a database of gene families (e.g. built using Ensembl Compara; Vilella et al. 2009), or (if no information is found from orthologues) based on InterPro (Hunter et al. 2012) domains. Figure 1 shows an example of using our protein naming pipeline for four Strongyloides ratti genes that belong to the tubulin polyglutamylase family (underlined in pink), where four different protein names were assigned to them (in pink), based on names of their C. elegans or human orthologues.
    > Since each of the S. ratti genes belonged to a different subfamily of the tubulin polyglutamylase family, they were assigned different names.

### [12] Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids
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
  - Snippet 1 (score: 0.767)
    > We chose cell migration genes and proteases/inhibitors as candidate virulence factors, due to their relevance in hostpathogen interactions (e.g., Barragan and Sibley 2002;McKerrow et al. 2006;Bouzid et al. 2013). Given the low amount of functional (GO) annotation in our largest assembly, C. shasta þ NHP (see Results), we used BlastX to search for homologs of genes of interest in two custom concatenated databases that comprised the Cell Migration Knowledge Database (CMKB) which includes proteins, families, and complexes involved in cell migration (http://www.cellmigration. org/index.shtml, last accessed February 5, 2015; $7,600 protein sequences), and the MEROPS database, which consists of a nr library of full-length sequences of peptidases and peptidase inhibitors (http://merops.sanger.ac.uk/, last accessed December 2, 2014; $450,000 sequences; Rawlings et al. 2016). We searched using the longest representatives for each gene in the C. shasta þ NHP assembly (23,418 contigs; IIR-RBT6) then parsed matches (bit score > 100) and posteriorly classified homologs to proteases or motility genes matching the specific databases. We then selected only genes with the same annotation in UniProt (determined using the same standards: no ambiguous terms filtering, bit score > 100) to confirm gene identity. Due to disagreements between annotations (CMKB vs. UniProt, and MEROPS vs. UniProt), we curated gene lists manually, removing genes that matched one or more of the following criteria: 1) no genetic distances available (only available for reference); 2) disagreements between annotations from the different databases, after checking for synonyms or function similarity; 3) annotations that contained terms from UniProt "Uncharacterized protein" and "Predicted protein" (ambiguous terms), and whose identity could not be confirmed; and 4) annotations that contained nonspecific terms, such as "heat shock protein" or "ribosomal protein."

### [13] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
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
  - Snippet 1 (score: 0.767)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [14] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.765)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [15] The Minimal Translation Machinery: What We Can Learn From Naturally and Experimentally Reduced Genomes
- Authors: M. Garzón, Mariana Reyes-Prieto, Rosario Gil
- Year: 2022
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/8e30f413bf85f58bdedf24759a335f788b08459e
- DOI: 10.3389/fmicb.2022.858983
- PMID: 35479634
- PMCID: 9035817
- Citations: 6
- Summary: This proposed minimal translational machinery is composed by 142 genes which must be present in any synthetic prokaryotic cell designed for biotechnological purposes, 76.8% of which are shared with JCVI-syn3.0.
- Evidence snippets:
  - Snippet 1 (score: 0.753)
    > Before determining our universe of translational genes, we had to cope with the existence of poorly or wrongly annotated genes and pseudogenes within the analyzed genomes. In fact, a critical difficulty in carrying out this work has been the automation of the process because, even though great efforts are being made to unify the nomenclature (as defined by the International Nucleotide Sequence Database Collaboration, INSDC; Brunak et al., 2002), at present no database provides the unified names for all genes. Most gene descriptions are still based on their initial identification by classical genetics in each given organism, and a recent discovery of their function is often associated to errors, such as entering a function twice without unified descriptors or simply by not including it in databases. For this work, the UniProt nomenclature recommended by the INSDC has been used; in cases where there was no classification, the accepted nomenclature for in E. coli K-12 MG1655 (taxonomy ID 511145) was chosen (Schoch et al., 2020).
    > Once this problem was solved, we set up a universe of translational protein-coding genes, which is composed by the genes that encode the proteins that integrate the translation apparatus, as well as those that directly or indirectly participate in the different stages of rRNA or tRNA processing. This gene set was defined based on the genomes of the two selected model bacteria, E. coli K-12 MG1655 and B. subtilis 168. We detected a total of 309 unique genes (Supplementary Material 2). Most of them belong to the ribosomal proteins and tRNA modification categories, and only a few of them to RNA processing (Figure 2A).
    > Then, we compared the previously defined pangenome to the universe of translational genes, to search for the 309 genes involved in translation. As expected, the genome reduction process affects the total number of genes for this function, and the losses depend on the translational subprocess involved (Figure 2B). Most ribosomal proteins are present in all organisms regardless of their lifestyle, confirming the importance of the whole ribosome as a functional unit. In contrast, many genes of the other translational categories have been lost, especially in OS and, to a lesser extent, in SS, certainly affected by the genome reduction syndrome.

### [16] Soil properties and agricultural practices shape microbial communities in flooded and rainfed croplands
- Authors: Xiao-Yan Wang, Tianhua He, S. Gen, Xiao-qi Zhang, Xiao Wang et al.
- Year: 2020
- Venue: Applied Soil Ecology
- URL: https://www.semanticscholar.org/paper/39af2f84e27304c066c8a0da558194415f64dde5
- DOI: 10.1016/j.apsoil.2019.103449
- Citations: 34
- Summary: Abstract Understanding the dynamics of soil microbial communities and the factors that affect those dynamics is crucial for comprehending the processes affecting soil fertility in agricultural ecosystems. Here, we used shotgun DNA sequencing to characterise 29 soil microbial communities in flooded paddies in China's Yangtze River Basin, and comparatively analysed the composition and function of microbial communities with 132 communities from North and South America's rainfed cropland. We hypo...
- Evidence snippets:
  - Snippet 1 (score: 0.753)
    > To do so, sequence similarity was searched against several databases simultaneously--KEGG (Kyoto Encyclopedia of Genes and Genomes), NCBI (National Center for Biotechnology Information), RDP (Ribosomal Database Project), SEED (The SEED Project, Overbeek et al., 2005), UniProt (UniProt Knowledgebase), and eggNOG (evolutionary genealogy of genes Non-supervised Orthologous Groups) (Meyer et al., 2008). Genes were assigned to a subsystem by homology searches of protein sequences encoded by the reads. For both taxonomic assignment and function annotation, the match threshold was set at an expected value of < 1 × 10 −5 , similarity of > 50 bp, and a minimum identity of 65%. If no match was found in the relevant database, the sequence was classified as 'unclassified'. The taxonomic assignment and functional annotation results for each sample are deposited and retrievable from MG-RAST following the reference ID (Supplementary Table S1).

### [17] A Literature-Derived Knowledge Graph Augments the Interpretation of Single Cell RNA-seq Datasets
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
  - Snippet 1 (score: 0.753)
    > We obtained the full set of human protein-coding genes from HGNC [24] and curated potential gene synonyms from various sources including ENTREZ, UniProt, Ensembl, and Wikipedia. For specific gene families, we also manually added family-level synonyms which are not captured by synonyms curated at the single gene level. This included genes encoding the following proteins: T cell receptor subunits, immunoglobulin subunits, class II MHC molecules, hemoglobin subunits, surfactant proteins, chymotrypsinogen subunits, CD8 subunits (CD8A, CD8B), and CD3 subunits (CD3E, CD3G, CD3D, and CD247). The complete gene vocabulary is given in File S4.
    > For the cell type annotation algorithm described subsequently, we only considered protein-coding genes which were strongly associated with at least one cell type in the literature (local score ≥ 3; see description of local scores below). Further, we excluded mitochondrially encoded genes (gene names starting with "MT-"), genes encoding ribosomal proteins (gene names starting with "RPS", "RPL", "MRPS", or "MRPL"), and MHC class I genes except for HLA-G (HLA-A, HLA-B, HLA-C, HLA-E, HLA-F). These filtering steps yielded a final set of 5113 "eligible genes" for consideration during the cell type annotation steps (indicated in File S4).

### [18] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.751)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [19] Identification of 12 New Yeast Mitochondrial Ribosomal Proteins Including 6 That Have No Prokaryotic Homologues*
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
  - Snippet 1 (score: 0.751)
    > However, this name does not allow one to discriminate between small and large subunit proteins and thus may be misleading. For example, Mrp2 is not the homologue of the prokaryotic S2 ribosomal proteins but belongs to the S14p family. Accordingly, we preferred to designate the newly identified genes RSMxx genes, where RSM stands for ribosomal small subunit of mitochondria, and xx is the number of the corresponding prokaryotic protein family (see Table II). The genes that encode proteins that are not significantly similar to prokaryotic proteins were named with the same prefix RSM followed by a number that begins with 22, because there are 21 prokaryotic small ribosomal subunit protein families. Thus, the proposed name of the YKL155c gene is RSM22 (Table II). The matched peptide has the sequence VT-PGSLYK. The differences between the masses of the marked peaks correspond to the masses of amino acid residues Gly, Pro, and Thr. D, the fragmentation spectrum for the peptide that is found within residues 400 -408 in the predicted sequence of Ygl129c shows a very good signal-to-noise ratio. Fragmentation spectra that were generated for other peptides show a signal-to-noise ratio between the two extremes shown in C and D.
    > A large amount of functional data was generated in the course of genetic screenings and functional genomic studies in yeast. Hence, for a number of the identified proteins, some cellular or functional data were already available in public data bases. In addition, for some of the less well characterized proteins, we analyzed the cellular localization of the GFP C-terminally tagged proteins and the respiratory competency of strains disrupted for the corresponding genes. These data are summarized in Table II and described below.
    > Functional Data on the New Proteins That Belong to Known Ribosomal Protein Families-Ribosomal protein families S7p and S10p are represented in yeast mitochondria by the corresponding homologues Yjr113c and Ydr041w. Mammalian homologues of S7 (19) and S10 (20) were also recently described as components of the bovine small mitochondrial ribosomal subunit.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
2. Elif Diken, T. Ozer, M. Arıkan, Z. Emrence, E. Oner et al. (2015). Genomic analysis reveals the biotechnological and industrial potential of levan producing halophilic extremophile, Halomonas smyrnensis AAD6T. SpringerPlus. https://www.semanticscholar.org/paper/b5e5ea11a592b4a5d4494e455c197add1a6ec2c2
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
5. Jochen T. Bick, Shuqin Zeng, M. Robinson, S. Ulbrich, S. Bauersachs (2019). Mammalian Annotation Database for improved annotation and functional classification of Omics datasets from less well-annotated organisms. Database: The Journal of Biological Databases and Curation. https://www.semanticscholar.org/paper/e0716471510abb041c775418ffa9cea283a8c47c
6. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
7. Ding Cheng, Liang Qiao, P. Horvatovich (2018). Toward Spectral Library-Free Matrix-Assisted Laser Desorption/Ionization Time-of-Flight Mass Spectrometry Bacterial Identification. Journal of Proteome Research. https://www.semanticscholar.org/paper/49e3162fb738e88a6c6816c88e0855e645c1d43a
8. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
9. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
10. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
11. Avril Coghlan, M. Berriman (2018). Functional annotation of parasitic worm genomes, by assigning protein names and GO terms. https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
12. G. Alama-Bermejo, E. Meyer, S. Atkinson, A. Holzer, Monika M. Wiśniewska et al. (2020). Transcriptome-Wide Comparisons and Virulence Gene Polymorphisms of Host-Associated Genotypes of the Cnidarian Parasite Ceratonova shasta in Salmonids. Genome Biology and Evolution. https://www.semanticscholar.org/paper/7d5e64908d9bea80accb9389be84679778625620
13. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
14. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
15. M. Garzón, Mariana Reyes-Prieto, Rosario Gil (2022). The Minimal Translation Machinery: What We Can Learn From Naturally and Experimentally Reduced Genomes. Frontiers in Microbiology. https://www.semanticscholar.org/paper/8e30f413bf85f58bdedf24759a335f788b08459e
16. Xiao-Yan Wang, Tianhua He, S. Gen, Xiao-qi Zhang, Xiao Wang et al. (2020). Soil properties and agricultural practices shape microbial communities in flooded and rainfed croplands. Applied Soil Ecology. https://www.semanticscholar.org/paper/39af2f84e27304c066c8a0da558194415f64dde5
17. D. Doddahonnaiah, P. Lenehan, T. Hughes, D. Zemmour, E. Garcia-Rivera et al. (2021). A Literature-Derived Knowledge Graph Augments the Interpretation of Single Cell RNA-seq Datasets. Genes. https://www.semanticscholar.org/paper/f078685c8e996b4e80f3f872f296e1c14b17e01a
18. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
19. Cosmin Saveanu, M. Fromont‐Racine, A. Harington, Florence Ricard, A. Namane et al. (2001). Identification of 12 New Yeast Mitochondrial Ribosomal Proteins Including 6 That Have No Prokaryotic Homologues*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/19c21c6d297e524358a1809bfb53fc458763c293