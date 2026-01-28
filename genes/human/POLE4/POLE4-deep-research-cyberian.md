---
provider: cyberian
model: deep-research
cached: true
start_time: '2026-01-23T16:53:10.674195'
end_time: '2026-01-23T16:53:10.675797'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: POLE4
  gene_symbol: POLE4
  uniprot_accession: Q9NR33
  protein_description: 'RecName: Full=DNA polymerase epsilon subunit 4; AltName: Full=DNA
    polymerase II subunit 4; AltName: Full=DNA polymerase epsilon subunit p12;'
  gene_info: Name=POLE4;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: CBFA_NFYB_domain. (IPR003958); Histone-fold. (IPR009072); Transcr_DNA_Rep_Reg.
    (IPR050568); CBFD_NFYB_HMF (PF00808)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9NR33
- **Protein Description:** RecName: Full=DNA polymerase epsilon subunit 4; AltName: Full=DNA polymerase II subunit 4; AltName: Full=DNA polymerase epsilon subunit p12;
- **Gene Information:** Name=POLE4;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CBFA_NFYB_domain. (IPR003958); Histone-fold. (IPR009072); Transcr_DNA_Rep_Reg. (IPR050568); CBFD_NFYB_HMF (PF00808)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "POLE4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'POLE4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **POLE4** (gene ID: POLE4, UniProt: Q9NR33) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# POLE4 (DNA Polymerase Epsilon Subunit 4): A Comprehensive Functional Review

## Introduction and Summary

POLE4 (DNA polymerase epsilon subunit 4, also known as p12) is an accessory subunit of the eukaryotic DNA polymerase epsilon (Polε) complex, the primary enzyme responsible for leading strand DNA synthesis during chromosomal replication [li-2000-pole4-identification-abstract]. The human POLE4 gene is located on chromosome 2p12 and encodes a small 117 amino acid protein (approximately 12 kDa) that contains a C-terminal histone fold domain structurally similar to histone H2A [li-2000-pole4-identification-abstract]. POLE4 forms an obligate heterodimer with POLE3 (p17) through their complementary histone fold motifs, creating a structure that mimics the H2A-H2B histone dimer [bellelli-2018-histone-chaperone-abstract].

The primary functions of POLE4 are threefold: first, it serves as a structural scaffold essential for maintaining the stability of the entire Polε holoenzyme complex; second, as part of the POLE3-POLE4 heterodimer, it acts as a histone H3-H4 chaperone that facilitates the recycling of parental histones to the leading strand during DNA replication; and third, it contributes to the processivity of DNA polymerase epsilon by stabilizing its association with newly synthesized double-stranded DNA [bellelli-2018-pole-instability-abstract][bellelli-2018-histone-chaperone-abstract]. Unlike the catalytic subunit POLE1, POLE4 has no enzymatic activity of its own; rather, its role is regulatory and structural, coupling the DNA replication machinery to chromatin maintenance.

## Structural Organization and Domain Architecture

POLE4 is the smallest subunit of the tetrameric DNA polymerase epsilon complex. The complete Polε holoenzyme consists of four subunits: POLE1 (p261, the catalytic subunit containing the DNA polymerase and 3'-5' exonuclease activities), POLE2 (p59), POLE3 (p17/CHRAC17), and POLE4 (p12) [li-2000-pole4-identification-abstract]. The nomenclature follows a parallel system in budding yeast *Saccharomyces cerevisiae*, where the orthologous proteins are designated Pol2, Dpb2, Dpb4, and Dpb3, respectively (notably, POLE3 corresponds to Dpb4 and POLE4 to Dpb3) [bellelli-2018-histone-chaperone-abstract].

The defining structural feature of POLE4 is its C-terminal histone fold domain, which spans approximately residues 45-117 and comprises three alpha helices connected by two loops in an arrangement characteristic of the histone superfamily. The POLE4 histone fold exhibits 34% sequence identity with the yeast Dpb3 subunit and structural similarity to histone H2A [li-2000-pole4-identification-abstract]. The N-terminal region preceding the histone fold is predicted to be largely unstructured and may provide flexibility for interactions with other complex components.

