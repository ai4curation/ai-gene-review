---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T14:07:40.572597'
end_time: '2026-07-08T14:07:45.932522'
duration_seconds: 5.36
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0871
  gene_symbol: PP_0871
  uniprot_accession: Q88PH9
  protein_description: 'SubName: Full=Glycine betaine/carnitine/choline ABC transporter,
    permease protein {ECO:0000313|EMBL:AAN66496.1};'
  gene_info: OrderedLocusNames=PP_0871 {ECO:0000313|EMBL:AAN66496.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the binding-protein-dependent transport system
  protein_domains: ABC_transp_perm/SBD. (IPR051204); MetI-like. (IPR000515); MetI-like_sf.
    (IPR035906); BPD_transp_1 (PF00528)
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
- **UniProt Accession:** Q88PH9
- **Protein Description:** SubName: Full=Glycine betaine/carnitine/choline ABC transporter, permease protein {ECO:0000313|EMBL:AAN66496.1};
- **Gene Information:** OrderedLocusNames=PP_0871 {ECO:0000313|EMBL:AAN66496.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the binding-protein-dependent transport system
- **Key Domains:** ABC_transp_perm/SBD. (IPR051204); MetI-like. (IPR000515); MetI-like_sf. (IPR035906); BPD_transp_1 (PF00528)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0871" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0871' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0871** (gene ID: PP_0871, UniProt: Q88PH9) in PSEPK.

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
  - Snippet 1 (score: 0.825)
    > Many of the Firmicutes MAGs from the 5.8 m sample lack the biosynthetic pathway for glycine-betaine, but harbor various genes for osmoregulation and uptake of Fig. 6 Key functional genes involved in the repair of DNA and protein damage and survival under cold, osmotic, and oxidative stresses present (red) in MAGs. Gene abbreviations: protein L-isoaspartyl/D-aspartyl o-methyltransferase (PIMT), methionine sulfoxide reductase (MsrA), uracil-DNA glycosylase (UDG), DNA mismatch repair protein (MutS), DNA replication and repair protein (RecF), cold shock protein (CspA), choline dehydrogenase (betA), betaine aldehyde dehydrogenase (betB), choline sulfatase (betC), glycine betaine/proline ABC transporter (ProV), glycine betaine/proline betaine transport system permease protein (ProW), Glycine betaine/carnitine transport binding protein (GbuC), osmoprotectant ABC transporter ATP-binding protein (OpuAA), glycine betaine transport system permease protein (OpuAB), glycine betaine-binding protein (OpuAC), osmoregulated proline transporter (OpuE), choline transport ATP-binding protein (OpuBA), choline transport system permease protein (OpuBB), carnitine transport ATP-binding protein (OpuCA), carnitine transport permease protein (OpuCB), carnitine transport binding protein (OpuCC), carnitine transport permease protein (OpuCD), ectoine/5-hydroxyectoine-binding periplasmic protein (UehA), osmoprotectant import ATP-binding proteins (osmV), and aquaporin (Aqp).

### [2] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.779)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [3] Role of histone-lysine N-methyltransferase 2D (KMT2D) in MEK-ERK signaling-mediated epigenetic regulation: a phosphoproteomics perspective
- Authors: Sreeshma Ravindran Kammarambath, Leona Dcunha, Athira Perunelly Gopalakrishnan, Amal Fahma, N. Krishna et al.
- Year: 2025
- Venue: Frontiers in Bioinformatics
- URL: https://www.semanticscholar.org/paper/0ac0729148aff3d839e6a15984e11532e9e740f9
- DOI: 10.3389/fbinf.2025.1683469
- PMID: 41341998
- PMCID: 12669113
- Citations: 5
- Summary: The phosphoregulatory network of Histone-lysine N-methyltransferase 2D is delineated, positioning it as a dynamic epigenetic effector modulated by MEK-ERK signaling, with broader implications for cancer and developmental disorders.
- Evidence snippets:
  - Snippet 1 (score: 0.757)
    > Each protein was mapped to its corresponding gene symbol based on the HGNC (downloaded on 30.05.2023) and to its corresponding UniProt (13.04.2023) (UniProt, 2023) accessions using our in-built mapping tool to ensure consistent and standardized annotation. We conducted the analysis using the methodologies outlined in (Sanjeev et al., 2024). The overall workflow used in this study is outlined in Figure 1.

### [4] Genomic analysis of halophilic bacterium, Lentibacillus sp. CBA3610, derived from human feces
- Authors: S. Ahn, S. H. Lee, Hong-Seok Son, S. Roh, Yoon-E Choi
- Year: 2021
- Venue: Gut Pathogens
- URL: https://www.semanticscholar.org/paper/0d9dba4ef01e3fe5572149df8a40881b3f969274
- DOI: 10.1186/s13099-021-00436-2
- PMID: 34162403
- PMCID: 8220782
- Citations: 3
- Summary: Strain CBA3610 is predicted to be a novel candidate species of Lentibacillus through phylogenetic analysis and comparative genomic analysis with other species in the same genus.
- Evidence snippets:
  - Snippet 1 (score: 0.748)
    > Taking into consideration of the characteristics of Lentibacillus of being a halophilic bacterium that survives in a high salinity environment, genes related to osmotic stress of strain CBA3610 were analyzed. In the SEED subsystem of the RAST server, total 34 genes classified as related to 'osmotic stress' , were identified. Among these, one gene was classified as related to osmoregulation and the remaining 33 genes were annotated to be related to choline and betaine uptake and betaine biosynthesis. The gene involved in osmoregulation encoded the aquaporin family protein, a transporter of glycerol across the cytoplasmic membrane that has limited permeability to small uncharged compounds, such as water. The remaining 33 genes are described as follows. As genes involved in the biosynthesis of osmoprotectant glycine betaine, there is one betA gene that encodes oxygen-dependent choline dehydrogenase, which converts choline to betaine aldehyde, and three betB genes that encode NAD/NADPdependent betaine aldehyde dehydrogenase, which converts betaine aldehyde to glycine betaine. In addition, there are seven opuD genes that encode glycine betaine transporter, which are involved in glycine betaine uptake, and 12 genes belonging to the opuA gene family (including the opuAA, opuAB, and opuAC gene) that encode glycine betaine/carnitine/choline ABC transporter. Lastly, there are two ProV genes encoding glycine betaine/ proline betaine transport system ATP-binding protein involved in glycine betaine and proline betaine uptake, four genes belonging to the opuB gene cluster, including opuBA, opuBB, opuBC, and opuBD genes, encoding glycine betaine/carnitine/choline ABC transporter, one opuCB gene encoding carnitine transport permease protein, and three soxA genes that encode sarcosine oxidase alpha subunit that converts sarcosine to glycine [22][23][24].

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
  - Snippet 1 (score: 0.742)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [6] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.742)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [7] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.737)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

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
  - Snippet 1 (score: 0.736)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

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
  - Snippet 1 (score: 0.729)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [10] Environmental distribution and genomic characteristics of Solirubrobacter, with proposal of two novel species
