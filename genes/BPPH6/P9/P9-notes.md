# P9 (P9_BPPH6, P07581) — Curation Notes

## Overview
- **Organism:** *Pseudomonas* phage phi6 (`NCBITaxon:2928686`, *Cystovirus phi6*)
- **Gene / Protein:** `P9` / Major envelope protein P9 (`UniProtKB:P07581`, 90 AA)
- **Genomic Segment:** Encoded on the small (S) dsRNA segment.

## Biological Role in the Cystovirus Lifecycle
1. **Major Viral Envelope Transmembrane Protein (`GO:0039660`, `GO:0019031`, `GO:0055036`):**
   - P9 is a 90-residue single-pass transmembrane protein (helical transmembrane span AA 53–70) and the most abundant integral membrane protein of the bacteriophage phi6 lipid-containing envelope (`GO:0019031`, `GO:0055036`) [file:BPPH6/P9/P9-uniprot.txt; PMID:8021194].
2. **Intracellular Membrane Morphogenesis and Virion Assembly (`GO:0019068`):**
   - Co-expression of gene 9 (`P9`) and the nonstructural morphogenetic gene 12 (`P12`) on plasmids in *Pseudomonas syringae* pv. *phaseolicola* is necessary and sufficient to form low-density lipid-P9 precursor particles resembling the viral envelope precursor vesicles in phi6-infected cells [PMID:8021194].
   - In the absence of P12, P9 is proteolytically unstable and fails to form lipid-protein particles [PMID:8021194].
   - Note on `PMID:26213264`: This study used phi6 P9 as an artificial N-terminal fusion tag in *Escherichia coli* to improve heterologous expression and membrane integration of human membrane proteins. While it confirms P9's intrinsic membrane insertion capability (`GO:0033644` host cell membrane), P9's native biological role is assembly of the phage envelope from host membrane lipids (`GO:0019031`, `GO:0055036`, `GO:0019068`).

## Curation Decisions
- **Existing GOA Annotations:**
  - `GO:0019031` (`viral envelope`, IEA): `ACCEPT`.
  - `GO:0055036` (`virion membrane`, IEA): `ACCEPT`.
  - `GO:0033644` (`host cell membrane`, EXP from `PMID:8021194` and IDA from `PMID:26213264`): `KEEP_AS_NON_CORE` — P9 integrates into the bacterial plasma membrane prior to P12-assisted envelope budding (and in heterologous *E. coli* expression assays), making host cell membrane localization true as a biogenesis intermediate, while its mature core localization is the viral envelope (`GO:0019031`) and virion membrane (`GO:0055036`).
  - `GO:0044423` (`virion component`, IEP from `PMID:8021194`): `MODIFY` to `GO:0019031` (`viral envelope`) and `GO:0055036` (`virion membrane`) (note: `GO:0044423` is an obsolete general term replaced by specific virion subcompartment terms).
- **New Annotations (`action: NEW`):**
  - `GO:0039660` (`structural constituent of virion`, `enables`, `IC` from `PMID:8021194`): Captures P9's role as the major structural protein component of the phi6 viral envelope.
  - `GO:0019068` (`virion assembly`, `involved_in`, `IMP` / `IDA` from `PMID:8021194`): P9 and P12 are necessary and sufficient to drive assembly of the lipid-containing viral envelope.
