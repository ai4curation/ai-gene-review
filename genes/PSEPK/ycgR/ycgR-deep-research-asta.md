---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-09T22:34:13.712338'
end_time: '2026-07-09T22:34:50.923889'
duration_seconds: 37.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ycgR
  gene_symbol: ycgR
  uniprot_accession: Q88EQ6
  protein_description: 'RecName: Full=Flagellar brake protein YcgR; AltName: Full=Cyclic
    di-GMP binding protein YcgR;'
  gene_info: Name=ycgR; OrderedLocusNames=PP_4397;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the YcgR family. .
  protein_domains: PilZ_domain. (IPR009875); Split_barrel_FMN-bd. (IPR012349); T3SS_YcgR.
    (IPR023787); T3SS_YcgR_PilZN. (IPR009926); PilZ (PF07238)
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
- **UniProt Accession:** Q88EQ6
- **Protein Description:** RecName: Full=Flagellar brake protein YcgR; AltName: Full=Cyclic di-GMP binding protein YcgR;
- **Gene Information:** Name=ycgR; OrderedLocusNames=PP_4397;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the YcgR family. .
- **Key Domains:** PilZ_domain. (IPR009875); Split_barrel_FMN-bd. (IPR012349); T3SS_YcgR. (IPR023787); T3SS_YcgR_PilZN. (IPR009926); PilZ (PF07238)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ycgR" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ycgR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ycgR** (gene ID: ycgR, UniProt: Q88EQ6) in PSEPK.

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

### [1] Insertion of a Divergent GAF-like Domain Defines a Novel Family of YcgR Homologues That Bind c-di-GMP in Leptospirales
- Authors: Aline Biazola Visnardi, R. A. Ribeiro, A. S. de Souza, Tania Geraldine Churasacari Vinces, E. Llontop et al.
- Year: 2025
- Venue: ACS Omega
- URL: https://www.semanticscholar.org/paper/cb63e8add821142f662f4f3551b08004b9be8caf
- DOI: 10.1021/acsomega.4c09917
- PMID: 39926552
- PMCID: 11800159
- Citations: 2
- Summary: This study describes a novel signal transduction protein that has gained multiple paralogues in the Leptospiraceae and shows that one member of this protein family from Leptospira interrogans is still a monomeric c-di-GMP binding protein and that these novel YcgR-like proteins have mostly replaced other members of the YcgR family in Leptospiraceae.
- Evidence snippets:
  - Snippet 1 (score: 0.890)
    > Given their similar contexts, both the NpzN domain and these other extensions may be involved in protein−protein and/or protein−membrane interactions.
    > Given the extreme diversity of our sample of YcgR-like proteins, which includes YcgR GAZ and YcgR NpzN , we sought to evaluate whether associations of YcgR-like proteins with other gene families could provide evidence for functional links. We collected 11,980 gene neighborhoods for a nonredundant subset (sequence identity less than or equal to 70%) of the YcgR-like proteins. These loci included up to seven upstream and seven downstream genes of the canonical YcgR, YcgR GAZ , and YcgR NpzN homologues. We found that 3433 of these loci contained at least one gene involved in the flagellum assembly. Considering a binomial model for independent sampling and an estimate of an average of 60 flagellum genes per genome, these results indicate that flagellar genes occur more frequently than expected near loci of YcgR-like proteins (p-value ≤ 4.5 × 10 −59 ). This association is congruent with the known role of YcgR as a flagellum regulator. It is even stronger for the known interaction partners of YcgR, MotA, and MotB, which were found in 202 of the sampled loci (p-value = 0), while 100 of these loci had both a flagellar motor protein and at least one other flagellum marker gene.
    > Using the census of YcgR homologues, we assigned all homologues to five subfamilies, canonical YcgR, YcgR NpzN , YcgR GAZ , PilZN, and PilZ. Canonical YcgR members were recognized, as described above, by the presence of an N-terminal PilZ-like divergent domain (PilZN) and a C-terminal PilZ domain. Recognition of the GAZ and NpzN domains by our custom models was used to assign proteins to the YcgR GAZ and YcgR NpzN subfamilies.

