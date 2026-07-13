---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-11T00:02:23.184855'
end_time: '2026-07-11T00:02:28.576490'
duration_seconds: 5.39
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nhaB
  gene_symbol: nhaB
  uniprot_accession: Q88FQ6
  protein_description: 'RecName: Full=Na(+)/H(+) antiporter NhaB {ECO:0000255|HAMAP-Rule:MF_01599};
    AltName: Full=Sodium/proton antiporter NhaB {ECO:0000255|HAMAP-Rule:MF_01599};'
  gene_info: Name=nhaB {ECO:0000255|HAMAP-Rule:MF_01599}; OrderedLocusNames=PP_4031;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NhaB Na(+)/H(+) (TC 2.A.34) antiporter
  protein_domains: Na+/H+_antiporter_NhaB. (IPR004671); NhaB (PF06450)
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
- **UniProt Accession:** Q88FQ6
- **Protein Description:** RecName: Full=Na(+)/H(+) antiporter NhaB {ECO:0000255|HAMAP-Rule:MF_01599}; AltName: Full=Sodium/proton antiporter NhaB {ECO:0000255|HAMAP-Rule:MF_01599};
- **Gene Information:** Name=nhaB {ECO:0000255|HAMAP-Rule:MF_01599}; OrderedLocusNames=PP_4031;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NhaB Na(+)/H(+) (TC 2.A.34) antiporter
- **Key Domains:** Na+/H+_antiporter_NhaB. (IPR004671); NhaB (PF06450)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nhaB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nhaB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nhaB** (gene ID: nhaB, UniProt: Q88FQ6) in PSEPK.

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

### [1] Cloning, sequencing, and expression of the nhaB gene, encoding a Na+/H+ antiporter in Escherichia coli.
- Authors: E. Pinner, E. Padan, S. Schuldiner
- Year: 1992
- Venue: The Journal of biological chemistry
- URL: https://www.semanticscholar.org/paper/44da1fc651d1538e2cf9938ccffdb9fceea9f1bb
- DOI: 10.1016/s0021-9258(19)49875-x
- PMID: 1317851
- Citations: 118
- Influential citations: 6
- Summary: In contrast to NhaA, whose activity increases with pH, NhaB is practically insensitive to pH, and limited homologies with Na+ transporters have been identified.
- Evidence snippets:
  - Snippet 1 (score: 0.750)
    > In Escherichia coli, expulsion of sodium ions is driven by proton flux via at least two distinct Na+/H+ antiporters, NhaA and NhaB. When the nhaA gene is deleted from the chromosome, the cell becomes sensitive to high salinity and alkaline pH (Padan, E., Maisler, N., Taglicht, D., Karpel, R., and Schuldiner, S. (1989) J. Biol. Chem. 264, 20297-20302). In the current work we cloned the nhaB gene by complementation of the delta nhaA strain. The gene codes for a membrane protein 504 amino acids long. Hydropathic analysis of the sequence indicates the presence of 12 putative transmembrane helices. NhaB has been specifically labeled with [35S]methionine; it is a membrane protein and displays an apparent M(r) of 47,000, slightly lower than that predicted from its amino acid sequence. Membranes from cells containing multiple dose of nhaB display enhanced Na+/H+ antiporter activity, as measured by the ability of Na+ to collapse a preformed pH gradient or by direct measurement of 22Na+ fluxes. In contrast to NhaA, whose activity increases with pH, NhaB is practically insensitive to pH. Limited homologies with Na+ transporters have been identified.
  - Snippet 2 (score: 0.695)
    > Cloning, sequencing, and expression of the nhaB gene, encoding a Na+/H+ antiporter in Escherichia coli.

