# FOLH1 (Q04609) — curation notes

Deep-research providers are unavailable in this environment; research is from the cached
publications, the UniProt record and PubMed.

## Protein and localization

PSMA / glutamate carboxypeptidase II is a **type II** single-pass membrane protein: short
cytoplasmic N-terminus, one transmembrane helix, and a large glycosylated extracellular
catalytic domain that homodimerises.
[PMID:12949938 "PSMA is a type II membrane glycoprotein with a short cytoplasmic N-terminal region, a transmembrane domain, and a 701 amino acid extracellular portion with 10 potential N-linked glycosylation sites."]
[file:human/FOLH1/FOLH1-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:9809977}; Single-pass type II membrane protein"]
The alternatively spliced PSMA-prime form is cytoplasmic.
[file:human/FOLH1/FOLH1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform PSMA']: Cytoplasm"]

Localization conclusion: **plasma membrane, catalytic ectodomain extracellular and
surface-accessible** (the basis of PSMA imaging and radioligand therapy). The two
cytoplasm rows are isoform-specific and kept as non-core; the generic membrane rows were
refined to plasma membrane.

## Function

[file:human/FOLH1/FOLH1-uniprot.txt "Has both folate hydrolase and N-acetylated-alpha-linked- acidic dipeptidase (NAALADase) activity."]
[file:human/FOLH1/FOLH1-uniprot.txt "Release of an unsubstituted, C-terminal glutamyl residue, typically from Ac-Asp-Glu or folylpoly-gamma-glutamates."]
[file:human/FOLH1/FOLH1-uniprot.txt "Note=Binds 2 Zn(2+) ions per subunit. Required for NAALADase activity."]
[file:human/FOLH1/FOLH1-uniprot.txt "In the intestine, required for the uptake of folate."]

## Review decisions

- `carboxypeptidase activity` (2 rows) and `peptidase activity` (2 rows) marked
  TOO_GENERAL beside the accepted `metallocarboxypeptidase activity`.
- `dipeptidase activity` kept as non-core: the NAALADase reaction hydrolyses the
  dipeptide NAAG, but mechanistically the enzyme is a carboxypeptidase.
- `positive regulation of glutamate receptor signaling pathway` kept as non-core, because
  the enzyme supplies glutamate rather than participating in receptor signalling, and
  NAAG itself is an mGluR3 agonist so the net direction is context-dependent.
- `intestinal folate absorption` accepted: FOLH1 performs the deglutamylation step
  itself, so this is participation rather than mere necessity.
