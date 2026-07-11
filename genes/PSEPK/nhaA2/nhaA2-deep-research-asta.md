---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-11T00:02:14.066616'
end_time: '2026-07-11T00:02:20.996686'
duration_seconds: 6.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nhaA2
  gene_symbol: nhaA2
  uniprot_accession: Q88FW9
  protein_description: 'RecName: Full=Na(+)/H(+) antiporter NhaA 2 {ECO:0000255|HAMAP-Rule:MF_01844};
    AltName: Full=Sodium/proton antiporter NhaA 2 {ECO:0000255|HAMAP-Rule:MF_01844};'
  gene_info: Name=nhaA2 {ECO:0000255|HAMAP-Rule:MF_01844}; OrderedLocusNames=PP_3958;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NhaA Na(+)/H(+) (TC 2.A.33) antiporter
  protein_domains: Na/H_antiporter_dom_sf. (IPR023171); NhaA. (IPR004670); Na_H_antiport_1
    (PF06965)
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
- **UniProt Accession:** Q88FW9
- **Protein Description:** RecName: Full=Na(+)/H(+) antiporter NhaA 2 {ECO:0000255|HAMAP-Rule:MF_01844}; AltName: Full=Sodium/proton antiporter NhaA 2 {ECO:0000255|HAMAP-Rule:MF_01844};
- **Gene Information:** Name=nhaA2 {ECO:0000255|HAMAP-Rule:MF_01844}; OrderedLocusNames=PP_3958;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NhaA Na(+)/H(+) (TC 2.A.33) antiporter
- **Key Domains:** Na/H_antiporter_dom_sf. (IPR023171); NhaA. (IPR004670); Na_H_antiport_1 (PF06965)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nhaA2" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nhaA2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nhaA2** (gene ID: nhaA2, UniProt: Q88FW9) in PSEPK.

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
- Snippets retrieved: 20

## Relevant Papers

### [1] Cloning and disruption of a putative NaH-antiporter gene of Enterococcus hirae.
- Authors: M. Waser, Denise Hess-BienzS, K. Davies, Marc Soliozg
- Year: 1992
- Venue: The Journal of biological chemistry
- URL: https://www.semanticscholar.org/paper/eaf4cd2860116b84bc337d589f03d42459db8255
- DOI: 10.1016/s0021-9258(18)42779-2
- PMID: 1312090
- Citations: 94
- Influential citations: 3
- Summary: It is concluded that the napA gene codes for a NaH-antiporter, which is an extremely hydrophobic protein of 383 amino acids that probably forms 12 transmembraneous helices and does not exhibit significant homology to any protein in the EMBL genetic data bank.
- Evidence snippets:
  - Snippet 1 (score: 0.778)
    > The nucleotide sequence(s) reported in thispaper has been submitted to the GenBankTM/EMBL Data Bank with accession numbeds) M81961.
    > $. Present address: Biomedical Research Center, University of British Columbia, Canada.
    > To whom correspondence should be addressed Dept. of Clinical Pharmacology, Murtenstrasse 35, 3010 Berne, Switzerland. most extensively characterized in E. coli, where two NaHantiport genes, nhaA and nhaB, have been identified. The nhaA gene has been sequenced (7)) the protein purified from an overexpressing strain, and its function as a NaH-antiporter unequivocally demonstrated (8, 9).
    > We describe in this paper the cloning of a sodium transport gene by complementation of an E. hirae mutant defective in both, ATP-driven Na-extrusion and the NaH-antiporter. The gene, termed napA, complements defects in the NaH-antiporter. It codes for a very hydrophobic protein of 383 amino acids, likely to form 12 transmembraneous helices. Disruption of the napA gene leads to loss of NaH exchange activity, as measured in whole cells or membrane vesicles. Our results strongly indicate that napA codes for the NaH-antiporter of E. hirae.

