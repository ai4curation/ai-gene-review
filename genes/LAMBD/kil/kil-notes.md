# kil (P03758) - Curation Notes

## Overview
- **Gene symbol**: `kil`
- **UniProt ID**: `P03758` (`KIL_LAMBD`)
- **Protein name**: Protein kil (Host-killing protein, 89 AA; note: the active FtsZ-inhibiting Kil peptide is also characterized as a 47-AA polypeptide encoded in the `cIII`-`gam` interval of the `PL` operon)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Inhibitor of host cell division (septation)**: The `kil` gene is located in the delayed-early leftward (`PL`) operon between `cIII` and `gam` [PMID:6458018, "The sequence thus includes the genes, N, ral, Ea10, cIII, kil and gam, as well as the transcription terminators TL1 and TL2."]. Expression of `kil` inhibits *Escherichia coli* cell division (septum formation), causing infected cells to grow as elongated filaments and delaying host lysis while increasing burst size.
- **Direct inhibition of FtsZ ring assembly**: Lambda Kil interacts with the essential bacterial tubulin-like cytokinesis protein FtsZ (in a manner requiring the membrane anchor ZipA in vivo) to disrupt GTP-dependent FtsZ protofilament bundling and Z-ring assembly at midcell, blocking cytokinesis during lytic infection [PMID:24651041, "An affinity-tagged-Kil derivative interacts with both FtsZ and ZipA, and inhibits sedimentation of FtsZ filament bundles in vitro."].

## Review of Existing GO Annotations
- `kil` currently has **no existing GO annotations** in GOA (`existing_annotations: []`).
- We document its location in the `PL` operon (`PMID:6458018`, `PMID:6221115`) and its role in inhibiting host bacterial cell division (`PMID:24651041`, `file:LAMBD/kil/kil-uniprot.txt`).
