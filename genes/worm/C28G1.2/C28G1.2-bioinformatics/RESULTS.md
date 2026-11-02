# C28G1.2 (Q18287) bioinformatics results (2026-10-21 re-review)

Analyses are reproducible from the scripts in this folder:

- `panther_tree_placement.py` -> `panther_tree_placement.txt` (stdlib; fetches the PANTHER 19 PTHR11461 tree from the PANTHER web service and compares it with `interpro/panther/PTHR11461/PTHR11461-paint.tsv`).
- `serpin_architecture.py` -> `serpin_architecture.txt` (`uv run --script`; fetches UniProt sequences, searches for the reactive-centre-loop hinge and aligns Q18287 to tree neighbours with BLOSUM62 local alignment).
- Signal peptide / transmembrane prediction: EBI Phobius REST service, run interactively on the Q18287 sequence (output `Q18287 0 0 o`: no TM segment, no signal peptide).

## 1. Identity

Q18287 is the only UniProtKB entry for C28G1.2 (WBGene00016187; 265 aa; gene on chromosome X). The compact length is conserved in the Caenorhabditis orthologs (C. briggsae CBG15466/A8XM85, 263 aa; C. remanei E3NDY0, 263 aa; C. latens A0A261BKI7, 277 aa), so the short product is not an isolated gene-model artifact of the N2 annotation. InterPro assigns PANTHER PTHR11461 subfamily SF332 ("SERPIN DOMAIN-CONTAINING PROTEIN", HMM E-value 0.0015, residues 96-199); the only other SF332 members found in UniProt are those Caenorhabditis orthologs plus a myxozoan sequence, none experimentally characterised. UniProt itself carries no PANTHER cross-reference for Q18287.

## 2. Phylogenetic placement (PANTHER 19 tree)

Ancestors of the WBGene00016187 leaf, nearest first:

| Node | Event | Taxon | Leaves |
|---|---|---|---|
| PTN007508270 (SF332) | speciation | Caenorhabditis | 2 (C28G1.2 + C. briggsae CBG15466) |
| PTN002479232 | duplication | - | 18 |
| PTN002479231 | speciation | Rhabditida-Chromadorea | 28 |
| PTN000157032 | speciation | Ecdysozoa | 115 |
| ... | | | |
| PTN000156123 | speciation | Archaea-Eukaryota | 1371 |

PTN002479232 is a multifurcating duplication node whose children are the C. elegans/C. briggsae paralog lineages srp-3 (WBGene00005644), C28G1.2, srp-6/7/8 (WBGene00005647-9), srp-1 (WBGene00005642), WBGene00008854/WBGene00009708, and srp-2 (WBGene00005643). The C28G1.2 lineage has one of the two longest branches at this node (branch length 1.243; the WBGene00008854/WBGene00009708 lineage has 1.41; the srp-1, -2, -3 and -6/7/8 lineages have 0.58-0.76), i.e. it is markedly more divergent than the characterised inhibitory paralogs. No ortholog outside Caenorhabditis was placed with it, so no experimentally characterised ortholog exists; the closest characterised relatives are the paralogous intracellular serpins SRP-2, SRP-6, SRP-3 and SRP-1, all equally related by topology (polytomy).

PAINT nodes that are ancestors of Q18287 (from the local PAINT file):

- PTN000156123 (family root): GO:0005576 extracellular region, IBD. This is the source of the existing IBA.
- PTN002479231 (nematode clade): GO:0004867 serine-type endopeptidase inhibitor activity, IBD, seeded by WBGene00005643 (srp-2), dated 2026-08-28. Not yet present in the GOA file for Q18287 or for its paralogs (srp-1, -2, -3, -6 also lack this IBA in QuickGO), so its absence from Q18287 reflects release timing, not a curator exclusion of this leaf.

All other PAINT nodes in PTHR11461 (vertebrate, deuterostome, insect, plant clades), including the NOT extracellular region at PTN002606963 (Euteleostomi, intracellular clade B) are not ancestors of Q18287.

## 3. Serpin architecture

Best match to the hinge consensus EEGTEAAA (P17-P10 of an inhibitory reactive-centre loop):

| Protein | Length | Best window | Mismatches |
|---|---|---|---|
| Q18287 C28G1.2 | 265 | LSGIETTF@6 | 6 |
| SRP-2 O17365 | 359 | EDGTTAAA@310 | 2 |
| SRP-6 G5EFH4 | 375 | EDGTVAAA@324 | 2 |
| SRP-3 G5ECY2 | 362 | EEGTTAAA@312 | 1 |
| SRP-1 G5EE40 | 366 | QVGTRAAA@317 | 3 |

In every local alignment, the paralog's hinge/reactive-centre-loop segment has no counterpart in Q18287 (SRP-2 311-330; SRP-3 306-329; SRP-6 291-312 and 330-339; SRP-1 280-300). Against the full-length SRP-3 and SRP-6 alignments, Q18287 also lacks several internal segments in the N-terminal half (SRP-3 77-89, 94-116, 146-156; SRP-6 91-111, 132-168). Q18287 shares 27-32% identity with the paralogs over the aligned regions.

Interpretation: C28G1.2 retains a compact serpin-fold-like scaffold (SUPFAM serpin superfamily over residues 4-264) but lacks the hinge and reactive-centre loop that the inhibitory paralogs use to trap proteases. It is therefore unlikely to act as a protease inhibitor by the serpin suicide-substrate mechanism. This is a sequence-level inference; no experiment has tested it.

## 4. Localization signal

Phobius predicts no signal peptide and no transmembrane segment. Its closest paralogs are cytosolic intracellular serpins that lack signal peptides (PMID:25786854, PMID:14739286).

## Limitations

- The hinge search is a motif heuristic; a structurally divergent loop could exist that this check would miss, though the alignment gaps argue that the whole region is deleted.
- The PANTHER tree topology near PTN002479232 is a polytomy, so which inhibitory paralog is closest cannot be resolved.
- No expression, localization or biochemical data exist for C28G1.2.
