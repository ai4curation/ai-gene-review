# TCF7L1 notes

## 2026-11-26 curation

- Automated deep research did not run in this workspace: `just deep-research human TCF7L1 --provider perplexity` reported that `perplexity` was unavailable and only `claude_code` was configured. I used cached GOA evidence, UniProt, Reactome, PANTHER family data, and cached primary papers for manual synthesis instead.
- TCF7L1/TCF3 is the human PTHR10373:SF25 member. Its GOA profile is small: most experimental NAS rows are old TCF3/HMG-family or gastric-cancer TCF3 rows, while the most specific Wnt, chromatin, RNA polymerase II cis-regulatory binding, and beta-catenin-TCF complex annotations come from PAINT and Reactome.
- The same conserved TCF/LEF mechanism supports the IBA rows: HMG-box DNA binding and nuclear beta-catenin/TLE cofactor switching in canonical Wnt transcription. UniProt summarizes TCF7L1 as a DNA-binding repressor in the absence of CTNNB1, and the orthologous Xenopus Tcf3 paper directly showed physical interaction with Groucho-family corepressors [PMID:9783587, "Tcf factors physically interact with members of the Groucho family of transcriptional repressors"].
- Direct TCF7L1 rows to old `DNA binding`, `DNA-binding transcription factor activity`, and `regulation of DNA-templated transcription` terms were judged true but too general now that RNA polymerase II cis-regulatory DNA binding and canonical Wnt signaling rows are present.
- The single Dazap2 `GO:0005515` row was removed only because bare protein binding is uninformative; the row's `WITH/FROM` partner was preserved.
