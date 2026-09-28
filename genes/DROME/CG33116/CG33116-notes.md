# CG33116 evidence notes

Q9VIU4 is the native 427-residue PA product of FBgn0053116 (AAF53821/NP_788074); FlyBase lists one transcript and one polypeptide. The locus is also called dCCS1 and formerly CG10355. [FlyBase](https://flybase.org/reports/FBgn0053116).

[PMID:23449981](https://pmc.ncbi.nlm.nih.gov/articles/PMC3630839/) is cached with full text. Its title emphasizes the Golgi ceramide phosphoethanolamine synthase, but its experiments also explicitly assay CG33116. The comparative family analysis identifies “three proteins from the CEPT subfamily (dCCS1/CG33116, dCCS2/CG6016 and dCCS3/CG7149)”. It tests all four candidate synthases and assigns CPE synthesis to CG4585/dCCS4, not CG33116. The phosphatidylethanolamine activity in the review is a conserved-subfamily/PAINT inference, not a misreading of the CPE assay as a positive CG33116 result.

The decisive localization passage is “Both dCCS1-V5 and dCCS2-V5 localized exclusively to the ER”, with overlapping ER marker staining in S2 cells and consistent results in HeLa. The same experiment places dCCS3/dCCS4 at the Golgi. Thus CG33116 has specific evidence of localization divergence within the ancestral family: the Golgi IBA is removed while ER assignments are accepted. This judgment rests on the actual target comparison, not on the number of descendants supporting the ancestral annotation.

The original ProtNLM name in current UniProt and source predictions is not the proof of substrate specificity. The published subfamily analysis, direct ER localization, and curated ancestral activity assignment supply the inference. All three original GO predictions are LSP relative to those more precise functions and locations.

The completed Falcon investigation was inspected and agrees on target identity, ER localization, the conserved PE-synthesis inference, and the distinction from CG4585. It also identifies pathway-context studies of Pect and Toll activation; these are not imported as CG33116-specific neuronal or immune functions. The decisive local excerpts are taken from the full primary article rather than repeated synthesis prose.

## 2026-09-28 IBA re-review

All four IBA rows in the current GOA file propagate from `PANTHER:PTN000045767` in PTHR10414. The PAINT table shows that the same ancestor carries ethanolaminephosphotransferase activity and phosphatidylethanolamine-biosynthetic process assertions seeded by human SELENOI/EPT1 and CEPT1 descendants, plus both ER-membrane and Golgi-apparatus assertions seeded by compartment-diverged descendants. Current PAINT also has a 2026 `GO:0004142 cholinephosphotransferase activity` IBD at the same node, seeded by CHPT1 and CEPT1 descendants but not yet present in the CG33116 GOA snapshot. The functional and ER-membrane transfers therefore still fit CG33116/dCCS1 as a CEPT-related enzyme, but donor specificity should not be treated as ethanolamine-only; the Golgi IBA remains the specific bad propagation because the full-text Vacaru comparison places CG33116/dCCS1 exclusively in the ER and the related dCCS3/dCCS4 candidates at the Golgi.

Exact searches for `CG33116`, `dCCS1`, `Q9VIU4`, and `FBgn0053116` did not identify a newer direct CG33116 biochemical or localization publication. FlyBase-linked papers from the 2000 chromosome/genome studies were not functional for CG33116; PMID:23449981 remains the primary full-text direct source.
