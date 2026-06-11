# SRP72 (O76094, human) review notes

## Overview / core biology

SRP72 is the largest subunit of the signal recognition particle (SRP), a cytosolic ribonucleoprotein
that mediates cotranslational targeting of secretory and membrane proteins to the ER.

- "Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER)" [file:human/SRP72/SRP72-uniprot.txt "Component of the signal recognition particle (SRP) complex, a\nCC       ribonucleoprotein complex that mediates the cotranslational targeting"].
- SRP72 forms a heterodimer with SRP68 and together they belong to the S-domain: "Mammalian SRP is composed of six polypeptides among which SRP68 and SRP72 form a heterodimer" [PMID:16672232 "Mammalian SRP is composed of six \npolypeptides among which SRP68 and SRP72 form a heterodimer"].
- The full SRP: "consists of a 7SL RNA molecule of 300 nucleotides and six protein subunits: SRP72, SRP68, SRP54, SRP19, SRP14 and SRP9" [file:human/SRP72/SRP72-uniprot.txt "a 7SL RNA molecule\nCC       of 300 nucleotides and six protein subunits: SRP72, SRP68, SRP54,\nCC       SRP19, SRP14 and SRP9"].

SRP72 is NOT a GTPase. The GTPase activities in SRP signaling reside in SRP54 and the SRP receptor (SRPRA/SRPRB).
SRP72's role is as an RNA-binding scaffold subunit: it binds 7SL RNA (in presence of SRP68) and contributes
to ribosome contacts.

## Molecular function

- 7SL/7S RNA binding: "Binds the signal recognition particle RNA (7SL RNA) in presence of SRP68" and "Can bind 7SL RNA with low affinity" [file:human/SRP72/SRP72-uniprot.txt "Binds the signal recognition particle RNA (7SL RNA) in presence of\nCC       SRP68"].
- The C-terminal RNA-binding domain (RBD) crawls along the 5e/5f loops of SRP RNA: "The SRP72-RBD is a flexible peptide crawling along the 5e- and 5f-loops of SRP RNA. A conserved tryptophan inserts into the 5e-loop forming a novel type of RNA kink-turn" [PMID:27899666 "The SRP72-RBD is a flexible peptide crawling along the 5e- and 5f-loops of SRP RNA"].
- The N-terminal PBD (a TPR/tetratricopeptide repeat) binds SRP68: "The SRP72-PBD is a tetratricopeptide repeat, which binds an extended linear motif of SRP68 with high affinity" [PMID:27899666 "The SRP72-PBD is a tetratricopeptide repeat, which binds an\nextended linear motif of SRP68 with high affinity"]. This is the basis of the GO:0030911 "TPR domain binding" IPI annotation (SRP72 TPR is the binding entity; partner SRP68).
- SRP68/72 remodels 7SL RNA to make it competent for SRP54 binding: "SRP68/72, together with SRP19, rearranges the 7SL RNA in an SRP54 binding competent state" [PMID:17254600 "SRP68/72, together with SRP19, rearranges the \n7SL RNA in an SRP54 binding competent state"].
- RNA-binding residues mapped to region 545-617 ("RNA-binding" region; mutagenesis of basic residues abolishes binding) [file:human/SRP72/SRP72-uniprot.txt "RNA-binding"].

## Cellular component

- SRP complex (S-domain): "Component of a signal recognition particle (SRP) complex" [file:human/SRP72/SRP72-uniprot.txt "Component of a signal\nCC       recognition particle (SRP) complex"].
- Subcellular location: "Cytoplasm" and "Endoplasmic reticulum" [file:human/SRP72/SRP72-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"].
- ComplexPortal entry CPX-2652 "Signal recognition particle".
- The "nucleolus" CD-CODE annotation (DR CD-CODE; 91857CE7; Nucleolus) reflects SRP assembly trafficking; not the site of cotranslational targeting function. Treated as non-core when present (not in current GOA rows).

## Biological process

- SRP-dependent cotranslational protein targeting to membrane: "The SRP complex targets the ribosome-nascent chain complex to the SRP receptor (SR), which is anchored in the ER, where SR compaction and GTPase rearrangement drive cotranslational protein translocation into the ER" [file:human/SRP72/SRP72-uniprot.txt "The SRP complex targets the\nCC       ribosome-nascent chain complex to the SRP receptor (SR), which is\nCC       anchored in the ER"].
- Signal sequence recognition step (GO:0006617) is performed by the SRP complex (SRP54 reads the signal sequence); SRP72 is a part_of/involved_in member as an SRP subunit (NAS, ComplexPortal).

## Disease

- Bone marrow failure syndrome 1 (BMFS1, MIM:614675), autosomal dominant aplastic anemia / myelodysplasia: "autosomal-dominant SRP72 mutations associated with familial aplasia and myelodysplasia" [PMID:22541560 "autosomal-dominant SRP72 mutations associated with \nfamilial aplasia and myelodysplasia"].
- Disease variant R207H affects ER localization: "VARIANT BMFS1 HIS-207 ... affects protein localization to ER" [file:human/SRP72/SRP72-uniprot.txt "affects protein localization to\nFT                   ER"]. This is a disease phenotype, not a clean GO biological process for SRP72.

## Annotation-specific notes

- Multiple `protein binding` (GO:0005515) IPI rows from high-throughput interactome screens (PMID:32296183 binary interactome; PMID:33961781 BioPlex; PMID:35271311 OpenCell; PMID:16672232 SRP68 directed) -> bare protein binding is uninformative; KEEP_AS_NON_CORE. The SRP68 partner (Q9UHB9) is biologically meaningful but the bare term does not convey it; the heterodimer is captured by signal recognition particle binding (GO:0005047) and the SRP complex CC term.
- PMID:24965446 (pestivirus Npro host-factor screen) IPI with viral protease PRO_0000038050 — incidental capture of SRP72 in an RNP/stress-granule co-purification; non-core.
- PMID:18089836 (TAS-103) abstract foregrounds SRP54, but the curator annotated SRP72 as part_of SRP (GO:0005786) — the paper studies the SRP complex; ACCEPT the compartment.
- HDA RNA binding (PMID:22658674, PMID:22681889) — mRNA interactome capture; SRP72 binds 7SL RNA so RNA binding (GO:0003723) is correct as a general parent; the specific function is 7S RNA binding (GO:0008312).
- No GO:0030942 (SRP receptor activity) row is present in the current GOA, so no MARK_AS_OVER_ANNOTATED needed on that axis.

## Core function summary

- 7S/7SL RNA binding (GO:0008312) as the S-domain RNA-binding scaffold subunit, in heterodimer with SRP68.
- Signal recognition particle binding / SRP68 heterodimerization (GO:0005047).
- Part of the signal recognition particle (GO:0048500 / GO:0005786), acting in the cytosol/ER.
- Contributes to SRP-dependent cotranslational protein targeting to membrane (GO:0006614).
