---
provider: cyberian
model: deep-research
cached: false
start_time: '2025-12-06T21:29:46.832731'
end_time: '2025-12-06T21:43:10.165296'
duration_seconds: 803.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TERT
  gene_symbol: TERT
  uniprot_accession: O14746
  protein_description: 'RecName: Full=Telomerase reverse transcriptase; EC=2.7.7.49
    {ECO:0000269|PubMed:21602826, ECO:0000269|PubMed:29695869}; AltName: Full=HEST2;
    AltName: Full=Telomerase catalytic subunit; AltName: Full=Telomerase-associated
    protein 2; Short=TP2;'
  gene_info: Name=TERT; Synonyms=EST2, TCS1, TRT;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the reverse transcriptase family. Telomerase
  protein_domains: DNA/RNA_pol_sf. (IPR043502); RT_dom. (IPR000477); Telomerase_RBD.
    (IPR021891); Telomerase_RT. (IPR003545); TERT_C. (IPR049139)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O14746
- **Protein Description:** RecName: Full=Telomerase reverse transcriptase; EC=2.7.7.49 {ECO:0000269|PubMed:21602826, ECO:0000269|PubMed:29695869}; AltName: Full=HEST2; AltName: Full=Telomerase catalytic subunit; AltName: Full=Telomerase-associated protein 2; Short=TP2;
- **Gene Information:** Name=TERT; Synonyms=EST2, TCS1, TRT;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the reverse transcriptase family. Telomerase
- **Key Domains:** DNA/RNA_pol_sf. (IPR043502); RT_dom. (IPR000477); Telomerase_RBD. (IPR021891); Telomerase_RT. (IPR003545); TERT_C. (IPR049139)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TERT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TERT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TERT** (gene ID: TERT, UniProt: O14746) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Human Telomerase Reverse Transcriptase (TERT): Structure, Function, and Regulation

## Introduction

Telomerase reverse transcriptase (TERT) is the catalytic protein subunit of the telomerase ribonucleoprotein enzyme complex, responsible for maintaining telomere length at the ends of linear chromosomes. In humans, TERT (UniProt: O14746; NCBI Gene ID: 7015) is encoded by the TERT gene located on chromosome 5p15.33 and consists of 1132 amino acids with a molecular weight of approximately 127 kDa [meyerson-1997-hTERT-cloning-abstract]. The enzyme catalyzes the addition of TTAGGG repeats to chromosome 3' ends using an internal RNA template provided by the telomerase RNA component (TERC/hTR), thereby counteracting the end-replication problem and enabling unlimited cellular proliferation [podlevsky-2012-telomerase-review-abstract].

The discovery of telomerase traces back to the seminal work of Carol Greider and Elizabeth Blackburn in 1985, who first identified telomerase activity in Tetrahymena extracts [greider-1985-telomerase-discovery-abstract]. This foundational discovery, along with Jack Szostak's work on telomere function, was recognized with the 2009 Nobel Prize in Physiology or Medicine. The human TERT gene was subsequently cloned in 1997 by Meyerson, Weinberg, and colleagues, who demonstrated that TERT expression correlates with telomerase activity and is the rate-limiting component for telomerase function in human cells [meyerson-1997-hTERT-cloning-abstract].

TERT is particularly significant in cancer biology, as telomerase reactivation occurs in approximately 90% of human cancers, enabling tumor cells to bypass replicative senescence and achieve immortalization [dratwa-2020-TERT-regulation-cancer-abstract]. Understanding TERT's enzymatic mechanism, subcellular localization, and regulatory pathways is therefore essential for developing targeted cancer therapies and understanding cellular aging processes.

## Protein Structure and Domain Organization

Human TERT contains four evolutionarily conserved structural domains that work together to accomplish the unique enzymatic function of telomere extension [podlevsky-2012-telomerase-review-abstract][wu-2017-telomerase-mechanism-abstract]. These domains are arranged linearly from the N-terminus to C-terminus: the telomerase essential N-terminal (TEN) domain, the telomerase RNA-binding domain (TRBD), the reverse transcriptase (RT) domain, and the C-terminal extension (CTE) domain.

