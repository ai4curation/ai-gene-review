---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T06:05:29.005011'
end_time: '2026-07-07T06:05:34.429879'
duration_seconds: 5.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: atpB
  gene_symbol: atpB
  uniprot_accession: Q88BW8
  protein_description: 'RecName: Full=ATP synthase subunit a {ECO:0000255|HAMAP-Rule:MF_01393};
    AltName: Full=ATP synthase F0 sector subunit a {ECO:0000255|HAMAP-Rule:MF_01393};
    AltName: Full=F-ATPase subunit 6 {ECO:0000255|HAMAP-Rule:MF_01393};'
  gene_info: Name=atpB {ECO:0000255|HAMAP-Rule:MF_01393}; OrderedLocusNames=PP_5419;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATPase A chain family. {ECO:0000255|HAMAP-
  protein_domains: ATP_syn_F0_a_bact/chloroplast. (IPR045082); ATP_synth_F0_asu. (IPR000568);
    ATP_synth_F0_asu_AS. (IPR023011); F0_ATP_A_sf. (IPR035908); ATP-synt_A (PF00119)
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
- **UniProt Accession:** Q88BW8
- **Protein Description:** RecName: Full=ATP synthase subunit a {ECO:0000255|HAMAP-Rule:MF_01393}; AltName: Full=ATP synthase F0 sector subunit a {ECO:0000255|HAMAP-Rule:MF_01393}; AltName: Full=F-ATPase subunit 6 {ECO:0000255|HAMAP-Rule:MF_01393};
- **Gene Information:** Name=atpB {ECO:0000255|HAMAP-Rule:MF_01393}; OrderedLocusNames=PP_5419;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATPase A chain family. {ECO:0000255|HAMAP-
- **Key Domains:** ATP_syn_F0_a_bact/chloroplast. (IPR045082); ATP_synth_F0_asu. (IPR000568); ATP_synth_F0_asu_AS. (IPR023011); F0_ATP_A_sf. (IPR035908); ATP-synt_A (PF00119)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atpB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atpB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atpB** (gene ID: atpB, UniProt: Q88BW8) in PSEPK.

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
  - Snippet 1 (score: 0.771)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.685)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

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
  - Snippet 1 (score: 0.730)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [3] An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México
- Authors: Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel
- Year: 2023
- Venue: Microorganisms
- URL: https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
- DOI: 10.3390/microorganisms11071640
- PMID: 37512813
- PMCID: 10384328
- Citations: 8
- Summary: The quality obtained from the biogas suggests that this metabolism is not the main one in carbon use, possibly the sum of several conditions including growth conditions and the pollution present in these sediments.
- Evidence snippets:
  - Snippet 1 (score: 0.722)
    > When a genome is sequenced or a protein is characterized, databases classify the information in different ways using automatic identification or manual annotation. In the UniProt database, an annotation is possibly made using the formal representation proposed in Gene Ontology (GO) under three aspects related to biological knowledge of the proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively. An example of an ATP-binding protein is the subunit α of V-type ATP synthase (A0A8G2FW98) of Picrophilus oshimae DSM 9789. As expected, this protein has other three annotations related to proton transport. Besides that, the DNA helicase (A0A811T524) of Ca. Argoarchaeum ethanivorans has the MF of DNA binding and ATP binding. Interestingly, metal ion binding proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively.

### [4] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.714)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [5] Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control
- Authors: Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al.
- Year: 2023
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
- DOI: 10.3390/ijms241713058
- PMID: 37685862
- PMCID: 10488290
- Citations: 3
- Summary: Chilodonella hexasticha is a harmful parasitic ciliate that can cause severe damage to fish and high mortalities worldwide. Its congeneric species, C. uncinata, is a facultative parasite that not only can be free-living but also can parasitize on fish gills and fins. In this study, single-cell transcriptomes of these two species were assembled and characterized. Numerous enzymes related to energy metabolism and parasitic adaption were identified through annotation in the Non-Redundant (NR), C...
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > Some energy metabolism-related enzymes, such as isocitrate dehydrogenase (IDH), cytochrome c oxidase subunit 1 (Cox 1) and ATP synthase, were also up-regulated in C. hexasticha. for this study, while those of C. uncinata were adopted from [7]. The yellow boxes represent the upregulated genes, while the blue boxes represent down-expressed genes. The full names of protein products of these annotated genes are TUB: tubulin, ISCU: iron-sulfur cluster assembly scaffold protein IscU-like; ISCB: 2 iron, 2 sulfur cluster-binding protein, IDH: isocitrate dehydrogenase, Cox1: cytochrome c oxidase subunit 1, ATP5D: ATP synthase F1, delta subunit, OGC: 2oxoglutarate/malate carrier protein, ABC: ABC transporter family protein, ATPase: v-type ATPase subunit family protein, HSP: heat shock protein, ACP: acyl carrier protein, DNAH7: dynein heavy chain 7.

### [6] CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes
- Authors: M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo
- Year: 2020
- Venue: Nature Protocols
- URL: https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
- DOI: 10.1038/s41596-020-0292-x
- PMID: 32103204
- Citations: 2771
- Influential citations: 298
- Summary: The structure and content of CellPhoneDB is outlined, procedures for inferring cell–cell communication networks from single-cell RNA sequencing data are provided and a practical step-by-step guide to help implement the protocol is presented.
- Evidence snippets:
  - Snippet 1 (score: 0.692)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [7] Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts
- Authors: J. Doolittle, S. Gomez
- Year: 2011
- Venue: PLoS Neglected Tropical Diseases
- URL: https://www.semanticscholar.org/paper/baff9e82a73e77a021118c0910a5874568cd60b3
- DOI: 10.1371/journal.pntd.0000954
- PMID: 21358811
- PMCID: 3039688
- Citations: 97
- Influential citations: 2
- Summary: Dengue virus manipulates cellular processes to its advantage through specific interactions with the host's protein interaction network, and the interaction networks presented here provide a set of hypothesis for further experimental investigation into the DENV life cycle as well as potential therapeutic targets.
- Evidence snippets:
  - Snippet 1 (score: 0.683)
    > Figure S1 GO term enrichment of A. aegypti proteins based on data from Guo et al. [13]. (A) Enriched GO biological process terms. (B) Enriched GO molecular function terms. Light blue bars represent terms for A. aegypti targets, and pink is for terms from DENV-similar proteins. When more than ten terms were enriched for a set of proteins, only the ten most signicant terms are shown. Bonferroni corrected p-values were transformed by -log10. The following abbreviations are used: "translation factor nucleic acid bind" is "translation factor activity nucleic acid binding," and "macromolecular subunit organiz" is "macromolecular complex subunit organization." Found at: doi:10.1371/journal.pntd.0000954.s001 (1.39 MB TIF)  Table S3 Predicted interactions between DENV2 and human after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the target protein's Uniprot accession, Entrez Gene ID, and Symbol; if the target is a known host factor; and if the predicted interaction was already known in the literature. Found at: doi:10.1371/journal.pntd.0000954.s005 (3.01 MB TXT) Table S4 Predicted interactions between DENV2 and A. aegypti after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the D. melanogaster target protein's FlyBase gene number, and Symbol; the A. aegypti target protein's VectorBase protein ID, and Uniprot accession; and if the target is a known host factor. Found at: doi:10.1371/journal.pntd.0000954.s006

### [8] MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data
- Authors: Anthony C. Smith, A. Robinson
- Year: 2009
- Venue: Molecular & Cellular Proteomics : MCP
- URL: https://www.semanticscholar.org/paper/206a60d6d387688ce7f880e0dfe67af5a723c7b8
- DOI: 10.1074/mcp.M800373-MCP200
- PMID: 19208617
- PMCID: 2690483
- Citations: 84
- Influential citations: 7
- Summary: Analysis indicated that enzymes of some cytosolic metabolic pathways are regularly detected in mitochondrial proteomics experiments, suggesting that they are associated with the outside of the outer mitochondrial membrane.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > Recorded for each protein of the mass spectrometry data sets were, where available, the original protein identifier, subcellular location, sequence of identified peptides, sequence coverage, and the experimental techniques that had been used for the purification, separation, and identification of the protein. If the original protein identifier could not be mapped to a UniProt primary accession number by PIR ID or MGI, then the protein was compared with proteins in UniProt by using BLASTP (14). If there was a significant match, then the UniProt primary accession number was assigned to the protein. Those proteins without a significant match were discarded. By using the PIR ID and the MGI identifier conversion tools, the evidence of mitochondrial localization for a protein was linked to many of the UniProt entries representing it. Identifiers of proteins encoded in the mitochondrial genome of organisms were taken from the Organelle database of the European Molecular Biology Laboratory-European Bioinformatics Institute and used to annotate the appropriate proteins in MitoMiner.
    > The source of protein sequences, related features, and annotation was UniProt (11). All UniProt entries were downloaded for the six species with mitochondrial localization data sets. The literature citations in each UniProt entry were retrieved from PubMed by using an InterMine parser. Additional Gene Ontology annotation on the biological process, metabolic function, and cellular component of each protein was taken from UniProt (15) and individual genome projects of M. musculus (12), Rattus norvegicus (16), Drosophila melanogaster (17), and Saccharomyces cerevisiae (18).
    > Finally lists of human genes and the descriptions of their associated disease phenotypes were taken from OMIM (19), the definitions of groups of homologous proteins were taken from HomoloGene (20), and data on the reactions, enzymes, and compounds of metabolic pathways were taken from KEGG (21). The EC numbers of proteins in UniProt were used to define the cross-reference between proteins and metabolic pathways.

### [9] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.682)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [10] Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains
- Authors: J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al.
- Year: 2025
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
- DOI: 10.1038/s41598-025-29509-x
- PMID: 41310174
- PMCID: 12749726
- Citations: 1
- Summary: Findings include large plasmid deletions, an enrichment of mutations in secondary metabolite biosynthesis and regulatory genes, and metabolic shifts redirecting amino acid and carbon flux toward CA biosynthetic pathways.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > Gene annotation was primarily derived from the S. clavuligerus reference genome in the NCBI database and was annotated using the NCBI Prokaryotic Genome Annotation Pipeline 59 . However, several CA biosynthetic genes were manually corrected based on published literature 9 . For instance, two loci were originally annotated as clavaminate synthase 1 (cas1), but one of these loci is located near the cephamycin C biosynthetic cluster, indicating it was actually cas2. Following this correction, the RefSeq accession numbers of all genes in the reference genome were cross-referenced with the UniProt database to obtain additional annotations 60 . For the mutated genes identified through ICA, protein existence levels were manually assigned based on the UniProt data, including protein existence status, annotation score, similar proteins, and relevant publications.

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
  - Snippet 1 (score: 0.679)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [12] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
- Authors: Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al.
- Year: 2025
- Venue: Molecular Ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 3
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.674)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [13] Analysis of Sogatella furcifera proteome that interact with P10 protein of Southern rice black-streaked dwarf virus
- Authors: W. Than, F. Qin, Wenwen Liu, Xifeng Wang
- Year: 2016
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/4c847a661420bee76d1eaff3282bbb2f194f114d
- DOI: 10.1038/srep32445
- PMID: 27653366
- PMCID: 5032029
- Citations: 19
- Summary: A yeast two-hybrid system is used to investigate the interactions between the SRBSDV- P10 and the cDNA library of WBPH and finds that VAMP7 was high in adult males and gut, and Vti1A was abundant in adult female, and malpighian tubule, gut and ovary.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > For testing a protein-protein interaction in a pull-down assay, the full length of the gene sequence is needed. Based on the available gene fragment from the yeast two-hybrid screening result, strongly interacting proteins in the retransformation analysis and β-galactosidase assay, the vesicle-associated membrane protein 7, vesicle transport V-SNARE protein Vti1A, growth hormone-inducible transmembrane protein, nascent polypeptide-associated complex subunit alpha, and ATP synthase lipid-binding protein were selected and amplified, and the full-length sequence was obtained using 5′ rapid amplification of cDNA ends (RACE). Full-length gene sequences for 5 selected proteins could be amplified; the full-length of the genes, including the 5′-untranslated region (5′ UTR), open reading frame (ORF), 3′-untranslated region (3′ UTR), and poly (A) tail of each gene are described in Supplemental Table S1.

