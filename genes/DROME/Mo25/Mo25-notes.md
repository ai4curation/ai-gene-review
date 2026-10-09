# Mo25 (CG4083; UniProt P91891) notes

- MO25/CAB39 family armadillo-like scaffold (UniProt: "Belongs to the Mo25 family").
- Fly Mo25 binds LKB1 in vivo and acts with the GC kinase Fray in neuroblast asymmetric division
  [PMID:18054329 "Drosophila Mo25 interacts with the tumor suppressor kinase Lkb1 in vivo, as have shown in mammals"];
  [PMID:18054329 "mo25 and fray mutants show an indistinguishable defect in Miranda localization"].
- Localization: cytoplasmic, relocalized to cortex by LKB1 overexpression
  [PMID:18054329 "Overexpression of Lkb1, which accumulates in the cell cortex, drastically relocalizes both Mo25 and Fray from the cytoplasm to the cortex"].
- LKB1 cofactor in fly S2R+ cells; co-IP with LKB1 together with Stlk
  [PMID:36899949 "However, no differences in Stlk/Mo25 binding were detectable in co-immunoprecipitation assays (Figure 4G)"].
- LKB1 complex activity lowers mTOR [PMID:36899949 "Cells expressing phospho-deficient LKB1 consequently display enhanced AMPK activation and decreased mTOR activity, resulting in reduced cell size."]
  -> GOA "positive regulation of TORC1 signaling" (TAS) has the wrong sign; MODIFY to negative regulation (consistent with Lkb1 review).

## Deep research
- Falcon deep research was attempted but the run was killed (exit 137, memory pressure on the shared host); notes based on cached publications.

## Decisions
- ND root MF -> MODIFY to protein serine/threonine kinase activator activity (GO:0043539).
- Core: GO:0043539 in the LKB1-Stlk-Mo25 complex (GO:1902554), cytoplasm.
