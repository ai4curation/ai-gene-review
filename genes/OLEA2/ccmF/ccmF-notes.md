# ccmF manual review

CcmF is a polytopic membrane component of the System I* cytochrome c maturation apparatus in Oleidesulfovibrio alaskensis G20. It handles heme downstream of CcmE and contributes to its covalent attachment to apocytochrome c. Conserved histidines are required in the reconstructed system, whereas substitution at the proposed quinone-binding motif retains activity. The tested system functions without CcmH; its electron donor and isolated ligation mechanism remain unresolved.

Identity: {'gene': 'ccmF', 'accession': 'Q311X0', 'locus': 'Dde_1477', 'taxon': 'NCBITaxon:207559', 'species_code': 'OLEA2', 'length': 641, 'sequence_sha256': '282c85fc8a44f3a79ed4af41087309db8c37f4d7ee50aea5d08ddb4f7306ff23', 'genome': 'CP000112', 'cds_zero_based_half_open': '[1496226:1498152](-)', 'ena_protein': 'ABB38276.1', 'ena_uniprot_translation_identical': True, 'family_crossreferences': [{'database': 'InterPro', 'id': 'IPR032523', 'properties': [{'key': 'EntryName', 'value': 'CcmF_C'}]}, {'database': 'InterPro', 'id': 'IPR002541', 'properties': [{'key': 'EntryName', 'value': 'Cyt_c_assembly'}]}, {'database': 'InterPro', 'id': 'IPR003567', 'properties': [{'key': 'EntryName', 'value': 'Cyt_c_biogenesis'}]}, {'database': 'PANTHER', 'id': 'PTHR43653', 'properties': [{'key': 'EntryName', 'value': 'CYTOCHROME C ASSEMBLY PROTEIN-RELATED'}, {'key': 'MatchStatus', 'value': '1'}]}, {'database': 'PANTHER', 'id': 'PTHR43653:SF1', 'properties': [{'key': 'EntryName', 'value': 'CYTOCHROME C-TYPE BIOGENESIS PROTEIN CCMF'}, {'key': 'MatchStatus', 'value': '1'}]}]}

Heme-handling membrane component that contributes to the terminal heme-attachment machinery of System I*, without an obligatory CcmH partner in the tested reconstruction.

Primary interpretation and construct limitations: see [G20 source analysis](../ccmE/ccmE-source-analysis/primary-evidence.md) and identity-provenance.yaml. PMID20466730 establishes the heterologous operon; PMID24044352 tests individual residue substitutions. No native G20 knockout or flux claim is made. The2011 detection-limit correction was inspected.

Falcon was genuinely attempted with the normal default provider and failed authentication (403); the corresponding ignored-cache log records the failure. No provider report was fabricated. All seeded row payloads and raw files are preserved.

Which electron donor and partner contacts support isolated System I* heme ligation without CcmH?

Additional evidence checks: exact primary-source excerpts, corrected detection limits, current GO parent relationships and same-role process comparators are preserved in the shared source analysis. CcmI has no direct binding MF assignment.


## PR6121 round-1 evidence correction (2026-11-06)

- GO:0015886 ACCEPT: System I* CcmF participates in heme delivery at the terminal attachment machinery.
- GO:0015232 MARK_AS_OVER_ANNOTATED: G20 CcmF heme handling does not establish a membrane-crossing transporter.

Current GO definitions were checked against the official QuickGO API. All original annotation payloads, including authored NEW rows, are preserved. Primary scope and construct limits remain explicit; no raw UniProt/GOA, provider report or publication cache was edited. Scoped comparative proof is recorded in the round-1 audit.


## 2026-11-06: PR6121 round-2 location-evidence audit

Replaced chemistry-only support on location rows 2 and added matching locational evidence to location-bearing cores. The current G20 reference protein has 14 Phobius-predicted transmembrane helices. These target-specific features support membrane insertion; conserved CcmF architecture and characterized ortholog topology support assignment to the bacterial inner membrane. This is a topology/ortholog inference, not a direct native G20 localization experiment or an exact experimental map of every predicted helix. The evidence does not establish periplasmic orientation from transmembrane segments alone. ARBA-only location prose and heme-chemistry phenotypes are not used as location evidence. Annotation actions and every original non-review payload, including historical NEW rows, remain unchanged. Full prior reviews and source hashes were frozen before editing in the round2-location cache; the durable preservation proof records comparison to published head 044f9278bcea364ad66bccc221fdfc78132ba4eb.