POLE3 contains a complementary H2B-like histone fold domain at its N-terminus, followed by two additional alpha helices and an acidic C-terminal region [bellelli-2018-histone-chaperone-abstract]. The POLE3-POLE4 heterodimer forms through conserved hydrophobic interactions between residues in the central alpha helix (α2) of each histone fold domain; specifically, Phe44 in POLE3 and Phe74 in POLE4 engage in pi-stacking interactions that stabilize the dimer interface. Mutation of these residues disrupts heterodimer formation and consequently impairs both complex stability and histone chaperone function [bellelli-2018-histone-chaperone-abstract].

Cryo-electron microscopy studies of the yeast and human Polε holoenzyme have revealed that the enzyme adopts a bilobal architecture: the N-terminal catalytic domain of POLE1 forms the active polymerase core, while the C-terminal non-catalytic domain of POLE1 together with POLE2 forms a second lobe that mediates interaction with the CMG (Cdc45-MCM-GINS) helicase at the replication fork. The POLE3-POLE4 heterodimer binds to a linker region connecting these two lobes via a conserved "mooring helix" in POLE1, positioning the histone chaperone module adjacent to the nascent DNA as it emerges from the polymerase active site [bellelli-2018-histone-chaperone-abstract].

## Molecular Function: Role in DNA Replication

DNA polymerase epsilon is the principal enzyme synthesizing the leading strand during eukaryotic chromosomal DNA replication. The enzyme functions as part of the replisome, a large macromolecular machine that coordinates DNA unwinding by the CMG helicase with concurrent DNA synthesis by Polε on the leading strand and DNA polymerase delta (Polδ) on the lagging strand [bellelli-2018-pole-instability-abstract].

While the catalytic functions of Polε reside entirely within POLE1, the accessory subunits POLE3 and POLE4 perform essential regulatory roles. Studies in yeast demonstrated that deletion of Dpb3 (POLE4) and Dpb4 (POLE3) does not prevent DNA replication but reduces the processivity of the Pol2-Dpb2 subcomplex, leading to frequent dissociation from the DNA template [bellelli-2018-pole-instability-abstract]. This processivity defect manifests as gaps in the newly synthesized leading strand, elevated mutagenesis, and replication stress [hill-2024-parpinhibitor-abstract].

Recent work has defined a two-tier regulatory system governing Polε processivity during leading strand synthesis. The first tier involves PCNA (proliferating cell nuclear antigen), which is loaded specifically onto the leading strand by the CHTF18-RFC2/5 complex and serves as a sliding clamp to tether the polymerase to DNA. The second tier involves the POLE3-POLE4 heterodimer, which "grips" newly synthesized double-stranded DNA as it emerges from the polymerase, further stabilizing the enzyme-DNA association. Combined loss of both CHTF18-RFC loading and POLE3-POLE4 function is synthetically lethal, demonstrating that these represent parallel pathways essential for processive leading strand synthesis [hill-2024-parpinhibitor-abstract].

A critical finding from mammalian studies is that POLE4 is required for maintaining the stability of the entire Polε complex. In Pole4 knockout mice, levels of both POLE1 and POLE2 are substantially reduced, indicating that the POLE3-POLE4 subcomplex serves as a structural scaffold for holoenzyme assembly [bellelli-2018-pole-instability-abstract]. This contrasts with yeast, where Dpb3 deletion reduces processivity but does not destabilize the core enzyme. The enhanced requirement for POLE4 in mammals may reflect the greater complexity of mammalian genome replication or evolutionary divergence in complex assembly mechanisms.

## Histone Chaperone Activity and Epigenetic Maintenance

