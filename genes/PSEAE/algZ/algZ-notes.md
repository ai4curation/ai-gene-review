# algZ / fimS (PA5262, G3XCZ2) review notes

No deep-research provider was available. Literature checked by hand on 2026-11-05: cached
PMID:8790418 (abstract only; the PMC copy PMC38516 is a page scan with no extractable text),
Europe PMC searches "AlgZR" and "AlgZ AND (fimU OR twitching)", and the full-text review
PMID:24999454 (fetched with `just fetch-pmid`).

Name caution: the name "AlgZ" was first used for the DNA-binding protein now called AmrZ
(PA3385, e.g. PMID:16352829 "ribbon-helix-helix DNA-binding protein AlgZ (AmrZ)"). PA5262 is
the FimS sensor of Whitchurch et al. 1996, now called AlgZ/FimS. The PseudoCAP rows on PA5262
cite the FimS paper (PMID:8790418), so they are on the right gene.

## Function

- Membrane sensor of the AlgZR two-component system; four predicted N-terminal TM helices
  [PMID:24999454 "the first 150 amino-terminal amino acids of AlgZ are predicted to fold as four
  transmembrane helices."].
- Required for twitching motility, together with AlgR [PMID:8790418 abstract: "Adjacent to algR
  we have identified a sensor gene (fimS), which is also required for twitching motility."].
- Atypical kinase. The H box (RPHFLFNSL) and a degenerate N box are present, but there is no
  ATP lid [PMID:24999454 "The obvious similarities between AlgZ and canonical histidine
  kinases are limited to these two boxes, as AlgZ lacks identifiable G1, F, and G2 boxes that
  make up the ATP-coordinating flexible lid."]. In vitro autophosphorylation or phosphotransfer
  to AlgR is not described in the review; the AlgZ-AlgR link rests on genetics and on AlgR
  Asp54 phosphorylation being needed for fimU activation [PMID:24999454 "Together, these data
  indicate that AlgR phosphorylation by AlgZ increased AlgR affinity to the fimU promoter and
  activated its transcription."].
- Its signal is unknown [PMID:24999454 "Though the signal for the AlgZ sensor kinase has not
  been determined, the signal, via AlgR phosphorylation, activates twitching motility by
  increasing the expression of these prepilins."].

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; other seeds' rows from QuickGO, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002531636 | GO:0007165 signal transduction | 3 | 34 (17 taxa) | GO:0000160 phosphorelay signal transduction system, IDA, PMID:8790418 (PseudoCAP) | UNVERIFIABLE | The term is right for AlgZ, a TCS sensor needed for AlgR-dependent twitching. The IDA code could not be checked: the full text is a page scan. The abstract reports identification of fimS by sequence (next to algR) and a mutant phenotype, which fits IMP/ISS better. Recorded as a SUSPECTED evidence-code defect only. | E. coli YpdA P0AA93 (IMP PMID:23222720, EcoCyc); E. coli BtsS P0AD14 (IMP and RCA PMID:22685278, EcoCyc) | Yes |

The node term signal transduction is broad but suits a LytS/YpdA-type sensor clade. The IBD
stands on the two E. coli seeds; no GO_CENTRAL defect. On AlgZ the IBA row is TOO_GENERAL,
because GO:0000160 (is_a GO:0007165) is accepted.

Related node rows not seeded by AlgZ: GO:0000155 phosphorelay sensor kinase activity (IBA,
seed YpdA only) and plasma membrane (IBA). Both are accepted: the H box is conserved and the
genetics place AlgZ as AlgR's kinase, though the missing ATP lid leaves the catalytic
mechanism open (see suggested experiment).
