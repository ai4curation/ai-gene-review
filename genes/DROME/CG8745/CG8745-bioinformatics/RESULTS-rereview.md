# CG8745 (Q9VU95) phylogenetic placement within PANTHER PTHR45688 (re-review, 2026-10-21)

Script: `phylo_placement.py` (run with `uv run phylo_placement.py`). Raw output: `phylo_placement_output.txt`.
Inputs: UniProt sequences for 14 PTHR45688 members chosen to span subfamilies SF1 (ETNPPL), SF6 (PHYKPL),
SF3 (AGXT2) and SF13 (the subfamily containing CG8745). Subfamily assignments are from the PANTHER 19.0
classification files and `interpro/panther/PTHR45688/PTHR45688-entries.csv`. Alignment: MAFFT `--auto`;
tree: neighbour joining on BLOSUM62 distances (Biopython), rooted on the SF3 AGXT2 sequences. No bootstrap
support was computed, so the tree topology is indicative only.

## Percent identity to CG8745 (aligned positions)

| Sequence | PANTHER SF | % identity |
|---|---|---|
| ETNPPL human (Q8TBG4) | SF1 | 54.1 |
| etnppl zebrafish (Q7SY54) | SF1 | 53.4 |
| phykpl zebrafish (Q2YDQ8) | SF6 | 51.5 |
| PHYKPL human (Q8IUZ5) | SF6 | 50.0 |
| eppl-1 C. elegans (P91408) | SF13 | 47.6 |
| AGT2 Arabidopsis (Q940M2) | SF3 | 42.0 |
| AGT3 Arabidopsis (Q94AL9) | SF13 | 41.1 |
| CG11241 Drosophila (A8E6R2) | SF3 | 39.4 |
| T09B4.8 C. elegans (O02158) | SF3 | 38.5 |
| AGXT2 human (Q9BYV1) | SF3 | 37.4 |
| 2-aminohexano-6-lactam racemase (Q7M181) | SF13 | 29.1 |
| 2,2-dialkylglycine decarboxylase dgdA (P16932) | SF13 | 26.7 |
| SPAC1039.07c S. pombe (Q9US34) | SF13 | 26.5 |

## Findings

1. CG8745 is about equally similar to the two vertebrate ammoniophospholyase paralogs, ETNPPL (54%) and
   PHYKPL (50-51%), and clearly less similar to the AGXT2 transaminases (37-42%).
2. In the NJ tree CG8745 and C. elegans eppl-1 branch at the base of a clade that holds vertebrate ETNPPL
   (SF1) and PHYKPL (SF6). This is the pattern expected if CG8745 is a pro-ortholog (co-ortholog) of both,
   with the ETNPPL/PHYKPL duplication occurring in the vertebrate lineage. The tree did not separate SF1
   from SF6 cleanly, so the order of branching within that clade is unresolved.
3. PANTHER SF13 is not a coherent functional group. Its other members (bacterial dialkylglycine decarboxylase,
   aminohexanolactam racemase, S. pombe SPAC1039.07c, Arabidopsis AGT3) fall outside the
   CG8745/ETNPPL/PHYKPL clade and share only 26-41% identity with CG8745. Subfamily membership in SF13
   therefore cannot be used to transfer a reaction to CG8745.
4. The PLP-binding lysine is conserved: CG8745 K291 (the UniProt MOD_RES N6-(pyridoxal phosphate)lysine)
   aligns with human ETNPPL K278, PHYKPL K278 and the catalytic lysine of every other sequence analysed.
5. Consistent with this placement, the PAINT IBD for GO:0050459 ethanolamine-phosphate phospho-lyase
   activity sits at node PTN002904331 with taxon 117571 (Euteleostomi) in
   `interpro/panther/PTHR45688/PTHR45688-paint.tsv`, a node that does not include CG8745 or eppl-1.

## Interpretation

The evidence supports a PLP-dependent carbon-oxygen lyase acting on a phosphorylated amino compound
(the shared ETNPPL/PHYKPL chemistry) but does not choose between phosphoethanolamine and
5-phosphohydroxy-L-lysine as the substrate. No fly biochemistry exists.