### [2] Cyclic di‐GMP modulates sessile‐motile phenotypes and virulence in Dickeya oryzae via two PilZ domain receptors
- Authors: Yufan Chen, Mingfa Lv, Zhibin Liang, Zhiqing Liu, Jianuan Zhou et al.
- Year: 2022
- Venue: Molecular Plant Pathology
- URL: https://www.semanticscholar.org/paper/ad26c3ab30e53c70801be54958e8800fa593afda
- DOI: 10.1111/mpp.13200
- PMID: 35254732
- PMCID: 9104268
- Citations: 14
- Summary: The findings from this study fill a gap in understanding of how c‐di‐GMP modulates bacterial motility and biofilm formation, and provide useful clues for further elucidation of sophisticated virulence regulatory mechanisms in this important plant pathogen.
- Evidence snippets:
  - Snippet 1 (score: 0.858)
    > The second messenger c-di-GMP can bind to several classes of effector proteins, and most of these proteins do not share sequence or structural similarity with each other. Among them, PilZ domaincontaining proteins were the first to be discovered and are wellstudied c-di-GMP effectors with conserved binding motifs found in a range of bacterial species (Cheang et al., 2019;Galperin & Chou, 2020;Ryan et al., 2012;Ryjenkov et al., 2006). To characterize the signalling pathways of c-di-GMP in D. oryzae EC1, we searched for genes encoding PilZ domain-containing proteins through the Pfam program, which led to the identification of W909_08750 (NCBI accession no. AJC66149) and W909_19655 (NCBI accession no. AJC68175). The gene W909_08750 encodes a YcgR-like protein and W909_19655 encodes a BcsA-like protein. For the convenience of this discussion, these two proteins of strain EC1 were named YcgR and BcsA, respectively. YcgR shares about 35% amino acid identity with its counterpart (PDB: 5Y6F_A) in E. coli K-12 (Table 1), which is known to be a flagellar brake protein involved in motility inhibition (Hou et al., 2020;Paul et al., 2010). BcsA from strain EC1 exhibits over 40% protein identity with homologs in E. coli K-12 and Salmonella typhimurium (Table 1), which represent another family of well-studied PilZ domain-containing proteins involved in cellulose biosynthesis and translocation (Romling & Galperin, 2015).
    > Protein domains were predicted by the simplified modular architecture research tool (SMART) and illustrated by DOG 2.0 software (Ren et al., 2009). YcgR contains YcgR and PilZ domains located in the N-terminus and C-terminus, respectively (Figure 1a).

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
  - Snippet 1 (score: 0.775)
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
  - Snippet 1 (score: 0.765)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [5] The Stand-Alone PilZ-Domain Protein MotL Specifically Regulates the Activity of the Secondary Lateral Flagellar System in Shewanella putrefaciens