Beyond its structural role in the Polε complex, the POLE3-POLE4 heterodimer functions as a bona fide histone H3-H4 chaperone, directly coupling DNA replication to the re-establishment of chromatin structure on newly synthesized DNA [bellelli-2018-histone-chaperone-abstract]. This function has important implications for epigenetic inheritance, as the faithful transmission of histone modifications from parental to daughter cells depends on the accurate recycling and partitioning of parental histones during DNA replication.

Biochemical studies established that purified POLE3-POLE4 complex directly binds histones H3 and H4 in the absence of other replisome components. Hydrogen-deuterium exchange mass spectrometry mapped the interaction interface to the C-terminal region of POLE3 (including the acidic domain) and the histone fold of H4 (particularly the α2-L2 region) [bellelli-2018-histone-chaperone-abstract]. The POLE3-POLE4 complex can bind both H3-H4 dimers and tetramers, with a preference for the tetrameric form, and promotes tetrasome (H3-H4 tetramer-DNA complex) assembly on linear DNA substrates in vitro. It also induces negative supercoiling of plasmid DNA in the presence of topoisomerase I, a hallmark of histone deposition activity.

At the replication fork, parental histones must be disassembled ahead of the advancing replisome and then reassembled onto the two daughter DNA duplexes behind the fork. The POLE3-POLE4 complex participates specifically in recycling parental H3-H4 tetramers to the leading strand. This pathway operates in parallel with the MCM2-dependent pathway that mediates parental histone transfer to the lagging strand via interactions with DNA polymerase alpha and the adapter protein Ctf4 [bellelli-2018-histone-chaperone-abstract].

Cellular experiments confirmed that POLE3-POLE4 binds both newly synthesized and parental histones in chromatin. Depletion of POLE3-POLE4 function impairs both parental histone retention and new histone deposition, resulting in altered chromatin maturation kinetics at replication forks. Specifically, POLE3-POLE4 deficiency leads to delayed PCNA unloading from chromatin and reduced RPA (replication protein A) accumulation at forks, indicating defects in the coordination of DNA synthesis with chromatin reassembly [bellelli-2018-histone-chaperone-abstract].

Recent studies have extended these findings by examining the consequences of disrupting both leading and lagging strand histone recycling pathways. While POLE4 knockout alone causes moderate asymmetry in parental histone inheritance (with reduced recycling to the leading strand), combined loss of POLE4 and MCM2-mediated pathways results in substantial parental histone loss to the soluble pool and aberrant accumulation of the repressive histone modification H3K27me3, which precedes changes in gene expression [bellelli-2018-histone-chaperone-abstract].

## Subcellular Localization

Consistent with its role in DNA replication and chromatin maintenance, POLE4 is localized to the nucleus, specifically within the nucleoplasm where DNA replication occurs. The Human Protein Atlas reports nuclear/nucleoplasmic localization based on immunofluorescence studies, with additional evidence for cytosolic presence at lower levels. During S phase, POLE4 is recruited to replication foci as part of the Polε holoenzyme, where it associates with replicating chromatin.

The subcellular distribution of POLE4 is expected to be cell cycle-regulated, with peak chromatin association during S phase when DNA replication occurs. The protein lacks a classical nuclear localization signal, and nuclear import likely occurs through association with other Polε subunits or via the histone chaperone pathway. Upon depletion of POLE4, its partner POLE3 is rapidly destabilized, suggesting that the heterodimer must form in the cytoplasm prior to nuclear import [bellelli-2018-pole-instability-abstract].

## Biological Processes and Disease Associations

### Developmental Phenotypes

The biological importance of POLE4 is dramatically illustrated by mouse knockout studies. Pole4-/- mice exhibit embryonic lethality in the inbred C57BL/6 genetic background, while in outbred strains the knockout animals survive but display severe developmental abnormalities [bellelli-2018-pole-instability-abstract]. These include intrauterine growth restriction with low birth weight, craniofacial defects, skeletal abnormalities, cerebellar hypoplasia leading to ataxia, and profound immune system defects characterized by a 5-fold reduction in T cells and impaired thymic development.

