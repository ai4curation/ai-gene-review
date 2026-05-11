# ramosa1 notes

- The GOA file contains nucleus and regulation of DNA-templated transcription annotations.
- UniProt identifies ramosa1 as a RAMOSA1 C2H2 zinc-finger transcription factor and supports nuclear localization [file:MISSI/ramosa1/ramosa1-uniprot.txt "SubName: Full=RAMOSA1 C2H2 zinc-finger transcription factor"] [file:MISSI/ramosa1/ramosa1-uniprot.txt "SUBCELLULAR LOCATION: Nucleus"].
- I accepted both existing annotations and used DNA-binding transcription factor activity as the synthesized core molecular function based on the C2H2 zinc-finger transcription factor identity.
- I did not add a more specific inflorescence-development GO process because the fetched UniProt/GOA evidence does not directly support a specific Miscanthus developmental annotation.
- UniProt has a zinc ion binding GO cross-reference, but the current GOA TSV does not include GO:0008270; if a future GOA re-fetch adds it, it should be reviewed as KEEP_AS_NON_CORE because zinc coordination supports the C2H2 domain rather than the main transcription-regulatory function [file:MISSI/ramosa1/ramosa1-uniprot.txt "GO; GO:0008270; F:zinc ion binding"].