### [2] Cloning and disruption of a putative NaH-antiporter gene of Enterococcus hirae.
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
  - Snippet 1 (score: 0.745)
    > The nucleotide sequence(s) reported in thispaper has been submitted to the GenBankTM/EMBL Data Bank with accession numbeds) M81961.
    > $. Present address: Biomedical Research Center, University of British Columbia, Canada.
    > To whom correspondence should be addressed Dept. of Clinical Pharmacology, Murtenstrasse 35, 3010 Berne, Switzerland. most extensively characterized in E. coli, where two NaHantiport genes, nhaA and nhaB, have been identified. The nhaA gene has been sequenced (7)) the protein purified from an overexpressing strain, and its function as a NaH-antiporter unequivocally demonstrated (8, 9).
    > We describe in this paper the cloning of a sodium transport gene by complementation of an E. hirae mutant defective in both, ATP-driven Na-extrusion and the NaH-antiporter. The gene, termed napA, complements defects in the NaH-antiporter. It codes for a very hydrophobic protein of 383 amino acids, likely to form 12 transmembraneous helices. Disruption of the napA gene leads to loss of NaH exchange activity, as measured in whole cells or membrane vesicles. Our results strongly indicate that napA codes for the NaH-antiporter of E. hirae.

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
  - Snippet 1 (score: 0.732)
    > In this study, a Na + /H + antiporter-deficient E. coli mutant KNabc ( nhaA, nhaB, chaA) (Nozaki et al., 1996) was employed to screen Na + /H + antiporter gene from strain NEAU-ST10-9 T by functional complementation on LBK medium plates containing 0.2 M NaCl, which is the upper limit for the growth of E. coli KNabc and routinely selected as the growth condition for the screening of Na + /H + antiporter genes. As a result, a recombinant plasmid designated pUC-S5 with a 2712 bp digestion fragment succeeded in complementing with E. coli KNabc. Sequence analysis showed three open reading frames (ORFs 1-3) in the fragment (Supplementary Figure 1). ORF1 shares the highest identity (48%) with a hypothetical protein (accession version No. AQU78343.1) from Planococcus faecalis, ORF2 shares the highest identity (69%) with a TetR/AcrR family transcriptional regulator (accession version WP_052144530.1) from Bacillus okhensis, and ORF3 shares the highest identity (63%) with a CDF transporter (accession version No. WP_084309370.1) from Bacillus okhensis. Each ORF is preceded by a predicted promoter and a Shine-Dalgarno (SD) sequence and also ORF3 is followed by one possible terminator (Supplementary Figure 1). It seems that each of them can be a Na + /H + antiporter gene candidate.
    > However, each of three ORFs shares no identity with identified single-gene Na + /H + antiporters or proteins reported to exhibit Na + /H + antiport activity, the subunit of doublegene or multiple-gene Na + /H + antiporters, and even predicted Na + /H + antiporters.

