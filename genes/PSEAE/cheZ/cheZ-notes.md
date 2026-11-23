# cheZ (PA1457, Q51434) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q51434 --alias cheZ`; accession matches the worklist.
Reviewed entry (function by similarity). No deep-research provider was used; PubMed search was
down (NCBI 500). Literature: the cached seed paper, abstract only (the PMC record PMC176688 is a
scanned article with no extractable body text; checked online).

### Literature

- PMID:7860605 (Masduki et al. 1995), abstract. Chemotaxis mutants were selected on swarm
  plates [PMID:7860605 "These mutants were fully motile but incapable of swarming, suggesting that
  they had a defect in the intracellular signalling pathway."]. Those mutants were PC1 (cheY)
  and PC2 (cheY cheZ). The cheZ single mutant was built by cassette insertion and phenotyped by
  swimming behaviour [PMID:7860605 "A chromosomal cheZ mutant, constructed by inserting a
  kanamycin resistance gene cassette into the wild-type gene, changed its swimming direction
  much more frequently than did wild-type strain PAO1."].
- "Swarm plate" in this 1995 chemotaxis screen is the classical soft-agar chemotaxis assay of
  swimming cells, not flagellum-dependent surface swarming (GO:0071978, a later concept in
  P. aeruginosa requiring rhamnolipid and harder agar). The abstract ties the swarm-plate defect
  to chemotactic signalling in motile cells, and no swarm-plate result is given for the cheZ
  single mutant. So the PseudoCAP GO:0071978 row is a term confusion: PSEUDOCAP WRONG_TERM,
  PROBABLE (abstract only).
- Molecular function: UniProt function is by similarity to E. coli CheZ (accelerates CheY-P
  dephosphorylation). No P. aeruginosa biochemistry found.

### Other seeds of PTN001098776

Queried live in QuickGO 2026-11-05: E. coli CheZ P0A9H9, GO:0006935 chemotaxis IMP
(PMID:353036); B. subtilis CheC P40403, GO:0050918 positive chemotaxis IMP (PMID:14749334).
Either seed alone supports the chemotaxis node term.

### Annotation decisions

- GO:0006935 chemotaxis (IBA, IMP seed): ACCEPT, core BP.
- GO:0004721 phosphoprotein phosphatase activity (IBA): ACCEPT, core MF (no aspartyl-phosphate
  phosphatase term exists).
- GO:0003824 catalytic activity (IEA): TOO_GENERAL.
- GO:0005737 cytoplasm (IEA): ACCEPT.
- GO:0009288 bacterial-type flagellum (IEA, InterPro): MARK_AS_OVER_ANNOTATED; CheZ acts on
  CheY-P in the cytoplasm, not as a flagellar component.
- GO:0050920 regulation of chemotaxis (IEA): KEEP_AS_NON_CORE.
- GO:0071978 swarming motility (IMP): REMOVE; PSEUDOCAP WRONG_TERM, PROBABLE.
- Action counts: ACCEPT 4, TOO_GENERAL 1, MARK_AS_OVER_ANNOTATED 1, KEEP_AS_NON_CORE 1,
  REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001098776 | GO:0006935 chemotaxis | 3 | 17 (13 taxa) | GO:0006935, IMP, PMID:7860605 (PseudoCAP) | SOUND | Abstract shows a cheZ insertion mutant with an altered swimming-reversal phenotype and loss of chemotactic responses in the cheY cheZ mutant. | E. coli CheZ P0A9H9 (IMP chemotaxis), B. subtilis CheC P40403 (IMP positive chemotaxis) | Yes; node term suits a CheY-P phosphatase clade |

PSEUDOCAP defects: 1 (non-seed swarming row, WRONG_TERM, PROBABLE). No GO_CENTRAL defect.
