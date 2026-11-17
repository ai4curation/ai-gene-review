# cysM (E. coli K-12, P16703) curation notes

## 2026-11-03 review (cysteine biosynthesis module promotion)

Deep research: no provider deep-research run was possible in this session (no
provider API keys). The review rests on the reviewed UniProt entry, the local
PTHR10314 PAINT table, and the cached publications listed below (all
abstract-only except the interactome papers).

- Core activity: purified OASS-B makes L-cysteine from O-acetyl-L-serine and
  sulfide [PMID:16546401 "O-Acetylserine sulfhydrylase-B (OASS-B, EC 2.5.1.47)
  is one of the two isozymes produced by Escherichia coli that catalyze the
  synthesis of L-cysteine from O-acetyl-L-serine and sulfide."].
- No cysteine synthase complex: [PMID:16546401 "OASS-B did not form a complex
  with E. coli serine acetyltransferase"].
- Thiosulfate route: UniProt curated function text [file:ECOLI/cysM/cysM-uniprot.txt
  "Cysteine synthase B can also use thiosulfate in place of sulfide to give
  cysteine thiosulfonate as a product."]. GO has no MF term for the
  O-acetylserine + thiosulfate reaction (EC 2.5.1.144); searched the GO
  labels for "sulfocysteine"/"sulfo-L-cysteine"/"thiosulfonate" and found only
  obsolete GO:0019345. Recorded as a proposed new term, not a core function,
  because no cited E. coli paper in the cache measures it.
- Desulfhydrase side activity [PMID:16000837 "three additional proteins having
  L-cysteine desulfhydrase activity were identified as O-acetylserine
  sulfhydrylase-A, O-acetylserine sulfhydrylase-B, and MalY protein"], with
  tryptophanase dominant; kept non-core.
- Fe-S assembly row (PMID:8663055) is an in vitro crude-extract reconstitution;
  CysM performs no step of cluster assembly (ISC/SUF cysteine desulfurases do
  in vivo), so MARK_AS_OVER_ANNOTATED.
- Bare protein binding rows (AccC partner, two interactome screens) removed
  under the protein-binding policy.
- Cytoplasm IBA refined to cytosol (soluble homodimer; sibling CysK cytosolic
  by IDA), consistent with the sibling reviews in the module.
- PANTHER: PTHR10314:SF162 (CYSTEINE SYNTHASE B) with P. aeruginosa and
  Salmonella CysM; P16703 is the seed of the CysM-type node PTN008497439.

## 2026-11-03 PR #5929 review round

- Cytoplasm -> cytosol MODIFY reason now states that the refinement is an inference from solubility plus the PAINT node, not a localization measurement.


## Comparative cysteine-route audit (2026-11-06)

Retained all fifteen original row payloads and decisions, including true secondary cysteine degradation and the supported sulfide-dependent synthase activity. Corrected the Fe-S rationale: CysM does catalytically mobilize sulfur in the crude-extract reconstitution (PMID8663055); the concern is unproven physiological Fe-S assembly specialization, not an absence of chemical participation. The desulfhydrase branch is not described as literal reversal of the net OAS+sulfide reaction. PMID16546401 supports failure to form a CysE complex. Thiosulfate yields S-sulfocysteine, and conversion to cysteine requires a separate reaction.

Default Falcon research was attempted normally with --provider falcon and failed with HTTP403. No provider report was fabricated; this section records manual review.

Original GOA payloads, raw UniProt/GOA files and inherited authored proposals are preserved. Current GO checks distinguish the active cysteine synthase MF from obsolete route-specific BP terms GO:0006535 and GO:0019345. Focused gene and helper-history validations are recorded in the audit manifest.

The whole-gene core now separately represents S-sulfocysteine synthase using the same proposed MF as PAO1. Evidence is curated P16703 reaction text plus BW25113/pDES branch genetics (PMID:22607201), not a fabricated purified E.coli CysM thiosulfate assay. That paper directly assays downstream reductases. PMID:28756590 remains abstract-only and reports slow ΔcysM growth on thiosulfate; the branch is not universally necessary. No annotation row was added for the NTR core.


## 2026-11-06 PR #6120 round-1 follow-up

Merged the two chemically identical S-sulfo-L-cysteine synthase proposals into one. The fuller mechanistic justification is retained. The support union retains the curated target reaction and PMID22607201; two differently wrapped copies of the same UniProt sentence count as one evidence item. No annotation row was removed or changed.
