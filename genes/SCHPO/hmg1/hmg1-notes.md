# SCHPO hmg1 PAINT re-review

## 2026-10-24

- Re-ran `just fetch-gene SCHPO hmg1`; the seeded GOA, UniProt, and review YAML
  were current.
- Re-ran the project default Falcon deep-research command:
  `just deep-research-falcon SCHPO hmg1`. The wrapper extracted the UniProt
  context for Q10283 but no provider was available because the required remote
  research API keys were unset.
- Checked the cached hmg1 publications used by the review:
  - PMID:16270032 is a budding-yeast INSIG/Nsg paper. It supports the broader
    fungal INSIG/sterol-sensing-domain context but is not direct evidence for
    the S. pombe Hmg1 catalytic mechanism.
  - PMID:16823372 is the ORFeome localization screen that placed Hmg1 in the ER.
  - PMID:19041767 is the direct fission-yeast mechanism paper: Ins1 binds Hmg1,
    Hmg1 remains stable rather than undergoing Insig-dependent degradation, and
    Ins1 promotes S1024/T1028 phosphorylation in the catalytic domain to raise
    the apparent KM for NADPH and lower HMG-CoA reductase activity.
  - PMID:19486165 identifies the `hmg1-1`/`its12` mutation and supports Hmg1 as
    the essential ER/nuclear-envelope sterol-biosynthetic HMGR.
  - PMID:20576575 uses partially purified S. pombe HMGR as an inhibitor assay.
  - PMID:21680738 connects glucose withdrawal to Ins1-dependent Hmg1
    phosphorylation, Ppe1/Sds23, lower HMGR activity, and restraint of sterol
    intermediate accumulation under nutrient limitation.
- Searched for newer S. pombe hmg1 work. A 2026 bioRxiv preprint,
  `DOI:10.64898/2026.05.18.725815`, reports that a fission-yeast
  nucleus-vacuole junction enriches Hmg1 and Ins1 in a nutrient-regulated
  Snd302-dependent manner. It refines where Hmg1 can concentrate within the
  nuclear-envelope/ER system but does not support the current peroxisomal
  membrane IBA.
- Aligned the IBA calls with `interpro/panther/PTHR10572`. The exact
  `GO:0004420` node `PTN000060346`, the ER-membrane node `PTN000060347`, and
  the fungal ergosterol node `PTN000832055` are sound for this canonical long
  fungal HMG-CoA reductase. The same broad `PTN000060347` node also
  over-propagates `GO:0005778 peroxisomal membrane`; the only seed is human
  HMGCR, and S. pombe Hmg1 is an ER/nuclear-envelope enzyme.
- Kept broad `GO:0008299 isoprenoid biosynthetic process` as core in both the
  PAINT and InterPro2GO rows, matching the existing budding-yeast HMG1/HMG2
  reviews: the term is general but still names the core pathway that Hmg1 feeds
  by producing mevalonate.