The TEN domain, located at the N-terminus, is connected through a flexible linker to the remainder of the protein and serves critical roles in substrate handling and repeat addition processivity [wu-2017-telomerase-mechanism-abstract]. This domain traps single-stranded telomeric DNA and facilitates processive repeat synthesis by capturing the substrate and maintaining association with the single-stranded product during the catalytic cycle. The TEN domain also participates in the recruitment of telomerase to chromosome ends through its interaction with the shelterin component TPP1 [liu-2022-TPP1-telomerase-structure-abstract].

The TRBD is essential for telomerase RNA binding and activity both in vitro and in vivo [podlevsky-2012-telomerase-review-abstract]. This domain contains conserved T, CP, and QFP motifs that are critical for RNA interaction. The TRBD engages TERC through hydrogen bonds and electrostatic interactions, maintaining a stable yet flexible association that is necessary for template positioning and catalysis.

The RT domain contains the catalytic center of the enzyme and shares seven conserved motifs with conventional reverse transcriptases: motifs 1, 2, A, B', C, D, and E [podlevsky-2012-telomerase-review-abstract]. Motifs A and C contain a catalytic triad of universally conserved aspartate residues (D712, D868, and D869 in human TERT) that are essential for catalytic activity. These residues coordinate divalent metal ions (typically Mg²⁺) that stabilize the developing negative charge during nucleotide addition, a mechanism common to all polymerases [wu-2017-telomerase-mechanism-abstract]. A unique feature of the telomerase RT domain is the insertion in fingers domain (IFD), located between motifs A and B, which is thought to stabilize short RNA-DNA hybrids crucial for template translocation [podlevsky-2012-telomerase-review-abstract]. Recent cryo-EM studies have revealed an additional TERT-specific domain called TRAP (telomerase RAP motif) that participates in interactions with the shelterin protein TPP1 [liu-2022-TPP1-telomerase-structure-abstract].

The CTE domain contributes to structural stability and may enhance nucleic acid association [podlevsky-2012-telomerase-review-abstract]. Crystal structures of the Tribolium castaneum TERT revealed that the TRBD, RT, and CTE domains fold together to form a toroidal (ring-like) structure with a central cavity that accommodates the RNA-DNA hybrid during catalysis [gillis-2008-tribolium-TERT-structure-abstract][mitchell-2010-TERT-nucleic-acid-binding-abstract]. Although Tribolium TERT lacks the TEN and TRAP domains present in human TERT, this ring structure has proven useful for modeling the human enzyme architecture.

## Enzymatic Mechanism and Catalytic Activity

TERT catalyzes the addition of telomeric DNA repeats (5'-TTAGGG-3' in humans) to chromosome 3' ends, classifying it as a template-dependent DNA polymerase with EC number 2.7.7.49 [podlevsky-2012-telomerase-review-abstract]. Unlike conventional polymerases, telomerase uses an intrinsic RNA template provided by the TERC component rather than an external template strand. This unique arrangement enables telomerase to synthesize multiple telomeric repeats through a distinctive two-phase catalytic cycle [wu-2017-telomerase-mechanism-abstract].

The first phase is the nucleotide addition phase, during which TERT synthesizes a single telomeric repeat by copying the template region of TERC onto the chromosome 3' end. Human TERC contains an 11-nucleotide template sequence (5'-CUAACCCUAAC-3') that directs the synthesis of the hexanucleotide repeat 5'-GGTTAG-3' [podlevsky-2012-telomerase-review-abstract]. Nucleotide addition proceeds through the standard polymerase mechanism, with the conserved aspartate residues in motifs A and C coordinating two divalent metal ions that catalyze the nucleophilic attack of the primer 3'-OH on the α-phosphate of the incoming dNTP [wu-2017-telomerase-mechanism-abstract].

