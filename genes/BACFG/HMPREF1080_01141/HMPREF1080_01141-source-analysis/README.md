# Assayed sequence identity

The original NCBI FASTA for WP_005801052.1 was fetched through EFetch using the
URL in `sequence-identity.json`. Strip the FASTA header and concatenate sequence
lines; compare with the whitespace-stripped amino-acid block after `SQ` and
before `//` in the unchanged adjacent UniProt record. All 397 residues match
exactly; the JSON records both sequence hashes and the result. This is an
accession/sequence identity check, not an alignment-based functional prediction.

PMID37437886 states that WP_005801052.1 was synthesized, codon optimized and
expressed in E. coli. Equality links that assay sequence to I9VY56; it does not
mean the reference B. fragilis strain itself was experimentally manipulated.