Remarkably, many of these phenotypes can be rescued by inactivation of p53, the guardian of genome integrity. This finding indicates that developmental defects in Pole4-/- mice result primarily from p53-mediated cell death or senescence in response to replication stress, rather than from direct loss of an essential cellular function [bellelli-2018-pole-instability-abstract]. Polε deficiency leads to inefficient replication origin firing and increased replication fork stalling, which activates the ATR-p53 checkpoint pathway and eliminates cells with compromised genome replication.

### Human IMAGe-like Syndrome

Human patients with biallelic hypomorphic mutations in POLE1 (the catalytic subunit) exhibit a syndrome closely resembling the Pole4-/- mouse phenotype [logan-2018-pole-image-syndrome-abstract]. These patients present with intrauterine growth restriction, metaphyseal dysplasia, adrenal hypoplasia congenita, and genitourinary abnormalities in males—features that define IMAGe syndrome, which was previously associated only with gain-of-function mutations in the cell cycle inhibitor CDKN1C. POLE1-deficient patients also display distinctive facial features and variable immunodeficiency with lymphocyte deficiency.

The parallel phenotypes between human POLE1 deficiency and mouse Pole4 deficiency underscore the functional interdependence of Polε subunits. Because POLE4 is required for the stability of the entire complex, Pole4 knockout effectively phenocopies hypomorphic POLE1 deficiency [logan-2018-pole-image-syndrome-abstract].

### Cancer Predisposition and Tumorigenesis

Pole4-/- mice that survive to adulthood exhibit increased cancer susceptibility, particularly lymphomas. The incidence of thymic lymphoma is approximately 12% in Pole4-deficient mice compared to 4% in wild-type controls, while mesenteric lymph node lymphomas occur in 23.5% of knockouts versus 7.7% of controls [bellelli-2018-pole-instability-abstract]. This cancer predisposition is consistent with the role of Polε in maintaining genome stability during DNA replication.

Intriguingly, while p53 inactivation rescues developmental defects in Pole4-/- mice, it dramatically accelerates lymphomagenesis, with Pole4-/- p53+/- double mutant mice succumbing rapidly to T-cell lymphomas [bellelli-2018-pole-instability-abstract]. This illustrates the dual role of p53: it protects against cancer by eliminating cells with replication stress, but in so doing it also causes the developmental abnormalities observed in Polε-deficient animals. Two human patients with POLE1 deficiency also developed lymphomas (T-cell lymphoma at age 11 and Hodgkin lymphoma at age 28), suggesting that POLE deficiency confers lymphoma susceptibility in humans as well [logan-2018-pole-image-syndrome-abstract].

### PARP Inhibitor Sensitivity

A therapeutically relevant discovery is that loss of POLE3 or POLE4 sensitizes cancer cells to PARP (poly-ADP-ribose polymerase) inhibitors, a class of drugs approved for treatment of BRCA1/2-deficient cancers [hill-2024-parpinhibitor-abstract][mamar-2024-parpinhibitor-abstract]. Two independent studies in 2024 demonstrated that POLE3-POLE4 knockout cells are hypersensitive to PARP inhibitors through a mechanism distinct from homologous recombination deficiency.

POLE4 knockout cells treated with PARP inhibitors accumulate single-stranded DNA gaps behind replication forks due to impaired post-replicative repair [mamar-2024-parpinhibitor-abstract]. This gap accumulation depends on the translesion polymerase PRIMPOL and leads to elevated replication stress signaling through ATR and DNA-PK kinases. Importantly, POLE4 loss sensitizes cells to PARP inhibitors even when resistance mechanisms associated with restoration of homologous recombination (such as 53BP1 knockdown) are operative, suggesting that targeting POLE4 could overcome acquired PARP inhibitor resistance in cancer therapy [hill-2024-parpinhibitor-abstract].

## Additional Interactions: The ATAC Complex

