# pqqC curation notes

## 2026-07-20 OpenScientist assessment

- OpenScientist correctly identifies Q88QV6 as the terminal
  pyrroloquinoline-quinone synthase and retrieves the PqqC structural and
  mechanistic literature.
- Its simplified equation, `AHQQ + O2 -> PQQ + H2O2`, is not the curated net
  reaction. UniProt and Rhea 10692 specify three O2 as substrate and two H2O2,
  two H2O, and one proton as products.
- The seven-helix structure and detailed active-site mechanism come from an
  ortholog, while the downstream glucose-dehydrogenase examples cited in the
  report are from Pseudomonas putida S11 and Pseudomonas cepacia rather than
  KT2440. They provide family and physiological context, not direct Q88QV6
  evidence.
- The report is therefore marked `MISCITED`. The core function remains grounded
  in Q88QV6 UniProt/HAMAP, GOA, and the Rhea reaction already represented in the
  reusable module.