### [4] Functional Characterization of Multiple Ehrlichia chaffeensis Sodium (Cation)/Proton Antiporter Genes Involved in the Bacterial pH Homeostasis
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
  - Snippet 1 (score: 0.703)
    > Bacterial pathogens are known to contain different types of antiporters expressed on the membranes to support their growth in diverse environmental conditions [17,[33][34][35]. The results presented in the current study represent the first detailed description of multiple antiporters. Our initial search in the E. chaffeensis genome allowed the identification of 10 gene open reading frames encoding for sodium (cation)/proton antiporter proteins or protein subunits. Homologs for all antiporter genes are also present in the genomes of other E. chaffeensis strains, as well as in all Anaplasmataceae family organisms of the genera Ehrlichia, Anaplasma, and Wolbachia for which the genome sequences are available in the GenBank. Further, analysis of the transmembrane topology revealed that all encoded antiporter proteins from the genes possess transmembrane domains. Except for one, all genes were also transcribed in E. chaffeensis during its replication in macrophage and tick cell cultures. We then assessed the antiporter genes in E. coli mutant with functional deficiency for antiporters; we presented data demonstrating that all predicted antiporters are functionally active. Specifically, our study demonstrated that all E. chaffeensis genes can complement the E. coli antiporter function at pH 5.5, while some genes can also provide complementation at physiological pH conditions. The data establish that all putative E. chaffeensis antiporter genes code for functional sodium/proton antiporters.
    > Transcriptional-level expression analysis of RNA transcripts of the putative antiporter protein genes of E. chaffeensis were detected when cultured in the macrophage cell line and tick cells, suggesting that they are functional genes and that the translated proteins of the antiporters may have a biological function during its lifecycle within its vertebrate and tick hosts. In the E. coli surrogate system, recombinant proteins made from all predicted antiporters provided functional complementation in relieving the inhibition of its growth in the presence of NaCl at pH 5.5.

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
  - Snippet 1 (score: 0.692)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [6] Characterization of a novel two-component Na+(Li+, K+)/H+ antiporter from Halomonas zhaodongensis
- Authors: Lin Meng, Fankui Meng, Rui Zhang, Zhenglai Zhang, Ping Dong et al.
- Year: 2017
- Venue: Scientific Reports
- URL: https://www.semanticscholar.org/paper/3478afb60143c107d1eb6a1f79e3ab8e77443c98
- DOI: 10.1038/s41598-017-04236-0
- PMID: 28652569
- PMCID: 5484666
- Citations: 12
- Summary: Functional analysis of co-expression of two genes designated umpAB, encoding paired homologous unknown membrane proteins belonging to DUF1538 family, reveals that UmpAB exhibit pH-dependent Na+(Li+, K+)/H+ antiport activity at a wide pH range of 6.5 to 9.5 with an optimal pH at 9.0.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > Na + (Li + )/H + antiport assays confirm that UmpAB is likely to function as a pH-dependent Na + (Li + )/H + antiporter (Figs 7A,B and 8). Radchenko et al. showed that one mutant E. coli strain TO114 (the different designation with the same genotype as KNabc) lacking three major Na + (Li + )/H + antiporters (NhaA, NhaB and ChaA) may be used for the identification of K + /H + antiporter candidate genes 33 . K + /H + antiport assay by using Na-free KCl reveals that UmpAB is also likely to function as a pH-dependent K + /H + antiporter (Figs 7C and 8). Therefore, we propose that UmpAB should function as a two-component pH-dependent Na + (Li + , K + )/H + antiporter.
    > Known Na + /H + antiporters belonging to CPA family include two major sorts: single-gene Na + /H + antiporters such as NhaA, NhaB, etc. 5, 8-21 and multi-gene ones such as Mrp, Mnh, Pha or Sha [23][24][25][26][27][28][29][30][31] . In addition to two  above-mentioned major categories, such proteins as ChaA, MleN, TetA(L), MdfA and Nap were also continually shown to exhibit Na + /H + antiport activity [32][33][34][35][36][37][38] . However, a careful protein alignment at the NCBI website 43 showed that there is no identity between either of UmpA or UmpB and all known specific Na + (Li + )/H + antiporters, proteins with Na + (Li + )/H + antiport activity, or even any subunit of multi-gene Na + /H + antiporters.

### [7] Kinetic properties of NhaB, a Na+/H+ antiporter from Escherichia coli.
- Authors: E. Pinner, E. Padan, S. Schuldiner
- Year: 1994
- Venue: The Journal of biological chemistry
- URL: https://www.semanticscholar.org/paper/9ea24762744c1731e9bd16fc85f60855e8808d21
- DOI: 10.1016/s0021-9258(18)47190-6
- PMID: 7929345
- Citations: 82
- Influential citations: 4
- Summary: NhaB, a Na+/H+ antiporter from Escherichia coli, was overproduced, purified, and reconstituted in a functional state, demonstrating that a single polypeptide, the product of the nhaB gene, can catalyze full activity.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > NhaB, a Na+/H+ antiporter from Escherichia coli, was overproduced, purified, and reconstituted in a functional state, demonstrating that a single polypeptide, the product of the nhaB gene, can catalyze full activity. NhaB is a minor protein that accounts for less than 0.1% of the total membrane protein. The use of proteoliposomes made possible the determination of important kinetic and pharmacological properties in the absence of passive and mediated leaks. The activity of NhaB was found to have some pH dependence; the apparent Km for Na+ changes by 10-fold from 1.55 mM at pH 8.5 to 16.66 mM at pH 7.2, while the Vmax remains constant. It was demonstrated that NhaB is electrogenic and translocates more H+ than Na+ per cycle; the rate of sodium efflux from proteoliposomes was accelerated by a membrane potential, negative inside, and NhaB activity generated a membrane potential as monitored by two techniques. The stoichiometry of NhaB was estimated by a thermodynamic method in which the magnitude of delta psi generated by NhaB was measured at various Na+ gradients. A kinetic method, in which the electrophoretic movement of 86Rb+ (in the presence of valinomycin) was monitored in parallel with measurements of NhaB-mediated 22Na+ uptake, allowed us to determine a stoichiometry of 3H+/2Na+. The significance of the existence of two antiporters with different stoichiometries, NhaA and NhaB, active in the same cell, is discussed.
  - Snippet 2 (score: 0.664)
    > DISCUSSION Kinetic properties of NhaB, a specific Na+/H' antiporter from E. coli, were analyzed with a purified and reconstituted protein preparation. The fact that a specific Na+/H+ exchange activity is enhanced 1000-€old with the overexpression and purification steps of the 43-kDa membrane protein, confirms that NhaB is a Na+/H+ antiporter and that a single polypeptide can catalyze full activity. In addition, it can be calculated that NhaB is a minor protein that accounts for less than 0.1% of the total membrane protein ofE. coli under given growth conditions. The use of proteoliposomes reconstituted with purified NhaB is essential for some measurements. In this system, passive and mediated leaks are minimal and ion gradients can be manipulated at will.
    > We previously suggested that the activity of NhaB is pHindependent as assayed by acridine orange with inverted membrane vesicles (Padan et al., 1989;Pinner et al., 1993). When the activity was analyzed in detail in NhaB-proteoliposomes, we found that NhaB-mediated, ApH-driven "Na' uptake reaction is affected significantly by pH. The apparent K,,, to Na' changes by 10-fold from 1.53 mM at pH 8.5 to 16.66 mM at pH 7.2, while V,,, does not change significantly. In the acridine orange experiments relatively high Na+ concentrations were used masking the differences between the pH values. A similar effect of pH on the K, of Na+/H+ antiporters was reported by Leblanc and collaborators (Bassilana et al., 1984b). These studies were performed in membrane vesicles isolated from cells containing both nhaA and nhaB genes. However, the cells were grown under conditions (low Na+, low pH) in which we now know that the level of nhaA expression is low (Karpel et al., 1991). One possible explanation for the effect of pH on the Km of NhaB is competition of both ions to a common site.

### [8] The evolution of a Na+-sensitive Vibrio cholerae mutant unmasks the moonlighting aminopeptidase PepA as a regulator of nhaB Na+/H+ antiporter gene expression
- Authors: Sebastian Herdan, Katharina Kohm, R. Warneke, Florian Roth, Nicolas Görge et al.
- Year: 2026
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/82f066b97791d7cc35b5a0b45ad1b5c179c58a9d
- DOI: 10.64898/2026.03.13.711655
- PMID: 41889926
- PMCID: 13015355
- Summary: The perturbation of sodium ion homeostasis does indeed impair the fitness of the human pathogenic bacterium Vibrio cholerae but can be restored by the rapid evolution of the bacteria, suggesting that inhibiting multiple targets with different antibiotics might be more effective in preventing the development of resistant bacteria.
- Evidence snippets:
  - Snippet 1 (score: 0.676)
    > Furthermore, the multi-subunit Na + /H + antiporter Mrp allowed the E. coli nhaA nhaB mutant to grow at toxic Na + and Li + concentrations as well as with natural bile salts [33]. While the exact contribution of the Na + /H + antiporters NhaB, NhaD, NhaP1 and Mrp in maintaining Na + and H + homeostasis in V. cholerae is yet unclear, NhaA can be considered as the major Na + /H + antiporter that, together with the Na + -NQR, was shown to be required by the bacteria for Na + resistance at alkaline conditions [6].
    > In the present study, we confirmed that the nhaA and nqr genes encoding the Na + /H + antiporter NhaA and Na + -NQR, respectively, become synthetically lethal in V. cholerae at high Na + concentrations and pH. Serendipitously, we found that the V. cholerae nhaA nqr mutant is genomically highly unstable and rapidly forms suppressor mutants in which Na + /H + homeostasis is restored. The characterization of the suppressor mutants revealed that restoration of Na + /H + homeostasis can be achieved by the strong overexpression of the nhaB Na + /H + antiporter gene. The suppressor screen also identified the multifunctional PepA protein as a novel repressor of the nhaB gene because loss-of-function mutations in pepA results in NhaB overproduction and Na + resistance. As an aminopeptidase, PepA is involved in amino acid metabolism, and the protein's DNA binding activity controls plasmid segregation and gene expression. The role of PepA in maintaining Na + /H + homeostasis in V. cholerae is discussed.

### [9] Physiological role of nhaB, a specific Na+/H+ antiporter in Escherichia coli.
- Authors: E. Pinner, Yaniv Kotler, E. Padan, S. Schuldiner
- Year: 1993
- Venue: The Journal of biological chemistry
- URL: https://www.semanticscholar.org/paper/4077b016c474d570f2419443b2e19925920a2487
- DOI: 10.1016/s0021-9258(18)53913-2
- PMID: 8093613
- Citations: 181
- Influential citations: 11
- Summary: The nhaB gene which codes for Na+/H+ antiporter activity in Escherichia coli was recently cloned (Pinner, E., Padan, E., and Schuldiner, S. (1992) J. Biol. Chem. 267, 11064-11068). In order to elucidate the role of nhaB in Na+ and H+ ions physiology and its interaction with nhaA, we generated mutants in which the chromosomal gene has been inactivated by insertion/deletion. A mutant devoid of both nhaA and nhaB is extremely sensitive to Na+ and Li+ at all pH values, and membranes prepared from...
- Evidence snippets:
  - Snippet 1 (score: 0.668)
    > The gene, nhaA, located at 0.3 min in the chromosome, encodes a membrane protein of M, 41,000 (Karpel et al., 1988;Taglicht et al., 1991). When in high copy number the wild type nhaA increases the Na+/H+ antiporter activity and confers to cells Li+ resistance.
    > In order to elucidate the role of nhaA in the Na+ cycle, we have deleted the chromosomal nhaA gene (Padan et al., 1989) and found that it is necessary for adaptation to high salinity, alkaline pH, and detoxication of Li+. Nevertheless, analysis of Na' transport in membrane vesicles isolated from the AnhaA strain (NM81) implied that in addition to nhaA and the K+/H+ antiporter an alternative sodium extrusion system(s) exists, designated nhaB (Padan et al., 1989).
    > We used NM81 which is sensitive to Na' and Li+ and devoid of the already cloned nhaA, and cloned the nhaB gene by functional complementation of the AnhaA strain (Pinner et al., 1992b). This strain has proved useful also for cloning of heterologous genes from Salmonella enteritidis (Pinner et al., 1992a) and from Bacillus firmus OF4 (Ivey et al., 1991).
    > By determining the nucleotide sequence of nhaB and its flanking regions, the gene has been localized at 25.5 min in the E. coli chromosome (Pinner et al., 1992b). It codes for a 504-amino acid long protein which has been specifically labeled and located in the membrane (Pinner et d., 199213).
    > Unlike NhaA, the activity of NhaB shows no dependence on pH in the range 6. 4-8.3 (Padan et al., 1989). On the other hand, the affinity of NhaB to Na+ ions ( K , = 40-70 PM) is higher than that of NhaA or any other Na+/H+ antiporter characterized thus far (Schuldiner and Padan, 1992).
  - Snippet 2 (score: 0.650)
    > The nhaB gene which codes for Na+/H+ antiporter activity in Escherichia coli was recently cloned (Pinner, E., Padan, E., and Schuldiner, S. (1992) J. Biol. Chem. 267, 11064-11068). In order to elucidate the role of nhaB in Na+ and H+ ions physiology and its interaction with nhaA, we generated mutants in which the chromosomal gene has been inactivated by insertion/deletion. A mutant devoid of both nhaA and nhaB is extremely sensitive to Na+ and Li+ at all pH values, and membranes prepared from this strain show no Na+/H+ antiporter activity. As opposed with the delta nhaA mutant which contains NhaB, the pH independent Na+/H+ antiporter (Padan, E., Maisler, N., Taglicht, D., Karpel, R., and Schuldiner, S. (1989) J. Biol. Chem. 264, 20297-20302), the delta nhaB mutant, containing NhaA, shows Na+/H+ antiporter activity highly dependent on pH. nhaB, in the absence of nhaA, confers a certain tolerance to Na+ which decreases with increasing pH. In the absence of NhaB, NhaA alone confers complete halotolerance under all conditions tested. However, when grown on agar in minimal medium on substrates which are symported with Na+ (proline, serine, and glutamate) at pH 6 and at low Na+ concentrations (< 10 mM), delta nhaB grows slower than the wild type and its Na+ dependent transport of glutamate and proline is markedly inhibited. Since both of these defects of the delta nhaB strain are alleviated upon transformation of the mutant with multicopy plasmid bearing nhaA, we conclude that nhaB is crucial when the level of NhaA activity is growth limiting, when nhaA is not sufficiently induced, and/or when NhaA is not activated.

### [10] Potassium/Proton Antiport System of Escherichia coli*
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
  - Snippet 1 (score: 0.668)
    > Because of the lack of knowledge about genes encoding K ϩ /H ϩ antiporter systems of E. coli described by Rosen and coworkers (27,28), we attempted to identify K ϩ /H ϩ antiporter(s) of this bacterium. Our previous data indicated that E. coli strain TO114, which lacks the genes nhaA, nhaB, and chaA, cannot mediate K ϩ efflux under diethanolamine (DEA) 2 pressure, whereas E. coli strain LB2003, which carries nhaA, nhaB, and chaA, extrudes K ϩ under the same conditions (17). Therefore, we studied the genes nhaA, nhaB, and chaA as possible candidates to mediate K ϩ efflux from E. coli. Our data indicate that the protein encoded by chaA is not only a Na ϩ (Ca 2ϩ )/H ϩ antiporter but also a K ϩ /H ϩ antiporter.

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
  - Snippet 1 (score: 0.667)
    > The lists of proteins used for the comparison contain more items than listed previously due to expansion out of gene clusters, for example, to allow the updating and comparison of current HGNC gene symbols. These lists of proteins were compared in Microsoft Excel 2011 using PivotTable.
    > The protein set for the CHO midbody was derived from the accession numbers in Table S1 and Table S2 from Skop et al. [9]. Original accession numbers were updated to more recent UniProt accessions (2/2010), and duplicates from different species or different protein isoforms were removed. The unique UniProt accessions were mapped to gene names using UniProt KB Unimart, UniProt dataset [82], and these gene names were confirmed manually as HGNC symbols using HGNC, with ambiguities checked using BLASTP of the sequence corresponding to the original accession number. Accessions that didn't map successfully in Unimart were manually analyzed using BLASTP against the human RefSeq protein set using sequences from the original accessions, combined with TreeFam.org data for the non-human UniProt accessions. HGNC symbols were updated again on 12/14/2010 before comparison with this paper's protein set.
    > The protein set for the HeLa spindle proteome is derived from the 1121 accession numbers in Sauer et al. supplementary table 1 column 2 [17]. Updating the 1116 UniProt accession numbers and 5 IPI accession numbers from 795 rows required several steps. Most proteins were updated to current UniProt accessions using UniProt retrieve. Duplicates were removed. Sequences for the IPI accession numbers and 16 defunct UniProt accession numbers were recovered from other sources on the web, and BLASTP against the human RefSeq protein set with a cutoff of at least 90% identity was used to update some of these accessions. The unique current UniProt accessions were mapped to HGNC symbols using UniProt ID mapping to HGNC IDs. Biomart, database Ensembl Genes 60, dataset GRCh37.p2 [http://uswest.ensembl.org/biomart/martview/]

### [12] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
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
  - Snippet 1 (score: 0.662)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [13] Characterization of a Functionally Unknown Arginine–Aspartate–Aspartate Family Protein From Halobacillus andaensis and Functional Analysis of Its Conserved Arginine/Aspartate Residues
- Authors: Li Shao, Heba Abdel-motaal, Jin Chen, Huiwen Chen, Tong Xu et al.
- Year: 2018
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/67aa6d4dd6e56604bbff8c9d5db18b9921bdd3c5
- DOI: 10.3389/fmicb.2018.00807
- PMID: 29922240
- PMCID: 5996927
- Citations: 14
- Summary: The characterization of a member of this family designated RDD from the moderate halophile Halobacillus andaensis NEAU-ST10-40T is presented and it is reported for the first time that RDD should function as a novel Na+(Li+, K+)/H+ antiporter.
- Evidence snippets:
  - Snippet 1 (score: 0.661)
    > In prokaryotes, Na + /H + antiporters are ubiquitous transmembrane proteins that mainly catalyze the efflux of cytoplasmic Na + and Li + or sometimes also K + driven by an electrochemical proton gradient generated by distinct transporters such as ion-pumping ATPases or respiratory complexes across cytoplasmic membranes (Padan and Schuldiner, 1994;Ito et al., 1999;Padan et al., 2005;Slonczewski et al., 2009;Quinn et al., 2012). This category of proteins were also designated Na + (Li + )/H + antiporters due to the simultaneous existence of Na + /H + and Li + /H + antiport activity, some of which function sometimes as K + /H + antiporters (Ito et al., 1999;Padan et al., 2005;Quinn et al., 2012). In Escherichia coli, two specific Na + /H + antiporters, NhaA (Karpel et al., 1988) and NhaB (Pinner et al., 1992), and a non-specific Na + (Ca 2+ , K + )/H + antiporter, ChaA (Ivey et al., 1993;Radchenko et al., 2006), were found to be essential for the growth of the host under high saline-alkaline stress. Therefore, E. coli mutants EP432 ( nhaA nhaB; Padan et al., 2001), KNabc ( nhaA nhaB chaA; Nozaki et al., 1996), or TO114 (the different designation with the same genotype as KNabc; Radchenko et al., 2006), especially the latter two of which can't tolerate 0.2 M NaCl or 5 mM LiCl, have been extensively used as a heterologous host to clone and express genes with Na + /H + antiport activity.

### [14] Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine
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
  - Snippet 1 (score: 0.661)
    > Genes overrepresented for nonsynonymous and structural mutations were classified into functional groups based on the functional annotation table constructed with DAVID v.2023q3 91,92 (Table S4). We established the following rules for generalizing genes into functional groups: Chaperone: genes that encode proteins that perform chaperone or chaperonin-like activities (Uniprot Keyword: KW-0143); Envelope: Genes that encode proteins involved in the maintenance of the cell-envelope such as phospholipid biosynthesis (GO-BP: 0008654) and peptidoglycan biosynthesis (GO-BP: 0000270); Metabolism: Genes that encode proteins involved in general metabolic functions, such as purine metabolism (KEGG: eco00230), amino acid metabolism (KEGG: eco00470, eco00330); or TCA Cycle (KEGG: eco00020); Regulators: Genes that encode proteins directly involved in transcription (GO-BP: 0031564; Uniprot Keyword: KW-0804), translation (GO-BP:0006412, GO-BP:0006413; Uniprot Keyword: KW-0689), or the regulation of transcription (GO-BP: 0006355, GO-BP:2000143, GO-BP:0006353, GO-BP: GO:0045893; Uniprot Keyword: KW-0805); and Transport: Genes that encode proteins involved in transport: such as ABC transporters (Interpro: PR017871), MFS transporters (Interpro: IPR011701); symporters (Interpro: IPR023954, IPR001204, IPR001734, IPR023025, IPR004840), or Antiporters (Interpro: IPR004771). A combination of resources were used to determine if a parallel mutation arose in a functional region of a protein including, EcoCyc, 96 UniProt, 97 and the primary literature (see supplemental bibliography).

### [15] LMPD: LIPID MAPS proteome database
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
  - Snippet 1 (score: 0.653)
    > For each record selected from the results summary, all LMPD data relevant to that protein are displayed, with external database IDs linked to their respective resources.
    > Annotations are organized by category: Record Overview, Gene/GO/KEGG Information, UniProt Annotations, and Related Proteins. The record overview contains LMPD_ID, species, description, gene symbols, lipid categories, EC number, molecular weight, sequence length and protein sequence. Gene information includes Entrez Gene ID, chromosome, map location, primary name, primary symbol and alternate names and symbols; Gene Ontology (GO) IDs and descriptions, and KEGG pathway IDs and descriptions. UniProt annotations include primary accession number, entry name and comments such as catalytic activity, enzyme regulation, function and similarity. For related proteins and splice variants, we display source database, database ID, sequence length, and title.

### [16] Characterization of Two Na+(K+, Li+)/H+ Antiporters from Natronorubrum daqingense
- Authors: Qi Wang, Meng Qiao, Jinzhu Song
- Year: 2023
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/f4440e4acf8f98eea71381326dea2cfc7acb409e
- DOI: 10.3390/ijms241310786
- PMID: 37445962
- PMCID: 10342064
- Citations: 9
- Summary: Two Na+/H+ antiporter genes, nhaC1 and NhaC2, were screened from the genome of Natronorubrum daqingense based on the gene library and complementation of salt-sensitive Escherichia coli KNabc andylogenetic analysis shows they belong to the Na-/H- antiporter N haC family of proteins and are significantly distant from the identified N HaC proteins from Bacillus.
- Evidence snippets:
  - Snippet 1 (score: 0.651)
    > Therefore, N. daqingense has great potential to screen genes that can encode Na + /H + exchangers.In 2022, Wang S. et al. [29] disclosed more detailed data when analyzing the whole genome sequencing of Natronorubrum daqingense, which will also be conducive to the identification of Na + /H + antiporters.In this study, the salt-sensitive E. coli KNabc (E. coli with the knockout of three major Na + /H + antiporter genes: nhaA, nhaB, and chaA) was used to screen Na + /H + antiporter genes from the genome of N. daqingense.Two NhaC-type Na + /H + antiporter genes were found, which allow E. coli Knabc to tolerate 0.6 M/0.7 M NaCl or 30 mM/40 mM LiCl, respectively, with a maximum resistance of pH 8.5/9.5.In summary, we cloned nhaC1 and nhaC2 from the N. daqingense genome, expressed and functionally validated their encoded proteins, and finally identified two novel NhaC-type Na + /H + antiporters from extremely halophilic archaea.

### [17] PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse
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
  - Snippet 1 (score: 0.649)
    > Accession numbers from UniPROT KB, NCBI and Ensembl (24)(25)(26), as well as gene symbols from HGNC (27), are curated for all proteins when possible. Basic protein descriptions include information parsed from UniPROT KB (24), and may include additional information from the literature. Descriptions are updated in bulk occasionally. Gene Ontology (28) annotations are parsed from NCBI (25). Editors assign protein types.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. E. Pinner, E. Padan, S. Schuldiner (1992). Cloning, sequencing, and expression of the nhaB gene, encoding a Na+/H+ antiporter in Escherichia coli.. The Journal of biological chemistry. https://www.semanticscholar.org/paper/44da1fc651d1538e2cf9938ccffdb9fceea9f1bb
2. M. Waser, Denise Hess-BienzS, K. Davies, Marc Soliozg (1992). Cloning and disruption of a putative NaH-antiporter gene of Enterococcus hirae.. The Journal of biological chemistry. https://www.semanticscholar.org/paper/eaf4cd2860116b84bc337d589f03d42459db8255
3. Tong Xu, Huiwen Chen, Jincheng Li, Shan Hong, Li Shao et al. (2019). Implications for Cation Selectivity and Evolution by a Novel Cation Diffusion Facilitator Family Member From the Moderate Halophile Planococcus dechangensis. Frontiers in Microbiology. https://www.semanticscholar.org/paper/3b53fc9b10b3be409a13bb269876653d00cdc026
4. Lanjing Wei, Huitao Liu, Kimia Alizadeh, M. Juárez-Rodríguez, R. Ganta (2021). Functional Characterization of Multiple Ehrlichia chaffeensis Sodium (Cation)/Proton Antiporter Genes Involved in the Bacterial pH Homeostasis. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/2acb57a1744267d7dbc1c9fef172beaf1e60317a
5. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
6. Lin Meng, Fankui Meng, Rui Zhang, Zhenglai Zhang, Ping Dong et al. (2017). Characterization of a novel two-component Na+(Li+, K+)/H+ antiporter from Halomonas zhaodongensis. Scientific Reports. https://www.semanticscholar.org/paper/3478afb60143c107d1eb6a1f79e3ab8e77443c98
7. E. Pinner, E. Padan, S. Schuldiner (1994). Kinetic properties of NhaB, a Na+/H+ antiporter from Escherichia coli.. The Journal of biological chemistry. https://www.semanticscholar.org/paper/9ea24762744c1731e9bd16fc85f60855e8808d21
8. Sebastian Herdan, Katharina Kohm, R. Warneke, Florian Roth, Nicolas Görge et al. (2026). The evolution of a Na+-sensitive Vibrio cholerae mutant unmasks the moonlighting aminopeptidase PepA as a regulator of nhaB Na+/H+ antiporter gene expression. bioRxiv. https://www.semanticscholar.org/paper/82f066b97791d7cc35b5a0b45ad1b5c179c58a9d
9. E. Pinner, Yaniv Kotler, E. Padan, S. Schuldiner (1993). Physiological role of nhaB, a specific Na+/H+ antiporter in Escherichia coli.. The Journal of biological chemistry. https://www.semanticscholar.org/paper/4077b016c474d570f2419443b2e19925920a2487
10. M. Radchenko, Kimihiro Tanaka, Rungaroon Waditee, Sawako Oshimi, Yasutomo Matsuzaki et al. (2006). Potassium/Proton Antiport System of Escherichia coli*. Journal of Biological Chemistry. https://www.semanticscholar.org/paper/c7d79d2f512c2a33547e0d7ac48b399dd6bc76af
11. Mary Kate Bonner, D. Poole, Tao Xu, Ali Sarkeshik, J. Yates et al. (2011). Mitotic Spindle Proteomics in Chinese Hamster Ovary Cells. PLoS ONE. https://www.semanticscholar.org/paper/8a46e242e657489c1933c76e06a37618f7d1901f
12. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
13. Li Shao, Heba Abdel-motaal, Jin Chen, Huiwen Chen, Tong Xu et al. (2018). Characterization of a Functionally Unknown Arginine–Aspartate–Aspartate Family Protein From Halobacillus andaensis and Functional Analysis of Its Conserved Arginine/Aspartate Residues. Frontiers in Microbiology. https://www.semanticscholar.org/paper/67aa6d4dd6e56604bbff8c9d5db18b9921bdd3c5
14. Megan G. Behringer, Wei-Chin Ho, Samuel F. Miller, Sarah B. Worthan, Zeer Cen et al. (2024). Trade-offs, trade-ups, and high mutational parallelism underlie microbial adaptation during extreme cycles of feast and famine. Current biology : CB. https://www.semanticscholar.org/paper/13c71a271ad81ea813516193454b0fed04b2cd2b
15. Dawn Cotter, A. Maer, C. Guda, Brian Saunders, S. Subramaniam (2005). LMPD: LIPID MAPS proteome database. Nucleic Acids Research. https://www.semanticscholar.org/paper/265c37b45326b7927e396484751e84e4aeff92d5
16. Qi Wang, Meng Qiao, Jinzhu Song (2023). Characterization of Two Na+(K+, Li+)/H+ Antiporters from Natronorubrum daqingense. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/f4440e4acf8f98eea71381326dea2cfc7acb409e
17. P. Hornbeck, J. Kornhauser, S. Tkachev, Bin Zhang, E. Skrzypek et al. (2011). PhosphoSitePlus: a comprehensive resource for investigating the structure and function of experimentally determined post-translational modifications in man and mouse. Nucleic Acids Research. https://www.semanticscholar.org/paper/93e4acf4ba3bca1b379ae8292e73dddb344abd90