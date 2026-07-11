---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T06:05:03.294815'
end_time: '2026-07-07T06:05:09.597496'
duration_seconds: 6.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: atpH
  gene_symbol: atpH
  uniprot_accession: Q88BX1
  protein_description: 'RecName: Full=ATP synthase subunit delta {ECO:0000255|HAMAP-Rule:MF_01416};
    AltName: Full=ATP synthase F(1) sector subunit delta {ECO:0000255|HAMAP-Rule:MF_01416};
    AltName: Full=F-type ATPase subunit delta {ECO:0000255|HAMAP-Rule:MF_01416}; Short=F-ATPase
    subunit delta {ECO:0000255|HAMAP-Rule:MF_01416};'
  gene_info: Name=atpH {ECO:0000255|HAMAP-Rule:MF_01416}; OrderedLocusNames=PP_5416;
    ORFNames=PP5416;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATPase delta chain family.
  protein_domains: ATP_synth_OSCP/delta_N_sf. (IPR026015); ATPase_OSCP/dsu. (IPR000711);
    OSCP (PF00213)
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
- **UniProt Accession:** Q88BX1
- **Protein Description:** RecName: Full=ATP synthase subunit delta {ECO:0000255|HAMAP-Rule:MF_01416}; AltName: Full=ATP synthase F(1) sector subunit delta {ECO:0000255|HAMAP-Rule:MF_01416}; AltName: Full=F-type ATPase subunit delta {ECO:0000255|HAMAP-Rule:MF_01416}; Short=F-ATPase subunit delta {ECO:0000255|HAMAP-Rule:MF_01416};
- **Gene Information:** Name=atpH {ECO:0000255|HAMAP-Rule:MF_01416}; OrderedLocusNames=PP_5416; ORFNames=PP5416;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATPase delta chain family.
- **Key Domains:** ATP_synth_OSCP/delta_N_sf. (IPR026015); ATPase_OSCP/dsu. (IPR000711); OSCP (PF00213)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atpH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atpH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atpH** (gene ID: atpH, UniProt: Q88BX1) in PSEPK.

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
  - Snippet 1 (score: 0.778)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.
  - Snippet 2 (score: 0.700)
    > (I think match should be teal and mismatch -red?)
    > The legend was previously mismatched with the labels. This has been corrected in the new uploaded figure . 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section?
    > The reviewer's presumption is correct; we had stated the date of data retrieval in the caption of Table 1, but we agree it should instead be stated centrally in the Methods. We have now added it to the Methods section as well, for clarity (Lines 696-700) 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copypasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...")
    > We thank the reviewer for catching this accidental insertion. We have now removed the spurious fragment.
    > 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > We have removed this speculation in the revised submission.
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or under-annotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets.

### [2] Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control
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
  - Snippet 1 (score: 0.713)
    > Some energy metabolism-related enzymes, such as isocitrate dehydrogenase (IDH), cytochrome c oxidase subunit 1 (Cox 1) and ATP synthase, were also up-regulated in C. hexasticha. for this study, while those of C. uncinata were adopted from [7]. The yellow boxes represent the upregulated genes, while the blue boxes represent down-expressed genes. The full names of protein products of these annotated genes are TUB: tubulin, ISCU: iron-sulfur cluster assembly scaffold protein IscU-like; ISCB: 2 iron, 2 sulfur cluster-binding protein, IDH: isocitrate dehydrogenase, Cox1: cytochrome c oxidase subunit 1, ATP5D: ATP synthase F1, delta subunit, OGC: 2oxoglutarate/malate carrier protein, ABC: ABC transporter family protein, ATPase: v-type ATPase subunit family protein, HSP: heat shock protein, ACP: acyl carrier protein, DNAH7: dynein heavy chain 7.

### [3] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.696)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