- Authors: Zhu-Ming Jiang, Tong Mou, Ye Sun, J. Su, Li-Yan Yu et al.
- Year: 2023
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/8c527bbaaf0b36018b7505248f5eb2f58049af65
- DOI: 10.3389/fmicb.2023.1267771
- PMID: 38107860
- PMCID: 10722151
- Citations: 30
- Summary: Pan-genomic analysis of available Solirubrobacter spp.
- Evidence snippets:
  - Snippet 1 (score: 0.729)
    > Thus, most Solirubrobacter species were able to tolerate certain levels of osmotic pressure. Genomic analysis revealed the presence of several genes related to osmoprotectant capacity, including genes encoding the choline transport system permease protein OpuBB (opuBB), choline ABC transporter substrate-binding lipoprotein OpuBC (opuBC), glycine betaine/carnitine/choline transport system permease protein OpuCB (opuCB), glycine betaine/carnitine/cholinebinding protein OpuCC (opuCC), osmoprotectant import ATP-binding protein OsmV (osmV), osmoprotectant-binding protein OsmX (osmX), trehalose-6-phosphate synthase (otsA), trehalose-phosphate phosphatase (otsB), malto-oligosyltrehalose trehalohydrolase (treZ), trehalose synthase/amylase TreS (treS), maltooligosyl trehalose synthase (treY), HTH-type transcriptional regulator BetI (betI), oxygen-dependent choline dehydrogenase (betA), betaine aldehyde dehydrogenase (betB), and glycine betaine/proline betaine transport system ATP-binding protein ProV (proV) (Figure 4). Notably, many of these proteins are  Heatmap showing the copy numbers of functional genes predicted in the genomes of seven Solirubrobacter species. Functional genes were identified based on comparison to the KEGG database.
    > involved in trehalose uptake and associated biosynthesis pathways. Trehalose is a major compatible solute involved in osmotic stress responses of cells, cellular adaptation, and survival under heat and desiccation stress (Reina-Bueno et al., 2012).

