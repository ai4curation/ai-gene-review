---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T21:17:16.884191'
end_time: '2026-07-08T21:17:23.030020'
duration_seconds: 6.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fbpA
  gene_symbol: fbpA
  uniprot_accession: Q88CI5
  protein_description: 'SubName: Full=Iron(III) iron ABC transporter, periplasmic
    iron-binding protein {ECO:0000313|EMBL:AAN70761.1};'
  gene_info: Name=fbpA {ECO:0000313|EMBL:AAN70761.1}; OrderedLocusNames=PP_5196 {ECO:0000313|EMBL:AAN70761.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial solute-binding protein 1 family.
  protein_domains: Ferric-bd. (IPR026045); SBP. (IPR006059); SBP_bac_8 (PF13416)
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
- **UniProt Accession:** Q88CI5
- **Protein Description:** SubName: Full=Iron(III) iron ABC transporter, periplasmic iron-binding protein {ECO:0000313|EMBL:AAN70761.1};
- **Gene Information:** Name=fbpA {ECO:0000313|EMBL:AAN70761.1}; OrderedLocusNames=PP_5196 {ECO:0000313|EMBL:AAN70761.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial solute-binding protein 1 family.
- **Key Domains:** Ferric-bd. (IPR026045); SBP. (IPR006059); SBP_bac_8 (PF13416)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fbpA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fbpA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fbpA** (gene ID: fbpA, UniProt: Q88CI5) in PSEPK.

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

### [1] Phylogeny and putative virulence gene analysis of Bartonella bovis
- Authors: S. Tay, K. Kho, S. Lye, Y. Ngeow
- Year: 2017
- Venue: The Journal of Veterinary Medical Science
- URL: https://www.semanticscholar.org/paper/38591b9d494453f8e363495d635019d59267129c
- DOI: 10.1292/jvms.17-0448
- PMID: 29311425
- PMCID: 5938196
- Citations: 8
- Summary: The phylogenetic trees generated from the genome-wide comparison of orthologous genes exhibited a topology almost similar to that of the tree generated from SNP-based comparison, indicating a high concordance in the nucleotide and amino acid sequences of Bartonella spp.
- Evidence snippets:
  - Snippet 1 (score: 0.794)
    > Several genes encoding protein translocation across the cytoplasmic membrane, ABC transporters, cation transporters and Uni-Sym-and Antiporters are annotated in BbUM genome (Table 2). Various components of iron acquisition metabolism including iron compound ABC uptake transporter substrate-binding proteins PiuA and PiuC, hemin transport protein HmuS, periplasmic hemin-binding protein, ABC-type hemin transport system, ATPase component, electron transfer flavoprotein, beta subunit, ferric siderophore transport system, periplasmic binding protein TonB, TonB-dependent hemin, and ferrichrome receptor are also annotated in the BbUM genome.
    > Since flagella-like structure was observed under electron microscopy (Fig. 1), the presence of flagellin gene in BbUM genome was investigated. Based on RAST analysis, 50 genes associated with flagellar motility were annotated under the motility and chemotaxis category (Table 2). The genes included flaA, flgB, flgC, flgD, flgE, flgF, flgG, flgH, flgI, flgK, flgL, flhA, flhB, fliE, fliF, fliG, fliI, fliL, fliM, fliP, fliQ, fliR, motA and motB. Additionally, the genes for flagellar protein FlgJ and flagellar hook-associated switch protein (FliN) were also annotated. Two flagellin genes (labelled as flaA sequence types 1 and 2) sharing the highest sequence similarities (60.6 and 73.0% nucleotide similarity, respectively) with that of B. bacilliformis, and 59.8 and 73.6% nucleotide similarity, respectively, with that of B. clarridgeiae, were retrieved for further analysis.

### [2] Analysis of Iron and Iron-Interacting Protein Dynamics During T-Cell Activation
- Authors: Megan R. Teh, Joe N. Frost, A. Armitage, H. Drakesmith
- Year: 2021
- Venue: Frontiers in Immunology
- URL: https://www.semanticscholar.org/paper/912bf84469a61cdc9db3bb47a2104a7bbbcfa4c5
- DOI: 10.3389/fimmu.2021.714613
- PMID: 34880854
- PMCID: 8647206
- Citations: 46
- Influential citations: 2
- Summary: This work identified iron-interacting proteins in CD4+ and CD8+ T-cell proteomes that were differentially expressed during activation, suggesting that pathways enriched with such proteins, including histone demethylation, may be impaired by iron deficiency.
- Evidence snippets:
  - Snippet 1 (score: 0.779)
    > Using the Uniprot IDs of human iron interacting proteins provided by Andreini et al, corresponding standard human gene names were identified using the Uniprot mapping tool (https://www.uniprot.org/uploadlists/) (16). To curate an equivalent list of mouse iron interacting protein homologues, the list of human iron interacting genes was input into the Ensembl BioMart tool (http://useast.ensembl.org/biomart/ martview/893cea99357a57529ab65ce92c12e306) selecting for comparison to the Ensembl Genes 100 database, Human genes (GRCh38.p13) dataset (Supplementary File 1) (17). Filtering was completed by gene name using an external reference ID list and selecting for the attributes: gene stable ID, gene name, mouse gene stable ID, mouse gene name and gene description. This method was able to identify mouse homologues for the majority of human iron interacting proteins (349/398, 88%). In cases where gene matches were not identified by Ensembl, manual verification was completed and several more matches were identified (8 proteins). Some human iron interacting proteins were found to have no mouse homologues (23 proteins, ex//KDM4E, SCD5, NOX5, etc.) or poor gene annotation limited the identification of matches (18 proteins, ex//CYP2C, FADS2P1, DKFZp686G0638). To obtain further cofactor information regarding protein to iron atom stoichiometry, the Uniprot database was manually searched using the cofactor terms: 4Fe-4S, 3Fe-3S, 2Fe-2S, heme, Fe2+, Fe3+. Retrieved cofactor information was manually added to the list of iron interacting information Notably, the iron interacting protein list does not include proteins that indirectly interact with iron such as TFRC which interacts with iron via intermediate contact with Tf. The resulting list of mouse iron interacting proteins is relatively comprehensive but likely does not include the complete set of iron interacting proteins.

### [3] The Fur-like regulatory protein MAP3773c modulates key metabolic pathways in Mycobacterium avium subsp. paratuberculosis under in-vitro iron starvation
- Authors: Sajani Thapa, Govardhan Rathnaiah, D. Zinniel, R. Barletta, J. Bannantine et al.
- Year: 2024
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/fc291356ba58778e38db3feb0c0c687b3db85b78
- DOI: 10.1038/s41598-024-59691-3
- PMID: 38637716
- PMCID: 11026511
- Citations: 2
- Summary: Pathway analysis revealed that the MAP3773c knockout has an impairment in Pan and Coenzyme A (CoA) biosynthesis pathways suggesting that the absence of those pathways likely affect overall metabolic processes and cellular functions, which have consequences on MAP survival and pathogenesis.
- Evidence snippets:
  - Snippet 1 (score: 0.773)
    > ΔMAP3773c strain upregulated genes involved in the transport of cholesterol and lipid at 30 min post-iron starvation ≥ 3.0-fold (Supplementary Information 2). A total of nine genes involved in lipid transport were identified from network analysis (Fig. 5d). MCE genes upregulated by ΔMAP3773c are MAP0765, MAP2111c, MAP2113c, MAP2114c, MAP2116c, MAP2190, MAP2191, MAP2192, and MAP2117c (ABC transporter permease) which have been proposed to play roles in lipid transport (Fig. 5d). www.nature.com/scientificreports/ ΔMAP3773c upregulated ATP-binding cassette (ABC) type metal transporters genes, MAP3774c (metal ABC transporter permease), MAP3775c (ATP-binding cassette domain-containing protein) and MAP3776c (zinc ABC transporter substrate-binding protein) at 30 min iron stress. MAP3173c (ABC type transporter, mptF) gene was also upregulated. Putative siderophore synthesis genes (MAP3743-MAP4745) were also upregulated in ΔMAP3773c at 30 min post-iron starvation. Similarly, MAP0487c, a putative zinc ABC transporter, transmembrane protein (ZnuB) was upregulated in ΔMAP3773c strain at 30 min post-iron starvation. MAP3737, a PE family protein expression was upregulated at 30 min post iron starvation in ΔMAP3773c strain. MAP3092, an iron siderophore ABC transporter substrate-binding protein (FecB) was upregulated at 30 min post-iron starvation. MAP3092 has 99% identity with FecB protein of Mycobacterium avium subsp avium, which is potentially involved in iron transport 21 .

### [4] Phase Variation in Myxococcus xanthus Yields Cells Specialized for Iron Sequestration
- Authors: K. Dziewanowska, M. Settles, Samuel S. Hunter, Ingrid Linquist, Faye D. Schilkey et al.
- Year: 2014
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/6d7d24a81c82f114458ab6480622f9fe6394a09d
- DOI: 10.1371/journal.pone.0095189
- PMID: 24733297
- PMCID: 3986340
- Citations: 14
- Summary: A consequence of phase variation is that yellow cells shift from producing antibiotic and pigment to producing components involved in acquisition of iron, which may increase fitness during periods of iron limitation.
- Evidence snippets:
  - Snippet 1 (score: 0.753)
    > The species name for M. xanthus is from the Latin word for yellow, the color of the compound DKxanthene. Loss of pigment Fig. 1. Tan strains activate pathways dedicated to acquisition of iron. Many of the genes whose expression is increased significantly in the tan strains comprise the siderophore production and transport, hemin transport, and proteins that provide energy for transport of iron-binding compounds. A partial list of components produced in tan cells is shown in this cartoon. The blue/purple circles represent the siderophore myxochelin pathway (MXAN_3639-3647) [39,40]. Myxochelin (mxc) is shown as a yellow star that binds Fe 3+ when exported. MxcNFe 3+ may be imported by a FepA-like protein (candidate is MXAN_6911; dark green shape), located in the outer membrane [41]. Light green shapes represent the ferric siderophore ABC transporter genes (permease and MXAN_0684-0687 in membrane); brown cylinders represent periplasmic energy transduction TonB proteins (MXAN_0276, MXAN0820, and 6485) that may energize the outer membrane proteins (dashed lines). Red/orange icons represent hemin transporters (MXAN_1318-1321). Not shown are RhtX/FptX siderophore transporter (MXAN_5357), iron ABC transporters (MXAN_0770-0772), iron compound ABC transporter, and a periplasmic iron compound binding protein, FeNABC (MXAN_6000). Search Tool for the Retrieval of Interacting Genes/Proteins (STRING) software [42] predicts MXAN_3639 (putative iron-chelator utilization protein in the myxochelin operon) interacts with the ferric siderophore ABC transporter permease (MXAN_0685, 0686).

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
  - Snippet 1 (score: 0.751)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [6] Complete genome sequence and analysis of Alcaligenes faecalis strain Mc250, a new potential plant bioinoculant
- Authors: É. B. Felestrino, A. B. Sanchez, W. L. Caneschi, Camila G. C. Lemes, R. A. Assis et al.
- Year: 2020
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/ac9a470bb9ade3a30a9c9bcde25e3822256cbab2
- DOI: 10.1371/journal.pone.0241546
- PMID: 33151992
- PMCID: 7643998
- Citations: 14
- Summary: The complete genome of Alcaligenes faecalis strain Mc250 (Mc250), a bacterium isolated from the roots of Mimosa calodendron, an endemic plant growing in ferruginous rupestrian grasslands in Minas Gerais State, Brazil, is presented and reveals biotechnological potential for the Mc250 strain.
- Evidence snippets:
  - Snippet 1 (score: 0.751)
    > We found 12 genes associated with siderophore biosynthesis. These genes are: ybdZ, and immediately downstream, entCEBA, followed by entS, the gene that encodes a siderophore carrier protein; fes, a gene encoding for enterobactin esterase; entF (synthesis component, serine activating enzyme); and the transport system of this compound to the medium (fepAGDCB) (S2B Fig) . Eleven genes associated with iron acquisition were also found. Among them four copies of pitADC genes (two of which are complete and in tandem), which correspond respectively to subunits of iron-binding, ATP-binding, and permease proteins of an ABC transporter system. We also found the ABC transport system of ferrichrome/iron (III) dicitrate (fhu/fec), plus a gene for the receptor for hemin (hemR), two copies of the tonB gene, which codes for a periplasmic protein involved with transport of iron-chelated siderophores, a gene coding for a protein that utilizes heme groups (hutX), and two genes coding for paraquat-inducible proteins (parAB).

### [7] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.746)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.
  - Snippet 2 (score: 0.710)
    > Protein annotations were primarily obtained from UniProt (7) and include UniProt accession, UniProt entry name, domain information and Swiss-Prot (8) comments such as function, catalytic activity, subcellular location and similarity. Accession numbers were used to link to various public databases and collect available information for each protein. From NCBI EntrezGene (8) we collected gene information, such as Gene ID, alternate names/synonyms and symbols, chromosomal mapping and cross-references to other databases.
    > The 2959 proteins comprising the LMPD protein list correspond to 2300 unique genes. We also gathered all the GO and KEGG annotations, not just the lipid-specific ones, using Gene IDs and UniProt accessions. Other protein records with sequences that are (i) identical with the ones in our list, (ii) splice variants of those or (iii) related (from the same gene/locus) were gathered using EntrezGene and an in-house generated non-redundant protein sequence database compiled from the most well-known public protein sequence databases such as Swiss-Prot, Trembl and GenBank (9).

### [8] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
- Authors: P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al.
- Year: 2011
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
- DOI: 10.1093/nar/gkr1122
- PMID: 22135298
- PMCID: 3245126
- Citations: 1606
- Influential citations: 155
- Summary: PhosphoSitePlus (http://www.phosphosite.org) is an open, comprehensive, manually curated and interactive resource for studying experimentally observed post-translational modifications, primarily of human and mouse proteins. It encompasses 1 30 000 non-redundant modification sites, primarily phosphorylation, ubiquitinylation and acetylation. The interface is designed for clarity and ease of navigation. From the home page, users can launch simple or complex searches and browse high-throughput d...
- Evidence snippets:
  - Snippet 1 (score: 0.743)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [9] MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis
- Authors: Xiaohua Jiang, Daren Zhao, Asim Ali, Bo Xu, Wei Liu et al.
- Year: 2021
- Venue: Frontiers in Cell and Developmental Biology
- URL: https://www.semanticscholar.org/paper/aeb08368a5540685473578345739bb569103bd46
- DOI: 10.3389/fcell.2021.673073
- PMID: 34485275
- PMCID: 8415030
- Citations: 6
- Summary: The developed MeiosisOnline provides the most updated and detailed information of experimental verified and predicted genes in meiosis, and will greatly help researchers in studying meiosis in an easy and efficient way.
- Evidence snippets:
  - Snippet 1 (score: 0.742)
    > Annotation information for each gene in MeiosisOnline contains "basic information, " "function annotation and classification, " "protein-protein interaction (PPI) and gene expression."
    > (1) Basic information: gene name/synonyms, nucleotide sequences, etc., were extracted from GenBank3 and UniProt Knowledgebase.4 (2) Function annotation and classification: detailed functional information is also manually collected from literature reports. (i) Which meiotic stage is the gene involved? (ii) Did the gene function in one sex or both sexes? (iii) Whether deletion or mutation of the gene in model organism has a phenotype in fertility? (iv) Which protein complex of the gene is involved? (v) The cellular location and expression pattern in tissues or cell lines.
    > (vi) Experimental methods used for functional analysis.
    > (vii) The information of related literature and figures for illustrating the function of protein/gene. (viii) Gene ontology annotation for collected genes.
    > (3) Protein-protein interaction and gene expression: both verified and predicted PPI information were provided. Gene expression pattern in reproductive system was also provided graphically.

### [10] Analysis of the Global Ocean Sampling (GOS) Project for Trends in Iron Uptake by Surface Ocean Microbes
- Authors: E. Toulza, A. Tagliabue, S. Blain, G. Piganeau
- Year: 2012
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/ef1537c5ee75f378034c8891dd1253ef40fbd488
- DOI: 10.1371/journal.pone.0030931
- PMID: 22363520
- PMCID: 3281889
- Citations: 79
- Influential citations: 3
- Summary: A database of 2319 sequences, corresponding to 140 gene families of iron metabolism with a large phylogenetic spread, is built to explore the microbial strategies of iron acquisition in the ocean's bacterial community, showing significant quantitative and qualitative variations in iron metabolism pathways.
- Evidence snippets:
  - Snippet 1 (score: 0.742)
    > We selected genes involved in iron metabolisms from the literature in cases where the protein product had been characterized or where the function of the protein could be inferred by sequence analysis. In this way, we identified 140 genes specifically involved in iron metabolism. We assigned these genes to 10 ironrelated metabolic pathways, summarized in Table 1. A maximal phylogenetic coverage for each gene was achieved by retrieving all available bacterial sequences using the NCBI search tool with the gene names as a query. All 9917 annotations and protein sequences were manually inspected to discard irrelevant or incomplete protein sequences. To discard redundant sequences from the same genus, we randomly selected one full-size sequence per gene per available genus, resulting in 1753 remaining sequences. Additionally, we screened the annotations of the protein sequences from the Moore Microbial Genome database (marine bacteria isolates) for genes involved in iron metabolism (http://www.moore.org/microgenome/) and retrieved 566 genes. After manual inspection of these sequences, 191 putative ABC iron transporters could not be assigned to any one of the previous pathways, and therefore constituted the unspecified iron transport category (TR). We thus obtained a dataset of 2319 sequences belonging to 11 phyla (Actinobacteria, alphaproteobacteria, Bacteroidetes, betaproteobacteria, Cyanobacteria, deltaproteobacteria, Deinococcus-thermus, Firmicutes, gammaproteobacteria, Spirochetes, epsilonproteobacteria) (Table S1). The 140 gene families with at least two sequences were aligned and processed to estimate an identity and coverage threshold within each gene family. These thresholds estimations are needed because many proteins involved in different pathways could share sequence similarities, like ABC transporters of different iron-related pathways. We found that 65% amino-acid identity over a minimum length of 100 amino acids (or 80% of query length coverage) corresponded to 96% of correct orthologous gene assignment and 100% of correct pathway assignment (Table S2). Our criteria are stringent and we therefore probably underestimated the number of matches, but this enables a robust analysis of the different proportion of each iron-related pathway between sites.

### [11] Iron-dependent gene expression in Actinomyces oris
- Authors: Matthew P. Mulè, D. Giacalone, Kayla Lawlor, A. Golden, C. Cook et al.
- Year: 2015
- Venue: Journal of Oral Microbiology
- URL: https://www.semanticscholar.org/paper/511fb8327ad6a1f9275b289753acc48e3f630253
- DOI: 10.3402/jom.v7.29800
- PMID: 26685151
- PMCID: 4684579
- Citations: 4
- Summary: Clinical isolates of Actinomyces spp.
- Evidence snippets:
  - Snippet 1 (score: 0.737)
    > We identified genes that were likely to be involved in iron acquisition by examining the genome of A. oris, which is available via the Bioinformatics Resources for Oral Pathogens (BROP). At the time of this publication, BROP refers to A. oris MG1 as A. naeslundii MG1.
    > As outlined here, sequence analyses revealed that there are over a dozen genes that may be involved in iron acquisition. Two of these genes identified, fetA and sidD, are located in operons with a high degree of sequence similarity (!98%) to transporters involved in iron uptake (Fig. 2). The sidC gene encodes a predicted 37 kDa, ironÁ siderophore ABC transporter substrate-binding protein, whose periplasmic component is 99% identical to ironÁ siderophore ABC transporter substrate-binding protein from A. viscosus. The sidD gene likely encodes the ironÁ siderophore ATP-binding protein of the ABC transporter component containing an ATP-binding site and the ABC transporter signature motif. The SidD protein is 95% identical to the iron dicitrate ABC transporter ATPbinding protein from A. viscosus (accession number WP_009406982.1; Fig. 2a). The first gene in the fetA (anae_c_1_8278) operon encodes a predicted 32 kDa protein with 98% identity and 99% similarity to a predicted A. oris high-affinity iron transporter (accession number WP_010612841.1; Fig. 2b) with 65% identity and 78% similarity to predicted ferrous iron permease EfeU from Propionibacterium acidipropionici ATCC 4875 (accession number 0WP_015071892.1). The second gene in the operon fetB (anae_c_1_8283) encodes a 46.8 kDa protein with 99% similarity and 99% identity to a predicted peptidase M75 from A. oris.

### [12] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.730)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [13] Tn6553, a Tn7-family transposon encoding putative iron uptake functions found in Acinetobacter
- Authors: Mehrad Hamidian
- Year: 2022
- Venue: Archives of Microbiology
- URL: https://www.semanticscholar.org/paper/6d6f853f0140f0a7fa3cc147e7b80ea7ea112793
- DOI: 10.1007/s00203-022-03291-0
- PMID: 36289115
- PMCID: 9605922
- Citations: 1
- Summary: Another Tn7-type transposon (named Tn6553) is described, which contains a set of iron utilisation genes with a transposition module related to Tn 7 and is important in the context of dissemination of virulence genes amongst Acinetobacter strains.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > Tn6553 encodes a set of functions required for iron uptake. It contains several genes such as irtAB, bauD-CEBA and fur, which mainly encode proteins predicted to be involved in ferrichrome uptake and transmembrane transport (Fig. 1a), which are distantly related to Escherichia coli ferrichrome-iron receptor (Coulton et al. 1983). The irtAB genes encode putative ABC-type multidrug transport systems (ATPase and permease component) belonging to the MdiB superfamily (Protein family accession number COG1132). The bauDCE genes encode putative iron chelate uptake ABC transporter family permease subunit (ferric acinetobactin ABC transporter), while bauB predicted to encode a siderophore-binding periplasmic lipoprotein and bauA a TonB-dependent siderophore protein (Fig. 1a). Tn6553 also carries a fur gene encoding an Fe2 + (or Zn2 +) uptake transcriptional regulation protein (Protein family accession number COG0732), which is in fact a putative master transcriptional regulator of the ironresponsive genes. Notably, the iron uptake proteins encoded by Tn6553 are distantly related to the siderophore systems (with amino acid identities ranging from 20-30%) that we recently described in A. baumannii in different Tn7-family transposons (Hamidian and Hall 2021). However, whether this operon functions as a siderophore system remains to be experimentally examined.
    > A recent study reported that A. baumannii DS002 (Gen-Bank accession number CP027704.2) contains a novel siderophore system present in a genomic island that encodes 30 genes/orfs including four (n = 4) genes encoding putative transposases TnsBC1C2E, 13 gene encoding putative iron acquisition functions, and the 13 reading frames coding for proteins of unknown functions (Yakkala et al. 2019).

### [14] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.724)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [15] Characterization of a novel root-associated diazotrophic rare PGPR taxa, Aquabacter pokkalii sp. nov., isolated from pokkali rice: new insights into the plant-associated lifestyle and brackish adaptation
- Authors: V. S. Sunithakumari, Rahul Ravikumar Menon, Gayathri G. Suresh, R. Krishnan, N. Rameshkumar
- Year: 2024
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/7b6d113f0e2717352b20e31091b586b3ec2f0753
- DOI: 10.1186/s12864-024-10332-z
- PMID: 38684959
- PMCID: 11059613
- Citations: 4
- Summary: A better understanding is provided of a marine-adapted PGPR strain L1I39^T that may perform a substantial role in host growth and health in nitrogen-poor brackish environments.
- Evidence snippets:
  - Snippet 1 (score: 0.722)
    > In addition to examining the genome for sulfur and phosphate assimilation, we also identified several potential genes involved in the assimilation of nitrogen, including genes coding for ammonium transporters, reductases for nitrate and nitrite, regulators that sense nitrogen status, glutamate dehydrogenase, and a functional glutamine synthetase/glutamate synthase (GS/GOGAT) system as listed in (Table S18). In addition, the L1I39 T genome possesses genes coding for the uptake and hydrolysis of urea, including a urease operon (ureABCEFGD) and the urea transport systems (urtEDC and urtBA) and a functional urea carboxylase/allophanate hydrolyase pathway, suggesting its ability to degrade urea into ammonia (Table S19).
    > Iron acquisition The L1I39 T genome lacks genes that participate in the biosynthesis and secretion of siderophores. In support, we experimentally prove that L1I39 T is negative for siderophore production (data not shown). However, the L1I39 T contains dedicated transport systems to capture and uptake external iron, including TonB-dependent siderophore receptor proteins, siderophore-interacting proteins, iron ABC transport substrate-binding proteins, iron ABC transport permease, iron ABC transport ATP-binding proteins, ferric hydroxamate ABC transport permease (fhuB), and siderophoreiron reductase (fhuF). Importantly, these genes are organized into different gene clusters (Table S20).
    > Further investigations revealed genes encoding for ferrochelatase (hemH), TonB-dependent hemoglobin/transferrin/lactoferrin family proteins, biliverdin-producing heme oxygenase, heme ABC transporter-ATP binding protein, and hemin uptake protein (hemP), responsible for acquiring host iron. Also, genes coding for iron storage proteins that include ferritin, bacterioferritin (bfr), and two copies of ferritin-like domain-containing proteins and fur-type iron response transcriptional regulator (three copies) were present.

### [16] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.722)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [17] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.714)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [18] Microbial iron management mechanisms in extremely acidic environments: comparative genomics evidence for diversity and versatility
- Authors: H. Osorio, Verónica Martínez, Pamela A. Nieto, D. Holmes, Raquel Quatrini
- Year: 2008
- Venue: BMC Microbiology
- URL: https://www.semanticscholar.org/paper/6205c573e90929f186c4d6f1eead426d238e53f8
- DOI: 10.1186/1471-2180-8-203
- PMID: 19025650
- PMCID: 2631029
- Citations: 60
- Influential citations: 3
- Summary: Silico analyses of the genomes of acidophilic bacteria are beginning to tease apart the mechanisms that mediate iron uptake and homeostasis in low pH environments, and initial models pinpoint significant differences in abundance and diversity of iron management mechanisms between Leptospirilla and Acidithiobacilli.
- Evidence snippets:
  - Snippet 1 (score: 0.714)
    > Taxonomically restricted genes are of special interest because they are expected to play a role in defining exclusive ecological adaptations to particular niches [44]. We predict a genomic island containing a gene cluster associated with iron metabolism in A. ferrooxidans that may be an exclusive system of physiological/ecological significance for the bioleaching consortia. The FepA2-FecA4 TonB-dependent Fe(III) transport system comprises a 13 gene cluster (Figure 7) that resides within a predicted genomic island containing 69 genes that is absent from the genomes of A. thiooxidans and A. caldus. The predicted protein products encoded by the 13 gene cluster include two OMRs with different predicted siderophore affinity, a TonB system and two contiguous partially complete high affinity metal ABC transporter systems (Figure 7, Additional file 1). These two ABC transporters include three high affinity periplasmic solute-binding proteins that differ in size, sequence and ligand specificity (Figure 7). Two of these have predicted affinity for Fe(III) siderophores and one for molybdate. The most similar orthologs to the Mo-binding protein of A. ferrooxidans are found in several nitrogen-fixing bacteria. Interestingly, nitrogen fixation is performed by an enzymatic complex made up of a Fe/Moprotein (the dinitrogenase) and a Fe-protein (the dinitrogenase reductase) [45]. The association of a gene predicted to encode ModA-like periplasmic binding protein with affinity for molybdate with genes predicted to be involved in siderophore uptake suggests that the gene cluster might be a bifunctional ABC transporter system, destined to cover the requirements of both Fe and Mo essential metabolic cofactors.
    > Adjacent to the proposed 13 gene Fe-Mo transport cluster is a region of 44 genes predicted to be involved in nitrogen fixation including the full set of nif genes required for nitrogenase assembly and maturation [13].

### [19] Tell me if you prefer bovine or poultry sectors and I’ll tell you who you are: Characterization of Salmonella enterica subsp. enterica serovar Mbandaka in France
- Authors: Madeleine De sousa Violante, V. Michel, Karol Romero, L. Bonifait, L. Baugé et al.
- Year: 2023
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/070b499b75818eb8ebbc0dc765efdf2c3cca932c
- DOI: 10.3389/fmicb.2023.1130891
- PMID: 37089562
- PMCID: 10116068
- Citations: 8
- Summary: All strains present resistance determinants including heavy metals and biocides that could explain the ability of this serovar to survive and persist in the environment, within herds, and in food processing plants.
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > The Salmonella iron transporter gene cluster sitABCD, coding for a periplasmic ATP-binding-protein, previously identified in S. Typhimurium (Kehres et al., 2002) was also identified in all genomes. Interestingly, in line with iron cytoplasm starvation, the entB gene coding for the Escherichia coli catecholate siderophore enterobactin (Pakarian and Pawelek, 2016) was identified in all genomes with 80% identity (data not showed), such as the fepCG genes that code for ferric enterobactin transport ATP-binding proteins.
    > Several heavy metal resistance genes were identified. Genes implied in cobalt/magnesium resistance (corABCD), gold resistance (gesABC and golST), arsenic (pstB), and copper (cuiD and cueP) resistances were found in all genomes. The merCRT genes implied in mercury resistance were also found in only one strain isolated from poultry (S18LNR1211). This last strain also presents the tetracycline, sulphonamide, and aminoglycoside resistance genes tetAB, sul1, and ant3-D, ' respectively (Supplementary Table 2, "MEGAResV2" tab).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. S. Tay, K. Kho, S. Lye, Y. Ngeow (2017). Phylogeny and putative virulence gene analysis of Bartonella bovis. The Journal of Veterinary Medical Science. https://www.semanticscholar.org/paper/38591b9d494453f8e363495d635019d59267129c
2. Megan R. Teh, Joe N. Frost, A. Armitage, H. Drakesmith (2021). Analysis of Iron and Iron-Interacting Protein Dynamics During T-Cell Activation. Frontiers in Immunology. https://www.semanticscholar.org/paper/912bf84469a61cdc9db3bb47a2104a7bbbcfa4c5
3. Sajani Thapa, Govardhan Rathnaiah, D. Zinniel, R. Barletta, J. Bannantine et al. (2024). The Fur-like regulatory protein MAP3773c modulates key metabolic pathways in Mycobacterium avium subsp. paratuberculosis under in-vitro iron starvation. Scientific Reports. https://www.semanticscholar.org/paper/fc291356ba58778e38db3feb0c0c687b3db85b78
4. K. Dziewanowska, M. Settles, Samuel S. Hunter, Ingrid Linquist, Faye D. Schilkey et al. (2014). Phase Variation in Myxococcus xanthus Yields Cells Specialized for Iron Sequestration. PLoS ONE. https://www.semanticscholar.org/paper/6d7d24a81c82f114458ab6480622f9fe6394a09d
5. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
6. É. B. Felestrino, A. B. Sanchez, W. L. Caneschi, Camila G. C. Lemes, R. A. Assis et al. (2020). Complete genome sequence and analysis of Alcaligenes faecalis strain Mc250, a new potential plant bioinoculant. PLoS ONE. https://www.semanticscholar.org/paper/ac9a470bb9ade3a30a9c9bcde25e3822256cbab2
7. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
8. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
9. Xiaohua Jiang, Daren Zhao, Asim Ali, Bo Xu, Wei Liu et al. (2021). MeiosisOnline: A Manually Curated Database for Tracking and Predicting Genes Associated With Meiosis. Frontiers in Cell and Developmental Biology. https://www.semanticscholar.org/paper/aeb08368a5540685473578345739bb569103bd46
10. E. Toulza, A. Tagliabue, S. Blain, G. Piganeau (2012). Analysis of the Global Ocean Sampling (GOS) Project for Trends in Iron Uptake by Surface Ocean Microbes. PLoS ONE. https://www.semanticscholar.org/paper/ef1537c5ee75f378034c8891dd1253ef40fbd488
11. Matthew P. Mulè, D. Giacalone, Kayla Lawlor, A. Golden, C. Cook et al. (2015). Iron-dependent gene expression in Actinomyces oris. Journal of Oral Microbiology. https://www.semanticscholar.org/paper/511fb8327ad6a1f9275b289753acc48e3f630253
12. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
13. Mehrad Hamidian (2022). Tn6553, a Tn7-family transposon encoding putative iron uptake functions found in Acinetobacter. Archives of Microbiology. https://www.semanticscholar.org/paper/6d6f853f0140f0a7fa3cc147e7b80ea7ea112793
14. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
15. V. S. Sunithakumari, Rahul Ravikumar Menon, Gayathri G. Suresh, R. Krishnan, N. Rameshkumar (2024). Characterization of a novel root-associated diazotrophic rare PGPR taxa, Aquabacter pokkalii sp. nov., isolated from pokkali rice: new insights into the plant-associated lifestyle and brackish adaptation. BMC Genomics. https://www.semanticscholar.org/paper/7b6d113f0e2717352b20e31091b586b3ec2f0753
16. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
17. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
18. H. Osorio, Verónica Martínez, Pamela A. Nieto, D. Holmes, Raquel Quatrini (2008). Microbial iron management mechanisms in extremely acidic environments: comparative genomics evidence for diversity and versatility. BMC Microbiology. https://www.semanticscholar.org/paper/6205c573e90929f186c4d6f1eead426d238e53f8
19. Madeleine De sousa Violante, V. Michel, Karol Romero, L. Bonifait, L. Baugé et al. (2023). Tell me if you prefer bovine or poultry sectors and I’ll tell you who you are: Characterization of Salmonella enterica subsp. enterica serovar Mbandaka in France. Frontiers in Microbiology. https://www.semanticscholar.org/paper/070b499b75818eb8ebbc0dc765efdf2c3cca932c