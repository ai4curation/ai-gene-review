---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T23:33:55.521897'
end_time: '2026-08-31T23:46:29.834855'
duration_seconds: 754.31
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: plo1
  gene_symbol: plo1
  uniprot_accession: P50528
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: spb-insertion-mechanism
  hypothesis_text: Plo1 directly phosphorylates a spindle-pole-body ring component
    to drive localized nuclear-envelope breakdown and mitotic spindle-pole-body insertion
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/plo1/plo1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Plo1 directly phosphorylates a spindle-pole-body\
    \ ring component to drive localized nuclear-envelope\n  breakdown and mitotic\
    \ spindle-pole-body insertion\nfocus_type: free_text\ncontext: []\nreference_id:\
    \ []"
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
citation_count: 1
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** plo1
- **Gene symbol:** plo1
- **UniProt accession:** P50528

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** spb-insertion-mechanism
- **Source file:** genes/SCHPO/plo1/plo1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Plo1 directly phosphorylates a spindle-pole-body ring component to drive localized nuclear-envelope breakdown and mitotic spindle-pole-body insertion

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Plo1 directly phosphorylates a spindle-pole-body ring component to drive localized nuclear-envelope
  breakdown and mitotic spindle-pole-body insertion
focus_type: free_text
context: []
reference_id: []
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

# AIGR Deep Research Report — *plo1* (S. pombe, UniProt P50528)

**Hypothesis slug:** `spb-insertion-mechanism`
**Seed hypothesis:** *Plo1 directly phosphorylates a spindle-pole-body (SPB) ring component to drive localized nuclear-envelope breakdown and mitotic SPB insertion.*
**Focus type:** free_text (core-function / mechanistic)

---

## Executive Judgment

**Verdict: Partially supported — the process is supported and already curated; the specific "direct phosphorylation of a ring component" molecular step is unresolved (inferred, not demonstrated).**

- **Supported (process/BP level):** Plo1 kinase **activity is genetically required** for the SPB-ring protein redistribution, the localized (partial) nuclear-envelope remodeling, and the insertion of the SPB into the nuclear envelope that build the mitotic spindle. This is exactly the process already captured by GO:0140480 (IMP).
- **Not established (molecular/MF level):** No primary study demonstrates a **direct kinase→substrate** reaction in which Plo1 phosphorylates a *named SPB ring component* to trigger NEBD/insertion. The directness and substrate identity are **inferred from loss-of-activity phenotypes**, not from an in-vitro/in-vivo phospho-site assay.
- **Wording caveat:** S. pombe undergoes **closed mitosis**. "Nuclear-envelope breakdown" should be qualified as **partial/local fenestration** ("insertion into the nuclear envelope"), as the seed's "localized" wording and the GO term already reflect. Global NEBD does **not** occur.
- **Notable constraint:** Plo1 is **not** required for the founding Sad1 ring redistribution (Bestul 2021), so any direct-phosphorylation model cannot be a single upstream Plo1→Sad1 event.

**Overall:** The hypothesis is a reasonable, literature-consistent *mechanistic model*, but the "**directly phosphorylates a SPB ring component**" clause exceeds the current evidence. Treat the process claim as **retained/justified**; treat the direct-substrate claim as a **hypothesis requiring a discriminating phospho-assay** before any substrate-specific MF annotation.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID 34133218 (Bestul et al. 2021, *Mol Biol Cell*) | Mutant phenotype + super-res localization (SIM) | Supports process; **qualifies directness** | Plo1 drives localized NEBD & SPB-ring formation for insertion | SPB proteins redistribute into a **ring** around the SPB (precursor for localized NEBD); **Plo1 activity is vital for redistribution of the other SPB ring proteins and for complete NEBD enabling SPB insertion**; **Plo1 is NOT required for Sad1 redistribution** | S. pombe mitosis; plo1 loss-of-activity | Functional necessity, **not a direct kinase–substrate assay**; no phospho-site mapped |
| PMID 24963130 (Wälde & King 2014, *J Cell Biol*) | Mutant phenotype + interaction | Supports process; qualifies directness | Plo1 promotes SPB remodeling/insertion into NE | **Plo1 activity drives a burst of Cut12/Pcp1 incorporation**; delayed Plo1 recruitment (Kms2 depletion) → SPB-insertion defects; Kms2 binds Cut12/Pcp1/Plo1 | S. pombe SUN-KASH (Kms2/Sad1) | Effect partly via **recruitment timing**; incorporation ≠ demonstrated direct phosphorylation |
| PMID 7744248 (Ohkura, Hagan & Glover 1995, *Genes Dev*) | Mutant phenotype | Supports essential role | plo1 essential for bipolar spindle | plo1 loss → **monopolar spindle / mitotic arrest**; overexpression → monopolar spindles + ectopic septa | S. pombe disruption/overexpression | **Pleiotropic** (also septation/actin ring); silent on direct SPB-ring phospho-mechanism |
| PMID 23222840 (Grallert et al. 2013, *Nature*) | Mutant phenotype + localization | Qualifies (context) | Local MPF activates Plo1 at G2 SPB | MPF activation of Plo1 on the SPB dictates timing of mitotic commitment & NETO | S. pombe SPB | Places Plo1 upstream in commitment; not a direct NEBD substrate mechanism |
| QuickGO record P50528 (76 annotations) | Database | Supports (process already curated) | Existing GO capture | **GO:0140480 "mitotic spindle pole body insertion into the nuclear envelope" (IMP)**; CC: mitotic SPB, half bridge, inner plaque (IDA); MF only **generic** Ser/Thr kinase activity | GO database | IMP = mutant-based; **no substrate-level MF annotated** |