### [11] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
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
  - Snippet 1 (score: 0.718)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [12] Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype
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
  - Snippet 1 (score: 0.714)
    > Protein identifications with 2 peptides and a confident protein score (P <0.05) from the HpH fractionation and IDA-MS were used to assign subcellular localization. Using the top score given by WoLF PSORT [10] (www.genscript.com/wolf-psort.html) proteins were categorized into 8 locations. Membrane proteins were predicted using transmembrane helical Markov model (TMHMM) [11] (www.cbs.dtu.dk/services/TMHMM/). Proteins in the solute carrier protein (SLC) and ATP-binding cassette (ABC) transporter families were identified according to gene and protein name. We also used website gene names (www.genenames.org/data) to characterise the subcellular location of the transporter and the type of substrate they transport.
    > For proteins annotated as 'uncharacterised' in figures and tables in the manuscript a BLAST protein homology search was carried out using the Ensembl or uniport accession code in uniprotKB (www.uniprot.org). The accession code page contains the sequence and a link to BLAST. BLASTp results against uniprotkb_Swissprot reference proteomes and an identity sequence match of >95.5% to human, bovine (cattle) or caprine (goat) proteome annotation was accepted as the protein name.

### [13] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.709)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [14] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.708)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [15] Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser
- Authors: Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała
- Year: 2025
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
- DOI: 10.1186/s12864-025-12329-8
- PMID: 41408139
- PMCID: 12822150
- Citations: 2
- Summary: An R script is developed that performs a gene symbol update to current official versions combined with identification of ambiguous symbols and retrieval of other IDs from the Ensembl database and provides a single list of updated symbols with annotation about their ambiguity.
- Evidence snippets:
  - Snippet 1 (score: 0.708)
    > Gene nomenclature contains current official symbols and various numbers of synonyms, which pose a challenge to integrating genomic data and increase the probability that different genes share the same symbol. Therefore, we retrieved identifiers assigned to all protein-coding genes in human, mouse, rat and pig genomes that are available in the Ensembl genome browser (release 113) to assess the number of genes, compare species and identify ambiguous symbols. Results: Our analysis revealed that the total number of symbols, both official symbols and synonyms, used to identify protein-coding genes ranges from 16,600 in pigs to 64,580 in mice. Furthermore, the gene nomenclature is not complete because there are also genes without an assigned symbol, which indicates gaps in understanding protein-coding genes, especially in pigs. We also found a large number of gene symbols that map to more than one gene. These symbols might complicate the identification of about 10% of rat and mouse genes and 18% of human protein-coding genes. A simple solution for this problem is the usage of stable gene IDs assigned by scientific institutions and committees (Ensembl, NCBI, RGD, HGNC and VGNC) provided that the genomic information associated with these IDs is retrieved directly from proprietary databases containing the most accurate data. Finally, although gene symbols may pose a problem with unequivocal identification of genes, there are instances when no other identifiers are available in the literature. Therefore, we have developed an R script performing search of the Ensembl database and integrating data to provide a single list of updated symbols with annotation about their ambiguity. Conclusions: Gene symbols are not always reliable and should be reported together with stable IDs to enable unequivocal identification of genes. Therefore, data containing only gene symbols should be used cautiously to avoid misidentification of genes. A solution for this problem is our R script REgeness that performs a gene symbol update to current official versions combined with identification of ambiguous symbols and retrieval of other IDs from the Ensembl database.

### [16] Overexpression of Scr1 protein induces strong changes in the transcriptome and metabolome of Streptomyces coelicolor that affect antibiotic production
- Authors: C. Riascos, Gemma Fernández-García, Javier García-Martín, Ángel Manteca, R. Santamaría et al.
- Year: 2025
- Venue: Microbial Cell Factories
- URL: https://www.semanticscholar.org/paper/1459f4ce98f53d7b31337731f37caa2e8199a493
- DOI: 10.1186/s12934-025-02843-5
- PMID: 41077587
- PMCID: 12516864
- Summary: Xenobiotic response element (XRE) regulator proteins play an important role in gene regulation in Streptomyces. In these bacteria, they are often encoded together with a small protein containing a DUF397 domain. Previous work on 15 such pairs present in S. coelicolor has shown they act as pleiotropic regulators. They dependently affect antibiotic production and morphological differentiation on different culture media. Overexpression of the protein Scr1, which is encoded by gene SCO4441, induc...
- Evidence snippets:
  - Snippet 1 (score: 0.708)
    > In addition to the metabolic processes that were altered by Scr1 overexpression, the RNA-Seq assay also detected differential expression of several important genes involved in molecular transport and gene regulation, as detailed below.
    > ABC transporters: three types of ABC transporters were differentially expressed in the strain Sscr1: mineral and organic ion transporters; oligosaccharide, polyol and lipid transporters; and phosphate and amino acid transporters (Additional File 12). The expression pattern of these genes varied greatly from one type to another. For example, in the Sscr1 strain, genes for three molybdate transport-associated proteins (SCO3704, SCO3705, and SCO3706) were overexpressed only at 36 h. The same occurred for the betaine transporter (SCO4831), an osmoprotectant; except in this case, the gene for the substrate-binding protein (SCO2933) was not differentially expressed. Additionally, the genes for the three proteins responsible for the multiple sugar transporter were under-expressed. Thus, the gene encoding a putative sugar-binding protein (SCO2404) was under-expressed at 36 h, while those genes encoding the permease protein (SCO2406) and the ATP-binding protein (SCO2405) were under-expressed at 48 h. In the case of adenosine and the genes of four proteins associated with transport, the first, a lipoprotein (SCO4884), was under-expressed at 36 h, while the genes for the other three proteins, two permease proteins (SCO4887 and SCO4888) and an ATP-binding protein (SCO4886), were overexpressed at 48 h. As for orthophosphate transport, the genes for the three proteins responsible for its transport (SCO6814, SCO6415, and SCO6416) were overexpressed at 36 and 48 h and showed high FC values.

