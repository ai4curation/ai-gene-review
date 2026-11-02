# Bacteriophage P2 Gene old ( Overcoming lysogenization defect nuclease/ATPase; UniProt P13520)

## Overview
Gene **old** (*overcoming lysogenization defect*) of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes a 583-amino-acid (65.4 kDa; `UniProt:P13520`) Class 1 OLD family antiphage defense nuclease-ATPase (`PMID:2695400`, `PMID:7836278`, `PMID:32009148`). Expressed constitutively from the integrated P2 prophage (as well as during infection), Old mediates abortive infection that blocks the growth of superinfecting bacteriophage lambda (`Spi+` phenotype; plating efficiency $<10^{-6}$) and kills *Escherichia coli* `recB` and `recC` host mutants (`PMID:4913204`, `PMID:4884707`, `PMID:2695400`).
Architecturally, P2 Old comprises an N-terminal ABC-family ATPase domain (with Walker A `K37`, Walker B `D299`, D-loop `H306`, H-loop `H332`) coupled to a C-terminal Toprim two-metal-ion catalytic nuclease domain (`E398`, `E402`, `D453`, `D455`, `D541`, `E543`, `K550`) (`PMID:32009148`). Biochemically, purified Old exhibits 5'-to-3' exonuclease activity on double-stranded DNA as well as endonuclease/exonuclease activity on single-stranded DNA and RNA (`EC:3.1.11.3`), and both ATPase and Toprim nuclease active sites are strictly required in vivo (`PMID:7836278`, `PMID:32009148`).

## Key Literature & Experimental Evidence
- **PMID:4913204** (*Bacteriophage lambda; abortive infection of bacteria lysogenic for phage P2.*) & **PMID:4884707**:
  - Defined P2-mediated interference with phage lambda growth and killing of `recB`/`recC` mutants: `"The efficiency of plating of wild-type lambda on a host lysogenic for P2 is less than 10(-6), and only a small number of infected cells produce progeny phage."`
- **PMID:2695400** (*The P2 phage old gene: sequence, transcription and translational control.*):
  - Sequenced the `old` gene (583 aa): `"The old (overcoming lysogenization defect) gene product of bacteriophage P2 kills Escherichia coli recB and recC mutants and interferes with phage lambda growth"`
- **PMID:7836278** (*The old exonuclease of bacteriophage P2.*):
  - Purified MBP-Old and characterized its enzymatic activities: `"The Old protein fused to maltose-binding protein has exonuclease activity on double-stranded DNA as well as nuclease activity on single-stranded DNA and RNA. The direction of digestion of double-stranded DNA is from 5' to 3', and digestion initiates at either the 5'-phosphoryl or 5'-hydroxyl terminus. The nuclease is active on nicked circular DNA, degrades DNA in a processive manner, and releases 5'-phosphoryl mononucleotides."`
- **PMID:32009148** (*The full-length structure of Thermus scotoductus OLD defines the ATP hydrolysis properties and catalytic mechanism of Class 1 OLD family nucleases.*):
  - Mutated both the ABC ATPase and Toprim nuclease active-site residues in P2 Old and assayed in vivo function: `"We also demonstrate that mutants perturbing ATP hydrolysis or DNA cleavage in vitro impair P2 OLD-mediated killing of recBC-Escherichia coli hosts, indicating that both the ATPase and nuclease activities are required for OLD function in vivo."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0051908` (`double-stranded DNA 5'-3' DNA exonuclease activity`, EXP `PMID:7836278` and IEA `GO_REF:0000003`): **ACCEPT** both rows.
  - `GO:0004518` (`nuclease activity`, IEA), `GO:0004527` (`exonuclease activity`, IEA), `GO:0016787` (`hydrolase activity`, IEA): **MODIFY** to `GO:0051908` (`double-stranded DNA 5'-3' DNA exonuclease activity`) and `GO:0016887` (`ATP hydrolysis activity`).
  - `GO:0005524` (`ATP binding`, IEA): **ACCEPT**
  - `GO:0000166` (`nucleotide binding`, IEA): **MODIFY** to `GO:0005524` (`ATP binding`).
  - `GO:0046872` (`metal ion binding`, IEA): **ACCEPT** (two-metal-ion Toprim catalytic center and $\text{Mg}^{2+}$-ATPase; `PMID:32009148`).
  - `GO:0016887` (`ATP hydrolysis activity`): **NEW** supported by `PMID:32009148`.
- **Biological Process**:
  - `GO:0006308` (`DNA catabolic process`) and `GO:0051607` (`defense response to virus`): **NEW** supported by `PMID:7836278`, `PMID:4913204`, and `PMID:32009148`.
- **Cellular Component**:
  - `GO:0030430` (`host cell cytoplasm`): **NEW** supported by `PMID:32009148`.
