# dsdA (PA3357, Q9HYN9) review notes

No deep-research provider was available. Literature checked by hand on 2026-11-05: cached
PMID:26957519 (abstract only; no PMC copy) and Europe PMC search '"dsdA" AND aeruginosa'. The
other hits concern E. coli, Proteus or P. putida; PMID:26957519 is the only PAO1 study.

## Function

- PLP-dependent D-serine dehydratase (D-serine ammonia-lyase, EC 4.3.1.18) of the
  serine/threonine dehydratase family, DsdA subfamily (HAMAP MF_01030). The PLP lysine is K119
  (HAMAP).
- Activity and substrate range [PMID:26957519 "Among D- and L-amino acids tested, only D-serine
  and D-threonine could serve as the substrates of DsdA, and the Km of DsdA with D-serine was
  calculated to be 330 μM."].
- Physiology: the gene is cryptic. PAO1 uses D-serine through DadA, and dsdA supports growth
  only when supplied on a plasmid [PMID:26957519 "Growth on D-serine as the sole source of
  nitrogen was retained in the ∆dsdA mutant and was abolished completely in the ∆dadA and
  ∆dadA-∆dsdA mutants."; "However, when complemented by dsdA on a plasmid, the double mutant
  was able to grow on D-serine as the sole source of carbon and nitrogen, supporting the
  proposed biochemical function of DsdA in the conversion of D-serine into pyruvate and
  ammonia."].

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; other seeds' rows from QuickGO, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000034699 | GO:0008721 D-serine ammonia-lyase activity | 2 | 7 (7 taxa) | GO:0008721, IDA, PMID:26957519 (PseudoCAP) | SOUND | The abstract states a substrate screen and a Km for D-serine (330 μM), so the activity was assayed on DsdA itself. | E. coli DsdA P00926 (IDA PMID:5327100, PMID:5327101; EcoliWiki, CACAO, EcoCyc) | Yes |

The node term is the exact reaction and suits a small DsdA clade (7 leaves). The node also
carries NOT annotations for L-serine/L-threonine dehydratase activities, consistent with the
D-specificity reported here. No PSEUDOCAP or GO_CENTRAL defect.

Other rows:
- GO:0036088 D-serine catabolic process (IBA, IEA): accepted. DsdA converts D-serine to
  pyruvate and ammonia when it is expressed, although the chromosomal gene is cryptic in
  PAO1 and DadA does this job under laboratory conditions.
- GO:0016836 hydro-lyase activity (UniRule IEA): the overall reaction is classed as an
  ammonia-lyase (EC 4.3.1.18; GO:0008721 is_a carbon-nitrogen lyase), not a C-O hydro-lyase.
  MODIFY to GO:0008721.
