# PA0472 (Q9I646) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I646 --alias PA0472` (the symbol-based fetch timed out on a UniProt
search; the accession fetch worked). Accession Q9I646 matches the worklist. Unreviewed entry. No
deep-research provider was used; literature searched in Europe PMC (queries: "PA0472 AND aeruginosa",
and FoxI/FiuI/PA0472/PA2468 variants) and PubMed MCP.

### Identity

- ECF (group IV) sigma-70 family factor: PF04542 Sigma70_r2, PF08281 Sigma70_r4_2, TIGR02937, PTHR43133:SF63. FiuI (also FiuS); fiuI-fiuR (PA0472-PA0471) upstream of fiuA (PA0470). UniProt carries no gene name, so the folder uses the locus tag.
- The UniProt "Belongs to the sigma-70 factor family. ECF subfamily" note is ARBA-only, so the
  review cites the Pfam/NCBIfam DR lines instead.

### Literature

Seed paper PMID:16484199: full text read on the PMC article page (PMC1426570); cached file is abstract-only.

[PMID:16484199 "The involvement of this putative regulatory locus in the specific induction of the ferrioxamine B and ferrichrome receptors has been demonstrated"]. Full text (PMC1426570, read 2026-11-05): a fiuI (PA0472) ISphoA/hah mutant did not produce FiuA in ferrichrome and lacked the 7-fold ferrichrome induction of fiuA-lacZ; complementation with pMMBFiuI restored FiuA; FiuI overexpression raised fiuA promoter activity 13.5- and 20-fold. [PMID:35138377 "The regulatory proteins FoxR and FiuR act as anti-sigma factors in that they inhibit the sigma factors FoxI and FiuI"]. FiuA imports ferrichrome-type siderophores [PMID:39138320 "ferricrocin-Fe and ferrichrycin-Fe by FpvB and FiuA"].

### Annotation decisions

- GO:0016987 sigma factor activity (IMP, IBA, IEA): ACCEPT, core MF.
- GO:0003700 DNA-binding transcription factor activity (IEA): MODIFY to GO:0016987; sigma factors are
  RNA polymerase specificity subunits, not stand-alone DNA-binding TFs.
- GO:0006355 (IBA, IEA): TOO_GENERAL; GO:2000142 (accepted) is an is_a descendant.
- GO:0006352 and GO:2000142 (IEA): ACCEPT.
- Transport regulation IMP row: MODIFY to GO:0034758 positive regulation of iron ion transport (full text shows induction of the siderophore receptor, which imports iron), non-core.
- Action counts: ACCEPT 5, KEEP_AS_NON_CORE 1, MODIFY 2, TOO_GENERAL 2.

## PseudoCAP IBA-seed assessment

Node-level assessment held here (see below).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002455017 | GO:0016987 sigma factor activity | 16 | 250 (29 taxa) | GO:0016987, IMP, PMID:16484199 | SOUND | Full text: loss-of-function mutant, complementation and overexpression all show FiuI is required and sufficient for fiuA promoter activity. The most direct evidence among the five. | FecI, Mtb SigE/SigL (IDA), SigR, AlgU, PvdS, FpvI, SigX (IDA); Mtb SigD, VreI, PA4896 and four batch paralogues (IMP) | Yes; eight independent IDA seeds |

No `source_defects` were recorded: the PseudoCAP row is sound and the IBD is sound.

The IBD at PTN002455017 (GO:0016987, 16 seeds, 250 leaf IBAs in 29 taxa) is also seeded by IDA rows for E. coli FecI (P23484, PMID:8596456), M. tuberculosis SigE (P9WGG7, PMID:9139909) and SigL (P9WGH5, PMID:16552079), S. coelicolor SigR (Q7AKG9, PMID:9755177), and P. aeruginosa AlgU (Q06198, PMID:7644517), PvdS (G3XCV1, PMID:10692351), FpvI (Q9I193, PMID:12492864) and SigX (Q9I2W5, PMID:10438740), plus IMP rows for Mtb SigD (P9WGG9) and VreI (Q9I5P9); queried live in QuickGO on 2026-11-05. The PseudoCAP seeds from this batch (PA2093, FoxI, PA2050, PA0149, PA0472) and PA4896 add nothing the IDA seeds do not already establish. The node is an ECF sigma clade of PTHR43133, so the term suits it. No GO_CENTRAL defect is needed for this node. The node-level assessment is recorded here once, on PA0472 (FiuI), the gene with the most direct evidence; the other genes in this batch, and the parallel PA4896/vreI/pvdS/sigX/fpvI/algU reviews, cross-reference it.
