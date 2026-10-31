# PTHR32329 subfamily profile

Script: `subfamily_profile.py`. Run it from the repository root with
`uv run python interpro/panther/PTHR32329/PTHR32329-bioinformatics/subfamily_profile.py`.
It queries UniProtKB for every entry whose PANTHER cross-reference names each
subfamily, and writes `subfamily_profile.json`. All numbers below are copied
from that file (retrieved 2026-10-31).

## Subfamily composition

| Subfamily | Members | Median length (aa) | Members >= 1000 aa | Kingdoms | Most common Pfam architectures |
|---|---|---|---|---|---|
| SF2 | 3154 | 315 | 46 | Bacteria 2936, Archaea 217, Eukaryota 1 | PF01869 (1609), PF09989 (580), no Pfam (376), PF06050+PF09989 (210) |
| SF4 | 2061 | 1415 | 1580 | Bacteria 2040, Eukaryota 16, Archaea 5 | PF01869+PF09989 (1760), no Pfam (229), PF01869 (49) |
| SF5 | 237 | 255 | 3 | Bacteria 237 | PF01869 (223) |
| SF7 | 779 | 327 | 209 | Bacteria 757, Archaea 14, Eukaryota 8 | PF01869 (555), PF01869+PF09989 (214) |
| SF8 | 159 | 252 | 5 | Bacteria 158, Archaea 1 | PF01869 (153) |

PF01869 is the BadF/BadG/BcrA/BcrD ATPase domain. PF09989 is DUF2229, the
CoA enzyme activase domain that corresponds to Red1 of PlsA
(PMID:33350306). PF06050 is HGD-D, the 2-hydroxyglutaryl-CoA dehydratase
component-D domain.

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
| Q9CDI2 yxcA | plasmalogen synthase | 1436 | SF4 |
| A0A0H2YUD5 CPF_1406 | PlsA subunit (C. perfringens) | 975 | SF4 |
| A0A0H2YN56 CPF_1405 | PlsR subunit (C. perfringens) | 420 | SF4 |

## Conclusions

- The experimentally studied proteins split cleanly. Every characterized
  dehydratase activator and benzoyl-CoA reductase ATPase subunit is in SF2.
  Every characterized plasmalogen synthase is in SF4, including both subunits
  of the two-protein C. perfringens enzyme.
- SF4 is dominated by long proteins with the PlsA architecture (1580 of 2061
  are 1000 aa or longer; 1760 have PF01869 + PF09989). It is almost entirely
  bacterial. Its 16 eukaryotic members are uncharacterized.
- SF2 is broad and mixed. Besides the short (about 260 aa) activators it holds
  580 DUF2229-only proteins and 210 proteins that fuse DUF2229 with an HGD-D
  dehydratase domain. None of these fusions has been characterized here.
- SF5, SF7 and SF8 contain no experimentally studied protein. SF5 and SF8 are
  short single-domain proteins like the SF2 activators. SF7 is mixed: 214 of
  its 779 members have the PF01869 + PF09989 architecture.
- Limits: subfamily membership comes from UniProt's PANTHER cross-references,
  not from re-scoring the HMMs. Pfam architecture is taken from UniProt
  cross-references, which can miss divergent domains (PlsR, Red2, has no
  PF06050 hit in UniProt).
