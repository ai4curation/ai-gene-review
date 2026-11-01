# CEK2 review notes

## 2026-11-01

`just fetch-gene CANAL CEK2` seeded the CGD/UniProt review for A0A1D8PT38.
Deep research with Falcon was attempted but the provider was unavailable in this
environment, so the literature sweep below was performed manually and recorded
here rather than in a provider-named deep-research file.

Cached and read the CEK2 papers that directly support the pheromone-pathway
review:

- PMID:12075459 introduced CEK2 as a *C. albicans* MAPK that complements a
  budding-yeast `fus3/kss1` mutant and reported that Cek2 phosphorylates MBP in
  vitro.
- PMID:12453219 showed that the residual mating of `cek1` cells depends on
  CEK2, with the `cek1 cek2` double mutant completely defective in mating.
- PMID:30787119 separated the Candida pheromone MAPKs: Cek1 is the major MAPK
  for pheromone response, while Cek2 supplies residual mating in a `cek1`
  background and has its strongest wild-type role in adaptation after
  pheromone-mediated arrest.
- PMID:33793759 showed Cek2 phosphorylation after pheromone stimulation and
  pheromone-induced cytoplasmic-to-nuclear localization of Cek2-GFP.
- PMID:37045865 connected CEK2 to glucose-depletion-induced white-cell mating,
  where deleting either `CEK1` or `CEK2` reduced white-cell mating and ectopic
  `CEK2`, but not `CEK1`, enhanced mating in a white-locked `wor1/wor1` mutant.

I also fetched PMID:26682470 after searching PubMed because its abstract reports
a cryptic CEK2 role in cell-wall biogenesis. Only the abstract is locally
cached, so this review records a biological follow-up question rather than a
new `GO:0009272 fungal-type cell wall biogenesis` annotation.

### PAINT and IBA calls

`interpro/panther/PTHR24055/PTHR24055-paint.tsv` places `GO:0004674 protein
serine/threonine kinase activity`, `GO:0005634 nucleus`, and `GO:0005737
cytoplasm` on broad `PANTHER:PTN000622075`. CEK2 (`CGD:CAL0000200092`) is
listed among the descendants for the catalytic node. That self-source is
expected for an IBA with target-specific evidence and is not circular.

The exact pheromone-MAPK process is on `PANTHER:PTN001172087`, seeded by
*S. pombe* `spk1` (`PomBase:SPAC31G5.09c`) and *S. cerevisiae* `FUS3`
(`SGD:S000000112`). That node fits Candida Cek2. By contrast, the exact
`GO:0004707 MAP kinase activity` PAINT node `PANTHER:PTN001171896` is a
separate branch seeded by Candida CEK1, *S. pombe* `pmk1`/`spm1`, and budding
yeast `KSS1`; it does not drive any CEK2 IBA in current GOA.

### Deferred CGD filamentation annotations

The three CGD filamentation/starvation rows and the starvation response row all
cite PMID:12773383. The cached full text describes the Spider-medium and
serum-based haploinsufficiency screen and points to Supplementary table 1 for
the gene assignments, but the cached article does not include that table and
does not mention CEK2 or `orf19.460` in the body. I left those rows
`UNDECIDED` rather than second-guessing CGD without the supplement.
