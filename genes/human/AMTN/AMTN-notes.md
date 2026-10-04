# AMTN (Q6UX39) review notes

## 2026-10-04: PAINT/affinage review

AMTN (amelotin) is a secreted enamel basal-lamina protein that promotes hydroxyapatite mineralization.
- **HA binding:** [PMID:25407797 "The binding affinity of rh-AMTN to HA was found to be comparable to that of amelogenin, the major protein of the forming enamel matrix."]

Decisions:
- **NEW GO:0046848 hydroxyapatite binding (IDA, PMID:25407797).** The ND molecular_function row is MODIFYed to the same term.
  - Comparator check: AMELX carries it (ISS/IEA). DMP1, SPP1, ENAM and ODAM lack it, which I read as missing curation rather than a convention, since the term's definition is exactly what was measured.
- **Cell-cell junction (IBA, IEA, ISS): MARK_AS_OVER_ANNOTATED**, with propagation_review SOURCE_BAD.
  - The rodent IDAs (PMID:16787391) rest on localization to "the internal basal lamina of junctional epithelium". That is a gingival tissue name, not a cell-cell junction.
  - The source is abstract-only, so it is flagged rather than overruled, and raised as a suggested question.
  - This term-name conflation is a candidate case for the proposed gene-confusion project.
- **Protein-binding rows:** REMOVE. FAM20C is the kinase that phosphorylates AMTN as a substrate; BAG6 comes from HuRI.
- **Accepted:** location, mineralization and odontogenesis rows. The ER lumen row (Reactome) is non-core.
