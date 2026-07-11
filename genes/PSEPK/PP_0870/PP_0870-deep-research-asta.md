---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T14:07:32.737100'
end_time: '2026-07-08T14:07:38.592716'
duration_seconds: 5.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0870
  gene_symbol: PP_0870
  uniprot_accession: Q88PI0
  protein_description: 'SubName: Full=Glycine betaine/carnitine/choline ABC transporter,
    periplasmic binding protein {ECO:0000313|EMBL:AAN66495.1};'
  gene_info: OrderedLocusNames=PP_0870 {ECO:0000313|EMBL:AAN66495.1};
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
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88PI0
- **Protein Description:** SubName: Full=Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein {ECO:0000313|EMBL:AAN66495.1};
- **Gene Information:** OrderedLocusNames=PP_0870 {ECO:0000313|EMBL:AAN66495.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ABC_Gly_betaine_transp_sub-bd. (IPR007210); OpuAC (PF04069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0870" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0870' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0870** (gene ID: PP_0870, UniProt: Q88PI0) in PSEPK.

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

- Papers retrieved: 17
- Snippets retrieved: 18

## Relevant Papers

### [1] Genomic reconstruction of fossil and living microorganisms in ancient Siberian permafrost
- Authors: R. Liang, Zhou Li, Maggie C Y Lau Vetter, T. Vishnivetskaya, O. Zanina et al.
- Year: 2021
- Venue: Microbiome
- URL: https://www.semanticscholar.org/paper/6204b177c9d3defa17fd2344956d5d8940307f2d
- DOI: 10.1186/s40168-021-01057-2
- PMID: 34001281
- PMCID: 8130349
- Citations: 39
- Summary: The results indicated that coupling of DNA repair protocols with simultaneous sequencing of iDNA and eDNA fractions enabled the assembly of MAGs from past and living microorganisms in ancient permafrost, providing genomic insights into long-term survival mechanisms of microorganisms under cryogenic conditions through geological time.
- Evidence snippets:
  - Snippet 1 (score: 0.834)
    > Gene abbreviations: protein L-isoaspartyl/D-aspartyl o-methyltransferase (PIMT), methionine sulfoxide reductase (MsrA), uracil-DNA glycosylase (UDG), DNA mismatch repair protein (MutS), DNA replication and repair protein (RecF), cold shock protein (CspA), choline dehydrogenase (betA), betaine aldehyde dehydrogenase (betB), choline sulfatase (betC), glycine betaine/proline ABC transporter (ProV), glycine betaine/proline betaine transport system permease protein (ProW), Glycine betaine/carnitine transport binding protein (GbuC), osmoprotectant ABC transporter ATP-binding protein (OpuAA), glycine betaine transport system permease protein (OpuAB), glycine betaine-binding protein (OpuAC), osmoregulated proline transporter (OpuE), choline transport ATP-binding protein (OpuBA), choline transport system permease protein (OpuBB), carnitine transport ATP-binding protein (OpuCA), carnitine transport permease protein (OpuCB), carnitine transport binding protein (OpuCC), carnitine transport permease protein (OpuCD), ectoine/5-hydroxyectoine-binding periplasmic protein (UehA), osmoprotectant import ATP-binding proteins (osmV), and aquaporin (Aqp). The MAGs highlighted in blue represent the potentially living microbial populations inferred from DNA damage in both iDNA and eDNA fractions osmoprotective compounds such as choline, glycinebetaine, proline, carnitine, and ectoine (Fig. 6).
  - Snippet 2 (score: 0.789)
    > Many of the Firmicutes MAGs from the 5.8 m sample lack the biosynthetic pathway for glycine-betaine, but harbor various genes for osmoregulation and uptake of Fig. 6 Key functional genes involved in the repair of DNA and protein damage and survival under cold, osmotic, and oxidative stresses present (red) in MAGs. Gene abbreviations: protein L-isoaspartyl/D-aspartyl o-methyltransferase (PIMT), methionine sulfoxide reductase (MsrA), uracil-DNA glycosylase (UDG), DNA mismatch repair protein (MutS), DNA replication and repair protein (RecF), cold shock protein (CspA), choline dehydrogenase (betA), betaine aldehyde dehydrogenase (betB), choline sulfatase (betC), glycine betaine/proline ABC transporter (ProV), glycine betaine/proline betaine transport system permease protein (ProW), Glycine betaine/carnitine transport binding protein (GbuC), osmoprotectant ABC transporter ATP-binding protein (OpuAA), glycine betaine transport system permease protein (OpuAB), glycine betaine-binding protein (OpuAC), osmoregulated proline transporter (OpuE), choline transport ATP-binding protein (OpuBA), choline transport system permease protein (OpuBB), carnitine transport ATP-binding protein (OpuCA), carnitine transport permease protein (OpuCB), carnitine transport binding protein (OpuCC), carnitine transport permease protein (OpuCD), ectoine/5-hydroxyectoine-binding periplasmic protein (UehA), osmoprotectant import ATP-binding proteins (osmV), and aquaporin (Aqp).

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
  - Snippet 1 (score: 0.740)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [3] Identifying orthologs with OMA: A primer
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
  - Snippet 1 (score: 0.731)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [4] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.729)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [5] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.729)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [6] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.728)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [7] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.712)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [8] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.709)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [9] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