### [14] Isolation and Identification of miRNAs in Jatropha curcas
- Authors: Chun Ming Wang, F. Sun, Lei Li, Peng Liu, Jian Ye et al.
- Year: 2012
- Venue: International Journal of Biological Sciences
- URL: https://www.semanticscholar.org/paper/89362a3bf150081c8260f785de9299194d5e2d22
- DOI: 10.7150/ijbs.3676
- PMID: 22419887
- PMCID: 3303143
- Citations: 29
- Influential citations: 2
- Summary: To identify miRNAs in Jatropha curcas L, a bioenergy crop, cDNA clones from two small RNA libraries of leaves and seeds were sequenced and analyzed using bioinformatic tools, indicating diverse functions of JcumiR004.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > The 28 ESTs of putative targets were used to search for similar protein sequences in the Uniprot database (BLASTX). The functional information is presented in Additional file 2: Supplementary Table 1. Using the best hits found by BLASTX, an inferred gene ontology annotation was found for 16 of the sequences through QuickGO. Using GO Slimmer in AmiGO database, of the 16 known functional ESTs, one was associated with genes belonging to biological process, 7 with cellular component, and 8 with molecular function. The result showed that the miRNA target genes encoded a broad range of proteins, with majority (15/16) of the predicted protein products involved in molecular function and cellular compo-nent ontologies. The predicted protein description of the target EST sequences were listed in Additional file 2: Supplementary Table 1, with some interesting proteins such as DNA cross-link repair protein, vacuolar ATP synthase proteolipid, elongation factor 1-alpha, Cytochrome c-type biogenesis protein, 14-3-3 protein, heat stress transcription factor A-5, etc. Thus, the miRNA target genes encode a broad range of proteins.

