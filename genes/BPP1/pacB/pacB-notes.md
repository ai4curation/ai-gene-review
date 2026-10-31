# pacB (P27753) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `pacB` (defined genetically by amber mutation `am2.17`).
- **Protein**: Terminase large subunit (PacB / TerL; 494 aa, ~55.7 kDa). An internal in-frame product (`PacC`, ~16 kDa) translated from the distal third of `pacB` was also observed, though its physiological role is unknown [PMID:1538406, PMID:15489417].
- **Biological role**: Catalytic subunit of the bacteriophage P1 terminase ("pacase") complex (`PacAB`). Together with the small DNA-recognition subunit PacA (`P28813`), PacB cleaves concatemeric P1 DNA at the methylated `pac` site to initiate packaging, translocates ~110 kb of DNA (one headful, with ~10 kb terminal redundancy) into the prohead using the energy of ATP hydrolysis, and performs the headful termination cut [PMID:1538406, PMID:15489417, PMID:18687036].
- **Domain architecture**:
  - **N-terminal ATPase domain**: Contains a nucleotide-binding region (`aa 26–33`), Walker A motif (`aa 56–63`), and Walker B motif (`aa 158–163`) that couple ATP binding and hydrolysis to DNA translocation (`file:BPP1/pacB/pacB-uniprot.txt`, [PMID:15489417, PMID:18687036]).
  - **C-terminal nuclease domain**: RNase H-fold Mg2+-dependent endonuclease domain with conserved acidic divalent metal-coordinating residues (`Asp293`, `Asp356`, `Asp446`) that cleave both strands of concatemeric DNA (`file:BPP1/pacB/pacB-uniprot.txt`, [PMID:18687036]).

## Review of Existing GOA Annotations
- `GO:0000166` (`nucleotide binding`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0547): **TOO_GENERAL**. True but uninformative because the more specific descendant `GO:0005524` (`ATP binding`) is already present on this gene.
- `GO:0004518` (`nuclease activity`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0540): **TOO_GENERAL**. True but redundant with the more specific child term `GO:0004519` (`endonuclease activity`) already annotated on this gene.
- `GO:0004519` (`endonuclease activity`, IEA, `GO_REF:0000002` InterPro:IPR021653 `Terminase_lsu_bacteriophage`): **ACCEPT**. Core catalytic activity of the C-terminal nuclease domain of PacB, which cleaves concatemeric P1 dsDNA at `pac` to initiate packaging and makes the headful termination cut [PMID:1538406, PMID:15489417, PMID:18687036].
- `GO:0005524` (`ATP binding`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0067): **ACCEPT**. PacB contains conserved Walker A and Walker B ATP-binding motifs in its N-terminal packaging motor domain (`file:BPP1/pacB/pacB-uniprot.txt`, [PMID:15489417]).
- `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0378): **TOO_GENERAL**. True but entailed by the more specific accepted term `GO:0004519` (`endonuclease activity`).
- `GO:0046872` (`metal ion binding`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0479): **MODIFY** -> `GO:0000287` (`magnesium ion binding`). The C-terminal endonuclease active site of PacB specifically coordinates catalytic `Mg(2+)` ions via conserved aspartate residues (`Asp293`, `Asp356`, `Asp446`; `file:BPP1/pacB/pacB-uniprot.txt`).
