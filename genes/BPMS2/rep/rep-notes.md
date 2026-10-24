# BPMS2 rep (RNA-directed RNA polymerase beta chain / P00585) Notes

## Overview
- **Gene symbol**: `rep`
- **UniProt ID**: `P00585` (`RDRP_BPMS2`)
- **Organism**: Escherichia phage MS2 (`NCBITaxon:12022`)
- **Protein**: RNA-directed RNA polymerase beta chain (RNA replicase beta chain), 545 amino acids, EC 2.7.7.48.

## Biological Function & Subunit Composition
- **Catalytic RdRp subunit**: `rep` encodes the phage-specific catalytic beta subunit of the MS2 replicase holoenzyme (`GO:0003968`). It assembles with host *Escherichia coli* translation elongation factors EF-Tu and EF-Ts and 30S ribosomal protein S1 to replicate the positive-strand ssRNA genome via a complementary negative-strand RNA intermediate (`GO:0039694`) ([PMID:2202149]; [file:BPMS2/rep/rep-uniprot.txt]).
- **Experimental verification**: In [PMID:2202149], plasmid-expressed MS2 replicase rescued infectivity of in vitro transcribed negative-strand MS2 RNA in *E. coli* spheroplasts, directly demonstrating negative-strand-templated synthesis of infectious positive-strand viral RNA.

## Curation Decisions
- **ACCEPT**:
  - `GO:0003968` (`RNA-directed RNA polymerase activity`, IEA from GO_REF:0000120): Core enzymatic activity of the `rep` beta subunit.
  - `GO:0039694` (`viral RNA genome replication`, IEA from GO_REF:0000002): Core biological process mediated by the viral replicase complex.
- **KEEP_AS_NON_CORE**:
  - `GO:0000166` (`nucleotide binding`, IEA from GO_REF:0000043): True substrate-binding property of the polymerase (binds ribonucleoside 5'-triphosphates), kept as non-core alongside the catalytic `GO:0003968` activity.
  - `GO:0001172` (`RNA-templated transcription`, IEA from GO_REF:0000108): In (+)-ssRNA phages, synthesis of positive-sense genomic RNA from the negative-strand template produces the mRNA used for viral translation; kept as non-core alongside the more specific `GO:0039694` (`viral RNA genome replication`).
- **MODIFY**:
  - `GO:0016740` (`transferase activity`, IEA from GO_REF:0000043) -> `GO:0003968` (`RNA-directed RNA polymerase activity`).
  - `GO:0016779` (`nucleotidyltransferase activity`, IEA from GO_REF:0000043) -> `GO:0003968` (`RNA-directed RNA polymerase activity`).
  - `GO:0034062` (`5'-3' RNA polymerase activity`, EXP from PMID:2202149 and IEA from GO_REF:0000116) -> `GO:0003968` (`RNA-directed RNA polymerase activity`).
  - `GO:0019079` (`viral genome replication`, IEA from GO_REF:0000002) -> `GO:0039694` (`viral RNA genome replication`).
