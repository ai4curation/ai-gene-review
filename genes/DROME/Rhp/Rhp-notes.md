# Rhp (Q9XYY9): evidence and ProtNLM claim review

Rhophilin is a multidomain Rho-effector-family protein containing HR1 Rho-binding, BRO1, and PDZ domains. This architecture supports a signaling scaffold associated with cytoskeletal regulation, while its exact partners and the conservation of stress-fiber regulation in Drosophila remain incompletely resolved.

Exact input: [Q9XYY9](https://www.uniprot.org/uniprotkb/Q9XYY9/entry), 718 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Rhp-predictions-source.json](Rhp-predictions-source.json). Source features: [Rhp-uniprot.txt](Rhp-uniprot.txt), with an exact extraction in [Rhp-sequence-evidence.json](Rhp-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR004328; BRO1_dom.
DR   InterPro; IPR038499; BRO1_sf.
DR   InterPro; IPR011072; HR1_rho-bd.
DR   InterPro; IPR036274; HR1_rpt_sf.
DR   InterPro; IPR001478; PDZ.
DR   InterPro; IPR036034; PDZ_sf.
DR   InterPro; IPR047138; RHPN1_2.
FT   DOMAIN          36..110
FT                   /note="REM-1"
FT                   /evidence="ECO:0000259|PROSITE:PS51860"
FT   DOMAIN          121..520
FT                   /note="BRO1"
FT                   /evidence="ECO:0000259|PROSITE:PS51180"
FT   DOMAIN          567..645
FT                   /note="PDZ"
FT                   /evidence="ECO:0000259|PROSITE:PS50106"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Rhophilin-2 | UNC | IPR047138 supports the RHPN1/2 family and the source identifies fly Rhophilin. The vertebrate paralog-specific label Rhophilin-2 is more precise than this evidence establishes; an orthology analysis is needed to distinguish it from a family-level name. |
| Location | Cytoskeleton (SL-0090) | UNC | The Rho-effector architecture and existing stress-fiber-related IBA support cytoskeletal biology but do not establish structural residence at the cytoskeleton. Localization and participation in cytoskeletal regulation are distinct claims. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0007165 signal transduction (IEA): **ACCEPT**. HR1 Rho-binding plus BRO1 and PDZ domains support a scaffold role in signal transduction; this is not an intrinsic Rho GTPase activity.
- GO:0051497 negative regulation of stress fiber assembly (IBA): **UNDECIDED**. The existing IBA is a phylogenetic assertion and is not discounted by donor count. HR1/BRO1/PDZ architecture supports Rho-effector biology but does not by itself establish negative regulation of stress-fiber assembly in the exact fly protein; target-specific functional evidence or the ancestral assertion needs resolution.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `Rhp-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
