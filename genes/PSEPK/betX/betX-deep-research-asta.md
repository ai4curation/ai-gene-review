---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T15:51:11.297718'
end_time: '2026-07-08T15:51:16.610791'
duration_seconds: 5.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: betX
  gene_symbol: betX
  uniprot_accession: Q88M34
  protein_description: 'SubName: Full=Choline / betaine / carnitine ABC transporter-substrate
    binding protein BetX {ECO:0000313|EMBL:AAN67361.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN67361.1};'
  gene_info: Name=betX {ECO:0000313|EMBL:AAN67361.1}; OrderedLocusNames=PP_1741 {ECO:0000313|EMBL:AAN67361.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ABC_Gly_betaine_transp_sub-bd. (IPR007210); OpuAC (PF04069)
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
- **UniProt Accession:** Q88M34
- **Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX {ECO:0000313|EMBL:AAN67361.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN67361.1};
- **Gene Information:** Name=betX {ECO:0000313|EMBL:AAN67361.1}; OrderedLocusNames=PP_1741 {ECO:0000313|EMBL:AAN67361.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ABC_Gly_betaine_transp_sub-bd. (IPR007210); OpuAC (PF04069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "betX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'betX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **betX** (gene ID: betX, UniProt: Q88M34) in PSEPK.

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
- Snippets retrieved: 19

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
  - Snippet 1 (score: 0.750)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.745)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.675)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

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
  - Snippet 1 (score: 0.730)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] Identifying orthologs with OMA: A primer
- Authors: Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover
- Year: 2020
- Venue: F1000Research
- URL: https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
- DOI: 10.12688/f1000research.21508.1
- PMID: 32089838
- PMCID: 7014581
- Citations: 41
- Summary: This Primer is organized in two parts and provides all the necessary background information to understand the concepts of orthology, how to infer them and the different subtypes of Orthology in OMA, as well as what types of analyses they should be used for.
- Evidence snippets:
  - Snippet 1 (score: 0.721)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [5] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.720)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [6] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.717)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [7] Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype
- Authors: J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al.
- Year: 2022
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
- DOI: 10.1371/journal.pone.0273184
- PMID: 36256644
- PMCID: 9578583
- Citations: 4
- Influential citations: 1
- Summary: Background Ruminant livestock are a major contributor to Australian agricultural sector carbon emissions. Variation in methane (CH4) produced from enteric microbial fermentation of feed in the reticulo-rumen of sheep differs with different digestive functions. Method We isolated rumen epithelium enzymatically to extract membrane and cytosol proteins from sheep with high (H) and low (L) CH4 emission. Protein abundance was quantified using SWATH-mass spectrometry. Results The research found dif...
- Evidence snippets:
  - Snippet 1 (score: 0.708)
    > Protein identifications with 2 peptides and a confident protein score (P <0.05) from the HpH fractionation and IDA-MS were used to assign subcellular localization. Using the top score given by WoLF PSORT [10] (www.genscript.com/wolf-psort.html) proteins were categorized into 8 locations. Membrane proteins were predicted using transmembrane helical Markov model (TMHMM) [11] (www.cbs.dtu.dk/services/TMHMM/). Proteins in the solute carrier protein (SLC) and ATP-binding cassette (ABC) transporter families were identified according to gene and protein name. We also used website gene names (www.genenames.org/data) to characterise the subcellular location of the transporter and the type of substrate they transport.
    > For proteins annotated as 'uncharacterised' in figures and tables in the manuscript a BLAST protein homology search was carried out using the Ensembl or uniport accession code in uniprotKB (www.uniprot.org). The accession code page contains the sequence and a link to BLAST. BLASTp results against uniprotkb_Swissprot reference proteomes and an identity sequence match of >95.5% to human, bovine (cattle) or caprine (goat) proteome annotation was accepted as the protein name.

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
  - Snippet 1 (score: 0.693)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [9] The ATP-binding cassette transporter Cbc (choline/betaine/carnitine) recruits multiple substrate-binding proteins with strong specificity for distinct quaternary ammonium compounds
