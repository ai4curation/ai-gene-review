# Bacterial regulon evidence integration

Parent: [Transcription Factor Annotation Review Project](../TRANSCRIPTION_FACTORS.md).
Pilot: [P. putida KT2440 (PSEPK)](../P_PUTIDA.md).
Status: provisional census, membership/weight importer repair and 20 scoped calibration
assessments complete; first four full GO reviews and 12 regulatory relationships curated.
Last updated: 2026-11-08.

The first [KT2440 coverage report](../P_PUTIDA/tf_census/data/coverage.md) and
[prioritized inventory](../P_PUTIDA/tf_census/data/candidates.tsv) are available,
with [20 calibration cases](../P_PUTIDA/tf_census/data/calibration.tsv).
See the [rebuild instructions and limitations](../P_PUTIDA/tf_census/README.md).
Role assignments are provisional triage, not completed biological adjudication.

## Objective and scope

Account for all TF candidates in the KT2440 reference proteome and curate each
claim at the specificity its evidence supports. The main set is sequence-specific
DNA-binding TFs, including response regulators with transcriptional outputs.
Track sigma factors, transcription cofactors, nucleoid proteins, and
post-transcriptional regulators as separate classes. A protein may have more
than one role; retain supported multifunctionality.

Use proteome UP000000556 and taxon NCBITaxon:160488 as the starting scope. Pin the
assembly and sequence versions used for every import. Other strains and
plasmid-encoded regulators require explicit provenance and are not automatically
members of the KT2440 census. Preserve original source names and locus tags
alongside normalized accessions; ambiguous mappings remain unresolved.

The local metadata snapshot has 5,527 rows; 987 PSEPK review YAML files exist at
the 2026-11-04 audit. A case-insensitive `transcription|sigma factor` search of
the metadata's protein-name column finds 395 candidates. This is a discovery
count, not the TF denominator: it includes non-TFs and can miss unnamed TFs.
Existing review files also require assessment before being counted as complete.

## Three evidence layers

| Layer | Records | Required distinction |
|---|---|---|
| TF identity | Protein accession, locus, aliases, architecture/family, role classification, inclusion decision and evidence | A DNA-binding domain or expression-module membership alone does not establish TF function. Record phylogenetic inference separately from experiments on KT2440. |
| Regulatory relationships | Regulator, target gene/promoter/operon, sign, condition, directness, assay, strain and source | Binding, expression response, and a demonstrated functional binding site support different claims. Ligand binding, effector response, and environmental exposure also differ. |
| Expression-module membership | Dataset and module IDs, member gene, published membership call, measured weight if available, membership method/threshold, condition activity | Published regulator assignments are separate many-to-many links; membership does not establish direct targets or activation/repression. |

Each assertion must retain its source record and version, retrieval date, primary
publication(s), assay or inference method, biological context, and curator
assessment. Keep contradictory claims visible with their conditions. Unknown
sign, directness, ligand, or target is an acceptable result, not a slot to fill
from family membership. Keep missing numerical values null, distinct from zero.

Database agreement is not an evidence count. Group assertions derived from the
same publication, experiment, source dataset, or upstream inferred relationship.
Keep an upstream assertion identifier where available so reused evidence can be
recognized. A literature regulon reused to label an iModulon cannot independently
validate itself through that label or its reported overlap score.

## Source register

The census has acquired versioned regulator-identity extracts from RegPrecise and
PRECISE321, official domain-label catalogs and GO branch lists, alongside the
existing UniProt metadata. [Source provenance](../P_PUTIDA/tf_census/sources/manifest.json)
records locations, checksums and reuse notes. All 84 source module memberships and
weights have been imported. Target relationships are curated separately from primary
evidence, starting with the [first four-gene batch](../P_PUTIDA/batches/tf_carbon_utilization_01.md). Other resources below
remain candidate sources; their inclusion does not imply verified bulk access
or KT2440 coverage.