- Authors: A. Pecina, Meike Schwan, Vitan Blagotinsek, Tim Rick, Patrick Klüber et al.
- Year: 2021
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/040f09fa7d973fe2167f280646e5de5094bb5d56
- DOI: 10.3389/fmicb.2021.668892
- PMID: 34140945
- PMCID: 8203827
- Citations: 16
- Influential citations: 2
- Summary: A differential c-di-GMP-dependent regulation of the two flagellar systems in a single species is shown, and implicates that PilZ domain-only proteins can also act as molecular regulators to control the flagella-mediated motility in bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.764)
    > The protein is thus much smaller than YcgR (244 aa), FlgZ (263), and MotI (217 aa) as an N-terminal YcgR domain is not present (Figure 1C). The predicted c-di-GMP-binding motifs (RxxxRhxh, DhSxxG; Galperin and Chou, 2020) are fully conserved (Figure 1D). The protein is conserved in a number Shewanella species that possess dual flagellar systems, and the gene it is always located downstream of motB. Potential homologs of Sputcn32_3446 are also present in some species of Aeromonas and Vibrio, but absent from the well-characterized V. parahaemolyticus and V. alginolyticus, which also possess two distinct flagellar systems. We henceforth referred to the protein as MotL, relating to its location within the lateral flagellar gene operon and its differences to YcgR, FlgZ, and MotI with respect to the protein sequence and absence of further domains.
  - Snippet 2 (score: 0.720)
    > To identify the potential c-di-GMP-dependent effectors in Shewanella putrefaciens, we started with a genomic screen for homologs of the previously characterized flagellar regulators. The c-di-GMP-dependent functional regulators of the bacterial flagellar motors studied so far, E. coli YcgR, Pseudomonas FlgZ, and B. subtilis MotI, all possess a characteristic c-di-GMPbinding PilZ domain and an N-terminal domain referred to as the YcgR domain (Cheang et al., 2019). In S. putrefaciens, five proteins are annotated as putative PilZ domain-containing proteins (Sputcn32_2813, Sputcn32_2815, Sputcn32_2212, Sputcn32_1553, and Sputcn32_3446). Apart from possessing a putative PilZ domain, none of these proteins shows noticeable similarities to YcgR, FlgZ, or MotI at the protein level, and so far, none of them has been studied in any detail. Notably, the gene Sputcn32_3446 is located directly downstream of the secondary flagellar gene cluster, immediately following motA and motB, which encodes the proton-dependent stator of the lateral flagellar motor. We therefore hypothesized that this protein may somehow be involved in the formation and/or activity of the lateral and, potentially, the polar flagella.
    > Sputcn32_3446, annotated as a PilZ domain, is located 34 bp downstream of motB and transcribed in the same direction (Figure 1B). The gene is 435 bp in length and encodes a protein of 144 aa with an estimated molecular mass of 16.6 kDa and a theoretical pI of 5.94. The protein is thus much smaller than YcgR (244 aa), FlgZ (263), and MotI (217 aa) as an N-terminal YcgR domain is not present (Figure 1C).

### [6] Nucleotide Second Messenger-Based Signaling in Extreme Acidophiles of the Acidithiobacillus Species Complex: Partition Between the Core and Variable Gene Complements
- Authors: Ana Moya-Beltrán, Camila Rojas-Villalobos, M. Díaz, N. Guiliani, Raquel Quatrini et al.
- Year: 2019
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/594fefb49a0405cff8b3c2a21c98884c84256be0
- DOI: 10.3389/fmicb.2019.00381
- PMID: 30899248
- PMCID: 6416229
- Citations: 18
- Summary: Results indicate that the acidithiobacilli possess all the genetic elements required to establish functional transduction pathways based in three different nucleotide-second messengers: (p)ppGpp, cyclic AMP (cAMP), and c-di-GMP.
- Evidence snippets:
  - Snippet 1 (score: 0.763)
    > One of these elements, ICEAfe2, which encodes the carboxysome protein complex and the RuBisCo biphosphate carboxylase enzyme, both relevant for CO 2 fixation, is partially conserved in A. ferrooxidans ATCC 53993. This element also bares three GGDEF-EAL proteins with accessory domains of the GAF, PAS, and GCS type in the vicinity of a PilZ-type effector proteins and trb-type conjugative genes, suggesting a connection between these c-di-GMP dependent signal transduction pathways and conjugation. In A. caldus ATCC 51756 T (Figure 7B) the ICEAca TY .2, a 180 kb MGE (Acuña et al., 2013), comprises a predicted bifunctional DGC/PDE (Aca1879) and the c-di-GMP receptors/effector proteins PilZ (Aca1908), FleQ (Aca1947) and YcgR-like (unannotated gene between Aca1939 and Aca1940). In the immediate context of pilZ, chemotaxis and flagellar motility related functions were identified. Also, in the vicinity of the flagellar biosynthesis genes, we identified the Aca1947 gene, whose genetic product share is 69% of similarity with FleQ, a well-characterized transcriptional activator of the flagellar apparatus gene operon in other microorganisms (Arora et al., 1997). The third predicted effector protein identified in the A. caldus ICEAca TY .2, YcgR-like, shows 36% of similarity with flagellar brake protein YcgR. In enterobacteria the YcgR protein affects negatively both swimming and swarming in a c-di-GMP dependent manner (Ryjenkov et al., 2006;Christen et al., 2007).
    > An equivalent or related function may be proposed for the ycgR-like gene present in ICEAca TY .2, although demonstration of this function remains a challenge.

