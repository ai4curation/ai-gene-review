# SPINK5 (Q9NQ38): PANTHER 19 tree placement

Script: `panther_tree.py` (run 2026-10-21 against the PANTHER 19.0 treeinfo service for PTHR10913);
raw output in `panther_tree.out`.

## Family assignment

PANTHER 19.0 places SPINK5 in PTHR10913 (FOLLISTATIN-RELATED), subfamily PTHR10913:SF71 (SERINE PROTEASE
INHIBITOR KAZAL-TYPE 5), per the PANTHER 19 human classification file. The UniProt record carries an older
cross-reference to PTHR47499:SF1 (SERINE PROTEASE INHIBITOR KAZAL-TYPE 7); the tree analysis below uses the
PANTHER 19 family.

## Root-to-leaf path

PTN000099217 (Eukaryota) > PTN000099219 (Eumetazoa duplication) > PTN000857287 > PTN008956881 (Bilateria
duplication) > PTN000857333 (Bilateria speciation) > PTN000857275 (Deuterostomia) > PTN001331258 (Chordata) >
PTN008508634 (Euteleostomi duplication) > PTN000099251 (Theria speciation) > ... > Q9NQ38.

## Scope of the serine-type endopeptidase inhibitor IBD

The PAINT node PTN000099251 (Theria, speciation) lies on the SPINK5 path. Its 12 leaves are the therian
SPINK5 orthologs only: human, chimpanzee, gorilla, macaque, mouse, rat, cow, pig, horse, cat, dog and
opossum. The node does not include TMEFF2 (which diverges from SPINK5 at the Euteleostomi duplication
PTN008508634), the follistatins, or any invertebrate member.

## Last common ancestors

| Member | LCA with Q9NQ38 | Event |
|---|---|---|
| Spink5 (mouse, Q148R4) | PTN000099253 Euarchontoglires | speciation (ortholog) |
| TMEFF2 (human) | PTN008508634 Euteleostomi | duplication (paralog) |
| CG32354 (fly, Q9VSK1) | PTN000857333 Bilateria | speciation (co-ortholog, many-to-many) |
| Fs (fly, Q86NV3) | PTN000857333 Bilateria | speciation (co-ortholog, many-to-many) |
| FST (human) | PTN000099219 Eumetazoa | duplication (distant paralog) |

Interpretation: the mouse ortholog sits inside the therian clade that PAINT annotated with serine-type
endopeptidase inhibitor activity, so mouse experimental findings transfer to human SPINK5 at the orthology
level. The fly proteins share only a Bilateria speciation node with SPINK5, well above the Theria IBD node,
so the PAINT curators chose not to project the inhibitor function to them.