POLE4 has been identified as a component of the ATAC (ADA-two-A-containing) complex, a histone acetyltransferase complex involved in transcriptional regulation. ATAC contains the acetyltransferases GCN5 and ATAC2 along with numerous other subunits, and acetylates histones H3 and H4 to promote transcriptionally active chromatin states. However, the significance of POLE4's association with ATAC remains unclear, and some studies have failed to detect POLE4 in ATAC preparations, possibly reflecting differences in purification stringency or cell type [bellelli-2018-histone-chaperone-abstract]. Whether POLE4 plays a functional role in ATAC-mediated transcription or whether this association reflects promiscuous histone fold interactions remains to be determined.

## Role in Heterochromatin Maintenance

Beyond its roles in DNA replication processivity and histone chaperoning, the POLE4 ortholog in fission yeast (Dpb3) plays a critical role in the inheritance of heterochromatin states during DNA replication. Crystallographic studies determined a 1.9-Å structure of the fission yeast Dpb3-Dpb4 complex, confirming that these proteins form a canonical H2A-H2B-like histone fold dimer [he-2017-heterochromatin-abstract]. Disruption of the Dpb3-Dpb4 dimerization interface results in loss of heterochromatin silencing, demonstrating that the intact heterodimer is essential for epigenetic maintenance.

Mechanistically, the Dpb3-Dpb4 complex serves as a platform for recruiting chromatin-modifying enzymes to nascent DNA during replication. In fission yeast, this complex associates with Sir2 (a NAD-dependent histone deacetylase), chromatin remodelers, and Clr4 (the H3K9 methyltransferase responsible for heterochromatin establishment) [he-2017-heterochromatin-abstract]. Cells lacking Dpb3 fail to recruit Sir2 to heterochromatin regions and display strong silencing defects. These findings suggest that the POLE3-POLE4 heterodimer coordinates two key processes during replication-coupled heterochromatin assembly: histone hypoacetylation (via Sir2 recruitment) and H3K9 methylation (via Clr4 association).

This function provides a mechanistic explanation for the epigenetic defects observed in yeast mutants lacking these subunits, and suggests that the mammalian POLE3-POLE4 complex may similarly participate in recruiting chromatin modifiers during DNA replication, although direct evidence for this in mammalian cells remains limited.

## Evolutionary Conservation

The POLE3-POLE4 heterodimer is conserved from yeast to humans, although with some notable differences in essentiality and function. In budding yeast, Dpb3 and Dpb4 deletion mutants are viable and show relatively modest phenotypes including reduced Polε processivity, increased mutagenesis, and defects in heterochromatin maintenance. In fission yeast, Dpb3-Dpb4 has been structurally characterized and shown to be important for recruiting chromatin modifiers that maintain heterochromatin silencing [he-2017-heterochromatin-abstract]. In mammals, however, POLE4 has acquired an essential role in maintaining Polε complex stability, making it indispensable for normal development [bellelli-2018-pole-instability-abstract].

The histone fold domains of POLE4 belong to a superfamily that includes not only core histones but also transcription factors (NF-Y subunits, TAF subunits of TFIID) and other DNA-associated proteins. This domain architecture appears repeatedly in proteins that need to bind DNA in a sequence-independent manner or that mediate protein-protein interactions within large complexes. The evolutionary recruitment of histone-fold proteins into the DNA replication machinery likely reflects the ancient coordination between DNA synthesis and chromatin assembly.

## Open Questions

Several important questions about POLE4 function remain unresolved:

1. **Structural dynamics at the replication fork**: How does the POLE3-POLE4 heterodimer coordinate histone binding and release with the polymerase catalytic cycle? High-resolution structures of the complete replisome with bound histones would illuminate this mechanism.

2. **Relative contributions to leading strand synthesis versus histone chaperoning**: Can the processivity and histone chaperone functions of POLE3-POLE4 be genetically separated, and if so, which function is more critical for the observed phenotypes?

3. **Therapeutic targeting**: Can POLE4 be selectively targeted in cancer therapy, and what would be the consequences of inhibiting POLE4 function in normal proliferating tissues?

