# BAK1 Apoptosis Review Notes

## 2026-09-30

Reviewed the seeded human BAK1 GOA rows against cached primary literature,
Reactome events, UniProt-derived rows, the BAK-mediated apoptosis GO-CAM, the
completed BAX comparator review, and an annotation-reviewer audit.

Key curation decisions:

- Centered the review on BAK as a constitutively mitochondrial outer-membrane
  BCL2-family effector that changes conformation, self-associates, builds BAK
  oligomers, permeabilizes the outer membrane, and releases cytochrome c after
  BID or other BH3-only inputs [PMID:10950869, "Activated tBID results in an
  allosteric activation of BAK, inducing its intramembranous oligomerization
  into a proposed pore for cytochrome c efflux"; PMID:22006182, "active
  Bax/Bak, but not any other Bcl-2 family protein, displays holin behavior"].
- Accepted `GO:0015267 channel activity`, `GO:0015288 porin activity`,
  `GO:0005741 mitochondrial outer membrane`, `GO:0097193 intrinsic apoptotic
  signaling pathway`, `GO:0001836 release of cytochrome c from mitochondria`,
  and `GO:0097145 BAK complex` as core existing assertions. The poxvirus GO-CAM
  also models BAK porin activity at the mitochondrial outer membrane upstream of
  CASP9 in intrinsic apoptotic signaling.
- Removed nearly all generic `GO:0005515 protein binding` rows. Direct
  activator BH3 rows were tightened to `GO:0051434 BH3 domain binding`; the rest
  were uninformative duplicates of BCL2-family complexes, BAK self-binding,
  MCL1/BCL-XL sequestration, viral inhibitors, or proteome-scale interaction
  edges.
- Treated BAK self-association as a core pore-assembly function. The accepted
  `GO:0042802 identical protein binding`, `GO:0042803 protein homodimerization
  activity`, and BAK-complex rows reflect BH3/groove dimerization and higher
  oligomers rather than generic complex assembly [PMID:23782464, "BAK and BAX
  orchestrate outer mitochondrial membrane permeabilization (MOMP) during
  apoptosis by forming pores in the membrane"].
- Accepted the BCL2-family complex role because BAK is restrained by direct
  MCL1/BCL-XL sequestration in viable cells until BH3-only proteins displace it
  [PMID:15901672, "Here we show that Bak is subject to a distinctive mode of
  regulation involving its direct sequestration by two of its prosurvival
  relatives"].
- Tightened broad `GO:0006915 apoptotic process`, `GO:0043065 positive
  regulation of apoptotic process`, `GO:0046902 regulation of mitochondrial
  membrane permeability`, `GO:0097190 apoptotic signaling pathway`, and ARBA
  regulation rows to `GO:0097345 mitochondrial outer membrane permeabilization`
  when the row was really describing BAK's direct pore-forming step.
- Removed the PAINT `GO:0043066 negative regulation of apoptotic process`,
  ComplexPortal `GO:0090201 negative regulation of release of cytochrome c from
  mitochondria`, and ComplexPortal `GO:1901029 negative regulation of
  mitochondrial outer membrane permeabilization` rows. BAK is the effector held
  in check by MCL1 or BCL-XL, not the anti-apoptotic activity in those
  inhibited complexes.
- Kept ER calcium, ER-stress apoptosis, IRE1/UPR, UV-response, and chaperone
  rows as non-core where they were compatible with BAK/BAX side biology. Removed
  readout-derived or phenotype-level projections such as positive regulation of
  proteolysis from a DEVDG caspase reporter [PMID:18387192], cellular response
  to mechanical stimulus from a BAD prostate-cancer study [PMID:19593445], and
  generic endocrine-pancreas, xenobiotic, ethanol, regeneration, transport, or
  intracellular-signaling electronic imports.
- Replaced the 1998 permeability-transition-era `GO:0046930 pore complex`,
  membrane-potential, and electrochemical-gradient rows with BAK complex or
  negative regulation of mitochondrial membrane potential. The historical paper
  reported recombinant Bax and Bak causing cytochrome-c release and loss of
  mitochondrial potential [PMID:9843949], but BAK should not be curated today as
  a component of a permeability-transition pore complex.
- Left only the VDAC1 `GO:0044325 transmembrane transporter binding` row
  undecided because the cached K5/VDAC1 paper is abstract-only and does not
  expose the BAK-specific evidence.
