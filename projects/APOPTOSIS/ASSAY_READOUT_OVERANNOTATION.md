# Apoptosis Readout Over-Annotation

This note isolates the APOPTOSIS cases we care about most: annotations where
the paper assayed a late cell-death endpoint, such as TUNEL, Annexin V,
cleaved caspase-3, DEVDase activity, PARP cleavage, or a viability counter,
and the GO row then asserted that the assayed gene product was part of an
apoptotic pathway.

The important distinction is narrower than "all apoptosis cleanup". Generic
`protein binding` rows on AKT1/MAPK1, broad `protein kinase activity` imports,
and stimulus-response rows propagated to caspases 3/9 are over-annotations, but
they are not the specific assay-to-apoptosis pattern. The readout pattern is:

```text
perturb gene X -> more or less cell death/caspase/TUNEL signal
               -> annotate X to apoptotic signaling or apoptosis regulation
```

That chain is safe only when X performs a proximal apoptotic step. It is
usually too strong for survival kinases, transcriptional regulators,
metabolic proteins, autophagy proteins, and broad stress-response factors.

## Existing Mined Set

The ASSAY_TO_FUNCTION publication miner has already produced a useful seed
set in `projects/ASSAY_TO_FUNCTION/reports/paper_readout_matches.tsv`. Filtering
to rows where:

- `readout_class = APOPTOSIS_CASPASE`
- `aligned = True`

gave 72 rows whose source paper used a caspase/apoptosis readout and whose GO
term was itself apoptotic or caspase-related.

| Action after review | Rows |
|---|---:|
| `KEEP_AS_NON_CORE` | 35 |
| `ACCEPT` | 27 |
| `PENDING` | 4 |
| `MARK_AS_OVER_ANNOTATED` | 3 |
| `MODIFY` | 1 |
| `UNDECIDED` | 1 |
| `NEW` | 1 |

There were 17 mouse rows in this exact mined set. That action distribution is
the core lesson: apoptosis readouts are usually not false positives, but they
often support a contextual, non-core phenotype rather than a direct apoptosis
function.

## High-Signal Reviewed Cases

| Species/gene | Source | Existing GO assertion | Review action | Why this is a readout case |
|---|---|---|---|---|
| human `BECN1` | PMID:27031958 | `GO:2001244` positive regulation of intrinsic apoptotic signaling pathway | `MARK_AS_OVER_ANNOTATED` | Methamphetamine-treated endothelial cells were interpreted as BECN1 promoting BCL2-dependent apoptosis. The review judged this a toxicology context and a likely misread of the BECN1-BCL2 interaction, which primarily controls autophagy. |
| human `LRRK2` | PMID:21857923 | `GO:1902236` negative regulation of endoplasmic reticulum stress-induced intrinsic apoptotic signaling pathway | `MARK_AS_OVER_ANNOTATED` | Oxidative/ER-stress death endpoints in a disease model were too far from LRRK2's kinase function to make an ER-stress apoptosis branch part of the gene's function model. |
| human `SOD1` | PMID:12551919 | `GO:1902177` positive regulation of oxidative stress-induced intrinsic apoptotic signaling pathway | `MARK_AS_OVER_ANNOTATED` | SOD isoform overexpression altered hydroperoxide-induced apoptosis in PC12 cells, but SOD1's core role is superoxide detoxification; positive apoptosis regulation is context-specific and counter to its antioxidant function. |
| mouse `Camk2a` | PMID:23051746 | `GO:0010666` positive regulation of cardiac muscle cell apoptotic process | `UNDECIDED` | A broad CaMKII heart/apoptosis experiment was not clearly CaMKIIalpha-specific. The companion mitochondrial-permeability apoptosis row was kept non-core because the biology is a specialized cardiomyocyte stress output, not a core CAMK2A role. |
| mouse `Ctnnb1` | PMID:20454446 | `GO:0097190` apoptotic signaling pathway and `GO:2001234` negative regulation of apoptotic signaling pathway | `KEEP_AS_NON_CORE` | Genetic perturbation connected beta-catenin to altered granulosa-cell apoptosis, plausibly via a Wnt survival-gene program. The direct function remains canonical Wnt transcriptional control. |
| mouse `Pten` | PMID:20418913 | `GO:0006915` apoptotic process | `KEEP_AS_NON_CORE` | Genetic interaction evidence captured an apoptosis outcome downstream of PTEN/PI3K/AKT signaling, not a proximal PTEN step inside apoptosis. |
| mouse `Akt1` | PMID:19911006 | `GO:2001243` negative regulation of intrinsic apoptotic signaling pathway | `KEEP_AS_NON_CORE` | AKT1 survival signaling can reduce intrinsic apoptosis, but the row is downstream of kinase signaling rather than the AKT1 molecular activity itself. |
| mouse `Hdac1` | PMID:21093383 | `GO:0043066` negative regulation of apoptotic process | `KEEP_AS_NON_CORE` | HDAC1/2 epidermal loss derepresses p53 targets and increases apoptosis. That is closer than a pure endpoint assay because HDAC1 is a chromatin repressor of the p53 program, but the generic apoptosis parent is still a downstream non-core outcome. |
| mouse `Casp8` | PMID:16183742 | `GO:0006915` apoptotic process, `GO:0097190` apoptotic signaling pathway, `GO:2001238` positive regulation of extrinsic apoptotic signaling pathway | `MARK_AS_OVER_ANNOTATED` | PIDD expression activated caspase-2 and effector caspases, but the paper explicitly failed to detect procaspase-8 processing in PIDD-expressing MEFs. The PIDD arm observed a RAIDD/caspase-2 cascade, so these generic Casp8 apoptosis annotations overstate that assay. |
| yeast <gene species="yeast" symbol="COX20">COX20</gene> | PMID:31752220 | `GO:0043069` negative regulation of programmed cell death | `KEEP_AS_NON_CORE` | The protein is a respiratory-chain assembly factor. Its deletion promotes acetic-acid-dependent death, making programmed-cell-death resistance a downstream respiratory-fitness phenotype rather than its core role. |

