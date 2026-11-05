# cdhR (PA5389, Q9HTH5) review notes

No deep-research provider was available. Sources: reviewed UniProt record, cached abstract
of PMID:19406895 (PMC2857723; the PubMed MCP returned no full-text body). PubMed and Europe
PMC searches failed on 2026-11-05 (server errors), so later CdhR papers could not be retrieved.

## Function

- AraC/XylS-family regulator (HTH araC/xylS domain 213-311; N-terminal DJ-1/PfpI-like
  GATase1_AraC_ArgR_like domain), PANTHER PTHR43130.
- Required for growth on carnitine and for carnitine induction of the PA5388-PA5384 (cdh)
  transcripts
  [PMID:19406895 "The PA5389 and PA1998 transcription factors are required for growth on carnitine."];
  [PMID:19406895 "PA5389 is required for induction of the PA5388-PA5384 transcripts in response to carnitine"].
- UniProt curated function (ECO:0000269, PubMed:19406895): "Induces the transcription of the
  PA5384-PA5388 operon in response to carnitine."
- No direct DNA-binding data are in the sources read here; DNA binding rests on the AraC HTH domain.

## GO term choices

- CdhR is an activator, so the GO:0006355 rows are modified to GO:0045893 positive regulation of
  DNA-templated transcription, and GO:0003700 to GO:0001216 DNA-binding transcription activator activity.
- GO:0009896 positive regulation of catabolic process: GO has no carnitine-specific regulation term
  (GO:0042413 carnitine catabolic process has no regulation children), so this is as precise as GO
  allows. It is a regulator acting on the catabolic genes' transcription, not a participant in carnitine
  catabolism, which is the settled convention.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000111456 | GO:0006355 regulation of DNA-templated transcription | 4 | 50 (13 taxa) | GO:0006355, IMP, PMID:19406895 (PseudoCAP) | SOUND | The mutant fails to induce the cdh transcripts in response to carnitine, which directly shows CdhR regulates their transcription; AraC HTH domain. | P. aeruginosa ArgR G3XCU2, P. aeruginosa GbdR Q9HTI4, S. coelicolor AdpA Q9L062 | Yes; ArgR and GbdR are characterised AraC-family transcription factors. The general node term suits a clade of AraC regulators with mixed activator/repressor roles. No GO_CENTRAL defect. |

Defects recorded: PSEUDOCAP 0; GO_CENTRAL 0.
