# P58IPK (Q9VHA8): evidence and ProtNLM claim review

P58IPK is a DNAJC3-family cochaperone with tetratricopeptide repeats, an N-terminal signal peptide, and a C-terminal J domain. It assists protein folding in the endoplasmic reticulum through chaperone and unfolded-client interactions. Its secretory targeting is compatible with an ER-lumen cochaperone, while stable ER-membrane attachment is not established.

Exact input: [Q9VHA8](https://www.uniprot.org/uniprotkb/Q9VHA8/entry), 498 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [P58IPK-predictions-source.json](P58IPK-predictions-source.json). Source features: [P58IPK-uniprot.txt](P58IPK-uniprot.txt), with an exact extraction in [P58IPK-sequence-evidence.json](P58IPK-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR051727; DnaJ_C3_Co-chaperones.
DR   InterPro; IPR001623; DnaJ_domain.
DR   InterPro; IPR036869; J_dom_sf.
DR   InterPro; IPR011990; TPR-like_helical_dom_sf.
DR   InterPro; IPR019734; TPR_rpt.
FT   SIGNAL          1..36
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          396..463
FT                   /note="J"
FT                   /evidence="ECO:0000259|PROSITE:PS50076"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | J domain-containing protein | CNN | IPR001623 and the domain feature at residues 396-463 identify a J domain independently of ProtNLM. The name accurately describes architecture without establishing an intrinsic ATPase. |
| Location | Membrane (SL-0162) | UNC | The exact record has a cleavable signal peptide but no retained transmembrane helix. An ER-lumen cochaperone may interact with membrane-associated machinery; no stable membrane localization is established, so the broad membrane claim is unresolved. |
| Location | Endoplasmic reticulum membrane (SL-0097) | UNC | ER targeting is supported but ER membrane and ER lumen are different locations. The J/TPR protein has no retained transmembrane segment in the source record; an ER membrane assignment needs direct association/topology evidence and cannot be validated by the ARBA ER sentence. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0005783 endoplasmic reticulum (IBA): **ACCEPT**. An N-terminal signal peptide and DNAJC3-family J/TPR architecture support the phylogenetically curated ER annotation.
- GO:0005783 endoplasmic reticulum (IEA): **ACCEPT**. The signal peptide and DNAJC3 architecture support ER targeting. The ARBA sentence in UniProt is not treated as experimental localization evidence.
- GO:0012505 endomembrane system (HDA): **KEEP_AS_NON_CORE**. PMID:19317464 is a proteomic localization study; the exact source is abstract-only in the cache. The assignment is retained as compatible high-throughput evidence and does not establish membrane insertion.
- GO:0034975 protein folding in endoplasmic reticulum (IBA): **ACCEPT**. The signal peptide, TPR-repeat substrate-binding architecture, and J domain support the existing IBA role in ER protein folding.
- GO:0051087 protein-folding chaperone binding (IBA): **ACCEPT**. The DNAJC3-family protein contains a J domain at residues 396-463 and TPR repeats. This supports the existing phylogenetic inference of protein-folding-chaperone interaction without calling the protein an ATPase.
- GO:0051787 misfolded protein binding (IBA): **ACCEPT**. The TPR/J architecture supports the existing IBA misfolded-protein-binding inference; binding and delivery to a chaperone are distinct from independent ATP-driven folding.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `P58IPK-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
