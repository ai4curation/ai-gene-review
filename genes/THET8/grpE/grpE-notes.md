# THET8 grpE: manual annotation review

GrpE is a soluble dimeric nucleotide-exchange factor for the Hsp70 chaperone DnaK. It binds DnaK and accelerates nucleotide release, allowing ATP rebinding and continuation of client folding cycles. Thermus GrpE efficiently stimulates nucleotide exchange even under conditions where DnaJ does not measurably stimulate DnaK ATP hydrolysis.

## Identity and evidence scope

See [identity-and-assay-scope.md](../dnaK/dnaK-source-analysis/identity-and-assay-scope.md) via the sibling dnaK source analysis; canonical reference: `file:genes/THET8/dnaK/dnaK-source-analysis/identity-and-assay-scope.md`. Native and heterologous observations are distinguished in the row reasons.

## Research and decisions

The normal Falcon research provider was attempted once and failed with HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supports the annotations below. Original seeded annotation payloads and raw UniProt/GOA files are frozen in the ignored baseline.

- Promotes adenyl-nucleotide exchange on DnaK and coordinates continuation of its client-folding cycle.
  PMID:11162122: “Kinetic experiments indicate that the maximal acceleration of nucleotide release by GrpE is 80,000-fold at a saturating GrpE concentration.”

Action counts: {"ACCEPT": 4, "MODIFY": 1}.



## 2026-11-06 — PR6125 evidence/action follow-up

7: align GrpE homodimerization with its core functional architecture; 3: distinguish cytoplasmic localization from purified-protein functional assays. Original machine rows and source bytes were frozen before edits. Published PMID and raw-source evidence remain separate from native target-specific experiments. Core location changes, where made, retain cytoplasm when finer cytosol resolution was not independently supported. Physiological uncertainty is not treated as automatic disproof of a directly measured molecular activity.
