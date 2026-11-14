# gbcB (PA5411, Q9HTF3) notes

Sources read on 2026-11-05: UniProt Q9HTF3 (GBMOR_PSEAE), the GOA file, the cached
abstract of PMID:17951379. The PubMed MCP returned no PMC body for PMC2293255 (abstract
only), so the full text of the seed paper was not read. No deep-research provider file
(no keys). The gbdR review (genes/PSEAE/gbdR) uses the same paper.

## Biology

- A PA14 transposon screen found gbcA (PA5410) and gbcB (PA5411) mutants that grow on
  dimethylglycine but not glycine betaine; 13C-choline NMR showed the genes are needed
  for GB to DMG conversion
  [PMID:17951379 "strains with mutations in two genes, gbcA (PA5410) and gbcB (PA5411), were capable of growth on dimethylglycine (DMG), a catabolic product of GB, but not on GB itself"];
  [PMID:17951379 "Subsequent nuclear magnetic resonance (NMR) experiments with 1,2-(13)C-labeled choline indicated that these genes are necessary for conversion of GB to DMG."].
- gbcA/gbcB induction by GB or DMG depends on GbdR
  [PMID:17951379 "that is required for growth on GB and DMG and for the induction of gbcA, gbcB, and dgcAB in response to GB or DMG"].
- GbcB is the reductase component of a two-component Rieske-type glycine betaine
  monooxygenase (GbcA is the oxygenase). Domain architecture: N-terminal FAD-binding
  FR-type domain (PF00970), NAD-binding domain (PF00175), C-terminal plant-type
  [2Fe-2S] ferredoxin domain (PF00111) with four cysteine ligands (UniProt FT BINDING,
  PROSITE-ProRule). The catalytic activity (EC 1.14.13.251) and FAD/2Fe-2S cofactors are
  assigned in UniProt by similarity to Q1QYU6 (ECO:0000250), not from a P. aeruginosa
  assay.
- No direct enzymatic assay of P. aeruginosa GbcB was found. GO has no term for
  glycine betaine monooxygenase activity (EC 1.14.13.251) (local GO db and OLS searched).

## Annotation judgements

- GO:0016491 oxidoreductase activity (IBA, IEA, PseudoCAP IDA): the term is true and is
  as specific as the gene's own evidence allows; the specific reductase acceptor is not
  established. ACCEPT all three rows. The PseudoCAP IDA rests (per the abstract) on mutant
  growth and in vivo NMR, which is IMP, not IDA: WRONG_EVIDENCE_CODE, SUSPECTED, since the
  full text was not read.
- GO:0051537 2Fe-2S cluster binding: ACCEPT (four conserved Cys ligands, PROSITE).
- GO:0051536 iron-sulfur cluster binding: TOO_GENERAL (entailed by GO:0051537).
- GO:0031457 glycine betaine catabolic process, IMP: ACCEPT, core.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005342051 | GO:0016491 oxidoreductase activity | 3 | 51 (18 taxa) | GO:0016491, IDA, PMID:17951379 (PseudoCAP) | SOUND | Term correct: GbcB is an FAD/NAD/2Fe-2S reductase and the abstract shows gbcAB are needed for GB to DMG conversion. The abstract describes mutant growth and in vivo NMR, so IMP would fit better than IDA (PSEUDOCAP WRONG_EVIDENCE_CODE, SUSPECTED; full text not read). | E. coli Hcr P75824 (EcoCyc IDA GO:0016651 NAD(P)H oxidoreductase, PMID:10651802), M. tuberculosis Hmp P9WJ93 (IDA GO:0036200 and GO:0047086, PMID:19234303) | Yes; both other seeds have IDA support for oxidoreductase descendants |

The node term is the most general oxidoreductase term and suits a mixed clade of
FAD/ferredoxin reductases (Hcr, Hmp, GbcB). No GO_CENTRAL defect on PTN005342051.
gbdR (PA5380) seeds a different node (PTN000111456); no shared node in this batch.
