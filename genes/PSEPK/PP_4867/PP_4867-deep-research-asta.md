---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T17:15:50.538323'
end_time: '2026-07-08T17:15:55.912625'
duration_seconds: 5.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4867
  gene_symbol: PP_4867
  uniprot_accession: Q88DF8
  protein_description: 'SubName: Full=Branched-chain amino acid ABC transporter, periplasmic
    amino acid-binding protein (BraC-like) {ECO:0000313|EMBL:AAN70436.1};'
  gene_info: OrderedLocusNames=PP_4867 {ECO:0000313|EMBL:AAN70436.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the leucine-binding protein family.
  protein_domains: Leu-bd. (IPR028081); Leu_Ile_Val-bd. (IPR000709); Peripla_BP_I.
    (IPR028082); Peripla_BP_6 (PF13458)
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
- **UniProt Accession:** Q88DF8
- **Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein (BraC-like) {ECO:0000313|EMBL:AAN70436.1};
- **Gene Information:** OrderedLocusNames=PP_4867 {ECO:0000313|EMBL:AAN70436.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the leucine-binding protein family.
- **Key Domains:** Leu-bd. (IPR028081); Leu_Ile_Val-bd. (IPR000709); Peripla_BP_I. (IPR028082); Peripla_BP_6 (PF13458)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4867" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4867' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4867** (gene ID: PP_4867, UniProt: Q88DF8) in PSEPK.

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

### [1] FusionPDB: a knowledgebase of human fusion proteins
- Authors: H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim
- Year: 2023
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
- DOI: 10.1093/nar/gkad920
- PMID: 37870473
- PMCID: 10767906
- Citations: 13
- Influential citations: 1
- Summary: FusionPDB is the only resource providing whole 3D structures of fusion proteins and comprehensive knowledge of human fusion proteins and it will be regularly updated until it covers all human fusion proteins in the future.
- Evidence snippets:
  - Snippet 1 (score: 0.763)
    > To assign functional or gene categories, we integrated cancer genes, tumor suppressors, epigenetic regulators, DNA damage repair genes, human essential genes, kinases and transcription factors. In each gene group, we checked the retention and ORFs of the main protein functional features. There are 13 features belonging to the 'region' category, including 'calcium binding', 'coiled coil', 'compositional bias', 'DNA binding', 'domain', 'intramembrane', 'motif', 'nucleotide binding', 'region', 'repeat', 'topological domain', 'transmembrane' and 'zinc finger'. To perform the protein functional feature retention search, we first downloaded the GFF (General Feature Format) format protein information of 10 651 UniProt accessions from UniProt for 10 619 genes involved in 15 030 fusion genes ( 10 ). UniProt provides the loci information of 39 protein features, including six molecule processing features, 13 region features, four site features, six amino acid modification features, two natural variation features, five experimental info features and three secondary structure features. Since such feature loci information is based on amino acid sequences, the genomic breakpoint information was converted into the amino acid level while considering all UniProt protein accessions, ENST isoforms and multiple breakpoints for each partner. To map each feature to the human genome sequence, we used the GENCODE (v19) gene model of human reference genome ( 11 ). For the 5 -partner gene, we considered the protein feature to be retained in the fusion gene if the breakpoints occurred on the 3 -end of the protein feature. On the contrary, if a protein domain was not entirely included in the fusion amino acid sequence, we reported such fusion genes as having not retained that protein feature. Similarly, for the 3partner gene, we considered the fusion gene to have retained the protein feature if the breakpoints occurred on the 5 -end of the protein feature region.

### [2] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.737)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [3] Environment sensing and response mediated by ABC transporters
- Authors: Sarah E. Giuliani, A. Frank, Danielle M. Corgliano, Catherine Seifert, L. Hauser et al.
- Year: 2011
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/cc4616ae2df0e74a413ae71b9560d956107ef0c5
- DOI: 10.1186/1471-2164-12-S1-S8
- PMID: 21810210
- PMCID: 3223731
- Citations: 65
- Influential citations: 2
- Summary: The functional screen identified specific ligands that bound to ABC transporter periplasmic binding subunits from R. palustris that provide unique insight for the metabolic capabilities of this organism and are consistent with the ecological niche of strain isolation.
- Evidence snippets:
  - Snippet 1 (score: 0.721)
    > Three proteins (RPA2499, RPA2628, and RPA3810) were identified as amino acid binding proteins via the FTS screening (Table 1). This observation is consistent with the assigned annotation and the general functional prediction of TransportDB (Table 2). The set of binding proteins specific for amino acids provide transport capabilities for seven of the individual amino acids. The genes encoding the RPA2628 (PBP), RPA2629 and RPA2630 (integral membrane subunits) (methionine/ cysteine/histidine) are orthologs of a verified amino acid transporter in Rhizobium leguminosarum [32]. They are also localized in a cluster of 10 ABC transporter proteins containing four periplasmic binding proteins (three screened by FTS assay, Additional file 1) and RPA2628 was the only protein with specific ligand binding. The characterized set of binding proteins reflects an emphasis on maintenance of sulfate and nitrogen stores. RPA2499, annotated as an arginine binding protein, is adjacent to an "amidase" gene. Asparagine has a N:C ratio of 2:4, which makes it an efficient molecule for the storage and transport of nitrogen.

### [4] Cj1199 Affect the Development of Erythromycin Resistance in Campylobacter jejuni through Regulation of Leucine Biosynthesis
- Authors: H. Hao, Fei Li, Jing Han, S. Foley, Menghong Dai et al.
- Year: 2017
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/9152e27a908296795b4779c02d4aa02ffae2f388
- DOI: 10.3389/fmicb.2017.00016
- PMID: 28144238
- PMCID: 5239772
- Citations: 11
- Summary: The Cj1199 gene may directly regulate the leucine biosynthesis and transport and indirectly affect the development of erythromycin resistance in C. jejuni.
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > The 20 genes down-regulated in Cj1199 are shown in Table 2.
    > Five genes (leuA, leuB, leuC, leuD, and trpE) were involved in amino acid biosynthesis. The leuABCD genes participated in leucine biosynthesis pathway. Five genes (Cj0919c, Cj0920c, peb1A, pebC, and ceuC) encoded transporters or binding proteins. The permease protein (Cj0919c-Cj0920c), substratebinding protein (Peb1A), and ATP-binding protein (PebC) worked cooperatively in an ABC-type amino acid transport system. The ceuC encoded enterochelin uptake permease which was also transporters or binding protein. The Cj0246c was involved in signal transduction. Six genes (Cj0560, Cj1356c, Cj0423, Cj0424, Cj0425, and Cj0200c) encoded putative integral membrane or periplasmic proteins. Another three (Cj1025c, Cj1722c, and Cj1388) were hypothetical genes. Only Cj1241 gene encoding a putative major facilitator superfamily (MFS) transport protein was up-regulated in Cj1199. Using qRT-PCR to verify the microarray results, Cj1241 gene was confirmed to be up-regulated, while other four respective genes (Cj0920c, Cj1388, Cj0560, and Cj1717c) were confirmed to be down-regulated (Figure 1).

### [5] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.708)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

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
  - Snippet 1 (score: 0.707)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [7] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.705)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [8] Genome-wide Identification of conditionally essential genes supporting Streptococcus suis growth in serum and cerebrospinal fluid
- Authors: Maria Juanpere-Borràs, Tiantong Zhao, Jos Boekhorst, Blanca Fernandez-Ciruelos, Rajrita Sanyal et al.
- Year: 2025
- Venue: Virulence
- URL: https://www.semanticscholar.org/paper/400884affc80cbd5eef1e69b6961748a60a5b400
- DOI: 10.1080/21505594.2025.2600145
- PMID: 41396007
- PMCID: 12707516
- Citations: 1
- Summary: Using Tn-Seq coupled with Nanopore sequencing to identify conditionally essential genes for growth of S. suis provides new insights into the genetic requirements for S. suis survival in host-like environments and a deeper understanding of its ability to adapt to distinct physiological niches.
- Evidence snippets:
  - Snippet 1 (score: 0.701)
    > Gene SSU_RS04755 has been predicted to encode a basic membrane family protein (BMP), a transmembrane component of specific ABC transporters. Growth curve experiments did not reveal a significant reduction in the growth rate of our ΔSSU_RS04755 mutant. The operon genes with SSU_RS04755 were predicted to encode an ATPbinding protein and a permease which are typical components of an ABC transporter. Both predicted ATPbinding protein and permease encoding genes appeared as CEGs in our Tn-seq results (Table 1). The protein sequence associated with SSU_RS04755 shares significant identity with lipoproteins that are components of nucleoside ABC transporters in Gram-positive bacteria (see above), suggesting that SSU_RS04755 and its operon genes may encode an ABC transporter complex involved in nucleoside transport. To investigate the possible functional equivalence of SSU_RS04755 operon genes with ABC transporters, we performed amino acid sequence alignments of SSU_RS04755 with PnrA and TmpC, which are homologous nucleoside binding lipoproteins from S. pneumoniae and Treponema pallidum (T. pallidum) respectively [49,50]. Using the crystal structure of PnrA binding to adenosine [49], we confirmed that all but one (T70) of the specific amino acids involved in adenosine binding by PnrA were conserved in SSU_RS04755 (Figure 5(c)).
    > To verify if the structural positions of these amino acids were conserved, we performed a structural prediction (see methods) of the predicted S. suis lipoprotein SSU_RS04755 and aligned it to the structure of PnrA (ID 6y9U in Protein Data Bank (PDB). We confirmed that all amino acids involved in the adenosine binding are located at the same position in both protein structures.

### [9] Revealing the Functions of the Transketolase Enzyme Isoforms in Rhodopseudomonas palustris Using a Systems Biology Approach
- Authors: Chia-Wei Hu, Ya-Ling Chang, Shiang-Jiuun Chen, L. Kuo-Huang, J. Liao et al.
- Year: 2011
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/74f5d8e7b988d3891c594826f109e7f5bad28bd2
- DOI: 10.1371/journal.pone.0028329
- PMID: 22174789
- PMCID: 3234253
- Citations: 14
- Summary: The results indicate that the two isoforms of transketolase in R. palustris could affect photoautotrophic growth through both common and divergent metabolic mechanisms.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > These results indicate that transketolase I and II have similar functions although they employ slightly different metabolic mechanisms. Moreover, the higher involvement of glycolysis-related proteins in transketolase II-overexpressing strain observed in protein interaction network results was similar with the results of gene ontology distribution obtained from the transcriptomic study. Some functional terms related to glycolysis and carbonhydrate metabolism such as the glyceraldehyde-3-phosphate dehydrogenase (phosphorylating) activity and 4-alpha-glucanotransferase were also enriched in gene ontology analysis. The significant appearance of photosynthesis associated genes were only observed in transcriptomic analysis. It probably was resulted from the low assistance of membrane proteins, where most photosynthesisassociated molecules located, in protein extracts. Notably, protein profiles showed that overexpression of both transketolase I and II upregulated PEPCK, a protein involved in CBB cycle-associated carbon metabolism. PEPCK is an enzyme that can reversibly catalyze oxaloacetate production from phosphoenolpyruvate via reductive carbon dioxide fixation in the bacterial cytosol [43,45]. The higher production of oxaloacetate might lead to the enhanced synthesis of amino acids or carbohydrates [46]. Amino acid transport is an important aspect of amino acid metabolism. Several classes of permeases, members of the family of binding protein-dependent transporter systems, along with periplasmic binding proteins, are responsible for amino acid transport. In this study, we found that branched chain aminoacid ABC transporter substrate-binding protein (RPA3297) and ABC transporter, periplasmic amino acid binding protein aapJ-1 (aapJ-1) are constituents of ATP-requiring ABC transporters responsible for amino acid uptake and efflux. Amino acids such as glutamate, aspartate and histidine are all substrates for periplasmic binding protein-dependent transport systems [47,48]. An extracellular solute-binding protein family 1 (RPA4404), was also upregulated in transketolase-overexpressing strains.

### [10] MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data
- Authors: Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang
- Year: 2010
- Venue: Journal of Biomedicine and Biotechnology
- URL: https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
- DOI: 10.1155/2009/642524
- PMID: 20169000
- PMCID: 2822236
- Citations: 18
- Influential citations: 1
- Summary: By applying the MIClique algorithm to real gene expression data, some DEC gene subsets which correlated under one experimental condition but uncorrelated under another condition are detected from the graph of colon dataset and leukemia dataset.
- Evidence snippets:
  - Snippet 1 (score: 0.695)
    > Table 3 lists the Genbank accession number, the gene symbols, accession number in UniProtKB (UniProt Knowledgebase), and gene descriptions given by colon data. The UniProtKB is the central hub for the collection of information on proteins such as amino acid sequence, protein name or description, taxonomic data, and biological ontology [24]. Figure 6 depicts gene expression profiles of the eight genes in normal and disease samples. As shown in Figure 6, the profiles of these genes are highly coexpressed in normal samples (samples 1-22) while the coexpression pattern disappears in disease samples (samples 23-62).

### [11] ‘Ca. Liberibacter asiaticus’ Proteins Orthologous with pSymA-Encoded Proteins of Sinorhizobium meliloti: Hypothetical Roles in Plant Host Interaction
- Authors: L. Kuykendall, J. Shao, J. Hartung
- Year: 2012
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/d1903bab3348459a5230cb86962e8df123d9be22
- DOI: 10.1371/journal.pone.0038725
- PMID: 22761700
- PMCID: 3382624
- Citations: 8
- Summary: The presence of multiple orthologs defies mutational analysis and is consistent with the hypothesis that these proteins may be of particular importance in host/microbe interaction and their duplication likely facilitates their ongoing evolution.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > ATP Binding Cassette type amino acid transporters comprise the largest class of genes shared by 'Ca. Liberibacter asiaticus', pSymA and the S. meliloti chromosome (Table 2). For most ABCtype transporter proteins encoded by 'Ca. Liberibacter asiaticus' genes there are multiple homologs on pSymA, dispersed over the megaplasmid (Table S1). YP_003064586 is an example of an ABC-type transporter protein from 'Ca. Liberibacter asiaticus'. In addition to NP_435288.1 there are 10 more pSymA-encoded proteins homologous to YP_003064586 (E = 4e-67 up to 1e-14), and all are annotated as general amino acid transporters with an ATP binding site and other characteristics of an ABC type amino acid transporter. The corresponding genes are dispersed across the pSymA (Fig. 1A; Table 2).
    > YP_003064753 is a proline/glycine betaine ABC transporter protein with eight pSymA-encoded homologs (Table S1). YP_003064754, another proline/glycine betaine permease/ABC transporter permease protein, has two pSymA-encoded homologs. 'Ca. Liberibacter asiaticus' YP_003065117 and YP_003064552, both ATP-binding ABC-type transporter proteins, each have four homologs encoded by genes on pSymA. YP_003065525, a putative amino acid-binding periplasmic protein, is homologous to two pSymA-encoded predicted proteins. YP_003065526, an ABC-type amino acid transporter permease, has 7 homologs encoded by pSymA genes. These are examples of multiple, redundant shared homologs of ABC-type amino acid transport systems encoded by pSymA. 'Ca.

### [12] GRIMM: Genetic stRatification for Inference in Molecular Modeling
- Authors: Ashley Babjac, Adrienne Hoarfrost
- Year: 2026
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/a923e3c2800f1ce4cc937015594f74395af624a9
- Citations: 1
- Summary: GRIMM (Genetic stRatification for Inference in Molecular Modeling), a benchmark for enzyme function prediction that employs genetic stratification, enables more realistic evaluation of functional prediction models on both familiar and unseen classes and establishes a benchmark that more faithfully assesses model performance and generalizability.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > We used amino acid sequence data from the Universal Protein Resource (UniProt) UniProt Consortium [2025] and associated gene DNA coding sequences in the European Nucleotide Archive (ENA) Leinonen et al. [2010]. The UniProt database is divided into two sections: (i) UniProt/TrEMBL (which includes more sequence diversity but more annotation errors owing to homology-based annotations and error propagation Schnoes et al. [2009]) and (ii) UniProt/SwissProt (which is carefully curated and provides high confidence accurate functional annotations). For this study, we limited the data retrieved to prokaryotic organisms in SwissProt (May 2025) UniProt Consortium [2025].
    > We mapped UniProt/SwissProt accession numbers to corresponding identifiers in UniRef (Universal Protein Resource Reference Clusters) UniRef50, UniRef90, and UniRef100, which define protein clusters based on amino acid sequence identity at 50, 90, and 100 percent amino acid identity respectively; and to their corresponding EMBL CDS IDs for gene coding sequences in the ENA database Leinonen et al. [2010] using ID mapping files uni [2021], Wang et al. [2021] from UniProtKB. Each EMBL CDS ID's corresponding DNA sequence was then obtained from ENA. EC numbers that were either incomplete or missing were removed from the dataset. Individual entries were created for UniProt records with more than one EMBL CDS ID in the nucleotide version of the dataset.

### [13] Adaptation, Ecology, and Evolution of the Halophilic Stromatolite Archaeon Halococcus hamelinensis Inferred through Genome Analyses
- Authors: Reema K. Gudhka, B. Neilan, B. Burns
- Year: 2015
- Venue: Archaea
- URL: https://www.semanticscholar.org/paper/d650f910b391d57d43d94e5305e4902735d9f51f
- DOI: 10.1155/2015/241608
- PMID: 25709556
- PMCID: 4325475
- Citations: 29
- Summary: Characteristics reflecting its survival in its extreme environment were revealed, including putative genes/pathways involved in osmoprotection, oxidative stress response, and UV damage repair, and genome analyses indicated the presence of putative transposases as well as positive matches of genes of H. hamelinensis against various genomes of Bacteria, Archaea, and viruses, suggesting the potential for horizontal gene transfer.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > H. hamelinensis whole cells indicated that the organism utilizes glucose, sucrose, xylose, maltose, trehalose, and glycerol as both single and complex carbon sources, in addition to  (gene ID: 2502301667) and NAD + synthetase (Gene ID: 2502298992, 2502299198, 2502299746). In addition to these enzymes, H. hamelinensis also possesses genes encoding three ABC transport proteins involving glutamine, namely, glutamine ABC transporter, periplasmic glutamine-binding protein (gene ID 2502298730), ABC-type glutamine/glutamate/polar amino acids transport system, permease protein (gene ID: 2502298731), and ABC-type glutamine/glutamate polar amino acids transport system, ATP-binding protein (gene ID: 2502298732).

### [14] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
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
  - Snippet 1 (score: 0.688)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [15] Computational screening of phytochemicals targeting mutant KRAS in colorectal cancer
- Authors: Muskan Arooj, R. Mateen, M. Javed, Muhammad Ali, Muhammad Irfan Fareed et al.
- Year: 2025
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/2e47ff33fc8e4bd8a85a3cd322f3441bb45db205
- DOI: 10.1038/s41598-025-14229-z
- PMID: 40770256
- PMCID: 12329011
- Citations: 2
- Summary: This study focused on the identification of potential phytochemicals that can inhibit the KRAS protein from being overexpressed in CRC using the anticancer medication fruquintinib, which has been authorized by the FDA.
- Evidence snippets:
  - Snippet 1 (score: 0.687)
    > For the structure retrieval of the KRAS gene, which is overexpressed in CRC, the Universal Protein Resource (UniProt) (https://www.uniprot.org/) database was first consulted for detailed functional information. UniProt provides extensive data on proteins and their functional annotations 19 . The KRAS gene encoding GTPase protein consisting of 189 amino acids with a molecular weight of approximately 21.6 kDa was recovered from the Protein Data Bank (PDB) using the RCSB-PDB ID: 7SCW, which has a resolution of 1.98 Å. The Protein Data Bank (PDB) ( https://doi.org/10.2210/pdb7SCW/pdb) is a crucial resource for studying the 3D structures, aiding research and education in many fields 20 .

### [16] Transcriptomic Analysis Reveals Competitive Growth Advantage of Non-pigmented Serratia marcescens Mutants
- Authors: T. Xiang, Wei Zhou, Cailing Xu, Jing Xu, R. Liu et al.
- Year: 2022
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/cf6eabbd1224ea1e12b6239237eb38081b0951d2
- DOI: 10.3389/fmicb.2021.793202
- PMID: 35058908
- PMCID: 8764370
- Citations: 7
- Summary: The data indicate that S. marcescens shuts down several high-cost systems and activates the amino acid degradation and transport pathways at the transcriptional level to obtain extra resources, which provides new insights into the competitive growth advantage of bacterial spontaneous color mutants.
- Evidence snippets:
  - Snippet 1 (score: 0.679)
    > Quantitative real-time RT-PCR analysis was performed to validate the RNA-sequencing results. As shown in Supplementary Figure S1, 11 downregulated genes, including 4′-phosphopantetheinyl transferase (pho), O-methyltransferase (pigF), BsmB family protein   phenylacetate-CoA oxygenase subunit PaaB (paaB), succinylglutamate desuccinylase (astE), D-threitol dehydrogenase (dthD), periplasmic protein CpxP (cpxP), binding-dependent transport system inner membrane component family protein (dppB), phosphonate-transporting ATPase (livF), phenylacetic acid degradation protein (paaE), PTS system maltose and glucosespecific IICB components (malX), D-amino-acid oxidase (mnmC), ABC transporter substrate-binding protein (dppA), transcriptional regulator LrhA (pecT), and periplasmic substrate-binding component of an ABC superfamily oligopeptide transporter (oppA), were selected. In general, the expression characteristics of the tested genes were consistent with RNA-Seq transcriptomic analysis.

### [17] Enterocin Cross-Resistance Mediated by ABC Transport Systems
- Authors: Claudia Teso-Pérez, M. Martínez-Bueno, J. Peralta‐Sánchez, E. Valdivia, M. Maqueda et al.
- Year: 2021
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/a8d177ecdcfd8fe0c3cdf9cf0e97ecd277dd3aeb
- DOI: 10.3390/microorganisms9071411
- PMID: 34208875
- PMCID: 8306556
- Citations: 8
- Influential citations: 1
- Summary: Antimicrobial activity assays showed that enterocin AS-48 Transporter-2 is responsible for cross-resistance between AS- 48 and MR10A/B enterocIn producers and allowed identification of the MR10a/B immunity gene system.
- Evidence snippets:
  - Snippet 1 (score: 0.678)
    > The mr10A/B gene cluster is formed by at least 10 genes (mr10A, mr10B, mr10E1, mr10F1, mr10G1, mr10H1, as48E, as48F, as48G, mr10H) (Figure 2c). Structural genes mr10A and mr10B encode two leaderless proteins of 134 and 131 amino acid residues, respectively. The putative gene mr10E1 encodes a Domain of Unknown Function (DUF) protein family. The putative genes mr10F1 and mr10G1 also encode two proteins of unknown function (90 and 141 aa, respectively). The putative mr10H1 gene encodes a Pleckstrin Homology (PH) domain-containing protein (458 aa). Additionally, the mr10EFGH gene cluster constitutes an ABC transport system in which mr10E encodes a protein of 163 amino acid residues of unknown function, mr10F (406 aa) encodes an efflux Resistance-Nodulation-Division (RND) transporter periplasmic adaptor subunit, mr10G (227 aa) encodes an ATP-binding protein, and finally, mr10H encodes the ABC transporter permease.

### [18] The molecular dimension of microbial species: 3. Comparative genomics of Synechococcus strains with different light responses and in situ diel transcription patterns of associated putative ecotypes in the Mushroom Spring microbial mat
- Authors: M. T. Olsen, Shane Nowack, J. Wood, Eric D. Becraft, K. Labutti et al.
- Year: 2015
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/08c90ebb1e5ef5c058f332936ee7c6cf6e27919d
- DOI: 10.3389/fmicb.2015.00604
- PMID: 26157428
- PMCID: 4477158
- Citations: 51
- Influential citations: 1
- Summary: In situ diel transcription patterns of genes revealed that expression is fine-tuned to the different light environments experienced by ecotypes prevalent at various depths in the mat, suggesting that strains of closely related PEs have different genomic adaptations that enable them to inhabit distinct ecological niches while living in close proximity within a microbial community.
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > The PE A1-OS and A1-MS strain genomes have a five-gene cluster annotated as a peptide/opine/nickel ABC transporter (PepT family), which includes a periplasmic substrate-binding protein, two permease subunits, and two ATP-binding protein genes. Additionally, the PE A1-OS and A1-MS strain genomes possess two components of a cystine ABC transporter, genes encoding the periplasmic cystine binding protein and the permease protein, as well as two genes, flanked by genes for mobile element proteins, that are annotated as succinate dehydrogenase flavoprotein subunit sdhA and omega-amino acid-pyruvate aminotransferase. Transcript abundances for all of these genes are higher during the light period and lower at night, similar to other genes that are expressed during the day (Supplementary Figure S2). Finally, along with the Type I and Type II CRISPR/cas arrays that are conserved among all four strains, the PE A1-MS genome contains a Type III CRISPR/cas array previously found in the PE A1-OS strain genome by Heidelberg et al. (2009). This is a unique CRISPR/cas array that is shared by Roseiflexus sp. RS-1, an anoxygenic photosynthetic organism that is also abundant in these microbial mat communities (Klatt et al., 2011). Although the amino acid similarities of the homologous genes are only 40-66% between the two organisms, there are transposons flanking the array in the PE A1 strain genomes, which suggests a possible, if not recent, lateral gene transfer event in the mat (Heidelberg et al., 2009).

### [19] Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B
- Authors: Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al.
- Year: 2022
- Venue: Data in Brief
- URL: https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
- DOI: 10.1016/j.dib.2022.108592
- PMID: 36164296
- PMCID: 9508510
- Citations: 2
- Influential citations: 1
- Summary: Covering differential proteomes of three cell lines in a pairwise model, the data could be used to further screen the kinesins that play a vital role in regulating the growth of UM.
- Evidence snippets:
  - Snippet 1 (score: 0.670)
    > 2.8.1. Annotation methods 2.8.1.1. Functional annotation. UniProt-GOA database was utilized to retrieve Gene Ontology (GO) annotation proteome. First, the identified protein identity was converted to UniProt identity and then mapped to GO identity based on the protein identity. When the identified protein was not annotated by UniProt-GOA, the functional annotation of that protein was conducted using the InterProScan software according to the amino acid sequence alignment approach. All proteins were then classified into 3 groups: molecular function, cellular component and biological process.

### [20] Topology based identification and comprehensive classification of four-transmembrane helix containing proteins (4TMs) in the human genome
- Authors: Misty M. Attwood, Arunkumar Krishnan, Valentina Pivotti, Samira Yazdi, M. S. Almén et al.
- Year: 2016
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/268e83d5e00c4b7b210ab19c9bd873e0e50ba87e
- DOI: 10.1186/s12864-016-2592-7
- PMID: 27030248
- PMCID: 4815072
- Citations: 10
- Summary: This study identifies the complete 4TM complement from the latest release of the human genome and assess the 4TM structure group as a whole and functionally characterize this dataset and evaluates the resulting groups and ubiquitous functions, and furthermore describe disease and drug target involvement.
- Evidence snippets:
  - Snippet 1 (score: 0.665)
    > The manual classification process included four steps, which are highlighted in Fig. 1B. Universal protein resource (Uniprot) [28] was used to access annotation information on the dataset by using the unique Ensembl protein identification associated with each protein. Uniprot is a large comprehensive repository of protein sequences with manually curated as well as automatically generated associated annotations. For each protein, the associated UniProt annotations were used in the curation process: gene name, sequence status, review status, Consensus Coding Sequence identifier, Transporter Classification number, Enzyme Commission number, Pfam domain information, Gene Ontology annotation terms, and protein family information.
    > The Uniprot sequence information is derived from translated sequences that have been submitted to the International Nucleotide Sequence Database Collaboration (INSDC), which is EMBL-bank, GenBank, and DDBJ. The canonical sequence is determined from either the most prevalent, the most similar to orthologous sequences, the properties of the amino acid composition, or in lieu of nothing else, then the longest sequence. The sequence status is defined as either complete or fragment, in which the canonical sequence is missing amino acid residues, often in the initial or terminal ends. Those protein sequences identified as fragments were considered invalid proteins and culled from the dataset. To reduce falsepositive predictions from TOPCONS-single, proteins that were identified in literature or database sources as having less than or greater than four-transmembrane segments were also removed from the dataset.
    > The initial gene annotation source, GenCode, has ~1050 more protein-coding gene entries than the most conservative annotation resource, the Consensus Coding Sequence dataset (CCDS) [64]. Therefore the CCDS identifier was used to assess the validity of each protein, i.e. that each has acceptable transcriptional support and recognized protein-coding annotation. Additionally, the sequence status, CCDS identifier, and sequence length were used to ensure that the predicted protein was the main (or canonical) protein product of the gene and not an isoform. There are eight predicted proteins in the dataset that do not have a CCDS identifier associated with them.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. H. Kumar, Lin-ya Tang, Chengyuan Yang, P. Kim (2023). FusionPDB: a knowledgebase of human fusion proteins. Nucleic Acids Research. https://www.semanticscholar.org/paper/6abc299ca227f23e802b197c4d7fdfcaca024697
2. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
3. Sarah E. Giuliani, A. Frank, Danielle M. Corgliano, Catherine Seifert, L. Hauser et al. (2011). Environment sensing and response mediated by ABC transporters. BMC Genomics. https://www.semanticscholar.org/paper/cc4616ae2df0e74a413ae71b9560d956107ef0c5
4. H. Hao, Fei Li, Jing Han, S. Foley, Menghong Dai et al. (2017). Cj1199 Affect the Development of Erythromycin Resistance in Campylobacter jejuni through Regulation of Leucine Biosynthesis. Frontiers in Microbiology. https://www.semanticscholar.org/paper/9152e27a908296795b4779c02d4aa02ffae2f388
5. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
6. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
7. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
8. Maria Juanpere-Borràs, Tiantong Zhao, Jos Boekhorst, Blanca Fernandez-Ciruelos, Rajrita Sanyal et al. (2025). Genome-wide Identification of conditionally essential genes supporting Streptococcus suis growth in serum and cerebrospinal fluid. Virulence. https://www.semanticscholar.org/paper/400884affc80cbd5eef1e69b6961748a60a5b400
9. Chia-Wei Hu, Ya-Ling Chang, Shiang-Jiuun Chen, L. Kuo-Huang, J. Liao et al. (2011). Revealing the Functions of the Transketolase Enzyme Isoforms in Rhodopseudomonas palustris Using a Systems Biology Approach. PLoS ONE. https://www.semanticscholar.org/paper/74f5d8e7b988d3891c594826f109e7f5bad28bd2
10. Huanping Zhang, Xiaofeng Song, Huinan Wang, Xiaobai Zhang (2010). MIClique: An Algorithm to Identify Differentially Coexpressed Disease Gene Subset from Microarray Data. Journal of Biomedicine and Biotechnology. https://www.semanticscholar.org/paper/db76c2ba82c53c1eb0967c1196ae98ca75de22e5
11. L. Kuykendall, J. Shao, J. Hartung (2012). ‘Ca. Liberibacter asiaticus’ Proteins Orthologous with pSymA-Encoded Proteins of Sinorhizobium meliloti: Hypothetical Roles in Plant Host Interaction. PLoS ONE. https://www.semanticscholar.org/paper/d1903bab3348459a5230cb86962e8df123d9be22
12. Ashley Babjac, Adrienne Hoarfrost (2026). GRIMM: Genetic stRatification for Inference in Molecular Modeling. https://www.semanticscholar.org/paper/a923e3c2800f1ce4cc937015594f74395af624a9
13. Reema K. Gudhka, B. Neilan, B. Burns (2015). Adaptation, Ecology, and Evolution of the Halophilic Stromatolite Archaeon Halococcus hamelinensis Inferred through Genome Analyses. Archaea. https://www.semanticscholar.org/paper/d650f910b391d57d43d94e5305e4902735d9f51f
14. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
15. Muskan Arooj, R. Mateen, M. Javed, Muhammad Ali, Muhammad Irfan Fareed et al. (2025). Computational screening of phytochemicals targeting mutant KRAS in colorectal cancer. Scientific Reports. https://www.semanticscholar.org/paper/2e47ff33fc8e4bd8a85a3cd322f3441bb45db205
16. T. Xiang, Wei Zhou, Cailing Xu, Jing Xu, R. Liu et al. (2022). Transcriptomic Analysis Reveals Competitive Growth Advantage of Non-pigmented Serratia marcescens Mutants. Frontiers in Microbiology. https://www.semanticscholar.org/paper/cf6eabbd1224ea1e12b6239237eb38081b0951d2
17. Claudia Teso-Pérez, M. Martínez-Bueno, J. Peralta‐Sánchez, E. Valdivia, M. Maqueda et al. (2021). Enterocin Cross-Resistance Mediated by ABC Transport Systems. Microorganisms. https://www.semanticscholar.org/paper/a8d177ecdcfd8fe0c3cdf9cf0e97ecd277dd3aeb
18. M. T. Olsen, Shane Nowack, J. Wood, Eric D. Becraft, K. Labutti et al. (2015). The molecular dimension of microbial species: 3. Comparative genomics of Synechococcus strains with different light responses and in situ diel transcription patterns of associated putative ecotypes in the Mushroom Spring microbial mat. Frontiers in Microbiology. https://www.semanticscholar.org/paper/08c90ebb1e5ef5c058f332936ee7c6cf6e27919d
19. Xi-feng Fei, Xiangtong Xie, X. Ji, Haiyan Tian, F. Sun et al. (2022). Quantitative proteomic dataset of whole protein in three melanoma samples of 92.1, 92.1-A and 92.1-B. Data in Brief. https://www.semanticscholar.org/paper/33312bb6cc2cf985d32f3a31cf4fdee6b4e17385
20. Misty M. Attwood, Arunkumar Krishnan, Valentina Pivotti, Samira Yazdi, M. S. Almén et al. (2016). Topology based identification and comprehensive classification of four-transmembrane helix containing proteins (4TMs) in the human genome. BMC Genomics. https://www.semanticscholar.org/paper/268e83d5e00c4b7b210ab19c9bd873e0e50ba87e