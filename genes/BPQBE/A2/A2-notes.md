# BPQBE A2 (Maturation protein A2 / Q8LTE2) Notes

## Overview
- **Gene symbol**: `A2`
- **UniProt ID**: `Q8LTE2` (`MATA2_BPQBE`)
- **Organism**: Qubevirus durum / Escherichia virus Qbeta (`NCBITaxon:39803`)
- **Protein**: Maturation protein A2 (MP, A2 protein), 420 amino acids.

## Dual Biological Function: Virion Maturation/Attachment & Host Lysis
- **Single-copy capsid maturation and F-pilus receptor attachment**: A single copy of `A2` is incorporated into each Qbeta virion (`GO:0039617`), replacing a coat protein (`cp`) dimer at a 2-fold axis. Its alpha-helical bundle binds the viral genomic ssRNA (`GO:0003723`) and an internalized coat protein dimer in the virion interior, while its exposed beta-region mediates phage attachment to the host *Escherichia coli* F-pilus (`GO:0039666`) and subsequent genome entry (`GO:0046718`) ([PMID:27671640]; [PMID:29078304]; [file:BPQBE/A2/A2-uniprot.txt]).
- **"Protein antibiotic" lysis mechanism via MurA inhibition**: Unlike MS2 (which encodes a separate membrane-targeted `L` protein), Qbeta lacks a dedicated lysis gene and instead uses `A2` as a dual-function lysis protein ([PMID:11892805]). Once sufficient `A2` is synthesized (and incorporated into virions), the outer surface of its beta-region binds specifically to the closed, substrate-liganded conformation of host UDP-N-acetylglucosamine 1-carboxyvinyltransferase (`MurA`), the enzyme catalyzing the committed first step of peptidoglycan biosynthesis (`GO:0039635`, `GO:0039640`, `GO:0044659`) ([PMID:11423662]; [PMID:29078304]).

## Curation Decisions
- **ACCEPT**:
  - `GO:0039635` (`symbiont-mediated suppression of host peptidoglycan biosynthetic process`, IDA from PMID:11423662): Directly shown by in vivo blockage of murein precursor synthesis and in vitro inhibition of purified MurA by Qbeta A2.
  - `GO:0039640` (`viral release via suppression of host peptidoglycan biosynthetic process`, IDA from PMID:11423662): Directly captures Qbeta's single-gene lysis mechanism via MurA inhibition.
  - `GO:0039666` (`virion attachment to host cell pilus`, IEA from GO_REF:0000120): Core receptor-binding function of A2 on the host F-pilus.
  - `GO:0046718` (`symbiont entry into host cell`, IEA from GO_REF:0000043): A2 mediates delivery of the genomic RNA into the host cell upon F-pilus adsorption.
- **MODIFY**:
  - `GO:0019062` (`virion attachment to host cell`, IEA from GO_REF:0000043) -> `GO:0039666` (`virion attachment to host cell pilus`).
  - `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`, IEA from GO_REF:0000043) -> `GO:0039666` (`virion attachment to host cell pilus`).
  - `GO:0031640` (`killing of cells of another organism`, IEA from GO_REF:0000043) -> `GO:0039640` (`viral release via suppression of host peptidoglycan biosynthetic process`).
  - `GO:0044659` (`viral release from host cell by cytolysis`, IMP from PMID:11892805) -> `GO:0039640` (`viral release via suppression of host peptidoglycan biosynthetic process`), the more specific descendant term already present on this gene.
  - `GO:0039636` (`symbiont-mediated suppression of host cell wall biogenesis`, IDA from PMID:11423662 and PMID:29078304) -> `GO:0039635` (`symbiont-mediated suppression of host peptidoglycan biosynthetic process`), the more specific descendant term already present on this gene.
