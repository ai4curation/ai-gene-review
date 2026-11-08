# Experimental regulatory evidence

Each reviewed TF can have a `GENE-regulatory-evidence.yaml` companion to its
gene-review YAML. These records preserve supported regulator–target relationships
without turning expression-module membership into direct regulation or creating
a gene-specific GO term. This pilot format is defined by the LinkML schema
[regulatory-evidence.schema.yaml](regulatory-evidence.schema.yaml).

The first four reviews and their results are tracked in the
[carbon-utilization batch](../batches/tf_carbon_utilization_01.md).

## Interpretation

- `regulator` identifies the KT2440 reference accession, locus and taxon.
- `target.type` distinguishes promoter, gene and operon assertions. For a promoter,
  optional `locus` anchors the associated gene; it does not encode binding-site coordinates.
  Leave the locus absent when only the published promoter name is securely resolved.
- `effect` records activation, repression or unknown sign under the stated condition.
- `directness: direct` requires binding evidence and a functional regulatory effect
  supporting that target. Binding alone or differential expression alone is insufficient.
  `unresolved` preserves supported regulation without claiming physical directness;
  `indirect` requires an argument for an intervening mechanism.
- `experimental_strain` retains native strain, derivative and heterologous-host context.
  The reference accession alone does not imply that every experiment was in KT2440.
- `evidence` records primary publication, assay and short exact support. Its reference
  must also be declared in the gene review. A source URL identifies inspected full text
  when the local PMID cache is abstract-only; the gene notes document access limitations.
- `pathway_context` records how transcriptional control regulates a pathway. An optional
  GO `process` identifies the process being regulated, **not an involved_in annotation**
  on the regulator. A name and mechanism suffice when a suitable term is unestablished.

One promoter assay does not establish separate direct contacts with every downstream
operon gene. Missing relationships are not negative assertions, and these sidecars
are evidence-supported subsets rather than complete regulons. Multiple rows citing
one paper do not become independent studies. Effector binding and growth-condition
responses remain distinguished in the gene review and evidence notes.

## Validation and maintenance

From the repository root:

```bash
uv run linkml-validate \
  -s projects/P_PUTIDA/tf_census/regulatory-evidence.schema.yaml \
  -C RegulatoryEvidence genes/PSEPK/BenR/BenR-regulatory-evidence.yaml
uv run python projects/P_PUTIDA/validate_regulatory_evidence.py \
  genes/PSEPK/{BenR,hexR,ptxS,cbrB}/*-regulatory-evidence.yaml
uv run pytest -q tests/test_putida_regulatory_evidence.py
```

For a standalone snippet, select its class rather than the complete record:

```bash
uv run linkml-validate \
  -s projects/P_PUTIDA/tf_census/regulatory-evidence.schema.yaml \
  -C RegulatoryRelationship relationship.yaml
```

Other snippet classes are `RegulatorIdentity`, `RegulatoryTarget`,
`RegulatoryEvidenceItem`, `PathwayContext`, and `RegulatoryProcessTerm`.
LinkML validation checks each snippet's structure; the project validator below
also needs a complete record and its adjacent gene review to check cross-file links.

The project validator uses LinkML for structure and checks unique assertion IDs, accession/locus/taxon joins,
known target loci, declared references and PMID cache presence. It does not certify
experimental interpretation or verify web quotations; those require manual source
inspection. Run `just validate PSEPK GENE` separately for the GO review and add a
gene history record for changes to either artifact. No automatic conversion to GO
annotation extensions or GO-CAM edges is performed.
