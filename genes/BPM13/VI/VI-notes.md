# Enterobacteria phage M13 — Gene VI (G6P / pVI)

## Overview
- **UniProt Accession:** P69532 (`G6P_BPM13`)
- **Gene Symbol:** `VI`
- **Protein Product:** Head (proximal tip) minor coat protein G6P (pVI, Coat protein D), 112 aa (~12.4 kDa) hydrophobic multi-pass membrane protein (`file:BPM13/VI/VI-uniprot.txt`).

## Biological Role in the M13 Lifecycle
- **Proximal ("Pointy") Virion Tip Structural Subunit:** In the mature M13 virion (cryo-EM structure at 3.30 Å, PDB: 8IXK, 8JWX), five copies of pVI form a pentameric ring that associates tightly with the C-terminal domains of five pIII subunits and the terminal layer of major coat protein pVIII to form the proximal ("head" / adsorption) tip of the filament (`file:BPM13/VI/VI-uniprot.txt`, [PMID:35746635]).
- **Termination of Viral Extrusion:** Prior to virion incorporation, pVI resides as a transmembrane protein in the *Escherichia coli* inner membrane (`GO:0020002` host cell plasma membrane). At the conclusion of filamentous phage assembly and extrusion, the pIII–pVI complex enters the pI/pXI assembly machine laterally, caps the trailing end of the extruding nucleoprotein filament, and releases the mature phage particle from the host inner membrane (`GO:0099045` viral extrusion) (`file:BPM13/VI/VI-uniprot.txt`, [PMID:35746635]).
- **Note on Existing Annotations:**
  - `GO:0039666` (virion attachment to host cell pilus) is an over-propagated keyword mapping (`KW-1241`); pIII (via its N2 domain) directly binds the F-pilus, whereas pVI is buried within the proximal tip adapter ring and has no surface-exposed pilus-binding domain (`REMOVE` or `MODIFY` to `GO:0099045` viral extrusion; since `KW-1241` is a false positive for pVI, `REMOVE` is appropriate, while `GO:0046718` symbiont entry into host cell can be kept as non-core or removed if unverified, or wait: UniProt states "Plays essential roles both in the entry of the viral genome into the bacterial host and in budding process (Probable)").

## Key GO Annotations
- **Molecular Function:** `GO:0039660` (structural constituent of virion).
- **Cellular Component:** `GO:0019028` (viral capsid) / `GO:0019029` (helical viral capsid) and `GO:0020002` (host cell plasma membrane).
- **Biological Process:** `GO:0099045` (viral extrusion).
