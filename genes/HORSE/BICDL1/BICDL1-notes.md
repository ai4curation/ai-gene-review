# BICDL1 (horse, F6SAQ3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New folder created with `just fetch-gene HORSE F6SAQ3 --alias BICDL1`; stub id confirmed F6SAQ3.
ProtNLM2 output was not consulted.

Deep research: `just deep-research-falcon HORSE BICDL1 --fallback perplexity-lite` failed
(falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). No
deep-research file exists; review is based on cached primary literature.

### Identity
- F6SAQ3 is 574 aa, full length. Aligns end to end with human Q6ZP65 (573 aa, 96.5% identity,
  no unpaired segment) and mouse A0JNT9 (577 aa, 95.1%). Not a fragment or alternative isoform.
  [file:HORSE/BICDL1/BICDL1-bioinformatics/RESULTS.md]
- PANTHER PTHR32123:SF12 (BICD family-like cargo adapter 1), same subfamily as mouse, human,
  zebrafish and Xenopus BICDL1. BICDL2 = SF11, Spindly = SF9. IBA rows come from PAINT node
  PTN001281025 (Deuterostomia), seeded by MGI:1922915 (mouse) and ZFIN bicdl1.
- Mouse K512 (Rab6 binding) -> horse K510; mouse W166 (cryo-EM coiled-coil registry) -> horse W164.

### Literature
- Schlager 2010 [PMID:20360680 "the conserved C-terminal domain of BICDR-1 directly binds to Rab6A and
  Rab6B"]; dynein/dynactin binding, KIF1C binding, pericentrosomal localisation, restricts Rab6/NPY
  vesicle delivery to neurites.
- Schlager 2014 [PMID:25176647 "BICD-related protein 1 (BICDR-1) accelerates minus-end-directed vesicle
  movements"].
- Urnavicius 2018 [PMID:29420470 "both BICDR1 and HOOK3 preferentially recruit two"] (mouse BICDR1).
- Chaaban & Carter 2022 [PMID:36071160] tandem BICDR adaptors on microtubule-bound dynein-dynactin.
- Mouse Bicdl1 point-mutant retinal phenotype [PMID:42774019] is downstream organismal phenotype; not annotated.

### Decisions
- GO:0047496 vesicle transport along microtubule (IBA): ACCEPT, core.
- GO:0055107 Golgi to secretory granule transport (IBA): KEEP_AS_NON_CORE; BICDL1 moves post-Golgi
  carriers rather than sorting into granules.
- NEW (ISS from mouse, SF12): GO:0140660 cytoskeletal motor activator activity; GO:0031267 small GTPase
  binding (Rab6; GO:0017137 is obsolete); GO:0005813 centrosome.
- No neuron projection development / neuritogenesis term proposed: that is a downstream effect of
  overexpression/knockdown, not executed work.

### Relative
- Closest experimentally characterised relative: mouse Bicdl1 A0JNT9 (same SF12, PAINT seed, used in
  all structural work). No review in repo for mouse Bicdl1 or human BICDL1 (Q6ZP65).
- No PANTHER family review (only metadata/entries/paint tsv) under interpro/panther/PTHR32123; no modules
  mention BICDL1.
