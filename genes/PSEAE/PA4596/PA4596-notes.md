# PA4596 (EsrC) review notes

Locus PA4596, UniProt Q9HVJ0 (unreviewed, PE 4), 172 aa as annotated. TetR-family
(PANTHER PTHR30055:SF234; InterPro IPR050109, IPR015893, IPR036271) transcriptional
regulator encoded downstream of oprJ in the nfxB-mexC-mexD-oprJ region. No
deep-research provider was available; literature search was done by hand (PubMed
MCP queries for "PA4596", "esrC" failed with API errors on 2026-11-05; the cached
PseudoCAP paper PMID:25143244 is the only primary paper on this gene known to the
reviewer).

## Literature

- PA4596 was renamed EsrC (envelope stress-regulated repressor of mexCD-oprJ)
  [PMID:25143244 "This envelope stress-regulated repressor of mexCD-oprJ has been renamed esrC."].
- Loss of PA4596 derepresses mexCD-oprJ only under envelope stress
  [PMID:25143244 "Inactivation of this gene had no impact on mexCD-oprJ expression in cells not exposed to envelope stress although its loss under envelope stress conditions yielded a > 10-fold increase in mexCD-oprJ expression."].
- Purified PA4596 binds the mexCD-oprJ promoter region (EMSA)
  [PMID:25143244 "the purified protein was able to bind to a DNA fragment carrying the mexCD-oprJ promoter region"].
- esrC expression is AlgU-dependent and envelope-stress inducible, and NfxB
  represses esrC; EsrC repressor activity may depend on NfxB
  [PMID:25143244 "suggesting that PA4596 repressor activity may be dependent on NfxB"].
- Cached paper is abstract-only (`full_text_available: false`).

## Gene model

`PA4596-bioinformatics/RESULTS.md`: the annotated start probably truncates TetR
HTH helix 1 (no PF00440/IPR001647 match; reading frame open 93 codons upstream;
70/73 UniRef50 members are >= 180 aa). Recorded as a SUSPECTED WRONG_START_SITE
gene model issue. Not relevant to the GO calls.

## PseudoCAP IBA-seed assessment

All three IBA rows come from PTN004738546 (TetR family node; 411 leaf IBAs across
33 taxa). PA4596 seeds only the GO:0006355 IBD (19 seeds). The node is shared with
nfxB, nalC, PA3678, atuR and nalD, which a parallel review covers; the shared-node
(GO_CENTRAL) verdict is recorded on those genes, and no duplicate GO_CENTRAL defect
is recorded here.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0006355, IDA, PMID:25143244 (PseudoCAP) | 18 others, incl. E. coli AcrR (P0ACS9) and other E. coli/M. tuberculosis TetR regulators, P. aeruginosa mexZ, psrA, PA3678 | Yes; many independent experimentally characterised TetR repressors | SOUND | The abstract states both the EMSA binding of purified PA4596 to the mexCD-oprJ promoter and the >10-fold derepression in the mutant under envelope stress. This is direct evidence for a DNA-binding transcriptional regulator. The seed is under-specific (negative regulation, GO:0045892, is supported) but not wrong, and the generic node term suits a TetR-family clade. No PseudoCAP defect. |

Shared-node verdict: recorded on nfxB/nalC/PA3678/atuR/nalD by the parallel review.
