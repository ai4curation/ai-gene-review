# EMENI mon1 notes

## 2026-10-24

- Seeded Q5BBI7 with `just fetch-gene EMENI mon1`; GOA contains four PAINT
  rows from PTHR13027 and four UniProt/InterPro IEA rows, but no direct PMID
  annotations.
- `just fetch-gene-pmids EMENI mon1` found no PMID-backed GOA rows.
- `just deep-research-falcon EMENI mon1 --fallback perplexity-lite` failed
  because no research provider credentials were available in this shell, so
  this review used the cached UniProt/GOA/PAINT records, targeted web/PubMed
  searches, and cached primary literature for Aspergillus, S. cerevisiae, and
  Fusarium Mon1 proteins.
- Targeted searches for `Q5BBI7`, `AN2093`, `Aspergillus nidulans mon1`,
  `Aspergillus nidulans monA`, and `Aspergillus Mon1 Ccz1` did not find a newer
  direct A. nidulans monA functional paper that changes the 2019 MonA study.
- PTHR13027 places A. nidulans mon1 (Q5BBI7/AN2093) in the
  `PTHR13027:SF7` fungal Mon1 subfamily with S. cerevisiae MON1, S. pombe
  mon1, C. albicans MON1, A. fumigatus mon1, and Neurospora apg-13.
- The fungal PAINT node `PTN000989606` asserts `GO:0000329 fungal-type vacuole
  membrane` and `GO:0006623 protein targeting to vacuole` from the S.
  cerevisiae MON1 seed. PMID:12364329 directly shows that Mon1 and Ccz1 form a
  stable complex and that both proteins act late in multiple routes that
  deliver cargo to the yeast vacuole.
- PMID:32010467 characterized MonA directly in A. nidulans and A. flavus. The
  A. nidulans AN2093 deletion strain had reduced growth, impaired asexual and
  sexual development, lower conidial trehalose and viability, heat sensitivity,
  and abnormal CMAC-stained vacuoles. The vacuole phenotype supports
  conservation of the Mon1 vacuole-delivery module in Aspergillus, while the
  developmental and stress phenotypes are downstream consequences rather than
  additional GO targets here.
- The eukaryotic PAINT node `PTN000315021` contributes to
  `GO:0005085 guanyl-nucleotide exchange factor activity`. The
  `contributes_to` qualifier is important: Mon1 is a subunit of the Mon1-Ccz1
  Rab7/Ypt7 GEF rather than an active standalone GEF. PMID:24413168 showed that
  S. cerevisiae Mon1-Ccz1 activity requires longin-domain residues in both
  subunits, and PMID:26657788 showed in Fusarium that FgMon1 interacts with
  FgRab7 and that constitutively active FgRab7 can rescue the mon1 mutant.
- The opisthokont PAINT node `PTN000315023` asserts Mon1-Ccz1 complex
  membership. S. cerevisiae, metazoan, and worm seeds support this as a
  conserved complex, but filamentous-fungal Ccz1 partners are diverged. Son and
  Park reported in 2019 that standard searches did not find Ccz1 orthologs in
  Aspergillus, Fusarium, or Penicillium; the PAINT row is still defensible for
  Mon1, but a direct A. nidulans MonA-Ccz1/Rab7 assay remains the main open
  experiment.
- S. cerevisiae MON1 carries `GO:0016236 macroautophagy` by IMP, and the
  Fusarium FgMon1 paper directly reports impaired autophagosome-vacuole fusion.
  I used the specific macroautophagy child rather than adding parent
  `GO:0006914 autophagy`, which the yeast MON1 review already treats as too
  general beside more specific autophagy-route terms.

## Annotation decisions

- `GO:0000329 fungal-type vacuole membrane`: ACCEPT. PAINT places this at the
  fungal Mon1 node, and A. nidulans MonA is directly required for normal vacuole
  morphology.
- `GO:0005085 guanyl-nucleotide exchange factor activity`: ACCEPT with
  `contributes_to`. Mon1 contributes to the Mon1-Ccz1 Rab7/Ypt7 GEF module and
  should not receive an unqualified GEF activity row.
- `GO:0005774 vacuolar membrane`: MODIFY to `GO:0000329 fungal-type vacuole
  membrane`.
- `GO:0006623 protein targeting to vacuole` by PAINT and InterPro: ACCEPT.
  InterPro IPR004353 reaches the same Mon1 family and same core process as the
  fungal PAINT row.
- `GO:0016192 vesicle-mediated transport`: MODIFY to
  `GO:0032511 late endosome to vacuole transport via multivesicular body
  sorting pathway`.
- `GO:0032585 multivesicular body membrane`: KEEP_AS_NON_CORE. The inferred
  MVB/prevacuolar site matches Mon1-Ccz1 endosomal recruitment, but the fungal
  vacuole membrane is the better core localization.
- `GO:0035658 Mon1-Ccz1 complex`: ACCEPT with the caveat that direct
  filamentous-fungal complex formation remains untested.
- Add `GO:0016236 macroautophagy` as a conservative NEW row because
  Mon1-Ccz1 executes Rab7/Ypt7-dependent autophagosome-vacuole fusion in yeast,
  and Fusarium FgMon1 has direct autophagy and Rab7 evidence.
