# ANKK1 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKK1 (Q8NFD2) is a RIP-family kinase next to DRD2 and home of the TaqIA variant. (Round 2 correction: TaqIA is rs1800497, Glu713Lys in ANK repeat 11. Ala239Thr is rs7118900, a separate SNP in linkage disequilibrium with it.) No study has measured its kinase activity; a PubMed search for ANKK1 plus kinase activity or phosphorylation returns one variant-expression paper (PMID:20845092).
- **Catalytic check** (`ANKK1-bioinformatics/`): the Gly loop, beta-3 K51, catalytic loop HLDLKPGN (D145) and DFG@163 are all intact, at the same positions as active RIPK2. The kinase IEAs are accepted as predictions; core MF is ser/thr kinase activity.
- **Locations:** nucleus and cytoplasm (IDA/IEA/IBA) accepted; it shuttles (PMID:20845092, PMID:27166167).
- **Kept as non-core** (the retinoic-acid row moved to MARK_AS_OVER_ANNOTATED in round 2):
  - Regulation of cell cycle process (IDA plus IBA at PTN002793965): mitotic peak plus overexpression only. Human ANKK1's own IDA is among the IBD donors, which is expected, not circular.
  - Retinoic acid response (IEA from a rat IEP; an expression change during neuroblastoma differentiation).
- **FIH1 (HIF1AN) IPI ×3** (HuRI, BioPlex, kinase network): MODIFY → GO:0019899 enzyme binding, consistent with ANKDD1A (#4067). The ankyrin repeats are a likely FIH1 substrate.
- **Other IPIs removed:** YEATS4 ×2, CHN1, CHN2, CATSPERT, C12orf57.
- **PAINT:** family PTHR24198 is already committed (20 nodes, 49 node-level annotations); `just fetch-panther-paint` left it unchanged.
- **Not used:** the striatal knockout behavior (PMID:36805080) shows necessity, not molecular role, so no NEW BP is proposed.

## 2026-10-04 round 2 (reviewer comments on #4074)

- **TaqIA corrected** in the description, gap and notes: rs1800497 (Glu713Lys, ANK repeat 11), in strong linkage disequilibrium with rs7118900 (Ala239Thr) per PMID:20845092. UniProt annotates 12 ankyrin repeats, not 11.
- **Retinoic acid IEA:** KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED. My own reason denied participation. The chain is a round trip: a human IEA from a rat IEP that rests on human neuroblastoma expression data.
- **Gap:** BP_DARK changed to MF_DARK, since the kinase activity itself is unmeasured.
- **Other fixes:**
  - The GO:0106310 reason notes that serine specificity is also unmeasured.
  - The description separates the HEK293T transfection result from the mouse brain immunohistochemistry.
