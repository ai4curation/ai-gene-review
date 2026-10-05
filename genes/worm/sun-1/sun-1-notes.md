# sun-1 (C. elegans) review notes

## Session 1 (2026-09-27, claude-code)

Context: meiotic/embryonic SUN protein partnering the KASH protein ZYG-12; reviewed for
`modules/linc_complex.yaml` (SUN component; meiotic variant) alongside human SUN1/KASH5.

### Identity
- Q20924, F57B1.2, also matefin/MTF-1. UniProt PANTHER PTHR12911:SF2 ("SUN DOMAIN-CONTAINING
  PROTEIN 1"), i.e. the SUN1-like subfamily, distinct from UNC-84 (PTHR12911:SF8, Koi-like).
- Type II INM protein [PMID:19759181 "SUN-1 is a type II inner nuclear membrane protein"].

### Function (with provenance)
- Binds ZYG-12 mini-KASH through a luminal region outside the SUN domain
  [PMID:19759181 "The proteins interact in the luminal space of the nuclear envelope via the ZYG-12 mini KASH domain and a region of SUN-1 that does not include the SUN domain."].
- Embryonic centrosome-nucleus attachment [PMID:14697201 "We propose that dynein and ZYG-12 move the centrosomes toward the nucleus, followed by a ZYG-12/SUN-1-dependent anchorage."].
- Meiotic pairing: [PMID:17543861 "the absence of presynaptic homolog alignment"];
  [PMID:19913287 "These connections through the intact nuclear envelope require the SUN/KASH domain protein pair SUN-1 and ZYG-12."] (fetched this session, PubMed-verified);
  [PMID:19913286 "They bridge the nuclear envelope, connecting the cytoplasm and the nucleoplasm to transmit forces that allow chromosome movement and homolog pairing and prevent nonhomologous synapsis."] (fetched, abstract only).
- Embryonic telomere anchoring with POT-1 [PMID:24297748].
- CED-4 NE receptor in apoptosis [PMID:16938876] (single study).
- Centrosome duplication suppressor [PMID:17446307].

### Decisions
- protein binding: ZYG-12 -> GO:0140444; CED-4 -> GO:0043495.
- intracellular protein localization -> MODIFY GO:0090435.
- GO:0034993 IBA ACCEPTED (contrast with UNC-84, where it was moved to GO:0106094).
- NEW: GO:0007129 homologous chromosome pairing at meiosis; GO:0005637 INM; GO:0034398 telomere tethering at nuclear periphery.
- Embryo development, regulation of centrosome duplication -> KEEP_AS_NON_CORE.

### Module implications
- The worm splits SUN functions between paralogs: UNC-84 (somatic nuclear migration/anchorage) and
  SUN-1 (meiotic chromosome movement, embryonic centrosome attachment). In human, SUN1 does both
  meiotic and somatic work. The SUN-1/ZYG-12 pair is the worm counterpart of SUN1/KASH5, and
  supports a C. elegans meiotic variant in `linc_complex`.
- C. elegans attaches pairing centers, not telomeres, in meiosis, so GO:0070197 (used for human
  SUN1) does not fit exactly; GO:0007129 was used instead.
- SUN-1 binds ZYG-12 outside its SUN domain, an exception to the canonical SUN-domain-KASH groove
  model in the module.

### Deep research
- `sun-1-deep-research-falcon.md` read; consistent. It adds lamin binding in vitro (Zuela 2016),
  MJL-1 at pairing centers (Kim 2023) and oocyte nuclear collapse after lamin loss (Liu 2023); not
  cached and not annotated.
