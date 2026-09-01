# rpoA notes

## 2026-09-01 annotation-reviewer pass

Reviewed every existing GOA-derived row and the previously proposed complex
membership row against Q88QL1 UniProt/HAMAP evidence and the completed
OpenScientist gene report. DNA binding is retained as non-core because the
alpha C-terminal domain contacts promoter DNA; cytoplasm, transcription,
dimerization, and complex membership are retained. GO:0003899 and GO:0034062
are marked over-annotated with their current `enables` semantics because RpoA
assembles the alpha platform but does not independently catalyze RNA synthesis.
Core-function synthesis therefore uses `contributes_to_molecular_function`.
