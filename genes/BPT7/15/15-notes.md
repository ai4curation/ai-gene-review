# BPT7 gene 15 (gp15, P03725) — Curation Notes

## Summary of Function
Bacteriophage T7 internal virion protein gp15 (`P03725`, 747 AA) is the middle component of the coaxial internal core cylinder (`gp14`–`gp15`–`gp16`) stacked on the gp8 portal inside the mature T7 head [PMID:6864790, PMID:23306440]. Upon receptor engagement and tail opening, unfolded/partially unfolded gp15 subunits are ejected through the portal-tail channel and refold in the host periplasm into a 210-Å-long hexameric periplasmic DNA-conducting tunnel (inner diameter ~24–35 Å) that bridges the gp14 outer membrane pore to the gp16 inner membrane hub [PMID:23306440, PMID:34214465]. The cryo-EM structure of the gp15–gp16-N complex at 2.7 Å resolution (`PMID:34214465`) shows that hexameric gp15 forms a smooth, electrostatically negative/neutral DNA-binding conduit across the host periplasmic space and lacks membrane-inserting domains.

## Annotation Review
- `GO:0044229` (`host cell periplasmic space`, `IEA` `GO_REF:0000044` `[UniProtKB-SubCell:SL-0420]`): **ACCEPT**.
- `GO:0044384` (`host outer membrane`, `EXP`, `PMID:34214465`): **MODIFY** to `GO:0044229` (`host cell periplasmic space`). In `PMID:34214465` ("Cryo-EM structure of the periplasmic tunnel of T7 DNA-ejectosome at 2.7 A resolution"), gp14 is shown to form the outer membrane pore, whereas gp15 is a soluble protein that lacks lipid bilayer insertion activity and forms the 210-Å-long hexameric tunnel spanning the host periplasmic space.
- `GO:0039678` (`symbiont genome ejection through host cell envelope`, `IEA` `GO_REF:0000002`) and `GO:0046718` (`symbiont entry into host cell`, `IEA` `GO_REF:0000043`): **MODIFY** to `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`).
- `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, `IEA` `GO_REF:0000120`): **ACCEPT**.
- **Proposed `NEW` annotations**:
  - `GO:0044423` (`virion component`, `IDA`, `PMID:23306440`): gp15 forms the middle ring of the cylindrical internal core inside the mature T7 virion head.
  - `GO:0003677` (`DNA binding`, `IDA`, `PMID:34214465`): Electrophoretic mobility shift assays in Swanson et al. (2021) demonstrate that hexameric gp15 binds double-stranded DNA inside its central channel.