### [7] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.760)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [8] Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome
- Authors: Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani
- Year: 2023
- Venue: Medicine
- URL: https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
- DOI: 10.1097/MD.0000000000034514
- PMID: 37565925
- PMCID: 10419424
- Citations: 2
- Summary: A network pharmacology-based method to determine the potential therapeutic pathways of phytoconstituents of UHPLC-PDA standardized stigma-based Crocus sativus extract for the management of PCOS revealed that the apocarotenoids and carotenoidal could act on various targets to regulate multiple pathways related to PCOS.
- Evidence snippets:
  - Snippet 1 (score: 0.756)
    > The target protein name of the active ingredient was converted to the standard target gene name using the UniProt Knowledge Base (UniProtKB). UniProt KB is the central hub for the collection of functional information on proteins, with accurate, consistent, and rich annotation. The target protein names were uploaded into UniProtKB, with the organism restricted to "Homo sapiens," eventually gaining the official symbol. The potential targets obtained from the UniproKB are depicted in Figures 3 and 4.

### [9] A Comprehensive Genetic Characterization of Bacterial Motility
- Authors: Hany S. Girgis, Yir-Chung Liu, W. Ryu, Saeed Tavazoie
- Year: 2007
- Venue: PLoS Genetics
- URL: https://www.semanticscholar.org/paper/9b928416ac447d389872466c3753ab944a1ebd24
- DOI: 10.1371/journal.pgen.0030154
- PMID: 17941710
- PMCID: 1976333
- Citations: 241
- Influential citations: 13
- Summary: A powerful experimental framework is developed that combines competitive selection and microarray-based genetic footprinting to comprehensively reveal the genetic basis of bacterial behaviors and uncovers genome-wide epistatic interactions through comprehensive analyses of double-mutant phenotypes.
- Evidence snippets:
  - Snippet 1 (score: 0.756)
    > However, the results of the genome-wide screen for suppressors of the DyhjH motility defect reveals that this is not the case (Table S2). These observations suggest that the expression and/or enzymatic activities of these GGDEF-containing proteins may be under precise contextdependent control. Alternatively, specificity in c-di-GMP signaling may be due to a number of mechanisms including spatial and temporal sequestration, microcompartmentalization, restricted production/degradation, or target modification [56].
    > The manner in which c-di-GMP alters motility at the molecular level is currently unknown. However, it has been reported that c-di-GMP binds to the PilZ domain of the aforementioned YcgR protein [48]. It is hypothesized that YcgR undergoes a conformational change upon binding to cdi-GMP, and that the YcgR-c-di-GMP complex impairs motility through a protein-protein interaction with the flagellar motor [57]. Such an interaction may explain the observed rotational bias of flagella in DyhjH mutants (Figure 6B) and is in agreement with our finding that mutations in ycgR strongly suppress the motility defects of DyhjH mutants (Figure 6F).
    > In addition to its effects on swimming, we found evidence that c-di-GMP signaling also plays a role in swarming motility. As stated previously, mutations in yfiR strongly abolish swarming motility. The yfiR gene is the first in an operon that also contains yfiN and yfiB (inset of Figure 7). The arrangement of these genes in an operon suggests that they may function together. YfiR is predicted to be a periplasmic protein, YfiB shows sequence similarity to outer-membrane porin proteins, and YfiN is a predicted inner-membrane protein with GGDEF and HAMP domains.

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
  - Snippet 1 (score: 0.754)
    > A typical use of an ortholog database is transferring functional annotations from known genes in model organisms to genes of unknown function in other organisms, on the basis of the conjecture that orthologs are usually functionally conserved. To demonstrate such an application in our database, we showed a query to retrieve ortholog information of a specified protein.
    > Here, we specified a UniProt ID to obtain ortholog information. For describing functional categories of genes, we used Gene Ontology (GO) [24]. The UniProt GO Annotation (UniProt-GOA) database [25] (http://www.ebi.ac.uk/GOA) provides GO term assignment to proteins with evidence codes (http://www.geneontology.org/GO.evidence.shtml). We created an ontology for GO annotation (GOA-O, Table 1, http://purl.jp/bio/11/goa) and described UniProt-GOA data in RDF using it (Table 2). If some model organisms have experimentally verified GO annotations, we can transfer such a validated annotation to orthologs of other organisms.

### [11] The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa
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
  - Snippet 1 (score: 0.751)
    > The protein sequences were functionally annotated by combining information retrieved from the UniProt database ( [25], accessed on 9 June 2022) and one-to-one fast orthology assignments using the eggNOG-mapper v.2.1.7 tool ( [26], accessed on 9 June 2022), as described in [27]. Briefly, the gene name, protein name, length, Gene Ontology (GO) IDs, and chromosome associated with each protein entry were obtained from UniProt using the retrieve/ID mapping tool. Additionally, gene names, descriptions, and experimentally validated GO IDs were obtained from eggNOG, with consideration given to a taxonomic scope auto-adjusted per query, a minimum hit bit-score of 60, and thresholds of 80% for identity, minimum query coverage, and minimum subject coverage.
    > Out of the 130 detected proteins, 71 (54.6%) had information manually verified by UniProt curators (Supplementary Spreadsheet S1.5). Utilizing the eggNOG-mapper v2.1.7 tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a descrip-tion, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.
    > tool, a total of 122 entries were scanned (Supplementary Spreadsheet S1.6). By combining data from both tools, a total of 123 proteins were characterized with a gene name, and 127 had GO information. However, 2 proteins still lacked information on a description, protein, gene, and preferred names. Figure 1 provides a summary of the functional annotation results.

### [12] Identifying orthologs with OMA: A primer
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
  - Snippet 1 (score: 0.746)
    > Get more information about your gene. After searching for your gene, you will be taken to the gene's page, which provides some external information. You can also find this by clicking on the Information tab. The information for our example gene, which corresponds to the human protein S100 calcium binding protein P, is shown in Figure 5. The information page includes the OMA ID, description, organism, locus, other IDs and cross-reference, domain architectures, and Gene Ontology annotations.

### [13] Roles of the second messenger c‐di‐GMP in bacteria: Focusing on the topics of flagellar regulation and Vibrio spp.
- Authors: M. Homma, S. Kojima
- Year: 2022
- Venue: Genes to Cells
- URL: https://www.semanticscholar.org/paper/5232fabadb7fa6f823b2c61f2181a03b86c0302b
- DOI: 10.1111/gtc.12921
- PMID: 35073606
- PMCID: 9303241
- Citations: 20
- Influential citations: 2
- Summary: This review aims to explain the direct or indirect regulatory mechanisms of c‐di‐GMP in bacteria, focusing on the study of c­di‐DMP in Vibrio spp.
- Evidence snippets:
  - Snippet 1 (score: 0.740)
    > Among the various c-di-GMP-binding proteins, the structure of V. cholerae PilZ domain-containing protein D (PlzD) was determined first (Benach et al., 2007). PlzD is one of the five PilZ domain proteins that was identified from the V. cholerae genome sequence as VC0042 protein. The N-terminal domain of PlzD is homologous to that of YcgR. YcgR is involved in flagellar gene regulation in E. coli and has a PilZ domain at its C-terminus. It was later shown to bind c-di-GMP and act on a flagellar motor (Hou et al., 2020). ycgR was initially identified as a suppressor gene for the defect of the nucleoid protein H-NS, which causes the repression of flagellar gene expression. Transposon insertion in ycgR suppresses the H-NS defect and restores flagellar formation (Ko & Park, 2000). PlzD has a c-di-GMP binding consensus sequence of RxxxR and D/NxSxxG in the PilZ domain on the C-terminal side region. Benach et al. (2007) determined the apo structure without c-di-GMP and the complex structure in which one molecule of c-di-GMP was bound to a PilZ domain, revealing that c-di-GMP-bound PlzD formed a dimer. Notably, the binding of c-di-GMP to the PilZ domain causes a large structural change (Figure 2a,b). In E. coli YcgR, the Cterminal PilZ domain interacts with the flagellar stator protein MotA in the motor, and the N-terminal domain interacts with other motor proteins (assuming the rotor protein FliG). Thus, it is currently thought to inhibit motor function (Hou et al., 2020). Recently, it has been found that degradation of the σ S sigma factor by ClpXP

### [14] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.738)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

### [15] Intermolecular interactions between HD-GYP and GGDEF domain proteins mediate virulence-related signal transduction in Xanthomonas campestris
- Authors: R. Ryan, J. Dow
- Year: 2010
- Venue: Virulence
- URL: https://www.semanticscholar.org/paper/46281fbf7c7e157c99b0e54fbee843b73ba3e70f
- DOI: 10.4161/viru.1.5.12704
- PMID: 21178479
- Citations: 44
- Influential citations: 1
- Summary: It is shown that the physical interaction of RpfG with two proteins with a diguanylate cyclase (GGDEF) domain, acts to control a sub-set of RfG-regulated virulence functions, which were dependent on DSF signaling.
- Evidence snippets:
  - Snippet 1 (score: 0.738)
    > 30] Interactions between the cyclic di-GMP binding protein YcgR (a protein with two PilZ domains) and proteins of the flagellar motor slow the motor rotation, leading to reduced swimming velocity. A network of five DGCs is responsible for the generation of the cyclic di-GMP that exerts this effect during bacterial starvation, whereas the PDE YhjH maintains low cellular levels of cyclic di-GMP during exponential growth.
    > In addition to regulation at the posttranslational level, cyclic di-GMP may influence motility through effects on gene

