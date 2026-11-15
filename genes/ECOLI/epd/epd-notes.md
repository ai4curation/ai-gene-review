# epd review notes (E. coli K-12, P0A9B6)

Reviewed as the reference exemplar for step 1 of the DXP-dependent de novo PLP
module (`modules/pyridoxal_5_phosphate_biosynthesis.yaml`).

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record, the PTHR43148 PAINT
  file and the cached publications below.
- Literature checked: PMID:7751290, PMID:9182530 and PMID:9696782 (all
  abstract-only in the cache) and PMID:18304323 (cytosol proteome; Epd is not
  named in the parsed text, so the curator's IDA row is deferred to).

## Function

- Epd is an E4P dehydrogenase, not a second GAPDH. [PMID:7751290 "We found that
  the gapB-encoded enzyme is indeed an E4PDH and not a second GA3PDH"]
- Kinetics on purified enzyme: [PMID:7751290 "E4PDH had an apparent Km value
  for E4P [Kmapp(E4P)] of 0.96 mM, an apparent kcat catalytic constant for E4P
  [kcatapp(E4P)] of 200 s-1"]
- Its product feeds PdxB. [PMID:7751290 "we showed that 4-phosphoerythronate is
  a likely substrate for the 2-hydroxy-acid dehydrogenase encoded by the pdxB
  gene."]
- GAPDH side activity is noise-level. [PMID:9182530 "The rate of oxidation of
  glyceraldehyde 3-phosphate is 0.12 s-1 and is hydride transfer limiting, at
  least 2000-fold less efficient compared with that of erythrose 4-phosphate."]
- Genetics. [PMID:9696782 "gapA epd double mutants lacking the glyceraldehyde
  3-phosphate and E4P dehydrogenases are auxotrophic for pyridoxine."]

## Curation decisions

- GO:0004365 GAPDH activity (IBA from PTN001652504 and IDA from PMID:9182530):
  REMOVE under the promiscuous-noise tier of `projects/ENZYME_SPECIFICITY.md`:
  dedicated GapA exists, the activity is >=2000-fold below the E4P activity,
  Epd is in a distinct subfamily (PTHR43148:SF3; HAMAP MF_01640; TIGR01532),
  and no in vivo GAPDH role is known. The assay is not doubted. A PANTHER
  source defect (CHECK) records the over-propagation into the Epd clade. The
  coordinator's PTHR43148 family review assesses this node as NEEDS_PRUNING for
  SF3, in agreement.
- GO:0006006 glucose metabolic process (IBA + IDA): REMOVE, consistent with the
  GAPDH verdict; no Epd evidence for glucose metabolism was found.
- GO:0042823 rows refined to GO:0036001 (de novo PLP), added as a NEW row.
- GO:0008615 pyridoxine biosynthetic process accepted: it is GO's term for the
  UniPathway pyridoxine 5'-phosphate branch (UPA00244); no PNP-specific GO term
  exists.
- Cytosol rows are KEEP_AS_NON_CORE, the same verdict used for cytosol on the
  P. putida PdxB review (TreeGrafter rereview 2026-09-24) and across the
  Epd/PdxB/SerC reviews; cytoplasm is refined to cytosol.
- NAD binding (IBA/IDA/IEA) KEEP_AS_NON_CORE.
