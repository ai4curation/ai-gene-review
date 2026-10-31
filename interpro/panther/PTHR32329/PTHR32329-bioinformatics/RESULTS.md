# PTHR32329 subfamily profile

Script: `subfamily_profile.py`. Run it from the repository root with
`uv run python interpro/panther/PTHR32329/PTHR32329-bioinformatics/subfamily_profile.py`.
It queries UniProtKB for every entry whose PANTHER cross-reference names each
subfamily, and writes `subfamily_profile.json`. All numbers below are copied
from that file (retrieved 2026-10-31).

## Subfamily composition

| Subfamily | Members | Median length (aa) | Members >= 1000 aa | Kingdoms |
|---|---|---|---|---|
| SF2 | 3154 | 315 | 46 | Bacteria 2936, Archaea 217, Eukaryota 1 |
| SF4 | 2061 | 1415 | 1580 | Bacteria 2040, Eukaryota 16, Archaea 5 |
| SF5 | 237 | 255 | 3 | Bacteria 237 |
| SF7 | 779 | 327 | 209 | Bacteria 757, Archaea 14, Eukaryota 8 |
| SF8 | 159 | 252 | 5 | Bacteria 158, Archaea 1 |

Pfam architectures with at least 10 members (n, median length in aa):

| Subfamily | Architectures |
|---|---|
| SF2 | PF01869 (1609, 261); PF09989 (580, 333); no Pfam (376, 372); PF06050+PF09989 (210, 328); PF01869+PF06050 (185, 562); PF06050 (141, 366); PF01869+PF09989 (47, 1412) |
| SF4 | PF01869+PF09989 (1760, 1420); no Pfam (229, 426); PF01869 (49, 590); PF09989 (22, 806.5) |
| SF5 | PF01869 (223, 254) |
| SF7 | PF01869 (555, 324); PF01869+PF09989 (214, 1390.5) |
| SF8 | PF01869 (153, 252) |

PF01869 is the BadF/BadG/BcrA/BcrD ATPase domain. PF09989 is DUF2229, the
CoA enzyme activase domain that corresponds to Red1 of PlsA. PF06050 is
HGD-D, the 2-hydroxyglutaryl-CoA dehydratase component-D domain, which
corresponds to Red2 of PlsR (PMID:33350306).

## Subfamily placement of experimentally studied proteins

| Protein | Function | Length | PANTHER subfamily |
|---|---|---|---|
| P11568 HgdC | (R)-2-hydroxyglutaryl-CoA dehydratase activator | 260 | SF2 |
| Q5U925 HadI | 2-hydroxyisocaproyl-CoA dehydratase activator | 266 | SF2 |
| Q93AM0 FldI | phenyllactate dehydratase activator | 264 | SF2 |
| G3KIM5 LcdC | lactoyl-CoA dehydratase activator | 259 | SF2 |
| O87876 BcrA | benzoyl-CoA reductase subunit A | 438 | SF2 |
| O87877 BcrD | benzoyl-CoA reductase subunit D | 282 | SF2 |
| Q8DVN8 SMU_438c | plasmalogen synthase | 1433 | SF4 |
| Q835P9 EF1327 | plasmalogen synthase | 1415 | SF4 |
| G0VRE7 MeHAD | plasmalogen synthase | 1431 | SF4 |
| A0A0H2YUD5 CPF_1406 | PlsA subunit (C. perfringens ATCC 13124) | 975 | SF4 |
| A0A0H2YN56 CPF_1405 | PlsR subunit (C. perfringens ATCC 13124) | 420 | SF4 |

The two C. perfringens ATCC 13124 proteins are the reference-proteome
counterparts of the tested strain 13 operon (CPE1195/CPE1194).

Placement of a protein whose function is inferred by orthology:

| Protein | Basis | Length | PANTHER subfamily |
|---|---|---|---|
| Q9CDI2 yxcA (L. lactis IL1403) | ortholog of the tested L. cremoris PlsA LACR_2543, which has no UniProtKB entry | 1436 | SF4 |

## Conclusions

- The experimentally studied proteins split cleanly. Every characterized
  dehydratase activator and benzoyl-CoA reductase ATPase subunit is in SF2.
  Every characterized plasmalogen synthase in UniProtKB is in SF4, including
  both subunits of the two-protein C. perfringens enzyme. The S. ruminantium
  and B. suis enzymes (PMID:39725447, PMID:41427725) are not placed here
  because their papers give no UniProtKB accession.
- SF4 is dominated by long proteins with the PlsA architecture (1580 of 2061
  are 1000 aa or longer; 1760 have PF01869 + PF09989). It is almost entirely
  bacterial. Its 16 eukaryotic members are uncharacterized.
- SF2 is mixed, and its architectures are not all activators:
  - PF01869 alone (1609, about 260 aa) matches the characterized activators.
  - PF01869 + PF06050 (185, about 560 aa) fuses an activator domain with a
    dehydratase component-D domain in one chain, the "bifunctional" protein
    PANTHER's family name describes. None is characterized.
  - PF09989 + PF06050 (210, about 330 aa) is the Red1 + Red2 architecture
    that PMID:33350306 assigns to the second gene of two-gene plasmalogen
    synthase systems (its architecture 3). These are probably PlsR-type
    subunits, not dehydratases.
  - PF01869 + PF09989 (47, about 1400 aa) is the PlsA architecture.
  - PF09989 alone (580), PF06050 alone (141) and no Pfam (376) have no
    PF01869 cross-reference. They lack direct support for any ATPase-based
    activity.
- SF5, SF7 and SF8 contain no experimentally studied protein. SF5 and SF8 are
  short single-domain proteins like the SF2 activators. SF7 is mixed: 214 of
  its 779 members have the PlsA architecture.
- Limits: subfamily membership comes from UniProt's PANTHER cross-references,
  not from re-scoring the HMMs. Pfam architecture is taken from UniProt
  cross-references, which miss divergent domains. Pfam's HGD-D model does
  not detect the Red2 domain of Q9CDI2 or of C. perfringens PlsR
  (genes/LACLA/yxcA/yxcA-bioinformatics/RESULTS.md), so the absence of
  PF06050 is weak evidence of absence.
