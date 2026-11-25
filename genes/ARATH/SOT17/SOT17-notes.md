# SOT17 (AtST5c, At1g18590, Q9FZ80) review notes

- Desulfoglucosinolate sulfotransferase; final step of core structure [PMID:15358770 "The three enzymes were shown to catalyze the final step in the biosynthesis of the glucosinolate (GS) core structure, the sulfation of desulfoglucosinolates (dsGSs)."]; ST5b/ST5c prefer long-chain Met-derived substrates [PMID:15358770 "long chain dsGSs derived from methionine are the preferred substrates of AtST5b and AtST5c"].
- [PMID:19077143 "AtSOT17 showed an increased specific activity with increasing chain length of ds-Gl derived from methionine"].
- Cytoplasmic by GFP [PMID:16367753 "All three desulfoglucosinolate AtSOT proteins are localized in the cytoplasm"].
- Decisions: all cytoplasm, sulfotransferase, sulfation, aromatic and aliphatic dsGS SOT activities, glucosinolate biosynthesis -> ACCEPT. Nucleus HDA -> MARK_AS_OVER_ANNOTATED. Core MF GO:0120527 (aliphatic preferred); GO:0047364 kept as accepted since activity with desulfobenzyl-GS is measured (Km 100 uM per UniProt).
- No NEW terms. Deep research not present at time of review.


## Module-member evidence audit — 2026-10-25

Reviewed every original row (10) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

Purified-protein studies15358770/16367753/19077143 establish PAPS-dependent aliphatic and aromatic desulfoglucosinolate sulfation. Both substrate classes are retained in broad-MF refinement, not just the preferred one. The C24 enzyme shows increased activity with increasing methionine-derived chain length. Nuclear HDA remains undecided because targeting expectations do not invalidate a fractionation observation.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.


## 2026-10-26 — PR #5550 source-level correction

Revisited review findings 1–3 against the actual publication cache and the primary sources. Removed generic source-unresolved boilerplate where the assay design is adjudicable. Restored relevant verbatim biochemical and localization evidence; did not restore label-only CHAIN features, unrelated introductory statements, or quotations that no longer support the revised claim. Existing source annotation fields were preserved.

Read PMID:28887381 full text, especially "Identification of True Membrane-associated Proteins" and Fig. 7: washed microsomes and sucrose gradients distinguish membrane association but do not separate organelles; named compartments are imported from SUBAcon/GFP knowledge. The paper states "no organelle fell in a single cluster". Mark the specific compartment claim as over-annotated while preserving proteomic detection. This applies projects/ORGANELLES.md at the actual resolution of the assay.