### [16] Identification of flgZ as a Flagellar Gene Encoding a PilZ Domain Protein That Regulates Swimming Motility and Biofilm Formation in Pseudomonas
- Authors: Francisco Martínez-Granero, A. Navazo, E. Barahona, M. Redondo-Nieto, Elena González de Heredia et al.
- Year: 2014
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/90d9ebec72b802465403aec426325ebccc95ad00
- DOI: 10.1371/journal.pone.0087608
- PMID: 24504373
- PMCID: 3913639
- Citations: 64
- Influential citations: 3
- Summary: It is shown that c-di-GMP intracellular levels produced by the enzymatic activity of the diguanylate cyclase WspR and the phosphodiesterase BifA regulates biofilm formation through FlgZ, a gene located in a flagellar operon encoding a protein that contains a PilZ domain.
- Evidence snippets:
  - Snippet 1 (score: 0.733)
    > Opposed sessile and planktonic lifestyles in bacteria have been associated with the intracellular levels of c-di-GMP [28]. The current paradigm indicates that high levels of this messenger are associated with a sessile lifestyle characterized by the formation of biofilms, while low c-di-GMP levels promote biofilm dispersal and swimming motility [29,30,31]. Perception of c-di-GMP has been associated with several protein domains [32,33] and with specific structures in mRNA (riboswitches) [34,35]. One of the protein domains that has been demonstrated to bind c-di-GMP across the bacterial kingdom is the PilZ domain [4,24], originally described in cellulose synthases [36,37]. The pseudomonads contain several proteins with PilZ domains. The gene encoding one of these proteins, here named flgZ, is present in all the pseudomonads genomes sequenced so far and the degree of sequence conservation and genomic context indicate that these genes are true orthologs. The Pseudomonas putida KT440 FlgZ protein has been purified and its crystal structure has been determined to show that FlgZ binds two molecules of c-di-GMP [38]. Binding of c-di-GMP induces dimer to monomer transition, suggesting that the monomeric state is the active form [38].
    > Several of the results presented here indicate that FlgZ is implicated in motility regulation. FlgZ shows homology with the enterobacterial YcgR protein that has been shown to modulate motility, acting as a flagellar brake in response to c-di-GMP [24,39]. FlgZ and YcgR share the same domain architecture, with a C-terminal PilZ domain and an N-terminal YcgR domain. Furthermore, we have shown here that flgZ is located in a flagellar operon and is co-transcribed with the flagellar flgMN genes. Transcription of flgZ depends on the flagellar regulators FleQ and FliA.