### [4] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.690)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [5] Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology
- Authors: Stefania D'Alessio, Katherine M. Buckley, I. Kraev, P. Hayes, S. Lange
- Year: 2021
- Venue: Biology
- URL: https://www.semanticscholar.org/paper/e2b33d9697175a6e724fdb85e3ac2ec169d92871
- DOI: 10.3390/biology10090866
- PMID: 34571743
- PMCID: 8464700
- Citations: 14
- Summary: This study assessed EVs present in the coelomic fluid of the purple sea urchin, and identified both total protein cargo as well as the deiminated protein cargo, adding to current understanding of how post-translational deimination may shape immunity across the phylogeny tree.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > For the detection of a putative PAD homologue from sea urchins, anti-human PAD2-specific antibody was used in Western blotting to assess any cross-reaction with a (B) KEGG pathways identified from STRING analysis for EV total protein cargo (annotated hits). (C) Gene Ontology (GO) Biological processes identified from STRING analysis for total EV protein cargo (annotated hits). (D) GO Molecular Function pathways identified from STRING analysis for total EV protein cargo (annotated hits; protein names of hits are presented in the figures; additional interacting proteins are: LOC579085 = ATP synthase subunit gamma, mitochondrial; LOC587430 = ATP synthase subunit O, mitochondrial; LOC373382 = ATP synthase subunit alpha; LOC576006 = ATP synthase subunit delta, mitochondrial; LOC579751 = ATP synthase F(0) complex subunit B1, mitochondrial).

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
  - Snippet 1 (score: 0.686)
    > CellPhoneDB stores ligand-receptor interactions, as well as other properties of the interacting partners, including their subunit architecture and gene and protein identifiers. To create the content of the database, four main .csv data files are required: gene_input.csv, protein_input.csv, complex_input.csv and interaction_input.csv (Fig. 4).
    > gene_input Mandatory fields are 'gene_name', 'uniprot', 'hgnc_symbol' and 'ensembl'. This file is critical for establishing the link between the scRNA-seq data and the interaction pairs stored at the protein level. It includes the following gene and protein identifiers: (i) gene name ('gene_name'), (ii) UniProt identifier ('uniprot'), (iii) HUGO Nomenclature Committee (HGNC) symbol ('hgnc_symbol') and (iv) gene Ensembl identifier (ENSG) ('ensembl'). To create this file, lists of linked proteins and gene identifiers are downloaded from UniProt and merged using gene names. Several rules need to be considered when merging the files • UniProt annotation prevails over the gene Ensembl annotation when the same gene Ensembl identifier points toward different UniProt identifiers. • UniProt and Ensembl lists are also merged by their UniProt identifier, but this information is used only when the UniProt or Ensembl identifier is missing in the original list merged by gene name. • If the same gene name points toward different HGNC symbols, only the HGNC symbol matching the gene name annotation is considered. • Only one HLA isoform is considered in our interaction analysis, and it is stored in a manually HLA-curated list of genes, named HLA_curated.
    > protein_input Mandatory fields are 'uniprot' and 'protein_name'.

### [7] Proteomic Analysis of Extracellular ATP-Regulated Proteins Identifies ATP Synthase β-Subunit as a Novel Plant Cell Death Regulator*
- Authors: S. Chivasa, Daniel Tomé, John M U Hamilton, A. Slabas
- Year: 2010
- Venue: Molecular & Cellular Proteomics
- URL: https://www.semanticscholar.org/paper/097975eee8336bdf9785e2d0316e5bf8f2e2edde
- DOI: 10.1074/mcp.M110.003905
- PMID: 21156838
- Citations: 78
- Influential citations: 6
- Summary: This study defines a new role for ATP synthase β-subunit as a pro-cell death protein, a novel target for extracellular ATP in its function as a key negative regulator of plant cell death.
- Evidence snippets:
  - Snippet 1 (score: 0.680)
    > Second, ATP synthase ␤-subunit might be capable of influencing gene expression directly or indirectly, thereby activating cell death genes. Cytosolic proteins such as gluceraldehyde-3-phosphate dehydrogenase (58) and enolase (66) are now known to translocate to the nucleus to affect gene expression, though they are classical glycolytic enzymes. ATP synthase ␤-subunit could have a similar secondary function in regulation of gene expression as revealed by altered basal expression of several genes in the knockout mutant plants (data not shown). Finally, ATP synthase ␤-subunit within the F 1 complex could be targeted for direct binding by FB1 or another prodeath protein/signal, leading to an inhibition of mitochondrial ATP production. Likewise, the basis for phytotoxicity of tentoxin, another fungal-derived toxin, is cellular depletion of ATP caused by inhibition of chloroplastic photophosphorylation (67). In this scenario, FB1 resistance in the At5g08690 knockout mutants could result from the lack of a binding site in the mitochondrial F 1 complex as the target At5g08690 gene product would be absent and replaced by products from one of the two other family members, At5g08680 and At5g08670. The Arabidopsis ATP synthase ␤-subunit protein belongs to a multigene family consisting of three members having 98% sequence similarity at the amino acid level, with differences only in the first 61 amino acids, making this region an ideal focal point for future genetic analyses to determine the basis for its cell death promotional function. Certain residues of the chloroplastic ATP synthase ␤-subunit were found to be critical for binding of the cell death-inducing tentoxin to the chloroplast F 1 -ATP synthase (68). Mutagenesis of a specific chloroplastic ATP synthase ␤-subunit gene codon of tentoxin-resistant Chlamydomonas reinhardtii to match the corresponding codon of tentoxinsensitive Nicotiana species rendered the alga tentoxin-sensitive (68), demonstrating very specific structural requirements for chloroplastic ATP synthase ␤-subunit function in cell death promotion.

