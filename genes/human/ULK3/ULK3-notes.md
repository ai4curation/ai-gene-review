# ULK3 manual review notes

- Ran `just paint-losses human ULK3` with the retained shared environment on
  2026-11-21. PAINT reports no IRD or IKR loss on the ULK3/Q6PHR2 lineage, so
  the autophagy IBA rows still exported from PTHR24348 have to be judged as
  ordinary over-propagation rather than as stale rows withdrawn by a newer loss.

- Direct ULK3 mechanism: PMID:19878745 cloned human ULK3, showed that ULK3 is
  autophosphorylated and phosphorylates GLI proteins in vitro, and found that
  ULK3 catalytic activity positively regulates GLI reporter output. PMID:20643644
  showed that SUFU binds the ULK3 kinase domain, blocks ULK3
  autophosphorylation, and suppresses its ability to phosphorylate and activate
  GLI proteins. PMID:31279575 tied ULK3 to the conserved Fused-family Ci/GLI
  phosphorylation mechanism downstream of Hedgehog stimulation.

- Autophagy scope: the PTHR24348 PAINT nodes PTN000681272 and PTN000681273 are
  dominated by canonical Atg1/ULK1/ULK2 autophagy biology. ULK3 has direct
  evidence for inducing autophagy on overexpression in the senescence paper
  (PMID:19279323) and in CSL-depleted or ULK3-overexpressing fibroblasts
  (PMID:28877478), but neither cached source establishes ULK3 as the endogenous
  phagophore-localized initiating kinase for autophagosome assembly, mitophagy,
  reticulophagy, or piecemeal microautophagy of the nucleus.

- Protein-binding rows: the SUFU IPI is mechanistically meaningful but has no
  precise existing GO binding term from the ULK3 side; the CDC37 and FKBP5
  interactions are large-scale chaperone/interactome edges. All five GO:0005515
  rows were therefore removed under the protein-binding policy rather than
  converted into untested specific functions.

- CAF and senescence rows: PMID:28877478 supports a non-core role for ULK3 in
  GLI-dependent cancer-associated fibroblast activation after CSL loss, while
  the same paper separates the ULK3/autophagy arm from the CAF effector program
  and reports that CSL-loss senescence markers are still induced when ULK3 is
  silenced. PMID:19279323 supports overexpression-induced autophagy and
  senescence from the abstract, but the senescence process row is best treated
  as an over-annotation of that gain-of-function phenotype.
