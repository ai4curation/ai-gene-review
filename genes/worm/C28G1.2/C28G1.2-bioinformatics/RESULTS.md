# C28G1.2 (Q18287) bioinformatics results

Two reproducible scripts (run with `uv run <script>`; inline PEP 723 dependencies):

- `panther_placement.py` -> `panther_placement_output.txt`: places the C28G1.2 leaf
  (PTN007508271) in the PANTHER 19 PTHR11461 (serpin) tree.
- `rcl_check.py` -> `rcl_check_output.txt`: global BLOSUM62 alignments of Q18287 against
  its PANTHER sister CBG15466 (A8XM85) and the characterised worm serpins SRP-2 (O17365)
  and SRP-3 (G5ECY2), plus a regex scan for the reactive-centre-loop hinge motif upstream
  of the conserved C-terminal DHPF motif.

## Phylogenetic placement

InterPro assigns Q18287 to PTHR11461 (SERINE PROTEASE INHIBITOR, SERPIN), subfamily
PTHR11461:SF332 (SERPIN DOMAIN-CONTAINING PROTEIN), with a weak HMM score (0.0015) over
residues 96-199. SF332 contains only Caenorhabditis proteins (C. elegans Q18287,
C. remanei and C. latens homologues) plus one myxozoan sequence; no member has
experimental data. All other C. elegans serpins (srp-1, -2, -3, -6, -7, -8) fall in
different subfamilies (SF146, SF211, SF299, SF352).

In the PANTHER tree the target pairs with C. briggsae CBG15466 (node PTN007508270,
Caenorhabditis), which sits inside PTN002479232 (Caenorhabditis serpins: srp-1, srp-2,
srp-3, srp-6, srp-7, srp-8 and their C. briggsae orthologs) and PTN002479231
(Rhabditida-Chromadorea, adding Pristionchus serpins). The resolution within
PTN002479232 is a near-polytomy in the PANTHER tree, so no single characterised paralog is
a closer relative than the others; C28G1.2 is a lineage-specific paralog of the nematode
clade L intracellular serpins, with no one-to-one ortholog outside Caenorhabditis.

## Architecture

| protein | length | DHPF motif at | RCL hinge upstream of DHPF |
|---|---|---|---|
| Q18287 C28G1.2 | 265 | 245 | absent |
| A8XM85 CBG15466 | 263 | 243 | absent |
| O17365 SRP-2 | 359 | 339 | DEDGTTAAAAS |
| G5ECY2 SRP-3 | 362 | 341 | EEGTTAAAV |

Q18287 aligns over its whole length to CBG15466 (64% identity) and at about 31-35% identity
to SRP-2 and SRP-3 (covering about 70% of their length). Relative to SRP-2, the target lacks
an internal block of roughly 50-60 residues near the N-terminal third and, decisively,
the entire hinge/reactive-centre loop (SRP-2 segment "EVDEDGTTAAAASAFKVQLEMMIMAEPTQFVA"),
which in inhibitory serpins is the bait sequence cleaved by the target protease and
inserted into beta-sheet A. The same deletion is present in CBG15466, so it is a
conserved feature of this Caenorhabditis lineage, not a C. elegans gene-model error.

## Interpretation

C28G1.2 is a truncated, RCL-less member of the nematode intracellular serpin clade.
Without a reactive-centre loop it cannot use the serpin suicide-substrate mechanism, so
transfer of serine- or cysteine-type endopeptidase inhibitor activity from SRP-2/SRP-3
is not supported. These scripts do not run signal-peptide predictors; the UniProt record
carries no SIGNAL feature, and its N-terminus (MSAQSLSGIETTFGLNLL) is not a hydrophobic
signal-like segment by inspection, which is consistent with the rest of the clade.