The second phase is template translocation, which is unique to telomerase among polymerases. After completing synthesis of one repeat, the enzyme must reposition the template to enable synthesis of additional repeats without dissociating from the DNA substrate [wu-2017-telomerase-mechanism-abstract]. This requires separation of the newly formed RNA-DNA hybrid, translocation of the RNA template by one repeat length (six nucleotides), and re-annealing of the template to the 3' end of the newly synthesized DNA. The precise mechanism of template translocation remains incompletely understood, but involves conformational changes in both TERT and TERC that maintain substrate retention while allowing template repositioning.

The ability to synthesize multiple repeats without dissociation is termed repeat addition processivity (RAP), and is a hallmark feature that distinguishes telomerase from conventional polymerases [wu-2017-telomerase-mechanism-abstract]. RAP requires the TEN domain anchor site, which binds single-stranded DNA upstream of the RNA-DNA hybrid and maintains association with the substrate during template translocation. A DNA hairpin model has been proposed to explain how the primer 3'-end remains engaged with the active site while the template translocates, with the complementary DNA repeat forming a transient non-canonical base-paired hairpin that is subsequently realigned for processive synthesis [wu-2017-telomerase-mechanism-abstract].

The cryo-EM structure of human telomerase holoenzyme bound to telomeric DNA revealed that only four base pairs form between the DNA substrate and RNA template at any given time, providing structural insight into the short RNA-DNA hybrid that facilitates template translocation [nguyen-2021-telomerase-DNA-structure-abstract]. Nucleotide selectivity is determined by contacts between the RNA template and RT domain motifs 2 and B', which position the solvent-accessible RNA bases close to the enzyme active site [mitchell-2010-TERT-nucleic-acid-binding-abstract].

## Telomerase Holoenzyme Assembly and Composition

Active human telomerase functions as a large ribonucleoprotein complex containing multiple protein subunits in addition to TERT and TERC [nguyen-2018-cryoEM-telomerase-abstract][nguyen-2021-telomerase-DNA-structure-abstract]. Cryo-EM structures have revealed that the human telomerase holoenzyme adopts a bilobed architecture consisting of a catalytic core lobe and an H/ACA ribonucleoprotein (RNP) lobe.

The catalytic core contains one TERT molecule and the essential template and pseudoknot domains of TERC [nguyen-2018-cryoEM-telomerase-abstract]. In this lobe, TERC encircles TERT, adopting a well-ordered tertiary structure with surprisingly limited direct protein-RNA interactions. The pseudoknot forms a rigid arc-like structure that may contribute to the co-folding of TERT and TERC rather than direct catalytic function.

The H/ACA RNP lobe comprises two sets of heterotetrameric H/ACA proteins (dyskerin, NOP10, NHP2, and GAR1) and one Cajal body protein, TCAB1 [nguyen-2018-cryoEM-telomerase-abstract]. These proteins bind to the 3' end of TERC, which contains conserved H/ACA motifs found in small nucleolar RNAs involved in ribosome biogenesis. The H/ACA proteins are essential for TERC stability and processing, while TCAB1 directs telomerase localization to Cajal bodies.

A surprising discovery from high-resolution cryo-EM structures was the identification of a histone H2A-H2B dimer as an integral component of the holoenzyme [nguyen-2021-telomerase-DNA-structure-abstract]. This histone dimer binds to the CR4/5 domain of TERC, suggesting a previously unappreciated role for histones in telomerase RNA folding and function beyond their canonical nucleosomal function.

The molecular chaperones HSP90 and p23 are required for correct assembly and stabilization of the active telomerase complex [wu-2017-telomerase-mechanism-abstract]. Assembly of the catalytic core involves the binding of TERT to two distinct regions of TERC: the template/pseudoknot domain and the CR4/5 domain. Both interactions are essential for reconstitution of catalytic activity.

## Subcellular Localization and Trafficking

TERT and the telomerase complex exhibit dynamic subcellular localization that is regulated by the cell cycle and is crucial for enzyme function [tomlinson-2006-telomerase-trafficking-abstract][tomlinson-2008-hTERT-localization-abstract]. In human cells, TERT contains both nuclear localization signals and mitochondrial targeting sequences, enabling its distribution among the nucleus, cytoplasm, and mitochondria [dratwa-2020-TERT-regulation-cancer-abstract].

