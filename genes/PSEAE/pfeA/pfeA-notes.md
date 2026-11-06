# pfeA (PA2688, Q05098) notes

## Identity

- Ferric enterobactin receptor PfeA, 746 aa, Swiss-Prot. TonB-dependent outer
  membrane receptor (TBDR): signal peptide 1-25, TonB box 39-44, plug domain
  47-174, 22-strand beta-barrel 179-746, TonB C-terminal box 729-746. FepA
  ortholog (>60% identity to E. coli FepA). PANTHER PTHR30069:SF51
  "FERRIENTEROBACTIN RECEPTOR"; TCDB 1.B.14.1.5.
- No N-terminal signalling extension before the TonB box (signal peptide ends at
  25, TonB box at 39): PfeA is a receptor/transporter, not a TonB-dependent
  transducer like FpvA. Enterobactin sensing for pfeA induction is done by the
  separate PfeS/PfeR two-component system (not reviewed here).
- No deep-research provider was available; notes are from cached publications.

## Literature

- PseudoCAP seed paper (Dean and Poole 1993, abstract only; PMC196144 full text not
  retrievable): mutant K407 lacking the 80 kDa receptor grows poorly on
  enterobactin under iron limitation
  [PMID:8419284 "Pseudomonas aeruginosa K407, a mutant lacking a high-affinity 80,000-molecular-weight ferric enterobactin receptor protein (80K protein), exhibited poor growth (small colonies) on iron-deficient succinate minimal medium containing ethylenediamine-di(o-hydroxyphenylacetic acid) (EDDHA) and enterobactin."];
  the cloned gene restores enterobactin-dependent iron uptake in E. coli fepA
  [PMID:8419284 "Moreover, the fragment complemented the fepA mutation in MT912, restoring both growth in EDDHA-containing medium and enterobactin-dependent uptake of 55Fe3+."];
  the product is made in outer membranes
  [PMID:8419284 "direct the synthesis of high levels of a protein of the same molecular weight in the outer membranes of Escherichia coli fepA strains MT912 and IR20"].
- PirA (PA0931) is a second ferric-enterobactin receptor; only the pfeA pirA
  double mutant fails to use ferric enterobactin
  [PMID:15899402 "Ferric-enterobactin also failed to stimulate growth of the double pfeA-pirA mutant although, like its synthetic analogues, it stimulated growth of the corresponding single mutants."].
- Fluorescent-sensor binding study (UniProt IDA for enterobactin binding)
  [PMID:35101443 "First, the EcoFepA orthologs KpnFepA1658 (82% identity) and PaePfeA (61% identity) had the same ligand preferences as EcoFepA (FeEnt > FeEnt∗ > FeGEnt)."].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN004738955 | GO:0015344 siderophore uptake transmembrane transporter activity | 4 (PfeA + 3 other PAO1 TBDRs) | 142 (21 taxa) | GO:0015344, IMP, PMID:8419284 (PseudoCAP) | SOUND | Loss of the receptor impairs growth on ferric enterobactin, and the cloned gene restores enterobactin-dependent 55Fe uptake in an E. coli fepA mutant: direct genetic evidence that PfeA transports a ferric siderophore across the outer membrane. The node is a large TBDR clade where siderophore uptake is the expected function (a NOT IRD already blocks one child, PTN004739012). |
| PTN000763909 | GO:0042930 enterobactin transport | 1 (sole seed) | 3 (3 taxa) | GO:0042930, IMP, PMID:8419284 (PseudoCAP) | SOUND | Same evidence; the node holds only the FepA/PfeA ferric-enterobactin receptors (E. coli P05825, Salmonella Q8ZR40, PfeA), for which enterobactin transport is the canonical, experimentally established function. |
| PTN000763909 | GO:0042931 enterobactin transmembrane transporter activity | 1 (sole seed) | 3 (3 taxa) | GO:0042931, IMP, PMID:8419284 (PseudoCAP) | SOUND | As above. GO:0015620 ferric-enterobactin transmembrane transporter activity would name the iron-loaded substrate more exactly, but GO:0042931 sits under siderophore-iron transmembrane transporter activity and is acceptable. |

Not a seed, but noted: the GO:0042912 colicin transmembrane transporter activity
IBA at PTN000763909 (seeded by E. coli FepA, a colicin B/D receptor) is propagated
to PfeA without evidence; P. aeruginosa is not a colicin target in the literature
reviewed. Marked over-annotated (with the inferred bacteriocin transport row).

## Decisions summary

- ACCEPT: cell outer membrane (IBA, IEA), enterobactin transport (IBA, IMP),
  siderophore transmembrane transport (IBA), siderophore uptake transmembrane
  transporter activity (IBA, IEA, IMP), enterobactin transmembrane transporter
  activity (IBA, IEA, IMP).
- MODIFY: siderophore-iron transmembrane transporter activity (IEA) -> enterobactin
  transmembrane transporter activity; siderophore transport (IEA, IMP) ->
  enterobactin transport; siderophore-iron import into cell (IEA) ->
  ferric-enterobactin import into cell; outer membrane (IDA) -> cell outer
  membrane.
- MARK_AS_OVER_ANNOTATED: colicin transmembrane transporter activity (IBA),
  bacteriocin transport (IEA).
- REMOVE: signaling receptor activity (IEA, InterPro2GO).
- KEEP_AS_NON_CORE: enterobactin binding (IDA).
- No PSEUDOCAP defect; GO_CENTRAL CHECK (SUSPECTED) for the colicin IBD reaching PfeA.