### [15] Construction and Analysis of an Enzyme-Constrained Metabolic Model of Corynebacterium glutamicum
- Authors: Jinhui Niu, Zhitao Mao, Yufeng Mao, Ke Wu, Zhenkun Shi et al.
- Year: 2022
- Venue: Biomolecules
- URL: https://www.semanticscholar.org/paper/b5d84cb624ba86272e3954fa6d89b63d59c5a333
- DOI: 10.3390/biom12101499
- PMID: 36291707
- PMCID: 9599660
- Citations: 26
- Influential citations: 2
- Summary: This study shows that incorporating enzyme kinetic information into the GEM enhances the cellular phenotypes prediction of C. glutamicum, which can help identify key enzymes and thus provide reliable guidance for metabolic engineering.
- Evidence snippets:
  - Snippet 1 (score: 0.669)
    > We found some errors in the GPR relationships in iCW773 during the analysis and corrected these errors using two methods. First, the modified GPRuler tool was used to identify more "and" relationships. The GPRuler tool identifies the 'and' relationships based on the protein complex information extracted from databases such as UniProt [27] and Complex Portal [28]. However, the original terms ('subunit' and 'chain') used to identify complexes in the GPRuler tool were extracted based on human and yeast protein description information and did not cover all C. glutamicum protein complexes. For example, the protein name of P06557 (encoding by Cgl3029) is Anthranilate synthase component 1, which will not be identified as a subunit forming an 'and' relationship with another subunit using the original terms. Therefore, we updated the terms by carefully checking the words used in UniProt to describe possible protein complex formation (e.g., 'component', 'binding protein', and 'assembly factor', etc. see Table S1 for the full list) to obtain more 'and' relationships in C. glutamicum. We also simplified the GPRuler tool process by parsing UniProt data directly to obtain the corresponding GPR relationships without running the processes for gene identification, reaction identification, and gene filter.
    > We also observed that some 'and' relationships in iCW773 were not identified by the GPRuler tool and could be wrong. To address this, we developed a semi-automated process based on protein similarity to determine the correct relationship. We calculated the protein sequence similarity for the remaining 'and' relationships in iCW773 and revised the relationship to 'or' if similarity exists between protein sequences as proteins with similarity are more likely to be isoenzymes rather than forming protein complexes. We then manually checked the gene annotation information in databases (BioCyc [29] and KEGG [30]) to ensure the correction is right.

