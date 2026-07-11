---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-07T04:15:08.254613'
end_time: '2026-07-07T04:15:15.164899'
duration_seconds: 6.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nudC
  gene_symbol: nudC
  uniprot_accession: Q88FQ8
  protein_description: 'RecName: Full=NAD-capped RNA hydrolase NudC {ECO:0000255|HAMAP-Rule:MF_00297};
    Short=DeNADding enzyme NudC {ECO:0000255|HAMAP-Rule:MF_00297}; EC=3.6.1.- {ECO:0000255|HAMAP-Rule:MF_00297};
    AltName: Full=NADH pyrophosphatase {ECO:0000255|HAMAP-Rule:MF_00297}; EC=3.6.1.22
    {ECO:0000255|HAMAP-Rule:MF_00297};'
  gene_info: Name=nudC {ECO:0000255|HAMAP-Rule:MF_00297}; OrderedLocusNames=PP_4029;
    ORFNames=PP4029;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the Nudix hydrolase family. NudC subfamily.
  protein_domains: NAD-cap_RNA_hydrolase_NudC. (IPR050241); NADH_PPase-like_N. (IPR015375);
    NudC-like_C. (IPR049734); NUDIX_hydrolase-like_dom_sf. (IPR015797); NUDIX_hydrolase_dom.
    (IPR000086)
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
- **UniProt Accession:** Q88FQ8
- **Protein Description:** RecName: Full=NAD-capped RNA hydrolase NudC {ECO:0000255|HAMAP-Rule:MF_00297}; Short=DeNADding enzyme NudC {ECO:0000255|HAMAP-Rule:MF_00297}; EC=3.6.1.- {ECO:0000255|HAMAP-Rule:MF_00297}; AltName: Full=NADH pyrophosphatase {ECO:0000255|HAMAP-Rule:MF_00297}; EC=3.6.1.22 {ECO:0000255|HAMAP-Rule:MF_00297};
- **Gene Information:** Name=nudC {ECO:0000255|HAMAP-Rule:MF_00297}; OrderedLocusNames=PP_4029; ORFNames=PP4029;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the Nudix hydrolase family. NudC subfamily.
- **Key Domains:** NAD-cap_RNA_hydrolase_NudC. (IPR050241); NADH_PPase-like_N. (IPR015375); NudC-like_C. (IPR049734); NUDIX_hydrolase-like_dom_sf. (IPR015797); NUDIX_hydrolase_dom. (IPR000086)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nudC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nudC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nudC** (gene ID: nudC, UniProt: Q88FQ8) in PSEPK.

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
- Snippets retrieved: 20

## Relevant Papers

### [1] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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

### [2] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.702)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