### [8] An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México
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
  - Snippet 1 (score: 0.673)
    > When a genome is sequenced or a protein is characterized, databases classify the information in different ways using automatic identification or manual annotation. In the UniProt database, an annotation is possibly made using the formal representation proposed in Gene Ontology (GO) under three aspects related to biological knowledge of the proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively. An example of an ATP-binding protein is the subunit α of V-type ATP synthase (A0A8G2FW98) of Picrophilus oshimae DSM 9789. As expected, this protein has other three annotations related to proton transport. Besides that, the DNA helicase (A0A811T524) of Ca. Argoarchaeum ethanivorans has the MF of DNA binding and ATP binding. Interestingly, metal ion binding proteins: molecular function (MF), biological processes (BP), and cellular components (CC). In SRS, 3206 proteins were detected and identified, but 5962 MF, 2542 BP, and 1399 CC were obtained from their annotations in UniProt. Some proteins have more than one annotation and others have none [39].
    > For MF, 478 different functions were obtained, but 625 proteins did not have any annotation (Figure 8). The most recurrent functions were ATP binding [GO:0005524] and DNA binding [GO:0003677] with 904 and 302 annotations, respectively.

### [9] Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts
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
  - Snippet 1 (score: 0.666)
    > Figure S1 GO term enrichment of A. aegypti proteins based on data from Guo et al. [13]. (A) Enriched GO biological process terms. (B) Enriched GO molecular function terms. Light blue bars represent terms for A. aegypti targets, and pink is for terms from DENV-similar proteins. When more than ten terms were enriched for a set of proteins, only the ten most signicant terms are shown. Bonferroni corrected p-values were transformed by -log10. The following abbreviations are used: "translation factor nucleic acid bind" is "translation factor activity nucleic acid binding," and "macromolecular subunit organiz" is "macromolecular complex subunit organization." Found at: doi:10.1371/journal.pntd.0000954.s001 (1.39 MB TIF)  Table S3 Predicted interactions between DENV2 and human after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the target protein's Uniprot accession, Entrez Gene ID, and Symbol; if the target is a known host factor; and if the predicted interaction was already known in the literature. Found at: doi:10.1371/journal.pntd.0000954.s005 (3.01 MB TXT) Table S4 Predicted interactions between DENV2 and A. aegypti after the CC Filter. Columns include the the DENV protein's Entrez Protein accession or PDB code, Uniprot accession, and name; the DENV-similar protein's PDB code, Uniprot accession, Entrez Gene ID, and Symbol; the D. melanogaster target protein's FlyBase gene number, and Symbol; the A. aegypti target protein's VectorBase protein ID, and Uniprot accession; and if the target is a known host factor. Found at: doi:10.1371/journal.pntd.0000954.s006

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
  - Snippet 1 (score: 0.662)
    > Gene annotation was primarily derived from the S. clavuligerus reference genome in the NCBI database and was annotated using the NCBI Prokaryotic Genome Annotation Pipeline 59 . However, several CA biosynthetic genes were manually corrected based on published literature 9 . For instance, two loci were originally annotated as clavaminate synthase 1 (cas1), but one of these loci is located near the cephamycin C biosynthetic cluster, indicating it was actually cas2. Following this correction, the RefSeq accession numbers of all genes in the reference genome were cross-referenced with the UniProt database to obtain additional annotations 60 . For the mutated genes identified through ICA, protein existence levels were manually assigned based on the UniProt data, including protein existence status, annotation score, similar proteins, and relevant publications.

