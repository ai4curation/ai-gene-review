# Curation Notes: Pseudomonas phage phiKZ `EXLYS` (`gp181`, UniProt `Q8SCY1`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `EXLYS` (`gp181`, `PHIKZ181`)
- **Organism**: *Pseudomonas phage phiKZ* (`NCBITaxon:2905945`), giant myovirus infecting *Pseudomonas aeruginosa*.
- **UniProt Accession**: `Q8SCY1` (2,237 AA, ~245.8 kDa).
- **Domains**: Contains a soluble lytic murein transglycosylase (`SLT`) / lysozyme-like domain (`Pfam:PF01464`, `InterPro:IPR008258`, `InterPro:IPR023346`) near its C-terminus (`residues 1879–2029`).

## Molecular Function & Role in Viral Entry
- **Virion-Associated Peptidoglycan Hydrolase (Exolysin)**: `gp181` (`EXLYS`) is a giant structural protein of the phiKZ tail/baseplate cell-puncturing apparatus (`~5 copies per virion`) that locally degrades the host *Pseudomonas aeruginosa* cell wall peptidoglycan during phage infection to allow tail tube penetration and viral DNA injection (`GO:0098932`, `symbiont entry into host cell via disruption of host cell wall peptidoglycan`) [PMID:18671939, file:BPDPK/EXLYS/EXLYS-uniprot.txt].
- **Biochemical Characterization**: Deletion mapping of nine recombinant truncations defined the minimal peptidoglycan hydrolase catalytic domain between `residues 1880–2042` (`gp181M8`), while inclusion of the C-terminal distal segment (`residues 2043–2237`) enhances specific muralytic activity 3-fold to 12 times that of commercial hen egg-white lysozyme [PMID:18671939]. The enzyme displays an optimum pH of 6.2 and retains activity at ionic strengths above 320 mM [PMID:18671939, file:BPDPK/EXLYS/EXLYS-uniprot.txt].

## Curation Decisions
- **MODIFY**: `GO:0003824` (`catalytic activity`, IEA from `GO_REF:0000043`) -> `proposed_replacement_terms: [{id: GO:0008933, label: peptidoglycan lytic transglycosylase activity}]` (or `GO:0003796` `lysozyme activity`). Because `gp181` contains a canonical SLT transglycosylase / lysozyme-like peptidoglycan hydrolase domain (`Pfam:PF01464`, `IPR008258`) experimentally shown to cleave bacterial peptidoglycan (`PMID:18671939`), `GO:0003824` is too general and should be refined to `GO:0008933` (`peptidoglycan lytic transglycosylase activity`).
- **ACCEPT**: `GO:0098932` (`symbiont entry into host cell via disruption of host cell wall peptidoglycan`).
- **TOO_GENERAL**: `GO:0044409` (`symbiont entry into host`), `GO:0046718` (`symbiont entry into host cell`), and `GO:0098994` (`symbiont entry into host cell via disruption of host cell envelope`), all entailed by `GO:0098932`.
- **REMOVE**:
  - `GO:0031640` (`killing of cells of another organism`, IEA from `KW-0081` Bacteriolytic enzyme): `gp181` is a virion-associated entry exolysin that locally punctures the peptidoglycan sacculus during infection without lysing the host cell (unlike the endolysin `gp144` / `PHIKZ144`).
  - `GO:0042742` (`defense response to bacterium`, IEA from `KW-0081` Antimicrobial): Automated keyword artifact; bacteriophages do not mount a host immune defense response against bacteria.
