# LONRF2 comparative domain analysis results

## Conclusion

The custom analysis adds a useful architecture check, but it is not needed to infer LONRF2's E3 activity: direct experimental literature is primary. In particular, Li et al. reported that LONRF2 selectively binds and ubiquitylates damaged or misfolded proteins and that its deficiency causes late-onset neurological phenotypes (PMID:37474791). The results below address the narrower questions of whether the sequence retains RING/zinc-binding architecture and whether it contains the catalytic machinery of a Lon peptidase.

InterPro identifies two broad RING-type zinc-finger regions (IPR001841) in reviewed human LONRF2 Q1L5Z9, at residues 143–193 and 448–487. Their support is unequal:

- The second region is the stronger, conserved RING call. It overlaps the InterPro RING conserved site IPR017907 (464–473), contains 11 Cys/His residues in the downloaded sequence, is 85.00% identical to the corresponding LONRF1 region and 87.50% identical to the corresponding LONRF3 region, and shares 45.00% identity with the characterized RNF4 RING control. Its conserved-site segment is 70% identical to RNF4's segment.
- The first region contains seven Cys/His residues but does not overlap an IPR017907 conserved-site call. It is only 21.74% identical to the RNF4 region and 43.59–47.37% identical to the compared LONRF regions. InterPro does not assign IPR018957 (C3HC4 RING type) anywhere in Q1L5Z9. Thus, this workflow does not establish that the first broad call is an intact canonical zinc-coordinating RING; it may be atypical or degenerate and would require structural or biochemical validation.

The second RING result is compatible with structural zinc binding and supports the architecture expected for a RING E3. Metal occupancy was not measured, so sequence/domain evidence for GO:0046872 (metal ion binding) remains computational. GO:0061630 (ubiquitin protein ligase activity) should be justified primarily by the experimental LONRF2 literature, with this analysis as corroborating architecture evidence.

Q1L5Z9 also contains an InterPro Lon protease N-terminal domain (IPR003111; residues 528–737). It is 60.00% identical to the LONRF1 region, 62.86% identical to the LONRF3 region, and only 26.60% identical to the corresponding region of active human LONP1. More decisively, the targeted presence matrix finds no AAA+ ATPase domain/core (IPR003593/IPR003959), Lon protease family call (IPR004815), peptidase S16 active site (IPR008268), or Lon proteolytic domain (IPR008269) in LONRF2. All five are present in the LONP1 control. The isolated N-terminal substrate-binding-domain homology and the alternative name “neuroblastoma apoptosis-related protease” are therefore not evidence of peptidase activity.

## Direct evidence trail

- `outputs/direct/uniprot_metadata.tsv`: all five inputs resolved as reviewed UniProtKB/Swiss-Prot records. Q1L5Z9 was entry version 151, annotated 2026-06-10.
- `outputs/direct/target_domain_presence.tsv`: explicit presence/absence and coordinates for nine targeted InterPro features.
- `outputs/direct/domain_architecture.tsv`: one row per observed target region.
- `outputs/direct/ring_ligand_patterns.tsv`: Cys/His counts, residue coordinates, and spacings calculated from downloaded sequences.
- `outputs/direct/domain_pairwise_identity.tsv`: global pairwise identities among like InterPro-defined regions.
- `outputs/direct/domain_regions.fasta`: exact sequence segments used in alignments.
- `outputs/raw/uniprot/` and `outputs/raw/interpro/`: official API responses and UniProt-derived FASTA files used to generate direct outputs.

## Scope and uncertainty

This is a domain-conservation analysis, not a biochemical assay. InterPro calls integrate computational signatures, and the ligand-pattern calculation describes residues inside those calls rather than independently predicting a fold. The first Q1L5Z9 RING-like region is notably less well supported than the second. Conversely, absence of the full Lon catalytic architecture is strong evidence against inferring Lon peptidase activity from the N-terminal domain alone, but it does not exclude every possible unrelated catalytic activity. No non-human LONRF2 sequence was used because the official reviewed-UniProt query returned only the human entry.

## Reproducibility checklist

- [x] Scripts do not use hardcoded input accessions or output paths; inputs and paths are command-line parameters and the accession set is in `inputs/proteins.tsv`.
- [x] Scripts were tested on proteins outside the LONRF family: reviewed RNF4 P78317 and LONP1 P36776 controls.
- [x] Analyses completed as expected with `uv sync --locked && just all`.
- [x] Direct results are present in `outputs/direct/`.
- [x] Raw official-source responses are present in `outputs/raw/`.
- [x] Summary includes detailed provenance, literature primacy, and uncertainty.
