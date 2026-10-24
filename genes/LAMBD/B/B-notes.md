# B (P03710) - Portal protein B (gpB)

## Summary
- **Gene symbol**: `B`
- **UniProt ID**: `P03710`
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Protein**: Portal protein B (`gpB`, 533 aa; processed to `gpB*`, residues 23-533, by prohead protease `gpC`)

## Biological Function
- Assembles into a 12-fold rotationally symmetric ring-shaped homododecamer (preconnector / portal complex) with a central axial channel localized at a single unique five-fold vertex of the icosahedral procapsid [PMID:6232391, file:LAMBD/B/B-uniprot.txt].
- During procapsid maturation, approximately 75-90% of `gpB` molecules in the portal ring are proteolytically cleaved by the prohead protease `gpC` to remove the N-terminal 22 residues, yielding mature `gpB*` [PMID:20620152, file:LAMBD/B/B-uniprot.txt].
- Serves as the central conduit and docking vertex for: (1) procapsid nucleation/assembly with host GroEL/GroES chaperonins, (2) docking of the terminase (`gpA`/`gpNu1`) motor and translocation of dsDNA into the capsid, (3) assembly of the neck adaptor rings (`gpW` and `gpFII`) and tail attachment, and (4) conduit for viral dsDNA ejection through the long flexible tail into the host cell during infection [PMID:6232391, PMID:20620152, PMID:20660769, file:LAMBD/B/B-uniprot.txt].

## Curation Decisions
- **ACCEPT**:
  - `GO:0046798` (`viral portal complex`, IDA `PMID:6232391`, IEA `GO_REF:0000104`)
  - `GO:0005198` (`structural molecule activity`, IEA `GO_REF:0000120`)
  - `GO:0003677` (`DNA binding`, IEA `GO_REF:0000043`)
  - `GO:0019028` (`viral capsid`, IEA `GO_REF:0000043`)
  - `GO:0099001` (`symbiont genome ejection through host cell envelope, long flexible tail mechanism`, IEA `GO_REF:0000120`)
- **MODIFY**:
  - `GO:0019068` (`virion assembly`, IEA `GO_REF:0000120`) -> `GO:0019069` (`viral capsid assembly`)
  - `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`) -> `GO:0099001` (`symbiont genome ejection through host cell envelope, long flexible tail mechanism`)
