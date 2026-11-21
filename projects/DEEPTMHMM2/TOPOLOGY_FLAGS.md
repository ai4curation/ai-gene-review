# Topology constraints as negative-evidence flags

DeepTMHMM2 can supply a sequence-based line of evidence to the existing
[Function Requirement (NOT) rules](../FUNCTION_REQUIREMENT_RULES.md). Those rules
generate review leads; neither they nor this companion pilot automatically emit
GO `NOT` assertions. Ruling out a proposed mechanism is useful even when the
correct function or exact compartment remains unknown.

## Implemented pilot

| Check | Trigger | Interpretation |
|---|---|---|
| DTM2:0001 | UniProt TRANSMEM, but complete prediction has IF/RE regions and no alpha or beta spans | Review a spanning-topology claim. Independent literature can corroborate the conflict or identify a predictor counterexample. |
| DTM2:0002 | Retained lipid-droplet annotation plus UniProt or predicted spanning segment | Check whether the same protein form directly occupies the droplet monolayer. ER-contact pools, tethered partners and alternative topologies require different interpretations. |
| FRR:0004 companion | In-scope `enables` transporter annotation but no predicted span | Preserve the existing rule's family alternatives, qualifier scope and exempt subtrees; expose prediction disagreements even when UniProt makes the original requirement pass. |
| DTM2:0003 | Human protein assigned a chloroplast inner/outer membrane | Reject the incompatible compartment prediction. Added during the expanded pilot. |
| DTM2:0004 | Predicted span overlaps UniProt INTRAMEM residues | Review local geometry; separate interfacial and spanning regions remain compatible. Added during the expanded pilot. |

The companion reads the existing FRR:0004 configuration and GO closure; it does
not change the ten existing rules or activate a validation gate. Primary active
transporter and other configured exemptions remain excluded. A beta-barrel is
spanning; a signal peptide alone is not. Mixed IF/RE and TM proteins are not
flagged as IF/RE-only.

**One leaflet is not the same as peripheral association.** Monotopic integral
proteins insert into one leaflet without spanning the bilayer. Thus evidence
against spanning must not become `NOT membrane` or `NOT integral membrane`.
DHRS3 cysteine scanning supports precisely this geometry
([PMID:30104359](https://pmc.ncbi.nlm.nih.gov/articles/PMC6126764/)).
ER plus lipid-droplet localization is compatible with monotopic insertion, as
shown for LPCAT1/2
([PMID:21498505](https://pmc.ncbi.nlm.nih.gov/articles/PMC3122193/)).

## What a stronger constraint would require

The unit of comparison should be **protein form, domain/residue range, membrane,
side and biological context**, rather than a gene-wide pair of cellular-component
terms. A domain established to face the cytosol argues against that same domain
performing an exclusively lumenal reaction in the same context. A genuinely
monotopic chain argues against a proposed mechanism requiring the chain to cross
that bilayer. Those constraints can narrow function without predicting a new one.

A protein can have domains on opposite sides, reside in multiple pools, be cleaved,
or have alternative isoforms. Accordingly, this pilot does not implement a global
table of incompatible organelles or assert gene-wide negatives. Domain-side and
substrate-access constraints are a next extension once the evidence has that scope.
No-TM predictions alone are weak negative evidence; suppressed organelle output is
not negative evidence at all. Several outputs from this model are one evidence
source, not independent votes. A curator-authored GO `NOT` still needs an explicit,
term-specific biological argument.

## Results on the existing 31-protein panel

[Machine-readable flags](topology-flags.json) contain **21 flags on 14 proteins**:

- 3 corroborated topology conflicts: SPTLC2, DHRS3, LPCAT1.
- 4 predictor-counterexample flags on 2 proteins: CYP46A1 and TOMM22, including
  TOMM22's two FRR:0004 annotation rows.
- 9 source conflicts needing further adjudication by this checker.
- 5 lipid-droplet context checks: ACSL4, DHRS3, LPCAT1, PNPLA2, PNPLA3.

These are source-discrepancy flags, not 21 newly discovered annotation errors.
Some were already resolved by the earlier manual audit. In particular, the small
[literature ledger](topology-evidence.yaml) currently covers only five proteins;
SUN2 and COQ8B remain checker review flags despite the earlier audit's conclusions.
The ledger's NONSPANNING entries are manual syntheses of literature and context,
not claims that every residue or cellular pool was experimentally assayed.
The deliberately enriched panel does not estimate a proteome-wide error rate.

Each flag retains accession, sequence hash, prediction path, source segment counts,
and the scoped literature entry if present. Transporter flags also retain the
original FRR verdict, annotation evidence/reference and matching review actions.
The current lipid-droplet check covers retained exact `GO:0005811` annotations,
including effective MODIFY replacements; it excludes removed and NOT claims.

## Reproduction and validation

The [expanded 205-protein pilot](../../genes/human/SPTLC2/SPTLC2-bioinformatics/deeptmhmm2-benchmark/flag-pilot-2026-11-12/RESULTS.md)
excludes the original 31 and provides manual triage for every flagged protein.
It produced 45 flags on 32 proteins after the two exploratory checks above were
added (37 flags on 26 proteins with the original checks). It reveals model
counterexamples, complex-role issues, contact-site context and regional geometry
questions. All five diagnostic outputs reproduced with the unmodified CLI.
The earlier 31-protein JSON remains a snapshot of the initial pilot; rerunning
the expanded checker preserves its 21 flags unchanged.

From the repository root, using the previously generated API predictions:

```bash
uv run python -m ai_gene_review.tools.topology_flags \
  --repo . \
  --manifest genes/human/SPTLC2/SPTLC2-bioinformatics/deeptmhmm2-benchmark/panel-2026-11-05/inputs.tsv \
  --predictions genes/human/SPTLC2/SPTLC2-bioinformatics/deeptmhmm2-benchmark/panel-2026-11-05/api \
  --evidence projects/DEEPTMHMM2/topology-evidence.yaml \
  --output projects/DEEPTMHMM2/topology-flags.json
uv run pytest tests/test_topology_flags.py tests/test_function_requirements.py -m 'not integration' -q
```

All 32 tests passed (three existing network integration tests deselected).
Tests cover missing/truncated predictions, sequence and context scope, mixed
topologies, beta strands, positive versus NOT/removed location claims, transporter
qualifiers/exempt scope, family alternatives and experimentally supported predictor
counterexamples. The panel run verifies prediction-run hashes against the manifest
and current UniProt sequence. It reuses the pinned benchmark and performs no new
inference. No gene review or GO assertion is modified by the checker.
