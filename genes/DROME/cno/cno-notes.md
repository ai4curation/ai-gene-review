# cno review notes

## Session 1 (initial review)

- fetch-gene resolved A0A0B4KF82 (FlyBase FBgn0259212, GeneID 40620) as requested; 21 GOA rows.
- Deep research API unavailable; manual summary in cno-deep-research-manual.md.
- Key paper PMID:22024168 (Wee et al. 2011) read in full: Canoe PBD (aa 1755-1950) directly binds
  Pins TPR [PMID:22024168 "We conclude that the CanoePBD directly binds the PinsTPR domain"]; RA
  domains bind RanGTP; Canoe/RanGTP required for Mud cortical recruitment and Pins(TPR)/Mud spindle
  orientation in S2 induced-polarity assay.
- Supporting entities: FBgn0020255 = Ran, FBgn0040080 = pins, FBgn0000229 = bsk,
  FBgn0025743 = mbt (FlyBase API).
- GO:0008536 Ran GTPase binding is merged into GO:0031267 small GTPase binding (QuickGO); used the
  latter for both Ran and Rap1 binding.
- PMID:19596848 (Sawyer 2009) full text: F-actin cosedimentation and PDZ-DEcad pulldown support
  actin filament binding and cadherin binding as NEW MF rows (direct biochemical evidence).
- PMID:23970418 abstract only; the abstract is about Ser in glia; glial proliferation and
  "second mitotic wave involved in compound eye morphogenesis" rows could not be verified -> UNDECIDED.
- Embryonic morphogenesis (Sawyer IMP) refined to ventral furrow formation, head involution,
  dorsal closure (all is_a/part_of descendants of GO:0048598 per QuickGO).
- Did not add NEW BP rows for apical-basal polarity or germband extension (mutant phenotype
  evidence only).
