# CG32086 (M9NF85): evidence and ProtNLM claim review

CG32086 is a 475-residue EFHB-related protein with a C-terminal EF-hand domain. Its architecture is compatible with a calcium-responsive regulatory role, but calcium binding, a ciliary function, and the precise cellular location of this fly product remain unresolved.

Exact input: [M9NF85](https://www.uniprot.org/uniprotkb/M9NF85/entry), 475 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG32086-predictions-source.json](CG32086-predictions-source.json). Source features: [CG32086-uniprot.txt](CG32086-uniprot.txt), with an exact extraction in [CG32086-sequence-evidence.json](CG32086-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR057428; EFHB_EF-hand_C.
FT   DOMAIN          399..469
FT                   /note="EFHB C-terminal EF-hand"
FT                   /evidence="ECO:0000259|Pfam:PF25325"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | EF-hand domain-containing family member B | CNN | The EFHB C-terminal EF-hand domain PF25325 at residues 399-469 supports the EFHB-family name. This does not establish a calcium-signaling mechanism or specific substrate. |
| Location | Cytoskeleton (SL-0090) | UNC | The EFHB-family architecture does not independently establish attachment to the cytoskeleton. Direct localization or a functionally justified ortholog transfer is required. |
| Location | Cilium axoneme (SL-0304) | UNC | An EF-hand and EFHB-like sequence are insufficient to specify cilium axoneme residence. No exact-target ciliary localization or assembly phenotype is established by the retrieved source record. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

The accession-specific GOA fetch contains no existing annotation rows. The molecular activity remains unresolved; no broad GO root or invented function is added to create apparent coverage.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG32086-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
