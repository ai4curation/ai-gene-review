# PARD3B (donkey, A0A9L0JEY6) notes

## Sources
- Donkey UniProt A0A9L0JEY6 (unreviewed; function, subunit and location text are ARBA predictions, ECO:0000256).
- Human PARD3B Q8TEW8 UniProt record fetched to PARD3B-bioinformatics/Q8TEW8-uniprot.txt. No human/mouse PARD3B review exists in this repository; the primary PARD3B papers (PMID:12234671, PMID:12459187, PMID:16458856) are not in the local publication cache.
- Ortholog experimental GO (QuickGO): PARD3B-bioinformatics/ortholog_experimental_goa.txt.
- Alignment: PARD3B-bioinformatics/RESULTS.md.

## Biology
- PARD3B (PAR3beta/PAR3L) is the vertebrate paralog of the polarity scaffold PARD3 (PAR3 family; PANTHER PTHR16484:SF4). Human UniProt: [file:EQUAS/PARD3B/PARD3B-bioinformatics/Q8TEW8-uniprot.txt "Putative adapter protein involved in asymmetrical cell"] division and cell polarization; "May play a role in the formation of epithelial tight junctions."
- Interacts with PARD6B and INSC (experimental, PMID:12234671, PMID:16458856, per human UniProt).
- Location: endomembrane system, cell junction, tight junction; [Q8TEW8-uniprot.txt "Colocalizes with TJP1 to epithelial tight junctions."].
- Experimental GO for PARD3B orthologs is limited to protein binding, protein-containing complex and cell junction (HPA IDA).
- Family-level (PARD3) functions such as phosphoinositide binding, centrosome positioning and microtubule organization are transferred by TreeGrafter from PAINT node PTN001444301; no PARD3B-specific evidence for them was found.

## Donkey sequence
- 88.3% identity overall; PDZ1-3 and N-terminal domain 94-99% identical [file:EQUAS/PARD3B/PARD3B-bioinformatics/RESULTS.md].

## Decisions
- ACCEPT: bicellular tight junction, establishment of cell polarity, establishment or maintenance of epithelial apical/basal polarity.
- TOO_GENERAL: apical junction complex, cell junction (both entailed by bicellular tight junction).
- KEEP_AS_NON_CORE (family-level transfer, plausible, unverified for PARD3B): adherens junction, cell cortex, apical plasma membrane, intracellular protein localization, microtubule cytoskeleton organization, establishment of centrosome localization, endomembrane system, protein-containing complex.
- MARK_AS_OVER_ANNOTATED: cell adhesion (scaffold organizes junctions but is not itself an adhesion mediator).
- UNDECIDED: phosphatidylinositol binding (PARD3 property; no PARD3B data accessible).
