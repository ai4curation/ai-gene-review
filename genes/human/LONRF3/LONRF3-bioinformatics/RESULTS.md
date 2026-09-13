# LONRF3 comparative domain analysis results

## Conclusion

Reviewed human LONRF3 Q496Y0 contains two InterPro RING-type zinc-finger regions (IPR001841; residues 158–195 and 466–505), and both overlap an InterPro RING conserved-site call (IPR017907; 173–182 and 482–491). The first is additionally assigned the C3HC4 RING-type entry IPR018957. Both regions retain dense Cys/His patterns and are strongly conserved in reviewed mouse Lonrf3, supporting intact rather than degenerate RING-family architecture:

- The first human region contains nine Cys/His residues with the calculated pattern `C-X2-C-H-X10-C-X1-H-X2-C-X2-C-X10-C-X2-C`. It is 94.74% identical to the mouse ortholog region, and its conserved-site segment is 100% identical.
- The second human region contains ten Cys/His residues with the pattern `C-X2-C-X11-C-X1-H-X2-C-X2-C-X3-C-X2-H-X3-C-X2-C`. It is 97.50% identical to the mouse ortholog region, and its conserved-site segment is also 100% identical.
- Relative to family and control proteins, the first region is 55.56% identical to the first LONRF1 RING and 36.84% identical to the RNF4 RING. The second is 80.00% identical to the second LONRF1 RING, 87.50% identical to the stronger LONRF2 RING, and 42.50% identical to RNF4.

These results provide strong computational support for structural zinc-binding RING domains and are compatible with GO:0046872 (metal ion binding). They are also compatible with RING E3 architecture, but sequence conservation alone does not establish GO:0061630 (ubiquitin protein ligase activity): no ubiquitin transfer, E2 recruitment, or substrate-dependent ligase activity was measured here. LONRF3-specific experimental evidence should remain necessary for a confident activity annotation.

Q496Y0 also contains an InterPro Lon protease N-terminal domain (IPR003111; residues 546–756), which is 94.31% identical to the mouse ortholog, 61.43% identical to LONRF1, 62.86% identical to LONRF2, and 28.79% identical to the corresponding region of active human LONP1. More decisively, the targeted presence matrix finds no AAA+ ATPase domain/core (IPR003593/IPR003959), Lon protease family call (IPR004815), peptidase S16 active site (IPR008268), or Lon proteolytic domain (IPR008269) in LONRF3. All five are present in the LONP1 control. The isolated N-terminal substrate-binding-domain homology is therefore not evidence of ATPase or peptidase activity.

## Direct evidence trail

- `outputs/direct/uniprot_metadata.tsv`: all six inputs resolved as reviewed UniProtKB/Swiss-Prot records. Q496Y0 was entry version 167, annotated 2026-06-10.
- `outputs/direct/target_domain_presence.tsv`: explicit presence/absence and coordinates for nine targeted InterPro features.
- `outputs/direct/domain_architecture.tsv`: one row per observed target region.
- `outputs/direct/ring_ligand_patterns.tsv`: Cys/His counts, residue coordinates, and spacings calculated from downloaded sequences.
- `outputs/direct/domain_pairwise_identity.tsv`: global pairwise identities among like InterPro-defined regions.
- `outputs/direct/domain_regions.fasta`: exact sequence segments used in alignments.
- `outputs/raw/uniprot/` and `outputs/raw/interpro/`: official API responses and UniProt-derived FASTA files used to generate all direct outputs.

## Scope and uncertainty

This is a domain-conservation analysis, not a biochemical assay. InterPro calls integrate computational signatures, and the ligand-pattern calculation describes residues within those calls rather than independently predicting a fold. The sequence evidence strongly disfavors degeneration of either RING region across the human–mouse comparison, but it cannot prove zinc occupancy or ligase activity. Likewise, absence of the complete Lon catalytic architecture strongly argues against inferring Lon peptidase activity from the N-terminal domain alone, but does not test every conceivable unrelated catalytic activity.

Reported pairwise identities use aligned non-gap residue pairs as the denominator; this can overstate similarity when compared regions differ in length, so length-mismatched values should be interpreted with that limitation.

## Reproducibility checklist

- [x] Scripts do not use hardcoded input accessions or output paths; inputs and paths are command-line parameters and the accession set is in `inputs/proteins.tsv`.
- [x] Scripts were tested on proteins outside the LONRF family: reviewed RNF4 P78317 and LONP1 P36776 controls.
- [x] Analyses completed as expected with `uv sync --locked && just all`.
- [x] Direct results are present in `outputs/direct/`.
- [x] Raw official-source responses are present in `outputs/raw/`.
- [x] Summary includes detailed provenance and uncertainty.
