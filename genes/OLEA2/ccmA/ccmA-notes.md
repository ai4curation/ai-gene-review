# ccmA manual review

CcmA is the cytoplasmic ATPase subunit associated with the System I* membrane apparatus of Oleidesulfovibrio alaskensis G20. ATP-dependent conformational work promotes heme delivery from CcmC toward CcmE and subsequent cytochrome maturation. Walker-A substitution impairs CcmE loading and abolishes detectable mature cytochrome in the reconstructed system, consistent with a requirement before or during covalent CcmE loading.

Identity: {'gene': 'ccmA', 'accession': 'Q311X1', 'locus': 'Dde_1476', 'taxon': 'NCBITaxon:207559', 'species_code': 'OLEA2', 'length': 215, 'sequence_sha256': 'b9dc068673772fbeecd94c44b8da6f4817cba3a0f2fef683af08dbc4cc08797a', 'genome': 'CP000112', 'cds_zero_based_half_open': '[1495589:1496237](-)', 'ena_protein': 'ABB38275.1', 'ena_uniprot_translation_identical': True, 'family_crossreferences': [{'database': 'InterPro', 'id': 'IPR003593', 'properties': [{'key': 'EntryName', 'value': 'AAA+_ATPase'}]}, {'database': 'InterPro', 'id': 'IPR003439', 'properties': [{'key': 'EntryName', 'value': 'ABC_transporter-like_ATP-bd'}]}, {'database': 'InterPro', 'id': 'IPR051782', 'properties': [{'key': 'EntryName', 'value': 'ABC_Transporter_VariousFunc'}]}, {'database': 'InterPro', 'id': 'IPR027417', 'properties': [{'key': 'EntryName', 'value': 'P-loop_NTPase'}]}, {'database': 'PANTHER', 'id': 'PTHR42939', 'properties': [{'key': 'EntryName', 'value': 'ABC TRANSPORTER ATP-BINDING PROTEIN ALBC-RELATED'}, {'key': 'MatchStatus', 'value': '1'}]}, {'database': 'PANTHER', 'id': 'PTHR42939:SF1', 'properties': [{'key': 'EntryName', 'value': 'ABC TRANSPORTER ATP-BINDING PROTEIN ALBC-RELATED'}, {'key': 'MatchStatus', 'value': '1'}]}]}

ATP-hydrolyzing subunit supplying conformational work for heme trafficking; the G20-specific functional test is Walker-A mutagenesis in a heterologous operon, not a purified ATPase-rate assay.

Primary interpretation and construct limitations: see [G20 source analysis](../ccmE/ccmE-source-analysis/primary-evidence.md) and identity-provenance.yaml. PMID20466730 establishes the heterologous operon; PMID24044352 tests individual residue substitutions. No native G20 knockout or flux claim is made. The2011 detection-limit correction was inspected.

Falcon was genuinely attempted with the normal default provider and failed authentication (403); the corresponding ignored-cache log records the failure. No provider report was fabricated. All seeded row payloads and raw files are preserved.

What is the purified G20 ATPase rate, and at which heme-transfer transition is ATP hydrolyzed?

Additional evidence checks: exact primary-source excerpts, corrected detection limits, current GO parent relationships and same-role process comparators are preserved in the shared source analysis. CcmI has no direct binding MF assignment.
