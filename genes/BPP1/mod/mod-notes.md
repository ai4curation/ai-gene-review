# mod (P08763) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `mod` (first gene of the constitutively expressed `mod-res` Type III restriction-modification operon).
- **Protein**: Type III restriction-modification system EcoP1I modification methyltransferase (`Mod` / `M.EcoP1I`; 646 aa, ~73.5 kDa, `EC:2.1.1.72`, beta-class $N^6$-adenine DNA methyltransferase) [PMID:2837577, PMID:11178902, PMID:12654995, PMID:14715260, PMID:21048863].
- **Biological role & mechanism**:
  - `Mod` (`M.EcoP1I`) is the sequence-recognition and DNA methyltransferase subunit of the prototype Type III restriction-modification enzyme EcoP1I [PMID:2837577, PMID:11178902].
  - Alone, `Mod` forms a homodimer (`Mod2`) that specifically recognizes the asymmetric pentanucleotide sequence `5'-AGACC-3'` (in both dsDNA and ssDNA) and transfers a methyl group from $S$-adenosyl-L-methionine (AdoMet) to the $N^6$ position of the second (internal) adenine (`5'-AGm6ACC-3'`, `GO:0009007` `site-specific DNA-methyltransferase (adenine-specific) activity`, `GO:0006306` `DNA methylation`), protecting endogenous host and prophage DNA from EcoP1I restriction cleavage [PMID:2837577, PMID:11178902, PMID:14715260, PMID:21048863].
  - `Mod2` also assembles with two subunits of the restriction endonuclease/helicase subunit `Res` (`P08764`) to form the heterotetrameric `Res2Mod2` EcoP1I restriction-modification holoenzyme (`GO:0009307` `DNA restriction-modification system`), in which `Mod` provides sequence-specific `5'-AGACC-3'` target recognition (`GO:0003677` `DNA binding`) required for `Res`-catalyzed ATP-dependent DNA translocation and cleavage 25–27 bp downstream of unmodified sites [PMID:11178902, PMID:15489417].

## Review of Existing GOA Annotations
- `GO:0003676` (`nucleic acid binding`, IEA, `GO_REF:0000119`): **TOO_GENERAL**. Entailed by `GO:0003677` (`DNA binding`) present on this gene.
- `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000043`): **ACCEPT**. `Mod` is the DNA-binding target recognition subunit of EcoP1I that recognizes `5'-AGACC-3'` [PMID:11178902, PMID:14715260].
- `GO:0003824` (`catalytic activity`, IEA, `GO_REF:0000119`): **TOO_GENERAL**. Entailed by `GO:0009007` (`site-specific DNA-methyltransferase (adenine-specific) activity`).
- `GO:0006304` (`DNA modification`, IEA, `GO_REF:0000002`): **TOO_GENERAL**. Entailed by `GO:0006306` (`DNA methylation`).
- `GO:0006306` (`DNA methylation`, IEA, `GO_REF:0000043` / `GO_REF:0000117`): **ACCEPT** (2 rows). Methylates the second adenine of `5'-AGACC-3'` to protect self DNA against restriction [PMID:2837577, PMID:14715260, PMID:21048863].
- `GO:0008168` (`methyltransferase activity`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0009007`.
- `GO:0008170` (`N-methyltransferase activity`, IEA, `GO_REF:0000117`): **TOO_GENERAL**. Entailed by `GO:0009007`.
- `GO:0008757` (`S-adenosylmethionine-dependent methyltransferase activity`, IEA, `GO_REF:0000002`): **TOO_GENERAL**. Entailed by `GO:0009007` (`site-specific DNA-methyltransferase (adenine-specific) activity`).
- `GO:0009007` (`site-specific DNA-methyltransferase (adenine-specific) activity`, IEA, `GO_REF:0000003` / `GO_REF:0000043` / `GO_REF:0000120`): **ACCEPT** (3 rows). Core catalytic activity of `M.EcoP1I` (`EC:2.1.1.72`) [PMID:2837577, PMID:14715260, PMID:21048863].
- `GO:0016740` (`transferase activity`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0009007`.
- `GO:0032259` (`methylation`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0006306` (`DNA methylation`).
