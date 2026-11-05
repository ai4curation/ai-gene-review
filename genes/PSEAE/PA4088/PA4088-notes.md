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

Defects: PSEUDOCAP WRONG_TERM on the EXP row (PROBABLE; abstract read only, plus sequence data). GO_CENTRAL on PTN000241400 (now PROBABLE; see the tree check below). No GO_CENTRAL defect on PTN000241365.

## PANTHER tree check (2026-11-05)

Topology of PTN000241400 in PTHR43713 fetched with `projects/PSEUDOCAP/panther_tree.py node PTN000241400 --depth 4` and `--contains`. The node is a **SPECIATION** node (Proteobacteria), 15 leaves, all PTHR43713:SF3, 13 of them named *hemL*.

| Child node | Event | Leaves | Subfamilies | Contents | Verdict |
|---|---|---|---|---|---|
| PTN002885326 / PTN002885327 / PTN000241401 | LEAF | 1 each | SF3 | hemL of *H. pylori*, *N. meningitidis*, *G. sulfurreducens* | GSAM sound |
| PTN000241402 | DUPLICATION | 2 | SF3 | *Bradyrhizobium* blr6632, blr3552 (no hemL-named copy in the family) | GSAM unverified, separate duplication |
| PTN000241405 | SPECIATION (Gammaproteobacteria) | 10 | SF3 | hemL of *Coxiella*, *Shewanella*, *Vibrio*, *Xanthomonas*; PTN002463962; PTN001736628 | GSAM sound |
| PTN002463962 | DUPLICATION | 3 | SF3 | **PA4088 (PTN002463963), PA5523 (PTN002463964), PAO1 HemL P48247 (PTN002463965)** | HemL retained in P48247; PA4088/PA5523 diverged |
| PTN001736628 | SPECIATION (Enterobacteriaceae) | 3 | SF3 | *Salmonella*, *Yersinia*, *E. coli* hemL (P23893, the seed) | GSAM sound |

Two things change the earlier call:

- The premise that PA4088, PA5523, blr6632 and blr3552 form a single divergent lineage is **wrong**. The *Bradyrhizobium* pair is its own duplication near the base of the node; PA4088 and PA5523 are *Pseudomonas*-specific, and their closest relative in the tree is PAO1 HemL itself. `--contains Q9HWU0,Q9HT50` returns PTN002463962, a three-leaf duplication that also holds P48247; `--contains Q9HWU0,P23893` returns PTN000241405.
- Consequently **the IBD cannot be moved to a HemL-only subclade** — no such clade exists, because the paralogs are nested inside the HemL radiation. The node placement for the GSAM term is sound; the over-annotation is the post-duplication propagation to PA4088 and PA5523. The right fix is a NOT/loss on those two leaf branches (PTN002463963, PTN002463964), and the defect explanation was rewritten to ask for that instead of relocation.

The tree raises confidence from SUSPECTED to PROBABLE: it confirms a recent lineage-specific duplication in which one copy keeps the hemL name and annotation while the other two are named only "probable aminotransferase" at ~27% identity — the classic paralog over-annotation shape. It does not establish that PA4088 has lost GSAM activity; only an assay (or the full text of PMID:29684343) would do that, so the call is not CONFIRMED.
