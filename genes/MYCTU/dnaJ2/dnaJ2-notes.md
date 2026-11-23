# MYCTU dnaJ2: manual annotation review

DnaJ2 is a J-domain cochaperone that assists DnaK-dependent protein folding. The two mycobacterial J proteins make distinct, partly overlapping contributions to DnaK activation and refolding; DnaJ2 activates DnaK more efficiently at substoichiometric concentrations. DnaJ2 also inhibits the reported RNase and beta-lactamase activities of RNase J/Rv2752c in a purified-protein study.

## Identity and evidence scope

See [identity-and-assay-scope.md](../dnaK/dnaK-source-analysis/identity-and-assay-scope.md) via the sibling dnaK source analysis; canonical reference: `file:genes/MYCTU/dnaK/dnaK-source-analysis/identity-and-assay-scope.md`. The H37Rv J-protein assignment uses species-level biochemical inference, not a verified identity of the 2016 donor construct. Native and heterologous observations are distinguished in the row reasons.

## Research and decisions

The normal Falcon research provider was attempted once and failed with HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supports the annotations below. Original seeded annotation payloads and raw UniProt/GOA files are frozen in the ignored baseline.

- Assists client-directed folding and refolding by the DnaK chaperone machinery.
  PMID:27872278: “ClpB alone could not restore luciferase activity, but DnaK and cofactors gave a time-dependent increase in luciferase reactivation that was enhanced when ClpB was added to the reaction.”
- Binds DnaK and stimulates its ATPase cycle; this H37Rv assignment is inferred from the characterized M. tuberculosis J protein, with the exact cloned donor sequence unresolved.
  PMID:27872278: “DnaJ2 was also able to stimulate DnaK in the absence of GrpE”

Action counts: {"ACCEPT": 7, "MARK_AS_OVER_ANNOTATED": 1, "MODIFY": 2, "NEW": 2}.

ATP binding is not inferred from activation of the DnaK ATPase. The Mtb electronic ATP-binding claim is marked over-annotated without asserting absolute absence of affinity.


## 2026-11-06 — PR6125 evidence/action follow-up

3: distinguish cytoplasmic localization from purified-protein functional assays; 5: distinguish bounded NOT-regulation from indirect overexpression effects; 8: keep biological core descriptions separate from construct provenance; 11: structured InterPro ATP-binding source concern; 4: retain directly reported RNase inhibition with explicit source limits. Original machine rows and source bytes were frozen before edits. Published PMID and raw-source evidence remain separate from native target-specific experiments. Core location changes, where made, retain cytoplasm when finer cytosol resolution was not independently supported. Physiological uncertainty is not treated as automatic disproof of a directly measured molecular activity.

The PR-authored RNase-inhibitor proposal remains supported by the explicit PMID:21568871 binding-and-inhibition result and its curated UniProt experimental FUNCTION statement. Normal force-fetch and publisher retrieval still yielded only abstract/subscription preview, so assay concentrations, detailed controls and native physiological role are not claimed verified. Both reported RNase and beta-lactamase inhibition are acknowledged; no additional proposal is manufactured solely for symmetry.