## Pending Or Worth Rechecking

`projects/ASSAY_TO_FUNCTION/reports/flagged_candidates.tsv` contains a Tier 2
block for `ACCEPT`ed BP calls aligned to `APOPTOSIS_CASPASE`, with the default
warning:

> rubric default is non-core unless gene is in the machinery

Most are probably defensible; the point is to re-ask whether a direct step was
demonstrated rather than trusting a caspase/TUNEL endpoint. The mouse rows from
that block are:

| Species/gene | PMID | GO term | Current action | Triage |
|---|---|---|---|---|
| mouse `Casp3` | PMID:12954857 | `GO:0097194` execution phase of apoptosis | `ACCEPT` | Likely valid: caspase-3 is core execution machinery, so a caspase readout paper can still be about the assayed gene product. |
| mouse `Casp3` | PMID:12847083 | `GO:0006915` apoptotic process | `ACCEPT` | Likely valid but broad: top-level apoptosis is acceptable for the core effector caspase, though the APOPTOSIS project generally prefers execution-phase descendants where evidence permits. |
| mouse `Hdac1` | PMID:21093383 | `GO:2001243` negative regulation of intrinsic apoptotic signaling pathway | `ACCEPT` | Boundary case: p53 deacetylation puts HDAC1 nearer to the apoptotic transcriptional program than a generic survival kinase, but it should be spot-checked against the broader HDAC1/HDAC2 double-knockout phenotype. |

## Triage Rules

- **Ask what entity performs the apoptotic step.** If a caspase, BAX/BAK pore,
  BCL2-family inhibitor, APAF1 apoptosome, FADD/DISC protein, or IAP is the
  acting entity, the apoptosis term may belong there. If the tested gene only
  changes whether those entities fire, default to non-core or over-annotated.
- **Treat late markers as convergent.** TUNEL, Annexin V, cleaved caspase-3,
  PARP cleavage, DEVDase reporters, mitochondrial depolarization, and viability
  assays are endpoints. They prove that the perturbation moved cells toward or
  away from death; they do not name the direct pathway edge.
- **Keep direct transcriptional control distinct from cell death.** A TF or
  chromatin regulator can directly activate or repress an apoptotic target gene
  program. That is stronger than a viability effect, but it is still a
  transcriptional role first and should not be collapsed into generic
  `GO:0006915`.
- **Prefer the nearest mechanism.** For AKT, PTEN, ERK, beta-catenin, and
  HDACs, use kinase, phosphatase, Wnt, or chromatin terms as the core model;
  keep apoptosis only when a proximal apoptotic branch is shown.
- **Do not penalize core apoptosis proteins for using apoptosis assays.** For
  effector and initiator caspases, APAF1, BCL2-family proteins, FADD, XIAP,
  and DIABLO, caspase/TUNEL assays are expected orthogonal evidence. The
  concern is only when the gene sits upstream, beside, or downstream of the
  death pathway.

## Next Slice

1. Start from `projects/ASSAY_TO_FUNCTION/reports/flagged_candidates.tsv`
   rows 60-83 and rerun the comparator check against the gene's core function.
2. Expand the filter to apoptosis terms whose cached papers match
   `VIABILITY_PROLIFERATION` or `MITO_MEMBRANE_POTENTIAL`, since many
   cell-death papers use viability or mitochondrial potential without a
   caspase-specific string.
3. Query mouse GOA for broad `GO:0043065 positive regulation of apoptotic
   process` and `GO:0043066 negative regulation of apoptotic process`; the
   survival-kinase failure mode will be denser there than under exact
   `GO:0006915`.
