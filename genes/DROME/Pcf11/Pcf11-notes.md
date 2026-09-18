# Pcf11 (C0P8M6): evidence and ProtNLM claim review

The C0P8M6 Pcf11 record encodes an 86-residue protein consisting largely of a CTD-interacting domain. Full-length Drosophila Pcf11 participates in RNA polymerase II transcription termination, but the activities and intracellular distribution of this short translation product are unresolved.

Exact input: [C0P8M6](https://www.uniprot.org/uniprotkb/C0P8M6/entry), 86 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Pcf11-predictions-source.json](Pcf11-predictions-source.json). Source features: [Pcf11-uniprot.txt](Pcf11-uniprot.txt), with an exact extraction in [Pcf11-sequence-evidence.json](Pcf11-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR006569; CID_dom.
DR   InterPro; IPR008942; ENTH_VHS.
DR   InterPro; IPR045154; PCF11-like.
FT   DOMAIN          11..86
FT                   /note="CID"
FT                   /evidence="ECO:0000259|PROSITE:PS51391"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | CID domain-containing protein | CNN | IPR006569 identifies a CID domain at residues 11-86 in the exact 86-residue product. This modest domain claim is supported without transferring full-length Pcf11 activity. |
| Location | Cytoplasm (SL-0086) | UNC | Cytoplasmic localization of the 86-residue product is not demonstrated. Full-length Pcf11 localization and function cannot settle the compartment of this exact short record. |
| Location | Nucleus (SL-0191) | UNC | Nuclear residence is plausible for a CID-containing Pcf11-derived product but remains unresolved for this 86-residue sequence. A mapped construct or isoform localization experiment is needed. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0000993 RNA polymerase II complex binding (IEA): **UNDECIDED**. A CID hit spanning residues 11-86 supports CTD-interaction potential but does not demonstrate RNA polymerase II complex binding by the exact 86-residue product.
- GO:0003723 RNA binding (IDA): **UNDECIDED**. PMID:16387654 concerns Pcf11 biochemical activity. The exact benchmark product is only 86 residues and requires construct or isoform mapping before the experimental RNA-binding result can be attributed to it.
- GO:0003729 mRNA binding (IEA): **UNDECIDED**. The truncated domain-bearing record cannot be assumed to retain full-length Pcf11 RNA-binding activity; exact-product or mapped-construct evidence is needed.
- GO:0006369 termination of RNA polymerase II transcription (IEA): **UNDECIDED**. A single 86-residue CID-containing product may not execute the full-length protein function. This is an isoform-resolution limitation and not evidence against the experimentally established gene-level role.
- GO:0010467 gene expression (IEA): **UNDECIDED**. The broad computational annotation cannot establish that the 86-residue product is produced or functionally contributes to gene expression in vivo.
- GO:0031124 mRNA 3'-end processing (IEA): **UNDECIDED**. The source sequence lacks most of the full-length Pcf11 architecture; domain presence does not establish assembly into the processing machinery.
- GO:0032991 protein-containing complex (IEA): **UNDECIDED**. The 86-residue sequence has a CID-family segment but no exact-product demonstration of complex incorporation.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `Pcf11-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
