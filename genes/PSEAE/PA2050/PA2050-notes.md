# PA2050 (Q9I265) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I265 --alias PA2050` (the symbol-based fetch timed out on a UniProt
search; the accession fetch worked). Accession Q9I265 matches the worklist. Unreviewed entry. No
deep-research provider was used; literature searched in Europe PMC (queries: "PA2050 AND aeruginosa",
and FoxI/FiuI/PA0472/PA2468 variants) and PubMed MCP.

### Identity

- ECF (group IV) sigma-70 family factor: PF04542 Sigma70_r2, PF08281 Sigma70_r4_2, TIGR02937, PTHR43133:SF63. No gene name (PE 3); folder uses the locus tag.
- The UniProt "Belongs to the sigma-70 factor family. ECF subfamily" note is ARBA-only, so the
  review cites the Pfam/NCBIfam DR lines instead.

### Literature

Seed paper PMID:18086184: abstract only (not in PMC).

[PMID:18086184 "the ECF sigmas PA0149, PA1912, PA2050, PA2093 and PA4896 have been overexpressed and their target gene candidates have been identified using DNA microarray, proteomic analysis, and/or lacZ reporter construct"]; [PMID:18086184 "two sigma factors, PA2050 and PA2093, regulate the synthesis of a second transducer"]. Europe PMC search for PA2050 found only transcriptomic mentions besides this paper.

### Annotation decisions

- GO:0016987 sigma factor activity (IMP, IBA, IEA): ACCEPT, core MF.
- GO:0003700 DNA-binding transcription factor activity (IEA): MODIFY to GO:0016987; sigma factors are
  RNA polymerase specificity subunits, not stand-alone DNA-binding TFs.
- GO:0006355 (IBA, IEA): TOO_GENERAL; GO:2000142 (accepted) is an is_a descendant.
- GO:0006352 and GO:2000142 (IEA): ACCEPT.
- Transport regulation IMP row: KEEP_AS_NON_CORE, deferring to the curator who read the full text; the abstract calls the targets putative (metal) transport systems.
- Action counts: ACCEPT 6, KEEP_AS_NON_CORE 2, MODIFY 1, TOO_GENERAL 2.

## PseudoCAP IBA-seed assessment

Node-level assessment: see genes/PSEAE/PA0472/PA0472-notes.md (recorded once there); summary repeated below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002455017 | GO:0016987 sigma factor activity | 16 | 250 (29 taxa) | GO:0016987, IMP, PMID:18086184 | SOUND | Same paper and experiment as PA2093: overexpression induced specific targets; MF follows. Abstract only. | FecI, Mtb SigE/SigL (IDA), SigR, AlgU, PvdS, FpvI, SigX (IDA); Mtb SigD, VreI, PA4896 and four batch paralogues (IMP) | Yes; eight independent IDA seeds |

No `source_defects` were recorded: the PseudoCAP row is sound and the IBD is sound.

The IBD at PTN002455017 (GO:0016987, 16 seeds, 250 leaf IBAs in 29 taxa) is also seeded by IDA rows for E. coli FecI (P23484, PMID:8596456), M. tuberculosis SigE (P9WGG7, PMID:9139909) and SigL (P9WGH5, PMID:16552079), S. coelicolor SigR (Q7AKG9, PMID:9755177), and P. aeruginosa AlgU (Q06198, PMID:7644517), PvdS (G3XCV1, PMID:10692351), FpvI (Q9I193, PMID:12492864) and SigX (Q9I2W5, PMID:10438740), plus IMP rows for Mtb SigD (P9WGG9) and VreI (Q9I5P9); queried live in QuickGO on 2026-11-05. The PseudoCAP seeds from this batch (PA2093, FoxI, PA2050, PA0149, PA0472) and PA4896 add nothing the IDA seeds do not already establish. The node is an ECF sigma clade of PTHR43133, so the term suits it. No GO_CENTRAL defect is needed for this node. The node-level assessment is recorded here once, on PA0472 (FiuI), the gene with the most direct evidence; the other genes in this batch, and the parallel PA4896/vreI/pvdS/sigX/fpvI/algU reviews, cross-reference it.
