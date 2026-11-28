# Curation Notes: Escherichia phage Mu `Mup27` (`Q9T1W7`, Probable terminase, small subunit gp27)

## Summary of Function
- **Product**: Terminase small subunit gp27 (`Mup27`, also called `gpD` or `pacase, small subunit`, 191 aa, 21.6 kDa; `IPR021874` / `PF11985`).
- **Role in Headful Packaging**: Recognizes the phage Mu packaging initiation site (`pac`) near the left (`c`) end of the integrated Mu genome (`GO:0003677`) and heterooligomerizes with the large terminase subunit gp28 (`Mup28` / `gpE`) to form the terminase complex (`GO:0097710`) at the portal vertex (`H` / `gp29`) of the procapsid (`PMID:14745593`). Directs the initial endonucleolytic cleavage ~50-150 bp into the flanking host DNA and regulates the ATP-driven translocation activity of gp28 during headful DNA packaging (`GO:0098006`).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0003677` (`DNA binding`, IEA): Core function in recognizing the viral `pac` sequence (`PMID:14745593`).
  - `GO:0030430` (`host cell cytoplasm`, IEA): Site of viral genome packaging in the bacterial host.
- **REMOVE**:
  - `GO:0032359` (`provirus excision`, IEA): Spurious mapping from UniProt keyword `KW-1250` (`Viral genome excision`). Phage Mu replicates via replicative transposition and packages dispersed copies directly out of the host chromosome (including flanking host DNA at both ends) without ever excising a provirus.
- **NEW**:
  - `GO:0098006` (`viral DNA genome packaging, headful`, `involved_in`, `PMID:14745593`).
  - `GO:0097710` (`viral terminase, small subunit`, `part_of`, `PMID:14745593`).
