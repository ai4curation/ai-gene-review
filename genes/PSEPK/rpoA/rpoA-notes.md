# rpoA notes

## 2026-09-01 annotation-reviewer pass

Reviewed every existing GOA-derived row and the previously proposed complex
membership row against Q88QL1 UniProt/HAMAP evidence and the completed
OpenScientist gene report. DNA binding is retained as non-core because the
alpha C-terminal domain contacts promoter DNA; cytoplasm, transcription,
dimerization, and complex membership are retained. GO:0003899 and GO:0034062
are accepted under the repository's current RNA-polymerase-subunit convention,
while core-function synthesis uses `contributes_to_molecular_function` because
RpoA assembles the alpha platform rather than acting as an isolated catalyst.
GO:0065003 is proposed to capture the alpha N-terminal domain's explicit role
in RNA polymerase core assembly.
