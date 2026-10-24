# Curation Notes: Pseudomonas phage phiKZ `PRO` (`gp175`, UniProt `Q8SCY7`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `PRO` (`gp175`, `PHIKZ175`, Capsid maturation protease)
- **Organism**: *Pseudomonas phage phiKZ* (`NCBITaxon:2905945`), giant myovirus infecting *Pseudomonas aeruginosa*.
- **UniProt Accession**: `Q8SCY7` (270 AA zymogen precursor, ~29.7 kDa; auto-cleaved after `Glu210` to a 210 AA mature enzyme + 60 AA C-terminal propeptide; EC `3.4.21.-`).
- **Classification**: Prototype member of MEROPS peptidase family `S80` (`S80.001`, `Pfam:PF20034` `Peptidase_S80`), distantly related to bacteriophage T4 prohead protease `gp21` (`S21`) and herpesvirus assemblin (`S21`) [PMID:22429790, PMID:23740980].

## Molecular Function & Role in Prohead and Inner Body Maturation
- **Serine-Type Prohead Endopeptidase (`His89`, `Ser168`, `Glu191`)**: `gp175` (`PRO`) possesses a conserved catalytic triad comprising `His89`, `Ser168`, and `Glu191` [PMID:22429790, PMID:23740980]. Synthesized as a 270-residue precursor, `gp175` undergoes autonomous C-terminal self-cleavage autoactivation at `Ser208-Leu209-Glu210 / Ala211` (`S-X-E` motif) to yield the active 210-residue mature protease [PMID:22429790, PMID:23740980]. Alanine substitution of either `His89` (`H89A`) or `Ser168` (`S168A`) completely abolishes both C-terminal self-cleavage and trans-cleavage of purified head substrates (`gp93` and `gp89`) in vitro [PMID:23740980].
- **Extensive Proteolysis of Prohead and Inner Body Proteins**: Mass spectrometry (`GeLC-MS/MS`, N-terminal dimethyl labeling, and TOF-MS) identified 39 cleavage sites across 19 of the 49 phiKZ head proteins, all conforming to a strict `[S/A/G]-X-E` consensus motif (where cleavage occurs exclusively C-terminal to `Glu`, with `Ser`, `Ala`, or `Gly` at P3) [PMID:22429790]. Substrates include:
  - The major capsid protein `gp120` (`CAPSD`, cleaved at 7 sites up to `Glu163` to remove its 163-AA N-terminal propeptide) and minor head protein `gp146` [PMID:22429790].
  - All five major proteins of the cylindrical "inner body" (`IB`: `gp89`, `gp90`, `gp93`, `gp95`, `gp97`) and low-abundance IB/head proteins (`gp92`, `gp94`, `gp96`, `gp98`, `gp153`, `gp162`, `gp163`, `gp177`, `gp184`, `gp203`, `gp303`) [PMID:22429790, PMID:23740980].
  - `gp175` itself (`Glu210-Ala211`, removing the 60-AA C-terminal propeptide, after which only ~70 molecules of mature `gp175` remain in the mature head) [PMID:22429790, PMID:23740980].

## Curation Decisions
- **ACCEPT**: `GO:0008236` (`serine-type peptidase activity`, IEA from `GO_REF:0000043`), `GO:0019082` (`viral protein processing`, IDA from `PMID:22429790`), and `GO:0046797` (`viral procapsid maturation`, IEA from `GO_REF:0000043`).
- **TOO_GENERAL**: `GO:0008233` (`peptidase activity`, entailed by `GO:0008236`), `GO:0016787` (`hydrolase activity`, entailed by `GO:0008236`), and `GO:0006508` (`proteolysis`, entailed by `GO:0019082`).
