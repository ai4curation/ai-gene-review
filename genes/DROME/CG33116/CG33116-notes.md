# CG33116 evidence notes

Q9VIU4 is the native 427-residue PA product of FBgn0053116 (AAF53821/NP_788074); FlyBase lists one transcript and one polypeptide. The locus is also called dCCS1 and formerly CG10355. [FlyBase](https://flybase.org/reports/FBgn0053116).

[PMID:23449981](https://pmc.ncbi.nlm.nih.gov/articles/PMC3630839/) is cached with full text. Its title emphasizes the Golgi ceramide phosphoethanolamine synthase, but its experiments also explicitly assay CG33116. The comparative family analysis identifies “three proteins from the CEPT subfamily (dCCS1/CG33116, dCCS2/CG6016 and dCCS3/CG7149)”. It tests all four candidate synthases and assigns CPE synthesis to CG4585/dCCS4, not CG33116. The phosphatidylethanolamine activity in the review is a conserved-subfamily/PAINT inference, not a misreading of the CPE assay as a positive CG33116 result.

The decisive localization passage is “Both dCCS1-V5 and dCCS2-V5 localized exclusively to the ER”, with overlapping ER marker staining in S2 cells and consistent results in HeLa. The same experiment places dCCS3/dCCS4 at the Golgi. Thus CG33116 has specific evidence of localization divergence within the ancestral family: the Golgi IBA is removed while ER assignments are accepted. This judgment rests on the actual target comparison, not on the number of descendants supporting the ancestral annotation.

The original ProtNLM name in current UniProt and source predictions is not the proof of substrate specificity. The published subfamily analysis, direct ER localization, and curated ancestral activity assignment supply the inference. All three original GO predictions are LSP relative to those more precise functions and locations.

The completed Falcon investigation was inspected and agrees on target identity, ER localization, the conserved PE-synthesis inference, and the distinction from CG4585. It also identifies pathway-context studies of Pect and Toll activation; these are not imported as CG33116-specific neuronal or immune functions. The decisive local excerpts are taken from the full primary article rather than repeated synthesis prose.

## 2026-09-28 IBA re-review

All four IBA rows in the current GOA file propagate from `PANTHER:PTN000045767` in PTHR10414. The PAINT table shows that the same ancestor carries ethanolaminephosphotransferase activity and phosphatidylethanolamine-biosynthetic process assertions seeded by human SELENOI/EPT1 and CEPT1 descendants, plus both ER-membrane and Golgi-apparatus assertions seeded by compartment-diverged descendants. Current PAINT also has a 2026 `GO:0004142 cholinephosphotransferase activity` IBD at the same node, seeded by CHPT1 and CEPT1 descendants but not yet present in the CG33116 GOA snapshot. The functional and ER-membrane transfers therefore still fit CG33116/dCCS1 as a CEPT-related enzyme, but donor specificity should not be treated as ethanolamine-only; the Golgi IBA remains the specific bad propagation because the full-text Vacaru comparison places CG33116/dCCS1 exclusively in the ER and the related dCCS3/dCCS4 candidates at the Golgi.

Exact searches for `CG33116`, `dCCS1`, `Q9VIU4`, and `FBgn0053116` did not identify a newer direct CG33116 biochemical or localization publication. FlyBase-linked papers from the 2000 chromosome/genome studies were not functional for CG33116; PMID:23449981 remains the primary full-text direct source.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 8 GOA rows, the description and the core function against PMID:23449981 (full text), the PAINT table for PTHR10414, PANTHER subfamily membership and a new small phylogeny. ProtNLM outputs were not opened or used.

Identity: Q9VIU4 is the canonical, full-length 427-aa product of FBgn0053116 (the only polypeptide). B6IDX7 and Q8T9G2 are redundant cDNA entries for the same protein, also in SF71. It is not a fragment, isoform or alternative gene model. It has 7 TM helices and an intact CAPT motif D(X)2DG(X)2(A/Y)R(X)8-16G(X)3D(X)3D at residues 113-138, including both terminal aspartates.

Evolutionary placement (new analysis, `CG33116-bioinformatics/RESULTS-rereview.md`, scripts `tree_rereview.py`, `capt_motif_rereview.py`):
- PTHR10414:SF71 has 692 UniProt members and no vertebrates (arthropods, nematodes including C. elegans ept-1/O44732, molluscs, flatworms, cnidarians). SF47 (human SELENOI/EPT1) is 717/718 vertebrate. SF71 is therefore the invertebrate counterpart of the vertebrate EPT1/SELENOI subfamily.
- Fly paralogs: bbc/CG6016 (dCCS2) is in SF37 (with yeast CPT1/EPT1 and Arabidopsis AAPT1, the CEPT1-like lineage). cpt/CG7149 (dCCS3) is in SF36. Cpes/CG4585 is outside PTHR10414.
- Identity to CG33116: CG7149 51%, SELENOI 48%, invertebrate SF71 members 42-49%, but CEPT1 25%, CHPT1 29%, bbc 33%. In the NJ tree CG33116 groups with CG7149 (bootstrap 66) in a clade with SELENOI. Deep nodes are poorly supported. The paper independently says "CG33116 and CG7149 (46% identity) have only one human orthologue and must therefore have originated from a gene duplication specific to the fly lineage" [PMID:23449981].
- Every EPT1-lineage sequence ends the motif with DHGLD; the CEPT1/CHPT1/bbc/AAPT1 group has DHGCD. This is an observation only, not evidence of specificity.

Changes from the previous version:
- Description rewritten to place CG33116 in the invertebrate EPT1/SELENOI lineage, to say that the activity is inferred and not assayed, and to separate it from Cpes.
- GO:0016780: KEEP_AS_NON_CORE changed to MODIFY → GO:0004307 (OLS confirms GO:0004307 is_a GO:0017169 is_a GO:0016780). The previous reason argued the term was too general, which requires MODIFY.
- GO:0005794 Golgi IBA stays REMOVE, with a corrected rationale. Its seeds are CHPT1 (human Q8WUD6, mouse MGI:2384841 = Chpt1, both verified via UniProt) and FBgn0031948, which is CG7149/dCCS3, the fly in-paralog. The paper shows CG33116 exclusively in the ER and CG7149 partly at the Golgi, so the compartment diverged after the duplication.
- Cholinephosphotransferase: the 2026 GO:0004142 IBD at PTN000045767 is not in this GOA snapshot. CG33116 sits in the ethanolamine-specific SELENOI lineage, not the dual-specificity CEPT1/SF27 or SF37 lineage, so choline transfer is not assumed. It stays an open question and is not added as NEW. The PTHR10414 family review also scopes GO:0004142 to SF32/SF27/SF37, which excludes SF71. This agrees.
- The other rows are unchanged in action (ACCEPT GO:0004307, GO:0005783, GO:0005789, GO:0006646; MODIFY GO:0008654 → GO:0006646, GO:0016020 → GO:0005789). Rationales and supporting quotes were refreshed, findings and reference_review were added for PMID:23449981, and suggested experiments were added.

Family review check (`interpro/panther/PTHR10414/PTHR10414-review.yaml`): no disagreement on subfamily placement. It lists CG33116 as the SF71 representative and leaves GO:0004307 scope UNRESOLVED at family level, which is consistent with this review's lineage-specific acceptance. One minor gap: its SF71 description reuses the family-level text and does not say that SF71 is the invertebrate EPT1 counterpart of SF47.

Relative for next review: human SELENOI (Q9C0D9), the vertebrate member of the EPT1 lineage (SF47, the sister of SF71) and the human orthologue named in the paper. `genes/human/SELENOI/SELENOI-ai-review.yaml` exists with all 24 annotations actioned and core functions present, so no new review is needed. The fly in-paralog CG7149/cpt has no repo review, but it has not been biochemically characterized beyond localization.

Modules: `modules/kennedy_pathway_phospholipid_synthesis.yaml` (EPT step, SELENOI/CEPT1 node) is the relevant module. CG33116 is not listed in it.