Within the nucleus, telomerase localization follows a cell cycle-dependent pattern that couples telomere synthesis specifically to S phase, when DNA replication occurs [tomlinson-2006-telomerase-trafficking-abstract]. During G1 and G2 phases, TERT and TERC occupy distinct subnuclear compartments: TERC resides primarily in Cajal bodies, while TERT is found in nucleoplasmic foci. Upon entry into S phase, both components are recruited to telomeres, with localization peaking at mid-S phase. In approximately 19% of mid-S phase cells, TERC was found at telomeres, typically at one to five telomeres per cell, declining in late S phase [tomlinson-2006-telomerase-trafficking-abstract].

Cajal bodies serve as critical sites for telomerase maturation, assembly, and storage [tomlinson-2006-telomerase-trafficking-abstract]. The localization of TERC to Cajal bodies and telomeres is specific to cancer cells expressing active telomerase and is not observed in primary cells lacking TERT expression. Importantly, TERT is required for TERC localization to both Cajal bodies and telomeres: RNAi-mediated depletion of TERT causes loss of TERC from these sites without affecting TERC levels, while introduction of TERT into normal cells induces TERC accumulation at Cajal bodies and telomeres [tomlinson-2008-hTERT-localization-abstract]. This indicates that telomerase assembly precedes transport to functional locations, with TERT serving as the critical determinant for intranuclear trafficking.

The TCAB1 protein (also known as WDR79) plays a key role in telomerase localization by directing the complex to Cajal bodies [wu-2017-telomerase-mechanism-abstract]. TCAB1 binds to the CAB-box motif in TERC and is required for proper localization of telomerase to both Cajal bodies and telomeres.

Telomerase is also found in mitochondria, where it appears to have functions distinct from telomere maintenance [dratwa-2020-TERT-regulation-cancer-abstract]. Mitochondrial localization of TERT is regulated by phosphorylation, particularly at tyrosine 707. Oxidative stress promotes Src kinase-mediated phosphorylation of Y707, which triggers nuclear export and translocation of TERT to mitochondria. Conversely, dephosphorylation by the phosphatase SHP2/PTPN11 promotes nuclear retention. Within mitochondria, TERT may contribute to mitochondrial DNA protection, reduce reactive oxygen species production, and regulate mitochondrial gene expression.

## Telomere Recruitment via Shelterin Complex

Recruitment of telomerase to chromosome ends in human cells is mediated by the shelterin complex, a six-protein assembly that caps and protects telomeres [liu-2022-TPP1-telomerase-structure-abstract][nandakumar-2012-TEL-patch-abstract]. The shelterin complex consists of TRF1, TRF2, RAP1, TIN2, POT1, and TPP1, with TPP1 serving as the direct recruitment factor for telomerase.

TPP1 interacts directly with TERT through a specific surface region called the TEL patch (TPP1 glutamate and leucine-rich patch) located within the N-terminal OB-fold domain of TPP1 [nandakumar-2012-TEL-patch-abstract]. The TEL patch contains four glutamic acid residues that confer a negative charge, which complements the highly basic TEN domain of TERT. Mutations in the TEL patch disrupt telomerase recruitment and abolish the stimulatory effects of TPP1 on enzyme processivity.

Recent cryo-EM structures have provided detailed views of the TERT-TPP1 interaction [liu-2022-TPP1-telomerase-structure-abstract]. TPP1 forms a structured interface with both the TEN domain and the TRAP motif of TERT, creating a three-way TEN-(IFD-TRAP)-TPP1 interaction that is critical for telomerase recruitment and processive repeat addition. TPP1 binding stabilizes the TEN domain conformation and allows the anchor site to engage the DNA substrate more stably.

POT1, which forms a heterodimer with TPP1 within shelterin, binds single-stranded telomeric DNA through two OB-fold domains with nanomolar affinity for the sequence 5'-TTAGGGTTAG [liu-2022-TPP1-telomerase-structure-abstract]. POT1 further stabilizes DNA binding by promoting the DNA-TEN domain interaction. Together, TPP1 and POT1 cooperatively increase repeat addition processivity by reducing DNA dissociation during repeat synthesis.

