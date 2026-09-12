# LONRF1 comparative domain analysis results

## Conclusion

Reviewed human LONRF1 Q17RB8 contains two InterPro RING-type zinc-finger regions (IPR001841; residues 123–159 and 478–517), and both overlap an InterPro RING conserved-site call (IPR017907). The first region has eight Cys/His residues with the sequence-derived pattern `C-X2-C-X11-C-X1-H-X2-C-X2-C-X8-C-X2-C`; the second has ten Cys/His residues and contains a closely related C3H/C-rich pattern. This is strong computational support that the two annotated regions retain zinc-coordinating RING architecture. It is therefore compatible with GO:0046872 (metal ion binding), specifically structural zinc binding, although the analysis does not directly measure metal occupancy.

The same regions are strongly conserved in reviewed mouse Lonrf1 D3YY23: the first and second human/mouse RING regions are 97.30% and 100.00% identical, respectively, and their Cys/His position patterns are identical after coordinate offset. The second RING region is also 85.00% identical to human LONRF2 and 80.00% identical to human LONRF3. Human LONRF1 RING regions share 45.00–48.65% identity with the RING region of the characterized RNF4 E3 control. These results support an intact RING-family interaction/metal-binding scaffold and are compatible with GO:0061630 (ubiquitin protein ligase activity). They do **not**, by sequence comparison alone, demonstrate ubiquitin transfer, E2 recruitment, substrate recognition, or catalytic activity; experimental E3 evidence remains preferable for GO:0061630.

Q17RB8 also has an InterPro Lon protease N-terminal domain (IPR003111; residues 558–768), which is 96.68% identical to mouse Lonrf1 and 60.00–61.43% identical to the human LONRF2/LONRF3 regions. Its identity to the corresponding region of the active human LONP1 control is lower (28.02%). Most importantly, the targeted presence matrix finds no AAA+ ATPase domain/core (IPR003593/IPR003959), Lon protease family call (IPR004815), peptidase S16 active site (IPR008268), or Lon proteolytic domain (IPR008269) in any tested LONRF protein. All five features are present in the LONP1 control. Thus, the LONRF1 N-terminal-domain homology must not be interpreted as evidence for ATPase or peptidase activity.

## Direct evidence trail

- `outputs/direct/uniprot_metadata.tsv`: all six inputs resolved as reviewed UniProtKB/Swiss-Prot records. Q17RB8 was entry version 155, annotated 2026-06-10.
- `outputs/direct/target_domain_presence.tsv`: explicit presence/absence and coordinates for nine targeted InterPro features.
- `outputs/direct/domain_architecture.tsv`: one row per observed target region.
- `outputs/direct/ring_ligand_patterns.tsv`: Cys/His counts, residue coordinates, and spacings calculated from downloaded sequences.
- `outputs/direct/domain_pairwise_identity.tsv`: global pairwise identities among like InterPro-defined regions.
- `outputs/direct/domain_regions.fasta`: exact sequence segments used in the alignments.
- `outputs/raw/uniprot/` and `outputs/raw/interpro/`: official API responses and UniProt-derived FASTA files used to generate all direct outputs.

## Scope and uncertainty

This is a domain conservation analysis, not a biochemical assay. InterPro calls integrate computational signatures, and the ligand-pattern calculation describes residues inside those calls rather than independently predicting a RING fold. GO:0046872 is broad; the result specifically concerns predicted structural zinc coordination. GO:0061630 is plausible from the intact RING-family architecture and positive-control similarity, but assigning it as a demonstrated molecular function requires independent experimental or curator-accepted evidence. No peptidase activity should be inferred for LONRF1.

## Reproducibility checklist

- [x] Scripts do not use hardcoded input accessions or output paths; inputs and paths are command-line parameters and the accession set is in `inputs/proteins.tsv`.
- [x] Scripts were tested on proteins outside the LONRF family: reviewed RNF4 P78317 and LONP1 P36776 controls.
- [x] Analyses completed as expected with `uv sync --locked && just all`.
- [x] Direct results are present in `outputs/direct/`.
- [x] Raw official-source responses are present in `outputs/raw/`.
- [x] Summary includes detailed provenance and uncertainty.
