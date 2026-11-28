# TEAD2 curation notes

- Treat TEAD2 as a nuclear/chromatin DNA-binding transcription factor whose core role is binding Pol II cis-regulatory DNA and recruiting YAP/TAZ-family coactivators for Hippo-responsive transcription.
- Preserve every YAP or TAZ `GO:0005515` row separately, with its own `WITH/FROM`, but modify these rows to `transcription coactivator binding` rather than collapsing them into a single TEAD-YAP claim.
- Remove interactome-only bare protein-binding rows with partners other than YAP, TAZ, or a vestigial-like coregulator.
- Follow the current TEAD1 review's split between accepting direct transcription and Hippo rows, keeping broad vertebrate development as non-core, and marking generic protein-containing complex assembly as over-annotated when the evidence only demonstrates TEAD-YAP binding.