- Authors: Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al.
- Year: 2015
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
- DOI: 10.1186/s12864-015-2287-5
- PMID: 26692227
- PMCID: 4687164
- Citations: 69
- Influential citations: 2
- Summary: A revised manually curated full genome sequence for Clostridium autoethanogenum DSM10061 is presented, which provides reliable information for genome-scale models that rely heavily on the accuracy of annotation, and represents an important step towards the manipulation and metabolic modelling of this industrially relevant acetogen.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [10] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.689)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [11] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.683)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [12] Evaluation of Proteins Released to Medium in Yeast-Bacteria Co-culture System
- Authors: Ayşegül Yanik, Ç. Tarhan
- Year: 2023
- Venue: Journal of Advanced Research in Natural and Applied Sciences
- URL: https://www.semanticscholar.org/paper/bf1e6e710a760d61cdce04ea82c683106fe2ad6d
- DOI: 10.28979/jarnas.1196962
- Summary: The wild strain of Schizosaccharomyces pombe and the DH5α strain of Escherichia coli were grown in their own specific media, then cultured for 48 hours and 72 hours by cultivating in media containing 0,1% glucose with different cell number, and finally the differentiation in the proteins released by the cells into the medium was observed in SDS polyacrylamide gels.
- Evidence snippets:
  - Snippet 1 (score: 0.681)
    > The proteins identified as a result of LC-MS/MS analysis were evaluated in UniProt and the names and functions of the proteins are given as an appendix. Here, 6 protein-coding genes in the bands of the proteins released into the medium by the co-culture were found in the S.pombe genome and were classified according to their biological functions and cellular locations using the online platform PANTHER (Figure 2). Other 257 protein-coding genes were found in the E. coli genome. These proteins were also classified according to their cellular location (Figure 3) and their cellular functions (Figure 4). Maltose/maltodextrin-binding periplasmic protein (malE) and D-galactose-binding periplasmic protein (mglB) found in E. coli cells are among the binding proteins found in LC-MS-MS results. The binding protein MglB has a high affinity for glucose (Ferenci, 1996), and at low glucose concentration, glucose is mainly taken up by cells in this way. In a study by Egli et al. (1993), giving 1.8 mg l−1 galactose to a low glucose-containing E. coli culture decreased the glucose utilization of the cells and led to glucose accumulation in continuous culture. In addition, Hua and., (2004) found that the expression of a series of genes encoding membrane transporter proteins was significantly induced in cultures of limited chemostats for various carbon sources, and that about half of these genes were maltose (all genes of malGFE and malK-lamB-malM operons), galactose. They showed that there are genes involved in a wide variety of high-affinity ABC transport systems that facilitate uptake (three genes of the mglBAC operon). In E. coli, the ABC transporter gene family covers approximately 5% of the entire genome (Linton and Higgins, 1998). This shows how important these genes are. Carbon-limited cultures have been proposed to investigate bacterial growth and behavior under environmental conditions (Matin, 1979;Moriarty, 1993;Morita, 1993).

### [13] Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype
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
  - Snippet 1 (score: 0.681)
    > Protein identifications with 2 peptides and a confident protein score (P <0.05) from the HpH fractionation and IDA-MS were used to assign subcellular localization. Using the top score given by WoLF PSORT [10] (www.genscript.com/wolf-psort.html) proteins were categorized into 8 locations. Membrane proteins were predicted using transmembrane helical Markov model (TMHMM) [11] (www.cbs.dtu.dk/services/TMHMM/). Proteins in the solute carrier protein (SLC) and ATP-binding cassette (ABC) transporter families were identified according to gene and protein name. We also used website gene names (www.genenames.org/data) to characterise the subcellular location of the transporter and the type of substrate they transport.
    > For proteins annotated as 'uncharacterised' in figures and tables in the manuscript a BLAST protein homology search was carried out using the Ensembl or uniport accession code in uniprotKB (www.uniprot.org). The accession code page contains the sequence and a link to BLAST. BLASTp results against uniprotkb_Swissprot reference proteomes and an identity sequence match of >95.5% to human, bovine (cattle) or caprine (goat) proteome annotation was accepted as the protein name.

