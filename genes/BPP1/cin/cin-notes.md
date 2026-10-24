# cin (P10311) — Curation Notes

## Summary
- **Gene symbol**: `cin`
- **UniProtKB**: `P10311` (`CIN_BPP1`, 186 aa, 21.2 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Serine site-specific DNA invertase Cin ("C-segment inversion"). Catalyzes conservative site-specific inversion of the 4.2-kb P1 C-segment flanked by 0.6-kb inverted repeats carrying 26-bp `cixL` and `cixR` crossover sites at their outer borders. Operates via a transient `O-(5'-phospho-DNA)-serine` covalent intermediate at active-site Ser-9 and is stimulated by host `E. coli` Fis protein binding to a recombinational enhancer embedded within the `cin` coding sequence. Inversion switches the C-terminal variable region of the tail fiber gene `S` (and companion chaperone gene `U`) between two alternative configurations (`Sc-Sv-U` in C(+) orientation vs `Sc-Sv'-U'` in C(-) orientation), thereby switching phage receptor specificity and bacterial host range (tropism).

## Literature Evidence
- **Hiestand-Nauer & Iida 1983 (`PMID:6315399`)**:
  - Sequenced the `cin` gene (`X01828`, 186 codons), the crossover sites `cixL` and `cixR`, and the adjacent inverted repeat ends of the invertible C-segment determining P1 host range.
  - Quote: `"The bacteriophage P1 carries the invertible DNA segment C which appears closely related to the invertible G area of phage Mu and which is known to determine phage host range."`
  - Quote: `"Site-specific inversion occurs between the survival crossover sites cixL and cixR localized at the outside ends of the inverted repeats."`
- **Huber, Iida, Arber & Bickle 1985 (`PMID:6327269` / `PMID:2995817` in UniProt)**:
  - Note: Cached `PMID_6327269.md` in `publications/` is a different 1984 paper, so we do not cite `PMID:6327269` in `supported_by`.
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Detailed the mechanism and biological role of Cin: Cin acts on the inverted 26-bp `cixL` and `cixR` crossover sites flanking the 4.2-kb C-segment (with assistance from host Fis binding a cis-acting enhancer inside `cin`) to invert the C-segment and fuse the constant 5' portion of the tail fiber gene (`Sc`) to either `Sv` or `Sv'`, switching phage host range.
  - Quote: `"Inversion of the C segment is accomplished by the Cin site-specific recombinase, the only product of an operon that adjoins the C segment on the opposite side from Sc"`
  - Quote: `"Cin acts on a pair of inverted 26-bp crossover sites, cix L and cix R, at the C-segment borders"`
- **UniProtKB `P10311` (`file:genes/BPP1/cin/cin-uniprot.txt`)**:
  - Quote: `"This protein catalyzes the inversion of the 4.2-kb C-segment of looking-glass DNA, which controls the host range of phage P1 by switching the synthesis of two different sets of tail fiber proteins."`

## Annotation Review Decisions
- `GO:0000150` (`DNA strand exchange activity`, IEA: `GO_REF:0000120`): **ACCEPT**. Cin is a serine site-specific recombinase (invertase) that catalyzes DNA cleavage and strand exchange between the 26-bp `cixL` and `cixR` sites via active-site Ser-9 (`PMID:6315399`, `PMID:15489417`).
- `GO:0003677` (`DNA binding`, IEA: `GO_REF:0000120`): **MODIFY** to `GO:0043565` (`sequence-specific DNA binding`). Cin specifically binds the 26-bp `cixL` and `cixR` crossover sequences via its C-terminal helix-turn-helix domain (residues 162-181) (`PMID:6315399`, `PMID:15489417`).
- `GO:0006310` (`DNA recombination`, IEA: `GO_REF:0000120`): **ACCEPT**. Cin catalyzes site-specific DNA inversion (recombination) of the 4.2-kb C-segment (`PMID:6315399`, `PMID:15489417`).
- `GO:0015074` (`DNA integration`, IEA: `GO_REF:0000043`): **REMOVE**. Keyword mapping artifact from `KW-0229 DNA integration`. Cin is a DNA invertase that catalyzes intramolecular inversion of the P1 C-segment; it does not integrate viral DNA into the host genome (`PMID:6315399`, `PMID:15489417`).
- `GO:0046718` (`symbiont entry into host cell`, IEA: `GO_REF:0000043`): **REMOVE**. Keyword mapping artifact from `KW-1160 Virus entry into host cell`. Cin is an intracellular site-specific DNA recombinase that switches expression of alternate tail fiber genes (`Sv` vs `Sv'`), not a virion structural component that directly mediates entry into the host cell (`PMID:15489417`).
- `GO:0098678` (`viral tropism switching`, IEA: `GO_REF:0000043`): **ACCEPT**. By catalyzing inversion of the C-segment between `cixL` and `cixR`, Cin switches expression between alternate tail fiber C-terminal regions (`Sv-U` vs `Sv'-U'`), directly driving viral tropism (host range) switching (`PMID:6315399`, `PMID:15489417`).