## Non-Canonical Functions

Beyond its canonical role in telomere maintenance, TERT possesses telomere-independent functions that contribute to cellular physiology and cancer progression [dratwa-2020-TERT-regulation-cancer-abstract]. These non-canonical functions can be grouped into two categories: those involving telomerase activity but not telomere elongation, and those requiring neither telomere elongation nor telomerase activity.

TERT functions as a transcriptional regulator through its interaction with the Wnt/β-catenin signaling pathway [dratwa-2020-TERT-regulation-cancer-abstract]. TERT can interact directly with β-catenin and occupy the promoters of β-catenin target genes such as vimentin and Cyclin D1. This interaction facilitates transcription of epithelial-mesenchymal transition (EMT)-related genes independent of telomerase catalytic activity. Furthermore, TERT controls a transcriptional program that overlaps those regulated by Myc and Wnt, pathways crucial for development, stem cell regulation, and cancer.

TERT also participates in NF-κB signaling, forming a positive feedback loop with this pathway [dratwa-2020-TERT-regulation-cancer-abstract]. NF-κB is a positive regulator of TERT expression, while in the cytosol, TERT can form a complex with the NF-κB p65 subunit. This complex migrates to the nucleus and regulates expression of NF-κB target genes, amplifying inflammatory and survival signals.

Mitochondrial localization of TERT contributes to cell survival and stress response [dratwa-2020-TERT-regulation-cancer-abstract]. Within mitochondria, TERT reduces reactive oxygen species production, improves mitochondrial membrane potential, and may participate in mitochondrial DNA repair and gene regulation. Translocation to mitochondria is promoted by oxidative stress through Src kinase-mediated phosphorylation of tyrosine 707.

## Transcriptional and Post-Translational Regulation

TERT expression is tightly regulated at multiple levels, including transcriptional control, epigenetic modifications, and post-translational modifications [dratwa-2020-TERT-regulation-cancer-abstract][bell-2016-TERT-promoter-mutations-abstract]. While TERC is ubiquitously expressed in human cells, TERT expression is stringently repressed in most somatic cells, making it the rate-limiting determinant of telomerase activity.

The TERT promoter is regulated by numerous transcription factors. Activators include c-MYC, which binds E-box motifs in the core promoter, Sp1, which binds GC-rich sites, and NF-κB [dratwa-2020-TERT-regulation-cancer-abstract]. Repressors include p53, WT1, and various other factors. The balance between activating and repressive signals determines TERT expression levels in different cell types and developmental stages.

In cancer, TERT is reactivated through multiple mechanisms [bell-2016-TERT-promoter-mutations-abstract]. Two hotspot point mutations in the TERT promoter (C228T and C250T), located 124 and 146 bp upstream of the translation start site, are found in over 50 cancer types with frequencies exceeding 80% in glioblastoma and melanoma. These mutations are typically heterozygous, occur in a mutually exclusive fashion, and both create an identical 11-nucleotide sequence (5'-CCCGGAAGGGG-3') that generates a de novo binding site for ETS family transcription factors. The GABPA transcription factor, functioning as a heterotetramer with GABPB1, selectively recognizes and activates the mutant TERT promoter without affecting wild-type promoter activity [bell-2016-TERT-promoter-mutations-abstract].

Post-translational modifications of TERT regulate its activity, stability, and localization [dratwa-2020-TERT-regulation-cancer-abstract]. Phosphorylation has been extensively studied, with key sites including:
- Serine 227: Phosphorylation by AKT promotes nuclear localization
- Tyrosine 707: Phosphorylation by Src kinase under oxidative stress promotes cytoplasmic/mitochondrial localization; dephosphorylation by SHP2 promotes nuclear retention
- Tyrosine residues: Phosphorylation by BCR-ABL in leukemia cells increases telomerase activity

