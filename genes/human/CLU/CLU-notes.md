# CLU - Clusterin (Human) Notes

## Overview

Human CLU (P10909), also known as clusterin, apolipoprotein J, complement
cytolysis inhibitor, and SP-40,40, encodes a secreted glycoprotein that is
proteolytically processed into disulfide-linked alpha and beta chains. The main
secreted isoform is an extracellular ATP-independent holdase chaperone.

Key evidence anchors:
- UniProt describes isoform 1 as "Functions as extracellular chaperone that
  prevents aggregation of non native proteins" [file:human/CLU/CLU-uniprot.txt].
- UniProt states that CLU "Does not require ATP" and "Does not refold proteins
  by itself" [file:human/CLU/CLU-uniprot.txt].
- UniProt states that CLU "Maintains partially unfolded proteins in a state
  appropriate for subsequent refolding by other chaperones" [file:human/CLU/CLU-uniprot.txt].
- UniProt describes broad anti-amyloid activity: "Inhibits formation of amyloid
  fibrils by APP, APOC2, B2M, CALCA, CSN3, SNCA and aggregation-prone LYZ
  variants" [file:human/CLU/CLU-uniprot.txt].
- UniProt supports terminal complement regulation: CLU "inhibits assembly of
  the complement membrane attack complex (MAC) by preventing polymerization of
  C9" [file:human/CLU/CLU-uniprot.txt].
- The Falcon deep research synthesis frames CLU as "a central node at the
  intersection of extracellular proteostasis, complement regulation, and lipid
  transport" [file:human/CLU/CLU-deep-research-falcon.md].

## Core Function Synthesis

The core evolved function is extracellular proteostasis. Secreted CLU binds
exposed hydrophobic surfaces on stressed, misfolded, or amyloid-prone clients,
keeps those clients soluble, and routes CLU-client complexes toward receptor
uptake and downstream degradation. CLU is therefore best curated as a holdase
and carrier chaperone, not as a classical ATP-dependent foldase.

Terminal complement inhibition is also core. CLU binds soluble MAC intermediates
and prevents C9 polymerization or membrane insertion, limiting complement-mediated
cytolysis. This explains why broad "complement activation" terms should be
modified or interpreted as negative regulation of terminal complement/MAC
assembly.

CLU's apolipoprotein J role is physiologically important but should be curated
carefully. CLU associates with HDL-like particles and lipoprotein receptors, but
its primary mechanistic role in these contexts appears to be chaperone/client
transport, receptor-mediated clearance, and extracellular protein quality
control rather than primary lipid transport catalysis.

Intracellular, nuclear, mitochondrial, and stress-associated CLU forms are real
but secondary to the predominant secreted isoform. Their in-vivo physiological
specificity remains unresolved and should not be overgeneralized from stress or
cancer contexts.

## Second-Pass Review Notes

The CLU review already validated cleanly and had comprehensive action decisions.
The second pass added this notes file, recorded reference-review metadata for the
Falcon deep-research report, and added knowledge-gap questions plus suggested
experiments focused on normal in-vivo CLU biology.

Outstanding biology for expert review:
- Which endogenous CLU glycoforms, proteolytic states, redox states, pH ranges,
  and hydrophobic-tail conformations control holdase strength, client selectivity,
  and receptor engagement?
- Which receptors dominate CLU-client clearance in different tissues and cell
  types: LRP2/megalin, VLDLR, LRP8/ApoER2, TREM2, or additional receptors?
- What determines the substrate-ratio-dependent switch between inhibition and
  promotion of amyloid assembly, and how often does the pro-assembly state occur
  under physiological extracellular conditions?
- Which intracellular or nuclear CLU isoforms have evolved in-vivo functions,
  rather than representing rare translation products, failed translocation, or
  stress-induced relocalization?

## 2026-11-15 ORGANELLES Golgi batch 2 (Golgi apparatus rows)

- One GO:0005794 row: ISS (GO_REF:0000024, ParkinsonsUK-UCL) from dog CLU P25473. That donor's Golgi row is an IDA from PMID:10837345 (Bando et al. 2000, ORP150 in MDCK cells; QuickGO). I fetched it: abstract-only, no PMC record. The abstract follows ER export and maturation of endogenous GP80/clusterin and does not mention the Golgi.
- The previous ACCEPT reason said the precursor is "processed in the Golgi". The UniProt PTM line says "probably within the Golgi lumen" and cites PMID:2387851, a 1990 apoJ plasma purification whose abstract only proposes a common precursor. That is not a Golgi assay. PMID:25051234 (transfected HEK293T fractionation) only interprets fractions as ER/Golgi-related, with no marker.
- Action ACCEPT -> UNDECIDED (unreadable donor, the CD247 line). If the donor shows endogenous GP80 with a Golgi marker in its native cell, the row is KEEP_AS_NON_CORE; otherwise MARK_AS_OVER_ANNOTATED (transit). It is never core for a secreted chaperone. The ER rows were not changed (out of scope).
