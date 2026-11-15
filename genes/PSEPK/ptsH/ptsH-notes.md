# ptsH (Pseudomonas putida KT2440) notes

## Provenance

- Re-reviewed while completing the bacterial nitrogen-regulatory PTS module
  (modules/bacterial_nitrogen_regulatory_pts.yaml). No new deep-research provider
  report was generated: no provider API key is configured in this session.
- Primary evidence: PMID:18296519 (full text; in vivo relay order PEP to PtsP to
  PtsO/NPr to PtsN, and FruB cross-talk), PMID:17416664, PMID:26224366 and
  PMID:21236318 (abstracts).

## Decisions in this pass

- Sugar-PTS process and carbohydrate phosphotransferase rows remain removed, now with
  quoted support ("comprise a branch of the system unrelated to sugar traffic") and
  source_defects naming the InterPro2GO / UniRule mappings.
- Correct-but-general MF rows (transferase, kinase, phosphorus-group transferase) are
  MODIFY to the specific activity rather than KEEP_AS_NON_CORE.
- For NPr (PP_0948) the phosphocarrier step is captured with GO:0016775
  (phosphotransferase activity, nitrogenous group as acceptor), matching the E. coli
  NPr review (genes/ECOLI/ptsO).
