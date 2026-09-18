# Manual research synthesis: NCU04637 (Q7S3B9)

This report was researched manually on 2026-09-09 after provider failure. It is not a Falcon or Perplexity report. Sources inspected include the complete current UniProt sequence/features, the seeded GO annotations, the preserved prediction/donor records where applicable, and the primary publications cited below.

## Biological synthesis

NCU04637 encodes a fungal Rvs167-family endocytic adaptor with an N-terminal BAR domain and a C-terminal SH3 domain. Comparative evidence supports lipid binding and association with cortical actin patches, where Rvs proteins help organize endocytic membrane invaginations and vesicle scission. The detailed localization dynamics and interaction partners of the Neurospora protein remain to be established.

## Direct and comparative evidence

- file:NEUCR/NCU04637/NCU04637-uniprot.txt: “DR   PANTHER; PTHR47174:SF1; REDUCED VIABILITY UPON STARVATION PROTEIN 167; 1.”
- PMID:20610658: “We show that the purified Rvs161-Rvs167 complex binds to liposomes in a curvature-independent manner and promotes tubule formation in vitro.”
- PMID:20610658: “Rvs161 consists solely of a BAR domain, whereas Rvs167 is composed of a BAR domain followed by a region rich in glycine, proline, and alanine (GPA), and an SH3 (Src-homology 3) domain at its C-terminus”

## Rvs167 and anatomical scope

The target architecture is BAR 17–269 plus SH3 407–467, not simply an unspecified BAR protein. PTHR47174:SF1 is explicitly Rvs167; the broader InterPro BIN3/RVS161-like label is not itself a specific Rvs161 call. PMID:20610658 distinguishes Rvs161 from Rvs167 by the latter’s SH3-containing architecture. The literal fly-derived paragraph is incompatible with fungal anatomy, while its conserved endocytosis component remains well supported. PMID:19596778 reports Candida RVS167 mutant defects in actin patch polarization, supporting the process annotation. The medial-cortex and mating-projection-tip patterns remain uncertain for the Neurospora protein.

## Annotation implications

- GO:0005737: ACCEPT. Rvs167-family placement and BAR/SH3 architecture support a cytoplasmic protein acting at the cytoplasmic face of endocytic membranes. Characterized fungal Rvs proteins associate with cortical actin patches, a more precise localization than cytoplasm.
- GO:0006897: ACCEPT. The Rvs167 subfamily assignment, N-terminal BAR and C-terminal SH3 domains support conserved endocytic function. Genetic and biochemical studies of fungal Rvs proteins establish membrane association and a role in endocytic scission.
- GO:0008289: ACCEPT. Purified Rvs161–Rvs167 binds liposomes, and the target retains the BAR domain and Rvs167-specific architecture. Lipid binding is therefore a defensible conserved property; no particular lipid species is asserted.
- GO:0015629: ACCEPT. Rvs167-family proteins act at cortical actin patches during endocytosis. Target family placement and intact BAR/SH3 architecture support the curated ancestral localization inference.
- GO:0030479: ACCEPT. Rvs167-family proteins act at cortical actin patches during endocytosis. Target family placement and intact BAR/SH3 architecture support the curated ancestral localization inference.
- GO:0031097: UNDECIDED. The medial cortex annotation describes a particular spatial distribution. Conserved cortical endocytosis is supported, but the relevant ancestral localization pattern has not been established in Neurospora hyphae; family membership alone does not locate the protein specifically at the cell middle.
- GO:0043332: UNDECIDED. Mating projection tip localization may be conserved for particular Rvs proteins, but the transfer to this filamentous fungal protein requires evidence about its sexual structures and localization. The conserved endocytic role does not determine that exact spatial context.
- GO:0051666: ACCEPT. Rvs proteins contribute to cortical actin patch organization, and RVS167 deletion in Candida produces defects in patch polarization. Conservation of the Rvs167 BAR/SH3 architecture supports participation in this process.
- GO:0097320: ACCEPT. The purified fungal Rvs complex induces membrane tubules, supporting the membrane-remodeling capacity of the conserved BAR domain. In vivo scission studies favor curvature sensing and stabilization as well as possible bending, so this annotation does not imply that NCU04637 alone initiates membrane invagination.
- GO:1990528: ACCEPT. The target is assigned specifically to the Rvs167 subfamily rather than Rvs161 by PANTHER, with the expected BAR-plus-SH3 architecture. Formation of the Rvs161–Rvs167 heterodimer is a conserved fungal family property supported by biochemical work and the curated phylogenetic complex annotation.
