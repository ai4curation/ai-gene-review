# ccmC manual review

CcmC is a membrane heme-handling protein in the System I* cytochrome c maturation apparatus of Oleidesulfovibrio alaskensis G20. It presents heme upstream of the cysteine-bearing CcmE chaperone. Conserved histidine substitutions in the experimental G20 operon disrupt heme loading and cytochrome maturation; the published mutant numbering differs from the current reference sequence by18 residues. Direct transmembrane heme transport by CcmC has not been established.

Identity: {'gene': 'ccmC', 'accession': 'Q311X3', 'locus': 'Dde_1474', 'taxon': 'NCBITaxon:207559', 'species_code': 'OLEA2', 'length': 230, 'sequence_sha256': 'dbe27419a3b59c2cb290adc697cdd35b1d1bcdd281ea7e9d3ce9b40a83bf1a93', 'genome': 'CP000112', 'cds_zero_based_half_open': '[1494171:1494864](-)', 'ena_protein': 'ABB38273.1', 'ena_uniprot_translation_identical': True, 'family_crossreferences': [{'database': 'InterPro', 'id': 'IPR003557', 'properties': [{'key': 'EntryName', 'value': 'Cyt_c_biogenesis_CcmC'}]}, {'database': 'InterPro', 'id': 'IPR045062', 'properties': [{'key': 'EntryName', 'value': 'Cyt_c_biogenesis_CcsA/CcmC'}]}, {'database': 'PANTHER', 'id': 'PTHR30071:SF1', 'properties': [{'key': 'EntryName', 'value': 'CYTOCHROME B_B6 PROTEIN-RELATED'}, {'key': 'MatchStatus', 'value': '1'}]}, {'database': 'PANTHER', 'id': 'PTHR30071', 'properties': [{'key': 'EntryName', 'value': 'HEME EXPORTER PROTEIN C'}, {'key': 'MatchStatus', 'value': '1'}]}]}

Binds and presents heme for CcmE loading. The exact current locus is established, but the experimental histidine numbering is not equated with reference residue numbers.

Primary interpretation and construct limitations: see [G20 source analysis](../ccmE/ccmE-source-analysis/primary-evidence.md) and identity-provenance.yaml. PMID20466730 establishes the heterologous operon; PMID24044352 tests individual residue substitutions. No native G20 knockout or flux claim is made. The2011 detection-limit correction was inspected.

Falcon was genuinely attempted with the normal default provider and failed authentication (403); the corresponding ignored-cache log records the failure. No provider report was fabricated. All seeded row payloads and raw files are preserved.

Why do experimental H68/H192 correspond to reference H50/H174; what sequence and start site does pDD86 encode?

Additional evidence checks: exact primary-source excerpts, corrected detection limits, current GO parent relationships and same-role process comparators are preserved in the shared source analysis. CcmI has no direct binding MF assignment.


## PR6121 round-1 evidence correction (2026-11-06)

- GO:0015232 UNDECIDED: G20 CcmC membrane-crossing activity is unresolved beyond its established heme-loading role.

Current GO definitions were checked against the official QuickGO API. All original annotation payloads, including authored NEW rows, are preserved. Primary scope and construct limits remain explicit; no raw UniProt/GOA, provider report or publication cache was edited. Scoped comparative proof is recorded in the round-1 audit.


## 2026-11-06: PR6121 round-2 location-evidence audit

Replaced chemistry-only support on location rows 0, 3 and added matching locational evidence to location-bearing cores. The current G20 reference protein has 6 Phobius-predicted transmembrane helices. These target-specific features support membrane insertion; conserved CcmC architecture and characterized ortholog topology support assignment to the bacterial inner membrane. This is a topology/ortholog inference, not a direct native G20 localization experiment or an exact experimental map of every predicted helix. The evidence does not establish periplasmic orientation from transmembrane segments alone. ARBA-only location prose and heme-chemistry phenotypes are not used as location evidence. Annotation actions and every original non-review payload, including historical NEW rows, remain unchanged. Full prior reviews and source hashes were frozen before editing in the round2-location cache; the durable preservation proof records comparison to published head 044f9278bcea364ad66bccc221fdfc78132ba4eb.
