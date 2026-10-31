# res (P08764) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `res` (second gene of the constitutively expressed `mod-res` Type III restriction-modification operon, translationally coupled to upstream `mod`).
- **Protein**: Type III restriction-modification system EcoP1I enzyme `res` subunit (`Res` / `R.EcoP1I`; 970 aa, ~111.4 kDa, `EC:3.1.21.5`).
- **Biological role & mechanism**:
  - `Res` is the restriction endonuclease and ATP-dependent DNA helicase/translocase subunit of the prototype Type III restriction-modification enzyme EcoP1I (`Res2Mod2` heterotetramer) [PMID:2837577, PMID:11178902, PMID:12654995].
  - `Res` is inactive in isolation and requires assembly with the sequence-specific DNA-recognition/methyltransferase subunit `Mod` (`P08763`) into a `Res2Mod2` heterotetramer [PMID:11178902].
  - `Res` comprises:
    1. **N-terminal superfamily 2 (SF2) DNA helicase/translocase domain** (`aa 309–707`, InterPro `IPR014001`), containing a Walker A ATP-binding motif (`aa 328–335`) and `DEPH` box (`aa 426–429`) that bind and hydrolyze ATP (`GO:0005524` `ATP binding`, `GO:0004386` `helicase activity`) to drive long-range communication (1D translocation/diffusion) between two inversely oriented unmethylated `5'-AGACC-3'` sites [PMID:11178902, PMID:15489417].
    2. **C-terminal PD-(D/E)xK endonuclease domain** (InterPro `IPR011335`), which catalyzes double-strand DNA cleavage 25–27 bp downstream of one of the two interacting `5'-AGACC-3'` recognition sites (`GO:0015668` `type III site-specific deoxyribonuclease activity`, `GO:0009307` `DNA restriction-modification system`) [PMID:2837577, PMID:11178902, PMID:12654995].

## Review of Existing GOA Annotations
- `GO:0000166` (`nucleotide binding`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0005524` (`ATP binding`).
- `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000043`): **ACCEPT**. Within `Res2Mod2`, `Res` contacts and translocates along double-stranded DNA via its SF2 helicase/translocase lobe and cleaves the DNA duplex 25–27 bp downstream of the recognition site via its C-terminal endonuclease domain [PMID:11178902].
- `GO:0003824` (`catalytic activity`, IEA, `GO_REF:0000119`): **TOO_GENERAL**. Entailed by `GO:0015668` (`type III site-specific deoxyribonuclease activity`) and `GO:0004386` (`helicase activity`).
- `GO:0004386` (`helicase activity`, IEA, `GO_REF:0000002` / `GO_REF:0000043` / `GO_REF:0000120`): **ACCEPT** (3 rows). `Res` contains conserved SF2 helicase motifs (Walker A `aa 328–335`, `DEPH` `aa 426–429`) that couple ATP hydrolysis to DNA translocation/sliding between target sites [PMID:11178902, PMID:15489417].
- `GO:0004518` (`nuclease activity`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0015668` (`type III site-specific deoxyribonuclease activity`).
- `GO:0004519` (`endonuclease activity`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0015668` (`type III site-specific deoxyribonuclease activity`).
- `GO:0005524` (`ATP binding`, IEA, `GO_REF:0000043` / `GO_REF:0000120`): **ACCEPT** (2 rows). `Res` binds and hydrolyzes ATP via its Walker A/B SF2 helicase domain; ATP hydrolysis is required for EcoP1I restriction cleavage [PMID:11178902].
- `GO:0009036` (`type II site-specific deoxyribonuclease activity`, IEA, `GO_REF:0000002` InterPro:IPR011335): **REMOVE**. Automated mapping from the structural `Restr_endonucl-II-like` PD-(D/E)xK fold (`IPR011335`); EcoP1I is the prototype **Type III** restriction endonuclease (`EC:3.1.21.5`, already annotated with `GO:0015668` `type III site-specific deoxyribonuclease activity`), not a Type II restriction enzyme [PMID:2837577, PMID:11178902, PMID:12654995].
- `GO:0009307` (`DNA restriction-modification system`, IEA, `GO_REF:0000002` / `GO_REF:0000043` / `GO_REF:0000117`): **ACCEPT** (3 rows). `Res` is the restriction subunit of the P1 EcoP1I Type III restriction-modification system that cleaves unmodified invading phage DNA [PMID:2837577, PMID:11178902, PMID:15489417].
- `GO:0015668` (`type III site-specific deoxyribonuclease activity`, IEA, `GO_REF:0000003` EC:3.1.21.5): **ACCEPT**. Core enzymatic activity of `Res` within the `Res2Mod2` holoenzyme (`EC:3.1.21.5`) [PMID:2837577, PMID:11178902, PMID:12654995].
- `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0015668` and `GO:0004386`.