### [16] GeneTools – application for functional annotation and statistical hypothesis testing
- Authors: V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al.
- Year: 2006
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
- DOI: 10.1186/1471-2105-7-470
- PMID: 17062145
- PMCID: 1630634
- Citations: 105
- Influential citations: 11
- Summary: GeneTools is the first "all in one" annotation tool, providing users with a rapid extraction of highly relevant gene annotation data for e.g. thousands of genes or clones at once.
- Evidence snippets:
  - Snippet 1 (score: 0.665)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [17] Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences
- Authors: M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al.
- Year: 2025
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
- DOI: 10.3390/ijms262411830
- PMID: 41465260
- PMCID: 12733082
- Summary: This work establishes a foundation for investigating the role of mitochondrial genome variation in key plant’s phenotypic traits, such as the enhanced responsiveness to arbuscular mycorrhiza observed in this agronomically valuable line of Medicago lupulina L. vulgaris Koch.
- Evidence snippets:
  - Snippet 1 (score: 0.664)
    > (ii). Annotation of Protein-Coding Genes Among the 33 ORFs encoding proteins with predicted functions were: nine encoding NADH dehydrogenase subunits, one encoding cytochrome b, three encoding cytochrome C oxidase subunits, five encoding ATP synthase subunits, four responsible for cytochrome C maturation, nine encoding ribosomal proteins, and two with other functions (matR and mttB; Table 1, Figure 2). Among these, the cox2, rps3, nad1, nad5, and rpl2 genes were characterized with potential mutations due to single nucleotide polymorphisms (SNPs). The rpl2 sequence from the VIK32, line MlS-1 mtDNA showed identity with exon 2 of the chloroplast gene encoding ribosomal protein L2. For example, it showed identity with an exon of the line MlS-1 chloroplast gene rplB (OR674883.1; coordinates 78,587-79,084; Cover 69%, Identity 98.3%) (Figure 3), as well as with exon 2 of the chloroplast gene rpl2 from M. lupulina (OM681370.1; Cover 72%, Identity 98.4%) and M. truncatula cultivar Jemalong A17 (MT965675.1; Cover 72%, Identity 97.5%). This sequence also showed high similarity to sequences from the chloroplast genomes of phylogenetically distant plants from the genera Trigonella, Melilotus, Lathyrus, and Pisum (Cover 97%, Identity 95.6-96.2%). The 45 protein-coding genes were characterized as genes encoding hypothetical proteins (Figure 2).

