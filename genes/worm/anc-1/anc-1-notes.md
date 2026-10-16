# anc-1 (C. elegans) review notes

## Session 1 (2026-09-27, claude-code)

Context: giant KASH protein, nesprin-1/2 ortholog; reviewed for `modules/linc_complex.yaml`
(KASH variants, actin arm) and for comparison with human SYNE1/SYNE2.

### Identity and family
- Q9N4M4, ZK973.6, 8545 aa. UniProt PANTHER: PTHR21524 / PTHR21524:SF5 ("SPECTRIN REPEAT
  CONTAINING NUCLEAR ENVELOPE PROTEIN 2"), the same family that UniProt assigns to Drosophila
  Klarsicht. Human nesprin-1/2 are in PTHR14514 (module notes), so ANC-1 is not in the human
  giant-nesprin PANTHER family despite being called an ortholog. No family id asserted in the
  review. Domains: tandem CH (IPR001715), ANC1 spectrin-like repeats, KASH (IPR012315), and a
  BAG-domain InterPro match (IPR003103) that drives the chaperone-binding IEA.

### Function (with provenance)
- Anchors nuclei and mitochondria [PMID:6889924 "We have isolated five mutants in which the nuclei of certain epithelial cells are not elastically anchored but float freely within the cytoplasm."].
- Classical model: KASH-UNC-84 plus CH-actin [PMID:12169658 "Thus, ANC-1 may connect nuclei to the cytoskeleton by interacting with UNC-84 at the nuclear envelope and with actin in the cytoplasm."].
- Revised model (Hao et al. 2021, PMID:33860766, fetched this session, PubMed-verified): CH domains
  dispensable ["Thus, the CH domains of ANC-1 are not required for hyp7 nuclear anchorage."]; KASH
  deletion mild, like unc-84 null ["Two independent anc-1(ΔKASH) mutants exhibited mild nuclear anchorage defects similar to those observed in unc-84(null) mutants"];
  ANC-1 on ER membranes; ER, mitochondria and lipid droplets unanchored in nulls.
- SUN-KASH cysteines matter for ANC-1 anchorage [PMID:30245107 "Mutations of conserved cysteines in SUN or KASH disrupted ANC-1-dependent nuclear anchorage in C. elegans"] (fetched this session).
- Mild pronuclear migration role [PMID:21798253].

### Decisions
- actin binding (ISS) -> KEEP_AS_NON_CORE (real, but CH domains dispensable for anchorage).
- protein binding with AMPH-1 -> MODIFY GO:0140444 (abstract-only; noted REMOVE as fallback).
- kinesin binding IBA (single Klar donor, oocyte co-IP of non-KASH isoforms) -> MARK_AS_OVER_ANNOTATED with propagation_review.
- protein-folding chaperone binding IEA (BAG InterPro) -> REMOVE.
- nuclear migration IBA/IEA, pronuclear migration, nucleus organization, cytoskeleton organization -> KEEP_AS_NON_CORE.
- NEW: mitochondrion localization, ER localization (IMP), ER membrane (IDA), all from PMID:33860766.

### Module implications
- ANC-1 is the worm counterpart of the module's "nesprin-1/2 actin" KASH variant, but the worm
  data weaken the "actin-binding CH domain + KASH" model: in hyp7 most anchorage is LINC- and
  CH-independent. The module's nesprin_1_2_anchor annoton should not be read as implying the CH
  domain is universally essential.
- in_complex GO:0106094 (defined as linking to microtubules) was not asserted for ANC-1, which
  anchors via actin/ER; the module's use of GO:0106094 for actin-coupled nesprins is a
  terminology stretch worth noting.

### Deep research
- `anc-1-deep-research-falcon.md` read; agrees with the cytoplasmic integrity model and adds
  neuronal mitochondrial positioning (Fischer 2022) and nucleophagy (Papandreou 2023); these were
  not cached and are not annotated here.
