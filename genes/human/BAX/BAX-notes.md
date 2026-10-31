# BAX Apoptosis Review Notes

## 2026-09-30

Reviewed the seeded human BAX GOA rows against cached primary literature,
Reactome events, UniProt-derived rows, and PAINT/IEA assertions.

Key curation decisions:

- Centered the review on BAX as a BH3-regulated mitochondrial outer-membrane
  permeabilization effector. The core direct assertions are OMM channel/pore
  activity, cytochrome c release, BAX self-association into the BAX complex,
  and BH3-domain binding to direct activators such as BID and BIM
  [PMID:9219694, "Bax formed pH- and voltage-dependent ion-conducting channels";
  PMID:17052454, "a direct binding interaction between BAX and a hydrocarbon-stapled
  BID BH3 domain"; PMID:18948948, "BIM SAHB binds BAX at an interaction site
  that is distinct from the canonical"].
- Accepted `GO:0005741 mitochondrial outer membrane`, `GO:0015267 channel
  activity`, `GO:0001836 release of cytochrome c from mitochondria`, `GO:0097144
  BAX complex`, and specific BCL2-family complex terms as the most informative
  existing BAX rows. Reactome's BAX activation events also support cytosolic
  inactive BAX and oligomerization at the mitochondrial membrane
  [Reactome:R-HSA-114264, "Activated BAX integrates in the outer mitochondrial membrane";
  Reactome:R-HSA-114275, "BAX forms oligomeric complexes which play an important
  role in cytochrome C release"].
- Removed all 97 `GO:0005515 protein binding` rows. The low-throughput BCL2-family
  edges are either redundant with existing `GO:0051434 BH3 domain binding`,
  `GO:0046982 protein heterodimerization activity`, or complex rows, while the
  proteome-scale maps should not be converted into BAX process inference.
- Treated BAX as upstream of the apoptosome and execution phase. Broad
  `GO:0006915 apoptotic process`, `GO:0043065 positive regulation of apoptotic
  process`, `GO:0097194 execution phase of apoptosis`, and ligand-absence
  extrinsic-pathway rows were tightened to MOMP, cytochrome-c release, or
  intrinsic apoptotic signaling where the source supported a proximal BAX step.
- Tightened the B-cell receptor paper to BCR apoptotic signaling where
  appropriate because that paper specifically reports that "the BCR-signal
  causes Bax translocation" followed by mitochondrial depolarization and cytC
  release [PMID:15214043].
- Changed the two `GO:0008053 mitochondrial fusion` rows to `GO:0010637 negative
  regulation of mitochondrial fusion`; the 2004 dynamics paper is literally
  titled as showing that "mitochondrial fusion is blocked during the Bax
  activation phase of apoptosis" [PMID:14769861].
- Removed the `GO:0005757 mitochondrial permeability transition pore complex`
  row. The isolated-mitochondria paper did report that recombinant Bax and Bak
  induced "loss, swelling, and cytochrome c release" through permeability
  transition pores [PMID:9843949], but later BCL2-family/MOMP curation should
  not make BAX a component of the PTP complex.
- Kept ER localization, IRE1/UPR TAS rows, chaperone binding, BCR signaling,
  neuronal apoptosis, and mitochondrial fragmentation as non-core or peripheral
  rows. The fission-site paper places BAX at apoptotic scission foci
  [PMID:12499352, "Bax foci were also present at mitochondrial constriction
  sites"], but this is not the core pore-forming activity.
- Removed Humanin fiber organization for BAX. Humanin sequesters BAX into fibers
  and blocks BAX MOMP [PMID:31690630, "sequesters it into fibers, preventing
  mitochondrial outer-membrane permeabilization"], so BAX is the restrained
  target, not the organizer of the supramolecular fibers.
- Left four rows undecided where the cached evidence could not verify the exact
  imported annotation: SARS-CoV 7a top-level apoptosis, a cell-screen
  mitochondrial-potential row, a BAD/BCL2/BCL-XL negative regulation of binding
  row, and APP/AICD cell-periphery localization.
