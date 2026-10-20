# XANAU/dhlA counterpart analysis

Run `just analyze` from this directory to regenerate the comparison, fetching any
missing cached inputs. Requires MMseqs2 18-8cc5c and the repository uv.lock
(Biopython 1.85). `just snapshot` refreshes current source records and the explicit
UniSave versions used here. Inspect source changes and reassess manually before
updating the review; rerunning analysis does not adjudicate relationships.

The live proteome download may change from release 2026_03. Database checksums,
retrieval dates and source releases are recorded in comparison.yaml. The full
proteome FASTAs are ignored cache artifacts; all retrieved candidate sequences
and the query remain committed for inspection. Manual decisions for this batch
are in projects/ORPHAN_CURATED/counterpart-decisions.yaml. [RESULTS.md](RESULTS.md)
records the interpretation for this gene.