*(Provenance CSVs saved during the run: `plo1_evidence_matrix.csv`, `plo1_go_decision_table.csv`.)*

---

## GO Curation Implications (leads — require curator verification)

| Term | Aspect | Action | Rationale |
|---|---|---|---|
| **GO:0140480** mitotic spindle pole body insertion into the nuclear envelope | BP | **RETAIN (IMP)** | Directly matches the seed's process claim; supported by PMID 34133218 and PMID 24963130 loss-of-activity phenotypes. |
| **GO:0004674** protein serine/threonine kinase activity | MF | **RETAIN** | Core catalytic activity (EXP/IBA/IDA). |
| Proposed **substrate-specific "phosphorylates SPB ring component"** MF/BP | MF | **DO NOT ADD (yet)** | No direct kinase–substrate assay; adding a specific substrate MF would **over-annotate** beyond the evidence. |
| GO:0007052 mitotic spindle organization | BP | RETAIN | Consistent with monopolar-spindle phenotype. |

- **Annotation provenance (verified this run):** the plo1 GO:0140480 annotation is a single record — `qualifier=involved_in, evidence=IMP, reference=PMID:34133218, assignedBy=PomBase`. PomBase itself curated this at **mutant-phenotype (IMP) / involved_in** strength — i.e., functional involvement, deliberately stopping short of a direct molecular-activity claim. The seed hypothesis's "directly phosphorylates a specific ring component" therefore **over-specifies** the mechanism relative to both the primary paper and the existing annotation.
- The **BP process** in the hypothesis is already annotated and justified — the hypothesis does **not** warrant a new/stronger BP term.
- The **MF layer** should stay at generic kinase activity. Do **not** promote to a substrate-specific molecular function, and do **not** fall back to "protein binding" as the informative term.
- If any curator statement asserts Plo1 *directly phosphorylates* a specific ring component, it should be flagged as **mechanistic inference (IMP-level), not IDA/direct-assay**.

---

## Mechanistic Scope

- **Immediate molecular activity (direct):** ATP-dependent protein serine/threonine kinase (Polo-like kinase) — well established.
- **Directly demonstrated at the SPB:** Plo1 **localizes** to the SPB (IDA) and its **catalytic activity is required** for mitotic SPB remodeling/insertion (loss-of-activity phenotype).
- **Inferred (not directly shown):** that a *specific SPB ring protein* is a **direct Plo1 phosphosubstrate**, and that this phospho-event is the trigger for local fenestration/insertion.
- **Downstream/pleiotropic (do not conflate with the core insertion mechanism):** mitotic commitment (Cdc25/Wee1 axis), septation-initiation-network activation, cytokinetic ring, NETO/polarity, meiotic SPB remodeling. Plo1's essentiality phenotypes are broad, so an SPB-insertion defect in a plo1 mutant is not, by itself, proof of a direct ring-substrate event.

---

## Conflicts and Alternatives

