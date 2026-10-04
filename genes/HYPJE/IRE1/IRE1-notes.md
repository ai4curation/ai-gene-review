# IRE1 evidence notes

## 2026-09-30 APOPTOSIS completion pass

Marked the review `COMPLETE` after revalidating the fungal IRE1 death-branch
calls. The existing focused OpenScientist follow-up had already resolved the
two mammalian over-propagations in the right direction: `GO:0070059 intrinsic
apoptotic signaling pathway in response to endoplasmic reticulum stress` stays
`MARK_AS_OVER_ANNOTATED` as a mammalian ERN apoptosis branch imported onto a
fungal SF6 IRE1 protein, and `GO:1990604 IRE1-TRAF2-ASK1 complex` stays
`REMOVE` because Trichoderma lacks TRAF2 and ASK1/MAP3K5.

The obsolete `GO:0051082 unfolded protein binding` rows still `MODIFY` to
`GO:0002235 detection of unfolded protein`: that keeps the sensor biology in
BP space without asserting chaperone/holdase activity or direct Trichoderma
ligand-binding kinetics. Broad molecular-function ancestors were also tightened
to the more informative terms already supported in the review: ATP binding,
RNA endonuclease activity, protein Ser/Thr kinase activity, and magnesium ion
binding.

## 2026-09-20 full-gene re-review

All 21 source assertions reviewed and preserved. Primary PMID:15480788 remains abstract-only after official refetch; the full target Falcon report was read but does not replace direct access to all experimental details. Accessible primary directly establishes kinase autophosphorylation, yeast complementation, HAC1 processing and bip1/pdi1 induction. The description and core functions now distinguish biochemical kinase proof, genetic support for conserved RNase/sensing and inferred topology/cofactors. Provider paraphrases were replaced with exact primary excerpts. No new annotation rows were manufactured.

Live QuickGO confirms GO:0051082 is obsolete; its historical definition is merely unfolded-protein binding, not chaperoning. The obsoletion comment suggests folding chaperone/holdase for appropriate proteins, not a universal mapping. Yeast PMID:21852455 directly demonstrates Ire1 ligand binding and peptide-induced oligomerization: sensors can bind unfolded proteins. For these legacy target assertions, MODIFY to active BP GO:0002235 detection of unfolded protein explicitly captures signal detection rather than asserting a folding/holdase activity. Direct Trichoderma ligand binding was not verified. Original source GO ids/labels/evidence remain unchanged.

Current PANTHER treeinfo v19 identifies TreeGrafter source PTN001017826 as Sclerotinia sclerotiorum A7EHN1/SS1G_04823. Current PAINT places the ER-stress apoptotic and IRE1-TRAF2-ASK1 complex IBDs at PTN000359344 on a distinct mammalian branch, absent from this fungal leaf's ancestors. Thus current source reconciliation is defective, but it is not proof of biological impossibility. No verified whole-proteome ortholog-absence analysis or target death assay supports the old categorical exclusions. Both functions are UNDECIDED and a neutral focused OpenScientist report has been requested after negative exact-target repository/global-cache checks.

The direct enzyme and broad parent annotations remain ACCEPT: RNA cleavage is hydrolase work, phosphorylation is transferase work, and ATP/metal binding support kinase catalysis. Target ER membrane topology is inferred by conserved sequence architecture.


## Recovery review consistency follow-up (2026-09-22)

Restored readable identifiers in manual prose. Where applicable, reconciled AP3M2 reference notes with the retained contextual claim, removed unrelated PIK3C3 support from unresolved projections, separated PIK3C3 aspect-specific reasons, and documented the surviving/renamed ATG14 membrane term. Source assertion fields and verbatim quotations are unchanged.


## Focused OpenScientist fungal IRE1 follow-up

The focused report resolves the two pending mammalian death-arm rows. G0RBE3 remains a conserved fungal IRE1 UPR sensor with kinase and RNase activities, but the IRE1-TRAF2-ASK1 complex requires TRAF2 and ASK1/MAP3K5, neither of which was found in the Trichoderma proteome; ASK1 was not recovered from Fungi at all. The apoptosis and complex evidence belongs to mammalian PTHR13954:SF17 IRE1, whereas G0RBE3 and the TreeGrafter Sclerotinia source are fungal SF6 IRE1 proteins. GO:1990604 is now REMOVE and GO:0070059 is MARK_AS_OVER_ANNOTATED as a mammalian subfamily carry-over.
