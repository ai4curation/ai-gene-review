---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-08T14:58:26.111353'
end_time: '2026-07-08T14:58:31.658622'
duration_seconds: 5.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rbsB
  gene_symbol: rbsB
  uniprot_accession: Q88K38
  protein_description: 'SubName: Full=Ribose ABC transporter, periplasmic ribose-binding
    subunit {ECO:0000313|EMBL:AAN68066.1};'
  gene_info: Name=rbsB {ECO:0000313|EMBL:AAN68066.1}; OrderedLocusNames=PP_2454 {ECO:0000313|EMBL:AAN68066.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial solute-binding protein 2 family.
  protein_domains: Peripla_BP_I. (IPR028082); SBP_2_dom. (IPR025997); Peripla_BP_4
    (PF13407)
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
- **UniProt Accession:** Q88K38
- **Protein Description:** SubName: Full=Ribose ABC transporter, periplasmic ribose-binding subunit {ECO:0000313|EMBL:AAN68066.1};
- **Gene Information:** Name=rbsB {ECO:0000313|EMBL:AAN68066.1}; OrderedLocusNames=PP_2454 {ECO:0000313|EMBL:AAN68066.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial solute-binding protein 2 family.
- **Key Domains:** Peripla_BP_I. (IPR028082); SBP_2_dom. (IPR025997); Peripla_BP_4 (PF13407)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rbsB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rbsB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rbsB** (gene ID: rbsB, UniProt: Q88K38) in PSEPK.

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
  - Snippet 1 (score: 0.775)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

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
  - Snippet 1 (score: 0.762)
    > However, the peaks were in different positions within the gene in the four individual experiments performed (Fig. 6), and no specific binding site within the mRNA could be identified from the data.
    > Among the genes identified were numerous genes related to protein biosynthesis (tRNAs, tRNA-aminoacyl synthetases, tRNA-modifying enzymes, ribosomal proteins). As an example, genes for ribosomal proteins were highly represented with 18 out of the 22 genes (82%) for small ribosomal proteins, (12 after cold shock, 55%), and 31 out of 34 genes (91%) for large ribosomal subunit proteins (22 after cold shock, 65%). Other protein families represented were chaperones (e.g., dnaK, dnaJ, grpE, but not dafA, groES, groEL, clpB), cold-shock and general stress proteins (TT_RS08235, _09210; hsp22, hsp30; uspA), topoisomerase genes (gyrA, gyrB, topA), genes for transporters and their subunits (often both the gene for the substrate-bind-ing protein and for the permease, for example, branchedchain amino acid ABC transporter, TT_RS01115 and _01120), and genes related to sugar-and cell wall metabolism and cell division, as well as CRISPR-related genes. In many cases, genes for all subunits of protein complexes (e.g., genes for cytochrome c oxidase subunits I and II; clpA, clpX coding for the ClpAX protease) were present.
    > A systematic gene ontology analysis using the DAVID server 6.7 (https://david-d.ncifcrf.gov/home.jsp) (Huang da et al. 2009a,b) with the consolidated gene lists for Hera1/Hera2, and Hera3/Hera4, translated into UniProt accession numbers, revealed three annotation clusters with significant enrichment (Supplemental Table 4a,b).

### [3] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.755)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [4] Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium
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
  - Snippet 1 (score: 0.739)
    > Sequence similarity analyses were accomplished using blastx [26] against the NCBI non-redundant database on protein level [32], the Swissprot database [33,34] and KEGG [35]. Additionally, manual gene annotation was performed using PRIAM [36], Motif Scan [37], Prosite  [38], BRENDA [39,40], UniProt/SwissProt [34], Inter-ProScan [41], and Pfam [42] databases. One example of how our manual annotation differed from that of the automated pipeline used by Brown et al. can be found in the case of CLAU_3519 (CAETHG_3609). Here the automated pipeline from the Brown et al. finished genome assigned this gene product as a hypothetical protein, however when the sequence was aligned using BLASTP as part of our manual curation all other proteins with >75 % identity were named sodium ABC transporter. Upon further inspection in Pfam, one large ABC-2 family transporter protein domain was found (E-value 6.8e-31). Similar searches of UniProt and KEGG databases agreed with Pfam, therefore we annotated this gene product as an ABC-2 family transporter. The correction of the previously short-called homopolymer reads through our sequencing efforts gave a fully annotated finished sequence of C. autoethanogenum without the erroneous frame-shift containing annotations which had occurred previously. Using these tools we were able to manually curate the entire genome to ensure that the automated annotation was correct and to insert additional information where required, as well as implementing a standardised protein product naming system as recommend by the NCBI guidelines [43] for ease of identification of genes with related functions. As a consequence of the automated and subsequent manual curation, we have found 482 instances across the genome where genes previously identified as 'hypothetical protein' have either been assigned a specific function, or have been named through identification of conserved domains based on sequence similarity.

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
  - Snippet 1 (score: 0.736)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.679)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

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
  - Snippet 1 (score: 0.736)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [7] Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes
- Authors: Shikai Liu, Qi Li, Zhanjiang Liu
- Year: 2013
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/427dc24364271d57abe57d9efe0b1ebfc116d51c
- DOI: 10.1371/journal.pone.0063895
- PMID: 23696857
- PMCID: 3655950
- Citations: 63
- Influential citations: 7
- Summary: A set of 50 ABC transporters in catfish genome is identified and identified into seven subfamilies, providing the essential genomic resources for future biochemical, toxicological and physiological studies of ABC drug effluxtransporters.
- Evidence snippets:
  - Snippet 1 (score: 0.719)
    > Background Although a large set of full-length transcripts was recently assembled in catfish, annotation of large gene families, especially those with duplications, is still a great challenge. Most often, complexities in annotation cause mis-identification and thereby much confusion in the scientific literature. As such, detailed phylogenetic analysis and/or orthology analysis are required for annotation of genes involved in gene families. The ATP-binding cassette (ABC) transporter gene superfamily is a large gene family that encodes membrane proteins that transport a diverse set of substrates across membranes, playing important roles in protecting organisms from diverse environment. Methodology/Principal Findings In this work, we identified a set of 50 ABC transporters in catfish genome. Phylogenetic analysis allowed their identification and annotation into seven subfamilies, including 9 ABCA genes, 12 ABCB genes, 12 ABCC genes, 5 ABCD genes, 2 ABCE genes, 4 ABCF genes and 6 ABCG genes. Most ABC transporters are conserved among vertebrates, though cases of recent gene duplications and gene losses do exist. Gene duplications in catfish were found for ABCA1, ABCB3, ABCB6, ABCC5, ABCD3, ABCE1, ABCF2 and ABCG2. Conclusion/Significance The whole set of catfish ABC transporters provide the essential genomic resources for future biochemical, toxicological and physiological studies of ABC drug efflux transporters. The establishment of orthologies should allow functional inferences with the information from model species, though the function of lineage-specific genes can be distinct because of specific living environment with different selection pressure.

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
  - Snippet 1 (score: 0.717)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [9] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.713)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [10] Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data
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
  - Snippet 1 (score: 0.704)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [11] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.701)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [12] Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging
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
  - Snippet 1 (score: 0.698)
    > e validated target proteins of the active components were obtained from the TCMSP database. e target protein name of the active ingredient was converted to the standard target gene name through the UniProt Knowledge Base (UniProtKB, http://www. uniprot.org/). e UniProtKB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. e target protein names were inputted into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol.

### [13] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
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
  - Snippet 1 (score: 0.697)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

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
  - Snippet 1 (score: 0.696)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

### [15] Reconstructing the functions of endosymbiotic Mollicutes in fungus-growing ants
- Authors: P. Sapountzis, M. Zhukova, J. Shik, M. Schiøtt, J. Boomsma
- Year: 2018
- Venue: eLife
- URL: https://www.semanticscholar.org/paper/4c326d290732c1e42f47940b1cf7466fd19dcf2c
- DOI: 10.7554/eLife.39209
- PMID: 30454555
- PMCID: 6245734
- Citations: 44
- Influential citations: 3
- Summary: Reconstructions of their functional significance showed that they are independently acquired symbionts, most likely to decompose excess arginine consistent with the farmed fungal cultivars providing this nitrogen-rich amino-acid in variable quantities.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > gene targeted based on the RAST annotation, the target organism, the primer sequences from 5' to 3' and the annealing temperatures used for the qPCR. . Supplementary file 6. Correlation statistics for the association between the number of EntAcro1 cells and the expression of 10 MCT-like genes in the Ac. echinatior midgut and fat body tissues. From left to right we present for each gene examined: The protein ID in the Uniprot database (http://www.uniprot.org/), the gene name and the gene ID based on the Ac. echinatior annotation, the predicted protein size, and the results of statistical analyses examining the correlation between expression of the bacterial ftsZ gene in midgut/fat body tissues and the expression of MCT-like genes. The significance of each correlation was first evaluated using a non-parametric Spearman correlation test (see Methods), for which we give r values, p values and Bonferroni corrected p values.
    > The only significant correlation (marked in bold) was between the ftsZ and the MCT1 (F4WHWZ) transporter, for which previous functional experiments have demonstrated that it is actively involved in the import of acetate in eukaryotic cells (Kirat and Kato, 2006;Moschen et al., 2012).

### [16] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.686)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [17] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.684)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [18] Evaluation of Proteins Released to Medium in Yeast-Bacteria Co-culture System
- Authors: Ayşegül Yanik, Ç. Tarhan
- Year: 2023
- Venue: Journal of Advanced Research in Natural and Applied Sciences
- URL: https://www.semanticscholar.org/paper/bf1e6e710a760d61cdce04ea82c683106fe2ad6d
- DOI: 10.28979/jarnas.1196962
- Summary: The wild strain of Schizosaccharomyces pombe and the DH5α strain of Escherichia coli were grown in their own specific media, then cultured for 48 hours and 72 hours by cultivating in media containing 0,1% glucose with different cell number, and finally the differentiation in the proteins released by the cells into the medium was observed in SDS polyacrylamide gels.
- Evidence snippets:
  - Snippet 1 (score: 0.684)
    > The proteins identified as a result of LC-MS/MS analysis were evaluated in UniProt and the names and functions of the proteins are given as an appendix. Here, 6 protein-coding genes in the bands of the proteins released into the medium by the co-culture were found in the S.pombe genome and were classified according to their biological functions and cellular locations using the online platform PANTHER (Figure 2). Other 257 protein-coding genes were found in the E. coli genome. These proteins were also classified according to their cellular location (Figure 3) and their cellular functions (Figure 4). Maltose/maltodextrin-binding periplasmic protein (malE) and D-galactose-binding periplasmic protein (mglB) found in E. coli cells are among the binding proteins found in LC-MS-MS results. The binding protein MglB has a high affinity for glucose (Ferenci, 1996), and at low glucose concentration, glucose is mainly taken up by cells in this way. In a study by Egli et al. (1993), giving 1.8 mg l−1 galactose to a low glucose-containing E. coli culture decreased the glucose utilization of the cells and led to glucose accumulation in continuous culture. In addition, Hua and., (2004) found that the expression of a series of genes encoding membrane transporter proteins was significantly induced in cultures of limited chemostats for various carbon sources, and that about half of these genes were maltose (all genes of malGFE and malK-lamB-malM operons), galactose. They showed that there are genes involved in a wide variety of high-affinity ABC transport systems that facilitate uptake (three genes of the mglBAC operon). In E. coli, the ABC transporter gene family covers approximately 5% of the entire genome (Linton and Higgins, 1998). This shows how important these genes are. Carbon-limited cultures have been proposed to investigate bacterial growth and behavior under environmental conditions (Matin, 1979;Moriarty, 1993;Morita, 1993).

### [19] Prediction of Horizontally and Widely Transferred Genes in Prokaryotes
- Authors: Yoji Nakamura
- Year: 2018
- Venue: Evolutionary Bioinformatics Online
- URL: https://www.semanticscholar.org/paper/af7bde229b96609907924d1c68ea463af656efb2
- DOI: 10.1177/1176934318810785
- PMID: 30546254
- PMCID: 6287321
- Citations: 5
- Influential citations: 1
- Summary: A data-driven approach using massive sequence data may contribute to a broader understanding of HGT in prokaryotes, and predicted that six as-yet-uncharacterized genes were widely distributed HT genes, and therefore, will be interesting targets for evolutionary studies.
- Evidence snippets:
  - Snippet 1 (score: 0.679)
    > Focusing on uncharacterized HT genes in the COG and KEGG databases, four gene groups (COG3209, COG1479, COG3291, and COG3791) were classified into "general function prediction only" (COG category code = R) or "function unknown" (S) according to the COG annotation. By adding two gene groups of "uncharacterized protein" (K08998 and K07062) from the KEGG annotation, a total of six were obtained as functionally ambiguous HT gene groups despite being distributed among more than 300 species. With reference to COG3209 (uncharacterized conserved protein RhaS, contains 28 RHS repeats), the genes encoded in E. coli have been suggested to be horizontally transferred from another organism. 43 Recently, RHS repeat-containing genes are reported to be involved in toxins against competitors 44 ; therefore, the genes in COG3209 could be considered as defense system genes. The functions of COG1479 (uncharacterized conserved protein, contains ParB-like and HNH nuclease domains), COG3291 (PKD repeat), and COG3791 (uncharacterized conserved protein) have yet to be examined. According to InterPro analysis, COG3791 genes have a domain of glutathione-dependent formaldehyde-activating enzyme (IPR006913); therefore, these genes might be related to formaldehyde detoxification. 45 The KO group, K08998, corresponds to COG0759 (membraneanchored protein YidD) of category M in the COG database that has previously been reported to be involved in the protein insertion process. 46 K07062 corresponds to COG1487 and is considered a toxic protein. 47 As a whole, it has to be said that the evolutionary significance of these six gene groups has not been fully realized. Conversely, these genes might be good targets for evolutionary studies in the context of HGT, providing an example of data-driven approaches from massive sequence data. 48

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
2. Pascal Donsbach, Brian A. Yee, Dione L Sánchez-Hevia, J. Berenguer, S. Aigner et al. (2020). The Thermus thermophilus DEAD-box protein Hera is a general RNA binding protein and plays a key role in tRNA metabolism. RNA. https://www.semanticscholar.org/paper/533f89524b50f1df6146e8665eed9512b23e1a5c
3. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
4. Christopher M. Humphreys, Samantha McLean, Sarah Schatschneider, Thomas Millat, A. Henstra et al. (2015). Whole genome sequence and manual annotation of Clostridium autoethanogenum, an industrially relevant bacterium. BMC Genomics. https://www.semanticscholar.org/paper/8960e4d28fe195cb11cf0274c2dbd5952eefbef1
5. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
6. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
7. Shikai Liu, Qi Li, Zhanjiang Liu (2013). Genome-Wide Identification, Characterization and Phylogenetic Analysis of 50 Catfish ATP-Binding Cassette (ABC) Transporter Genes. PLoS ONE. https://www.semanticscholar.org/paper/427dc24364271d57abe57d9efe0b1ebfc116d51c
8. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
9. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
10. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
11. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
12. Yanfei Liu, Yue Liu, Wantong Zhang, Mingyue Sun, Weiliang Weng et al. (2020). Network Pharmacology-Based Strategy to Investigate the Pharmacological Mechanisms of Ginkgo biloba Extract for Aging. Evidence-based Complementary and Alternative Medicine : eCAM. https://www.semanticscholar.org/paper/fadeff691eb41dff82e019cc3d38b846fdc605c4
13. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
14. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
15. P. Sapountzis, M. Zhukova, J. Shik, M. Schiøtt, J. Boomsma (2018). Reconstructing the functions of endosymbiotic Mollicutes in fungus-growing ants. eLife. https://www.semanticscholar.org/paper/4c326d290732c1e42f47940b1cf7466fd19dcf2c
16. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
17. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
18. Ayşegül Yanik, Ç. Tarhan (2023). Evaluation of Proteins Released to Medium in Yeast-Bacteria Co-culture System. Journal of Advanced Research in Natural and Applied Sciences. https://www.semanticscholar.org/paper/bf1e6e710a760d61cdce04ea82c683106fe2ad6d
19. Yoji Nakamura (2018). Prediction of Horizontally and Widely Transferred Genes in Prokaryotes. Evolutionary Bioinformatics Online. https://www.semanticscholar.org/paper/af7bde229b96609907924d1c68ea463af656efb2