- Authors: Chiliang Chen, Adel Malek, M. Wargo, Deborah A. Hogan, Gwyn A. Beattie
- Year: 2009
- Venue: Molecular microbiology
- URL: https://www.semanticscholar.org/paper/805aa43cc4c49264c16b54fda841cc11496bba95
- DOI: 10.1111/j.1365-2958.2009.06962.x
- PMID: 19919675
- PMCID: 5503199
- Citations: 93
- Influential citations: 9
- Summary: These studies demonstrate not only that the Cbc transporter serves as a useful model for exploring ABC transporter component interactions, but also that the orphan SBP genes common to bacterial genomes can encode functional SBPs.
- Evidence snippets:
  - Snippet 1 (score: 0.692)
    > We identified a choline, betaine and carnitine transporter, designated Cbc, from Pseudomonas syringae and Pseudomonas aeruginosa that is unusual among members of the ATP‐binding cassette (ABC) transporter family in its use of multiple periplasmic substrate‐binding proteins (SBPs) that are highly specific for their substrates. The SBP encoded by the cbcXWV operon, CbcX, binds choline with a high affinity (Km, 2.6 μM) and, although it also binds betaine (Km, 24.2 μM), CbcXWV‐mediated betaine uptake did not occur in the presence of choline. The CbcX orthologue ChoX from Sinorhizobium meliloti was similar to CbcX in these binding properties. The core transporter CbcWV also interacts with the carnitine‐specific SBP CaiX (Km, 24 μM) and the betaine‐specific SBP BetX (Km, 0.6 μM). Unlike most ABC transporter loci, caiX, betX and cbcXWV are separated in the genome. CaiX‐mediated carnitine uptake was reduced by CbcX and BetX only when they were bound by their individual ligands, providing the first in vivo evidence for a higher affinity for ligand‐bound than ligand‐free SBPs by an ABC transporter. These studies demonstrate not only that the Cbc transporter serves as a useful model for exploring ABC transporter component interactions, but also that the orphan SBP genes common to bacterial genomes can encode functional SBPs.

### [10] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
- Authors: Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al.
- Year: 2020
- Venue: Evidence-based Complementary and Alternative Medicine : eCAM
- URL: https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
- DOI: 10.1155/2020/8508491
- PMID: 32802136
- PMCID: 7403930
- Citations: 8
- Summary: The study found that flavonoids (quercetin, luteolin, and kaempferol) and beta-sitosterol and the top eight candidate targets, namely, PTGS2, PPARG, DPP4, GSK3B, CCNA2, AR, MAPK14, and ESR1, were selected as the main therapeutic targets of EGb.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [11] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
- Authors: Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al.
- Year: 2024
- Venue: Current biology : CB
- URL: https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
- DOI: 10.1016/j.cub.2024.02.040
- PMID: 38460514
- PMCID: 11066936
- Citations: 18
- Summary: It is found that evolution in response to extreme feast/famine is characterized by narrow adaptive trajectories with high mutational parallelism and notable mutational order, which demonstrate how microbes can navigate the adaptive landscapes of regularly fluctuating conditions and ultimately follow mutational trajectories that confer benefits across diverse environments.
- Evidence snippets:
  - Snippet 1 (score: 0.681)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [12] Genome-scale Model Constrained by Proteomics Reveals Metabolic Rearrangements in the Heterologous Host Streptomyces coelicolor
- Authors: Snorre Sulheim, T. Kumelj, Dino van Dissel, Ali Salehzadeh-Yazdi, Chao Du et al.
- Year: 2019
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/bee47d74917a677c792ed89d3d0d6496b790d5fb
- DOI: 10.1101/796722
- Citations: 1
- Summary: This study provides the first systems description of S. coelicolor M1152, an engineered heterologous expression host widely used for the production and discovery of natural products, and reconstructed the consensus model Sco-GEM in an open-science framework.
- Evidence snippets:
  - Snippet 1 (score: 0.680)
    > Gene annotations, substrate and transport class information were mostly extracted from Transport DB 2.0 (116) and TCDB (117). Then, transport proteins were extracted from IUBMB-approved Transporter Classification (TC) System and categorized into 9 main classes (Figure 1F): 1) ABC transporter; 2) PTS transporter; 3) Proton symporter; 4) Sodium symporter; 5) Other symporter; 6) Proton antiport; 7) Other antiport; 8) Facilitated diffusion; 9) Simple diffusion. For those transport proteins with an ambiguous substrate annotation in TCDB, the specific substrate annotation was obtain by extracting annotations from KEGG (51,52), UniProt (57) or through BLAST homology search (118) using a similarity threshold of 90% (see Supplemental Information 2 and Table S4 for details).