### [18] FlyBase: establishing a Gene Group resource for Drosophila melanogaster
- Authors: H. Attrill, K. Falls, J. Goodman, G. Millburn, Giulia Antonazzo et al.
- Year: 2015
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/0d58fdc5f1dfcb2910f7cc003338a82ef827f85c
- DOI: 10.1093/nar/gkv1046
- PMID: 26467478
- PMCID: 4702782
- Citations: 326
- Influential citations: 28
- Summary: FlyBase (flybase.org), the MOD for Drosophila melanogaster, has established a ‘Gene Group’ resource: high-quality sets of genes derived from the published literature and organized into individual report pages, to enable researchers with diverse backgrounds and interests to easily view and analyse acknowledged D. melanogsaster gene sets and compare them with those of other species.
- Evidence snippets:
  - Snippet 1 (score: 0.663)
    > Given the wealth of post-genomic data, it should be straightforward to query a biological database and obtain a robust list of genes related by the shared attributes of their products, such as actins, protein kinases or subunits of the proteasome. However, this is often not the case. For evolutionary-related genes, BLAST (1) or domain-based searches may yield a good preliminary list, but without further analysis, particularly when inferring function from se-quence, it is hard to distinguish false positives. Additionally, there may be false negatives because a gene may be somewhat atypical or fails to score above a given threshold. Gene Ontology (GO) annotations can be used to search for gene products that are related by common biological attributes, but annotation is not exhaustive and expressing features that pertain to sequence does not fall within its scope (2,3).
    > An alternative approach to finding related genes (at least in species with well-characterized genomes such as humans and model organisms) can be to search for gene symbols that share a common prefix. This can be effective for databases such as WormBase (4) or the HUGO Gene Nomenclature Committee (HGNC) (5) that assign unifying and systematic gene symbols to nematode and human genes, respectively, based on shared structures, functions or phenotypes. However, this strategy is not generally applicable to Drosophila melanogaster genes in FlyBase (6) as these are traditionally named on a gene-by-gene basis by the authors who first publish on the gene, often reflecting a specific mutant phenotype.
    > A third method for acquiring a set of related genes is to directly consult relevant research or review articles. The advantage of this approach is that the list is compiled directly from an expert and peer-reviewed source, and as such will be robust and clearly attributable. However, it can be time-consuming to seek out and then extract a set of genes from individual publications (or, often, their supplementary data) and lists obtained in this manner are inherently uncoupled from the relevant species database, meaning that the listed gene symbols/IDs may become stale over time.
    > Several databases have addressed these issues by providing explicit sets of related genes.

