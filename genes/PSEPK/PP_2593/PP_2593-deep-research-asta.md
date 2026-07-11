---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T22:54:10.454880'
end_time: '2026-07-10T22:54:15.131344'
duration_seconds: 4.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2593
  gene_symbol: PP_2593
  uniprot_accession: Q88JQ6
  protein_description: 'SubName: Full=Ferric siderophore ABC transporter, permease
    protein {ECO:0000313|EMBL:AAN68201.1};'
  gene_info: OrderedLocusNames=PP_2593 {ECO:0000313|EMBL:AAN68201.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the binding-protein-dependent transport system
  protein_domains: ABC_BtuC-like. (IPR037294); ABC_transptr_permease_BtuC. (IPR000522);
    FecCD (PF01032)
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
- **UniProt Accession:** Q88JQ6
- **Protein Description:** SubName: Full=Ferric siderophore ABC transporter, permease protein {ECO:0000313|EMBL:AAN68201.1};
- **Gene Information:** OrderedLocusNames=PP_2593 {ECO:0000313|EMBL:AAN68201.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the binding-protein-dependent transport system
- **Key Domains:** ABC_BtuC-like. (IPR037294); ABC_transptr_permease_BtuC. (IPR000522); FecCD (PF01032)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2593" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2593' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2593** (gene ID: PP_2593, UniProt: Q88JQ6) in PSEPK.

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
  - Snippet 1 (score: 0.790)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.690)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.750)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

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
  - Snippet 1 (score: 0.746)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [4] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.738)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [5] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.727)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [6] The Fur-like regulatory protein MAP3773c modulates key metabolic pathways in Mycobacterium avium subsp. paratuberculosis under in-vitro iron starvation
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
  - Snippet 1 (score: 0.727)
    > ΔMAP3773c strain upregulated genes involved in the transport of cholesterol and lipid at 30 min post-iron starvation ≥ 3.0-fold (Supplementary Information 2). A total of nine genes involved in lipid transport were identified from network analysis (Fig. 5d). MCE genes upregulated by ΔMAP3773c are MAP0765, MAP2111c, MAP2113c, MAP2114c, MAP2116c, MAP2190, MAP2191, MAP2192, and MAP2117c (ABC transporter permease) which have been proposed to play roles in lipid transport (Fig. 5d). www.nature.com/scientificreports/ ΔMAP3773c upregulated ATP-binding cassette (ABC) type metal transporters genes, MAP3774c (metal ABC transporter permease), MAP3775c (ATP-binding cassette domain-containing protein) and MAP3776c (zinc ABC transporter substrate-binding protein) at 30 min iron stress. MAP3173c (ABC type transporter, mptF) gene was also upregulated. Putative siderophore synthesis genes (MAP3743-MAP4745) were also upregulated in ΔMAP3773c at 30 min post-iron starvation. Similarly, MAP0487c, a putative zinc ABC transporter, transmembrane protein (ZnuB) was upregulated in ΔMAP3773c strain at 30 min post-iron starvation. MAP3737, a PE family protein expression was upregulated at 30 min post iron starvation in ΔMAP3773c strain. MAP3092, an iron siderophore ABC transporter substrate-binding protein (FecB) was upregulated at 30 min post-iron starvation. MAP3092 has 99% identity with FecB protein of Mycobacterium avium subsp avium, which is potentially involved in iron transport 21 .

### [7] Tn6553, a Tn7-family transposon encoding putative iron uptake functions found in Acinetobacter
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
  - Snippet 1 (score: 0.720)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [9] The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism
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
  - Snippet 1 (score: 0.717)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [10] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.715)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [11] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.714)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [12] Extracytoplasmic Function Sigma Factors Governing Production of the Primary Siderophores in Pathogenic Burkholderia Species
