# xcpU (Pseudomonas aeruginosa PAO1, Q00515) curation notes

## 2026-11-13 initial review

- Reviewed as the characterized GspH minor-pseudopilin exemplar for
  `modules/bacterial_type_ii_secretion.yaml`, alongside the KT2440 member `genes/PSEPK/xcpU`.
- Deep research was not run (no provider credentials in this environment); no
  `-deep-research-<provider>.md` file was created. Sources are the GOA-cited cached publications and the
  curated UniProt record.
- XcpU joins the pseudopilus tip through XcpW, making the tip complex quaternary rather than ternary
  [PMID:19828448 "This observation suggested the existence of a quaternary, rather than ternary, complex
  (XcpU(H)-V(I)-W(J)-X(K)) at the tip of the pseudopilus"].
- PANTHER places XcpU in PTHR30093:SF44, the GspG subfamily, rather than in a GspH-specific subfamily;
  the T2SS terms of PTN000764351 are nevertheless true of it, and the GspH-specific grounding comes from
  NCBIfam TIGR01708 and InterPro IPR049875.
- The two PseudoCAP phenotype rows from the Overhage et al. swarming screen are marked as
  over-annotations. The defects are shared by xcpS, xcpT and xcpY insertion mutants
  [PMID:17158671 "All mutants except the xcpQ mutant showed the same swarming and biofilm-deficient
  phenotype"], and the authors leave the mechanism open
  [PMID:17158671 "It still remains whether the excretion of an exoproduct of the Xcp machinery is
  necessary for swarming and biofilm formation or whether the pseudopilus itself is involved in these
  phenotypes"]. Swarming is performed by the flagellum, so this is necessity evidence for an indirect
  effect. The same reasoning was applied to the PA5208 rows from the same screen.
- The recurring PseudoCAP defects on the GO:0015627 IDA (reference) and GO:0015628 IDA (evidence code)
  are recorded as for the other Xcp proteins.
