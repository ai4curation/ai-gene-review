# MYCTU dnaJ1: manual annotation review

DnaJ1 is a J-domain cochaperone that assists DnaK-dependent protein folding. The two mycobacterial J proteins make distinct, partly overlapping contributions to DnaK activation and refolding; DnaJ2 activates DnaK more efficiently at substoichiometric concentrations.

## Identity and evidence scope

See [identity-and-assay-scope.md](../dnaK/dnaK-source-analysis/identity-and-assay-scope.md) via the sibling dnaK source analysis; canonical reference: `file:genes/MYCTU/dnaK/dnaK-source-analysis/identity-and-assay-scope.md`. The H37Rv J-protein assignment uses species-level biochemical inference, not a verified identity of the 2016 donor construct. Native and heterologous observations are distinguished in the row reasons.

## Research and decisions

The normal Falcon research provider was attempted once and failed with HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supports the annotations below. Original seeded annotation payloads and raw UniProt/GOA files are frozen in the ignored baseline.

- Assists client-directed folding and refolding by the DnaK chaperone machinery.
  PMID:27872278: “ClpB alone could not restore luciferase activity, but DnaK and cofactors gave a time-dependent increase in luciferase reactivation that was enhanced when ClpB was added to the reaction.”
- Binds DnaK and stimulates its ATPase cycle; this H37Rv assignment is inferred from the characterized M. tuberculosis J protein, with the exact cloned donor sequence unresolved.
  PMID:27872278: “significant activation was only observed at equimolar DnaJ1 and DnaK regardless of the presence of DnaJ2 or GrpE”

Action counts: {"ACCEPT": 7, "MARK_AS_OVER_ANNOTATED": 1, "MODIFY": 2, "NEW": 1, "UNDECIDED": 1}.

ATP binding is not inferred from activation of the DnaK ATPase. The Mtb electronic ATP-binding claim is marked over-annotated without asserting absolute absence of affinity.
