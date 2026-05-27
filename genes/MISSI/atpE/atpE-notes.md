# atpE notes

- The GOA file is header-only, so there are no existing GOA annotations to review or convert into NEW rows.
- The batch target accession is A0A0S2RMA2. A symbol-only fetch initially matched A0A0S2RM82, an atpH entry with atpE as a synonym, so the atpE data were re-fetched with `--uniprot-id A0A0S2RMA2 --force`.
- UniProt identifies A0A0S2RMA2 as plastid ATP synthase CF1 epsilon subunit and supports membership in the ATPase epsilon chain family [file:MISSI/atpE/atpE-uniprot.txt "SubName: Full=ATP synthase CF1 epsilon subunit"] [file:MISSI/atpE/atpE-uniprot.txt "Belongs to the ATPase epsilon chain family"].
- Core curation uses contributes_to proton-transporting ATP synthase activity because atpE is a subunit of the proton-transporting ATP synthase complex rather than the whole catalytic activity by itself [file:MISSI/atpE/atpE-uniprot.txt "GO; GO:0045259; C:proton-transporting ATP synthase complex"] [file:MISSI/atpE/atpE-uniprot.txt "GO; GO:0046933; F:proton-transporting ATP synthase activity, rotational mechanism"].
- Chloroplast thylakoid membrane is used as the location based on the plastid genome context and ATP synthase chloroplast/thylakoid keywords [file:MISSI/atpE/atpE-uniprot.txt "OG   Plastid"] [file:MISSI/atpE/atpE-uniprot.txt "KW   Chloroplast"] [file:MISSI/atpE/atpE-uniprot.txt "KW   Thylakoid"].
- PR review asked for a term-label check on GO:0015986. The local GO cache labels GO:0015986 as proton motive force-driven ATP synthesis, matching the label used in the review.
