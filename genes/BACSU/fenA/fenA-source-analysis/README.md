# Bacillus subtilis maturation-enzyme identity bridge

Official strain 168 records are FenA/ypcP P54161 (BSU22010, 296 aa), RnhC P94541 (BSU28620, 313 aa), and PolA O34996 (BSU29090, 880 aa). The normally fetched records remain unchanged.

The complete PY79 chromosome CP006881.1 was obtained from https://www.ebi.ac.uk/ena/browser/api/embl/CP006881.1 . Its unmodified SHA256, exact CDS coordinates, nucleotide sequences, translations and accession qualifiers are preserved in PY79-sequence-proof.json. The complete 9 MB source is retained in the ignored audit cache; the committed JSON is an explicitly derived extract, not a replacement database record.

Each frozen strain 168 protein has one exact full-length PY79 translation match: P54161 matches AHA78071.1/U712_10640; P94541 matches AHA78768.1/U712_14150; O34996 matches AHA78817.1/U712_14395. All three matches are 100% identical over their full lengths.

PMID37146086 explicitly states that wild-type genes were amplified from PY79 genomic DNA, plasmids were Sanger-verified, and strains derive from PY79. This supports transferring purified-protein chemistry to the identical strain 168 sequences. Native PY79 growth phenotypes remain PY79 observations: identical proteins do not make strain backgrounds identical. PMID30670546 also describes PY79-derived constructs/strains; its cached abstract and inspected online full text are distinguished in the notes. PMID42286923 uses fluorescent fusion constructs: main text does not resolve the parental strain, so it supplies contextual localization evidence only and no strain-168-specific assay is claimed.

Run `uv run python genes/BACSU/fenA/fenA-source-analysis/verify_identity.py` from the repository root to verify translated CDS sequences against frozen UniProt files.
