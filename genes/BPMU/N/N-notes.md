# Curation Notes for N (P08557) — Phage Mu DNA circularization protein N (Mup43 / BH1)

## Biological Summary
- **Gene / Protein**: `N` (Ordered locus name `Mup43`; UniProt `P08557`, 498 aa), also referred to as baseplate hub protein 1 (`BH1`) in Buettner et al. 2016 ([PMID:27555589]).
- **Dual Function in Virion Assembly and Post-Ejection DNA Protection**:
  1. **Baseplate central hub subunit (`BH1`)**: Forms a trimeric complex with baseplate hub protein gp44 (`P` / `Mup44` / `BH2`) at a 3:3 stoichiometry before recruiting three dimeric `Mup46`/`Mup47`/`Mup48` baseplate wedges (3:3:6:6:6 stoichiometry overall) to assemble the phage Mu baseplate and initiate contractile tail assembly ([PMID:27555589], "We have shown that five proteins are required for baseplate assembly with BW1 (Mup46), BW2 (Mup47), and BW3 (Mup48) proteins comprising the baseplate wedge and BH1 (Mup43) and BH2 (Mup44) forming the central hub on which the wedges are recruited.").
  2. **Pilot / DNA circularization protein**: Co-injected with the phage Mu linear dsDNA genome into the host cell cytoplasm during infection, where it binds both ends of the ejected viral DNA to form a non-covalent circularized supercoiled protein-DNA complex (`GO:0003677` DNA binding, `GO:0099009` viral genome circularization) and shields the linear genome ends from degradation by host exonucleases (`GO:0099016` symbiont-mediated evasion of DNA end degradation by host; `file:BPMU/N/N-uniprot.txt`, "-!- FUNCTION: Required for tail assembly of phage Mu and responsible for circularizing the viral DNA after it has been ejected into the host cell. Following infection, the circularized DNA can be isolated as a supercoiled, non-covalent protein-DNA complex, in which the protein N is bound to the ends of the DNA. Protects linear double-stranded DNA of viral genome from host exonuclease degradation.").

## Annotation Decisions
- **ACCEPT**:
  - `GO:0003677` (`DNA binding`): Core function of protein N in binding viral genome ends after ejection into the host cytoplasm.
  - `GO:0099009` (`viral genome circularization`): Core function in non-covalently circularizing the injected linear Mu genome.
  - `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`): Core function in protecting linear viral dsDNA ends against host exonucleases (such as RecBCD).
  - `GO:0098003` (`viral tail assembly`): Essential baseplate hub component (`BH1` / `Mup43`) required for baseplate and tail assembly ([PMID:27555589]).
  - `GO:0030430` (`host cell cytoplasm`): Site where protein N is synthesized during late gene expression and where it acts after co-injection with viral DNA.
- **KEEP_AS_NON_CORE**:
  - `GO:0046718` (`symbiont entry into host cell`): Broad process term reflecting co-ejection of the baseplate-associated pilot protein with the genome into the host cell.
- **TOO_GENERAL**:
  - `GO:0052031` (`symbiont-mediated perturbation of host defense response`) and `GO:0052170` (`symbiont-mediated suppression of host innate immune response`): Both are ancestor terms entailed by the specific annotation `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`) already present on this gene.
- **NEW**:
  - `GO:0098025` (`virus tail, baseplate`, `located_in`) and `GO:0039660` (`structural constituent of virion`, `enables`): Directly demonstrated by [PMID:27555589] showing Mup43 (`BH1`) is an integral structural subunit of the phage Mu baseplate hub.
