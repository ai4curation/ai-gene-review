# Gene Review Notes: Bacillus phage phi29 `10` (`P04332`, `PORTL_BPPH2`)

## Overview
- **Gene symbol**: `10`
- **UniProt ID**: `P04332` (`PORTL_BPPH2`)
- **Protein name**: Portal protein gp10 (head-tail connector protein)
- **Length**: 309 amino acids (35,895 Da)
- **Taxon**: *Bacillus phage phi29* (`NCBITaxon:2884424`)
- **InterPro / Pfam domains** (from `file:BPPH2/10/10-uniprot.txt`):
  - `InterPro:IPR008016` (`Gp10`, Bacteriophage phi29 connector protein Gp10)
  - `InterPro:IPR036199` (`Gp10_sf`, Phage portal protein, gp10-like superfamily)
  - `Pfam:PF05352` (`Phage_connector`)

## Literature & Bioinformatic Synthesis
- **Dodecameric Portal Architecture**: gp10 assembles into a 12-subunit ring-shaped homododecamer (`GO:0046798` `viral portal complex`) embedded at the unique 5-fold portal vertex of the prolate procapsid (`GO:0046729`) and mature capsid (`GO:0019028`) [PMID:10801350; PMID:15886394; PMID:22225806; file:BPPH2/10/10-uniprot.txt]. Its central 3.6-nm channel is lined by 48 positively charged lysine residues arranged in four 12-lysine rings (`PMID:22225806`).
- **Role in Procapsid Assembly and DNA Packaging**:
  1. **Capsid Nucleation**: Co-interactions between the gp10 portal dodecamer, the internal scaffolding protein `gp7`, and the major capsid protein `gp8` initiate prohead nucleation (`GO:0019069` `viral capsid assembly`) and determine its *T*=3, *Q*=5 prolate geometry (`file:BPPH2/10/10-uniprot.txt`).
  2. **pRNA Binding (`GO:0003723`) & Motor Assembly**: The basic N-terminal 14 amino acids (specifically Arg-Lys-Arg at residues 3–5) of each gp10 monomer protrude at the narrow outer end of the connector and directly bind the prohead packaging RNA (`pRNA`) ring (`PMID:10801350`; `PMID:15886394`). Proteolytic removal of the N-terminal 14 residues abolishes pRNA binding and DNA packaging (`PMID:15886394`).
  3. **One-Way Valve DNA Translocation (`GO:0019073`)**: During ATP-driven genome packaging by the `gp16` ATPase, viral dsDNA-gp3 is pumped through the gp10 central channel via a "push through a one-way valve" mechanism in which channel loops and lysine rings prevent DNA slippage (`PMID:22225806`).
  4. **Tail Attachment and Genome Ejection**: After DNA packaging is completed, pRNA and `gp16` dissociate and the lower collar/tail tube (`gp11`) attaches to the exposed lower end of gp10, forming the conduit through which viral DNA exits during infection (`GO:0099002` `symbiont genome ejection through host cell envelope, short tail mechanism`) [PMID:10801350; PMID:22225806; file:BPPH2/10/10-uniprot.txt].

## Annotation Review Summary
- `GO:0003723` (`RNA binding`, IEA, `GO_REF:0000043`): `ACCEPT`. Directly supported by photoaffinity cross-linking and N-terminal truncation assays showing gp10 binds pRNA via residues 1–14 (`PMID:15886394`).
- `GO:0019028` (`viral capsid`, IEA, `GO_REF:0000043`): `ACCEPT`. Embedded at the unique portal vertex of the viral capsid (`PMID:10801350`).
- `GO:0019073` (`viral DNA genome packaging`, IDA, `PMID:15886394`): `ACCEPT`. Essential hub and one-way valve channel of the phi29 DNA packaging motor (`PMID:15886394`; `PMID:22225806`).
- `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`): `TOO_GENERAL`. Entailed by the more specific annotation `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`) already present on this gene.
- `GO:0046729` (`viral procapsid`, IDA, `PMID:22225806`): `ACCEPT`. Core component of the procapsid (`PMID:22225806`).
- `GO:0046798` (`viral portal complex`, IDA, `PMID:10801350`): `ACCEPT`. Forms the dodecameric viral portal complex (`PMID:10801350`).
- `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IEA, `GO_REF:0000043`): `KEEP_AS_NON_CORE`. Serves as the passive exit channel at the head-tail junction through which the packaged genome is ejected during infection (`PMID:22225806`; `file:BPPH2/10/10-uniprot.txt`).