- Authors: A. Grove
- Year: 2022
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/a2ff8b48b76b9acc26e76590d4c3ad855a7bfcc9
- DOI: 10.3389/fmicb.2022.851011
- PMID: 35283809
- PMCID: 8908255
- Citations: 11
- Summary: Interference with siderophore-mediated iron acquisition is important for virulence, and interference with this process constitutes a viable approach to the treatment of bacterial infections.
- Evidence snippets:
  - Snippet 1 (score: 0.705)
    > A divergently encoded gene for a hypothetical protein (white) is followed by the gene encoding the cytoplasmic ABC permease (BTH_I2419; red). Two genes encoding NRPSs (gray) are in an operon, which also includes a modifying enzyme (gray), a TonB-dependent receptor (BTH_I2415; green), and another modifying enzyme (gray); this operon was experimentally verified in Burkholderia pseudomallei (Alice et al., 2006).
    > are usually encoded on the larger chromosome. Genes contained within these clusters encode two NRPSs as well as several modifying enzymes (Figure 1B; gray), an ABC transporter implicated in export of siderophores (red), and a set of proteins dedicated to uptake of iron-siderophore complexes. The latter comprise a TonB-dependent outer membrane receptor (green), a periplasmic binding protein (purple), and a cytoplasmic ABC transporter (light blue). The first gene in the clusters encodes an ECF σ factor referred to as MbaS (for malleobactin sigma) in B. pseudomallei and OrbS (for ornibactin sigma) in B. cenocepacia (Agnoli et al., 2006;Alice et al., 2006). Notably, none of the adjacent genes are predicted to encode an anti-σ factor.