### [3] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.697)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [4] Small Sized Yet Powerful: Nuclear Distribution C Proteins in Plants
- Authors: V. Vassileva, Mariyana Georgieva, D. Todorov, K. Mishev
- Year: 2023
- Venue: Plants
- URL: https://www.semanticscholar.org/paper/c14d91e7650393cbf1c0d65953e71ec87cacc01b
- DOI: 10.3390/plants13010119
- PMID: 38202427
- PMCID: 10780334
- Summary: This review synthesizes past and current research on NudC family members, focusing on their growing importance in plants and intricate contributions to plant growth, development, and stress tolerance, and outlines future research avenues centering on the exploration of under investigated functions of NudC proteins in plants.
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > Investigating the NudC interactions with specific protein partners which play an essential role in plant growth, development, and stress responses is of utmost importance. The dissection of the NudC protein interactome requires the generation of NudC gene versions with affinity purification tags, as well as fluorescent protein-tagged versions for further validation of the putative protein-protein interactions. Besides the interactomic studies, other systems biology approaches should also provide an added value to our knowledge of the role of plant NudC proteins. As outlined above, there is already some experimental evidence for the direct involvement of BOB1 in auxin-mediated processes. Hence, hormone profiling in lines with altered NudC expression will associate the observed growth phenotypes with the changes in the composition and quantity of endogenous phytohormones and their precursors, conjugates, and degradation products. Such findings, particularly their connection to temperature fluctuations and hormonal responses, offer the potential to unveil novel and essential aspects of plant functioning. An additional avenue of research may involve in-depth structural analyses of NudC domains in plant species to elucidate differences in structural features of plant NudC domains compared to other organisms, and how these distinctions correlate with plantspecific functions. A possible approach in this respect could be the design of chimeric NudC versions with swapped protein domains from other eukaryotic organisms. The expression of such gene constructs in Arabidopsis mutants with impaired NudC gene expression would be instrumental in addressing the capability for functional complementation based on conserved protein signatures. This notwithstanding, expression of plant NudC genes in heterologous systems, such as yeast and mammalian An additional avenue of research may involve in-depth structural analyses of NudC domains in plant species to elucidate differences in structural features of plant NudC domains compared to other organisms, and how these distinctions correlate with plantspecific functions. A possible approach in this respect could be the design of chimeric NudC versions with swapped protein domains from other eukaryotic organisms. The expression of such gene constructs in Arabidopsis mutants with impaired NudC gene expression would be instrumental in addressing the capability for functional complementation based on conserved protein signatures.
  - Snippet 2 (score: 0.667)
    > The expression of such gene constructs in Arabidopsis mutants with impaired NudC gene expression would be instrumental in addressing the capability for functional complementation based on conserved protein signatures. This notwithstanding, expression of plant NudC genes in heterologous systems, such as yeast and mammalian cells, would shed light on the extent of functional homology when it comes to cell cycle progression.
    > The distinctive chaperone activities of NudC proteins in plants warrant comprehensive exploration. It appears that the members of this protein family might orchestrate the functioning of many HSP proteins through differential interactions depending on the environmental context. Further experiments with truncated protein versions and with the aforementioned chimeric constructs would elucidate the significance of specific protein motifs for the composition of the NudC protein interactome within the heat shock granules. A comprehensive understanding of the plant-specific chaperone network involving NudC proteins will further illuminate the molecular mechanisms of plant stress resilience. In addition to this, the advances in next-generation sequencing technologies have recently enabled the dissection of heat stress regulation modules [90]. Such thorough studies of the transcriptional signatures would shed light on the NudC gene coexpression networks in response to unfavorable conditions. In summary, the ongoing studies on NudC proteins in plants hold the promise of revealing a wealth of knowledge that can significantly advance our comprehensive understanding of regulatory mechanisms at the whole-plant level. The obtained information could ultimately fuel novel strategies for enhancing crop productivity and strengthening plant resilience in response to environmental challenges. Notably, the structural and functional conservation of NudC proteins across species hints at their potential applications in medical research. Investigating NudC roles in cell division, microtubule regulation, and related pathways may lead to insights into human diseases and therapeutic opportunities. Realizing the full potential of NudC proteins necessitates further research and interdisciplinary collaboration. These endeavors hold the key to unlocking the profound benefits that NudC proteins can offer to plant biology and medical science.

