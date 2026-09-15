# CG46301 (A0A1W5PXH3): evidence and ProtNLM claim review

CG46301 is a 1237-residue NOL4/NOL4L-family protein with a nucleolar-protein-4 helical domain. Its gene model incorporates the CG17341 and CG16879 names. A nuclear location is inferred by curated similarity annotation, while its molecular activity and the role of its extended sequence remain unresolved.

Exact input: [A0A1W5PXH3](https://www.uniprot.org/uniprotkb/A0A1W5PXH3/entry), 1237 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG46301-predictions-source.json](CG46301-predictions-source.json). Source features: [CG46301-uniprot.txt](CG46301-uniprot.txt), with an exact extraction in [CG46301-sequence-evidence.json](CG46301-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR056549; HTH_NOL4.
DR   InterPro; IPR039788; NOL4/NOL4L.
FT   DOMAIN          789..886
FT                   /note="Nucleolar protein 4 helical"
FT                   /evidence="ECO:0000259|Pfam:PF23079"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Nucleolar protein 4 | CNN | IPR039788 establishes NOL4/NOL4L-family membership and PF23079 identifies a nucleolar-protein-4 helical domain. The family-level name is supported; the wording alone is not evidence of nucleolar localization or a specific NOL4 paralog. |
| Location | Nucleus (SL-0191) | LSP | The existing curated ISS nucleoplasm annotation is a more specific nuclear location. Family architecture supports this inference without establishing a nucleolar role. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. NOL4/NOL4L family assignment and the helical domain are insufficient to specify an enzymatic or RNA-processing activity.
- GO:0005654 nucleoplasm (ISS): **ACCEPT**. The NOL4/NOL4L assignment supports the existing ISS nuclear localization inference; there is no target-specific evidence contradicting it. The name nucleolar protein does not by itself establish nucleolar residence.
- GO:0008150 biological_process (ND): **ACCEPT**. The exact 1237-residue gene model contains NOL4-family sequence but no directly characterized biological process is established.

## Research assessment

The Falcon source leads do not establish a fly-specific molecular activity. PMID:25366156 studies murine NOL4 splice variants interacting with mouse Mlr proteins; use of Drosophila S2 cells as an assay host does not make the assayed NOL4 a fly gene product. The exact NOL4-family architecture and existing curated ISS support a nuclear inference, with no transfer of the mouse transcriptional mechanism.

Provider output: [CG46301-deep-research-falcon.md](CG46301-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.