### [13] Analysis of Iron and Iron-Interacting Protein Dynamics During T-Cell Activation
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
  - Snippet 1 (score: 0.698)
    > Using the Uniprot IDs of human iron interacting proteins provided by Andreini et al, corresponding standard human gene names were identified using the Uniprot mapping tool (https://www.uniprot.org/uploadlists/) (16). To curate an equivalent list of mouse iron interacting protein homologues, the list of human iron interacting genes was input into the Ensembl BioMart tool (http://useast.ensembl.org/biomart/ martview/893cea99357a57529ab65ce92c12e306) selecting for comparison to the Ensembl Genes 100 database, Human genes (GRCh38.p13) dataset (Supplementary File 1) (17). Filtering was completed by gene name using an external reference ID list and selecting for the attributes: gene stable ID, gene name, mouse gene stable ID, mouse gene name and gene description. This method was able to identify mouse homologues for the majority of human iron interacting proteins (349/398, 88%). In cases where gene matches were not identified by Ensembl, manual verification was completed and several more matches were identified (8 proteins). Some human iron interacting proteins were found to have no mouse homologues (23 proteins, ex//KDM4E, SCD5, NOX5, etc.) or poor gene annotation limited the identification of matches (18 proteins, ex//CYP2C, FADS2P1, DKFZp686G0638). To obtain further cofactor information regarding protein to iron atom stoichiometry, the Uniprot database was manually searched using the cofactor terms: 4Fe-4S, 3Fe-3S, 2Fe-2S, heme, Fe2+, Fe3+. Retrieved cofactor information was manually added to the list of iron interacting information Notably, the iron interacting protein list does not include proteins that indirectly interact with iron such as TFRC which interacts with iron via intermediate contact with Tf. The resulting list of mouse iron interacting proteins is relatively comprehensive but likely does not include the complete set of iron interacting proteins.

### [14] Deep Annotation of Protein Function across Diverse Bacteria from Mutant Phenotypes
- Authors: M. Price, Kelly M. Wetmore, R. J. Waters, Mark Callaghan, J. Ray et al.
- Year: 2016
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/b8766e12e04d726ab4f4a5d1c7e2a12d9ea2a64d
- DOI: 10.1101/072470
- Citations: 28
- Influential citations: 1
- Summary: This study demonstrates the utility and scalability of high-throughput genetics for large-scale annotation of bacterial proteins and provides a vast compendium of experimentally-determined protein functions across diverse bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > (2) "Hypothetical" includes proteins containing the annotation description "hypothetical protein", "unknown function", "uncharacterized", or if the entire description matched "TIGRnnnnn family protein" or "membrane protein". (3) Proteins were considered to have "vague" annotations if the gene description contained "family", "domain protein", "related protein", "transporter related", or if the entire description matched common non-specific annotations ("abc transporter atp-binding protein", "abc transporter permease", "abc transporter substrate-binding protein", "abc transporter", "acetyltransferase", "alpha/beta hydrolase", "aminohydrolase", "aminotransferase", "atpase", "dehydrogenase", "dna-binding protein", "fad-dependent oxidoreductase", "gcn5-related n-acetyltransferase", "histidine kinase", "hydrolase" "lipoprotein", "membrane protein", "methyltransferase", "mfs transporter", "oxidoreductase", "permease", "porin", "predicted dna-binding transcriptional regulator", "predicted membrane protein", "probable transmembrane protein", "putative membrane protein", "response regulator receiver protein", "rnd transporter", "sam-dependent methyltransferase", "sensor histidine kinase", "serine/threonine protein kinase", "signal peptide protein", "signal transduction histidine kinase", "tonb-dependent receptor", "transcriptional regulator", "transcriptional regulators", or "transporter"). The remaining proteins were considered to have "other detailed" annotations. To identify a subset of the proteins annotated as "hypothetical" or "vague" that do not belong to any characterized families, we relied on Pfam and TIGRFAM.

### [15] Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae
- Authors: Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli
- Year: 2021
- Venue: BMC Research Notes
- URL: https://www.semanticscholar.org/paper/4f78acee7559d5e406bacad91d5982d9f3244ea3
- DOI: 10.1186/s13104-021-05856-6
- PMID: 34823574
- PMCID: 8620141
- Citations: 10
- Summary: To identify candidate genes likely involved in complementation of mef( A) deletion, the Mef(A) amino acid sequence was used as probe for database searching and identified 3 putative candidates in the S. pneumoniae R6 genome, namely spr0971, spr1023 and spr1932.
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > The 405-aa Mef(A) sequence (GenBank accession no. AAT72347) was used as a query to conduct a BLAST homology search of S. pneumoniae R6 genome. Homology analysis revealed the presence of three genes coding for proteins with a significant homology (e-value < 0.001) to Mef(A): (i) spr0971 (GenBank accession number NP_ 358565.1); (ii) spr1023 (GenBank accession number NP_ 358617.1); (iii) spr1932 (GenBank accession number NP_ 359523.1). The spr0971 gene, annotated as "ABC transporter membrane-spanning permease-macrolide efflux", codes for a 403 aa protein displaying 23% identity to Mef(A). The spr1023 gene, annotated as "macrolide ABC transporter permease", codes for a 392 aa protein with 24% identity to Mef(A). The spr1932 gene, annotated as "hypothetical protein", codes for a 415 aa protein with 21% identity to Mef(A). Analysis of the transmembrane domains of all deduced amino acid products predicted the presence of up to 12 transmembrane helices.

### [16] Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae
- Authors: Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli
- Year: 2021
- Venue: BMC Research Notes
- URL: https://www.semanticscholar.org/paper/f30df2b539544c70ac0c1f373b0235d4e92d7687
- DOI: 10.1186/s13104-021-05856-6
- Summary: In streptococci, the type M resistance to macrolides is due to the mef(A)–msr(D) efflux transport system of the ATP-Binding cassette (ABC) superfamily, where it is proposed that mef(A) codes for the transmembrane channel and msr(D) for the two ATP-binding domains. Phage ϕ1207.3 of Streptococcus pyogenes, carrying the mef(A)–msr(D) gene pair, is able to transfer the macrolide efflux phenotype to Streptococcus pneumoniae. Deletion of mef(A) in pneumococcal ϕ1207.3-carrying strains did not affec...
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > The 405-aa Mef(A) sequence (GenBank accession no. AAT72347) was used as a query to conduct a BLAST homology search of S. pneumoniae R6 genome. Homology analysis revealed the presence of three genes coding for proteins with a significant homology (e-value < 0.001) to Mef(A): (i) spr0971 (GenBank accession number NP_ 358565.1); (ii) spr1023 (GenBank accession number NP_ 358617.1); (iii) spr1932 (GenBank accession number NP_ 359523.1). The spr0971 gene, annotated as "ABC transporter membrane-spanning permease-macrolide efflux", codes for a 403 aa protein displaying 23% identity to Mef(A). The spr1023 gene, annotated as "macrolide ABC transporter permease", codes for a 392 aa protein with 24% identity to Mef(A). The spr1932 gene, annotated as "hypothetical protein", codes for a 415 aa protein with 21% identity to Mef(A). Analysis of the transmembrane domains of all deduced amino acid products predicted the presence of up to 12 transmembrane helices.

### [17] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
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
  - Snippet 1 (score: 0.696)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

### [18] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.693)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [19] Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser
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
  - Snippet 1 (score: 0.692)
    > In the mouse, rat and human genomes, there are approximately twice as many synonyms (aliases) as official symbols. This large number of obsolete gene symbols leads to the problem with unequivocal identification of genes in the literature data because some synonyms can be attributed to more than one current official symbol of protein-coding genes. The ambiguity of symbols may lead to misidentification of 10% of rodent genes and even 18% of human protein-coding genes. Such misidentifications are most likely in case of literature data retrieved from older studies using past versions of gene nomenclature with a large number of obsolete symbols. A simple solution for this problem is usage of stable gene IDs (Table 2) for the unequivocal identification of genes, provided that the genomic information associated with these IDs is retrieved directly from proprietary databases containing the most accurate data. The usage of stable identifiers is important not only for accurate interpretation of literature data but also for currently published datasets because neither the annotation of genomes nor the understanding of gene function are complete.
    > This incompleteness means that official gene symbols will change over time. Data based only on gene symbols should be used cautiously to avoid misidentification of genes. A solution for this problem is our R script that updates gene symbols and provides annotation about their unique or ambiguous character.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
5. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
6. Sajani Thapa, Govardhan Rathnaiah, D. Zinniel, R. Barletta, J. Bannantine et al. (2024). The Fur-like regulatory protein MAP3773c modulates key metabolic pathways in Mycobacterium avium subsp. paratuberculosis under in-vitro iron starvation. Scientific Reports. https://www.semanticscholar.org/paper/fc291356ba58778e38db3feb0c0c687b3db85b78
7. Mehrad Hamidian (2022). Tn6553, a Tn7-family transposon encoding putative iron uptake functions found in Acinetobacter. Archives of Microbiology. https://www.semanticscholar.org/paper/6d6f853f0140f0a7fa3cc147e7b80ea7ea112793
8. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
9. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
10. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
11. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
12. A. Grove (2022). Extracytoplasmic Function Sigma Factors Governing Production of the Primary Siderophores in Pathogenic Burkholderia Species. Frontiers in Microbiology. https://www.semanticscholar.org/paper/a2ff8b48b76b9acc26e76590d4c3ad855a7bfcc9
13. Megan R. Teh, Joe N. Frost, A. Armitage, H. Drakesmith (2021). Analysis of Iron and Iron-Interacting Protein Dynamics During T-Cell Activation. Frontiers in Immunology. https://www.semanticscholar.org/paper/912bf84469a61cdc9db3bb47a2104a7bbbcfa4c5
14. M. Price, Kelly M. Wetmore, R. J. Waters, Mark Callaghan, J. Ray et al. (2016). Deep Annotation of Protein Function across Diverse Bacteria from Mutant Phenotypes. bioRxiv. https://www.semanticscholar.org/paper/b8766e12e04d726ab4f4a5d1c7e2a12d9ea2a64d
15. Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli (2021). Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae. BMC Research Notes. https://www.semanticscholar.org/paper/4f78acee7559d5e406bacad91d5982d9f3244ea3
16. Valeria Fox, Francesco Santoro, G. Pozzi, F. Iannelli (2021). Predicted transmembrane proteins with homology to Mef(A) are not responsible for complementing mef(A) deletion in the mef(A)–msr(D) macrolide efflux system in Streptococcus pneumoniae. BMC Research Notes. https://www.semanticscholar.org/paper/f30df2b539544c70ac0c1f373b0235d4e92d7687
17. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
18. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
19. Grzegorz R. Juszczak, C. Pareek, U. Czarnik, M. Pierzchała (2025). Protein-coding genes in humans and model mammals (mouse, rat and pig): gene identifiers and disambiguation of gene nomenclature retrieved from the Ensembl genome browser. BMC Genomics. https://www.semanticscholar.org/paper/d9089dfc889d790deb49cbc5b4617bda55bcc4da