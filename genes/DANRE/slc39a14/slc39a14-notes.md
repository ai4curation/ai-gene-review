# slc39a14 (Danio rerio) review notes


## Batch 05 curation notes
- Core interpretation: slc39a14 encodes ZIP14, a broad-scope divalent metal cation transporter that imports zinc, manganese, and non-transferrin-bound iron, likely as a metal:bicarbonate symporter, at plasma and endomembrane locations. Cadmium and signaling-response annotations are retained as non-core context relative to the core metal-cation uptake function.
- Key UniProt support: Broad-scope metal ion transporter with a preference for zinc uptake.
- Existing GOA annotations were reviewed against this core role; broad, inferred, or downstream phenotype annotations were kept as non-core unless they overstate the direct function.

## Re-review 2026-09-29

Re-reviewed all 45 GOA rows against UniProt A0A0G2KQY6 (ZIP14) and the two cached papers; replaced the
templated "matches the synthesized core function" reasons and the FUNCTION-line-everywhere
supporting_text, pointing localization rows at the SUBCELLULAR LOCATION lines and activity rows at
the metal:bicarbonate CATALYTIC ACTIVITY reactions. Rewrote the description (removed the embedded
blank lines and the metal:bicarbonate colon-in-scalar issue).

- Core: metal:bicarbonate symport (GO:0140410 IBA, GO:0015296 ISS) and the metal-specific
  transporter activities GO:0005385 zinc (IBA/ISS/Feeney), GO:0005384 manganese (ISS x2, one
  [Q15043-1] was PENDING -> ACCEPT), GO:0005381 iron (ISS) all ACCEPT; import processes GO:0071578,
  GO:0071421, GO:0034755, GO:0033212, GO:0006829, GO:0098739, GO:0071577 ACCEPT.
- Strongest zebrafish evidence: GO:0055071 manganese ion homeostasis (IMP, PMID:27231142)
  [PMID:27231142 "This is further corroborated in zebrafish carrying CRISPR-induced mutations in
  the slc39a14 orthologue which also show Mn dyshomeostasis while other metals remain unaffected."]
  and GO:0005886 plasma membrane (IDA) [PMID:27231142 "Comparable subcellular localization was seen
  when C-terminally eGFP-tagged human SLC39A14 was expressed in zebrafish embryos."] - both ACCEPT.
- Re-adjudicated the three MARK_AS_OVER_ANNOTATED rows (mouse-ortholog ISS): GO:0032869 cellular
  response to insulin, GO:0071333 cellular response to glucose, GO:0045745 positive regulation of
  GPCR signaling -> all changed to KEEP_AS_NON_CORE. Rationale: these are genuine mammalian
  experimental transfers (so not over-annotation to dismiss) describing indirect, zinc-flux-mediated
  physiological contexts, with no zebrafish support and no step of the process executed by ZIP14.
- Endomembrane/polarized-epithelium locations (apical, basolateral, early/late endosome, lysosome;
  IEA + ISS from human Q15043) KEEP_AS_NON_CORE (ortholog-inferred pools, no zebrafish data).
  Cd transport activity/process and bicarbonate/anion co-transport terms KEEP_AS_NON_CORE
  (non-physiological substrate; mechanistically-coupled bicarbonate flux). Generic parents
  GO:0016020, GO:0046873, GO:0055085 KEEP_AS_NON_CORE; GO:0030001 metal ion transport ACCEPT.
- Description rewritten; core_functions and suggested questions/experiments updated.
- Validation: zero errors, zero warnings.
