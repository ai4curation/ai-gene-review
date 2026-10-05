# CG8841 (Q0E9B5): evidence and ProtNLM claim review

CG8841 is an HID1/Ecm30-family protein associated by phylogenetic and similarity inference with Golgi organization, intracellular protein transport, and secretory-granule maturation. Its likely role is in secretory-pathway membrane organization rather than DNA recombination, despite the historical Dmc1 alias; its molecular activity is unresolved.

Exact input: [Q0E9B5](https://www.uniprot.org/uniprotkb/Q0E9B5/entry), 837 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG8841-predictions-source.json](CG8841-predictions-source.json). Source features: [CG8841-uniprot.txt](CG8841-uniprot.txt), with an exact extraction in [CG8841-sequence-evidence.json](CG8841-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR026705; HID1/Ecm30.
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Protein HID1 | CNN | IPR026705 independently establishes the HID1/Ecm30 family. The current UniProt name itself is ProtNLM-derived and contributes no independent evidence; the diagnostic family assignment is the support. |
| Location | Nucleus (SL-0191) | UNC | The supported biology is Golgi/secretory-pathway organization with a cytosolic pool. That does not establish nuclear residence or prove that a nuclear pool is absent; the nuclear claim remains unsupported. |
| Location | Cytoplasm (SL-0086) | LSP | Curated cytosol and Golgi annotations provide more specific cytoplasmic locations and are biologically coherent with HID1-family secretory-pathway function. The broad cytoplasm claim is supported without invoking ARBA. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0000138 Golgi trans cisterna (IBA): **ACCEPT**. IPR026705 identifies the HID1/Ecm30 family and the IBA locates the protein in the Golgi secretory pathway. No target-specific architectural conflict is apparent.
- GO:0003674 molecular_function (ND): **ACCEPT**. HID1-family secretory-pathway participation does not establish an intrinsic enzyme activity or a specific binding reaction.
- GO:0005794 Golgi apparatus (ISS): **ACCEPT**. The HID1/Ecm30 domain supports the existing ISS Golgi annotation; this is an inferred location rather than a direct fly imaging result.
- GO:0005797 Golgi medial cisterna (IBA): **ACCEPT**. The specific IBA is compatible with HID1-family Golgi organization and no target-specific evidence of localization loss is established.
- GO:0005829 cytosol (IBA): **ACCEPT**. HID1-family membership supports a protein cycling or associating with cytosolic faces of secretory membranes; the curated IBA is retained as an inference rather than direct localization.
- GO:0006886 intracellular protein transport (ISS): **ACCEPT**. The existing ISS fits the protein's Golgi/secretory-pathway architecture and inferred organization role.
- GO:0007030 Golgi organization (IBA): **ACCEPT**. The HID1/Ecm30-family assignment is coherent with the curated IBA Golgi-organization assertion and does not require catalytic activity.
- GO:0016020 membrane (IBA): **ACCEPT**. A retained transmembrane helix is not required for peripheral membrane association; HID1-family biology and the existing IBA support the broad membrane term.
- GO:0061792 secretory granule maturation (IBA): **ACCEPT**. HID1-family placement is consistent with a role in Golgi-dependent maturation of secretory cargo. The evidence establishes participation by phylogenetic inference rather than an intrinsic catalytic mechanism.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG8841-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
