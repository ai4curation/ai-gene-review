# GND1 (YHR183W, UniProt P38720) notes

Module: `pentose_phosphate_pathway` (6PGD step, RXN-9952). YeastCyc pathway page lists RXN-9952 with no gene; the SGD GO-CAM conversion nevertheless includes GND1/GND2.

## Evidence journal
- Major isoenzyme: gnd1 removes ~80% of 6PGD activity, no growth on glucono-delta-lactone [PMID:1328471 "The gnd1 mutation, responsible for an approximately 80% loss of 6-phosphogluconate dehydrogenase activity and the inability of the cells to grow on delta gl"].
- NADP-dependent oxidative decarboxylation, Km NADP 35 uM, homodimer, cytoplasm, 101000 molecules/cell [UniProt:P38720].
- Oxidative stress IMP from PMID:9480895 (abstract is about G6PDH-deficient cells; GND1 data presumably in full text) -> non-core.

## Curation decisions
- Core MF GO:0004616, BP GO:0009051, CC cytosol. YeastPathways "cytosol" is correct here.
- Mitochondrion HDA (3 proteomics papers): MARK_AS_OVER_ANNOTATED (abundant cytosolic contaminant).
- ARBA GO:0016614 -> MODIFY to GO:0004616. NADP binding -> non-core.
