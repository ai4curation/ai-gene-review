# THET8 dnaK: manual annotation review

DnaK is an Hsp70 chaperone that couples ATP binding and hydrolysis to binding and release of nonnative protein clients. DnaJ cochaperones assist client handling and GrpE promotes nucleotide exchange, enabling repeated folding cycles. In Thermus, productive folding is supported by DnaJ2 and GrpE; DafA can trap an inhibited assembly through client-pocket and J-domain interactions.

## Identity and evidence scope

See [identity-and-assay-scope.md](dnaK-source-analysis/identity-and-assay-scope.md) via the sibling dnaK source analysis; canonical reference: `file:genes/THET8/dnaK/dnaK-source-analysis/identity-and-assay-scope.md`. Native and heterologous observations are distinguished in the row reasons.

## Research and decisions

The normal Falcon research provider was attempted once and failed with HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supports the annotations below. Original seeded annotation payloads and raw UniProt/GOA files are frozen in the ignored baseline.

- Couples nucleotide cycling to folding and refolding of nonnative protein clients with its J-protein and GrpE partners.
  PMID:31604242: “We examined the role of ttHsp40 in the refolding of chemically denatured luciferase by the Hsp70/Hsp40/NEF”

Action counts: {"ACCEPT": 3, "MODIFY": 1, "NEW": 1}.



## 2026-11-06 — PR6125 evidence/action follow-up

3: distinguish cytoplasmic localization from purified-protein functional assays. Original machine rows and source bytes were frozen before edits. Published PMID and raw-source evidence remain separate from native target-specific experiments. Core location changes, where made, retain cytoplasm when finer cytosol resolution was not independently supported. Physiological uncertainty is not treated as automatic disproof of a directly measured molecular activity.