### [11] A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes
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
  - Snippet 1 (score: 0.660)
    > Labelling of such a gene as "inactivated" seems biologically correct. This is translated to the CDS qualifier /pseudo in EMBL and securely ensures that the protein translation is not present in UniProt (e.g., searching for OE_1059R results in no hit). When, however, an invalid partial translation product is produced but not tagged as disrupted (as is the case for VNG0034H), then this is considered by EMBL as a "regular" gene (CDS). Such a gene fragment is included as a regular protein in UniProt (VNG0034H is Q9HSX6). Upon superficial analysis, this may be taken as evidence for an "improved" (because less incomplete) genome annotation in strain NRC-1 compared to strain R1. In addition, according to EMBL requirements, the "CDS" coordinates of OE_1059R must be given as 29913-31570, thus covering and including the integrated transposon ISH1 (with its transposase gene). Only a "tolerated" misc_feature annotation allows representation of this disrupted gene in a biologically meaningful way, representing the reconstructed ancestral gene.

### [12] Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences
- Authors: M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al.
- Year: 2025
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
- DOI: 10.3390/ijms262411830
- PMID: 41465260
- PMCID: 12733082
- Summary: This work establishes a foundation for investigating the role of mitochondrial genome variation in key plant’s phenotypic traits, such as the enhanced responsiveness to arbuscular mycorrhiza observed in this agronomically valuable line of Medicago lupulina L. vulgaris Koch.
- Evidence snippets:
  - Snippet 1 (score: 0.653)
    > (ii). Annotation of Protein-Coding Genes Among the 33 ORFs encoding proteins with predicted functions were: nine encoding NADH dehydrogenase subunits, one encoding cytochrome b, three encoding cytochrome C oxidase subunits, five encoding ATP synthase subunits, four responsible for cytochrome C maturation, nine encoding ribosomal proteins, and two with other functions (matR and mttB; Table 1, Figure 2). Among these, the cox2, rps3, nad1, nad5, and rpl2 genes were characterized with potential mutations due to single nucleotide polymorphisms (SNPs). The rpl2 sequence from the VIK32, line MlS-1 mtDNA showed identity with exon 2 of the chloroplast gene encoding ribosomal protein L2. For example, it showed identity with an exon of the line MlS-1 chloroplast gene rplB (OR674883.1; coordinates 78,587-79,084; Cover 69%, Identity 98.3%) (Figure 3), as well as with exon 2 of the chloroplast gene rpl2 from M. lupulina (OM681370.1; Cover 72%, Identity 98.4%) and M. truncatula cultivar Jemalong A17 (MT965675.1; Cover 72%, Identity 97.5%). This sequence also showed high similarity to sequences from the chloroplast genomes of phylogenetically distant plants from the genera Trigonella, Melilotus, Lathyrus, and Pisum (Cover 97%, Identity 95.6-96.2%). The 45 protein-coding genes were characterized as genes encoding hypothetical proteins (Figure 2).

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
  - Snippet 1 (score: 0.651)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [14] Gene Nomenclature System for Rice
- Authors: S. McCouch
- Year: 2008
- Venue: Rice
- URL: https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
- DOI: 10.1007/s12284-008-9004-9
- Citations: 383
- Influential citations: 9
- Summary: A set of standard procedures for describing genes based on DNA, RNA, and protein sequence information that have been annotated and mapped on the sequenced genome assemblies, as well as those determined by biochemical characterization and/or phenotype characterization by way of forward genetics are outlined.
- Evidence snippets:
  - Snippet 1 (score: 0.651)
    > The name of a protein encoded by a particular gene should be consistent with the gene full name in cases where the gene name is based on phenotype or molecular function (refer to the "Gene full name" section), except that the protein name is written using all upper case characters without italics. If, at a later stage, a gene and its corresponding protein product are determined to have a biochemically characterized molecular function, such as an enzyme or a structural component (subunit) of a macromolecular complex, the protein should be assigned a synonym consistent with the enzyme nomenclature recommended by the IUPAC Enzyme Commission or the macromolecule name adapted by the IUBMB [4]. Because there may be several functional assignments for a given protein (i.e., based on a phenotypic assay, a biochemical assay, or a molecular function), there may be several synonyms for the protein name (and similarly, for the gene full name). The protein symbol should always be consistent with the adopted gene symbol, with the exception that protein symbols are written using all upper case characters without italics, followed by a space and the numeric locus designator. For example, the GLUTINOUS ENDOSPERM 1 (WX1) gene encodes the granule-bound starch synthase enzyme (EC: 2.4.1.11). The protein name is GLUTINOUS ENDOSPERM 1 and the symbol is 'WX1'. The protein name(s), 'WAXY', 'WAXY 1', and GRANULE-BOUND STARCH SYNTHASE (GBSS) will be recorded as synonyms. If a name cannot be assigned based on phenotype, known biochemistry, or other experimental evidence supporting its function, a systematic locus identifier (described above) and a name consistent with the description in Table 1 must be used to describe the gene until its function can be confirmed.

