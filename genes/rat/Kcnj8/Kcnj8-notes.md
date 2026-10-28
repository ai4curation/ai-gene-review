# Kcnj8 (rat) review notes

## Session 1 (initial review)

- fetch-gene resolved Q63664 (KCNJ8_RAT, RGD:2960, GeneID 25472); 93 GOA rows, most of
  them RGD ISO transfers of mouse Kcnj8 knockout phenotypes (acts_upstream_of_or_within).
- Literature summary in `Kcnj8-deep-research-manual.md` (no deep-research provider available).
- Core: Kir6.1 is the pore-forming subunit of the vascular (Kir6.1/SUR2B) KATP channel
  [PMID:34711681 "Vascular tone is dependent on smooth muscle KATP channels comprising
  pore-forming Kir6.1 and regulatory SUR2B subunits"]; KO abolishes pinacidil-induced
  VSMC K+ currents and vasodilation [PMID:11984590].
- PMID:20123112 (sulfonylurea receptor binding, RGD IPI): full text read. Kir6.1 is named
  only in the introduction; the co-IP is anti-Kir6.2 probed with anti-SUR2. Function is
  true for Kir6.1 (structure PMID:34711681; SUR1 complex PMID:17883401), so the row is
  accepted, with a PROBABLE source defect (reference supports Kcnj11, not Kcnj8).
- ARUK-UCL rows from PMID:28842488: GO:0019829 ATPase-coupled cation transporter activity
  and GO:0031004 potassium ion-transporting ATPase complex are mis-typed; Kir6.1 is a
  passive channel. MODIFY to GO:0015272 and GO:0008282.
- Mouse KO ISO process rows: kept as non-core where Kir6.1 channel activity plausibly
  contributes (vasodilation, blood pressure, heart rate, hypoxia/ischemia, glutamate
  release); developmental, immune and signalling rows marked over-annotated (indirect
  KO consequences).
- No NEW process terms proposed.
