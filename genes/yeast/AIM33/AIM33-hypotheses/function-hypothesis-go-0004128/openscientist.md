---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T17:00:11.728343'
end_time: '2026-08-22T17:14:51.512747'
duration_seconds: 879.78
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: AIM33
  gene_symbol: AIM33
  uniprot_accession: Q04516
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004128
  hypothesis_text: AIM33 has cytochrome-b5 reductase activity, acting on NAD(P)H (GO:0004128).
  term_context: '- Term: cytochrome-b5 reductase activity, acting on NAD(P)H (GO:0004128)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/yeast/AIM33/AIM33-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004128\n  label: cytochrome-b5 reductase\
    \ activity, acting on NAD(P)H\nevidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 2
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** AIM33
- **Gene symbol:** AIM33
- **UniProt accession:** Q04516

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004128
- **Source file:** genes/yeast/AIM33/AIM33-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis

AIM33 has cytochrome-b5 reductase activity, acting on NAD(P)H (GO:0004128).

## Term and Decision Context

- Term: cytochrome-b5 reductase activity, acting on NAD(P)H (GO:0004128)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0004128
  label: cytochrome-b5 reductase activity, acting on NAD(P)H
evidence_type: IBA
original_reference_id: GO_REF:0000033
```

## Research Objective

Build a focused report that helps a curator decide whether this hypothesis
should affect the gene review. Address the focus type directly:

1. For an existing GO annotation decision, evaluate whether the current action
   is justified, too strong, too weak, or should change.
2. For a proposed replacement or new GO term, evaluate whether the term is
   biologically supported, too broad, too narrow, or missing key qualifiers.
3. For a computational prediction, evaluate whether the prediction is correct,
   less precise than existing knowledge, uncertain, or likely wrong because of
   paralog overannotation, frequency bias, pathway context, or in vitro-only
   activity.
4. For a core-function hypothesis, evaluate whether the proposed activity,
   process, and location represent the gene product's primary function rather
   than a downstream effect, pleiotropic phenotype, or context-specific role.
5. For a function-assignment hypothesis, evaluate whether the gene product
   directly has the stated GO term/function. Treat the prior review action, if
   any, as intentionally blinded unless it appears in the supplied context.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

Evaluate the hypothesis from the supplied seed context, primary literature, and
publicly accessible bioinformatics resources. Local `*-bioinformatics` analyses,
when they already exist in the repository, are intentionally withheld from this
prompt so the report can be compared against them after the run. Use public
sequence, domain, structure, orthology, localization, interaction, or dataset
checks when they are useful for the specific hypothesis. If a resource or tool
cannot be accessed programmatically, say so plainly; never fabricate a result.
Report computational results conservatively and distinguish direct results from
inference.

## Required Output

### Executive Judgment

Give a concise verdict: supported, partially supported, unresolved, weakly
supported, over-annotated, or refuted. Explain the reasoning and the most
important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (direct assay, mutant phenotype, localization, interaction,
  structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies / competing
- Claim tested
- Key finding
- Organism, tissue, cell type, or assay context
- Confidence and limitations

### GO Curation Implications

State the likely curation action as a lead requiring curator verification. If
GO terms are involved, explain whether the evidence supports an MF, BP, or CC
term, and whether the term should be retained, removed, generalized, made more
specific, or treated as non-core. Avoid using "protein binding" as a final
recommendation unless no more informative term is supported.

### Mechanistic Scope

Describe the immediate molecular or cellular function being tested. Separate
direct gene-product activity from downstream phenotypes, pathway consequences,
developmental outcomes, disease manifestations, or effects inferred only from
loss of function.

### Conflicts and Alternatives

Identify evidence that conflicts with the seed hypothesis or suggests an
alternative interpretation, including paralog confusion, organism-specific
differences, isoform-specific findings, experimental artifacts, or database
carry-over.

### Knowledge Gaps

List explicit uncertainties that matter for curation. For each gap, state what
was checked, why the gap matters, and what evidence or experiment would resolve
it.

### Discriminating Tests

Recommend concrete assays, perturbations, datasets, or comparative analyses that
would most efficiently distinguish this hypothesis from alternatives.

### Curation Leads

Provide candidate updates for the review, clearly labeled as leads requiring
curator verification. Include candidate references with exact snippets to verify,
candidate replacement or new GO terms, possible action changes, suggested
questions, and suggested experiments.

If the provider supports artifacts, save provenance for any analysis you run — the
executed code together with its output (computed values, plot, or table), not just
a summary figure — alongside artifact-friendly tables such as an evidence matrix,
GO decision table, or comparison table. Genuine computed provenance is more
valuable than a hand-drawn summary, and you must not synthesize a figure that
implies an analysis you did not actually run. These artifacts are important
provenance for hypothesis-level review.


## Output

# AIGR Focused Hypothesis Report — AIM33 (Q04516) / GO:0004128

**Gene:** AIM33 (YML087C), *Saccharomyces cerevisiae* (NCBITaxon:559292)
**UniProt:** Q04516 — "Uncharacterized oxidoreductase AIM33"
**Focus:** function_assignment · slug `function-hypothesis-go-0004128`
**Seed hypothesis:** AIM33 has cytochrome-b5 reductase activity, acting on NAD(P)H (GO:0004128)
**Annotation under review:** GO:0004128, evidence **IBA**, ref **GO_REF:0000033**

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (plausible family-level inference; unconfirmed for AIM33 specifically; not paralog over-annotation).**

The molecular-function *class* is well supported: AIM33 has the complete
domain architecture of the flavoprotein pyridine-nucleotide cytochrome
reductase family (FAD-binding FR-type + NAD_binding_1), retains both catalytic
cofactor fingerprints (NAD-binding `CGPPKM`; FAD/NAD pyrophosphate `GSGITP`),
and folds confidently into an FNR-like reductase module (AlphaFold mean
pLDDT = 87.25). Critically, the closest experimentally-characterized member of
AIM33's own PANTHER subfamily (SF143), **PGA3/Q12746**, is a bona fide
**NADH-dependent cytochrome b5 reductase** (it is also the IBA seed). So the
transfer of GO:0004128 to AIM33 is a *defensible, standard phylogenetic
inference*, **not** a case of paralog over-annotation onto an unrelated protein.

However, the specific term is **unconfirmed for AIM33**: SGD explicitly curates
its molecular function as **ND ("No biological Data")**, there is no direct
enzymatic assay, AIM33 sits in a distinct subfamily whose physiological acceptor
may be **coenzyme Q6** rather than cytochrome b5, and its topology (3 TM helices)
differs from classic soluble/mono-anchored cyt-b5 reductases. The co-annotated
**cellular-component (plasma membrane) and process (ergosterol biosynthesis)**
IBA terms are PGA3-specific carry-overs that **conflict** with AIM33's only
experimental phenotype (increased mitochondrial genome loss).

**Bottom line for the curator:** Retaining GO:0004128 as an **IBA** MF term is
methodologically acceptable, but it should be treated as *inferred/unconfirmed*
(consider the generalized parent MF as the safest evidence-backed statement).
The higher-priority curation action is on the **plasma-membrane CC term**, which
is likely mis-transferred for AIM33.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt Q04516 / QuickGO | review/database | qualifies | Is GO:0004128 experimentally supported for AIM33? | Only IBA (GO_REF:0000033) + automated IEA; **SGD MF = ND**; IBA seeds = MCR1 + PGA3 | *S. cerevisiae*, curated DB | High that it is inference-only; no direct assay exists |
| InterPro/Pfam (PF00970 FAD_binding_6; PF00175 NAD_binding_1; IPR001709) | structural/evolutionary | supports (general) | Does AIM33 carry reductase machinery? | Full FAD-binding FR-type + NAD-binding architecture, same as MCR1/CBR1 | Sequence/domain | High for the **oxidoreductase class**; not acceptor-specific |
| Computed Needleman–Wunsch (this study) | structural/evolutionary | qualifies | Is AIM33 a *close* ortholog of cyt-b5 reductases? | 38.6% id vs CBR1, 32.4% vs MCR1 (CBR1–MCR1 = 33.6%) → paralog-level divergence | Sequence | High; divergence weakens direct 1:1 function transfer |
| Motif scan (this study) | structural/evolutionary | supports (general) | Are catalytic cofactor motifs intact? | `CGPPKM` (NAD) and `GSGITP` (FAD/NAD pyrophosphate) conserved | Sequence | High for cofactor binding; not acceptor identity |
| PANTHER PTHR19370:SF143 | structural/evolutionary | competing | Which subfamily / electron acceptor? | AIM33 in **SF143 = "coenzyme Q6 reductase PGA3"**, distinct from MCR1 (SF171)/CBR1 (SF184) | Phylogenetic | Medium; raises CoQ-acceptor alternative |
| PGA3 / UniProt Q12746 (subfamily seed) | review/database + evolutionary | supports (family) / competing (location) | Does the characterized subfamily member have this activity? | PGA3 = "NADH-dependent cytochrome b5 reductase that reduces coenzyme Q6 at the plasma membrane"; canonical cyt-b5 reductase reaction | *S. cerevisiae* | Medium–High; validates family MF but is PM/ER-localized |
| UniProt topology features | localization/structural | competing | Topology like classic cyt-b5 reductase? | 3 TM helices (aa 15–35, 42–62, 180–200) — polytopic, vs single N-anchor of Mcr1/Cbr1 | Sequence/topology | Medium–High; atypical for the classic enzymes |
| PMID:16847258 (Kim et al. 2006) | localization | qualifies | Is AIM33 an integral membrane protein? | Experimentally-constrained polytopic membrane topology | *S. cerevisiae*, large-scale | Medium (high-throughput) |
| PMID:19300474 (Hess et al. 2009) | mutant phenotype | qualifies | Does AIM33 perform cyt-b5 reductase function? | Deletion **increases mitochondrial genome loss / alters mito biogenesis** | *S. cerevisiae*, deletion screen | Medium; **downstream phenotype, not an MF assay** |
| AlphaFold AF-Q04516-F1 | structural/computational | supports (general) | Is the reductase fold intact/real? | Mean pLDDT = 87.25; confidently folded FNR-like module | Model | High that fold is genuine; not functional proof |
| SGD GO:0003674 = ND | review/database | refutes (specific) | Is any experimental MF known? | SGD curated "No biological Data" for molecular function | *S. cerevisiae* | High; explicit absence of experimental MF |

*Provenance artifacts:* `/tmp/aim33_evidence_matrix.csv` (computed table) plus the
executed alignment/motif/AlphaFold/UniProt-query code and outputs in the
iteration logs.

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Aspect | Term | Basis | Recommended action (lead) |
|---|---|---|---|---|
| **GO:0004128** | MF | cytochrome-b5 reductase activity, acting on NAD(P)H | IBA from MCR1+PGA3; PGA3 experimentally has this activity; but AIM33 unconfirmed, SF143 hints CoQ, atypical topology | **RETAIN as IBA but flag "inferred/unconfirmed."** Acceptable as a phylogenetic MF. If a more conservative statement is preferred, generalize to the parent MF (below). |
| GO:0016491 / GO:0016651 | MF | oxidoreductase / acting on NADH or NADPH | Domain + fold + conserved catalytic motifs | **SUPPORTED** — the safest evidence-backed MF generalization if a curator wants to avoid over-specificity. |
| **GO:0005886** | CC | plasma membrane | IBA carry-over from PGA3; conflicts with AIM33 mito phenotype; experimental location is only generic "Membrane" | **REVISE / REMOVE.** Highest-priority action. Replace with `membrane` (GO:0016020) or investigate mitochondrial/ER membrane. |
| GO:0006696 | BP | ergosterol biosynthetic process | IBA carry-over from PGA3; no AIM33-specific evidence | **TREAT AS NON-CORE / weak.** Not supported by AIM33's own data. |
| (candidate) mitochondrial genome maintenance BP | BP | e.g., mitochondrial genome maintenance | PMID:19300474 loss-of-function | **Candidate phenotype-based lead** (IMP-type), curator judgement; note it is a downstream requirement, not necessarily direct. |

Guidance note: "protein binding" is **not** used here — the family/domain evidence
supports the more informative NAD(P)H:FAD oxidoreductase statement.

---

## Mechanistic Scope

- **Immediate molecular function being tested:** NAD(P)H-dependent electron
  transfer via a bound FAD to an electron acceptor (cytochrome b5 and/or
  coenzyme Q6). The domain architecture, conserved `CGPPKM`/`GSGITP` motifs, and
  confident FNR-like fold directly support that AIM33 *can* bind NAD(P)H + FAD
  and act as an electron-transfer oxidoreductase.
- **Not established directly:** the identity of the physiological electron
  acceptor (cyt b5 vs CoQ6), catalytic turnover, and the subcellular membrane
  in which it acts.
- **Downstream / loss-of-function only (must not be conflated with MF):** the
  increased mitochondrial genome-loss phenotype (PMID:19300474) is a genetic
  requirement in mitochondrial biogenesis/inheritance, not a molecular activity.
- **Pure database carry-over (no AIM33 data):** plasma-membrane localization and
  ergosterol biosynthesis, both inherited from PGA3 via IBA.

---

## Conflicts and Alternatives

1. **Subfamily / acceptor alternative (competing):** AIM33 belongs to PANTHER
   SF143, whose namesake PGA3 reduces **coenzyme Q6**, not (only) cytochrome b5.
   The physiological acceptor for AIM33 could be ubiquinone; GO:0004128 may be
   over-specific relative to actual chemistry.
2. **Localization conflict (database carry-over):** the IBA CC "plasma membrane"
   and BP "ergosterol biosynthesis" match PGA3, but AIM33's experimental signal
   points to mitochondria (genome-loss phenotype) and only a generic "Membrane"
   location. This is classic single-anchor IBA package transfer.
3. **Topology divergence:** AIM33 is predicted polytopic (3 TM), unlike the
   mono-anchored soluble-domain architecture of the canonical NADH-cyt-b5
   reductases Mcr1/Cbr1 — hinting at a functionally/locationally distinct role.
4. **Paralog landscape:** *S. cerevisiae* has ≥4 members (MCR1, CBR1, PGA3,
   AIM33). Functional/localization partitioning among paralogs means AIM33 need
   not replicate PGA3's plasma-membrane sterol role even if it shares the
   catalytic chemistry.
5. **Not a refutation:** because PGA3 (same subfamily, the IBA seed) genuinely
   has cyt-b5 reductase activity, the MF inference is *not* a spurious paralog
   over-annotation onto an unrelated protein — it is a reasonable but unconfirmed
   transfer.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct enzymatic assay for AIM33 | UniProt/QuickGO/SGD — SGD MF = ND | Determines whether GO:0004128 is direct vs inferred | In-vitro NAD(P)H-cytochrome b5 / CoQ6 reductase assay on purified AIM33 |
| Electron-acceptor identity (cyt b5 vs CoQ6) | PANTHER subfamily, PGA3 function | Decides if GO:0004128 is precise or should be a CoQ-reductase term | Steady-state kinetics vs cyt b5 and vs ubiquinone analogs |
| True subcellular location | UniProt (generic "Membrane"), topology map, mito phenotype | Plasma-membrane CC likely wrong; affects CC curation | GFP/split-GFP or fractionation; check mitochondrial/ER membrane |
| NADH vs NADPH preference | Motifs present but not discriminating | Affects exact term (cyt-b5 reductase "acting on NAD(P)H") | Cofactor-preference kinetics |
| Mechanism linking to mito genome loss | PMID:19300474 (phenotype only) | Whether MF and phenotype are causally linked | Epistasis with Mcr1/Cbr1/Pga3; rescue by catalytic-dead AIM33 |

---

## Discriminating Tests

1. **Purified-enzyme kinetics** with (a) cytochrome b5 and (b) coenzyme Q6/ubiquinone
   analogs, using NADH and NADPH — the single most decisive test of both activity
   and acceptor specificity.
2. **Catalytic-dead complementation:** test whether a FAD/NAD-binding-site mutant
   AIM33 (e.g., disrupting the `CGPPKM` or `GSGITP` motif) fails to rescue the
   mitochondrial genome-loss phenotype — links MF to phenotype.
3. **Localization by fractionation + high-resolution imaging** to test
   plasma-membrane vs mitochondrial/ER assignment.
4. **Comparative genetic interactions** (SGA) of *aim33Δ* vs *pga3Δ*, *mcr1Δ*,
   *cbr1Δ* to define functional overlap/partitioning within the paralog set.
5. **Structural superposition** of the AlphaFold AIM33 model onto solved
   Mcr1/human CYB5R3 to inspect acceptor-binding surface conservation.

---

## Curation Leads (require curator verification)

- **Action on GO:0004128 (MF):** *Retain as IBA but annotate as inferred/unconfirmed
  for AIM33.* Acceptable phylogenetic call; consider adding/keeping the
  generalized parent MF (oxidoreductase acting on NAD(P)H) as the conservative
  evidence-backed statement. Do **not** upgrade to an experimental evidence code.
- **Action on GO:0005886 (CC, plasma membrane):** *Revise/remove* — likely
  mis-transferred from PGA3; replace with `membrane` (GO:0016020) pending
  localization data. **Highest-priority correction.**
- **Action on GO:0006696 (BP, ergosterol biosynthesis):** *Treat as non-core /
  weak* — no AIM33-specific support.
- **Candidate reference to verify (disruption phenotype / mito role):**
  - **PMID:19300474** — snippet to verify: *"we have identified 100 proteins whose
    deficiency alters mitochondrial biogenesis and inheritance in Saccharomyces
    cerevisiae"* (supports a mitochondrial genome-maintenance requirement, not a
    molecular-function assay).
  - **PMID:16847258** — snippet to verify: *"present experimentally constrained
    topology models for 546 proteins"* (basis for the polytopic membrane topology).
- **Comparator to verify (family MF is genuine):** UniProt **Q12746 (PGA3)** —
  *"NADH-dependent cytochrome b5 reductase that reduces coenzyme Q6 at the plasma
  membrane"* — confirms the subfamily truly bears this activity, justifying the
  IBA while flagging the CoQ alternative.
- **Suggested curator questions:** (1) Is there any post-2009 experimental
  characterization of AIM33 enzymology or localization? (2) Should the MF be kept
  as-is or generalized given SF143's CoQ association? (3) Is the plasma-membrane
  CC defensible for AIM33 or a PGA3 carry-over?
- **Suggested experiments:** the discriminating tests above (enzyme kinetics vs
  cyt b5 and CoQ6; catalytic-dead rescue of the mito phenotype; localization).

---

## Limitations

- The provided PubMed interface returned no yeast-genetics primary literature for
  AIM33/PGA3/AIM-screen queries; analysis relied on UniProt, QuickGO, InterPro,
  PANTHER, AlphaFold, and SGD primary records plus the two indexed primary papers
  (PMID 16847258, 19300474).
- Sequence identity was computed with a simple Needleman–Wunsch (identity
  scoring), adequate for order-of-magnitude divergence but not a substitute for a
  curated multiple alignment / phylogeny.
- No wet-lab data could be generated; all activity/acceptor conclusions are
  inference-level and flagged as such.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)