### [15] GeneTools – application for functional annotation and statistical hypothesis testing
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
  - Snippet 1 (score: 0.650)
    > The database enables searching by gene symbols/names, GenBank accession numbers, UniGene cluster IDs, Swiss-Prot entry names and several unique clone IDs (IMAGE clone IDs, University of Iowa clone IDs, Operon oligo IDs, TAIR IDs and a subset of selected Affymetrix and Agilent IDs).
    > The names and symbols of genes/proteins may be highly ambiguous [20]. We therefore recommend using primary gene IDs, like GeneBank accession numbers or specific probe IDs when querying the database. However, if gene names or symbols are used, caution is advised because only official names/symbols associated with UniProt knowledgebase will be recognized. The underlying database is updated on a weekly basis with annotation information from several external databases including UniGene, Swiss-Prot, Entrez Gene and GO. User data are submitted to the database as text files of gene reporters and analysis of the annotation data can be performed through three user interfaces: the NMC Annotation Tool, the GO Annotator Tool and eGOn. Analysis results and annotation data can be exported in various formats.

### [16] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
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
  - Snippet 1 (score: 0.647)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [17] Transcriptome profiling of the salt-stress response in Triticum aestivum cv. Kharchia Local
- Authors: E. Goyal, S. Amit, R. Singh, A. K. Mahato, S. Chand et al.
- Year: 2016
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/6349c048991a40b0e6ddec573990e5a9e0149914
- DOI: 10.1038/srep27752
- PMID: 27293111
- PMCID: 4904219
- Citations: 92
- Influential citations: 3
- Summary: The transcriptome data is the first report, which offers an insight into the mechanisms and genes involved in salt tolerance, which can be used to improve salt tolerance in elite wheat cultivars and to develop tolerant germplasm for other cereal crops.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > Only 83.18% of these unigenes are represented in public database. Based on the annotation, some of the unigenes were closely related with the plant stress functions i.e. stress tolerance function (salt responsive protein, salt overly sensitive 1, salt tolerant like protein, salt induced protein, sodium hydrogen exchanger, sodium calcium exchanger, universal stress protein, stress protein, calcineurin B like protein, CBL-interacting protein kinase family), signal transduction (calmodulin, calcium calmodulin dependent protein kinase), energy production and conversion (ATP synthase beta subunit, ATP synthase subunit d, ATP synthase delta subunit, ATP binding protein, ATP citrate synthase, vacuolar ATP synthase subunit b, vacuolar ATPase b subunit, vacuolar type H + ATPase, vacuolar proton ATPase b subunit) and inorganic ion transport (Na + /H + antiporter, vacuolar proton-inorganic pyrophosphatase, transmembrane protein, plasma membrane H + -ATPase) (Supplementary Table S1). These putative functional unigenes identified in the present study, can provide leads for future investigations and valuable information for deciphering the putative function of novel genes. However, detailed studies are needed to understand their precise roles and functions.
    > Out of all the assembled unigenes, 12,199 unigenes were classified into 32 functional groups with 48.66% to biological process, 24.39% to molecular function and 26.95% to cellular component. This is indicative of the tissues undergoing extensive metabolic activities. Genes involved in some important biological processes such as response to stimulus (9.14%), single organism process (14.34%) and biological regulation (6.99%) were also identified. This was mostly in harmony with other analysis of DEG(s) under salt stress conditions (Fig. 2). These results suggest that T. aestivum may have unique genes that regulate the response to salt stress. Logically, genes encoding these functions may be more conserved across different species and are thus easier to annotate in the database.

