# ccmD manual review

CcmD is a small single-pass membrane protein of the System I* cytochrome c maturation apparatus in Oleidesulfovibrio alaskensis G20. It belongs to an alternate CcmD family and supports the heme-handling assembly. Removing it from an otherwise active CcmI-deficient cassette eliminates detectable cytochrome c550 maturation in E. coli; its precise molecular action and native substrate dependence remain unresolved.

Identity: {'gene': 'ccmD', 'accession': 'F9XXF9', 'locus': 'Dde_4022', 'taxon': 'NCBITaxon:207559', 'species_code': 'OLEA2', 'length': 45, 'sequence_sha256': 'ac53bfc712e1d66fe581b47b42bc8490ae798660b99f3a05a2880b9004a906e4', 'genome': 'CP000112', 'cds_zero_based_half_open': '[1494023:1494161](-)', 'ena_protein': 'AEL79424.1', 'ena_uniprot_translation_identical': True, 'family_crossreferences': [{'database': 'InterPro', 'id': 'IPR030888', 'properties': [{'key': 'EntryName', 'value': 'Put_ccm'}]}, {'database': 'NCBIfam', 'id': 'TIGR04391', 'properties': [{'key': 'EntryName', 'value': 'CcmD_alt_fam'}, {'key': 'MatchStatus', 'value': '1'}]}]}

Small membrane component supporting heme handling in the maturation apparatus. Its biochemical role is inferred from alternate CcmD membership and the selective reconstruction defect; no standalone catalytic activity is assigned.

Primary interpretation and construct limitations: see [G20 source analysis](../ccmE/ccmE-source-analysis/primary-evidence.md) and identity-provenance.yaml. PMID20466730 establishes the heterologous operon; PMID24044352 tests individual residue substitutions. No native G20 knockout or flux claim is made. The2011 detection-limit correction was inspected.

Falcon was genuinely attempted with the normal default provider and failed authentication (403); the corresponding ignored-cache log records the failure. No provider report was fabricated. All seeded row payloads and raw files are preserved.

Which physical partners and conformational transitions explain the alternate CcmD requirement?

Additional evidence checks: exact primary-source excerpts, corrected detection limits, current GO parent relationships and same-role process comparators are preserved in the shared source analysis. CcmI has no direct binding MF assignment.