### [19] Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production
- Authors: Seth B Roberts, Christopher M. Gowen, J. Brooks, Stephen S. Fong
- Year: 2010
- Venue: BMC Systems Biology
- URL: https://www.semanticscholar.org/paper/dc66757785ecb9e1d1760f67f5410dddb5d3618c
- DOI: 10.1186/1752-0509-4-31
- PMID: 20307315
- PMCID: 2852388
- Citations: 129
- Influential citations: 15
- Summary: A genome-scale model of C. thermocellum metabolism is presented, i SR432, for the purpose of establishing a computational tool to study the metabolic network of the organism and establish a strong foundation for rational strain design.
- Evidence snippets:
  - Snippet 1 (score: 0.663)
    > GPR relationships specify the putative relationship between genes and enzymatic activities in an organism. Following previous work [52], we represented these relationships as Boolean statements. The simplest such statement was: gene A implies reaction X, i.e., gene A -> reaction X. Enzymatic activities associated with protein complexes required more complicated statements, e.g., (gene A or gene B) and (gene C) -> reaction X.
    > To develop the GPR relationships for C. thermocellum, we used the annotations described above and information on protein complexes from UniProt. For each EC number in the C. thermocellum annotations, we searched UniProt [23] to determine whether that EC is associated with protein complexes, and if so, what type of complex exists across different organisms (homodimer, heterotrimer, etc.). Based on this information, and the information in the annotations, we assigned putative GPR relationships for C. thermocellum, conforming to known enzyme complex architecture whenever possible. As a specific example of this process, consider the reaction corresponding to carbamoyl-phosphate synthase ('R_CBPS'), EC 6.3.5.5. Several UniProt entries (e.g., CARA_ECOLI) with this EC number are annotated as being members of a complex composed of two chains, a small glutamine-hydrolyzing chain and a large chain that synthesizes carbamoyl phosphate. We found two C. thermocellum genes annotated as "carbamoyl-phosphate synthase, small subunit" (Cthe_1867, Cthe_0950) and two genes annotated as "carbamoyl-phosphate synthase, large subunit" (Cthe_1868, Cthe_0949). Thus, we expressed the GPR relationship for this reaction as: (Cthe_1867 or Cthe_0950) and (Cthe_1868 or Cthe_0949) -> R_CBPS.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
3. Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel (2023). An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México. Microorganisms. https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
4. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
5. Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al. (2023). Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
6. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
7. J. Doolittle, S. Gomez (2011). Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts. PLoS Neglected Tropical Diseases. https://www.semanticscholar.org/paper/baff9e82a73e77a021118c0910a5874568cd60b3
8. Anthony C. Smith, A. Robinson (2009). MitoMiner, an Integrated Database for the Storage and Analysis of Mitochondrial Proteomics Data. Molecular & Cellular Proteomics : MCP. https://www.semanticscholar.org/paper/206a60d6d387688ce7f880e0dfe67af5a723c7b8
9. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
10. J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al. (2025). Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains. Scientific Reports. https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
11. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
12. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
13. W. Than, F. Qin, Wenwen Liu, Xifeng Wang (2016). Analysis of Sogatella furcifera proteome that interact with P10 protein of Southern rice black-streaked dwarf virus. Scientific Reports. https://www.semanticscholar.org/paper/4c847a661420bee76d1eaff3282bbb2f194f114d
14. Chun Ming Wang, F. Sun, Lei Li, Peng Liu, Jian Ye et al. (2012). Isolation and Identification of miRNAs in Jatropha curcas. International Journal of Biological Sciences. https://www.semanticscholar.org/paper/89362a3bf150081c8260f785de9299194d5e2d22
15. Jinhui Niu, Zhitao Mao, Yufeng Mao, Ke Wu, Zhenkun Shi et al. (2022). Construction and Analysis of an Enzyme-Constrained Metabolic Model of Corynebacterium glutamicum. Biomolecules. https://www.semanticscholar.org/paper/b5d84cb624ba86272e3954fa6d89b63d59c5a333
16. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
17. M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al. (2025). Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
18. H. Attrill, K. Falls, J. Goodman, G. Millburn, Giulia Antonazzo et al. (2015). FlyBase: establishing a Gene Group resource for Drosophila melanogaster. Nucleic Acids Research. https://www.semanticscholar.org/paper/0d58fdc5f1dfcb2910f7cc003338a82ef827f85c
19. Seth B Roberts, Christopher M. Gowen, J. Brooks, Stephen S. Fong (2010). Genome-scale metabolic analysis of Clostridium thermocellum for bioethanol production. BMC Systems Biology. https://www.semanticscholar.org/paper/dc66757785ecb9e1d1760f67f5410dddb5d3618c