### [18] Transcriptomic Characterization of Bradyrhizobium diazoefficiens Bacteroids Reveals a Post-Symbiotic, Hemibiotrophic-Like Lifestyle of the Bacteria within Senescing Soybean Nodules
- Authors: Sooyoung Franck, Kent N Strodtman, Jing Qiu, D. Emerich
- Year: 2018
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/15b1a0b897a7f157d3c395b1199379e426fcc902
- DOI: 10.3390/ijms19123918
- PMID: 30544498
- PMCID: 6321122
- Citations: 7
- Summary: The transcriptional activity of Bradyrhizobium diazoefficens isolated from soybean nodules was monitored over the period from symbiosis to late plant nodule senescence and indicates that the bacteria are responding to the changing environment within the nodule as the plant cells progress from an organized cellular structure to an unorganized state of internal decay.
- Evidence snippets:
  - Snippet 1 (score: 0.647)
    > Among the functionally annotated genes expressed at 71 and 95 DAP are several ABC transport ATP-binding proteins, including bll3190, blr3340, and blr3544 and the α-ketoglutarate permease bll2904, and several proteins of sulfur metabolism, including the glutathione S-transferase-like protein bll4398, the cystathionine beta lyase bll4445, and the cysteine synthase bll4453. The genes that are more actively transcribed at 95 DAP include the regulatory proteins blr2424, blr5109, and blr0155, the ABC permease proteins blr5304 and blr7869, the potassium uptake protein blr3802, the small heat shock protein blr5220, and the metabolic proteins, including the phospholipid N-methytransferase blr0681, the acetyl CoA synthase blr3924, the indolepyruvate ferredoxin oxidoreductase, alpha subunit, bll3411, the ribulose 1,5-bisphosphate carboxylase/oxygenase small subunit blr2586, the gluconolactonase precursor bll2956, the 3-oxoadipate CoA-transferase subunit A bll3462, and the glutathione reductase blr3757. These genes add to the composite of the genes represented in the other patterns, demonstrating a metabolically viable micro-organism.

### [19] Effect of Chloroplast ATP Synthase on Reactive Oxygen Species Metabolism in Cotton
- Authors: Li Zhang, Panpan Jing, Biao Geng, Jinlong Zhang, Jinjiang Shi et al.
- Year: 2024
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/14cea2fae2e9777d5d816f3b80da48f328b78e31
- DOI: 10.3390/ijms252312707
- PMID: 39684418
- PMCID: 11640765
- Citations: 1
- Summary: The results of the study show that the ATP synthase subunit genes atpE and atpF are closely linked with ROS metabolism, which provides basic information for the functional analysis of ATP synthase in cotton.
- Evidence snippets:
  - Snippet 1 (score: 0.644)
    > Chloroplast DNA is a double-stranded covalent closed-ring molecule in higher plants that varies in length in different species. Following genome assembly, the chloroplast genome length in Jin A-CMS was found to be 160,042 bp (Figure 1). The genome consists of 131 genes, including 112 functional genes (79 protein-coding genes, 29 tRNA genes, and 4 rRNA genes) and 19 repeat genes (Table 1). 4), and a total of 86 protein-coding genes (including 79 genes and 7 duplicate genes, all encoding proteins) were annotated. The base composition and gene distribution of each component region (LSC/SSC/IR) were determined, and this information is summarized in Table 2. Four typical regions were identified: LSC (55.37%), SSC (12.63%), and two IRs (15.99%). Functional analysis of the genome revealed that most of the genes are related to photosystem and ATP synthesis (Table 3). There are 5 genes encoding PSI subunits, 15 genes encoding PSII subunits, 12 genes encoding NADH dehydrogenase, 6 genes encoding cytochrome b/f, 6 genes encoding ATP synthase, and 1 gene encoding Rubisco large subunits. In addition, there are 9 genes encoding ribosome large subunit proteins, 12 genes encoding ribosome small subunit proteins, 4 genes encoding DNA-dependent RNA polymerase, 4 genes encoding ribosomal RNAs, and 28 genes encoding transfer RNAs. Other identified genes include a maturase enzyme-encoding gene (matK), a protease gene (clpP1), an envelope protein-encoding gene (cemA), an acetyl-CoA carboxylase gene (accD), and a cytochrome synthesis gene (ccsA). In addition, five genes of unknown function were identified. Five reference databases were used for gene annotation, among which the Swiss-Prot database was used to annotate the largest number of genes (Table 4), and a total of 86 protein-coding genes (including 79 genes and 7 duplicate genes, all encoding proteins) were annotated.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
