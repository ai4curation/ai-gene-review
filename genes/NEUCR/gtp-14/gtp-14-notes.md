# NEUCR/gtp-14 manual review notes

## Scope and source availability

Provider deep research was unavailable in this sparse worktree because the
configured deep-research providers require credentials that were not present. I
used the seeded GOA review, the cached UniProt flat file, the cached PTHR47981
PAINT rows, the full-text cached Bowman et al. 2015 PVC paper, the full-text
cached Bowman 2023 PVC super-resolution paper, and the full-text cached Rivetta
et al. 2023 non-canonical autophagy paper.

## PANTHER/IBA assessment

PTHR47981 is the Rab-family PAINT tree. N. crassa RAB-7 (`Q9C2L8`, `gtp-14`,
`NCU03711`) is in `PTHR47981:SF20`, `RAS-RELATED PROTEIN RAB-7A`, together with
S. cerevisiae YPT7, S. pombe ypt7, A. nidulans AvaA/RabS, and other fungal
Rab7/Ypt7 orthologs.

The important fungal node is `PTN001178553`. It places fungal-type vacuole
membrane, regulation of non-autophagic vacuole fusion, and non-autophagic
vacuole fusion on the fungal Rab7/Ypt7 branch, while explicitly pruning the
broad lysosome and phagosome-lysosome rows inherited from a broad Rab7 node.
The node placement is therefore the point to review, and N. crassa RAB-7 is a
normal fungal descendant of that branch. The fungal-type vacuole membrane and
non-autophagic fusion rows are sound IBA transfers rather than similarity-only
or wrong-paralog calls.

The broad Rab7 node `PTN000635769` places `GO:0005770 late endosome` from
fungal and animal Rab7/Ypt7/Rab9 seeds. That row is broad but appropriate here:
the fungal `PTN001178553` node leaves the late-endosome assertion intact, and
the N. crassa PVCs labelled by RAB-7 are interpreted as late
endosome/multivesicular body-like compartments.

The generic `GO:0005773 vacuole` rows are directionally correct but parent-level
relative to `GO:0000329 fungal-type vacuole membrane`. I treated both the PAINT
and ARBA rows as too general and pointed them at the fungal membrane term.

The `GO:0005886 plasma membrane` IEA comes from UniProtKB-SubCell on a
homology-based, low-specificity `Cell membrane` comment. The direct N. crassa
papers localize RAB-7 to prevacuolar, late-endosomal, and vacuolar membranes,
and the PAINT tree has no plasma-membrane assertion for the fungal Rab7/Ypt7
branch, so I removed that row.

## Cached publication findings

Bowman et al. 2015 is the direct confocal paper that identified large
hyphal-tip prevacuolar compartments in N. crassa and localized RAB-7 to those
PVCs together with the vacuolar ATPase subunit VMA-1
[PMID:26453652, "The fluorescence from RAB-7-dsRED almost completely overlapped
the fluorescence from VMA-1-GFP"].

Bowman 2023 revisited the same PVCs with super-resolution microscopy, using
RAB-7-RFP and RAB-7-GFP as PVC markers. The paper supports the interpretation
that N. crassa PVCs are unusual hyphal-tip late endosomes/multivesicular bodies
[PMID:37093794, "These data suggest that the PVC is the late endosome in hyphal
tips."].

Rivetta et al. 2023 studied carbon-starvation-induced vacuoles and
non-canonical autophagic structures in N. crassa. mCherry-RAB7 was used as a
late endosome/vacuolar-membrane marker and concentrated on tonoplasts rather
than vacuolar bulk during starvation, but the paper did not perturb gtp-14
itself [PMID:37847028, "appears concentrated in tonoplasts/vacuolar membranes
(panel g), but clearly is not in the vacuolar bulk."].

## 2024-2026 literature search

I searched PubMed and Europe PMC for direct or newer N. crassa gtp-14/RAB-7
papers with `gtp-14`, `NCU03711`, `Q9C2L8`, `Rab7`, and `RAB-7` queries. PubMed
only found the 2015 RAB-7/PVC paper by title or abstract, and the recent Europe
PMC hits were the 2023 N. crassa PVC/autophagy papers, non-Neurospora papers, or
papers about other Neurospora G proteins. I did not find a direct N. crassa
gtp-14 deletion, nucleotide-cycle, or vacuole-fusion assay newer than the cached
localization literature.