### [13] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.680)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [14] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.673)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [15] Overexpression of Scr1 protein induces strong changes in the transcriptome and metabolome of Streptomyces coelicolor that affect antibiotic production
- Authors: C. Riascos, Gemma Fernández-García, Javier García-Martín, Ángel Manteca, R. Santamaría et al.
- Year: 2025
- Venue: Microbial Cell Factories
- URL: https://www.semanticscholar.org/paper/1459f4ce98f53d7b31337731f37caa2e8199a493
- DOI: 10.1186/s12934-025-02843-5
- PMID: 41077587
- PMCID: 12516864
- Summary: Xenobiotic response element (XRE) regulator proteins play an important role in gene regulation in Streptomyces. In these bacteria, they are often encoded together with a small protein containing a DUF397 domain. Previous work on 15 such pairs present in S. coelicolor has shown they act as pleiotropic regulators. They dependently affect antibiotic production and morphological differentiation on different culture media. Overexpression of the protein Scr1, which is encoded by gene SCO4441, induc...
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > In addition to the metabolic processes that were altered by Scr1 overexpression, the RNA-Seq assay also detected differential expression of several important genes involved in molecular transport and gene regulation, as detailed below.
    > ABC transporters: three types of ABC transporters were differentially expressed in the strain Sscr1: mineral and organic ion transporters; oligosaccharide, polyol and lipid transporters; and phosphate and amino acid transporters (Additional File 12). The expression pattern of these genes varied greatly from one type to another. For example, in the Sscr1 strain, genes for three molybdate transport-associated proteins (SCO3704, SCO3705, and SCO3706) were overexpressed only at 36 h. The same occurred for the betaine transporter (SCO4831), an osmoprotectant; except in this case, the gene for the substrate-binding protein (SCO2933) was not differentially expressed. Additionally, the genes for the three proteins responsible for the multiple sugar transporter were under-expressed. Thus, the gene encoding a putative sugar-binding protein (SCO2404) was under-expressed at 36 h, while those genes encoding the permease protein (SCO2406) and the ATP-binding protein (SCO2405) were under-expressed at 48 h. In the case of adenosine and the genes of four proteins associated with transport, the first, a lipoprotein (SCO4884), was under-expressed at 36 h, while the genes for the other three proteins, two permease proteins (SCO4887 and SCO4888) and an ATP-binding protein (SCO4886), were overexpressed at 48 h. As for orthophosphate transport, the genes for the three proteins responsible for its transport (SCO6814, SCO6415, and SCO6416) were overexpressed at 36 and 48 h and showed high FC values.

### [16] Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea
- Authors: A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al.
- Year: 2023
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
- DOI: 10.3389/fmicb.2023.1066096
- PMID: 36876067
- PMCID: 9981795
- Citations: 2
- Summary: The present study concludes that deciphering the whole genome of F. udum would be instrumental in understanding evolution, virulence determinants, host-pathogen interaction, possible control strategies, ecological behavior, and many other complexities of the pathogen.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > The BLASTx homology search tool, a component of the standalone NCBI-blast-2.3.0+, was used to perform functional annotation of the F. udum genes (Altschul et al., 1990). With a cut-off E value of ≤1e−06 and a similarity of 34%, BLASTx identified the homologous sequences of the genes in the NCBI non-redundant protein database. Gene ontology (GO) analysis was carried out using Blast2GO PRO 4.1.5 (Conesa and Gotz, 2008). In three different mappings, B2G performed as follows: (1) Using two NCBI-provided mapping files, blast result accessions are used to get gene names (symbols; gene info, gene 2 accessions). (2) Blast result GI identifiers were used to retrieve UniProt IDs using a mapping file from PIR (non-redundant reference protein database), which includes PSD, Swiss-Prot, UniProt, TrEMBL, GenPept, RefSeq, and PDB. The names of the identified genes were searched in the species-specific entries of the gene product table of the GO database. With the aid of the KAAS-KEGG Automatic Annotation Server, pathway analyses were carried out. This database provides functional annotation of genes using other data servers (Moriya et al., 2007). Accessions from the blast results were looked for in the DBXRef table of the GO database.

