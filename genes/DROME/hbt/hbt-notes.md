# hbt (Q9VK03): evidence and ProtNLM claim review

Headbutt is a 451-residue Rost-family protein with six predicted transmembrane helices. It is an integral membrane protein with an unresolved molecular activity and biological role for this isoform.

Exact input: [Q9VK03](https://www.uniprot.org/uniprotkb/Q9VK03/entry), 451 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [hbt-predictions-source.json](hbt-predictions-source.json). Source features: [hbt-uniprot.txt](hbt-uniprot.txt), with an exact extraction in [hbt-sequence-evidence.json](hbt-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR049352; Rost.
FT   TRANSMEM        40..63
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        75..98
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        123..145
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        157..177
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        184..205
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        228..250
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | The nonspecific name is consistent with unresolved molecular activity but is not a testable prediction. Rost-family membership does not itself establish a transported substrate. |
| Location | Membrane (SL-0162) | CNN | Six predicted membrane-spanning helices strongly support the broad membrane claim already present as a curated ISS annotation. This does not specify a membrane or transport mechanism. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. Six membrane-spanning segments and a Rost-family domain do not establish a transporter substrate or catalytic activity.
- GO:0008150 biological_process (ND): **ACCEPT**. The exact Headbutt isoform lacks a sufficiently grounded physiological function in the retrieved evidence.
- GO:0016020 membrane (ISS): **ACCEPT**. The six Phobius transmembrane segments between residues 40 and 250 independently support the existing ISS membrane annotation. The membrane identity and transport activity are unresolved.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `hbt-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
