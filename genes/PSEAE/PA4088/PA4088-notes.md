# PA4088 (Q9HWU0) review notes

No deep-research provider was available; notes compiled from UniProt (unreviewed), the cached abstract of PMID:29684343 (full text behind subscription), a Europe PMC search, and a sequence analysis in PA4088-bioinformatics/.

- Structure: [PMID:29684343 "we crystallized the expression product of the uncharacterized pa4088 gene from the opportunistic pathogen Pseudomonas aeruginosa PAO1"]; [PMID:29684343 "The resulting high-resolution structure confirms it to be a member of the GSAM family"]; [PMID:29684343 "Continuous electron density indicates the presence of a PLP cofactor with a Schiff base linkage between the PLP cofactor and the ε-amino group of Lys286"]. No activity assay in the abstract.
- Europe PMC search "(PA4088 OR glutamate-1-semialdehyde) AND aeruginosa" (2026-11-05) found no paper reporting an activity for PA4088.
- PAO1 has a reviewed canonical HemL, PA3977 (P48247, 427 aa).
- PANTHER node PTN000241400 (15 leaves) contains canonical HemLs plus PA4088, PA5523 and B. japonicum blr6632 and blr3552.
- Sequence identity (file:PSEAE/PA4088/PA4088-bioinformatics/RESULTS.md): E. coli HemL vs PAO1 HemL 65.7%; HemL vs PA4088 about 27%; PA4088 vs PA5523 49.9%; PA4088 vs other PAO1 class-III aminotransferases 21-24%.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN000241400 | GO:0042286 glutamate-1-semialdehyde 2,1-aminomutase activity | 2 | 15 (12 taxa) | GO:0042286, EXP, PMID:29684343 (PseudoCAP) | E. coli HemL P23893 | For the canonical HemL subclade yes; for the PA4088/PA5523/blr paralog lineage no | OVER-SPECIFIC | Structure-only paper supports PLP binding and GSAM-like family membership, not GSAM activity; PA4088 is a distant paralog in a genome with its own HemL. |
| PTN000241365 | GO:0016853 isomerase activity | 3 | 100 (69 taxa) | same EXP row (propagated to the isomerase parent) | E. coli HemL P23893; Arabidopsis GSA (AT5G63570) | Yes, on E. coli and plant GSAM | OVER-SPECIFIC | IBD stands on the two GSAM seeds; the broad term at the family root is acceptable for GSAMs. No leaf IBA of this term appears on PA4088 in GOA. |

Defects: PSEUDOCAP WRONG_TERM on the EXP row (PROBABLE; abstract read only, plus sequence data). GO_CENTRAL on PTN000241400 (SUSPECTED; based on pairwise identity, not tree topology). No GO_CENTRAL defect on PTN000241365.
