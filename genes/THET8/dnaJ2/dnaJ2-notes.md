# THET8 dnaJ2: manual annotation review

DnaJ2 is a J-domain cochaperone that assists DnaK-dependent protein folding. The Thermus operon protein binds nonnative clients and participates in their transfer to DnaK. Its G/F region regulates J-domain accessibility, and DafA can block productive docking. Historical kinetic experiments did not detect autonomous stimulation of DnaK ATP hydrolysis under the tested conditions.

## Identity and evidence scope

See [identity-and-assay-scope.md](../dnaK/dnaK-source-analysis/identity-and-assay-scope.md) via the sibling dnaK source analysis; canonical reference: `file:genes/THET8/dnaK/dnaK-source-analysis/identity-and-assay-scope.md`. Native and heterologous observations are distinguished in the row reasons.

## Research and decisions

The normal Falcon research provider was attempted once and failed with HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supports the annotations below. Original seeded annotation payloads and raw UniProt/GOA files are frozen in the ignored baseline.

- Assists client-directed folding and refolding by the DnaK chaperone machinery.
  PMID:31604242: “We examined the role of ttHsp40 in the refolding of chemically denatured luciferase by the Hsp70/Hsp40/NEF”

Action counts: {"ACCEPT": 2, "MODIFY": 1, "NEW": 1}.

ATP binding is not inferred from activation of the DnaK ATPase. The Mtb electronic ATP-binding claim is marked over-annotated without asserting absolute absence of affinity. Thermus direct client handling is distinguished from unresolved unconditional ATPase stimulation.
