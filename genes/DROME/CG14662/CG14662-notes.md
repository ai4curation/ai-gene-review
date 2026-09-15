# CG14662 (Q9VN74): evidence and ProtNLM claim review

CG14662 is a 550-residue leucine-rich-repeat protein with two predicted hydrophobic membrane-spanning segments. It is a plausible membrane interaction protein, while ligand recognition, membrane topology, and physiological function remain unresolved.

Exact input: [Q9VN74](https://www.uniprot.org/uniprotkb/Q9VN74/entry), 550 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG14662-predictions-source.json](CG14662-predictions-source.json). Source features: [CG14662-uniprot.txt](CG14662-uniprot.txt), with an exact extraction in [CG14662-sequence-evidence.json](CG14662-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR032675; LRR_dom_sf.
FT   TRANSMEM        29..50
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        421..447
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | Uncharacterized protein supplies no testable activity claim. The LRR fold suggests an interaction scaffold without specifying ligands. |
| Location | Membrane (SL-0162) | COR | Two independently called Phobius transmembrane segments support the broad membrane hypothesis. The result remains a sequence-based localization inference; it does not identify topology or organelle residence. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. A leucine-rich-repeat scaffold can mediate many interactions and does not establish a specific receptor or ligand-binding activity.
- GO:0005575 cellular_component (ND): **UNDECIDED**. Two Phobius hydrophobic segments at residues 29-50 and 421-447 suggest membrane insertion. The source GOA unknown-component placeholder and sequence-level inference do not resolve localization or topology experimentally.
- GO:0008150 biological_process (ND): **ACCEPT**. Neither an LRR domain nor membrane-spanning architecture identifies the pathway in which this protein acts.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG14662-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
