# AimP (Bacillus phage phi3T) — Curation Notes

## Overview
- **Gene symbol**: `AimP`
- **UniProt ID**: `P0DOE2` (`AIMP_BPPHT`)
- **Organism**: *Bacillus* phage phi3T (`NCBITaxon:10736`)
- **Product**: Protein AimP (43 aa precursor) / Mature Arbitrium peptide (`SAIRGA`, residues 38–43)

## Biological Function and Mechanism
- **Arbitrium phage communication system**: `AimP` is the signaling peptide precursor of the three-gene arbitrium quorum-sensing-like system (`aimR`–`aimP`–`aimX`) that governs the lysis-lysogeny (`latency-replication`) decision in *Bacillus* phage phi3T [PMID:28099413].
- **Processing and secretion**: Translated as a 43-amino-acid precursor containing an N-terminal signal peptide (residues 1–30) and a propeptide sequence (residues 31–37), `AimP` is secreted into the extracellular medium and processed by *Bacillus* extracellular proteases into the mature C-terminal hexapeptide `SAIRGA` (residues 38–43) [PMID:28099413].
- **Import and receptor binding**: As phages infect host cells over successive infection cycles, `SAIRGA` accumulates in the extracellular medium and is imported into the bacterial cytoplasm via the host oligopeptide permease (`OPP`) transporter complex [PMID:28099413].
- **Allosteric inhibition of AimR**: Inside the cell, `SAIRGA` binds directly and specifically to the phage-encoded transcriptional activator `AimR` (`EC50 = 138 nM`), triggering dissociation of the DNA-binding `AimR` homodimer into inactive monomers [PMID:28099413]. Loss of `AimR` DNA binding prevents transcription of the non-coding negative regulator `aimX`, shifting the phage developmental program from lytic replication toward lysogeny (latency) to preserve the dwindling host population [PMID:28099413].

## Curation Decisions
- **Existing annotations**:
  - `GO:0005576` (`extracellular region`, IEA): `ACCEPT`. The mature arbitrium peptide is secreted into and accumulates within the extracellular medium.
  - `GO:0098689` (`latency-replication decision`, IDA from PMID:28099413 and IEA): `ACCEPT`. This is the defining biological process mediated by `AimP`.
- **Previous draft cleanup**:
  - Removed two unsupported `NEW` annotations (`GO:0005179` hormone activity and `GO:0030414` peptidase inhibitor activity) that were erroneously included in an earlier draft (`AimP` is a bacterial/phage peptide signal, not a hormone or peptidase inhibitor) and removed the non-existent `AimP-falcon-research.md` file reference.
