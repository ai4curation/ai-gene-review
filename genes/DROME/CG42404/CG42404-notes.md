# CG42404 (Q9VFA8): evidence and ProtNLM claim review

CG42404 is a 1133-residue VWFC-domain protein with a predicted membrane-spanning segment near its N terminus. Its extracellular-domain-like architecture and membrane association are compatible with a cell-surface interaction protein, but ligand specificity, topology, and biological activity are unresolved.

Exact input: [Q9VFA8](https://www.uniprot.org/uniprotkb/Q9VFA8/entry), 1133 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG42404-predictions-source.json](CG42404-predictions-source.json). Source features: [CG42404-uniprot.txt](CG42404-uniprot.txt), with an exact extraction in [CG42404-sequence-evidence.json](CG42404-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR042378; IDD.
DR   InterPro; IPR001007; VWF_dom.
FT   TRANSMEM        103..125
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   DOMAIN          27..92
FT                   /note="VWFC"
FT                   /evidence="ECO:0000259|PROSITE:PS50184"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | VWFC domain-containing protein | CNN | The VWFC domain at residues 27-92 is supported independently by PROSITE PS50184 and InterPro IPR001007. This validates the domain name without specifying a von Willebrand factor function. |
| Location | Membrane (SL-0162) | CNN | The Phobius transmembrane segment at residues 103-125 supports the broad membrane location already represented by curated IBA. It does not establish secretion as a soluble protein. |
| Keyword | Signal (KW-0732) | UNC | The source record contains an internal transmembrane segment but no cleavable signal-peptide feature. A signal anchor can route a membrane protein without a cleaved N-terminal signal peptide; the emitted Signal keyword requires a resolved N terminus and topology. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. A VWFC domain does not specify a ligand or a receptor activity for this fly product.
- GO:0005575 cellular_component (ND): **MODIFY**. The exact record carries a Phobius transmembrane segment at residues 103-125 and a curated IBA membrane annotation. The broad membrane term is supported without identifying a particular organelle.
- GO:0008150 biological_process (ND): **ACCEPT**. Domain and topology evidence do not establish a developmental or signaling pathway.
- GO:0016020 membrane (IBA): **ACCEPT**. A predicted membrane-spanning segment at residues 103-125 is consistent with the existing phylogenetically curated membrane annotation; specific topology and tissue function are unresolved.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG42404-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
