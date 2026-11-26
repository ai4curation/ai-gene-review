# ccmB manual review

CcmB is a polytopic membrane subunit of the System I* cytochrome c maturation apparatus in Oleidesulfovibrio alaskensis G20. Its conserved CcmB architecture supports a role coupling the CcmA ATPase to membrane heme-handling components. The G20 operon supports heterologous cytochrome maturation, but CcmB-specific transport chemistry has not been demonstrated.

Identity: {'gene': 'ccmB', 'accession': 'Q311X2', 'locus': 'Dde_1475', 'taxon': 'NCBITaxon:207559', 'species_code': 'OLEA2', 'length': 225, 'sequence_sha256': 'a66bc79eef3be957752e1e973177225c29d627ba819aa9e87c87e85f0bef3efb', 'genome': 'CP000112', 'cds_zero_based_half_open': '[1494918:1495596](-)', 'ena_protein': 'ABB38274.1', 'ena_uniprot_translation_identical': True, 'family_crossreferences': [{'database': 'InterPro', 'id': 'IPR003544', 'properties': [{'key': 'EntryName', 'value': 'Cyt_c_biogenesis_CcmB'}]}]}

Membrane coupling component of the ATP-dependent heme-handling apparatus; the individual coupling assignment is inferred from CcmB family architecture and the functional operon.

Primary interpretation and construct limitations: see [G20 source analysis](../ccmE/ccmE-source-analysis/primary-evidence.md) and identity-provenance.yaml. PMID20466730 establishes the heterologous operon; PMID24044352 tests individual residue substitutions. No native G20 knockout or flux claim is made. The2011 detection-limit correction was inspected.

Falcon was genuinely attempted with the normal default provider and failed authentication (403); the corresponding ignored-cache log records the failure. No provider report was fabricated. All seeded row payloads and raw files are preserved.

Does G20 CcmB transmit ATP-driven conformational change to CcmC, and does it translocate any substrate?

Additional evidence checks: exact primary-source excerpts, corrected detection limits, current GO parent relationships and same-role process comparators are preserved in the shared source analysis. CcmI has no direct binding MF assignment.


## PR6121 round-1 evidence correction (2026-11-06)

- GO:0015232 UNDECIDED: A transmembrane heme-transport activity is unresolved for G20 CcmB.

Current GO definitions were checked against the official QuickGO API. All original annotation payloads, including authored NEW rows, are preserved. Primary scope and construct limits remain explicit; no raw UniProt/GOA, provider report or publication cache was edited. Scoped comparative proof is recorded in the round-1 audit.


## 2026-11-06: PR6121 round-2 location-evidence audit

Replaced chemistry-only support on location rows 2 and added matching locational evidence to location-bearing cores. The current G20 reference protein has 6 Phobius-predicted transmembrane helices. These target-specific features support membrane insertion; conserved CcmB architecture and characterized ortholog topology support assignment to the bacterial inner membrane. This is a topology/ortholog inference, not a direct native G20 localization experiment or an exact experimental map of every predicted helix. The evidence does not establish periplasmic orientation from transmembrane segments alone. ARBA-only location prose and heme-chemistry phenotypes are not used as location evidence. Annotation actions and every original non-review payload, including historical NEW rows, remain unchanged. Full prior reviews and source hashes were frozen before editing in the round2-location cache; the durable preservation proof records comparison to published head 044f9278bcea364ad66bccc221fdfc78132ba4eb.
