# ATP5ME notes

## 2026-10-05 review (PAINT, affinage)

- Subunit e of complex V F(o). Dimer stabilization [PMID:42138716 "ATP5I maintains the stability of F₁F₀-ATP synthase dimers, which is crucial for shaping cristae morphology."].
- [Superseded by the revision sections below.] Original call: proton transporter activity (IEA) over-annotated; proton transport (IEA) and complex binding (IEA) non-core. The round-1 revision makes all three over-annotated and drops the 'not in the proton path' argument.
- No NEW cristae-formation or assembly term. Comparator check: QuickGO shows none of the dimer-associated F(o) subunits (ATP5MG/g, ATP5MK/k, ATP5MF/f, ATP5PD/d) carries GO:0042407, GO:0033615 or GO:0065003. Raised as a suggested question.
- Four Y2H/pull-down IPIs (FOS twice, SPG21, CIDEB) removed under policy.

## 2026-10-05 revision (reviewer round 1)

- The location rows now cite the UniProt SUBCELLULAR LOCATION line instead of a wrap fragment.
- The GO:0015078 reason now rests on UniProt's composition statement (the F(o) proton channel is the assembled c, a, 8, e, f, g, k, j sector) and on the evidence being about dimer stability, not conduction. The derived GO:1902600 row (GO_REF:0000108 from GO:0015078) is now also over-annotated, for consistency.
- GO:0044877 (rat IEA) is now over-annotated, matching its reasoning.
- Added NEW GO:0033615 complex assembly (IMP, PMID:42138716): knockout loses subunit g, dimers and monomers become scarce, and intermediates accumulate. This follows the ATP5MD (subunit k) review.
- core_functions now has molecular_function GO:0005198 structural molecule activity (ATP5MD precedent) alongside contributes_to GO:0046933.

## 2026-10-05 revision (reviewer round 2)

- Added GO:0005198 structural molecule activity as a NEW IMP row (PMID:42138716), so the core MF is reflected in existing_annotations, as in ATP5MD.
- Narrowed the suggested question to cristae formation, since GO:0033615 is now proposed.
- Now cites PMID:37244256, UniProt's source for the F(o) composition line.
