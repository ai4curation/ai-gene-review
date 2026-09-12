# clpB (Chaperone protein ClpB) — Pseudomonas putida KT2440

UniProt: Q88Q71 (CLPB_PSEPK); locus PP_0625; 854 aa; PE 3 (Inferred from homology).
Belongs to the ClpA/ClpB family. Member of COG0542; HSP100/Clp AAA+ class.

## FUNCTION

ClpB is an ATP-dependent molecular chaperone (HSP100/Clp family) that functions as a
protein disaggregase. Together with the DnaK/DnaJ/GrpE (Hsp70) co-chaperone system it
extracts polypeptides from protein aggregates and promotes their refolding to the native
state, allowing the cell to recover from heat- and stress-induced protein damage. ClpB acts
upstream of DnaK in processing aggregates: ATP hydrolysis by its two nucleotide-binding
domains (NBD1, NBD2) drives translocation/threading of substrate polypeptides, pulling
aggregates apart. Substrate (unfolded/misfolded protein) binding stimulates the ATPase
activity. Unlike ClpA and ClpX, ClpB does NOT partner with the ClpP peptidase and is
therefore NOT a protease regulatory subunit — it solubilizes and refolds rather than
degrades proteins. ClpB is central to acquired thermotolerance.

Provenance:
- [UniProt "Part of a stress-induced multi-chaperone system, it is involved in the recovery of the cell from heat-induced damage, in cooperation with DnaK, DnaJ and GrpE."]
- [UniProt "Acts before DnaK, in the processing of protein aggregates."]
- [UniProt "Protein binding stimulates the ATPase activity; ATP hydrolysis unfolds the denatured protein aggregates, which probably helps expose new hydrophobic binding sites on the surface of ClpB-bound aggregates, contributing to the solubilization and refolding of denatured protein aggregates by DnaK"]
- [UniProt "Belongs to the ClpA/ClpB family."]

## SUBUNIT / STRUCTURE

ClpB assembles into a homohexameric ring; oligomerization is ATP-dependent. It contains an
N-terminal Clp repeat (R) substrate-discriminating domain (residues 3–146), two AAA+
nucleotide-binding domains (NBD1 ~159–340, NBD2 ~555–763) each with a Walker-A ATP-binding
motif (P-loop at 206–213 and 605–612), a long inserted coiled-coil "M-domain" (391–524),
and a C-terminal domain. The mobile coiled-coil/M-domain motion is essential for
disaggregation, pulling apart aggregates bound between coiled-coils of adjacent subunits.

Provenance:
- [UniProt "Homohexamer. The oligomerization is ATP-dependent"]
- [UniProt "The NBD2 domain is responsible for oligomerization, whereas the NBD1 domain stabilizes the hexamer probably in an ATP-dependent manner."]
- [UniProt "The movement of the coiled-coil domain is essential for ClpB ability to rescue proteins from an aggregated state, probably by pulling apart large aggregated proteins, which are bound between the coiled-coils motifs of adjacent ClpB subunits in the functional hexamer"]
- [UniProt "The Clp repeat (R) domain probably functions as a substrate-discriminating domain, recruiting aggregated proteins to the ClpB hexamer and/or stabilizing bound proteins."]

## LOCALIZATION

Cytoplasm.
- [UniProt "SUBCELLULAR LOCATION: Cytoplasm"]

## Core functions (synthesis)

- MF: ATP hydrolysis activity (GO:0016887) — AAA+ ATPase powering disaggregation.
- MF: misfolded/unfolded protein binding (substrate recognition); broad "ATP binding" (GO:0005524) is subsumed by the more specific ATP hydrolysis activity.
- BP: protein refolding (GO:0042026) — solubilization/reactivation of aggregates.
- BP: response to heat / cellular response to heat (GO:0009408 / GO:0034605) — stress recovery, thermotolerance.
- CC: cytoplasm / cytosol.

## Annotation review notes

- "regulation of DNA-templated transcription" (GO:0006355) is a spurious InterPro transfer
  from IPR002078 (Sigma-54 interaction domain signature). The InterPro match reflects a
  shared AAA+ ATPase fold with sigma-54-dependent transcriptional activators (e.g. NtrC),
  not a real transcriptional function. ClpB is a disaggregase with no evidence of DNA
  binding or transcriptional regulation → REMOVE.
- "ATP binding" (GO:0005524) is correct but broad/uninformative given the specific
  "ATP hydrolysis activity" term is present → MARK_AS_OVER_ANNOTATED.
- "identical protein binding" (GO:0042802) reflects homohexamer self-association; correct
  but non-core (it is structural self-assembly, not the disaggregase activity) → KEEP_AS_NON_CORE.
- "response to heat" and "cellular response to heat" are both supported (stress-induced
  multi-chaperone system, recovery from heat-induced damage); cellular response to heat is
  the more specific child → ACCEPT both.
- ClpB does NOT associate with ClpP and is NOT a protease; watch for protease/proteolysis
  over-transfer (PANTHER/PRINTS map the broader ClpA/B/Clp protease family). None present in
  current GOA, but flagged.
