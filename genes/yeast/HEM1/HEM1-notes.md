# HEM1 (YDR232W) notes

UniProt P09950, 5-aminolevulinate synthase, mitochondrial (EC 2.3.1.37) [UniProt:P09950].

- Purified from mitochondria; PLP essential; hemin-inhibited [PMID:6381051 "5-Aminolevulinate synthase from yeast mitochondria has been purified to homogeneity for the first time."; "Pyridoxal 5'-phosphate has been shown to be an essential cofactor."].
- Matrix import/processing [PMID:3023841 "The enzyme is synthesized as a precursor in the cytoplasm and imported into the matrix of the mitochondria, where it is processed to its mature form."].
- hem1 mutants: heme-less, grow on ALA, methionine-requiring due to siroheme loss [PMID:323256 "hem1 mutants grew on delta-aminolevulinate and lacked delta-aminolevulinate synthase activity"]. => tetrapyrrole (heme + siroheme) biosynthesis accepted.
- Overexpression raises ALA but not heme -> ALA synthesis not rate limiting in yeast [PMID:24173275].
- YeastPathways RCA cytosol (PWY3O-50, PWY3O-69) is wrong (matrix enzyme) -> REMOVE.
- Bouchez 2020 positive regulation of organelle assembly IMP: hem1 strain used as heme-titration tool; effect is via heme/Hap4 -> MARK_AS_OVER_ANNOTATED.
- PANTHER subfamily on UniProt record is PTHR13693:SF102 (labelled 2-amino-3-ketobutyrate CoA ligase) although IBA uses ALAS node PTN000343737 [UniProt:P09950].
