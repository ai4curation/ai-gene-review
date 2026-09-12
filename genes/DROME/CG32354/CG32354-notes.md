# CG32354 (Q9VSK1): evidence and ProtNLM claim review

CG32354 is a 662-residue protein with seven Kazal-like domains and a predicted N-terminal membrane-spanning segment. It is compatible with an extracellular or cell-surface interaction protein; intrinsic protease-inhibitor activity, soluble secretion, and the precise developmental role remain unresolved.

Exact input: [Q9VSK1](https://www.uniprot.org/uniprotkb/Q9VSK1/entry), 662 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG32354-predictions-source.json](CG32354-predictions-source.json). Source features: [CG32354-uniprot.txt](CG32354-uniprot.txt), with an exact extraction in [CG32354-sequence-evidence.json](CG32354-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR002350; Kazal_dom.
DR   InterPro; IPR036058; Kazal_dom_sf.
DR   InterPro; IPR050653; Prot_Inhib_GrowthFact_Antg.
FT   TRANSMEM        57..78
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   DOMAIN          158..214
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          215..268
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          270..322
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          374..432
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          438..495
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          497..550
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          600..652
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Kazal-like domain-containing protein | CNN | Seven domain features and PROSITE PS51465 independently establish the Kazal-like architecture. This validates the domain name without asserting serine-protease inhibition. |
| Location | Secreted (SL-0243) | UNC | The extracellular IBA supports an exposed or extracellular protein region, but the exact source has a transmembrane segment at residues 57-78 and no cleavable signal-peptide feature. An ectodomain on a membrane-tethered protein is not equivalent to soluble secretion; topology or shedding evidence is needed. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0004867 serine-type endopeptidase inhibitor activity (IEA): **UNDECIDED**. Repeated Kazal-like domains support a protease-interaction hypothesis, but the exact inhibitory loops and target protease have not been functionally resolved. This fold also occurs in non-inhibitory extracellular proteins.
- GO:0005576 extracellular region (IBA): **ACCEPT**. Seven Kazal-like domains and an N-terminal hydrophobic segment support the existing curated IBA extracellular localization. This does not imply release as a soluble secreted protein.
- GO:0030154 cell differentiation (IBA): **UNDECIDED**. Extracellular Kazal-domain proteins can have regulatory or structural functions; family architecture does not establish which differentiation process this fly protein participates in. The ancestral assertion and target function need resolution.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG32354-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
