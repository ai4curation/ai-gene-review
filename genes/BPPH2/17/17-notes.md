# Gene 17 (Early replication auxiliary protein gp17 / p17, P03686) — Curation Notes

## Summary of Function
Gene `17` of *Bacillus phage phi29* (`NCBITaxon:2884424`) encodes a 166-amino-acid early acidic protein (gp17, p17; UniProt `P03686`) transcribed from the rightmost early operon (C2 promoter).
- **Biological role in protein-primed viral DNA genome replication (`GO:0039693`)**: Protein p17 is conditionally required at the very beginning of viral DNA amplification when *Bacillus subtilis* is infected at a low multiplicity of infection (MOI), which reflects natural infection conditions, whereas it becomes dispensable at high MOI (`PMID:9858710`, `file:BPPH2/17/17-uniprot.txt`).
- **Mechanism of action**: Protein p17 does not bind DNA on its own; instead, it physically interacts with the viral histone-like double-stranded DNA-binding protein p6 (`P03685`) in solution and optimizes the affinity and specificity of p6 binding to the viral DNA replication origins at both genome termini, thereby stimulating formation of the p6-DNA initiation nucleoprotein complex when template and initiation factor concentrations are limiting (`PMID:9858710`, `file:BPPH2/17/17-uniprot.txt`). It also participates in a pulling/injection step of the viral genome during the second stage of DNA entry into the host cell (`PMID:9858710`).

## Domain Architecture & Structural Features
- **InterPro / Pfam**: `InterPro:IPR035184` (Bacillus phage phi29 early protein Gp17), `Pfam:PF17549` (`Phage_Gp17`).

## Literature & Annotation Review
- `PMID:9858710`: Demonstrated that gene 17 mutants (`sus17(112)`) have a severe defect in phage DNA synthesis at low MOI in *B. subtilis*, but synthesize near-wild-type DNA levels at high MOI, showing that p17 is conditionally required for the first rounds of viral DNA replication.
- `PMID:820555`: Classical genetic characterization showing gene 17 mutants affect phage DNA synthesis.
- **GO Annotation Decisions**:
  - Refine `GO:0006260` (`DNA replication`, IEA `GO_REF:0000043`) via `MODIFY` to `GO:0039693` (`viral DNA genome replication`), and `ACCEPT` `GO:0039693` (`viral DNA genome replication`, IDA `PMID:9858710`, IEA `GO_REF:0000120`, IMP `PMID:820555`).
