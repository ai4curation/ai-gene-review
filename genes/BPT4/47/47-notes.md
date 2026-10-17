# Curation Notes: Bacteriophage T4 `47` (Exonuclease subunit 1 / Mre11 homolog gp47, P04521)

## Overview
- **Gene symbol:** `'47'` (gp47)
- **UniProt ID:** `P04521` (`EXO1_BPT4`)
- **Length:** 339 amino acids
- **Function:** Mre11-family calcineurin-like metallophosphoesterase nuclease subunit of the heterotetrameric T4 Mre11-Rad50 (`gp47(2)-gp46(2)`) DNA end-processing complex required for double-strand break (DSB) repair, homologous recombination, recombination-dependent DNA replication (RDR), and degradation of cytosine-containing host chromosomal DNA.

## Biological Role and Mechanism
- gp47 contains a conserved N-terminal calcineurin-like metallophosphoesterase domain (`PF00149` / `IPR004843`) that coordinates divalent metal ions at the nuclease active site.
- Together with gp46 (the Rad50-family ABC ATPase subunit), gp47 forms the T4 MR complex (`gp46(2)-gp47(2)`).
- Biochemically, gp47 provides the nuclease active site for Mn2+-dependent single-stranded DNA endonuclease activity and ATP/gp46-stimulated double-stranded DNA exonuclease activity (up to ~7.7 nucleotides/s, removing ~4 nucleotides per ATP hydrolyzed by gp46).
- In the presence of the single-stranded DNA-binding protein gp32 and the recombination mediator UvsY, the T4 MR complex switches to a Mg2+-dependent endonucleolytic/exonucleolytic resection mode that generates 15-25 nt oligonucleotide products and 3' single-stranded DNA tails for UvsX recombinase loading.
- In vivo, gp47 is essential alongside gp46 for DSB repair, homologous recombination, RDR, and step-two exonucleolytic degradation of fragmented cytosine-containing host chromosomal DNA into mononucleotides (PubMed 4305016, PubMed 4886654, PubMed 7026800).

## Review of Existing GO Annotations
- `GO:0004527` (exonuclease activity, IEA, GO_REF:0000043): **ACCEPT**. Core catalytic activity of gp47 within the T4 MR complex.
- `GO:0004518` (nuclease activity, IEA, GO_REF:0000043) & `GO:0016787` (hydrolase activity, IEA, GO_REF:0000120): **MODIFY** to `GO:0004527` (exonuclease activity).
- `GO:0003677` (DNA binding, IEA, GO_REF:0000043): **ACCEPT**. gp47 directly binds ssDNA and dsDNA substrates at its metallophosphoesterase active site and allosterically stimulates gp46 ATPase activity upon DNA binding.
- `GO:0006281` (DNA repair, IEA, GO_REF:0000043) & `GO:0006974` (DNA damage response, IEA, GO_REF:0000043): **MODIFY** to `GO:0006302` (double-strand break repair), which more specifically describes the role of gp47 in resecting DSB ends during recombinational repair.
- `GO:0099015` (degradation of host chromosome by virus, IEA, GO_REF:0000043): **ACCEPT**. Mutants in gene 47 fail to degrade endonuclease-cleaved host chromosomal DNA into acid-soluble nucleotides (PubMed 4305016).
- `GO:0039657` (symbiont-mediated suppression of host gene expression, IEA, GO_REF:0000043): **REMOVE**. Automated UniProt keyword mapping artifact (`Host gene expression shutoff by virus`); gp47 participates in host DNA degradation after endonucleolytic cleavage rather than transcriptional or translational host shutoff.
