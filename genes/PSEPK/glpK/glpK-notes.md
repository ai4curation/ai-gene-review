# glpK (PP_1075, Q88NX8) notes

## 2026-11-03 review completion (Claude (AI-assisted))

- Deep research: `glpK-deep-research-asta.md` (Asta retrieval) is present, but
  all 20 retrieved papers are off-target (UniProt and gene-symbol mapping
  tools, network pharmacology, unrelated organisms). None mentions P. putida
  glycerol kinase, so the file supports no annotation. It is listed in the
  references with relevance NONE, and the validator's "no deep research cited"
  warning is left in place deliberately.
- Organism-specific evidence: Nikel et al. 2015 (PMID:25827416, abstract only)
  places glpK in the GlpR-repressed glpFKRD cluster. In that study, "altering
  G3P formation (by overexpressing glpK, encoding glycerol kinase) abolished
  the bimodal glpD expression" [PMID:25827416]. No biochemical assay of KT2440
  GlpK was found. The activity rests on the HAMAP MF_00186, IPR005999 and
  TIGR01311 family assignments and on the characterized E. coli ortholog
  P0A6F3, the ISS donor.
- Q88NX8 is not a leaf of the PTHR10196 PAINT tree (`just paint-losses`), so no
  IBA rows exist. TreeGrafter (PTN002230053) supplies glycerol metabolic
  process.
- Actions were aligned with ECOLI/glpK: carbohydrate metabolic process and
  glycerol metabolic process (TreeGrafter, ISS) now MODIFY to GO:0019563.
  Kinase activity and phosphotransferase activity, alcohol group as acceptor
  now MODIFY to GO:0004370. Glycerol-3-phosphate metabolic process stays
  KEEP_AS_NON_CORE. The glycerol kinase activity, ATP binding, cytosol and
  glycerol catabolic process rows are ACCEPT.
- No source defects were found.
- Open question: P. putida has no glucose PTS EIIA-Glc, so E. coli-style
  inducer exclusion cannot operate. Whether FBP inhibits this enzyme, as the
  HAMAP rule predicts, is untested.

## 2026-11-04 (PR #5936 review follow-up)

- GO:0006072 changed to MODIFY toward GO:0046167, as for the E. coli ortholog. PMID:25827416 full text is now cached (PMC XML).

## 2026-11-04 (PR #5936 second review round)

- GO:0006072 -> GO:0046167 reason now cites the PAINT GO:0046167 IBD on the eukaryotic glycerol kinase node PTN000023394 as corroboration (not propagated to this bacterial protein).


## 2026-11-07 comparative glycerol audit

Rechecked all 11 rows. Corrected the old claim that PMID25827416 does not assay the kinase: its full Methods and Results measure coupled GlpK activity in KT2440 cell extracts and a threefold increase after glpFK overexpression. This supports the target-strain catalytic assignment but supplies neither purified Q88NX8 kinetic constants nor direct E. coli-type FBP/EIIA-Glc regulation. The latter is stated only where supported as homology prediction. Existing Asta retrieval is genuine but off-topic; no provider file was edited.

Existing genuine provider research was inspected and preserved byte-for-byte; conclusions were checked against primary sources. All original ordered annotation payloads are preserved, with no new GO rows. Focused validation, source preservation, and helper-history results are recorded in analysis/module_audits/bacterial_glycerol_uptake_catabolism/existing-member-consultation/. COMPLETE denotes completed adjudication, including explicit unresolved claims.
