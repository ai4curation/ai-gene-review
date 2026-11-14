# PA5089 (pldB, Tle5b) review notes

UniProt: Q9HU94 (unreviewed, 745 aa), "PLD phosphodiesterase domain-containing
protein". Locus PA5089. The literature name is **PldB** (also Tle5b).

## Identity and genomic context

- PA5089 is *pldB*, and PA3487 is *pldA*: the two loci are distinct genes, both
  phospholipase D-family T6SS effectors. The strain table of
  [PMID:31417515 "vgrG5 (PA5090, blue) is encoded directly upstream of pldB (PA5089, cyan)"]
  gives the locus mapping explicitly, as does its
  `PAO1ΔrsmAΔpldAtli5a` entry ["Deletion in rsmA, pldA-tli5a (PA3487-PA3488)"].
- PldB is followed by three cognate immunity proteins, tli5b1-3 (PA5088-PA5086)
  [PMID:24832454 "Here we describe the characterization of a P. aeruginosa H3-T6SS-dependent
  phospholipase D effector, PldB, and its three tightly linked cognate immunity proteins."].
- Secretion requires VgrG5, and killing of competitors is lost without it
  [PMID:31417515 "Remarkably, PldB secretion was abrogated in absence of VgrG5
  (Figure 1B, middle panel, lane 5), while PldB-mediated killing was abolished
  when using attacker strains lacking vgrG5"]. PMID:24832454 attributed delivery
  to the H3-T6SS; PMID:31417515 re-assigns it to the H2-T6SS. This disagreement
  concerns the secretion system, not the enzyme family.

## Family and catalytic motif

- UniProt Q9HU94 carries a PROSITE PLD phosphodiesterase domain (637-664) with
  predicted active-site residues 642, 644 and 649, Pfam PF00614 (PLDc) and
  InterPro IPR001736.
- The Tle5 family is defined by the PLD HKD motif
  [PMID:23552891 "Four of the families (Tle1-4) exhibit the GxSxG motif common in
  esterases and many lipases, while the fifth (Tle5) possesses dual HxKxxxxD motifs
  found in PLD enzymes"]. Note that the enzymology in that paper is on Tle5PA =
  PldA (His167/His855), not on PldB. Q9HU94 shows only one PROSITE-detected HKD;
  no in vitro assay of purified PldB was found.

## Literature search

Europe PMC searches on `aeruginosa AND (PldA OR PldB) AND "phospholipase D"`,
`aeruginosa AND PldB` and `aeruginosa AND PldA AND trans-kingdom` (2026-11-05)
returned PMID:24832454, PMID:23552891, PMID:31417515, PMID:32356524 (immunity
protein structures) and PMID:36216841 (PldA structure); no paper reporting a
purified-PldB phospholipase assay was found.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004499769 | GO:0004630 D-type glycerophospholipase activity | 24 | 713 (91 taxa) | GO:0004630, IMP, PMID:24832454 (PseudoCAP) | SOUND | The cited paper characterises PldB, which is this gene (PA5089), as a phospholipase D effector with antibacterial activity in the prey periplasm, and the protein carries the family's HKD motif. The evidence code is IMP, so the activity itself rests on the family assignment plus the toxicity phenotype rather than on an assay visible in the cached abstract; the claim is nevertheless the family-defining activity and the node term is at exactly that level. | Human PLD1 (Q13393), yeast SPO14 (SGD:S000001739), rat Pld1/Pld2 (RGD:3349, RGD:3350), mouse (MGI:109585, MGI:892877), ten Arabidopsis PLDs, zebrafish, Dictyostelium, PomBase SPAC2F7.16c, Candida, and PA3487/pldA | Yes - comfortably. The characterised eukaryotic PLDs alone place the activity at this node. |

No `GO_CENTRAL` defect for the GO:0004630 IBD. One node-level observation is
recorded instead on the *second* IBD at the same node, GO:0009395 phospholipid
catabolic process (4 eukaryotic seeds, no PAO1 seed): propagating an endogenous
lipid-turnover process term to a secreted interbacterial toxin conflates the
roles. That is handled as `MARK_AS_OVER_ANNOTATED` on the leaf row with a
`propagation_review`, not as an upstream defect, because the node term is
defensible for the eukaryotic members that seeded it.

No `PSEUDOCAP` defect for this gene: the seed row cites the paper about this
locus. (Contrast genes/PSEAE/pldA, where the same PseudoCAP row was copied onto
PA3487 and cites this PldB paper instead of the PldA papers.)