### [17] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.669)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [18] The GbsR Family of Transcriptional Regulators: Functional Characterization of the OpuAR Repressor
- Authors: Stefanie Ronzheimer, Bianca Warmbold, C. Arnhold, E. Bremer
- Year: 2018
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/870efb61fecea60dee006daba32938f63e0197f6
- DOI: 10.3389/fmicb.2018.02536
- PMID: 30405586
- PMCID: 6207618
- Citations: 7
- Summary: GbsR-/OpuAR-type proteins are characterized as an extended sub-group within the MarR-superfamily of transcriptional regulators and a novel type of substrate-inducible import system for osmostress protectants is identified.
- Evidence snippets:
  - Snippet 1 (score: 0.668)
    > A GbsB-like choline dehydrogenase (blue) (Boch et al., 1996) is encoded in the gene clusters of all members belonging to the genus Bacillus. Glycine betaine synthesis gene clusters of members of the genus Staphylococcus (Rosenstein et al., 1999) harbor a choline dehydrogenase, which is related to the BetA enzyme from Escherichia coli (gold) (Lamark et al., 1991). Genes encoding transport systems are depicted and color-coded according to the superfamily they belong to. gbsU-type genes (yellow) encode proteins with similarity to substrate binding proteins from ABC transporters (Scheepers et al., 2016), cudT-like genes (pink) encode a transporter of the betaine-choline-carnitine-transporter (BCCT) family (Ziegler et al., 2010), and genes for transporters of the sodium-solute-symporter (SSS) family (Bracher et al., 2016) are marked in green. In H. halophilus DSM 2266 (Burkhardt et al., 2009), the choline dehydrogenase gene has been labeled according to the nomenclature of the gbsAB gene cluster of B. subtilis (Boch et al., 1996); however, this gene actually encodes a BetA-type enzyme (Lamark et al., 1991). (B) Genetic organization of opuA gene clusters and sub-unit composition of the encoded OpuA-type ABC transporters. A total number of 18 genes for GbsR-like regulatory proteins (OpuAR) were identified, which are encoded in the immediate vicinity of gene clusters encoding an OpuA-type transporter (Kempf and Bremer, 1995;Obis et al., 1999;Wolters et al., 2010). Representative genetic arrangements of opuA gene loci are shown, and the sub-unit composition of the encoded OpuA-type ABC transporters is depicted.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
5. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
6. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
7. J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al. (2022). Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype. PLoS ONE. https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
8. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
9. Chiliang Chen, Adel Malek, M. Wargo, Deborah A. Hogan, Gwyn A. Beattie (2009). The ATP-binding cassette transporter Cbc (choline/betaine/carnitine) recruits multiple substrate-binding proteins with strong specificity for distinct quaternary ammonium compounds. Molecular microbiology. https://www.semanticscholar.org/paper/805aa43cc4c49264c16b54fda841cc11496bba95
10. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
11. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
12. Snorre Sulheim, T. Kumelj, Dino van Dissel, Ali Salehzadeh-Yazdi, Chao Du et al. (2019). Genome-scale Model Constrained by Proteomics Reveals Metabolic Rearrangements in the Heterologous Host Streptomyces coelicolor. bioRxiv. https://www.semanticscholar.org/paper/bee47d74917a677c792ed89d3d0d6496b790d5fb
13. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
14. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
15. C. Riascos, Gemma Fernández-García, Javier García-Martín, Ángel Manteca, R. Santamaría et al. (2025). Overexpression of Scr1 protein induces strong changes in the transcriptome and metabolome of Streptomyces coelicolor that affect antibiotic production. Microbial Cell Factories. https://www.semanticscholar.org/paper/1459f4ce98f53d7b31337731f37caa2e8199a493
16. A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al. (2023). Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea. Frontiers in Microbiology. https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
17. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
18. Stefanie Ronzheimer, Bianca Warmbold, C. Arnhold, E. Bremer (2018). The GbsR Family of Transcriptional Regulators: Functional Characterization of the OpuAR Repressor. Frontiers in Microbiology. https://www.semanticscholar.org/paper/870efb61fecea60dee006daba32938f63e0197f6