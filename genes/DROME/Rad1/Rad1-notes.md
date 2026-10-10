# Rad1 (Drosophila RAD1) review notes

## Literature journal
- 9-1-1 complex: [PMID:22666434 "Our results demonstrate for the first time that it is possible to co-precipitate DmRad9 with DmRad1 (Figure 3) and Hus1, indicating that DmRad9 forms a complex with DmRad1 and DmHus1."]
- Localization: [PMID:22666434 "We also found that GFP-tagged DmRad1 was localized throughout the entire S2R+ cell"]
- No Drosophila Rad1 mutant phenotype was found in the cached literature; repair/checkpoint roles are inferred from the 9-1-1 complex and the hus1 mutant [PMID:19501158 "Together, our results imply that hus1 is required for repair of DSBs during meiotic recombination."].

## Curation decisions
- All checkpoint, repair, complex, nucleus and nuclear envelope annotations accepted; cytoplasm kept as non-core.
- Core: 9-1-1 clamp subunit (MF approximated by GO:0030674) in DNA damage checkpoint signaling.

## Deep research (falcon) update
- Consistent with the review: Rad1 is a non-enzymatic PCNA-like 9-1-1 subunit [file:DROME/Rad1/Rad1-deep-research-falcon.md "Its principal proposed role is to help form a ring that can surround DNA and organize checkpoint signaling and DNA-repair factors at damaged or incompletely replicated DNA."]; yeast two-hybrid shows a strong Hus1-Rad1 interaction (Abdu et al. 2007). Not to be confused with yeast RAD1 (fly MEI-9).
- Review follow-up: the core MF GO:0030674 is asserted with contributes_to_molecular_function, not molecular_function. Rad1 is a PCNA-like ring subunit; the recruitment-platform (adaptor) activity belongs to the assembled 9-1-1 clamp, and no experiment shows this subunit bridging macromolecules on its own (unlike Rad9, whose C-terminal extension targets the complex). This matches how RnrS models its complex-level activity.