### [17] Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells
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
  - Snippet 1 (score: 0.725)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [18] Functional annotation of parasitic worm genomes, by assigning protein names and GO terms
- Authors: Avril Coghlan, M. Berriman
- Year: 2018
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
- DOI: 10.1038/protex.2018.055
- Citations: 1
- Summary: A computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and Go terms from orthologues in other species.
- Evidence snippets:
  - Snippet 1 (score: 0.724)
    > Given a set of predicted protein-coding genes for a newly sequenced genome, functional annotation involves assigning putative functions to the predicted genes. Two ways in which this can be done are assigning protein names and Gene Ontology (GO;Gene Ontology Consortium, 2010) terms to the predicted proteins. Here we describe a computational pipeline for assigning protein names and GO terms to predicted proteins in parasitic worm (nematode and platyhelminth) genomes, which transfers names and GO terms from orthologues in other species.
    > When assigning protein names, UniProt protein naming rules (www.uniprot.org/docs/nameprot) are followed where possible. This recommends that a good and stable name for a protein is "as neutral as possible"; that a protein name "should be, as far as possible, unique and attributed to all orthologs"; and a protein name "should not contain a specific characteristic of the protein, and in particular it should not reflect the function or role of the protein, nor its subcellular location, its domain structure, its tissue specificity, its molecular weight or its species of origin".
    > In our protocol, a protein name is assigned to each predicted protein based on curated names in UniProt (Bairoch & Apweiler, 2000) for human, zebrafish, Drosophila melanogaster, Caenorhabditis elegans, and Schistosoma mansoni orthologues identified from a database of gene families (e.g. built using Ensembl Compara; Vilella et al. 2009), or (if no information is found from orthologues) based on InterPro (Hunter et al. 2012) domains. Figure 1 shows an example of using our protein naming pipeline for four Strongyloides ratti genes that belong to the tubulin polyglutamylase family (underlined in pink), where four different protein names were assigned to them (in pink), based on names of their C. elegans or human orthologues.
    > Since each of the S. ratti genes belonged to a different subfamily of the tubulin polyglutamylase family, they were assigned different names.

