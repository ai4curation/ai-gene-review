# PA5017 (DipA, Q9HUF2) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUF2 --alias PA5017`; accession matches the worklist.
No deep-research provider used. PMID:22493016 has full text cached (PMC3370607) and was read.

### Literature

- [PMID:22493016 "Using biochemical and in vivo studies, we show that DipA associates with the membrane and exhibits phosphodiesterase activity but no detectable diguanylate cyclase activity."]
- PDE assay: His-tagged DipA purified from P. aeruginosa, bis-pNPP and c-di-GMP substrates
  [PMID:22493016 "Similar low activities were observed when c-di-GMP was used as a substrate"].
  Low activity is attributed to partial insolubility; EAL1 and EAL2 alanine mutants fail to
  complement swarming or dispersion and fail to suppress PA4843-induced aggregation.
- The GGDEF domain is degenerate (ASNEF) and no cyclase activity was detected.
- Dispersion phenotype is cue-general [PMID:22493016 "to be dispersion deficient in response to glutamate, nitric oxide, ammonium chloride, and mercury chloride."]

### Annotation decisions

- ACCEPT: GO:0071111 (IDA, IBA, IEA).
- KEEP_AS_NON_CORE: GO:0043200 response to amino acid (IMP); a cue-general dispersion phenotype.
- Action counts: ACCEPT 3, KEEP_AS_NON_CORE 1. No source defects.

## PseudoCAP IBA-seed assessment

Shares PTN002403463 with mucR (PA1727, Q9I310); verdicts kept consistent, see mucR notes. No
node-level defect. The node sits in PTHR44757:SF2 and is distinct from the PTN002105365 PDE node
covered in the rocR review and the PTN002895351 node covered in wspR.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002403463 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 3 | 14 (5 taxa) | GO:0071111, IDA, PMID:22493016 (PseudoCAP) | SOUND | Full text: purified DipA hydrolyses c-di-GMP and bis-pNPP; EAL motifs required. | E. coli PdeR P77334 (IDA PMID:17010156, EXP PMID:23708798), mucR Q9I310 (IDA PMID:23729646) | Yes |

Clade note (no defect recorded): leaf PA4929 (Q9HUN5) in this clade has MHYT and GGDEF domains
but no EAL domain in UniProt/InterPro, so the PDE IBA on that leaf is doubtful. This is a
leaf-level exception (a NOT for that leaf) rather than an unsound node, and PA4929 is not in
this batch.
