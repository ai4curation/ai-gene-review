# ubiF review notes (E. coli K-12, P75728)

Reviewed for the ubiquinone_biosynthesis module (UbiF late hydroxylase annoton).

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  reviewed UniProt record, cached abstracts and the PTHR43876 PAINT table.

## Which hydroxylation

- UbiF performs the last ring hydroxylation, demethoxyubiquinol-8 to
  3-demethylubiquinol-8 (GO:0008682). [PMID:10802164 "The ubiF encoded oxygenase
  introduces the hydroxyl group at carbon five of
  2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol"] The "carbon five" is the old
  E. coli numbering; in ubiquinone numbering this is the C6 (GO's "3-") position.
- The same abstract's assignment of other positions to UbiB and UbiH predates
  UbiI's discovery (PMID:23709220) and is outdated for UbiB.
- ubiF mutants accumulate the substrate. [PMID:4323297 "Mutants accumulating
  2-octaprenyl-6-methoxy-1,4-benzoquinone and
  2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinone were shown to carry mutations
  in genes designated ubiE and ubiF, respectively."]

## Decisions

- Generic oxygenase (ARBA, InterPro, EcoCyc ISS) and flavin terms: MODIFY to
  GO:0008682 / GO:0071949. Protein-binding rows removed.
