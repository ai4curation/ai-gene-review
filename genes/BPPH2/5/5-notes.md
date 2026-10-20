# Gene 5 (Single-stranded DNA-binding protein gp5 / p5, Q38504) — Curation Notes

## Summary of Function
Gene `5` of *Bacillus phage phi29* (`NCBITaxon:2884424`) encodes the 124-amino-acid monomeric single-stranded DNA-binding protein (gp5, p5; UniProt `Q38504`). During protein-primed viral DNA replication (`GO:0039685`), strand-displacement synthesis initiated from both ends of the linear genome generates long single-stranded DNA (ssDNA) intermediates (Type I and Type II replication intermediates). Protein p5 binds cooperatively and non-sequence-specifically to this displaced viral ssDNA (`GO:0003697`), protecting it from host nuclease degradation, preventing unproductive non-specific binding of the viral DNA polymerase gp2 to ssDNA, and Removing secondary structure /helix-destabilizing barriers to stimulate the DNA synthesis rate (`PMID:2499869`, `PMID:1899235`).

## Domain Architecture & Structural Features
- **InterPro / Pfam**: `InterPro:IPR035408` (Phi29-like phage single-stranded DNA-binding protein), `Pfam:PF17427` (`Phi29_Phage_SSB`).
- **OB-fold**: Adopts an oligonucleotide/oligosaccharide-binding (OB) fold characteristic of phage and cellular SSBs, functioning as a monomer in solution that forms cooperative helical filaments along ssDNA (covering ~3–4 nucleotides per monomer).

## Literature & Annotation Review
- `PMID:2499869`: Purified protein p5 and demonstrated that it binds ssDNA, protects ssDNA against nuclease degradation, and stimulates in vitro phi29 DNA-p3 replication after an initial incubation period.
- `PMID:1899235`: Showed that p5 has helix-destabilizing activity, prevents non-productive binding of phi29 DNA polymerase to ssDNA, and increases DNA replication rate severalfold on natural phi29 DNA and primed M13 ssDNA templates.
- `PMID:4630506`: Temperature-sensitive gene 5 mutants are defective in viral DNA synthesis in vivo.
- **GO Annotation Decisions**:
  - Refine `GO:0003677` (`DNA binding`, IDA `PMID:2499869` and IEA `GO_REF:0000043`) via `MODIFY` to `GO:0003697` (`single-stranded DNA binding`).
  - Refine `GO:0006260` (`DNA replication`) and `GO:0039693` (`viral DNA genome replication`) via `MODIFY` to `GO:0039685` (`protein-primed viral DNA replication`).
