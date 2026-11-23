# Enterobacteria phage P4 `sid` (Capsid size-determining protein Sid, `P05461`)

## Identity & Genomic Context
- **UniProt**: `P05461` (`SID_BPP4`, 244 aa, ~27.3 kDa).
- **Locus**: First gene of the P4 late `sid-delta-psu` operon transcribed from the late promoter `Psid` ([PMID:6095206], [PMID:3295254], [PMID:2183201]).
- **Domains**: Coiled-coil / α-helical external capsid scaffolding protein (no InterPro or Pfam accession is cross-referenced in `sid-uniprot.txt`).

## Molecular Function & Biological Role
- Satellite phage P4 lacks genes for structural virion components and parasitizes the morphogenetic proteins of its helper phage P2 ([PMID:3295254], [PMID:7643390]).
- Whereas helper phage P2 normally assembles a large `T=7` icosahedral procapsid to package its ~33.5 kb genome, P4 redirects the P2 major capsid protein (`gpN`) and internal scaffolding protein (`gpO`) to assemble a much smaller `T=4` procapsid tailored to package the ~11.6 kb P4 genome ([PMID:7643390]).
- Cryo-electron microscopy and three-dimensional image reconstruction of P4 procapsids demonstrated that Sid (60 or 120 copies per procapsid) forms an external icosahedral scaffolding cage on the outside of the procapsid shell ([PMID:7643390]).
- Sid molecules form arches that contact `gpN` hexamers at the icosahedral 2-fold axes and self-associate as trimers over the icosahedral 3-fold axes, creating a continuous dodecahedral outer cage that constrains capsid curvature to the smaller `T=4` geometry ([PMID:7643390]).

## Curation Summary
- `existing_annotations` in the GOA stub is empty.
- Added `NEW` annotations supported by [PMID:7643390]:
  - `GO:0042802` (`identical protein binding`, `IDA`, [PMID:7643390]) for Sid homodimer/homotrimer self-association at the 2-fold and 3-fold axes of the external dodecahedral scaffold cage.
  - `GO:0019069` (`viral capsid assembly`, `IDA`, [PMID:7643390]) for its direct role as the external capsid-size-determining scaffolding protein in P4 procapsid assembly.
