# CG13096 (H0RNN8): evidence and ProtNLM claim review

CG13096 is a 681-residue protein containing ribosomal-uL1-like domains associated with ribosome biogenesis proteins. Its architecture suggests an RNA-associated role, but the exact molecular activity, RNA substrate, and localization of this fly product remain unresolved.

Exact input: [H0RNN8](https://www.uniprot.org/uniprotkb/H0RNN8/entry), 681 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG13096-predictions-source.json](CG13096-predictions-source.json). Source features: [CG13096-uniprot.txt](CG13096-uniprot.txt), with an exact extraction in [CG13096-sequence-evidence.json](CG13096-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR053110; Ribosomal_L1-TF.
DR   InterPro; IPR023674; Ribosomal_uL1-like.
DR   InterPro; IPR028364; Ribosomal_uL1/biogenesis.
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | Uncharacterized protein supplies no testable function. Ribosomal-uL1-like architecture narrows the likely biology but does not establish an intrinsic ribosomal-subunit role. |
| Location | Nucleolus (SL-0188) | UNC | Ribosomal-uL1-like domains occur in ribosome-biogenesis factors and make nucleolar localization plausible. The exact target has no localization experiment or curated GO localization in the retrieved evidence, so nucleolar residence is not established. |
| Location | Nucleus (SL-0191) | UNC | A nuclear location is compatible with ribosome biogenesis but is not established solely by the uL1-like fold. The exact target needs localization or a well-resolved characterized ortholog inference. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

The accession-specific GOA fetch contains no existing annotation rows. The molecular activity remains unresolved; no broad GO root or invented function is added to create apparent coverage.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG13096-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
