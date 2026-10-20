# Gene 6 (Double-stranded DNA-binding histone-like nucleoprotein gp6 / p6, P03685) — Curation Notes

## Summary of Function
Gene `6` of *Bacillus phage phi29* (`NCBITaxon:2884424`) encodes the abundant 104-amino-acid (103 AA after initiator methionine removal) histone-like architectural double-stranded DNA-binding protein (gp6, p6; UniProt `P03685`, ~700,000 copies per infected cell). Protein p6 dimers bind cooperatively across the viral dsDNA genome (`GO:0003677`), recognizing minor-groove bendability rather than a strict consensus sequence, and wrap DNA into a right-handed toroidal superhelix around a multimeric protein core (~24 bp per dimer, compacting the DNA ~4.3-fold) (`PMID:2111580`, `PMID:15118076`, `file:BPPH2/6/6-uniprot.txt`).
This architectural nucleoprotein complex performs two core biological roles:
1. **Activation of protein-primed viral DNA replication (`GO:0039685`)**: High-affinity nucleation of p6 at both replication origins (specifically nucleotides 62–125 at the right end and 46–68 at the left end) induces localized unwinding/structural distortion of the adjacent AT-rich origin region, stimulating formation of the covalent p3-dAMP initiation complex by DNA polymerase gp2 (`PMID:2111580`, `PMID:15118076`, `PMID:820555`).
2. **Global and promoter-specific regulation of viral transcription (`GO:0046782`)**:
   - At the right-end early promoter C2, p6 binding across the promoter impairs formation of the closed complex with *Bacillus subtilis* $\sigma^A$-RNA polymerase (`PMID:11384991`).
   - In the central intergenic region between early promoters A2c/A2b and late promoter A3, p6 binds cooperatively with the sequence-specific transcriptional regulator p4 (`P03682`) over ~200 bp to form a hairpin-like ternary repression/switching complex that represses early promoters A2c and A2b while favoring activation of late promoter A3 (`PMID:12426390`).

## Domain Architecture & Structural Features
- **InterPro / Pfam**: `InterPro:IPR035188` (Bacteriophage phi29 histone-like protein p6), `Pfam:PF17548` (`p6`).
- **Oligomerization**: Homodimer in solution that polymerizes into a multimeric protein scaffold upon binding supercoiled or linear dsDNA (`PMID:2111580`, `PMID:15118076`).

## Critical Evaluation of Existing GO Annotations
- **DNA binding (`GO:0003677`, IDA `PMID:2111580` and IEA `GO_REF:0000120`)**: `ACCEPT`.
- **`GO:0001217` (`DNA-binding transcription repressor activity`, IMP `PMID:12426390`)**: Marked `MODIFY` to `GO:0003677` (`DNA binding`). In GO, `GO:0001217` is a child of `GO:0003700` (`DNA-binding transcription factor activity`), which is restricted to sequence-specific transcription factors and explicitly excludes chromatin/nucleoid architectural proteins that compact or wrap DNA non-specifically. In `PMID:12426390`, sequence specificity is provided by p4 (`P03682`), which contacts the C-terminal tail of p6 to nucleate a cooperative architectural nucleoprotein complex across the promoter region.
- **Replication terms (`GO:0006260`, `GO:0039693`)**: Refined via `MODIFY` to `GO:0039685` (`protein-primed viral DNA replication`).
- **Transcription terms**:
  - `GO:0046782` (`regulation of viral transcription`, IDA `PMID:11384991`): `ACCEPT`.
  - `GO:0006351` (`DNA-templated transcription`, IMP `PMID:12426390`) and `GO:0045892` (`negative regulation of DNA-templated transcription`, IEA `GO_REF:0000108`): Refined via `MODIFY` to `GO:0046782` (`regulation of viral transcription`), as p6 specifically regulates viral promoters (repressing early promoters C2, A2b, A2c and cooperating with p4 at late promoter A3).
- **`GO:0017053` (`transcription repressor complex`, IDA/IMP `PMID:12426390`)** and **`GO:0030261` (`chromosome condensation`, IEA `GO_REF:0000043`)**: Kept as `KEEP_AS_NON_CORE` because p6 forms a ternary nucleoprotein repression complex with p4 at A2c/A2b and compacts viral dsDNA ~4-fold across the genome in vivo.