### [2] Functional Characterization of Multiple Ehrlichia chaffeensis Sodium (Cation)/Proton Antiporter Genes Involved in the Bacterial pH Homeostasis
- Authors: Lanjing Wei, Huitao Liu, Kimia Alizadeh, M. Juárez-Rodríguez, R. Ganta
- Year: 2021
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/2acb57a1744267d7dbc1c9fef172beaf1e60317a
- DOI: 10.3390/ijms22168420
- PMID: 34445146
- PMCID: 8395091
- Citations: 4
- Summary: This is the first description of antiporters in E. chaffeensis and demonstrates that the pathogen contains multiple antiporters with varying biological functions, which are likely important for the pH homeostasis of the pathogenic’s replicating and infectious forms.
- Evidence snippets:
  - Snippet 1 (score: 0.756)
    > Since molecular tools are still limited for use in the Anaplasmataceae family pathogens, including for E. chaffeensis, it is challenging to study gene/protein function in this pathogenic bacterium in vivo. To overcome this limitation, we used E. coli as a surrogate system to study the functions of genes and proteins of E. chaffeensis [12,13]. Recently, we reported an E. coli function complementation system to define E. chaffeensis antiporter protein gene transcription and protein function [12] (Figure S2). We described that the functional complementation studies in the E. coli EP432 strain are ideally suited for defining the function of E. chaffeensis antiporter genes as it has mutations in two of its native antiporter genes [12,14]. The E. coli EP432 strain growth is significantly inhibited in the presence of sodium chloride [14] and the growth can be restored with its native gene (nhaA) expressed from a recombinant plasmid or with another bacterial gene homolog that it can functionally complement [12, [15][16][17]. To define the functions of E. chaffeensis antiporter genes, we transformed the EP432 strain with recombinant plasmids containing E. chaffeensis antiporter genes cloned along with their predicted promoter segments; this was conducted one gene at a time. The E. coli nhaA gene was similarly cloned to serve as a positive control. All transformed EP432 containing E. chaffeensis antiporter gene recombinant plasmids were then assessed for transcripts by RT-PCR analysis (Figure 3). Predicted amplicons were detected in the transformed EP432 organisms containing the E. chaffeensis antiporter genes.
    > porter genes [12,14]. The E. coli EP432 strain growth is significantly inhibited in the presence of sodium chloride [14] and the growth can be restored with its native gene (nhaA) expressed from a recombinant plasmid or with another bacterial gene homolog that it can functionally complement [12, [15][16][17].
  - Snippet 2 (score: 0.709)
    > Bacterial pathogens are known to contain different types of antiporters expressed on the membranes to support their growth in diverse environmental conditions [17,[33][34][35]. The results presented in the current study represent the first detailed description of multiple antiporters. Our initial search in the E. chaffeensis genome allowed the identification of 10 gene open reading frames encoding for sodium (cation)/proton antiporter proteins or protein subunits. Homologs for all antiporter genes are also present in the genomes of other E. chaffeensis strains, as well as in all Anaplasmataceae family organisms of the genera Ehrlichia, Anaplasma, and Wolbachia for which the genome sequences are available in the GenBank. Further, analysis of the transmembrane topology revealed that all encoded antiporter proteins from the genes possess transmembrane domains. Except for one, all genes were also transcribed in E. chaffeensis during its replication in macrophage and tick cell cultures. We then assessed the antiporter genes in E. coli mutant with functional deficiency for antiporters; we presented data demonstrating that all predicted antiporters are functionally active. Specifically, our study demonstrated that all E. chaffeensis genes can complement the E. coli antiporter function at pH 5.5, while some genes can also provide complementation at physiological pH conditions. The data establish that all putative E. chaffeensis antiporter genes code for functional sodium/proton antiporters.
    > Transcriptional-level expression analysis of RNA transcripts of the putative antiporter protein genes of E. chaffeensis were detected when cultured in the macrophage cell line and tick cells, suggesting that they are functional genes and that the translated proteins of the antiporters may have a biological function during its lifecycle within its vertebrate and tick hosts. In the E. coli surrogate system, recombinant proteins made from all predicted antiporters provided functional complementation in relieving the inhibition of its growth in the presence of NaCl at pH 5.5.
  - Snippet 3 (score: 0.695)
    > The E. coli EP432 strain growth is significantly inhibited in the presence of sodium chloride [14] and the growth can be restored with its native gene (nhaA) expressed from a recombinant plasmid or with another bacterial gene homolog that it can functionally complement [12, [15][16][17]. To define the functions of E. chaffeensis antiporter genes, we transformed the EP432 strain with recombinant plasmids containing E. chaffeensis antiporter genes cloned along with their predicted promoter segments; this was conducted one gene at a time. The E. coli nhaA gene was similarly cloned to serve as a positive control. All transformed EP432 containing E. chaffeensis antiporter gene recombinant plasmids were then assessed for transcripts by RT-PCR analysis (Figure 3). Predicted amplicons were detected in the transformed EP432 organisms containing the E. chaffeensis antiporter genes.

### [3] Implications for Cation Selectivity and Evolution by a Novel Cation Diffusion Facilitator Family Member From the Moderate Halophile Planococcus dechangensis
- Authors: Tong Xu, Huiwen Chen, Jincheng Li, Shan Hong, Li Shao et al.
- Year: 2019
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/3b53fc9b10b3be409a13bb269876653d00cdc026
- DOI: 10.3389/fmicb.2019.00607
- PMID: 30967858
- PMCID: 6440370
- Citations: 11
- Summary: The presented findings imply that MceT has evolved from its native CDF family function to a Na+/H+ antiporter in an evolutionary strategy of the substitution of key conserved residues to “Q150-S158-D184” motif.
- Evidence snippets:
  - Snippet 1 (score: 0.718)
    > In this study, a Na + /H + antiporter-deficient E. coli mutant KNabc ( nhaA, nhaB, chaA) (Nozaki et al., 1996) was employed to screen Na + /H + antiporter gene from strain NEAU-ST10-9 T by functional complementation on LBK medium plates containing 0.2 M NaCl, which is the upper limit for the growth of E. coli KNabc and routinely selected as the growth condition for the screening of Na + /H + antiporter genes. As a result, a recombinant plasmid designated pUC-S5 with a 2712 bp digestion fragment succeeded in complementing with E. coli KNabc. Sequence analysis showed three open reading frames (ORFs 1-3) in the fragment (Supplementary Figure 1). ORF1 shares the highest identity (48%) with a hypothetical protein (accession version No. AQU78343.1) from Planococcus faecalis, ORF2 shares the highest identity (69%) with a TetR/AcrR family transcriptional regulator (accession version WP_052144530.1) from Bacillus okhensis, and ORF3 shares the highest identity (63%) with a CDF transporter (accession version No. WP_084309370.1) from Bacillus okhensis. Each ORF is preceded by a predicted promoter and a Shine-Dalgarno (SD) sequence and also ORF3 is followed by one possible terminator (Supplementary Figure 1). It seems that each of them can be a Na + /H + antiporter gene candidate.
    > However, each of three ORFs shares no identity with identified single-gene Na + /H + antiporters or proteins reported to exhibit Na + /H + antiport activity, the subunit of doublegene or multiple-gene Na + /H + antiporters, and even predicted Na + /H + antiporters.

### [4] NhaR, a protein homologous to a family of bacterial regulatory proteins (LysR), regulates nhaA, the sodium proton antiporter gene in Escherichia coli.
- Authors: O. Rahav-Manor, O. Carmel, R. Karpel, Daniel N. Taglicht, G. Glaser et al.
- Year: 1992
- Venue: The Journal of biological chemistry
- URL: https://www.semanticscholar.org/paper/e87562370dfa1d79d8b5e1561f29be32f09a36f5
- DOI: 10.1016/s0021-9258(19)50037-0
- PMID: 1316901
- Citations: 89
- Influential citations: 5
- Summary: It is shown that nhaR is a regulator of nhaA, a gene encoding a Na+/H+ antiporter in Escherichia coli, and the effect of nnaR in cells is dependent on the level of n haA.
- Evidence snippets:
  - Snippet 1 (score: 0.709)
    > NhaR, a protein homologous to a family of bacterial regulatory proteins (LysR), regulates nhaA, the sodium proton antiporter gene in Escherichia coli.

### [5] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.701)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [6] Mutational Analysis of NHAoc/NHA2 in Saccharomyces cerevisiae
- Authors: Xiaobing Huang, L. Morse, Yan Xu, Jaromír Zahrádka, H. Sychrová et al.
- Year: 2010
- Venue: Biochimica et biophysica acta
- URL: https://www.semanticscholar.org/paper/774f5b6450449bbfef6b0e90e6a5a79fb89ac253
- DOI: 10.1016/j.bbagen.2010.08.001
- PMID: 20713131
- PMCID: 2967667
- Citations: 9
- Influential citations: 1
- Summary: Mutations in amino acid residues V161 and F357 reduced the ability of transfected BW31a cells to remove intracellular sodium and to grow in NaCl-containing medium, suggesting that these residues are also essential for antiporter activity.
- Evidence snippets:
  - Snippet 1 (score: 0.701)
    > We have performed a mutational analysis of the osteoclast-specific Sodium-Proton antiporter NHAoc/NHA2 by phenotypic complementation in yeasts and found that evolutionarily conserved amino acids are required for full antiporter function. Na+/H+ antiporters are ubiquitous throughout the biological kingdom. The main Na+/H+ antiporter of E. coli, NhaA, has eukaryotic orthologues. Among these are the murine NHAoc/ NHA2 [4] and the human HsNHA2 [7], which are part of a newly recognized family of metazoan CPA2 antiporters [1]. To date, the structure of these metazoan CPA2 antiporters have not been solved, however the primary sequence predicts a structure with 10 to 12 transmembrane segments (TMS) comparable to that of NhaA [10], suggesting that these proteins have a similar structural architecture. In addition to their structural similarity and despite the enormous evolutionary distance, NhaA and its eukaryotic homologues also have some sequence similarity. Many amino acid residues are conserved, notably, a pair of adjacent Aspartic acid residues, which are essential for antiporter activity in NhaA [10] as well as in NHAoc/NHA2 and HsNHA2 [7] and in antiporters from other organisms. In this report we have confirmed those findings and we have described new mutations that affect NHAoc/NHA2 antiporter activity: Valine 161 to Alanine, Phenylalanine 357 to Cysteine and the double mutant Phenylalanine 357-437 to Cysteine. These mutations correspond to amino acid residues that are conserved between NhaA and NHAoc/NHA2 and are required for proper function.
    > The pathophysiology of many skeletal diseases is associated with either increased (osteoporosis, metastatic bone disease and Paget's disease) or decreased (various types of osteopetrosis) bone resorption by osteoclasts. In normal osteoclasts, all resorption activity may be experimentally abolished by combined pharmacological inhibition of proton pumping and sodium
  - Snippet 2 (score: 0.671)
    > The exchange of Na + or K + and H + down their concentration gradients (antiport or exchange activity) occurs in cells in all phyla and kingdoms. This activity is essential to control intracellular pH, cell volume and reuptake of Na + , and cellular events such as migration, adhesion, proliferation and apoptosis [1][2][3].
    > We identified a mouse gene, nhaoc/NHA2, which is induced by RANKL stimulation of osteoclast precursors in vitro and in vivo [4,5]. Orthologues of nhaoc/NHA2 are found in all metazoans studied and define a newly recognized subfamily of metazoan proteins within the CPA2 family of antiporters [1,4,6,7]. Members of this family share a conserved N-terminus (~500 amino acids) predicted to have 10 to 12 transmembrane segments, and a short C-terminal tail (~50-100 amino acids). Together they form a novel family of antiporters which share a common ancestor with NhaA, the main antiporter of Escherichia coli [8].
    > NhaA has been extensively studied and is the only antiporter for which the 3D crystal structure is known. It is an electrogenic antiporter with a stoichiometry of 2H + /1Na + whose activity is strongly pH-dependent [8]. Data from genetic-complementation, biochemical pull-down experiments, intermolecular cross-linking and cryo-electron microscopy of 2D crystals studies reveal that NhaA exists as a dimer in the native membrane.
    > Despite the evolutionary distance, NhaA and its eukaryotic orthologues show remarkable sequence similarity, suggesting that these proteins also have a similar structural architecture, characterized by 10 to 12 predicted transmembrane segments (TMS), depending on the software used [9]. Many amino acid residues are conserved, notably, a pair of adjacent aspartic acid residues, which are essential for antiporter activity in NhaA [10] as well as in HsNHA2 [7]. NhaA has been also subjected to extensive mutational studies. An analysis of the NhaA E241-F267 segment revealed

### [7] Lithium-sensing riboswitch classes regulate expression of bacterial cation transporter genes
- Authors: Neil White, Harini Sadeeshkumar, A. Sun, Narasimhan Sudarsan, R. Breaker
- Year: 2022
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/0a85ebed2d295844671fc95cb2788c029711501b
- DOI: 10.1038/s41598-022-20695-6
- PMID: 36352003
- PMCID: 9646797
- Citations: 20
- Summary: It is demonstrated that the primary function of Li+ riboswitches and associated NhaA transporters is to prevent Li+ toxicity, particularly when bacteria are living at high pH, which might become more problematic as its industrial applications increase.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > -specific genetic switches. NhaA proteins (pfam06965, pfam07399 and COG3004) are known to function as Na + /H + antiporters, and these membrane-localized proteins are generally implicated in Na + homeostasis 20,21 , along with another demonstrated Na + /H + protein class called NhaB 22 . However, previous biochemical assays 21,23,24 reveal that NhaA proteins robustly transport both Na + and Li + . In Escherichia coli, it was demonstrated that deleting the nhaA gene results in increased Li + toxicity, whereas deleting the nhaB gene alone has no effect on Li + sensitivity 25 . Furthermore, expression of the bacteria NhaA protein confers tolerance for Li + , but not Na + , in Saccharomyces cerevisiae 26 . Because the nhaA-I and nhaA-II motif RNAs are associated with nhaA genes and never nhaB genes, we considered the possibility that these RNAs might function as selective Li + -sensing riboswitches.
    > To assess the ligand binding and gene regulation functions of nhaA-I motif RNAs, we first prepared a genetic fusion (translational) between a β-galactosidase (lacZ) reporter gene and the riboswitch candidate based on the nhaA-I motif representative from Azorhizobium caulinodans (Fig. 2A). Transcription is driven by a heterologous (Bacillus subtilis lysC) promoter known to be constitutively active 27,28 . This construct, evaluated in surrogate E. coli cells grown on LBK agar plates at pH 9.1 using agar diffusion assays (see Materials and Methods), yielded low reporter gene expression in the absence of added Li + and robust gene expression when cells were experiencing Li + toxicity (Fig. 2B).
    > Furthermore, mutant E. coli cells lacking the gene coding for the native NhaA protein (ΔnhaA) were sensitive to lower concentrations of Li + and exhibited higher reporter gene expression even when Li + was not supplemented in the growth medium. This result suggested that the ΔnhaA strain could not efficiently expel Li + Figure 1.

### [8] Protein Localization Analysis of Essential Genes in Prokaryotes
- Authors: Chong Peng, Feng Gao
- Year: 2014
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
- DOI: 10.1038/srep06001
- PMID: 25105358
- PMCID: 4126397
- Citations: 28
- Summary: A comprehensive protein localization analysis of essential genes in 27 prokaryotes including 24 bacteria, 2 mycoplasmas and 1 archaeon has been performed and shows that proteins encoded by essential genes are enriched in internal location sites, while exist in cell envelope with a lower proportion compared with non-essential ones.
- Evidence snippets:
  - Snippet 1 (score: 0.692)
    > Bioinformatics Databases. DEG is a database of essential genes (http://www. essentialgene.org/). The newly released DEG 10 has been developed to accommodate the quantitative and qualitative advancements brought by the progressive identification methods. Currently available records of both essential and nonessential genes among a wide range of organisms can be downloaded from DEG 10, making it possible to compare the two different types of genes in many aspects 21 .
    > 27 prokaryotic organisms including 24 bacteria, 2 mycoplasmas and Methanococcus maripaludis S2, the only record of the Archaea domain were selected to analyze the protein localization and GO distribution of the essential and nonessential genes. There are 31 bacterial records corresponding to 27 organisms in the database in total and 26 sets of data were selected in the current study. Streptococcus pneumonia was not chosen for the lack of non-essential genes. Since the essential genes were not genome-widely identified, it's not reasonable to regard the complementary set of essential genes as non-essential genes in Streptococcus pneumonia 29,30 . In the case of multiple records for one organism, the one with the most convincing experimental methods was chosen. The non-essential genes in Methanococcus maripaludis S2 and 13 bacteria such as Escherichia coli MG1655 are obtained based on the original literatures, while non-essential genes in other 12 organisms such as Bacillus subtilis 168 are the complementary set of essential genes. The information of the organisms used in the current study are displayed in Table 1.
    > The three model genomes' subcellular location information and the Gene Ontology (GO) terms used for the analysis in the current study were downloaded from the Universal Protein Resource (UniProt; http://www.uniprot.org). Maintained by the UniProt Consortium, UniProt is committed to providing biologists with a comprehensive, high-quality and freely accessible resource of protein sequences and functional annotation 27 . Among the wealth of annotation data, detailed GO annotation statements are included.

### [9] CRONOS: the cross-reference navigation server
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
  - Snippet 1 (score: 0.684)
    > In order to detect gene and protein names which are assigned to products of different genes and thus result in erroneous cross-references, dedicated lists are created for each organism separately. Organism-specific lists are necessary, since terms that are ambiguous in one organism might be explicit in another. For example, ADORA2 is an ambiguous gene name in Homo sapiens but not in mouse, and GALT in mouse but not in H.sapiens.
    > In a first step, ambiguous names within the databases were extracted. If a name occurs in at least two entries describing different genes or proteins (splice variants count as one gene/protein), this particular name is marked as ambiguous and is excluded from the mapping process. In a second step, corresponding gene names occurring in the manually annotated sections of RefSeq as well as in UniProt were analyzed. Entries containing the same gene product name and having a one-to-many or many-to-many relation (e.g. one Swiss-Prot entry maps to many RefSeq entries) were scrutinized for misleading annotation. This process is done manually by inspecting additional information like sequence similarity or functional information about the involved entries. In most of the cases, the exclusion of the ambiguous gene names resulted in correct one-to-one relations.
    > As statistical analysis revealed (Supplementary Material S2) that gene names with less than four letters are exceptionally error-prone, only gene names with at least four letters are kept for mapping purposes. However, gene names with less than four letters can be queried, e.g. a search for the tumor suppressor 'p53' reveals the respective entries with the official gene name 'TP53'. Organism-specific lists of ambiguous gene and protein names are available for download on the CRONOS home page.

### [10] A genetic system for targeted mutations to disrupt and restore genes in the obligate bacterium, Ehrlichia chaffeensis
- Authors: Ying Wang, Lanjing Wei, Huitao Liu, Chuanmin Cheng, R. Ganta
- Year: 2017
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/4c0bd552ba99ff0ba08c20b5fd5c18f935d14109
- DOI: 10.1038/s41598-017-16023-y
- PMID: 29150636
- PMCID: 5693922
- Citations: 14
- Influential citations: 1
- Summary: Obligate intracellular bacteria (obligates) belonging to Rickettsiales and Chlamydiales cause diseases in hundreds of millions of people worldwide and in many animal species. Lack of an efficient system for targeted mutagenesis in obligates remains a major impediment in understanding microbial pathogenesis. Challenges in creating targeted mutations may be attributed to essential nature of majority of the genes and intracellular replication dependence. Despite success in generating random muta...
- Evidence snippets:
  - Snippet 1 (score: 0.681)
    > gene restored E. chaffeensis. We previously predicted that the Ech_0379 gene encodes for an antiporter gene 15 . E. coli antiporter gene mutant strain, EP432 having mutations in two of the three antiporter genes 33 , is exploited as a great research tool in studying antiporter proteins of several Gram negative bacteria 34,35 . In particular, this E. coli strain is used in mapping the functions of antiporter proteins by functional complementation assays. Complementation assays are performed in conferring resistance to its Na + sensitivity in high NaCl concentrations in a growth medium. To define the function of Ech_0379 gene product in E. chaffeensis and also to assess the impact of targeted disruption and complementation mutations, we adopted the E. coli complementation assay using the EP432 strain. We cloned the Ech_0379 gene sequences, including its native promoter, from wild-type, gene disruption or gene restoration mutant organisms into a plasmid and then transformed the plasmids individually into the EP432 strain. To serve as a positive control, E. coli NhaA (one of its missing antiporter genes) is similarly cloned and transformed, while non-recombinant plasmid transformed culture of the strain was used as a negative control. DNA-free total RNAs recovered from E. coli strains containing the Ech_0379 genes were assessed for the presence of the gene transcripts by RT-PCR (Fig. 6A). Predicted amplicons were detected only for RNAs recovered from the E. coli containing Ech_0379 gene from the wild-type and the gene restoration mutant of E. chaffeensis, but not in the RNA from the strain containing the disruption mutant E. chaffeensis gene. We then tested the E. coli cultures for the antiporter protein activity by functional complementation assay to rescue its Na + sensitivity (Fig. 6B).

### [11] A genetic system for targeted mutations to disrupt and restore genes in the obligate bacterium, Ehrlichia chaffeensis
- Authors: Ying Wang, Lanjing Wei, Huitao Liu, Chuanmin Cheng, R. Ganta
- Year: 2017
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/4a29d2e4748798bb365dc8203381295cc17c78bd
- DOI: 10.1038/s41598-017-16023-y
- Summary: Obligate intracellular bacteria (obligates) belonging to Rickettsiales and Chlamydiales cause diseases in hundreds of millions of people worldwide and in many animal species. Lack of an efficient system for targeted mutagenesis in obligates remains a major impediment in understanding microbial pathogenesis. Challenges in creating targeted mutations may be attributed to essential nature of majority of the genes and intracellular replication dependence. Despite success in generating random muta...
- Evidence snippets:
  - Snippet 1 (score: 0.680)
    > gene restored E. chaffeensis. We previously predicted that the Ech_0379 gene encodes for an antiporter gene 15 . E. coli antiporter gene mutant strain, EP432 having mutations in two of the three antiporter genes 33 , is exploited as a great research tool in studying antiporter proteins of several Gram negative bacteria 34,35 . In particular, this E. coli strain is used in mapping the functions of antiporter proteins by functional complementation assays. Complementation assays are performed in conferring resistance to its Na + sensitivity in high NaCl concentrations in a growth medium. To define the function of Ech_0379 gene product in E. chaffeensis and also to assess the impact of targeted disruption and complementation mutations, we adopted the E. coli complementation assay using the EP432 strain. We cloned the Ech_0379 gene sequences, including its native promoter, from wild-type, gene disruption or gene restoration mutant organisms into a plasmid and then transformed the plasmids individually into the EP432 strain. To serve as a positive control, E. coli NhaA (one of its missing antiporter genes) is similarly cloned and transformed, while non-recombinant plasmid transformed culture of the strain was used as a negative control. DNA-free total RNAs recovered from E. coli strains containing the Ech_0379 genes were assessed for the presence of the gene transcripts by RT-PCR (Fig. 6A). Predicted amplicons were detected only for RNAs recovered from the E. coli containing Ech_0379 gene from the wild-type and the gene restoration mutant of E. chaffeensis, but not in the RNA from the strain containing the disruption mutant E. chaffeensis gene. We then tested the E. coli cultures for the antiporter protein activity by functional complementation assay to rescue its Na + sensitivity (Fig. 6B).

### [12] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
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
  - Snippet 1 (score: 0.674)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [13] Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea
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
  - Snippet 1 (score: 0.674)
    > The BLASTx homology search tool, a component of the standalone NCBI-blast-2.3.0+, was used to perform functional annotation of the F. udum genes (Altschul et al., 1990). With a cut-off E value of ≤1e−06 and a similarity of 34%, BLASTx identified the homologous sequences of the genes in the NCBI non-redundant protein database. Gene ontology (GO) analysis was carried out using Blast2GO PRO 4.1.5 (Conesa and Gotz, 2008). In three different mappings, B2G performed as follows: (1) Using two NCBI-provided mapping files, blast result accessions are used to get gene names (symbols; gene info, gene 2 accessions). (2) Blast result GI identifiers were used to retrieve UniProt IDs using a mapping file from PIR (non-redundant reference protein database), which includes PSD, Swiss-Prot, UniProt, TrEMBL, GenPept, RefSeq, and PDB. The names of the identified genes were searched in the species-specific entries of the gene product table of the GO database. With the aid of the KAAS-KEGG Automatic Annotation Server, pathway analyses were carried out. This database provides functional annotation of genes using other data servers (Moriya et al., 2007). Accessions from the blast results were looked for in the DBXRef table of the GO database.

### [14] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.673)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [15] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.672)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [16] Potassium/Proton Antiport System of Escherichia coli*
- Authors: M. Radchenko, Kimihiro Tanaka, Rungaroon Waditee, Sawako Oshimi, Yasutomo Matsuzaki et al.
- Year: 2006
- Venue: Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/c7d79d2f512c2a33547e0d7ac48b399dd6bc76af
- DOI: 10.1074/jbc.M600333200
- PMID: 16687400
- Citations: 91
- Influential citations: 8
- Summary: The results suggest that ChaA K+/H+ antiporter activity enables E. coli to adapt to K+ salinity stress and to maintain K+ homeostasis.
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > Because of the lack of knowledge about genes encoding K ϩ /H ϩ antiporter systems of E. coli described by Rosen and coworkers (27,28), we attempted to identify K ϩ /H ϩ antiporter(s) of this bacterium. Our previous data indicated that E. coli strain TO114, which lacks the genes nhaA, nhaB, and chaA, cannot mediate K ϩ efflux under diethanolamine (DEA) 2 pressure, whereas E. coli strain LB2003, which carries nhaA, nhaB, and chaA, extrudes K ϩ under the same conditions (17). Therefore, we studied the genes nhaA, nhaB, and chaA as possible candidates to mediate K ϩ efflux from E. coli. Our data indicate that the protein encoded by chaA is not only a Na ϩ (Ca 2ϩ )/H ϩ antiporter but also a K ϩ /H ϩ antiporter.

### [17] Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem
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
  - Snippet 1 (score: 0.671)
    > We decided to prioritize human genes and proteins. The following strategy has been implemented to resolve gene and protein text entities to the most reasonable gene, protein, or enzyme symbol (corresponding to human, when possible):
    > -Try to find a match among Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC) names (Braschi et al., 2019;HUGO, 2021);
    > -Try to find a match among names in The IUPHAR/BPS Guide to Pharmacology (Armstrong et al., 2020; IUPHAR/BPS, 2021); -Try to find matches among names in UniProt (Bateman et al., 2017); -Otherwise, try to match to an enzyme name and resolve to an EC number (Bairoch, 2000;Expassy, 2021).
    > In general, it is very difficult and often impossible to distinguish the name of a gene from the name of the protein encoded by that gene. Therefore, gene and protein names are not strictly distinguished from each other but considered as one category. Therefore, the annotations considered in this study can be grouped into three categories: chemicals, genes/proteins, and diseases.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. M. Waser, Denise Hess-BienzS, K. Davies, Marc Soliozg (1992). Cloning and disruption of a putative NaH-antiporter gene of Enterococcus hirae.. The Journal of biological chemistry. https://www.semanticscholar.org/paper/eaf4cd2860116b84bc337d589f03d42459db8255
2. Lanjing Wei, Huitao Liu, Kimia Alizadeh, M. Juárez-Rodríguez, R. Ganta (2021). Functional Characterization of Multiple Ehrlichia chaffeensis Sodium (Cation)/Proton Antiporter Genes Involved in the Bacterial pH Homeostasis. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/2acb57a1744267d7dbc1c9fef172beaf1e60317a
3. Tong Xu, Huiwen Chen, Jincheng Li, Shan Hong, Li Shao et al. (2019). Implications for Cation Selectivity and Evolution by a Novel Cation Diffusion Facilitator Family Member From the Moderate Halophile Planococcus dechangensis. Frontiers in Microbiology. https://www.semanticscholar.org/paper/3b53fc9b10b3be409a13bb269876653d00cdc026
4. O. Rahav-Manor, O. Carmel, R. Karpel, Daniel N. Taglicht, G. Glaser et al. (1992). NhaR, a protein homologous to a family of bacterial regulatory proteins (LysR), regulates nhaA, the sodium proton antiporter gene in Escherichia coli.. The Journal of biological chemistry. https://www.semanticscholar.org/paper/e87562370dfa1d79d8b5e1561f29be32f09a36f5
5. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
6. Xiaobing Huang, L. Morse, Yan Xu, Jaromír Zahrádka, H. Sychrová et al. (2010). Mutational Analysis of NHAoc/NHA2 in Saccharomyces cerevisiae. Biochimica et biophysica acta. https://www.semanticscholar.org/paper/774f5b6450449bbfef6b0e90e6a5a79fb89ac253
7. Neil White, Harini Sadeeshkumar, A. Sun, Narasimhan Sudarsan, R. Breaker (2022). Lithium-sensing riboswitch classes regulate expression of bacterial cation transporter genes. Scientific Reports. https://www.semanticscholar.org/paper/0a85ebed2d295844671fc95cb2788c029711501b
8. Chong Peng, Feng Gao (2014). Protein Localization Analysis of Essential Genes in Prokaryotes. Scientific Reports. https://www.semanticscholar.org/paper/69181762648fd77a085b2f93618a71b43b62cf76
9. Brigitte Waegele, I. Dunger, G. Fobo, Corinna Montrone, H. Mewes et al. (2008). CRONOS: the cross-reference navigation server. Bioinformatics. https://www.semanticscholar.org/paper/8c05b3aa0ba01c41ee97c2dc98ea7b5b14ce0e9c
10. Ying Wang, Lanjing Wei, Huitao Liu, Chuanmin Cheng, R. Ganta (2017). A genetic system for targeted mutations to disrupt and restore genes in the obligate bacterium, Ehrlichia chaffeensis. Scientific Reports. https://www.semanticscholar.org/paper/4c0bd552ba99ff0ba08c20b5fd5c18f935d14109
11. Ying Wang, Lanjing Wei, Huitao Liu, Chuanmin Cheng, R. Ganta (2017). A genetic system for targeted mutations to disrupt and restore genes in the obligate bacterium, Ehrlichia chaffeensis. Scientific Reports. https://www.semanticscholar.org/paper/4a29d2e4748798bb365dc8203381295cc17c78bd
12. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
13. A. Srivastava, R. Srivastava, Jagriti Yadav, Ashutosh Kumar Singh, P. Tiwari et al. (2023). Virulence and pathogenicity determinants in whole genome sequence of Fusarium udum causing wilt of pigeon pea. Frontiers in Microbiology. https://www.semanticscholar.org/paper/ac4c8e1cd07dbd943c544dab0dff140617956e3a
14. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
15. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
16. M. Radchenko, Kimihiro Tanaka, Rungaroon Waditee, Sawako Oshimi, Yasutomo Matsuzaki et al. (2006). Potassium/Proton Antiport System of Escherichia coli*. Journal of Biological Chemistry. https://www.semanticscholar.org/paper/c7d79d2f512c2a33547e0d7ac48b399dd6bc76af
17. L. Zaslavsky, Tiejun Cheng, A. Gindulyte, Siqian He, Sunghwan Kim et al. (2021). Discovering and Summarizing Relationships Between Chemicals, Genes, Proteins, and Diseases in PubChem. Frontiers in Research Metrics and Analytics. https://www.semanticscholar.org/paper/57b86aef9aae576c2ae4199c0b74971f4c195211