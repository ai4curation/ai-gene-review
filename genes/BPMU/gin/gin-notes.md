# Curation Notes for gin (P03015) — Phage Mu Serine recombinase gin (G-segment invertase / Mup53)

## Biological Summary
- **Gene / Protein**: `gin` (Ordered locus name `Mup53`; UniProt `P03015`, 193 aa; also designated `Gin` or `gp53`).
- **Structure and Function**:
  - Prototype member of the resolvase/invertase family of serine site-specific recombinases (`Pfam:PF00239` `Resolvase` N-terminal catalytic domain residues 1–134 with catalytic nucleophile `Ser-9`, and `Pfam:PF02796` `HTH_7` C-terminal helix-turn-helix DNA-binding domain residues 138–183; `PDB:3UJ3`, `PDB:4M6F`).
  - Catalyzes site-specific DNA inversion of the viral 3-kb `G-segment` flanked by inverted 34-bp palindromic `gix` recombination sites (`gixL` and `gixR`) in the presence of the *Escherichia coli* host factor `Fis` bound to the recombinational enhancer sequence (`file:BPMU/gin/gin-uniprot.txt`).
  - Within the synaptic tetramer, each of the four Gin monomers introduces a single-strand cleavage and forms a transient covalent `O-(5'-phospho-DNA)-serine` intermediate at `Ser-9` (`FT   ACT_SITE 9`), followed by a 180° subunit rotation of one dimer relative to the other and religation of the DNA strands (`file:BPMU/gin/gin-uniprot.txt`).
  - Inversion between the `G(+)` and `G(-)` orientations alternates expression between the `S-U` (`Mup49-Mup50`) and `S'-U'` (`Mup52-Mup51`) tail fiber gene pairs, switching viral host range (`GO:0098678` viral tropism switching).

## Annotation Decisions
- **ACCEPT**:
  - `GO:0003677` (`DNA binding`): Binds specifically as a homodimer via its C-terminal HTH motif (`residues 138–183`) to the 34-bp palindromic `gix` recombination sites.
  - `GO:0006310` (`DNA recombination`): Catalyzes site-specific recombinational inversion of the 3-kb G-segment.
  - `GO:0098678` (`viral tropism switching`): Inversion of the G-segment switches expression between S-U and S'-U' tail fibers, altering the host specificity of phage Mu.
  - `GO:0030430` (`host cell cytoplasm`): Acts in the host bacterial cytoplasm where phage DNA replication/recombination and late gene expression occur.
- **MODIFY**:
  - `GO:0000150` (`DNA strand exchange activity`), `GO:0016787` (`hydrolase activity`), and `GO:0016874` (`ligase activity`) -> `MODIFY` with `proposed_replacement_terms: [{id: GO:0009009, label: site-specific recombinase activity}]`:
    - `GO:0000150` is a parent term of `GO:0009009` (`site-specific recombinase activity`), while `GO:0016787` and `GO:0016874` are broad IEA keyword mappings derived from the dual partial EC numbers (`EC 3.1.22.-` and `EC 6.5.1.-`) assigned to serine recombinases to represent the cleavage and religation half-reactions of a single concerted transesterification mechanism via `Ser-9`. In GO, this unified catalytic activity is precisely represented by `GO:0009009` (`site-specific recombinase activity`).
- **REMOVE**:
  - `GO:0015074` (`DNA integration`): False-positive UniProt keyword mapping (`KW-0229`). Phage Mu chromosomal integration and replicative transposition are catalyzed by the DDE-family transposase `MuA` (`P07636`), whereas `Gin` exclusively catalyzes intramolecular inversion of the internal 3-kb G-segment.
  - `GO:0046718` (`symbiont entry into host cell`): Over-annotation from viral tropism keyword mapping (`KW-1160`). Gin is a cytoplasmic DNA invertase that never forms part of the virion or participates directly in host cell entry; the tail fiber proteins S and S' whose expression is toggled by Gin mediate attachment and entry.
