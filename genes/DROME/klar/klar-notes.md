# klar (Drosophila melanogaster) review notes

## Session 1 (2026-09-27, claude-code)

Context: founding KASH protein; reviewed for `modules/linc_complex.yaml` (KASH variants) and
`modules/nucleokinesis.yaml` (photoreceptor nuclear migration as a candidate variant).

### Identity and family
- Q9Y0E4, CG17046. UniProt PANTHER PTHR21524:SF5 (the same family UniProt assigns to worm ANC-1,
  named "SPECTRIN REPEAT CONTAINING NUCLEAR ENVELOPE PROTEIN 2"); human nesprin-1/2 are in
  PTHR14514. Only recognizable domain is KASH (IPR012315/PF10541). No PANTHER id asserted in the review.
- Isoforms: alpha (KASH), beta (lipid-droplet domain), gamma, delta/epsilon (per deep research).

### Function (with provenance)
- MTOC-nucleus link for photoreceptor nuclear migration [PMID:14617811 "Here, we show that Klarsicht is required for connecting the microtubule organizing center (MTOC) to the nucleus."].
- KASH domain needed for perinuclear localization [PMID:15579692 "We find that the KASH domain of Klar is critical for perinuclear localization and for function."].
- SUN partner Klaroid [PMID:18820457 "Here, we identify Drosophila Klaroid, a SUN protein that tethers Klarsicht."].
- Isoform targeting [PMID:15647372 "In early embryos, Klar is attached to lipid droplets, a localization mediated by a novel C-terminal domain encoded by an alternatively spliced exon."].
- Muscle nuclear spacing with Msp300 [PMID:22927463 "A novel MSP-300 nuclear ring assembles and anchors the MTs to the nuclear envelope in a Klar- and MSP-300 KASH–dependent manner, mediating MT astral organization around each nucleus."].
- Kinesin-1 co-IP, oskar RNP restraint [PMID:25049271].

### Decisions
- protein binding (Kuduk) -> REMOVE (uninformative; Kud is a LINC regulator).
- lipid transport (IMP, RNAi screen) -> MODIFY to GO:0031887 lipid droplet transport along microtubule.
- locomotion, flight -> MARK_AS_OVER_ANNOTATED (secondary to myonuclear spacing).
- eye morphogenesis, photoreceptor development, visceral muscle development, tube morphogenesis,
  membrane organization, tracheal lumen formation, oskar localization, nucleus organization,
  cytoskeleton organization -> KEEP_AS_NON_CORE.
- tracheal lumen (PMID:15848387): cached text partial; Europe PMC full-text search confirms the
  article mentions klarsicht; deferred to curator.
- NEW GO:0140444 (KASH anchor), consistent with other KASH reviews.

### Module implications
- Klar is a KASH protein whose cytoplasmic region couples to microtubules/MTOC (functional analog of
  UNC-83 and nesprin-4/KASH5 rather than of the actin-binding giant nesprins), yet it shares a
  PANTHER family with ANC-1. The KASH arm is functionally convergent rather than a single
  homologous lineage, as the module notes.
- Isoform switching of the cargo-targeting C-terminus (KASH vs lipid-droplet domain) is a
  Drosophila-specific feature; module variants should attach only the alpha isoform to LINC.
- In muscle, two KASH proteins (Klar, Msp300) act together at one nucleus, like nesprin-1 and
  nesprin-2 in mammals.

### Deep research
- `klar-deep-research-falcon.md` read; consistent (isoform architecture, LD-domain necessity and
  sufficiency from Yu et al. 2011, not cached). Used as retrieval support in the lipid-droplet core function.
