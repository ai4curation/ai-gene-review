# P5 (P07582) — Pseudomonas phage phi6

## Overview
- **Gene symbol**: P5
- **UniProt ID**: P07582 (`EXLYS_BPPH6`)
- **Product**: Peptidoglycan hydrolase gp5 (220 AA, 23.9 kDa), encoded on dsRNA segment S.

## Literature & Functional Evidence
- **Dual-function muralytic D-alanyl-D-alanine carboxypeptidase / endopeptidase (virion-associated exolysin and late endolysin)**:
  - Purified from disrupted phi6 virions as a ~24 kDa monomer that cleaves the peptide cross-bridge between meso-diaminopimelic acid and D-alanine in the Gram-negative host peptidoglycan layer [PMID:1390911, "The lytic enzyme of the lipid-containing bacteriophage phi 6, protein P5, has been purified to apparent homogeneity from disrupted viral particles. The enzyme is a monomer with a molecular mass of approx. 24 kDa."]; [PMID:1390911, "Analysis of cell wall digests indicates that P5 is not a glycosidase, but an endopeptidase splitting the peptide bridge formed by meso-diaminopimelic acid and D-alanine."].
  - Functions both during viral entry (located between the nucleocapsid and the envelope, exposed to the periplasmic peptidoglycan layer after P6-mediated outer membrane fusion to allow the nucleocapsid core to cross the cell wall) and late in infection (causing host cell lysis in conjunction with membrane proteins to release progeny virions) [file:BPPH6/P5/P5-uniprot.txt, "FUNCTION: Muralytic enzyme exposed to host peptidoglycan layer after membrane fusion during viral entry. Functions as an exolysin that cleaves the peptide bridge formed by meso-diaminopimelic acid and D-alanine. Also lyses the host cell late in infection to release the virions."]; [PMID:41574337, "Conversely, pJLC149 and pJLC150, which pair the lambda holin with phi6 endolysin (pJLC150 contains an optimized ribosome binding site) produced spherical cells, similar to pJLC155, indicative of PG degradation with the outer membrane remaining intact. These observations indicate that the phi6 endolysin is active in E. coli when paired with lambda holin"].

## Curation Decisions
- **ACCEPT**:
  - `GO:0061783` (`peptidoglycan muralytic activity`, IDA `PMID:41574337`): Core muralytic activity degrading the bacterial peptidoglycan sacculus (`PMID:1390911`, `PMID:41574337`).
  - `GO:0098932` (`symbiont entry into host cell via disruption of host cell wall peptidoglycan`, IEA): Specifically captures P5's virion-associated exolysin function during entry after outer membrane fusion.
  - `GO:0031640` (`killing of cells of another organism`, IEA): Captures P5's late-stage endolysin function in lysing the host bacterium to release progeny phage particles (`PMID:41574337`).
- **TOO_GENERAL**:
  - `GO:0016787` (`hydrolase activity`, IEA): Subsumed by `GO:0061783` (`peptidoglycan muralytic activity`).
  - `GO:0044409` (`symbiont entry into host`, IDA `PMID:1390911`), `GO:0046718` (`symbiont entry into host cell`, IEA), and `GO:0098994` (`symbiont entry into host cell via disruption of host cell envelope`, IEA): Subsumed by the more specific descendant term `GO:0098932` (`symbiont entry into host cell via disruption of host cell wall peptidoglycan`).
