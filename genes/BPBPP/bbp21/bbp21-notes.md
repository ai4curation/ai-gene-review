# bbp21 (Bordetella phage BPP-1) — Curation Notes

## Overview
- **Gene symbol**: `bbp21`
- **UniProt ID**: `Q775C3` (`PORTL_BPBPP`)
- **Organism**: *Bordetella* phage BPP-1 (`NCBITaxon:2885909`)
- **Product**: Probable portal protein gp21 (`Bbp21`, Head-to-tail connector; 555 aa, ~61.6 kDa; `InterPro:IPR020991`, `Pfam:PF12236`)
- *(Note on gene nomenclature: In Bordetella phage BPP-1, the DGR accessory variability determinant `Avd` is encoded by `bbp7`, whereas `bbp21` (`Q775C3`) encodes the virion portal / head-to-tail connector protein gp21.)*

## Biological Function and Mechanism
- **Portal vertex / head-to-tail connector**: `bbp21` was identified in the complete genomic analysis of *Bordetella* phage BPP-1 (`Podoviridae` morphology, 42.4 kb dsDNA genome) as the gene encoding the head-tail connector (portal protein) [PMID:14973019]. It contains the conserved phage portal protein domain (`PF12236` / `IPR020991`, residues 119–454) [file:BPBPP/bbp21/bbp21-uniprot.txt].
- **Structural and assembly role**: As the portal protein of a short-tailed podovirus, `Bbp21` multimerizes into a ring-shaped homododecamer at one unique five-fold vertex of the icosahedral T=7 capsid, forming the axial channel required for procapsid nucleation, ATP-driven dsDNA packaging with the terminase complex (`Bbp27`/`Bbp28`), neck/tail attachment, and genome ejection across the *Bordetella* cell envelope [PMID:14973019; file:BPBPP/bbp21/bbp21-uniprot.txt].

## Curation Decisions
- **Existing annotations**:
  - `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IEA): `ACCEPT`. The portal channel of the short-tailed phage BPP-1 serves as the conduit through which packaged viral dsDNA exits the capsid into the tail assembly during genome ejection.
  - `GO:0046718` (`symbiont entry into host cell`, IEA): `TOO_GENERAL` (entailed by its descendant `GO:0099002` already present in this review).
