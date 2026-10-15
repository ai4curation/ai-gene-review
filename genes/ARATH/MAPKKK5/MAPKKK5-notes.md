# MAPKKK5 (At5g66850, Q9C5H5) notes

Sources: UniProt Q9C5H5; Falcon deep research (MAPKKK5-deep-research-falcon.md, used as retrieval aid only);
cached papers PMID:27679653 (full text), PMID:35652263 (full text), PMID:29871986, PMID:29440595, PMID:21477822 (abstracts).

## Activity
- MAP3K of the MEKK subfamily. Kinase domain directly phosphorylates MKK4/MKK5 activation loops
  [PMID:27679653 "The kinase domain of MAPKKK5 directly phosphorylated MKK4K108R and MKK5K99R (Fig 8B)"];
  [PMID:27679653 "MAPKKK5 interacts with MKK4 and MKK5 in vivo and phosphorylates their activation loops"].
- Autophosphorylation weak [PMID:27679653 "has a low autophosphorylation activity compared with the transphosphorylation of MKK4 and MKK5"].

## Upstream inputs (MAPKKK5 is the substrate)
- PBL27 (CERK1-dependent) [PMID:27679653 "PBL27 phosphorylates MAPKKK5 in a CERK1"].
- RLCK VII kinases at Ser-599; MPK6 feedback at Ser-682/692 [PMID:29871986 "directly phosphorylate MAPKKK5 Ser-599, which is required for pattern-triggered MPK3/6 activation, defense gene expression, and disease resistance"].
- BSK1 at Ser-289 (PMID:29440595).

## Genetics
- Redundant with MAPKKK3 downstream of >=4 PRRs [PMID:29871986 "two highly related MAPKKKs, MAPKKK3 and MAPKKK5, mediate MPK3/6 activation by at least four PRRs"];
  [PMID:35652263 "In plant immunity, MAPKKK3 and MAPKKK5 function redundantly upstream of the same MKK4/MKK5-MPK3/MPK6 module."]
- Yamada single mutants: reduced chitin MAPK activation and callose, larger A. brassicicola lesions, no ROS defect
  [PMID:27679653 "The mapkkk5 mutation did not influence ROS production"]. Yamada also saw enhanced flg22 MAPK activation
  [PMID:27679653 "suggesting that MAPKKK5 may negatively regulate flg22"] - conflicts with Bi 2018 (positive role in double mutant).
- With YDA in embryogenesis/gamete transmission (PMID:35652263) - not in GOA; not proposed as NEW (redundant genetic necessity only).

## Localization
- Cytosol and PM (N. benthamiana transient; Arabidopsis protoplast BiFC)
  [PMID:27679653 "the plasmolysis experiment indicated the GFP fluorescence of MAPKKK5 was detected at cytosol and plasma membrane (PM) in Nb leaves"].
  Chloroplast ISM prediction contradicted -> REMOVE.

## Curation decisions
- Core: GO:0004709 MAP3K activity; GO:0000165 MAPK cascade; GO:0002752 cell surface PRR signaling pathway. Agrees with modules/chitin_perception.yaml annoton (GO:0004709).
- Protein binding (5 rows) removed (consistent with MPK3 review).
- PRR signaling (GO:0002221) -> MODIFY to GO:0002752.
- Defense/callose/immune-regulation rows kept non-core (necessity via MAPK relay, not participation in effector steps).
- No NEW annotations.