### [5] Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates
- Authors: Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa
- Year: 2023
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
- DOI: 10.1101/2023.09.20.558425
- Citations: 1
- Summary: It is found that proteins initiating LLPS are frequently implicated in somatic cancers, even surpassing their involvement in neurodegeneration, and protein regions driving condensate formation show an increased association with DNA- or chromatin-binding domains of transcription regulators within OFPs, indicating a common molecular mechanism underlying several soft tissue sarcomas and hematologic malignancies.
- Evidence snippets:
  - Snippet 1 (score: 0.695)
    > We defined the subcellular localization for each protein in the human proteome by integrating data from Gene Ontology annotations in UniProt (GOA), UniProt annotations, the Human Transmembrane Proteome (HTP) 121 , MatrixDB 122 , and MatrisomeDB 123 . We divided the UniProt and the Gene Ontology annotations (GOA) into tier 1 (more reliable) and tier 2 (less reliable) annotations, depending on the attached evidence codes. For UniProt, annotations with the evidence codes ECO:0000269 or ECO:0000305 are considered as tier 1, while annotations with evidence codes ECO:0000250, ECO:0000255, or ECO:0000303 are tier 2. For Gene Ontology, annotations with evidence codes IDA, IMP, IPI, IGI, EXP, IBA, IKR, TAS, NAS, IC, or ND are tier 1, while annotations with evidence codes HDA, ISS, ISA, RCA, ISO, ISM, IGC, or IEA are tier 2. Based on these, each protein was assigned exactly one broad localization. It was considered to be a transmembrane protein (TMP), if it is assigned the 'integral component of membrane (GO:0016021)' GO term in tier 1 GOA annotations, or it is annotated as a TMP in HTP with a confidence score over 85, or is annotated in HTP as a TMP with a confidence score above 50 and is also annotated as a TMP in GOA (either tier).

### [6] Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana
- Authors: K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al.
- Year: 2020
- Venue: Journal of Food Science and Engineering
- URL: https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
- DOI: 10.17265/2159-5828/2020.02.001
- Summary: Baccaurea motleyana (rambai) is underutilized fruits that are native to Malaysia, Indonesia and Thailand and used for simple sequence repeat (SSR) analysis by MIcroSAtellite (MISA).
- Evidence snippets:
  - Snippet 1 (score: 0.695)
    > To get comprehensive gene function of rambai genes, gene annotation to seven databases, namely National Center for Biotechnology Information (NCBI) non-redundant protein sequences (NR), NCBI nucleotide sequences (NT), Kyoto Encyclopedia of Genes and Genome Ortholog (KO), SwissProt, Protein family (Pfam), Gene Ontology (GO) and Cluster of Orthologous Groups (KOG), was used as reference.
    > The NCBI non-redundant protein sequences (NR), include protein sequence information from GenBank, Protein Data Bank (PDB), SwissProt, Protein Information Resource (PIR) and Protein Research Foundation (PRF). The NCBI nucleotide sequences (NT) are the nucleotide sequence database that includes nucleotide sequence from GenBank of the European Bioinformatics Institute (EMBL) and DNA Data Bank of Japan (DDBJ). KEGG is a database resource for understanding high-level functions and utilities of the biological system, such as cell, organism and ecosystem, from molecular-level information, especially for large-scale molecular datasets generated by genome sequencing and other high-throughput experimental technologies. KEGG is an established Cluster of Orthologous (KO) annotation system that can accomplish the function annotation of the genome/transcriptome of a newly sequenced species. SwissProt is a manual annotated and reviewed protein sequence database that has a high-quality protein sequence database from experimental results, computed features and scientific conclusions. Pfam is comprehensive collection of protein domains and families, represented as multiple sequence alignments and as profile of hidden Markov models. Many proteins are composed of structural domains, and the protein sequence of a specific structural domain possesses a certain degree of conservative property. GO is the established standard for the functional annotation of gene products and controlled vocabulary used to classify the functional attributes of gene products of a biological process, a molecular function and a cellular component.

