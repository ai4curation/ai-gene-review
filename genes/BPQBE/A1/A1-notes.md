# BPQBE A1 (Minor capsid protein A1 / Q8LTE1) Notes

## Overview
- **Gene symbol**: `A1`
- **UniProt ID**: `Q8LTE1` (`A1_BPQBE`)
- **Organism**: Qubevirus durum / Escherichia virus Qbeta (`NCBITaxon:39803`)
- **Protein**: Minor capsid protein A1 (A1 read-through protein), 329 amino acids.

## Biological Function & Read-Through Mechanism
- **Translational read-through of `cp` UGA stop codon**: `A1` is produced by episodic ribosomal read-through (~3–5% frequency, inserting tryptophan at the leaky UGA stop codon after Tyr-133 of `cp`), generating a 329-aa polypeptide consisting of the N-terminal 133-aa coat domain (`cp`), a flexible proline-rich linker, and a 196-aa C-terminal read-through domain ([PMID:27671640]; [PMID:29078304]; [file:BPQBE/A1/A1-uniprot.txt]).
- **Capsid incorporation and essentiality for infectivity**: Approximately 3 to 10 copies of `A1` are incorporated into each T=3 icosahedral Qbeta virion (`GO:0039617`), replacing monomers of the major coat protein so that the C-terminal read-through extensions project from the exterior of the capsid (`GO:0039660`). Incorporation of `A1` is essential for phage infectivity ([PMID:27671640]; [PMID:29078304]; [file:BPQBE/A1/A1-uniprot.txt]).

## Curation Decisions
- **MODIFY**:
  - `GO:0005198` (`structural molecule activity`, IEA from GO_REF:0000002) -> `GO:0039660` (`structural constituent of virion`).
  - `GO:0019028` (`viral capsid`, IEA from GO_REF:0000120) -> `GO:0039617` (`T=3 icosahedral viral capsid`).
