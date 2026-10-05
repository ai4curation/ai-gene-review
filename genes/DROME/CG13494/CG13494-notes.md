# CG13494 (Q8MZA7): evidence and ProtNLM claim review

CG13494 is a 120-residue protein with a predicted transmembrane helix at residues 37-61. It is a plausible small membrane protein whose molecular activity and cellular role are unresolved.

Exact input: [Q8MZA7](https://www.uniprot.org/uniprotkb/Q8MZA7/entry), 120 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG13494-predictions-source.json](CG13494-predictions-source.json). Source features: [CG13494-uniprot.txt](CG13494-uniprot.txt), with an exact extraction in [CG13494-sequence-evidence.json](CG13494-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
FT   TRANSMEM        37..61
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | Uncharacterized protein is suitably nonspecific but contains no testable functional hypothesis. |
| Location | Membrane (SL-0162) | COR | The 25-residue predicted transmembrane segment at residues 37-61 supports a membrane-associated product. This is sequence-based inference rather than measured localization and does not identify the membrane or topology. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

The accession-specific GOA fetch contains no existing annotation rows. The molecular activity remains unresolved; no broad GO root or invented function is added to create apparent coverage.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG13494-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
