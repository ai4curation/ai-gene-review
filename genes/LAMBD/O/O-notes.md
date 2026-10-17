# Curation Notes for Escherichia phage lambda `O` (P03688)

## Summary of Gene Product
Bacteriophage lambda replication protein O (`O`, UniProt `P03688`, 333 AA; mass ~33.9 kDa, 299 AA in standard reference sequence annotation, `InterPro:IPR006497`) is the phage-encoded origin-recognition and replication initiator protein essential for early bidirectional theta-mode replication of the circularized lambda genome [file:LAMBD/O/O-uniprot.txt; PMID:2525129]. Multiple dimers of O bind cooperatively to the four 19-bp inverted-repeat iterons within the phage replication origin (`ori lambda`, located internal to the `O` coding sequence itself) to wrap the origin DNA into a nucleosome-like nucleoprotein complex termed the "O-some" [file:LAMBD/O/O-uniprot.txt; PMID:2525129].

## Structural and Mechanistic Architecture
- **N-terminal origin DNA-binding domain (`PDB:5FDK`)**: Forms a winged-helix dimer that recognizes the four iterons (`I`–`IV`) of `ori lambda` and induces sharp DNA bending, wrapping `ori lambda` into the O-some and destabilizing the adjacent AT-rich region (`GO:0003688`, `DNA replication origin binding`) [PMID:2525129].
- **C-terminal P-recruitment domain (`PDB:6CKA`)**: Binds the N-terminal domain of the phage helicase-loader protein `P`, recruiting the `P-DnaB` complex to the O-some to assemble the pre-primosomal `ori lambda:O:P:DnaB` initiation complex prior to DnaK/DnaJ/GrpE-mediated remodeling and bidirectional replication fork activation [PMID:2525129].
- **Rapid proteolysis by host ClpXP**: Free O protein is rapidly degraded by the host ClpXP protease, whereas assembly into the O-some and pre-primosomal complex protects O from proteolysis, coupling origin firing to active transcription and translation.

## Review of Existing GO Annotations
- **`GO:0003677` (`DNA binding`, 2 rows: IDA `PMID:2525129` and IEA `GO_REF:0000043`)**: `MODIFY` both rows -> `GO:0003688` (`DNA replication origin binding`). Both UniProt and `PMID:2525129` specifically establish that lambda O binds the চার iterons of the bacteriophage lambda replication origin (`ori lambda`) to assemble the O-some during replication initiation [file:LAMBD/O/O-uniprot.txt; PMID:2525129].
- **`GO:0039686` (`bidirectional double-stranded viral DNA replication`, IDA `PMID:2525129`)**: `ACCEPT`. Core biological role of lambda O in initiating bidirectional theta replication of the viral dsDNA genome [file:LAMBD/O/O-uniprot.txt; PMID:2525129].
- **`GO:0006260` (`DNA replication`, IEA `GO_REF:0000120`)**: `TOO_GENERAL`. Entailed by `GO:0039686` (`bidirectional double-stranded viral DNA replication`).
