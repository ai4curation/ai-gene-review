# Gss (rat glutathione synthetase, P46413) notes

## Re-review 2026-10-04

**GOA changes.** Five new seeded rows: glutathione synthase activity (GO:0004363) by IBA (PANTHER:PTN000122964) and by ISO from human GSS (UniProtKB:P48637, alongside the existing mouse Gss MGI:MGI:95852 row); cytosol (GO:0005829, is_active_in) and glutathione biosynthetic process (GO:0006750) by IBA; and a donor split of the peptide binding IPI (PMID:10964706) whose WITH is PubChem_Compound:193514 (gamma-glutamyl-2-aminobutyrate) rather than CHEBI:17515. No retired rows. Total 34 rows.

**Actions.**
- GO:0004363 IBA and ISO (human GSS): PENDING -> ACCEPT. Directly assayed on rat enzyme [PMID:10964706 "We report the detailed kinetic data for purified recombinant rat glutathione synthetase."].
- GO:0005829 IBA: PENDING -> ACCEPT (site of glutathione synthesis; the rat UniProt entry gives no subcellular location). Cytosol added to core_functions locations.
- GO:0006750 IBA: PENDING -> ACCEPT [UniProtKB:P46413 "PATHWAY: Sulfur metabolism; glutathione biosynthesis; glutathione from L-cysteine and L-glutamate: step 2/2."].
- GO:0042277 peptide binding IPI (gamma-Glu-Abu): PENDING -> KEEP_AS_NON_CORE, matching its sibling; substrate binding within the catalytic cycle [PMID:10964706 "The Lineweaver-Burk double reciprocal plot for gamma-glutamyl substrate binding revealed a departure from linearity indicating cooperative binding."].
- GO:0005654 nucleoplasm ISO (human GSS): REMOVE -> KEEP_AS_NON_CORE. The donor annotation is a Human Protein Atlas immunofluorescence IDA (GO_REF:0000052), the human GSS review keeps it as a secondary localization, and there is no contrary evidence; the earlier REMOVE gave no evidence-based reason.
- All 18 UniProt quotes were stale: UniProt now appends "(PubMed:7862666)" inside the FUNCTION sentence (and the flat file hyphen-breaks "gamma-glutamylcysteine"). Replaced with current CATALYTIC ACTIVITY, PATHWAY, COFACTOR or SUBUNIT text as appropriate to each row.
- IDA rows from PMID:10964706 now quote the rat-specific kinetic sentences (specific activity; K(m) for ATP and glycine; cooperative gamma-glutamyl binding) instead of the generic opening sentence.
- Description rewritten as standalone biology (removed review/curation commentary).

**Open questions.** Is rat glutathione synthetase detectable in the nucleus (e.g. by fractionation or imaging), which would turn the nucleoplasm ISO into direct rat evidence?
