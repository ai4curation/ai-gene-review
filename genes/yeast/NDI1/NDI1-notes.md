# NDI1 (YML120C, UniProt P32340) notes

Module: `oxphos` (type_II_ndh_variant, internal/matrix-facing NDH-2 exemplar).

## Evidence journal
- Single-subunit FAD enzyme, rotenone-insensitive, NADH-specific; uses ubiquinone-6 [PMID:3138118 "The purified enzyme can use ubiquinone-2, -6 or -10, menaquinone, dichloroindophenol or ferricyanide as electron acceptors, but at different rates."]. Note: this 1988 paper guessed the purified enzyme was the *external* NADH dehydrogenase; the same group then cloned its gene (NDI1) and showed it oxidises matrix NADH [PMID:1900238 "this NADH dehydrogenase catalyzes the oxidation of NADH generated inside the mitochondrion"].
- ndi1 null: growth on lactate, pyruvate, acetate impaired [PMID:1900238 "growth on lactate, pyruvate and acetate is impaired or absent"].
- Non-pumping NDH-2, monotopic, matrix-directed [PMID:22949654 "The Ndi1 protein from Saccharomyces cerevisiae is a monotopic membrane protein, directed to the matrix."]; homodimer via C-terminal membrane anchor [PMID:23086143 "Ndi1 homodimerization through its carboxy-terminal domain is critical for its catalytic activity and membrane targeting"].
- Peripheral inner-membrane protein, matrix side [UniProt:P32340].
- Overexpression -> ROS and apoptosis-like death; deletion extends CLS [PMID:16436509 "overexpression of yeast AMID homologue internal NADH dehydrogenase (NDI1), but not external NADH dehydrogenase (NDE1), can cause apoptosis-like cell death"].

## Curation decisions
- Core MF GO:0120555 (ubiquinone-specific NDH-2), BP GO:0006120, CC GO:0005743.
- REMOVE RCA cytosol (YeastPathways default compartment).
- Generic oxidoreductase activity (IBA/IEA) -> MODIFY to GO:0120555.
- Module uses parent GO:0050136; GOA (IDA, RCA, Rhea IEA) uses the ubiquinone child GO:0120555.