### [19] The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research
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
  - Snippet 1 (score: 0.722)
    > Structural annotation refers to the prediction of gene structures on a genome assembly, including the positions of transcripts, exons, introns, coding sequences, and other features [49]. Functional annotation provides information about the gene's biological role(s), for example, gene ontologies [50], pathways, functional domains, and names. Model organism databases can manually assign biological function to genes by accumulating evidence from the scientific literature and structuring it in human and machine-readable formats. In contrast, for non-model organisms such as those in the Ag100Pest Initiative, most, if not all, functional annotation is performed computationally, as (1) gene function in very few genes have been established experimentally for these non-model species, and (2) the capacity for literature-based curation of gene function does not yet exist for these species.
    > Most of the genome assemblies generated by the Ag100Pest project are being annotated using the NCBI eukaryotic annotation pipeline [51]. This pipeline relies on Gnomon [52] for gene prediction and uses genome assembly, RNA sequencing (RNA-Seq) alignments, transcripts, and protein alignments as inputs. The resulting gene predictions are given an accession number and made publicly available. Gene names are assigned based on homology to proteins in SwissProt [53,54]. The NCBI eukaryotic annotation pipeline requires both the genome assembly and associated RNA-Seq evidence to be publicly available in the NCBI's GenBank and Sequence Read Archive, respectively (SRA; see [55]). In the event that an Ag100Pest species lacks sufficient RNA-Seq evidence in SRA, additional data will be generated, as appropriate, and submitted to aid with NCBI gene structure prediction and annotation.
    > NCBI does not currently generate additional functional annotations. Proteins deposited in GenBank or generated by RefSeq should eventually be functionally annotated by UniProt [53].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Aline Biazola Visnardi, R. A. Ribeiro, A. S. de Souza, Tania Geraldine Churasacari Vinces, E. Llontop et al. (2025). Insertion of a Divergent GAF-like Domain Defines a Novel Family of YcgR Homologues That Bind c-di-GMP in Leptospirales. ACS Omega. https://www.semanticscholar.org/paper/cb63e8add821142f662f4f3551b08004b9be8caf
