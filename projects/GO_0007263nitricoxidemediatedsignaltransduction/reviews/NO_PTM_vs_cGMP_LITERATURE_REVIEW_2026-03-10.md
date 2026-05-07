# Deep literature review: NO post-translational signaling vs cGMP axis

Date: 2026-03-10
Question: Is post-translational modification (PTM), especially S-nitrosylation/transnitrosylation, a major axis of NO-mediated signaling in parallel to cGMP?

## Short answer

Yes. The literature strongly supports NO-dependent PTM (especially S-nitrosylation/transnitrosylation) as a major signaling axis parallel to the canonical NO→sGC→cGMP pathway.

## Evidence base used

## 1) Quantitative PubMed landscape (Title/Abstract-focused signaling queries)

Query definitions:
- **NO_cGMP_core**: nitric oxide + (cGMP or guanylyl cyclase) + signaling/pathway
- **NO_Snitrosylation_core**: nitric oxide + (S-nitrosylation or transnitrosylation) + signaling/pathway
- **NO_PTM_broad**: nitric oxide + (post-translational or S-nitrosylation or nitration) + signaling/pathway

Total hit counts (current run):
- NO_cGMP_core: **5601**
- NO_Snitrosylation_core: **1111**
- NO_PTM_broad: **1865**

Interpretation:
- cGMP-axis remains larger, but PTM/S-nitrosylation signaling is a very large and sustained literature domain, not a niche edge case.

## 2) Time-trend comparison (5-year bins)

Bin | cGMP | PTM
---|---:|---:
1995–1999 | 661 | 38
2000–2004 | 987 | 88
2005–2009 | 1184 | 226
2010–2014 | 1090 | 382
2015–2019 | 880 | 379
2020–2024 | 625 | 315

Interpretation:
- PTM/S-nitrosylation signaling rose strongly from 2005 onward and remains substantial in modern literature.
- PTM volume is lower than cGMP but clearly of comparable biological importance in many contexts (neuro, cancer, inflammation, ischemia-reperfusion, etc.).

## 3) Representative mechanistic papers (PTM axis)

- PMID:10442087 — *S-nitrosylation of proteins* (foundational PTM concept).
- PMID:11086993 — nNOS/CAPON coupling to Dexras1; NO-targeted signaling specificity.
- PMID:16908409 — NMDA-NO signaling through Dexras1 in neuronal iron homeostasis.
- PMID:30464072 — pathophysiological role of S-nitrosylation/transnitrosylation networks.
- PMID:33957758 — transnitrosylation signaling networks in inflammaging/neurodegeneration.
- PMID:39299646 — modern transnitrosylase-focused synthesis.

## 4) Representative canonical papers (cGMP axis)

- PMID:27451093 — endothelium-dependent NO-cGMP pathway review.
- PMID:31747372 — cGMP system overview.
- PMID:36400326 — NO/cGMP/CREB pathway in AD context.

## Conclusion for curation policy

- Treat NO signaling as **dual-major-axis**:
  1. **Canonical NO→sGC→cGMP signaling**
  2. **NO-driven PTM signaling** (S-nitrosylation/transnitrosylation and related redox PTMs)

- For annotations:
  - Prefer cGMP terms where the mechanism explicitly depends on sGC/cGMP effectors.
  - Prefer PTM/NO-response terms where mechanism is direct modification of proteins by NO-derived chemistry.

## Implication for Rasd1/NOS-CAPON-Dexras curation

- The Dexras pathway belongs naturally to the PTM/NO-targeted signaling side (and NO-response/neuronal pathway context), not necessarily to broad GO:0007263.
- Existing terms often suffice for individual assertions (e.g., GO:0071732 + pathway-context terms), but repeated “NO-dependent Ras activation” use cases may justify a future focused NTR.

## NTR stance from this review

- **General NTR for “NO PTM signaling” is not needed** (well-established broad ontology coverage exists).
- **Potential focused NTR may be warranted later** if many curation cases require a more specific concept like NO-dependent Ras signaling and existing terms repeatedly lose mechanistic precision.
