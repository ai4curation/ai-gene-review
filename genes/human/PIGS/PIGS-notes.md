# PIGS (Q96S52) review notes

## Summary of verified biology
PIGS is the **PIG-S subunit of the GPI transamidase (GPI-T) complex** (a.k.a.
phosphatidylinositol-glycan biosynthesis class S protein). GPI-T is an ER membrane,
equimolar heteropentameric complex of **PIGK, GPAA1, PIGT, PIGS and PIGU** that
post-translationally attaches a pre-assembled GPI anchor to the C-terminus of GPI-anchored
proteins, replacing the C-terminal GPI-attachment signal peptide.

- **PIGK** is the catalytic (cysteine-protease/transaminase-like) subunit; the catalytic
  triad is C206-H164-N58 [PMID:35165458]. **GPAA1** (M28-peptidase-like) is proposed to
  form the amide bond with the bridging EtNP.
- **PIGS is a required, non-catalytic accessory subunit** — "PIGS is an indispensable
  subunit of GPI-TA activity, although its role is unclear" [PMID:34576938]. Loss of any
  one subunit abolishes activity.
- Topology: multi-pass ER membrane protein; N-terminal TM (19-39) and C-terminal TM
  (518-532), large lumenal domain (40-517) [UniProt; PMID:35165458, PMID:35551457].
- Structures: human GPI-T cryo-EM (PDB 7W72 [PMID:35165458], 7WLD [PMID:35551457],
  8IMX/8IMY liganded [PMID:37684232]).

## Provenance for key claims
- Complex membership + 4 named partners: [PMID:11483512 "we report two new components of
  this enzyme: PIG-S and PIG-T"; "PIG-S and PIG-T form a protein complex with GAA1 and
  GPI8"]. Fifth subunit PIG-U added in [PMID:12802054 "PIG-U and the yeast orthologue
  Cdc91p are the fifth component of GPI transamidase"].
- ER localization of GPI-T: [PMID:15713669 "the five subunits of the ER-localized
  glycosylphosphatidylinositol transamidase complex"]; [PMID:12582175 "GPI transamidase is
  localized in the endoplasmic reticulum and mediates post-translational transfer of
  preformed GPI to proteins"]; cryo-EM structures place complex in ER membrane
  [PMID:35165458, PMID:35551457].
- Function of the complex: [PMID:11483512 "The GPI transamidase mediates GPI anchoring in
  the endoplasmic reticulum, by replacing a protein's C-terminal GPI attachment signal
  peptide with a pre-assembled GPI"].
- PIGS required for activity: [PMID:34576938]; PIGS/PIGT knockout cells defective in GPI
  transfer [PMID:11483512 "PIG-S and PIG-T knockout cells were defective in transfer of GPI
  to proteins"].
- Disease: GPIBD18 (autosomal recessive; developmental delay, seizures, hypotonia)
  [PMID:30269814; UniProt DISEASE].

## Annotation notes
- GOA carries NO catalytic MF term for PIGS. The only MF is `protein binding` (GO:0005515),
  from IntAct/large-scale interactome IPIs (PIGT partner Q969N2, plus keratin-associated
  proteins and other proteins from binary screens). These are uninformative and
  over-annotate a subunit whose real role is complex membership -> MARK_AS_OVER_ANNOTATED
  (per policy: do not REMOVE bare protein-binding IPIs).
- Core BP: GPI anchor biosynthetic process (GO:0006506) and attachment of GPI anchor to
  protein (GO:0016255) / GPI anchored protein biosynthesis (GO:0180046) — all accept.
- Core CC: GPI-anchor transamidase complex (GO:0042765); ER membrane (GO:0005789).
- `membrane` (GO:0016020, HDA, NK-cell membrane proteome PMID:19946888) is a correct but
  unspecific location -> MARK_AS_OVER_ANNOTATED (ER membrane is the informative term).
- Because PIGS is non-catalytic and GOA has no MF, core_functions omits `molecular_function`
  and instead uses directly_involved_in (BP) + locations (ER membrane) + in_complex (GPI-T).