### [14] Gene Discovery through Transcriptome Sequencing for the Invasive Mussel Limnoperna fortunei
- Authors: Marcela Uliano-Silva, J. Americo, R. Brindeiro, F. Dondero, F. Prosdocimi et al.
- Year: 2014
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/6e168d6898550dc5793d4b1606efdb9c7e9caaed
- DOI: 10.1371/journal.pone.0102973
- PMID: 25047650
- PMCID: 4105566
- Citations: 52
- Influential citations: 4
- Summary: The presence of toll-like receptors gives a first insight into an immune system that could be more complex than previously assumed and may be involved in the prevention of disease and extinction when population densities are high and the apparent lack of special adaptations to extremely low O2 levels is a target worth pursuing for the development of a molecular control approach.
- Evidence snippets:
  - Snippet 1 (score: 0.671)
    > BLAST analysis returned significant similarities (e-value cutoff , = 10 25 ) with other protein-coding genes for a small fraction of assembled genes. Table 3 reports the results obtained against the three major protein databases, UNIPROT, NCBI non redundant (nr) and eggNOG. UNIPROT more frequent BLAST hits were against human sequences (16%), Mus musculus (15%), Ratus novergicus (9%) and Drosophila melanogaster (5%). The reproducibility of results in different databases highlights the robustness of the analysis. However, almost 71% of unigenes were not annotated in BLAST searches with protein sequences from the NCBI nr database (FASTA sequences and the annotation text file can be downloaded at http://goo.gl/DZt7K8). We identified several key genes for gene-environment relationships such as cytochrome P450, proteins involved in the toll-like receptors signaling pathway, glutathione S-transferase (GST), gammaglutamil-transpeptidase (GGT) and adhesive proteins Mepf1 (9 unigenes) and Mepf2 (103 unigenes) (Table S2 in supporting information presents the KEGG Orthology identifiers (KO) and the unigenes IDs). For a more straightforward analysis, Table 4 shows the quantity of unigenes annotated as cellular defensesrelated genes through BLAST searches against C. gigas protein sequences (Table S5 presents L. fortunei IDs for genes in Table 4).
    > A total of 3,612 L. fortunei unigenes were classified into 20 of 24 functional categories at eggNOG database (Figure 2). KO identifiers were assigned to 2,579 unigenes, indicating involvement in 292 different pathways (Table S2). These sequences could be assigned to specific KEGG classes: 39.8% to genetic information processing (GIP); 34.3% to metabolism (with enzymes being the most abundant subcategory, 368 unigenes) and 11.5% to Signaling and cellular processes, including cytoskeleton proteins and transporters.

### [15] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.670)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [16] The ATP-binding cassette transporter Cbc (choline/betaine/carnitine) recruits multiple substrate-binding proteins with strong specificity for distinct quaternary ammonium compounds
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
  - Snippet 1 (score: 0.669)
    > We identified a choline, betaine and carnitine transporter, designated Cbc, from Pseudomonas syringae and Pseudomonas aeruginosa that is unusual among members of the ATP‐binding cassette (ABC) transporter family in its use of multiple periplasmic substrate‐binding proteins (SBPs) that are highly specific for their substrates. The SBP encoded by the cbcXWV operon, CbcX, binds choline with a high affinity (Km, 2.6 μM) and, although it also binds betaine (Km, 24.2 μM), CbcXWV‐mediated betaine uptake did not occur in the presence of choline. The CbcX orthologue ChoX from Sinorhizobium meliloti was similar to CbcX in these binding properties. The core transporter CbcWV also interacts with the carnitine‐specific SBP CaiX (Km, 24 μM) and the betaine‐specific SBP BetX (Km, 0.6 μM). Unlike most ABC transporter loci, caiX, betX and cbcXWV are separated in the genome. CaiX‐mediated carnitine uptake was reduced by CbcX and BetX only when they were bound by their individual ligands, providing the first in vivo evidence for a higher affinity for ligand‐bound than ligand‐free SBPs by an ABC transporter. These studies demonstrate not only that the Cbc transporter serves as a useful model for exploring ABC transporter component interactions, but also that the orphan SBP genes common to bacterial genomes can encode functional SBPs.

### [17] Phyletic Profiling with Cliques of Orthologs Is Enhanced by Signatures of Paralogy Relationships
- Authors: N. Skunca, Matko Bosnjak, A. Kriško, P. Panov, S. Džeroski et al.
- Year: 2013
- Venue: PLoS Computational Biology
- URL: https://www.semanticscholar.org/paper/1510cd0e087650323cdf75ea132e6fcbc4d7e852
- DOI: 10.1371/journal.pcbi.1002852
- PMID: 23308060
- PMCID: 3536626
- Citations: 41
- Influential citations: 2
- Summary: A novel model for computational annotation that refines two established concepts: annotation based on homology and annotations based on phyletic profiling is introduced, which will contribute to making experimental validation of computational predictions more approachable, both in cost and time.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > In addition to the systematic experimental verification of novel annotations in three GO categories as described above, here we highlight individual predictions for which we found supporting evidence in the publicly available databases. This information was not available to the classifiers at the time when the models were constructed. The following examples are for E. coli K12, as this is by far the best-studied model prokaryote [21].
    > We predict genes hypC and hybG to have ''nickel cation binding.'' These genes had no GO terms assigned in the 07-02-2012 UniProt-GOA release (http://www.uniprot.org/uniprot/ P0AAM3 and http://www.uniprot.org/uniprot/P0AAM7), and we therefore considered them unannotated. In the meantime, hypC was annotated with ''metal ion binding'' using experimental evidence: this is a parent GO term of our prediction. Moreover, when examining the literature, we found evidence that these two genes are involved in the biosynthesis of the [NiFe] cluster [22].
    > Another prediction is for gltL: we predicted it is annotated with ''ATP-binding cassette (ABC) transporter complex.'' In line with our predictions, PortEco, a portal that includes information from 14 different E. coli data resources [23], labels the gene as ''ATPbinding component of ABC superfamily.'' Note that more general electronic GO annotations were available for this gene, e.g. ''ATP binding,'' ''ATPase activity,'' and ''ATP catabolic process'' (http://www.uniprot.org/uniprot/P0AAG3).
    > A similar prediction of a more detailed function is for ybgI, where we predict GO terms from both BP and MF ontologies. This gene is known to be a conserved metal-binding protein [24], having an electronic GO annotation ''metal ion binding''; we predict it is annotated with the BP GO term ''Mo-molybdopterin cofactor metabolic process.''

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. R. Liang, Zhou Li, Maggie C Y Lau Vetter, T. Vishnivetskaya, O. Zanina et al. (2021). Genomic reconstruction of fossil and living microorganisms in ancient Siberian permafrost. Microbiome. https://www.semanticscholar.org/paper/6204b177c9d3defa17fd2344956d5d8940307f2d
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
4. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
5. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
6. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
7. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
8. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
9. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
10. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
11. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
12. Ayşegül Yanik, Ç. Tarhan (2023). Evaluation of Proteins Released to Medium in Yeast-Bacteria Co-culture System. Journal of Advanced Research in Natural and Applied Sciences. https://www.semanticscholar.org/paper/bf1e6e710a760d61cdce04ea82c683106fe2ad6d
13. J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al. (2022). Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype. PLoS ONE. https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
14. Marcela Uliano-Silva, J. Americo, R. Brindeiro, F. Dondero, F. Prosdocimi et al. (2014). Gene Discovery through Transcriptome Sequencing for the Invasive Mussel Limnoperna fortunei. PLoS ONE. https://www.semanticscholar.org/paper/6e168d6898550dc5793d4b1606efdb9c7e9caaed
15. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
16. Chiliang Chen, Adel Malek, M. Wargo, Deborah A. Hogan, Gwyn A. Beattie (2009). The ATP-binding cassette transporter Cbc (choline/betaine/carnitine) recruits multiple substrate-binding proteins with strong specificity for distinct quaternary ammonium compounds. Molecular microbiology. https://www.semanticscholar.org/paper/805aa43cc4c49264c16b54fda841cc11496bba95
17. N. Skunca, Matko Bosnjak, A. Kriško, P. Panov, S. Džeroski et al. (2013). Phyletic Profiling with Cliques of Orthologs Is Enhanced by Signatures of Paralogy Relationships. PLoS Computational Biology. https://www.semanticscholar.org/paper/1510cd0e087650323cdf75ea132e6fcbc4d7e852