# CG10359 (B7Z0B2): evidence and ProtNLM claim review

CG10359 is a 485-residue secretory-pathway protein with a fibrinogen-like C-terminal domain. Its architecture supports an extracellular interaction role, while ligand specificity, membrane association, and receptor-mediated signaling remain uncertain.

Exact input: [B7Z0B2](https://www.uniprot.org/uniprotkb/B7Z0B2/entry), 485 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG10359-predictions-source.json](CG10359-predictions-source.json). Source features: [CG10359-uniprot.txt](CG10359-uniprot.txt), with an exact extraction in [CG10359-sequence-evidence.json](CG10359-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR036056; Fibrinogen-like_C.
DR   InterPro; IPR014716; Fibrinogen_a/b/g_C_1.
DR   InterPro; IPR002181; Fibrinogen_a/b/g_C_dom.
DR   InterPro; IPR050373; Fibrinogen_C-term_domain.
FT   SIGNAL          1..23
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          263..477
FT                   /note="Fibrinogen C-terminal"
FT                   /evidence="ECO:0000259|PROSITE:PS51406"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Fibrinogen C-terminal domain-containing protein | CNN | PROSITE PS51406 and InterPro IPR002181 independently identify the fibrinogen C-terminal domain at residues 263-477. The domain name is accurate without implying a vertebrate coagulation function. |
| Location | Secreted (SL-0243) | CNN | A Phobius signal peptide at residues 1-23 together with the extracellular fibrinogen-like domain supports secretion. Existing curated extracellular-matrix localization is compatible; secretion does not independently establish matrix binding or a GPCR interaction. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0001664 G protein-coupled receptor binding (ISS): **UNDECIDED**. The ISS assertion is a curated transfer rather than an experiment on this protein. Its fibrinogen-like domain and signal peptide support extracellular biology but do not identify a GPCR partner or establish conserved receptor binding.
- GO:0007186 G protein-coupled receptor signaling pathway (ISS): **UNDECIDED**. The sequence supports a secretory fibrinogen-domain protein but does not establish the receptor or pathway represented by this ISS annotation.
- GO:0008061 chitin binding (ISS): **UNDECIDED**. The extracellular fold permits diverse ligands; target-specific binding or a resolved transfer from a characterized chitin-binding ortholog is needed.
- GO:0016020 membrane (ISS): **UNDECIDED**. The source record contains a signal peptide at residues 1-23 but no retained transmembrane segment. Peripheral membrane binding remains possible; the ISS membrane assertion cannot be resolved from this architecture alone.
- GO:0031012 extracellular matrix (IBA): **UNDECIDED**. The IBA is a curated phylogenetic assertion, but a fibrinogen-like domain and signal peptide alone do not establish matrix residence. PMID:24675716 describes a candidate angiopoietin-like protein without establishing ligand or matrix binding. The relevant ancestral localization inference remains unresolved.

## Research assessment

The Falcon report identifies PMID:24675716 as a primary CG10359 lead. The full text describes CG10359 as a predicted angiopoietin homolog and reports a negative deficiency result in the tested protection assay; it does not establish a receptor-binding function. The report also cites a secretome preprint, but the specific raw B7Z0B2 assignment is not independently verified here and is not counted as experimental proof. Secretion is supported as a sequence-based hypothesis; extracellular-matrix residence and receptor specificity remain unresolved.

Provider output: [CG10359-deep-research-falcon.md](CG10359-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.
