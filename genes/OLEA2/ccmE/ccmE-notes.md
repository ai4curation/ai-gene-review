# ccmE manual review

CcmE is the membrane-anchored, periplasm-facing heme chaperone of System I* in Oleidesulfovibrio alaskensis G20. It forms a transient covalent heme bond through Cys127 and delivers heme for cytochrome c maturation. Its cysteine-bearing binding site differs from the histidine-bearing canonical CcmE and is not functionally interchangeable with the E. coli protein.

Identity: {'gene': 'ccmE', 'accession': 'Q311W9', 'locus': 'Dde_1478', 'taxon': 'NCBITaxon:207559', 'species_code': 'OLEA2', 'length': 137, 'sequence_sha256': '1d0c160798c881c42363ec53f239da4579a43b743deb05c47f04f232115d27a8', 'genome': 'CP000112', 'cds_zero_based_half_open': '[1498279:1498693](-)', 'ena_protein': 'ABB38277.1', 'ena_uniprot_translation_identical': True, 'family_crossreferences': [{'database': 'InterPro', 'id': 'IPR004329', 'properties': [{'key': 'EntryName', 'value': 'CcmE'}]}, {'database': 'InterPro', 'id': 'IPR036127', 'properties': [{'key': 'EntryName', 'value': 'CcmE-like_sf'}]}, {'database': 'InterPro', 'id': 'IPR012340', 'properties': [{'key': 'EntryName', 'value': 'NA-bd_OB-fold'}]}, {'database': 'PANTHER', 'id': 'PTHR34128', 'properties': [{'key': 'EntryName', 'value': 'CYTOCHROME C-TYPE BIOGENESIS PROTEIN CCME HOMOLOG, MITOCHONDRIAL'}, {'key': 'MatchStatus', 'value': '1'}]}, {'database': 'PANTHER', 'id': 'PTHR34128:SF2', 'properties': [{'key': 'EntryName', 'value': 'CYTOCHROME C-TYPE BIOGENESIS PROTEIN CCME HOMOLOG, MITOCHONDRIAL'}, {'key': 'MatchStatus', 'value': '1'}]}]}

Covalently carries heme through Cys127 and participates in its delivery to apocytochrome c; membrane anchoring places the heme-handling domain on the periplasmic side.

Primary interpretation and construct limitations: see [G20 source analysis](../ccmE/ccmE-source-analysis/primary-evidence.md) and identity-provenance.yaml. PMID20466730 establishes the heterologous operon; PMID24044352 tests individual residue substitutions. No native G20 knockout or flux claim is made. The2011 detection-limit correction was inspected.

Falcon was genuinely attempted with the normal default provider and failed authentication (403); the corresponding ignored-cache log records the failure. No provider report was fabricated. All seeded row payloads and raw files are preserved.

What chemistry breaks the Cys127-heme bond during productive transfer, and which native reductants participate?

Additional evidence checks: exact primary-source excerpts, corrected detection limits, current GO parent relationships and same-role process comparators are preserved in the shared source analysis. CcmI has no direct binding MF assignment.


## PR6121 round-1 evidence correction (2026-11-06)

- GO:0005886 ACCEPT: Target membrane-anchor predictions support the plasma-membrane assignment.
- GO:0016020 MODIFY: Target membrane-anchor predictions support the plasma-membrane assignment.
- GO:0017003 ACCEPT: CcmE forms its own covalent Cys127-heme intermediate before downstream transfer.

Current GO definitions were checked against the official QuickGO API. All original annotation payloads, including authored NEW rows, are preserved. Primary scope and construct limits remain explicit; no raw UniProt/GOA, provider report or publication cache was edited. Scoped comparative proof is recorded in the round-1 audit.
