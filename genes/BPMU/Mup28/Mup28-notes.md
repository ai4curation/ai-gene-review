# Curation Notes: Escherichia phage Mu `Mup28` (`Q9T1W6`, Probable terminase, large subunit gp28)

## Summary of Function
- **Product**: Terminase large subunit gp28 (`Mup28`, also known as `gpE` or `pacase, large subunit`, 551 aa, 62.6 kDa; `IPR012036`, `IPR027417`).
- **Role in Headful Packaging**: Bifunctional catalytic subunit of the phage Mu terminase complex (`GO:0098009`) that complexes with the `pac`-binding small subunit gp27 (`Mup27` / `gpD`) and docks at the dodecameric portal vertex (`H` / `gp29`). Possesses an N-terminal P-loop ATPase motor domain (`GO:0016887`, `GO:0015616`) that translocates viral and flanking host DNA into the empty procapsid and a `Mg2+`-dependent C-terminal endonuclease domain (`GO:0004519`, `GO:0000287`) that cleaves host DNA outside the left and right ends of integrated Mu DNA during headful genome packaging (`GO:0098006`) [PMID:14745593].

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0004519` (`endonuclease activity`, IEA): Core catalytic activity for initiation and headful termination cuts.
  - `GO:0030430` (`host cell cytoplasm`, IEA): Site of procapsid docking and DNA packaging.
- **TOO_GENERAL**:
  - `GO:0004518` (`nuclease activity`, IEA): Entailed by `GO:0004519` (`endonuclease activity`).
  - `GO:0016787` (`hydrolase activity`, IEA): Entailed by `GO:0004519` and `GO:0016887`.
- **REMOVE**:
  - `GO:0032359` (`provirus excision`, IEA): Spurious mapping from UniProt keyword `KW-1250` (`Viral genome excision`). Phage Mu packages integrated copies directly from the bacterial chromosome by headful cleavage without excising a provirus.
- **MODIFY**:
  - `GO:0046872` (`metal ion binding`, IEA) -> `GO:0000287` (`magnesium ion binding`): Refines to the specific divalent cation (`2 Mg2+` per subunit) required for catalysis.
- **NEW**:
  - `GO:0015616` (`DNA translocase activity`, `enables`), `GO:0016887` (`ATP hydrolysis activity`, `enables`), `GO:0098006` (`viral DNA genome packaging, headful`, `involved_in`), `GO:0098009` (`viral terminase, large subunit`, `part_of`).
