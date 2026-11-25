# pen-2 (Drosophila melanogaster, Q86BE9) notes

## Identity
- Small two-TM hairpin subunit of gamma-secretase; required for presenilin endoproteolysis and activation of the complex.

## Literature
- [PMID:12110170 "RNAi-mediated inactivation of aph-1, pen-2, or nicastrin in cultured Drosophila cells reduces gamma-secretase cleavage of betaAPP and Notch substrates and reduces the levels of processed presenilin."]
- [PMID:12660785 "Depletion of PEN-2 by RNA interference prevents endoproteolysis of presenilin and promotes stabilization of the holoprotein in both Drosophila and mammalian cells"]; [PMID:12660785 "PEN-2 is required for endoproteolytic processing of presenilin and conferring gamma-secretase activity to the complex"].
- [PMID:20421416 "coexpression of these four components promotes the efficient assembly of mature, proteolytically active gamma-secretase"].

## Curation thoughts
- Activator role: positive regulation of endopeptidase activity (IMP) accepted; endopeptidase activator activity (GO:0061133, as for human PSENEN) used as core MF.
- Shared gamma-secretase terms treated as for Nct and aph-1.

## 2026-10-12: why core_functions asserts no location
- The core location is given by `in_complex: GO:0070765 gamma-secretase complex`, which is part_of membrane. The two generic `membrane` rows are MODIFY'd to that complex.
- pen-2 has no plasma membrane annotation. Its compartment annotations are late endosome and recycling endosome (IDA, PMID:20421416). They are kept as non-core because gamma-secretase is spread across the plasma membrane and endolysosomal compartments, and no single compartment defines it. So no location is asserted, consistent with aph-1.
