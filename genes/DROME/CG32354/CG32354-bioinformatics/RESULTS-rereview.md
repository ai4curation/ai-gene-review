# CG32354 (Q9VSK1) re-review: PANTHER tree placement and Kazal reactive sites

Script: `panther_tree_rereview.py` (run 2026-10-21 against PANTHER 19.0 treeinfo and UniProt REST);
raw output in `panther_tree_rereview.out`.

## Tree placement

Q9VSK1 descends from both PAINT nodes that give it IBA annotations: PTN000099217 (Eukaryota, family root,
extracellular region) and PTN000099219 (Eumetazoa duplication, cell differentiation). The full path is
PTN000099217 > PTN000099219 > PTN000857287 > PTN008956881 > PTN000857333 (Bilateria speciation) >
PTN002588966 (Protostomia) > PTN000099399 (Ecdysozoa) > PTN002588941 (Hexapoda-Crustacea duplication) >
PTN008508655 > PTN008508656 > PTN000099406 (Diptera).

Last common ancestors with characterised or reference members:

| Member | LCA with Q9VSK1 | Event |
|---|---|---|
| Fs, CG12716, anon-f (fly) | PTN002588941 Hexapoda-Crustacea | duplication (paralogs) |
| ZK813.6 (worm) | PTN000099399 Ecdysozoa | speciation (ortholog, uncharacterised) |
| SPINK5, TMEFF2 (human) | PTN000857333 Bilateria | speciation (co-orthologs, many-to-many) |
| FST, FSTL3 (human) | PTN000099219 Eumetazoa | duplication (distant paralogs) |

The serine-type endopeptidase inhibitor IBD (PTN000099251, taxon:32525 Theria, seed SPINK5) and the
activin-binding IBDs (PTN001657053, taxon:6072) are not on the Q9VSK1 path, so PAINT did not propagate either
function to this protein.

## Subfamily membership

A UniProt query for all PTHR10913 members (stream, `xref:panther-PTHR10913`, 8,362 entries) returned 291
entries assigned to PTHR10913:SF79. All but one (Trichoplax B3S9W4) are arthropods, and none is a reviewed
(Swiss-Prot) entry. In the model-organism PANTHER 19 classification files, Q9VSK1 is the only SF79 member.
No experimentally characterised SF79 protein exists to transfer function from.

## Reactive-bond sites

The seven PROSITE PRU00798 reactive-bond sites carry P1 residues P, T, S, K, K, R and R. Three or four
(K/R at P1) are compatible with trypsin-like protease targets; P at 170 is not a typical inhibitory P1.
The UniProt record also flags that the rule lacks conserved residues for feature propagation. This is
inconclusive for inhibitory activity: it neither establishes nor excludes it.
