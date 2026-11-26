# Gene 5 (gp5) Curation Notes — Bacteriophage T4 (P16009)

## Overview
- **Gene symbol**: `5` (encodes pre-baseplate central spike protein gp5 / peptidoglycan hydrolase gp5)
- **UniProt accession**: `P16009`
- **Organism**: *Tequatrovirus T4* (Bacteriophage T4; `NCBITaxon:10665`)

## Biological Role and Architecture
- **Central spike complex**: Three copies of gp5 assemble with a trimer of gp27 and one copy of the tip protein gp5.4 at the center of the T4 baseplate hub to form the `(gp27-gp5*-gp5C)3-gp5.4` cell-puncturing needle complex (`file:BPT4/5/5-uniprot.txt`; `file:BPT4/5/5-deep-research-falcon.md`).
- **Domain organization and maturation**: Full-length gp5 (575 aa, ~63 kDa) consists of three domains:
  1. An N-terminal OB-fold / antiparallel beta-barrel domain (residues 1–129) that inserts into the trimeric gp27 cylinder (`file:BPT4/5/5-deep-research-falcon.md`, PubMed 11823865).
  2. A middle T4-type lysozyme (N-acetylmuramidase, EC 3.2.1.17) domain (residues 174–339) that hydrolyzes the beta-1,4-glycosidic bond between N-acetylmuramic acid (NAM) and N-acetylglucosamine (NAG) in the host periplasmic peptidoglycan layer (`file:BPT4/5/5-deep-research-falcon.md`, PubMed 3157805).
  3. A C-terminal triple-stranded beta-helix domain (gp5C, residues 389–575) that forms a rigid equilateral triangular prism ("molecular needle") (`file:BPT4/5/5-deep-research-falcon.md`, PubMed 11823865).
- **Maturation cleavage and zymogen regulation**: During virion assembly, gp5 undergoes maturation cleavage between Ser351 and Ala352 into N-terminal mature tail lysozyme gp5* (~43 kDa) and C-terminal beta-helix gp5C (~20 kDa), both of which remain associated in the baseplate prior to infection (`file:BPT4/5/5-uniprot.txt`, PubMed 10217762, PubMed 15701513). In the pre-infection state, a linker loop from an adjacent gp5 subunit occludes the lysozyme active site, inhibiting muramidase activity until outer membrane penetration releases the gp5C needle (`file:BPT4/5/5-deep-research-falcon.md`, PubMed 15701513).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0003796` (`lysozyme activity`, IEA/EXP/IMP/IDA): Directly demonstrated N-acetylmuramidase activity of the middle domain (PubMed 3157805, PubMed 10217762, PubMed 15701513).
  - `GO:0009253` (`peptidoglycan catabolic process`, IEA): Accurately captures the enzymatic cleavage of host cell wall peptidoglycan.
  - `GO:0098932` (`symbiont entry into host cell via disruption of host cell wall peptidoglycan`, IEA): Core biological process describing the role of gp5 during phage infection.
  - `GO:0098003` (`viral tail assembly`, IEA): Essential hub component required for baseplate and tail morphogenesis.
  - `GO:0098025` (`virus tail, baseplate`, IEA/IDA): Directly resolved in the central spike of the baseplate by X-ray crystallography and cryo-EM (PubMed 27193680).
- **KEEP_AS_NON_CORE**:
  - `GO:0005515` (`protein binding`, IPI with gp27 `P13325`) and `GO:0042802` (`identical protein binding`, IPI): Valid structural interactions within the `(gp27-gp5)3` complex, retained as non-core binding terms.
- **MODIFY**:
  - Broad catalytic terms (`GO:0003824` `catalytic activity`, `GO:0016787` `hydrolase activity`, `GO:0016798` `hydrolase activity, acting on glycosyl bonds`) -> `GO:0003796` (`lysozyme activity`).
  - `GO:0016998` (`cell wall macromolecule catabolic process`) -> `GO:0009253` (`peptidoglycan catabolic process`).
  - Broad entry terms (`GO:0044409` `symbiont entry into host`, `GO:0046718` `symbiont entry into host cell`, `GO:0098994` `symbiont entry into host cell via disruption of host cell envelope`) -> `GO:0098932` (`symbiont entry into host cell via disruption of host cell wall peptidoglycan`).
  - `GO:0098015` (`virus tail`) -> `GO:0098025` (`virus tail, baseplate`).
- **REMOVE**:
  - `GO:0031640` (`killing of cells of another organism`, IEA) and `GO:0042742` (`defense response to bacterium`, IEA): Spurious automated keyword mappings from `Antimicrobial` / `Bacteriolytic enzyme`. Unlike host antimicrobial lysozymes or the phage endolysin gpE (which lyses the host at the end of the lytic cycle), gp5 performs localized cell-envelope puncturing and peptidoglycan digestion to enable genome injection without lysing the host cell during normal single-hit infection.