| Source | Pilot use | Evidence and acquisition notes |
|---|---|---|
| [Local UniProt metadata](../P_PUTIDA/data/psepk_uniprot_metadata.tsv), GOA, InterPro/Pfam | Census backbone, domain architecture, existing review join | Union of signals; preserve annotation provenance. Search proteins without TF names as well as named regulators. |
| [Pseudomonas Genome Database](https://pseudomonas.com/strain/download) | KT2440 identifiers, sequences and genome context | KT2440 download listing located; reconcile assembly versions and aliases before joining. Annotation is not automatically experimental evidence. |
| [RegPrecise KT2440](https://regprecise.lbl.gov/genome.jsp?genome_id=267) | Regulons, sites, proposed effectors, family context | KT2440 page verified. Manually curated comparative-genomic inferences; distinguish reconstructed and propagated records. RNA regulators occur on the same page and need separate classification. |
| [CollecTF](https://collectf.org/EXPREG_000011c0/) | Binding-site and regulatory experiments | KT2440 PtxS example located. Preserve assay, publication, genome coordinates and reference assembly. Review the actual experiments before adopting a direct functional relationship. |
| [PRODORIC](https://doi.org/10.1093/nar/gkab1110) | Bacterial binding sites, motifs and literature | Audit KT2440 coverage and export access. Preserve expression, binding, and site-variation evidence separately; predicted motif matches remain predictions. |
| [iModulonDB](https://imodulondb.org/) / [modulome_ppu](https://github.com/SBRG/modulome_ppu) | PRECISE321 modules, weights, activities, regulator assignments | Pinned supplement supplies identities/metrics; pinned modulytics exports supply all 84 published memberships and measured weights, independently checked against thresholds and named matrix columns. Activities remain a future import. See [Lim et al. 2022](https://pubmed.ncbi.nlm.nih.gov/35489688/). |
| [P2TF and P2CS](https://www.cite-des-energies.fr/en/home-biam/search/lemire/lemire-databases/) | Additional TF and two-component-system candidates | Predicted inventories; verify access, release currency and KT2440 coverage. A response regulator need not have a transcriptional output. |
| [groovDB](https://doi.org/10.1093/nar/gkaf1074) | TF–ligand and biosensor evidence | Audit coverage and primary experiments. Distinguish native KT2440 proteins from orthologs, engineered variants, and heterologous assays. |

The 2026 [RpoD/RpoS/RpoN study](https://doi.org/10.1186/s13036-026-00769-z)
is a targeted literature lead for the sigma-factor class; extract its binding and
expression evidence independently. Other-species records can guide orthology
analysis but do not become experiments on the KT2440 protein.

[iRegulon](https://pubmed.ncbi.nlm.nih.gov/25058159/) is a different motif/track
enrichment tool, originally supporting human, mouse and Drosophila. No iRegulon
integration was found in this repository; it is outside the KT2440 pilot.

## Existing implementation and prerequisites

The [integration documentation](../../docs/imodulondb_integration.md) describes
the actual state of the two scripts, dataset mappings and existing BenR report.
The `just compare-imodulondb` recipe calls the shared repaired importer through
the v2 entry point. It reads review YAML for identity/status context; target-overlap
comparison awaits structured curated target sets. See the [calibration results](../P_PUTIDA/tf_census/imodulon/calibration-results.md).

Before using generated reports as curation input:

- [x] Use source-defined membership or the dataset's documented module-specific
  threshold. Keep ranking/display filters separate from membership counts.
- [x] Remove synthetic CSV weights (`1/(i+1)`); retain null when measurements
  are unavailable. Never infer activation/repression from ICA weight sign.
- [x] Preserve missing metrics, including p/q values, as null; validate sheet
  headers and join matrix columns by module identifiers rather than row position.
- [x] Support multiple modules per regulator and multiple regulator assignments
  per module; retain unassigned modules. Missing matches are coverage gaps, not
  evidence against TF function.
- [x] Normalize aliases through accession/locus mappings, report unresolved
  mappings, and write to canonical repository organism directories (`PSEPK`).
- [x] Label imported reference-regulon metrics and provenance separately from any
  comparison to curated relationships; explicitly report that the latter is not performed.
- [x] Validate downloads, pin source versions and checksums, and make failed
  acquisition or parse errors explicit rather than generating partial success.

## Deliverables and execution order

### 1. Reconciled census and coverage report

Build on the existing P_PUTIDA metadata pipeline before seeding full reviews.
Union GO terms, descriptions, domains, database inventories and literature;
optionally use a sequence predictor to find additional candidates. Retain every
candidate's discovery sources and inclusion/exclusion/unresolved reason.

Produce a deterministic inventory keyed by accession and locus, with role class,
family, existing review path/status, evidence availability and priority. Report
source intersections, unmatched identifiers, ambiguous aliases, exclusions, and
unreviewed candidates. The census denominator is the adjudicated candidate set,
not the initial text search or a count of database records.

### 2. Import repair and evidence tables

Repair the prototype using the prerequisites above. Export the three evidence
layers separately, with stable assertion IDs and a source manifest. Add separate
regulator–module assignments and effector assertions rather than packing these
into gene membership rows. Confirm representative source records manually and
exercise missing data, aliases, multiple assignments, and source membership
boundaries before running the full pilot.

### 3. Calibration review: 15–20 candidates

Select the final set after identifier reconciliation. Revisit existing PSEPK
reviews for BenR, hexR, fleQ, gacA and cbrB, plus rpoS in the sigma-factor class.
Add poorly characterized family members, likely false positives and conflicting
database assignments. These names are starting candidates, not an asserted
complete pilot or newly accepted functions.

For each candidate, independently judge TF identity, targets, regulatory sign,
and effector response. Compare primary publications, curated assertions, and
module associations. Record disagreements and missing evidence. Calibrate
whether batch imports save review effort without manufacturing specificity.

### 4. Regulatory-system and family batches

Proceed through carbon utilization, nitrogen regulation, metals, stress,
motility/biofilm, and aromatic catabolism, linking existing pathway modules
where appropriate. Finish with family-based batches for the remaining candidates.
Share family research but assess paralog-specific functions individually. Do not
create a mechanistic module simply because an expression cluster exists.

Use the standard gene-review workflow (`just fetch-gene PSEPK <gene>`, literature
research, annotation assessment, core-function synthesis, validation and history).
Assess all GOA rows consistently. Preserve ND where only inferred function is
known and the species-specific literature gap remains. Use UNDECIDED when
necessary publications cannot be accessed. Regulatory perturbation of a pathway
does not automatically justify a NEW annotation to that pathway's execution;
apply the participation and comparator checks before proposing a process term.

## Completion criteria

- Every census candidate has an explicit included, excluded, or unresolved
  decision; each unresolved case has a documented reason and next evidence need.
- Every included protein has a reviewed role classification and either a
  validated gene review with supported core functions or a clearly documented
  unresolved assessment. Unknown targets or ligands are reported as gaps.
- Every imported assertion is traceable to a versioned source and mapped entity;
  unresolved identifiers and other-strain records are counted separately.
- Published module membership is reproduced; absent weights remain absent;
  association, binding, direct regulation, and sign remain distinct claims.
- Coverage reports show identity, target, sign and effector evidence separately,
  plus review completion and source availability. Annotation counts are not a
  success metric.
- Changed curated files pass their relevant validators and have history records.

## Status

- [x] Locate existing iModulon implementation, mappings, docs and BenR example.
- [x] Define KT2440 scope, evidence layers, source register and completion criteria.
- [x] Audit prototype limitations and correct the integration guidance.
- [x] Build the provisional census and publish coverage counts, alias conflicts and unresolved source records.
- [x] Acquire versioned regulator-identity and vocabulary snapshots.
- [x] Select 20 calibration cases, including in-proteome and out-of-proteome controls.
- [x] Complete 20 scoped calibration assessments, resolving supported identities and retaining uncertain roles/targets.
- [x] Repair the membership/weight importer and check all 84 PRECISE321 modules.
- [x] Review BenR, HexR, PtxS and CbrB GO annotations; capture 12 supported regulatory relationships and pathway context in [validated sidecars](../P_PUTIDA/tf_census/regulatory-evidence.md).
- [ ] Acquire remaining evidence sources and curate structured experimental relationships.
- [ ] Complete the remaining 16 calibration GO reviews, then regulatory-system and family batches.

## Notes

### 2026-11-08 — first full GO-review batch

Completed the four-gene carbon-utilization batch with primary-evidence review of
all existing annotations, core-function synthesis and structured target assertions.
BenR and HexR no longer inherit pathway-execution claims from regulation of enzymes.
Binding, functional regulation, sign, host strain and pathway context are retained
separately. The newly located 2026 HexR paper broadens the biological context;
its inaccessible target tables remain a follow-up, not asserted activating edges.
Primary-source review proceeded despite failed research-provider or fitness services;
all acquisition and evidence limitations are documented in gene notes. See the
[batch report](../P_PUTIDA/batches/tf_carbon_utilization_01.md) for outcomes and checks.

### 2026-11-05 — calibration and importer repair

Recorded [20 evidence assessments](../P_PUTIDA/tf_census/calibration-review.md)
with separate identity, directness, sign and effector findings. Corrected source-name
joins include CbrB/AlgB, GacA/uvrY, TurB/MvaT and RsmE/csrA; unknown targets and
ligands remain unknown. Experimental derivative-strain context is retained.
The checked source export reproduces all 84 modules; BenR has 10 published
members rather than the historical 13-gene display-cutoff list. Both importer
entry points share the same code. Legacy non-pilot dataset routes are disabled
pending verification. No gene-review YAML or GO annotation was changed.

### 2026-11-04

Established this workstream under TRANSCRIPTION_FACTORS and linked it from
P_PUTIDA. The existing BenR report is a historical example requiring reassessment,
not a validated template. No database-wide import or new gene annotation was
performed in this planning session.

### 2026-11-04 — census implementation

Added reproducible source extraction and offline census builds, a coverage report,
prioritized candidate and calibration tables, review-file audit, alias conflicts,
and source/build manifests. The 647 evidence-discovered candidates include 422
provisional main-TF candidates; 59 candidates have accession-matched review files.
These are discovery/triage counts, not validated function or review-completion
counts. One RegPrecise identity remains unresolved; multiple-locus source records
remain explicit. No gene annotation was changed. The separate legacy iModulon
membership/weight importer remains awaiting repair.
