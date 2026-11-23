# serC curation notes

## 2026-07-19 GO term check

The official QuickGO ontology search was queried for
'phosphohydroxythreonine aminotransferase' and for 'RHEA:16573'. It returned no
dedicated molecular-function term for the PdxF reaction. GO:0004648 covers the
separate phosphoserine aminotransferase reaction, so the proposed new term in
the review remains warranted.

Queries:

- https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=phosphohydroxythreonine%20aminotransferase
- https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=RHEA%3A16573

## 2026-11 completion of the draft

- Status set COMPLETE; all rows now carry vetted support (HAMAP/NCBIfam/PIRSF
  family lines, curated HAMAP CC text, the OpenScientist report, and E. coli
  genetics PMID:2121717).
- The second core function now uses `proposed_molecular_function` pointing to
  the proposed "phosphohydroxythreonine aminotransferase activity" term, rather
  than leaving the MF unset.
- Removed the GOA-file reference. Verdicts match the E. coli SerC review except
  cytoplasm, which stays KEEP_AS_NON_CORE here because no cytosol row exists.
