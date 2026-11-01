# darB (Q71TF8) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `darB`
- **Protein**: Defense against restriction protein B (`DarB`; 2,255 aa, ~251.5 kDa — the largest protein encoded by bacteriophage P1) [PMID:15489417].
- **Biological role & domain architecture**:
  - `DarB` is a giant internal capsid protein (~35 copies per virion) that is packaged into the P1 head in a `DarA`/`DdrA`/`Hdf`-dependent manner via an N-terminal capsid-targeting sequence (residues 1–30) and co-ejected with the viral DNA into the host bacterium upon infection [PMID:3029954, PMID:15489417, PMID:28509398, PMID:35458408].
  - Once injected into the host cell, `DarB` acts exclusively in *cis* to protect entering P1 or transduced DNA against Type I restriction-modification systems of the `EcoB` and `EcoK` families (`GO:0099018` `symbiont-mediated evasion of host restriction-modification system`) [PMID:3029954, PMID:15489417, PMID:28509398].
  - Sequence analysis shows that `DarB` is a bifunctional enzyme comprising:
    1. **N-terminal gamma-class N6-adenine DNA methyltransferase domain** (`aa 570–661`, InterPro `IPR002052`), containing all nine conserved sequence motifs of gamma-type DNA adenine methyltransferases including the catalytic `NPPY/F` motif IV (`GO:0006304` `DNA modification`), which is proposed to methylate adenine residues on entering DNA to block Type I restriction [PMID:15489417].
    2. **C-terminal superfamily 2 (SF2) DNA/RNA helicase domain** (`aa 1207–1487`, InterPro `IPR014001`/`IPR001650`), containing an ATP-binding Walker A motif (`aa 1236–1243`, `GO:0005524` `ATP binding`, `GO:0004386` `helicase activity`) [PMID:15489417].

## Review of Existing GOA Annotations
- `GO:0000166` (`nucleotide binding`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0005524` (`ATP binding`).
- `GO:0004386` (`helicase activity`, IEA, `GO_REF:0000002` / `GO_REF:0000043` / `GO_REF:0000120`): **ACCEPT** (3 rows). C-terminal SF2 helicase domain (`aa 1207–1487`) [PMID:15489417].
- `GO:0005524` (`ATP binding`, IEA, `GO_REF:0000043` / `GO_REF:0000120`): **ACCEPT** (2 rows). ATP-binding motif (`aa 1236–1243`) within the C-terminal SF2 helicase domain [PMID:15489417].
- `GO:0006304` (`DNA modification`, IEA, `GO_REF:0000002` InterPro:IPR002052): **ACCEPT**. N-terminal gamma-class N6-adenine DNA methyltransferase domain (`aa 570–661`) containing the catalytic `NPPY/F` motif IV that modifies entering DNA upon infection [PMID:15489417].
- `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0004386` (`helicase activity`).
- `GO:0019028` (`viral capsid`, IEA, `GO_REF:0000043` / `GO_REF:0000044`): **ACCEPT** (2 rows). Packaged inside the P1 capsid (~35 copies/virion) and ejected with the viral genome upon infection [PMID:3029954, PMID:15489417, PMID:28509398, PMID:35458408].
- `GO:0052031` (`modulation by symbiont of host process`, IEA, `GO_REF:0000119`): **TOO_GENERAL**. Entailed by `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`).
- `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`).
- `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA, `GO_REF:0000043`): **ACCEPT**. Core function of DarB in protecting injected P1 and transduced DNA in *cis* against `EcoB` and `EcoK` Type I restriction systems [PMID:3029954, PMID:15489417, PMID:28509398].
