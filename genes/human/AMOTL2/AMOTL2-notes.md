# AMOTL2 (Q9Y2J4) review notes

## 2026-10-04: PAINT/affinage review

AMOTL2 is a junctional angiomotin-family scaffold with two characterized roles.
- **Actin coupling:** [PMID:28842668 "In this report we show that p100 amotL2 forms a complex with E-cadherin that associates with radial actin filaments connecting cells over multiple layers."]
- **YAP/TAZ retention:** [PMID:23911299 "Here we demonstrate that AMOTL2 robustly co-immunoprecipitates with TAZ, and their interaction is dependent on the WW domain of TAZ and the PPXY motif in the N-terminus of AMOTL2."]

Decisions:
- **YAP1 and TAZ protein-binding rows (x3): MODIFY to GO:0050699 WW domain binding.**
- **Positive regulation of protein localization (IDA): MODIFY to GO:1900181 negative regulation of protein localization to nucleus.** AMOTL2 keeps TAZ out of the nucleus.
- **63 protein-binding rows: REMOVE.** These are 47 from HuRI, other Y2H/variant screens, the LL5beta co-purification and the RSV matrix screen. None has a PDZ partner, so no PDZ MODIFY applies, even though the C-terminal motif exists.
- **Accepted:** Hippo, junction, actin, podosome and cytoplasm rows.
- **Kept as non-core:** family IBAs (angiogenesis, migration, polarity, vesicle), endothelial morphogenesis, recycling endosome, transcription regulation, and the ortholog-only binding rows.

## Round 1 (PR #4045 review)

- **Family IBAs now cite AMOTL2-specific papers**, not the generic affinage sentence:
  - angiogenesis: PMID:21937427, PMID:24806444;
  - polarity and ameboid migration: PMID:21937427, PMID:25080976, PMID:37443716;
  - migration: PMID:21937427;
  - vesicle: PMID:25080976, PMID:22362771.
- **Recycling endosome rows** now cite PMID:22362771 (Amotl2 traps beta-catenin in Rab11-positive recycling endosomes).
- **GO:0042802 identical protein binding: now ACCEPT.** The p60 isoform binds the p100 isoform (PMID:37443716), which is a functional interaction.
- **GO:0016324 apical plasma membrane: now MARK_AS_OVER_ANNOTATED.** No human observation supports it, and UniProt records none.
- **GO:0000122: now MARK_AS_OVER_ANNOTATED.** Its effect on transcription is only indirect.
- **Core actin function** also cites the VE-cadherin study (PMID:24806444).
