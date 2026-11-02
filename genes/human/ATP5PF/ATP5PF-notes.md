# ATP5PF notes

## 2026-10-05 review (PAINT, affinage)

- **Affinage record NOT saved.** Its trust gate flagged a symbol collision, and the gate was right. The narrative's lead finding (PMID:7866306) is about yeast ATP5, which is OSCP (the ortholog of human ATP5PO), not coupling factor 6. The remaining findings concern human ATP5J/CF6 (cancer migration, vasoactive CF6, microglia, S100A9, POU3F3, DDX21), and none bears on the GOA rows. The check copy stays outside the gene folder.
- F6 [PMID:1825642 "Coupling factor 6 (F6) is a component of mitochondrial ATP synthase which is required for the interactions of the catalytic and proton-translocating segments."].
- Following the merged ATP6V1C2 and ATP5MC1 reviews (and the ATP5ME PR #4336): proton transmembrane transporter activity (IEA) over-annotated, proton transport (IEA) non-core, complex, contributes_to, ATP synthesis and location rows accepted.
- Substantia nigra development (HEP, PMID:22926577) marked over-annotated, the majority treatment of this study's rows across the repo.
- 22 GO:0005515 IPIs removed. The ATP5F1A and ATP5PD rows reflect complex co-membership.

## 2026-10-05 revision (reviewer round 1)

- Corrected the PMID:22926577 description: the study covers Alzheimer's disease, Huntington's disease and multiple sclerosis, not Parkinson's.
- GO:0015078 now cites UniProt's F(o) composition line (c, a, 8, e, f, g, k, j, which does not include F6) instead of the F(1)/F(0) typo line.
- GO:1902600 (GO_REF:0000108 from GO:0015078) was briefly changed to over-annotated in round 1, then restored to non-core in round 2 (see below).
- Replaced the uncited circulating-CF6 suggested question with a peripheral-stalk assembly question supported by PMID:26297831.

## 2026-10-05 revision (reviewer round 2)

- Restored GO:1902600 to KEEP_AS_NON_CORE. The MF asks whether F6 conducts protons (no); the BP asks whether it takes part in the complex that does (yes, as the stator). This matches ATP6V1C2, ATP5PO, ATP5F1A and ATP5MC1, and the accepted ATP synthesis rows here. The reason now notes that the term is kept at the complex level rather than through the rejected MF row.
- Label casing fixed (builder used str.capitalize).