4. **Interaction with DNA repair pathways**: The synthetic interaction between POLE4 loss and PARP inhibition suggests that POLE4 may have roles in DNA repair beyond its established replication functions. The nature of post-replicative repair pathways requiring POLE4 deserves further investigation.

5. **Epigenetic consequences**: What are the long-term epigenetic consequences of POLE4 deficiency in surviving cells? Do defects in parental histone recycling lead to altered gene expression programs or cellular identity changes?

6. **ATAC complex function**: Does POLE4 play a genuine functional role in the ATAC transcriptional coactivator complex, and if so, how are its replication and transcription functions coordinated?

## References

* [li-2000-pole4-identification-abstract] Li Y, Pursell ZF, Linn S. Identification and cloning of two histone fold motif-containing subunits of HeLa DNA polymerase epsilon. J Biol Chem. 2000;275(30):23247-52. PMID: 10801849. DOI: 10.1074/jbc.M002548200

* [bellelli-2018-pole-instability-abstract] Bellelli R, Borel V, et al. Polε Instability Drives Replication Stress, Abnormal Development, and Tumorigenesis. Mol Cell. 2018;70(4):707-721.e7. PMID: 29754823. PMCID: PMC5972231. DOI: 10.1016/j.molcel.2018.04.008

* [bellelli-2018-histone-chaperone-abstract] Bellelli R, Belan O, Pye VE, Clement C, et al. POLE3-POLE4 Is a Histone H3-H4 Chaperone that Maintains Chromatin Integrity during DNA Replication. Mol Cell. 2018;72(1):112-126.e5. PMID: 30217558. PMCID: PMC6179962. DOI: 10.1016/j.molcel.2018.08.043

* [logan-2018-pole-image-syndrome-abstract] Logan CV, Murray JE, Jackson AP, et al. DNA Polymerase Epsilon Deficiency Causes IMAGe Syndrome with Variable Immunodeficiency. Am J Hum Genet. 2018;103(6):1038-1044. PMID: 30503519. PMCID: PMC6288413. DOI: 10.1016/j.ajhg.2018.10.024

* [hill-2024-parpinhibitor-abstract] Hill BR, Ozgencil M, Buckley-Benbow L, et al. Loss of POLE3-POLE4 unleashes replicative gap accumulation upon treatment with PARP inhibitors. Cell Rep. 2024;43(5):114205. PMID: 38753485. DOI: 10.1016/j.celrep.2024.114205

* [mamar-2024-parpinhibitor-abstract] Mamar H, Fajka-Boja R, Mórocz M, et al. The loss of DNA polymerase epsilon accessory subunits POLE3-POLE4 leads to BRCA1-independent PARP inhibitor sensitivity. Nucleic Acids Res. 2024;52(12):6994-7011. PMID: 38828775. PMCID: PMC11229324. DOI: 10.1093/nar/gkae439

* [he-2017-heterochromatin-abstract] He H, Li Y, Dong Q, et al. Coordinated regulation of heterochromatin inheritance by Dpb3-Dpb4 complex. Proc Natl Acad Sci U S A. 2017;114(47):12524-12529. PMID: 29109278. PMCID: PMC5703312. DOI: 10.1073/pnas.1712961114


## Citations

1. bellelli-2018-histone-chaperone-abstract.md
2. bellelli-2018-histone-chaperone-summary.md
3. bellelli-2018-pole-instability-abstract.md
4. bellelli-2018-pole-instability-summary.md
5. he-2017-heterochromatin-abstract.md
6. he-2017-heterochromatin-summary.md
7. hill-2024-parpinhibitor-abstract.md
8. hill-2024-parpinhibitor-summary.md
9. li-2000-pole4-identification-abstract.md
10. li-2000-pole4-identification-summary.md
11. logan-2018-pole-image-syndrome-abstract.md
12. logan-2018-pole-image-syndrome-summary.md
13. mamar-2024-parpinhibitor-abstract.md
14. mamar-2024-parpinhibitor-summary.md
15. moiseeva-2016-pole1-phosphorylation-abstract.md