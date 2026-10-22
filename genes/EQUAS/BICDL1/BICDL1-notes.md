# BICDL1 (donkey, A0A9L0JLY3) notes

DONKEY40 cohort review. Evidence: donkey UniProt TrEMBL record (PE 4, predicted; no comment lines), donkey
GOA (2 TreeGrafter IEA rows), human Swiss-Prot Q6ZP65 fetched to `BICDL1-bioinformatics/`, and a
donkey-human pairwise comparison (`BICDL1-bioinformatics/RESULTS.md`). No cached publications exist for this
gene; human BICDL1 functional text is itself transferred from mouse Bicdl1/BICDR-1 (A0JNT9, ECO:0000250).
No deep-research provider call was made.

## Sequence

- 573 aa vs human 573 aa; 95.99% identity over 524 paired residues, 91.45% coverage of each
  [file:EQUAS/BICDL1/BICDL1-bioinformatics/RESULTS.md "with 95.99% identity across 524 paired residues"].
- The donkey model lacks human residues 255-303 (inside the long central coiled coil) and instead contains
  donkey 389-436, which matches the extra exon of human isoform 2 [human UniProt VAR_SEQ 436 "T ->
  TGSRRLDDDSLEEQIRQTSEDSRALRELMEGERGKLRQSLEELQRLH SQ (in isoform 2)"; donkey alignment shows
  SSRRIDDDSLEEQIRQTSEDSRALRELMEGERGKLRQSLEELQRLHSQ]. So the donkey entry is an alternative splice form;
  its effect on adaptor length/dynein recruitment is unknown.
- CC1 box (dynein light intermediate chain binding motif) conserved [RESULTS.md "MOTIF (CC1 box): human
  [113, 114, 115, 116, 117] AARLG -> donkey [114, 115, 116, 117, 118] AARLG."]. C-terminal BICDL1/2-like
  domain (Rab6-binding region in the family) present (donkey 489-541, Pfam PF27654).
- PANTHER PTHR32123:SF12 BICD FAMILY-LIKE CARGO ADAPTER 1.

## Function (transferred)

- Activating dynein adaptor: links dynein to cargo, converts dynein to a processive motor with dynactin,
  recruits two dyneins [human UniProt "Acts as an adapter protein linking the dynein motor complex to various
  cargos and converts dynein from a non-processive to a highly processive motor in the presence of
  dynactin"].
- Rab6 vesicles: pericentrosomal accumulation of Rab6 secretory vesicles, restricting anterograde secretion
  in early neuronal differentiation; regulator of neurite outgrowth [human UniProt "Regulates the secretory
  vesicle transport by controlling the accumulation of Rab6-containing secretory vesicles in the
  pericentrosomal region"].
- Binds RAB6A/B, KIF1C; tripartite complex with dynein and dynactin.

## Decisions

- GO:0047496 vesicle transport along microtubule (TreeGrafter): ACCEPT (core).
- GO:0055107 Golgi to secretory granule transport (TreeGrafter): KEEP_AS_NON_CORE. Rab6 constitutive
  secretory vesicles are not classical secretory granules, and BICDL1 restrains rather than drives their
  anterograde delivery; human carries the same term by ISS.
- NEW GO:0140660 cytoskeletal motor activator activity (ISS from human/mouse).

## ProtNLM2 GO predictions

- GO:0034452 dynactin binding: COR. GO:0005813 centrosome: COR. GO:0031267 small GTPase binding: COR
  (Rab6). GO:0031175 neuron projection development: COR (human ISS same term; mechanism is negative
  regulation of neuritogenesis). All absent from donkey GOA; all ultimately rest on mouse experiments.