Ubiquitination of TERT targets it for proteasomal degradation. Dyrk2 kinase phosphorylates TERT, promoting its degradation by the EDD-DDB1-VprBP E3 ligase complex [dratwa-2020-TERT-regulation-cancer-abstract]. SUMOylation by CBX4 at specific sites can enhance cell migration and invasiveness in breast cancer cells.

## Open Questions

Despite significant advances in understanding TERT structure and function, several important questions remain:

1. **Mechanism of template translocation:** The precise conformational changes that enable telomerase to reposition its RNA template while maintaining DNA substrate binding remain incompletely characterized. High-resolution structures capturing intermediate states would clarify this unique catalytic cycle step.

2. **Regulation of processivity:** How does the TEN domain specifically enable repeat addition processivity? The dynamics of anchor site engagement during the catalytic cycle require further investigation.

3. **Non-canonical function mechanisms:** While TERT's roles in Wnt signaling, NF-κB signaling, and mitochondrial function are established, the precise molecular mechanisms underlying these telomere-independent activities require further elucidation.

4. **Coordination with DNA replication:** How is telomerase activity restricted to S phase, and what prevents inappropriate telomeric activity at other cell cycle stages or non-telomeric sites?

5. **Therapeutic targeting:** Despite the strong rationale for targeting telomerase in cancer, clinical success has been limited. Understanding resistance mechanisms and developing more effective inhibitors remains an active area of research.

6. **Alternative lengthening of telomeres (ALT):** A subset of cancers maintain telomeres through a telomerase-independent mechanism. Understanding the relationship between ALT and telomerase pathways could reveal new therapeutic vulnerabilities.

7. **TERT in disease beyond cancer:** Mutations causing telomerase insufficiency lead to diseases including dyskeratosis congenita, aplastic anemia, and pulmonary fibrosis. Understanding how partial loss of function leads to tissue-specific pathology remains an important question.

## References

* bell-2016-TERT-promoter-mutations-abstract: Bell RJA, Rube HT, Xavier-Magalhães A, Costa BM, Mancini A, Song JS, Costello JF. Understanding TERT Promoter Mutations: A Common Path to Immortality. Mol Cancer Res. 2016;14(4):315-323. PMID: 26941407. DOI: 10.1158/1541-7786.MCR-16-0003. PMCID: PMC4852159. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4852159/

* dratwa-2020-TERT-regulation-cancer-abstract: Dratwa M, Wysoczańska B, Łacina P, Kubik T, Bogunia-Kubik K. TERT—Regulation and Roles in Cancer Formation. Front Immunol. 2020;11:589929. PMID: 33329574. DOI: 10.3389/fimmu.2020.589929. PMCID: PMC7717964. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7717964/

* gillis-2008-tribolium-TERT-structure-abstract: Gillis AJ, Schuller AP, Skordalakes E. Structure of the Tribolium castaneum telomerase catalytic subunit TERT. Nature. 2008;455(7213):633-637. PMID: 18758444. DOI: 10.1038/nature07283. URL: https://www.nature.com/articles/nature07283

* greider-1985-telomerase-discovery-abstract: Greider CW, Blackburn EH. Identification of a specific telomere terminal transferase activity in Tetrahymena extracts. Cell. 1985;43(2 Pt 1):405-413. PMID: 3907856. DOI: 10.1016/0092-8674(85)90170-9

* liu-2022-TPP1-telomerase-structure-abstract: Liu B, He Y, Wang Y, Song H, Zhou ZH, Feigon J. Structure of active human telomerase with telomere shelterin protein TPP1. Nature. 2022;604(7906):578-583. PMID: 35418675. DOI: 10.1038/s41586-022-04582-8. PMCID: PMC9912816. URL: https://www.nature.com/articles/s41586-022-04582-8

* meyerson-1997-hTERT-cloning-abstract: Meyerson M, Counter CM, Eaton EN, et al. hEST2, the putative human telomerase catalytic subunit gene, is up-regulated in tumor cells and during immortalization. Cell. 1997;90(4):785-795. PMID: 9288757. DOI: 10.1016/s0092-8674(00)80538-3. URL: https://pubmed.ncbi.nlm.nih.gov/9288757/

