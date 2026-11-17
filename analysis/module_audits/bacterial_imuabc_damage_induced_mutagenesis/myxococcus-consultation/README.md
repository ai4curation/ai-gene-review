# Myxococcus consultation

This folder establishes the primary-source identity of MXAN_3991/Q1D5A2 and
records a focused annotation review. It is kept with the module audit because
the identity question arose during module capacity review; the gene's biological
review and notes remain under `genes/MYXXD/MXAN_3991/`.

Run `just identity` from this directory after the repository-root input files
have been acquired. `just download-genome` downloads the versioned ENA reference
into ignored cache. `uv run --with biopython==1.85` pins the sole sequence-analysis
dependency. The figure provenance and manually transcribed query blocks are
separate inputs. `identity-results.json` contains raw matches and translation
comparison; RESULTS.md contains the interpretation.

`baseline.json` freezes the seed before curation, and `preserve.py` checks the
ordered original annotation payloads and protected source hashes while accounting
for explicitly appended proposals. It verifies preservation, not scientific
truth. The source and identity reports provide the independent evidence.