### [7] A Multi-Label Learning Framework for Drug Repurposing
- Authors: Suyu Mei, Kun Zhang
- Year: 2019
- Venue: Pharmaceutics
- URL: https://www.semanticscholar.org/paper/6025d6668bd544c1f3cbb8e4433c549b4f7eed03
- DOI: 10.3390/pharmaceutics11090466
- PMID: 31505805
- PMCID: 6781509
- Citations: 18
- Influential citations: 1
- Summary: The proposed multi-label learning framework is used to predict new drugs for the known target genes, identify new genes for the old drugs, and infer new associations between old drugs and new disease phenotypes via the OMIM database.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > The gene, NUDC, plays indispensable roles in neurogenesis, neuronal migration, correct formation of mitotic spindles, chromosome separation during mitosis, cytokinesis, and cell proliferation (https://www.uniprot.org/uniprot/Q9Y266). The protein, NUDC, is mainly located in the nucleus (GO:0005634), cytoplasm (GO:0005737), cytoskeleton (GO:0005856), and microtubule (GO:0005874), etc., and participates in the major biological processes of the cell cycle (GO:0007049), multicellular organismal development (GO:0007275), cell differentiation (GO:0030154), cell division (GO:0051301), and developmental process (GO:0032502). The analyses show that the predicted novel gene, NUDC, and the known genes targeted by drug CIDm00004156 (trideuteriomethyl methanesulfonate) share highly similar patterns of subcellular localization and biological processes. In this sense, it may be safely assumed that drug CIDm00004156 could be clinically repurposed for the diseases caused by the gene, NUDC. The gene, NUDC, plays indispensable roles in neurogenesis, neuronal migration, correct formation of mitotic spindles, chromosome separation during mitosis, cytokinesis, and cell proliferation (https://www.uniprot.org/uniprot/Q9Y266). The protein, NUDC, is mainly located in the nucleus (GO:0005634), cytoplasm (GO:0005737), cytoskeleton (GO:0005856), and microtubule (GO:0005874), etc., and participates in the major biological processes of the cell cycle (GO:0007049), multicellular organismal development (GO:0007275), cell differentiation (GO:0030154), cell division (GO:0051301), and developmental process (GO:0032502).
  - Snippet 2 (score: 0.683)
    > Meanwhile, these genes majorly get involved in the biological processes of regulation of transcription DNA-dependent (GO:0006355), transcription DNA-dependent (GO:0006351), cell cycle (GO:0007049), multicellular organismal development (GO:0007275), DNA repair (GO:0006281), and cell differentiation (GO:0030154). The gene, NUDC, plays indispensable roles in neurogenesis, neuronal migration, correct formation of mitotic spindles, chromosome separation during mitosis, cytokinesis, and cell proliferation (https://www.uniprot.org/uniprot/Q9Y266). The protein, NUDC, is mainly located in the nucleus (GO:0005634), cytoplasm (GO:0005737), cytoskeleton (GO:0005856), and microtubule (GO:0005874), etc., and participates in the major biological processes of the cell cycle (GO:0007049), multicellular organismal development (GO:0007275), cell differentiation (GO:0030154), cell division (GO:0051301), and developmental process (GO:0032502). The analyses show that the predicted novel gene, NUDC, and the known genes targeted by drug CIDm00004156 (trideuteriomethyl methanesulfonate) share highly similar patterns of subcellular localization and biological processes. In this sense, it may be safely assumed that drug CIDm00004156 could be clinically repurposed for the diseases caused by the gene, NUDC. The gene, NUDC, plays indispensable roles in neurogenesis, neuronal migration, correct formation of mitotic spindles, chromosome separation during mitosis, cytokinesis, and cell proliferation (https://www.uniprot.org/uniprot/Q9Y266).

### [8] Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes
- Authors: Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer
- Year: 2023
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
- DOI: 10.1093/nar/gkad385
- PMID: 37216585
- PMCID: 10320097
- Citations: 8
- Summary: The new implementation of the CUPP-webserver, https://cupp.info/, now includes all published fungal and algal genomes from the Joint Genome Institute (JGI), genome resources My coCosm and PhycoCosm, dynamically subdivided into motif groups of CAZymes, allowing users to browse the JGI portals for specific predicted functions or specific protein families from genome sequences.
- Evidence snippets:
  - Snippet 1 (score: 0.684)
    > To inspect the transcriptomics result of individual genes, proteins originating from JGI have a hyperlink to a summary page which links to a 'Genome browser' page that displays the predicted gene splicing, including which regions have RNA support (Figure 1 D).
    > Hence, in the protein specific site in the JGI w e bsite under 'To Genome Browser', the current protein (GeneCatalog) can be seen together with se v eral other alternati v e predictions of the gene splicing, which is essential to have correct, for the protein to function naturally (Figure 2 ).
    > As the RNA coverage supports the exon / intron splicing, it is possible to infer whether a particular gene, in this case Table 1. Comparison between the dbCAN webserver, the eggNOG webserver for both family and functional annotation of CAZymes and the updated CUPP-w e bserver using the recommended significance cut-off at 5. The column 'CAZy -All characterized' encompasses all 10784 characterized proteins in the CAZy database used for the training, whereas the 'CAZy -Newly characterized '   a gene such as the one selected in Figure 2 , is more likely to work after heterologous gene expression.
    > To further improve the enzyme selection, all NCBI Genbank accessions were mapped to Uniprot ID to link to the specific Uniprot accession page including the predicted Al-phaFold structures, Go annotations and InterPro annotations and more ( 19 ).

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
  - Snippet 1 (score: 0.669)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [10] Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir
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
  - Snippet 1 (score: 0.667)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [11] Basidioascus undulatus: genome, origins, and sexuality
- Authors: Hai D. T. Nguyen, D. Chabot, Y. Hirooka, R. Roberson, K. Seifert
- Year: 2015
- Venue: IMA Fungus
- URL: https://www.semanticscholar.org/paper/a5deb29da5109780b4d55dfa35ea0d9fe13216d5
- DOI: 10.5598/imafungus.2015.06.01.14
- PMID: 26203425
- PMCID: 4500085
- Citations: 12
- Influential citations: 1
- Summary: Nuclear staining and confocal microscopy showed meiosis occurring in basidia and genome analysis confirmed the existence of genes involved in meiosis and mating, leading to a move out of the Wallemiomycetes and into the new class Geminibasidiales cl. nov.
- Evidence snippets:
  - Snippet 1 (score: 0.659)
    > run on the scaffolds to detect the percentage of conserved eukaryotic genes (CEGs).
    > Genome annotation was performed following established guidelines (Haas et al. 2011 (Slater & Birney 2005). Predicted gene models exhibiting strong evidence by exon alignment were exported as protein sequences and coding nucleotide sequences (CDS). Predicted gene models lacking evidence from exon alignment were discarded in downstream analyses. To determine function, the protein sequences were used as input for InterProScan 5RC6 (Jones et al. 2014) (parameters: -dp -f -t p -iprlookup -pa -goterms) and were also compared to the manually curated protein data set from UniProt/Swiss-Prot by blastp v. 2.2.28+. The results in XML format from blastp v. 2.2.28+ and InterProScan were loaded into Blast2GO v. 2.7.1 (Conesa et al. 2005) and merged to create an annotation table (available from the first author on request). The gene models with BLAST hits having e-value of less than 1.0E -100 and mean similarity hit of ≥ 70% were assumed to be orthologs and they were given names following recommended conventions (http:// www.uniprot.org/docs/proknameprot). Ribosomal RNA's were predicted by RNAmmer v. 1.2 (Lagesen et al. 2007). Data files are publicly available at NCBI (Genome Accession No. JTLS00000000 version JTLS01000000; BioProject Accession No. PRJNA247992) and JGI MycoCosm portal (Grigoriev et al. 2014).

### [12] AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes
- Authors: D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al.
- Year: 2023
- Venue: Mammalian Genome
- URL: https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99
- DOI: 10.1007/s00335-023-10008-1
- PMID: 37460664
- PMCID: 10382368
- Citations: 5
- Summary: This work presents genome visualization and annotation tools to support seven livestock species, available in a new resource called AgAnimalGenomes, and describes the data and search methods available and how to use the provided tools to edit and create new gene models.
- Evidence snippets:
  - Snippet 1 (score: 0.657)
    > As previously described (Triant et al. 2020), once a proteincoding gene annotation is complete, each new or modified isoform should be compared to a well-curated protein sequence database to check for congruency with known proteins. The sequence of an annotation is obtained by right clicking it and selecting Get Sequence. The first choice of database to search is the well-curated UniProtKB/Swissprot database using BLAST at either the UniProt (https:// www. unipr ot. org/ blast) or NCBI website (https:// blast. ncbi. nlm. nih. gov/ Blast. cgi) (Sayers et al. 2023a;UniProt Consortium 2023). If there is no match with a significant e-value (< 1e−05) in UniProtKB/Swissprot, the next database to try is the Model Organisms (landmark) database at NCBI. If that fails, select the RefSeq Proteins database and exclude your organism of interest from the search. Although RefSeq includes computationally predicted and hypothetical proteins, an alignment to a homologous protein from another organism provides support for the annotation. An alignment that covers the full length of both the annotated protein and the database protein sequence suggests the annotation is correct. An alignment that encompasses the full length of an annotated protein sequence but only part of a database protein suggests that the annotation is truncated. You may be able to correct the annotation with additional evidence, but if there is not sufficient evidence the issue can be noted in the Annotation Information Panel under the Comment tab. A partial alignment of an annotated protein to a database protein suggests the annotation has a reading frame shift or was extended incorrectly. Aligning the coding sequence (CDS) to the protein database will reveal whether the problem is due to a reading frame shift. Further annotation editing should be performed to correct the reading frame. If an incorrect extension was due to the merging of two genes, you should edit or redo the annotation. Any unresolved issues should be entered in the Comment section of the Annotation Information Panel.

### [13] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.652)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

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
  - Snippet 1 (score: 0.649)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [15] RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications
- Authors: Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al.
- Year: 2025
- Venue: Nucleic Acids Research
- URL: https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
- DOI: 10.1093/nar/gkaf1206
- PMID: 41206768
- PMCID: 12807602
- Citations: 2
- Summary: The new RM2Target v2.0 will serve as a foundational resource for exploring RNA epitranscriptomic regulation, enabling investigations into cross-talk among modifications, underlying molecular mechanisms, and disease connections, thereby facilitating both basic research and translational applications in RNA epigenetics.
- Evidence snippets:
  - Snippet 1 (score: 0.648)
    > To obtain basic information on WERs and their target genes, such as official gene symbols, gene IDs, gene types, and genomic locations, gene annotations were downloaded from the GENCODE project [ 44 ] for human and mouse, and from NCBI [ 45 ] and Ensembl [ 46 ] for the other species. Genomic locations were extracted from the corresponding GTF annotation files. Gene symbols were primarily standardized based on the NCBI Gene database [ 45 ] for mRNAs and lncRNAs, GtR-NAdb [ 47 ] for tRNAs, miRbase [ 48 ] for microRNAs, and cir-cBase [ 49 ] for circRNAs. Deprecated or substituted versions of genes were filtered out. The LiftOver [ 50 ] program was employed to convert and unify genomic coordinates across different genome assembly versions.
    > The functional descriptions of WERs were compiled based on the UniProt database [ 51 ] and further supplemented with evidence from relevant publications, with particular emphasis on their functions as RNA modification regulatory proteins.

### [16] Switching of Platelet-activating Factor Acetylhydrolase Catalytic Subunits in Developing Rat Brain*
- Authors: H. Manya, J. Aoki, M. Watanabe, T. Adachi, H. Asou et al.
- Year: 1998
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/90ef28b827b32a144f6af20611ee762390c17052
- DOI: 10.1074/jbc.273.29.18567
- PMID: 9660828
- Citations: 70
- Influential citations: 1
- Summary: Results indicate that α1 expression is restricted to actively migrating neurons in rats and that switching of catalytic subunits from the α1/α2 heterodimer to the α2/ α2 homodimer occurred in these cells during brain development, suggesting that PAF acetylhydrolase plays a role(s) in neuronal migration.
- Evidence snippets:
  - Snippet 1 (score: 0.648)
    > An other gene, nudC, encodes a 22-kDa protein of unknown function, but it shows 68% identity to the C-terminal half of C15 protein, which was originally identified as a prolactin-inducible gene in activated T cells (24). Complementation experiments showed that the full-length mammalian (rat) C15 protein, which has a molecular mass of 45 kDa, is capable of rescuing the nuclear movement defect of nudC mutants (25), indicating that rat C15 protein and fungal nudC protein not only have similar structures, but also serve similar functions. Studies on A. nidulans mutants have shown that the nudC protein regulates the nudF protein post-transcriptionally, suggesting that nudF and nudC proteins interact within cells. In addition to nudF and nudC, two other genes have been identified, nudA and nudG, which encode a cytoplasmic dynein heavy and light chain, respectively (19,20), indicating that cytoplasmic dynein is involved in nuclear migration. Microtubules have been shown to be required for nuclear migration in a wide variety of organisms. Cytoplasmic dynein, a microtubule-dependent, minus end-directed motor (26), apparently provides the motive force for nuclear migration. Genetic studies have located nudF (and also nudC) upstream of dynein (27). Therefore, the nudF gene product, which may be a homolog of the LIS1 gene product, and the PAF acetylhydrolase ␤ subunit may interact with multiple proteins involved in nuclear migration. In fact, Sapir et al. (28) recently demonstrated that the ␤ subunit interacts directly with tubulin and regulates microtubular dynamics. A complex of Ͼ200 kDa may contain such components in addition to the PAF acetylhydrolase subunits. Identification of a protein(s) that interacts with (the subunits of) PAF acetylhydrolase will be essential to elucidate the physiological function of the enzyme.

### [17] Full-length messenger RNA sequences greatly improve genome annotation
- Authors: B. Haas, N. Volfovsky, C. Town, Maxim Troukhan, N. Alexandrov et al.
- Year: 2002
- Venue: Genome Biology
- URL: https://www.semanticscholar.org/paper/c0fef9285e065ae7cb4e470902a1920c9f73e124
- DOI: 10.1186/gb-2002-3-6-research0029
- PMID: 12093376
- PMCID: 116726
- Citations: 200
- Influential citations: 9
- Summary: It is demonstrated that sequencing of large numbers of full-length transcripts followed by computational mapping greatly improves identification of the complete exon structures of eukaryotic genes.
- Evidence snippets:
  - Snippet 1 (score: 0.645)
    > The scientific community has recently witnessed the publication of several large eukaryotic genomes in various stages of completion, including the human genome [1,2], the nematode Caenorhabditis elegans [3], the fruit fly Drosophila melanogaster [4], and the model plant Arabidopsis thaliana [5,6]. Each of these genomes contains over 10,000 genes, and as scientists attempt to study these genes more closely, the need for accurate gene models becomes increasingly apparent. For high-throughput genome sequencing projects, equally rapid high-throughput genome annotation is necessary, and bioinformaticists use a variety of computational methods to generate this annotation. Despite many improvements in recent years, these computational methods still fall short of producing correct models for every gene. In order to improve the annotation and facilitate further research, it is essential that we develop methods to identify genes correctly.
    > Annotation of a gene model should include a precise description of where the genomic DNA sequence is transcribed into messenger RNA, the positions in the mRNA of any and all introns, and the translated protein sequence of the gene. If alternative splice variants are present, these should be annotated as well. Computational methods for genome annotation have several shortcomings that result in the following errors in annotation.
    > Gene prediction programs predict exon boundaries correctly only about 80% of the time, even for the most intensively studied organisms [7][8][9]. Thus a gene with five exons will be completely correct only 0.8 5 = 33% of the time, and genes with more exons will be even less likely to be correct. Gene prediction programs also tend to merge and split gene models. Thus two real genes may be merged into one predicted transcript, or vice versa. In addition, programs to align genomic DNA to protein sequences often miss small exons, especially when the homologous proteins are not well conserved. Annotation protocols also tend to miss short genes.

### [18] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.643)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
2. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508
3. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
4. V. Vassileva, Mariyana Georgieva, D. Todorov, K. Mishev (2023). Small Sized Yet Powerful: Nuclear Distribution C Proteins in Plants. Plants. https://www.semanticscholar.org/paper/c14d91e7650393cbf1c0d65953e71ec87cacc01b
5. Nazanin Farahi, Tamas Lazar, P. Tompa, Bálint Mészáros, Rita Pancsa (2023). Phase-separating fusion proteins drive cancer by dysregulating transcription through ectopic condensates. bioRxiv. https://www.semanticscholar.org/paper/57a63e3228a18d5d68d54eb8303eeb7c0ae29da6
6. K. Nasir, Muhammad Fairuz Mohd Yusof, M. S. F. A. Razak, Siti Norsaidah Ibrahim, Mira Farzana Mohamad Moktar et al. (2020). Discovery of Simple Sequence Repeat Markers through Transcriptome Analysis of Baccaurea motleyana. Journal of Food Science and Engineering. https://www.semanticscholar.org/paper/f99fe2940881ec45ecbd8ba3da7f10b4fb22fc3b
7. Suyu Mei, Kun Zhang (2019). A Multi-Label Learning Framework for Drug Repurposing. Pharmaceutics. https://www.semanticscholar.org/paper/6025d6668bd544c1f3cbb8e4433c549b4f7eed03
8. Kristian Barrett, Cameron J. Hunt, L. Lange, I. Grigoriev, A. Meyer (2023). Conserved unique peptide patterns (CUPP) online platform 2.0: implementation of +1000 JGI fungal genomes. Nucleic Acids Research. https://www.semanticscholar.org/paper/cf508bb4b0c60e0806ee7b9af7440d14c1d31ef2
9. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
10. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular Mechanisms Underlying Response to Influenza in Grey Seals (Halichoerus grypus), a Potential Wild Reservoir. Molecular Ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
11. Hai D. T. Nguyen, D. Chabot, Y. Hirooka, R. Roberson, K. Seifert (2015). Basidioascus undulatus: genome, origins, and sexuality. IMA Fungus. https://www.semanticscholar.org/paper/a5deb29da5109780b4d55dfa35ea0d9fe13216d5
12. D. Triant, Amy T. Walsh, Gabrielle Hartley, B. Petry, Morgan R. Stegemiller et al. (2023). AgAnimalGenomes: browsers for viewing and manually annotating farm animal genomes. Mammalian Genome. https://www.semanticscholar.org/paper/38a969fd5641e503106cb215010f84ea0a271f99
13. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
14. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
15. Xiaoqiong Bao, Qi Jiang, Weixuan Chen, Huiqin Li, Xuan Li et al. (2025). RM2Target v2.0: an updated database for the target genes of writers, erasers, and readers of RNA modifications. Nucleic Acids Research. https://www.semanticscholar.org/paper/15dbf5509222f17a624912633aa05cc9183fcc70
16. H. Manya, J. Aoki, M. Watanabe, T. Adachi, H. Asou et al. (1998). Switching of Platelet-activating Factor Acetylhydrolase Catalytic Subunits in Developing Rat Brain*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/90ef28b827b32a144f6af20611ee762390c17052
17. B. Haas, N. Volfovsky, C. Town, Maxim Troukhan, N. Alexandrov et al. (2002). Full-length messenger RNA sequences greatly improve genome annotation. Genome Biology. https://www.semanticscholar.org/paper/c0fef9285e065ae7cb4e470902a1920c9f73e124
18. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211