### [17] Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea
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
  - Snippet 1 (score: 0.706)
    > The BLASTx homology search tool, a component of the standalone NCBI-blast-2.3.0+, was used to perform functional annotation of the F. udum genes (Altschul et al., 1990). With a cut-off E value of ≤1e−06 and a similarity of 34%, BLASTx identified the homologous sequences of the genes in the NCBI non-redundant protein database. Gene ontology (GO) analysis was carried out using Blast2GO PRO 4.1.5 (Conesa and Gotz, 2008). In three different mappings, B2G performed as follows: (1) Using two NCBI-provided mapping files, blast result accessions are used to get gene names (symbols; gene info, gene 2 accessions). (2) Blast result GI identifiers were used to retrieve UniProt IDs using a mapping file from PIR (non-redundant reference protein database), which includes PSD, Swiss-Prot, UniProt, TrEMBL, GenPept, RefSeq, and PDB. The names of the identified genes were searched in the species-specific entries of the gene product table of the GO database. With the aid of the KAAS-KEGG Automatic Annotation Server, pathway analyses were carried out. This database provides functional annotation of genes using other data servers (Moriya et al., 2007). Accessions from the blast results were looked for in the DBXRef table of the GO database.

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
  - Snippet 1 (score: 0.702)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. R. Liang, Zhou Li, Maggie C Y Lau Vetter, T. Vishnivetskaya, O. Zanina et al. (2021). Genomic reconstruction of fossil and living microorganisms in ancient Siberian permafrost. Microbiome. https://www.semanticscholar.org/paper/6204b177c9d3defa17fd2344956d5d8940307f2d
2. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
3. Sreeshma Ravindran Kammarambath, Leona Dcunha, Athira Perunelly Gopalakrishnan, Amal Fahma, N. Krishna et al. (2025). Role of histone-lysine N-methyltransferase 2D (KMT2D) in MEK-ERK signaling-mediated epigenetic regulation: a phosphoproteomics perspective. Frontiers in Bioinformatics. https://www.semanticscholar.org/paper/0ac0729148aff3d839e6a15984e11532e9e740f9
4. S. Ahn, S. H. Lee, Hong-Seok Son, S. Roh, Yoon-E Choi (2021). Genomic analysis of halophilic bacterium, Lentibacillus sp. CBA3610, derived from human feces. Gut Pathogens. https://www.semanticscholar.org/paper/0d9dba4ef01e3fe5572149df8a40881b3f969274
5. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
6. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
7. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
8. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
9. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
10. Zhu-Ming Jiang, Tong Mou, Ye Sun, J. Su, Li-Yan Yu et al. (2023). Environmental distribution and genomic characteristics of Solirubrobacter, with proposal of two novel species. Frontiers in Microbiology. https://www.semanticscholar.org/paper/8c527bbaaf0b36018b7505248f5eb2f58049af65
11. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
12. J. Bond, A. Donaldson, S. Woodgate, K. Kamath, M. McKay et al. (2022). Quantification of cytosol and membrane proteins in rumen epithelium of sheep with low or high CH4 emission phenotype. PLoS ONE. https://www.semanticscholar.org/paper/b1e6e0b34671baf1eb1ec74743f7301a52572b0b
13. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
14. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
15. Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała (2025). Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser. BMC Genomics. https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da
16. C. Riascos, Gemma Fernández-García, Javier García-Martín, Ángel Manteca, R. Santamaría et al. (2025). Overexpression of Scr1 protein induces strong changes in the transcriptome and metabolome of Streptomyces coelicolor that affect antibiotic production. Microbial Cell Factories. https://www.semanticscholar.org/paper/1459f4ce98f53d7b31337731f37caa2e8199a493
17. A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al. (2023). Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea. Frontiers in Microbiology. https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
18. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a