* mitchell-2010-TERT-nucleic-acid-binding-abstract: Mitchell M, Gillis A, Futahashi M, Fujiwara H, Skordalakes E. Structural basis for telomerase catalytic subunit TERT binding to RNA template and telomeric DNA. Nat Struct Mol Biol. 2010;17(4):513-518. PMID: 20357774. DOI: 10.1038/nsmb.1777. URL: https://www.nature.com/articles/nsmb.1777

* nandakumar-2012-TEL-patch-abstract: Nandakumar J, Bell CF, Weidenfeld I, Zaug AJ, Leinwand LA, Cech TR. The TEL patch of telomere protein TPP1 mediates telomerase recruitment and processivity. Nature. 2012;492(7428):285-289. PMID: 23103865. DOI: 10.1038/nature11648. PMCID: PMC3521838

* nguyen-2018-cryoEM-telomerase-abstract: Nguyen THD, Tam J, Wu RA, et al. Cryo-EM structure of substrate-bound human telomerase holoenzyme. Nature. 2018;557(7704):190-195. PMID: 29695869. DOI: 10.1038/s41586-018-0062-x. PMCID: PMC6223129. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6223129/

* nguyen-2021-telomerase-DNA-structure-abstract: Nguyen THD, et al. Structure of human telomerase holoenzyme with bound telomeric DNA. Nature. 2021;593(7859):449-453. PMID: 33883742. DOI: 10.1038/s41586-021-03415-4. PMCID: PMC7610991. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7610991/

* podlevsky-2012-telomerase-review-abstract: Podlevsky JD, Chen JJ. It all comes together at the ends: Telomerase structure, function, and biogenesis. Mutat Res. 2012;730(1-2):3-11. PMID: 22093366. DOI: 10.1016/j.mrfmmm.2011.11.002. PMCID: PMC4420735. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4420735/

* tomlinson-2006-telomerase-trafficking-abstract: Tomlinson RL, Ziegler TD, Supakorndej T, Terns RM, Terns MP. Cell cycle-regulated trafficking of human telomerase to telomeres. Mol Biol Cell. 2006;17(2):955-965. PMID: 16339074. DOI: 10.1091/mbc.E05-09-0903. PMCID: PMC1356603. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC1356603/

* tomlinson-2008-hTERT-localization-abstract: Tomlinson RL, Abreu EB, Ziegler T, et al. Telomerase reverse transcriptase is required for the localization of telomerase RNA to Cajal bodies and telomeres in human cancer cells. Mol Biol Cell. 2008;19(9):3793-3800. PMID: 18562689. DOI: 10.1091/mbc.E08-02-0184. PMCID: PMC2526684. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC2526684/

* wu-2017-telomerase-mechanism-abstract: Wu RA, Upton HE, Vogan JM, Collins K. Telomerase Mechanism of Telomere Synthesis. Annu Rev Biochem. 2017;86:439-460. PMID: 28141967. DOI: 10.1146/annurev-biochem-061516-045019. PMCID: PMC5812681. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5812681/


## Citations

1. bell-2016-TERT-promoter-mutations-abstract.md
2. dratwa-2020-TERT-regulation-cancer-abstract.md
3. gillis-2008-tribolium-TERT-structure-abstract.md
4. greider-1985-telomerase-discovery-abstract.md
5. liu-2022-TPP1-telomerase-structure-abstract.md
6. meyerson-1997-hTERT-cloning-abstract.md
7. mitchell-2010-TERT-nucleic-acid-binding-abstract.md
8. nandakumar-2012-TEL-patch-abstract.md
9. nguyen-2018-cryoEM-telomerase-abstract.md
10. nguyen-2021-telomerase-DNA-structure-abstract.md
11. podlevsky-2012-telomerase-review-abstract.md
12. tomlinson-2006-telomerase-trafficking-abstract.md
13. tomlinson-2008-hTERT-localization-abstract.md
14. wu-2017-telomerase-mechanism-abstract.md