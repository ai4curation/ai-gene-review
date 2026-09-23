# IBA and TreeGrafter re-review, 2026-09-20

This audit covers every gene review carrying IBA or TreeGrafter
(`IEA` / `GO_REF:0000118`) annotations, together with the IBA project's named
genes. The scope includes the full gene reviews, with disputed propagated
annotations reviewed first. The corpus-wide scope prevents the featured examples
from becoming an accidental limit on coverage.

The branch was fetched and rebased against `origin/main`; Git reported it already
up to date at `3246edc2f3`. The immutable baseline records the exact commit in
`baseline.json`. Main project pages are findings pages and are not audit logs.

- `inventory.tsv`: baseline gene coverage and priority, generated from Git objects.
- `annotations.tsv`: baseline propagated assertions and actions, including NOT
  and contributes-to flags. Counts are triage information, not judgments.
- Other batch YAML files: manual, source-grounded assessments, changes,
  unresolved questions, and OpenScientist incorporation.
- The corresponding TreeGrafter batch records live in
  [the TreeGrafter audit folder](../../TREEGRAFTER/rereview-2026-09-20/).
- Gene changes also have append-only records scaffolded with `just new-history`.

An inventory row is **not** a completed review. A completed full-gene assessment
must explicitly record `scope: full_gene`, the evidence considered, and a final
status. `awaiting_adjudication` is unfinished. Existing OpenScientist reports
must be read and their substantive findings incorporated before considering an
overlapping question resolved; matching verdicts alone do not suffice.

Batch records use a top-level `genes` list, with `gene_file`, `scope`, `status`
(`reviewed`, `awaiting_adjudication`, or `in_progress`), `outcome`, `changes`,
`evidence`, and `adjudication`. The last fields may contain structured details.
Do not change an existing baseline when resuming this audit.

Generate the baseline once with:

```sh
uv run python projects/IBA_REVIEW/rereview-2026-09-20/inventory.py --create
```

Refresh the derived progress report after manual review batches with:

```sh
uv run python projects/IBA_REVIEW/rereview-2026-09-20/inventory.py
```

`verify_sources.py` compares every changed review named in the manual audit records
with the frozen Git baseline (excluding unrelated changes that arrive on main)
and checks that all original non-NEW source assertions (term, evidence,
reference, isoform, NOT, and qualifier) survive unchanged. The sole registered
identity migration is worm/csr-1: its frozen review mixed a deleted LARP-1
accession with NHR-47 source annotations. The checker verifies that the original
review and source files equal the frozen baseline in their archive, that the
canonical H2KZD5 sources equal the official fetch snapshots, and that all 21
replacement source assertions equal the preserved unreviewed seed. The 16
archived NHR-47 assertions are reported separately, not silently counted as
canonical CSR-1 annotations. See the [migration manifest](../../../genes/worm/csr-1/csr-1-provenance/identity-migration-manifest.json).
It does not assess biological correctness or count as a manual review.

Scientific review checks whether the claimed activity, participation, or
location is supported. Primary location does not establish exclusivity; broad
true terms are not biological errors; absence of a target experiment does not
refute a supported phylogenetic inference. Challenging an IBA requires examining
the ancestral assertion and relevant divergence, rather than counting donors.

OpenScientist requests are recorded in `adjudication-requests.yaml` and executed
with the repository's hypothesis runner. Reports are evidence to inspect,
including their limitations, rather than an automatic authority for changing an
annotation.

Recovery PRs and remaining work are tracked in [recovery-prs.md](recovery-prs.md).