1. **Directness gap / alternative = indirect action:** Plo1 could enable insertion by controlling **recruitment/incorporation timing** of SPB components (Wälde & King: "burst of incorporation") rather than by directly phosphorylating a ring protein — the phenotype is consistent with either.
2. **Sad1 independence:** Plo1 is dispensable for Sad1 ring redistribution (Bestul 2021), so the "ring component" in the hypothesis cannot be Sad1; the responsible substrate (if any) is unidentified.
3. **Wording/organism biology:** "nuclear-envelope breakdown" risks importing an open-mitosis concept; S. pombe uses **partial/local fenestration** in an otherwise closed mitosis (cf. Brr6 fenestra work, PMID 22042620). The term should stay "insertion into the nuclear envelope."
4. **Pleiotropy / phenotype attribution:** plo1 null is pleiotropic (spindle + septation), so SPB-insertion phenotypes must be isolated from indirect commitment/SIN effects.
5. **No paralog-overannotation issue detected:** Plo1 is the single S. pombe Polo kinase; the concern here is *directness/substrate identity*, not paralog confusion.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Identity of the direct Plo1 substrate among SPB ring proteins | Searched primary literature + QuickGO MF annotations | Determines whether a substrate-specific MF/mechanism can be curated | In-vitro kinase assay + in-vivo phospho-site mapping (phosphoproteomics) on candidate ring proteins |
| Whether phosphorylation *causes* insertion vs. correlates | Bestul/Wälde phenotypes | Distinguishes direct trigger from permissive/recruitment role | Non-phosphorylatable (S/T→A) and phosphomimetic (S/T→D/E) substrate alleles rescuing/blocking insertion |
| Kinase-dead vs. localization-only separation | Grallert 2013 (activity timing) | Separates catalytic requirement from scaffolding | Analog-sensitive plo1 (as-plo1) acute inhibition during SPB insertion window |
| Exact NE-remodeling target (lipid/pore/fenestra machinery) | Brr6/Tts1 literature noted | Connects Plo1 activity to membrane fenestration | Epistasis of plo1 with brr6/apq12/tts1 for insertion |

---

## Discriminating Tests

1. **Analog-sensitive plo1 (as-plo1) acute inhibition** timed to the SPB-insertion window + live imaging of SPB/NE markers — tests catalytic necessity for insertion specifically (vs. earlier commitment).
2. **Candidate-substrate phospho-mapping:** IP–MS phosphoproteomics of SPB ring proteins (e.g., Cut12, Pcp1, Cut11, other ring proteins from Bestul 2021) ± active Plo1; confirm sites by in-vitro kinase assay with recombinant Plo1.
3. **Phosphosite allele swap:** non-phosphorylatable vs. phosphomimetic alleles of the top candidate; score SPB insertion/fenestration and bipolar spindle formation.
4. **Epistasis** of plo1 activity with brr6/apq12/tts1 fenestration mutants to place Plo1 relative to NE-membrane remodeling.
5. **Comparative check** with budding-yeast Polo (Cdc5)/Mps1 SPB-insertion pathways to test conservation of a direct ring-substrate mechanism.

---

## Curation Leads (require curator verification)

- **Action:** *Retain* BP GO:0140480 (IMP) and MF GO:0004674; **do not** add a substrate-specific "phosphorylates SPB ring component" MF/BP term at this time; **do not** downgrade to "protein binding."
- **Candidate references + snippets to verify:**
  - PMID **34133218**: "*its activity is vital for redistribution of other SPB ring proteins and for complete NEBD at the SPB to allow for SPB insertion*" and "*the Polo kinase Plo1 is not necessary for Sad1 redistribution*".
  - PMID **24963130**: "*Plo1 activity supports mitotic SPB remodeling by driving a burst of incorporation of Cut12 and Pcp1*".
  - PMID **7744248** (essentiality / monopolar spindle); PMID **23222840** (SPB-local Plo1 activation timing).
- **Suggested curator questions:**
  1. Is any statement in the review implying **direct phosphorylation** of a specific SPB ring component? If so, mark as **mechanistic inference**, not direct assay.
  2. Should the review text replace "nuclear-envelope breakdown" with "**localized/partial nuclear-envelope fenestration / SPB insertion into the nuclear envelope**" to match closed-mitosis biology?
- **Suggested experiments:** the discriminating tests above (as-plo1 timing; phospho-site mapping + S/T→A/D alleles).

---

## Limitations of this analysis

- Based on abstract-level literature synthesis and the public GO/QuickGO record; full-text methods were not parsed.
- No local sequence/structure computation was needed to adjudicate the core (directness) question; the decisive gap is an unavailable **direct kinase-substrate assay**, which cannot be substituted by bioinformatics.
- One citation-snippet auto-validation failed only because the stored abstract copy for PMID 34133218 was truncated; the verbatim text above is from the full NCBI abstract retrieved during the run.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)