2. Xia-lian Bu, Weishan Zhao, Wenxiang Li, H. Zou, Ming Li et al. (2023). Comparative Transcriptomics of Chilodonella hexasticha and C. uncinata Provide New Insights into Adaptations to a Parasitic Lifestyle and Mdivi-1 as a Potential Agent for Chilodonellosis Control. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/d4398b01c3bebfec9c074dd0fe83508f7be50ce7
3. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211
4. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
5. Stefania D'Alessio, Katherine M. Buckley, I. Kraev, P. Hayes, S. Lange (2021). Extracellular Vesicle Signatures and Post-Translational Protein Deimination in Purple Sea Urchin (Strongylocentrotus purpuratus) Coelomic Fluid—Novel Insights into Echinodermata Biology. Biology. https://www.semanticscholar.org/paper/e2b33d9697175a6e724fdb85e3ac2ec169d92871
6. M. Efremova, Miquel Vento-Tormo, S. Teichmann, R. Vento-Tormo (2020). CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes. Nature Protocols. https://www.semanticscholar.org/paper/6a3b3e4a2eebc3fad3b03ee6d8228264247abbc8
7. S. Chivasa, Daniel Tomé, John M U Hamilton, A. Slabas (2010). Proteomic Analysis of Extracellular ATP-Regulated Proteins Identifies ATP Synthase β-Subunit as a Novel Plant Cell Death Regulator*. Molecular & Cellular Proteomics. https://www.semanticscholar.org/paper/097975eee8336bdf9785e2d0316e5bf8f2e2edde
8. Jesús Barrera-Rojas, K. J. Gurubel-Tun, Emmanuel Ríos-Castro, M. López-Méndez, B. Sulbarán-Rangel (2023). An Initial Proteomic Analysis of Biogas-Related Metabolism of Euryarchaeota Consortia in Sediments from the Santiago River, México. Microorganisms. https://www.semanticscholar.org/paper/90322d59d4f96d5bfe50890815bd2bdf223dcb79
9. J. Doolittle, S. Gomez (2011). Mapping Protein Interactions between Dengue Virus and Its Human and Insect Hosts. PLoS Neglected Tropical Diseases. https://www.semanticscholar.org/paper/baff9e82a73e77a021118c0910a5874568cd60b3
10. J. Gong, Jeong Sang Yi, Seungchan An, Hang Su Cho, Chang Hun Shin et al. (2025). Integrated genomic-transcriptomic analysis of clavulanic acid production in differentially productive Streptomyces clavuligerus strains. Scientific Reports. https://www.semanticscholar.org/paper/b4903d3729bba93d1d47e38f3353a26f3530a8dd
11. F. Pfeiffer, D. Oesterhelt (2015). A Manual Curation Strategy to Improve Genome Annotation: Application to a Set of Haloarchael Genomes. Life. https://www.semanticscholar.org/paper/f5983d01e0ac838554f7f5c29481d70a9d728c30
12. M. Vladimirova, M. Roumiantseva, A. S. Saksaganskaia, A. P. Kozlova, V. Muntyan et al. (2025). Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/330ca6bee6a495267fb0c36453382e2fa3b4a6fc
13. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
14. S. McCouch (2008). Gene Nomenclature System for Rice. Rice. https://www.semanticscholar.org/paper/a3a888f2a605aa89ad11eb7f205bf243967cad1a
15. V. Beisvåg, Frode K. R. Jünge, Hallgeir Bergum, Lars Jølsum, S. Lydersen et al. (2006). GeneTools – application for functional annotation and statistical hypothesis testing. BMC Bioinformatics. https://www.semanticscholar.org/paper/1d9e0c2f67acd5bf64c659f1f3f8624325b6be8a
16. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
17. E. Goyal, S. Amit, R. Singh, A. K. Mahato, S. Chand et al. (2016). Transcriptome profiling of the salt-stress response in Triticum aestivum cv. Kharchia Local. Scientific Reports. https://www.semanticscholar.org/paper/6349c048991a40b0e6ddec573990e5a9e0149914
18. Sooyoung Franck, Kent N Strodtman, Jing Qiu, D. Emerich (2018). Transcriptomic Characterization of Bradyrhizobium diazoefficiens Bacteroids Reveals a Post-Symbiotic, Hemibiotrophic-Like Lifestyle of the Bacteria within Senescing Soybean Nodules. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/15b1a0b897a7f157d3c395b1199379e426fcc902
19. Li Zhang, Panpan Jing, Biao Geng, Jinlong Zhang, Jinjiang Shi et al. (2024). Effect of Chloroplast ATP Synthase on Reactive Oxygen Species Metabolism in Cotton. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/14cea2fae2e9777d5d816f3b80da48f328b78e31