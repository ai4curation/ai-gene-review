# pldA (PA3487, Tle5a) review notes

UniProt: Q9HYC2 (unreviewed, 1099 aa), "Phospholipase D". Locus PA3487.
Literature names: **PldA**, Tle5a.

## What is established

- PldA is a eukaryotic-type phospholipase D with calcium-regulated activity,
  localised to the periplasm of the producing cell, and the gene is present
  only in some strains, always linked to vgrA1 and ORF4
  [PMID:11136451 "The pldA gene was cloned and shown to express an approximately
  116 kDa protein with calcium-regulated PLD activity that is localized to the
  periplasm."].
- PldA is Tle5PA: purified protein releases choline from phosphatidylcholine in
  a manner that depends on a catalytic histidine
  [PMID:23552891 "Consistent with prior observations, Tle5PA catalyzes the release
  of choline from phosphatidylcholine (PC), in a manner dependent upon a predicted
  catalytic histidine residue (His855)"], and in vivo its unchecked action
  converts phosphatidylethanolamine to phosphatidic acid in the target cell
  [PMID:23552891 "Taken together, these data strongly suggest that Tle5PA-imposed
  cell death occurs through PA accumulation via PLD activity, primarily directed
  against PE."].
- The crystal structure confirms the eukaryotic-like HKD catalytic core
  [PMID:36216841 "As noted, as a member of the PLD family, PldA possesses the highly
  conserved HxK(xxxx)nD consensus sequence."] and broad phospholipid substrate
  tolerance.
- Delivery into prey cells requires VgrG4b and the H2-T6SS
  [PMID:31417515 "Here, we show that the lack of PldA secretion is solely due to the
  absence of VgrG4b since PldA release is restored by complementing the vgrG4b mutant
  (Figure 1A, middle panel, lane 6)."].
- UniProt Q9HYC2 has two PLD phosphodiesterase domains (162-189, 850-877) with
  predicted active-site residues 167/169/174 and 855/857/862 - matching His167
  and His855 of the Russell et al. mutagenesis.

## Locus identity: PA3487 is pldA, PA5089 is pldB

The strain table of PMID:31417515 lists `pldA (PA3487)` and `pldB (PA5089)`
separately ["Deletion in rsmA, pldA-tli5a (PA3487-PA3488)"; "vgrG5 (PA5090, blue)
is encoded directly upstream of pldB (PA5089, cyan)"]. This matters because the
PseudoCAP seed row on PA3487 cites PMID:24832454, whose abstract states that the
work characterises PldB ["Here we describe the characterization of a P. aeruginosa
H3-T6SS-dependent phospholipase D effector, PldB, and its three tightly linked
cognate immunity proteins."]. The claim (PldA is a phospholipase D) is true and
well supported by PMID:11136451 and PMID:23552891; it is the citation that is
misdirected, so this is recorded as a `PSEUDOCAP` `WRONG_REFERENCE` defect rather
than a change of action. Confidence is `PROBABLE`: the abstract positively states
whose characterisation the paper reports, but the full text is not cached and
could contain PldA experiments as well.

## Literature search

Europe PMC, 2026-11-05: `aeruginosa AND (PldA OR PldB) AND "phospholipase D"`,
`AUTH:"Wilderman PJ" AND phospholipase`, `TITLE:"type VI secretion phospholipases"
AND Russell`, `aeruginosa AND PldA AND trans-kingdom`. Relevant hits cached:
PMID:11136451, PMID:23552891, PMID:31417515, PMID:36216841, PMID:24832454.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004499769 | GO:0004630 D-type glycerophospholipase activity | 24 | 713 (91 taxa) | GO:0004630, IMP, PMID:24832454 (PseudoCAP) | WRONG (citation) / claim SOUND | The term is right for PA3487: purified PldA/Tle5PA hydrolyses phosphatidylcholine and phosphatidylethanolamine, with His855 required, and the structure shows the HKD core. But the cited paper characterises PldB (PA5089), not PldA, and the same row with the same PMID also sits on PA5089. The defect is the reference, not the term, so the row keeps its action and PseudoCAP is asked to re-point it to PMID:23552891 (or PMID:11136451). | Human PLD1 (Q13393), yeast SPO14 (SGD:S000001739), rat Pld1/Pld2 (RGD:3349, RGD:3350), mouse (MGI:109585, MGI:892877), ten Arabidopsis PLDs, zebrafish, Dictyostelium, PomBase SPAC2F7.16c, Candida, and PA5089/pldB | Yes. The IBD would stand on the characterised eukaryotic PLDs alone, and the PAO1 claim itself is true on better references, so no `GO_CENTRAL` defect. |

The second IBD at this node, GO:0009395 phospholipid catabolic process (4
eukaryotic seeds, no PAO1 seed), propagates an endogenous lipid-turnover process
to a secreted interbacterial toxin. Handled as `MARK_AS_OVER_ANNOTATED` with a
`propagation_review` on the leaf row, consistently with genes/PSEAE/PA5089; the
node term remains defensible for the eukaryotic members that seeded it, so no
upstream defect is filed.