2. Yufan Chen, Mingfa Lv, Zhibin Liang, Zhiqing Liu, Jianuan Zhou et al. (2022). Cyclic di‐GMP modulates sessile‐motile phenotypes and virulence in Dickeya oryzae via two PilZ domain receptors. Molecular Plant Pathology. https://www.semanticscholar.org/paper/ad26c3ab30e53c70801be54958e8800fa593afda
3. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
4. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
5. A. Pecina, Meike Schwan, Vitan Blagotinsek, Tim Rick, Patrick Klüber et al. (2021). The Stand-Alone PilZ-Domain Protein MotL Specifically Regulates the Activity of the Secondary Lateral Flagellar System in Shewanella putrefaciens. Frontiers in Microbiology. https://www.semanticscholar.org/paper/040f09fa7d973fe2167f280646e5de5094bb5d56
6. Ana Moya-Beltrán, Camila Rojas-Villalobos, M. Díaz, N. Guiliani, Raquel Quatrini et al. (2019). Nucleotide Second Messenger-Based Signaling in Extreme Acidophiles of the Acidithiobacillus Species Complex: Partition Between the Core and Variable Gene Complements. Frontiers in Microbiology. https://www.semanticscholar.org/paper/594fefb49a0405cff8b3c2a21c98884c84256be0
7. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
8. Anshul Tiwari, Siddharth J Modi, A. Girme, L. Hingorani (2023). Network pharmacology-based strategic prediction and target identification of apocarotenoids and carotenoids from standardized Kashmir saffron (Crocus sativus L.) extract against polycystic ovary syndrome. Medicine. https://www.semanticscholar.org/paper/3e3253804574634d1968a0fd5b65dd1674bff6c6
9. Hany S. Girgis, Yir-Chung Liu, W. Ryu, Saeed Tavazoie (2007). A Comprehensive Genetic Characterization of Bacterial Motility. PLoS Genetics. https://www.semanticscholar.org/paper/9b928416ac447d389872466c3753ab944a1ebd24
10. H. Chiba, Hiroyo Nishide, I. Uchiyama (2015). Construction of an Ortholog Database Using the Semantic Web Technology for Integrative Analysis of Genomic Data. PLoS ONE. https://www.semanticscholar.org/paper/7cc805575c642aa8efdc1204383a7662965fbb60
11. P. Pinto-Pinho, Joana Quelhas, Francis Impens, Sara Dufour, Delphi Van Haver et al. (2025). The Surface Proteome of Bovine Unsexed and Sexed Spermatozoa. Animals : an Open Access Journal from MDPI. https://www.semanticscholar.org/paper/66496158140e8f55a2c2ca8965bd298300ce9ab0
12. Monique Zahn-Zabal, C. Dessimoz, Natasha M. Glover (2020). Identifying orthologs with OMA: A primer. F1000Research. https://www.semanticscholar.org/paper/3b77eadcdd6979352c81d0876b0ed3a3ef4215d6
13. M. Homma, S. Kojima (2022). Roles of the second messenger c‐di‐GMP in bacteria: Focusing on the topics of flagellar regulation and Vibrio spp.. Genes to Cells. https://www.semanticscholar.org/paper/5232fabadb7fa6f823b2c61f2181a03b86c0302b
14. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90
15. R. Ryan, J. Dow (2010). Intermolecular interactions between HD-GYP and GGDEF domain proteins mediate virulence-related signal transduction in Xanthomonas campestris. Virulence. https://www.semanticscholar.org/paper/46281fbf7c7e157c99b0e54fbee843b73ba3e70f
16. Francisco Martínez-Granero, A. Navazo, E. Barahona, M. Redondo-Nieto, Elena González de Heredia et al. (2014). Identification of flgZ as a Flagellar Gene Encoding a PilZ Domain Protein That Regulates Swimming Motility and Biofilm Formation in Pseudomonas. PLoS ONE. https://www.semanticscholar.org/paper/90d9ebec72b802465403aec426325ebccc95ad00
17. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
18. Avril Coghlan, M. Berriman (2018). Functional annotation of parasitic worm genomes, by assigning protein names and GO terms. https://www.semanticscholar.org/paper/583c74a2e225dbff5fca04d36298e5b690491e82
19. Anna K. Childers, S. Geib, S. Sim, Monica F. Poelchau, B. Coates et al. (2021). The USDA-ARS Ag100Pest Initiative: High-Quality Genome Assemblies for Agricultural Pest Arthropod Research. Insects. https://www.semanticscholar.org/paper/a33d31da6f5aee18501cfc2332ff50d5b7f23508