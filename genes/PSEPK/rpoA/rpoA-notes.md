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

## 2026-11-13 cross-subunit alignment with E. coli K-12

Re-reviewed alongside the new E. coli K-12 rpoA/rpoB/rpoC/rpoZ reviews so that
both species follow one policy (projects/PROTEIN_COMPLEX_FUNCTIONS.md). The
earlier "accept polymerase activity on every subunit" convention is retired:
GO:0003899/GO:0034062 are MARK_AS_OVER_ANNOTATED on alpha and omega; on beta and
beta-prime GO:0003899 is accepted and GO:0034062 is MODIFY to GO:0003899. The
proposed complex row now uses GO:0000345 (the eubacterial RNAP) instead of the
pan-domain parent GO:0000428. Omega's core function is GO:0001000 core enzyme
binding (NEW, from HAMAP MF_00366 and the E. coli experimental evidence);
beta-prime's core functions are contribution to GO:0003899 plus Mg(2+) binding,
with structural Zn(2+) binding kept as non-core.
