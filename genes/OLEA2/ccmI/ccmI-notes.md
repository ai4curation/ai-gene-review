# ccmI manual review

CcmI is a membrane-anchored tetratricopeptide-repeat protein associated with the System I* cytochrome c maturation apparatus in Oleidesulfovibrio alaskensis G20. It enhances maturation efficiency in a heterologous reconstruction, consistent with an accessory assembly or substrate-handling role. Deletion retains approximately20% of cytochrome c550 production, so CcmI is not essential under those assay conditions.

Identity: {'gene': 'ccmI', 'accession': 'Q311X4', 'locus': 'Dde_1473', 'taxon': 'NCBITaxon:207559', 'species_code': 'OLEA2', 'length': 204, 'sequence_sha256': 'f09895224790784147e515f73ff4c6b54ed24ad9d5eceb0c35260757aadb8571', 'genome': 'CP000112', 'cds_zero_based_half_open': '[1493416:1494031](-)', 'ena_protein': 'ABB38272.1', 'ena_uniprot_translation_identical': True, 'family_crossreferences': [{'database': 'InterPro', 'id': 'IPR011990', 'properties': [{'key': 'EntryName', 'value': 'TPR-like_helical_dom_sf'}]}, {'database': 'InterPro', 'id': 'IPR019734', 'properties': [{'key': 'EntryName', 'value': 'TPR_rpt'}]}, {'database': 'PANTHER', 'id': 'PTHR12558', 'properties': [{'key': 'EntryName', 'value': 'CELL DIVISION CYCLE 16,23,27'}, {'key': 'MatchStatus', 'value': '1'}]}, {'database': 'PANTHER', 'id': 'PTHR12558:SF13', 'properties': [{'key': 'EntryName', 'value': 'CELL DIVISION CYCLE PROTEIN 27 HOMOLOG'}, {'key': 'MatchStatus', 'value': '1'}]}]}

Accessory membrane-associated TPR component supporting efficient cytochrome maturation; a substrate-binding or assembly role is inferred, while direct G20 binding partners and native essentiality remain unestablished.

Primary interpretation and construct limitations: see [G20 source analysis](../ccmE/ccmE-source-analysis/primary-evidence.md) and identity-provenance.yaml. PMID20466730 establishes the heterologous operon; PMID24044352 tests individual residue substitutions. No native G20 knockout or flux claim is made. The2011 detection-limit correction was inspected.

Falcon was genuinely attempted with the normal default provider and failed authentication (403); the corresponding ignored-cache log records the failure. No provider report was fabricated. All seeded row payloads and raw files are preserved.

Does CcmI bind G20 apocytochromes directly, and how do substrate identity and growth conditions affect its contribution?

Additional evidence checks: exact primary-source excerpts, corrected detection limits, current GO parent relationships and same-role process comparators are preserved in the shared source analysis. CcmI has no direct binding MF assignment.


## 2026-11-06: PR6121 round-2 core location evidence

Added explicit membrane-anchor and comparative topology evidence to the location-bearing core, previously supported only by maturation phenotypes. The target Phobius membrane anchor and TPR architecture support membrane association, with inner-membrane context inferred from the G20 maturation cassette and characterized CcmI proteins. Rhodobacter CcmI has two membrane helices whereas this target has one predicted helix; no identical topology, direct native G20 localization or target periplasmic orientation is asserted from this comparison. All annotation payloads and actions are unchanged. Pre-edit text is frozen against published head044f9278 in round2-location/additional-unchanged-records.json.
