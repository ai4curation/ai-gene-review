# PP_4348 curation notes

## GO term status verification

Checked the EMBL-EBI QuickGO API on 2026-07-19:

- `GO:0004121` returned `isObsolete: true` with the comment: "The reason for obsoletion is that this term is equivalent to GO:0047804 cysteine-S-conjugate beta-lyase activity."
- `GO:0047804` returned `isObsolete: false` and lists "cystathionine beta-lyase activity" as a related synonym.

API request: `https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0004121,GO%3A0047804`

## 2026-11-13 audit and promotion to COMPLETE
- QuickGO (live) still has the same 4 IEA rows. GO:0019346 is now obsolete (consider GO:0071269 / GO:0019344), so the
  ACCEPT was changed to MODIFY with GO:0071269.
- GO:0006520 was changed from MARK_AS_OVER_ANNOTATED to TOO_GENERAL (true but broad).
- References to the GOA file (never valid support) and to a non-existent GapMind cache path were removed.
- Alignment with E. coli MetC: about 30% identity, PP_4348 Lys186 = MetC Lys210 [file:PSEPK/PP_4348/PP_4348-bioinformatics/RESULTS.md].
  Both proteins are in PTHR43500:SF1.
- The fitness summary file has an empty phenotype table, and the live Fitness Browser was blocked by a bot challenge,
  so fitness is not used as evidence.
- Evidence ceiling: there is no KT2440 enzymology or genetics. Cystathionine beta-lyase activity was measured only in extracts of
  P. putida S-313 [PMID:10482527], and direct sulfhydrylation is the main methionine route there.
