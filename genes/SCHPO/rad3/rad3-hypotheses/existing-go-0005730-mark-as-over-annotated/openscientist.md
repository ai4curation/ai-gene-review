---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T08:24:50.366556'
end_time: '2026-09-01T08:43:58.051686'
duration_seconds: 1147.69
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: rad3
  gene_symbol: rad3
  uniprot_accession: Q02099
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: existing_go_annotation_decision
  hypothesis_slug: existing-go-0005730-mark-as-over-annotated
  hypothesis_text: 'The existing rad3 GO annotation to nucleolus (GO:0005730) should
    receive review action MARK_AS_OVER_ANNOTATED. Current rationale: A single localization
    observation; not a core functional site and not the principal compartment for
    Rad3 checkpoint activity.'
  term_context: '- Term: nucleolus (GO:0005730)

    - Evidence type: IDA

    - Original reference: PMID:18180284

    - Current review action: MARK_AS_OVER_ANNOTATED

    - Review summary: Nucleolar localization is weakly supported and likely a minor
    or context-specific pool. Rad3''s well-established sites of action are chromatin,
    stalled forks and telomeres, not the nucleolus.

    - Review reason: A single localization observation; not a core functional site
    and not the principal compartment for Rad3 checkpoint activity.'
  reference_context: '- PMID:18180284

    - PMID:17531813'
  source_file: genes/SCHPO/rad3/rad3-ai-review.yaml
  source_selector: existing_annotations[36]
  source_context_yaml: "term:\n  id: GO:0005730\n  label: nucleolus\nevidence_type:\
    \ IDA\noriginal_reference_id: PMID:18180284\nqualifier: is_active_in\nreview:\n\
    \  summary: Nucleolar localization is weakly supported and likely a minor or context-specific\
    \ pool. Rad3's\n    well-established sites of action are chromatin, stalled forks\
    \ and telomeres, not the nucleolus.\n  action: MARK_AS_OVER_ANNOTATED\n  reason:\
    \ A single localization observation; not a core functional site and not the principal\
    \ compartment\n    for Rad3 checkpoint activity.\n  supported_by:\n  - reference_id:\
    \ PMID:17531813\n    supporting_text: Cdc18 persists in a chromatin-bound complex\
    \ including the checkpoint kinases Rad3\n      and Rad26.\n    reference_section_type:\
    \ ABSTRACT"
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
citation_count: 12
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
- **Gene directory:** rad3
- **Gene symbol:** rad3
- **UniProt accession:** Q02099

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** existing-go-0005730-mark-as-over-annotated
- **Source file:** genes/SCHPO/rad3/rad3-ai-review.yaml
- **Source selector:** existing_annotations[36]

## Seed Hypothesis

The existing rad3 GO annotation to nucleolus (GO:0005730) should receive review action MARK_AS_OVER_ANNOTATED. Current rationale: A single localization observation; not a core functional site and not the principal compartment for Rad3 checkpoint activity.

## Term and Decision Context

- Term: nucleolus (GO:0005730)
- Evidence type: IDA
- Original reference: PMID:18180284
- Current review action: MARK_AS_OVER_ANNOTATED
- Review summary: Nucleolar localization is weakly supported and likely a minor or context-specific pool. Rad3's well-established sites of action are chromatin, stalled forks and telomeres, not the nucleolus.
- Review reason: A single localization observation; not a core functional site and not the principal compartment for Rad3 checkpoint activity.

## Reference Context

- PMID:18180284
- PMID:17531813

## Source Context YAML

```yaml
term:
  id: GO:0005730
  label: nucleolus
evidence_type: IDA
original_reference_id: PMID:18180284
qualifier: is_active_in
review:
  summary: Nucleolar localization is weakly supported and likely a minor or context-specific pool. Rad3's
    well-established sites of action are chromatin, stalled forks and telomeres, not the nucleolus.
  action: MARK_AS_OVER_ANNOTATED
  reason: A single localization observation; not a core functional site and not the principal compartment
    for Rad3 checkpoint activity.
  supported_by:
  - reference_id: PMID:17531813
    supporting_text: Cdc18 persists in a chromatin-bound complex including the checkpoint kinases Rad3
      and Rad26.
    reference_section_type: ABSTRACT
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

# AIGR Focused Review — rad3 (SCHPO, Q02099) nucleolus GO:0005730

**Gene:** rad3 (SPBC216.05) · **Organism:** *Schizosaccharomyces pombe* 972 / ATCC 24843 (NCBITaxon:284812) · **UniProt:** Q02099
**Focus:** existing GO annotation decision — `existing_annotations[36]` of `genes/SCHPO/rad3/rad3-ai-review.yaml`
**Hypothesis slug:** `existing-go-0005730-mark-as-over-annotated`
**Annotation under review:** nucleolus (GO:0005730), IDA, qualifier `is_active_in`, reference PMID:18180284
**Seed review action:** MARK_AS_OVER_ANNOTATED

---

## Summary

**The seed hypothesis is SUPPORTED, and on closer inspection the annotation is even weaker than "over-annotated" implies — it is a candidate for outright REMOVAL or reference correction.** The rad3→nucleolus (GO:0005730) association rests on a **single, uncorroborated IDA annotation** whose only cited primary source, PMID:18180284 (Bailis et al. 2008, *Mol. Cell. Biol.*, PMC2258774), does not localize Rad3 to the nucleolus — or anywhere. Full-text mining of that paper (~97,000 characters covering Abstract, Methods, Results, Discussion and References) recovered **zero** occurrences of "nucleol-", "rDNA", "ribosom-", or "GFP", and the only Rad3 mentions (4 total) are genetic/pathway references (Rad3–Cds1 checkpoint, Δrad3 mutant, Rad3 required for Cds1 activation, and one citation). The proteins actually imaged in that study are Rad22-YFP, Rhp51, Mcm4, Rad52, Crb2 and phospho-H2A. **Rad3 itself was never subjected to a localization assay.** This strongly indicates the annotation is a **mis-attributed reference or a curation error**, not a genuine minor or context-specific pool.

Independent lines of evidence corroborate the over-annotation call. QuickGO returns exactly **one** annotation linking Q02099 to GO:0005730 (IDA/ECO:0000314, assigned by PomBase, qualifier `is_active_in`); no second, independent primary source exists. The genome-wide YFP ORFeome localization screen (PMID:16823372) places Rad3 in the **cytosol/diffuse** signal, not the nucleolus. The intensively studied human ortholog ATR (Q13535) is **not** curated to the nucleolus; its curated compartments are nucleoplasm, chromosome, PML body, nuclear envelope and sites of DNA damage. Where ATR-family kinases do engage the nucleolus in mammals, the activity is demonstrably **stress-induced and context-specific** (TopBP1 overexpression, RNA Pol I inhibition), not a constitutive core compartment.

Rad3's established, multiply corroborated sites of action are the **ATR–ATRIP (Rad3–Rad26) complex, chromatin/stalled replication forks, and telomeres** — each supported by multiple primary references with IDA evidence. The `is_active_in` qualifier on the nucleolus term is particularly problematic because it asserts *functional activity* in a compartment where neither the cited paper nor any other primary source demonstrates Rad3 presence, let alone function. **Recommended lead: REMOVE or correct the reference; MARK_AS_OVER_ANNOTATED is fully supported as a conservative floor**, pending a curator's inspection of the journal PDF and supplemental figures to exclude a reference typo or overlooked panel.

---

## Executive Judgment

**Verdict: SUPPORTED — and the underlying evidence is weaker than the seed states.** The over-annotation call is justified; the evidence in fact points toward outright **removal / reference correction**, subject to a curator's check of the published PDF and supplemental figures.

The decisive result is the full-text mining of the cited reference (Finding 2). Because the annotation carries evidence code **IDA/ECO:0000314** ("inferred from direct assay"), it requires a demonstrated experimental localization of Rad3 in the cited paper. No such assay exists in PMID:18180284. The annotation therefore **fails its own evidence-code requirement**. The strongest residual caveat is that retrieval was of the PMC HTML article, so a small chance remains that a separately hosted supplemental figure contains Rad3 data — although the main text and figure legends never mention the nucleolus and give no indication Rad3 was imaged.

---

## Key Findings

### Finding 1 — The nucleolus annotation is single-source and non-core; the over-annotation call is justified

Rad3's curated cellular-component (CC) annotations span several compartments, but they are not of equal evidential weight. Assembling the PomBase curated set for SPBC216.05 / Q02099:

| Compartment (GO CC) | Evidence | Supporting references | Corroboration |
|---|---|---|---|
| ATR–ATRIP complex (GO:1990635) | IDA | PMID:10559981 | Core complex — the Rad3–Rad26 heterodimer |
| chromatin (GO:0000785) | IDA | PMID:17531813, PMID:21945095 | Multiple references |
| telomeric repeat–containing region | IDA | PMID:12196391, PMID:20140190 | Multiple references |
| nuclear chromosome | IDA | PMID:8843195 | Consistent with chromatin role |
| cytosol | HDA | PMID:16823372 | Genome-wide ORFeome screen |
| **nucleolus (GO:0005730)** | **IDA** | **PMID:18180284 (only)** | **None — single source** |

The nucleolus term is the **only** CC annotation resting on a single IDA, and its source paper (Bailis et al. 2008) is primarily about the MCM complex and replication-fork protection; its abstract does not mention the nucleolus. The genome-wide YFP ORFeome study (PMID:16823372) that systematically localized *S. pombe* proteins assigned Rad3 to a **cytosolic/diffuse** signal — an orthogonal, high-throughput dataset that fails to reproduce a nucleolar pool. The deeply studied human ortholog **ATR (Q13535)** carries curated CC terms for nucleoplasm, chromosome, PML body, nuclear envelope and sites of DNA damage, but **no nucleolus term**, despite decades of study.

Where mammalian ATR/ATM signaling has been documented at the nucleolus, it is explicitly **inducible and stress-dependent**: TopBP1 overexpression triggers ATR-dependent shut-down of rRNA transcription and nucleolar segregation (PMID:25916852), and Pol I transcription inhibition (CX-5461) activates non-canonical ATM/ATR signaling within nucleoli (PMID:27391441). These are context-specific responses, not evidence of a constitutive nucleolar compartment for the checkpoint kinase. Taken together, the nucleolus annotation is single-source, non-core, and inconsistent with orthogonal localization data and ortholog curation — **MARK_AS_OVER_ANNOTATED is well supported.**

### Finding 2 — The cited reference PMID:18180284 contains no Rad3 localization and never mentions the nucleolus; the annotation is likely mis-attributed

This is the decisive finding. Full text of PMID:18180284 (Bailis et al. 2008, PMC2258774; ~97,000 characters including Abstract, Methods, Results, Discussion and References) was mined directly:

- `nucleol` → **0 occurrences**
- `rDNA` → **0 occurrences**
- `ribosom` → **0 occurrences**
- `GFP` → **0 occurrences**
- `Rad3` → **4 occurrences**, all as genetic/pathway references (the Rad3–Cds1 checkpoint; the Δrad3 mutant; Rad3 required for Cds1 activation; one bibliographic citation). None occurs within 60 characters of "foci", "focus", "localiz", "nucle", "stain", "YFP" or "GFP".

The proteins actually imaged in the paper are **Rad22-YFP, Rhp51, Mcm4, Rad52, Crb2 and phospho-H2A**. Rad3 itself is never subjected to a localization assay. The PomBase annotation detail (id 433558) records IDA / ECO:0000314, low-throughput, assigned_by PomBase on 2015-11-25, with no extension and only the `is_active_in` qualifier. Because IDA/ECO:0000314 demands a demonstrated experimental localization in the cited paper, and no such assay for Rad3 exists in PMID:18180284, **the annotation fails its own evidence-code requirement.** The two most parsimonious explanations are (1) a mis-attributed/typo'd reference (the wrong PMID was entered), or (2) a curation slip in which text about a different imaged protein was mapped to Rad3. Either way, the citation does not support the term.

### Finding 3 — QuickGO confirms a single, uncorroborated `is_active_in` nucleolus annotation

An independent QuickGO annotation search (geneProductId=Q02099, goId=GO:0005730) returns **numberOfHits = 1**: IDA / ECO:0000314, reference PMID:18180284, assignedBy PomBase, qualifier `is_active_in`. There is no second or independent annotation from any other database or reference. Targeted PubMed searches for an alternative primary paper reporting *S. pombe* Rad3 nucleolar localization returned none. The `is_active_in` qualifier is especially problematic: it asserts that Rad3 is **functionally active** in the nucleolus, a claim demanding functional evidence there. The cited paper provides neither localization nor function, so an `is_active_in nucleolus` assertion is unsupported on its own terms.

---

## Mechanistic Model / Interpretation

The entity under evaluation is **Rad3**, the *S. pombe* ATR-family PIKK Ser/Thr checkpoint kinase (InterPro domains: PI3/4-kinase catalytic, FAT, FATC, HEAT-ATR, UME). It functions as the Rad3–Rad26 (ATR–ATRIP) heterodimer — the sensor apex of the DNA replication/damage checkpoint — sensing stalled replication forks and DNA damage and activating downstream effector kinases Cds1 and Chk1. The GO term in question, nucleolus (GO:0005730), asserts a cellular location (and, via `is_active_in`, a functional site) that must be judged against where Rad3 is actually demonstrated to reside and act.

```
   Rad3 established sites of action (multiply corroborated)
   ┌───────────────────────────────────────────────────────────┐
   │  Rad3–Rad26 (ATR–ATRIP) complex  ── PMID:10559981 (IDA)     │
   │  chromatin / stalled forks       ── PMID:17531813,21945095  │
   │  telomeric repeat region         ── PMID:12196391,20140190  │
   │  nuclear chromosome              ── PMID:8843195            │
   └───────────────────────────────────────────────────────────┘
                         │  activates
                         ▼
              Cds1 / Chk1 effector kinases
                         │
                         ▼
   Downstream: Clp1/Flp1 released FROM the nucleolus on stress
   (PMID:18385517, 22918952) — a SUBSTRATE relocalization event,
   NOT evidence that Rad3 itself resides in the nucleolus.

   Nucleolus (GO:0005730) annotation
   ┌───────────────────────────────────────────────────────────┐
   │  Single IDA · PMID:18180284 · qualifier is_active_in        │
   │  → cited paper: 0 mentions of nucleolus/rDNA/ribosom/GFP    │
   │  → Rad3 never imaged; proteins imaged = Rad22, Rhp51, Mcm4… │
   │  → orthogonal ORFeome screen: Rad3 = cytosol/diffuse        │
   │  → human ATR ortholog: NOT curated to nucleolus             │
   └───────────────────────────────────────────────────────────┘
```

A crucial conceptual distinction is that **downstream substrates of the Rad3 pathway do relocalize at the nucleolus**. The Cdc14-family phosphatase Clp1/Flp1 is nucleolar-sequestered and is released into the nucleoplasm on replication stress in a Cds1/checkpoint-dependent manner (PMID:18385517, PMID:22918952). This is genuine and interesting nucleolar biology — but it concerns the **substrate (Clp1/Flp1)**, not Rad3 itself. It would be an error to infer Rad3 nucleolar residence from the nucleolar release of one of its pathway's downstream targets. This substrate-versus-kinase conflation is a plausible route by which a nucleolar annotation could have entered Rad3's record. The correct GO representation of Rad3's function localizes it to chromatin, forks and telomeres — the sites where the kinase is directly demonstrated to bind and act.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID:18180284](https://pubmed.ncbi.nlm.nih.gov/18180284/) | Localization (IDA) — annotation source | **Refutes / not supported** | rad3 in nucleolus | Full-text mining: 0 mentions of "nucleolus"/"rDNA"; Rad3 never imaged (only Rad22, Rhp51, Mcm4, Rad52, Crb2, γH2A localized). Cited paper does not support any Rad3 localization | *S. pombe*, MCB 2008 | Medium–High: complete main text mined (~97k chars, PMC2258774); residual risk from separately-hosted supplements |
| [PMID:16823372](https://pubmed.ncbi.nlm.nih.gov/16823372/) | Genome-wide localization (HDA) | Refutes core nucleolar call | Steady-state rad3 location | ORFeome YFP screen assigns rad3 to **cytosol/diffuse**, not nucleolus | *S. pombe*, systematic | Medium–High: systematic but low resolution; tag/expression caveats |
| [PMID:17531813](https://pubmed.ncbi.nlm.nih.gov/17531813/) | Interaction/localization (IDA) | Supports core = chromatin | rad3 site of action | "Cdc18 persists in a chromatin-bound complex including the checkpoint kinases Rad3 and Rad26" | *S. pombe* | High |
| [PMID:12196391](https://pubmed.ncbi.nlm.nih.gov/12196391/) | Localization (IDA) | Supports core = telomere | rad3 site of action | Checkpoint sensors incl. rad3 bind **telomeres** | *S. pombe* | High |
| [PMID:20140190](https://pubmed.ncbi.nlm.nih.gov/20140190/) | Recruitment/localization (IDA) | Supports core = chromatin/telomere | rad3 site of action | Kinase-independent Rad3–Rad26 recruitment role | *S. pombe* | High |
| [PMID:10559981](https://pubmed.ncbi.nlm.nih.gov/10559981/) | Complex (IDA) | Supports core assembly | Rad3–Rad26 complex | ATR–ATRIP (Rad3–Rad26) complex responds to DNA damage | *S. pombe* | High |
| UniProt Q13535 (human ATR) | Curated database | Supports over-annotation | Is nucleolus a curated ATR compartment? | ATR CC = nucleoplasm, chromosome, PML body, nuclear envelope, DNA-damage sites — **no nucleolus** | Human, curated | Medium: ortholog inference; absence weaker than positive evidence |
| [PMID:25916852](https://pubmed.ncbi.nlm.nih.gov/25916852/) | Mechanism (mammalian) | Qualifies (context-specific) | ATR at nucleolus | "TopBP1-induced nucleolar segregation is coupled to shut-down of ribosomal RNA transcription in an ATR-dependent manner" | Human cells | Medium: real but induced |
| [PMID:27391441](https://pubmed.ncbi.nlm.nih.gov/27391441/) | Mechanism (mammalian) | Qualifies (context-specific) | ATR/ATM in nucleolus | Pol I inhibition (CX-5461) activates ATM/ATR signaling **within nucleoli** | Human cells | Medium: stress-induced |
| [PMID:18385517](https://pubmed.ncbi.nlm.nih.gov/18385517/) | Mechanism/localization | Competing/alternative | Is nucleolar biology about Rad3 or its substrate? | "Active Cds1p checkpoint kinase is required to release Flp1p into the nucleus" — a substrate event | *S. pombe* | High: clarifies nucleolar link is downstream substrate |
| [PMID:22918952](https://pubmed.ncbi.nlm.nih.gov/22918952/) | Mechanism/localization | Competing/alternative | Same as above | Rad3-effector kinases Cds1/Chk1 phosphorylate Clp1 to drive nucleoplasmic accumulation | *S. pombe* | High: reinforces substrate-relocalization interpretation |

*(Computed provenance from the iterations was saved as `evidence_matrix.csv`, `rad3_CC_provenance.csv`, and `GO_decision_table.csv`.)*

---

## GO Curation Implications

**Lead (requires curator verification): remove or correct the reference for GO:0005730 (nucleolus, CC) on rad3.**

- **Term class:** GO:0005730 is a cellular-component term. The question is whether the nucleolus is even a supported localization of Rad3, and whether it is *core*. The weight of evidence says the cited support is **absent** and the nucleolus is **not core** — chromatin, forks, telomeres and the ATR–ATRIP complex are the core CCs.
- **Primary recommendation: REMOVE** (IDA/ECO:0000314 is not satisfied by PMID:18180284 — the paper neither images Rad3 nor mentions the nucleolus). At minimum, the reference is wrong and must be corrected.
- **Fallback (if an inaccessible supplemental figure does show Rad3 in the nucleolus): MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE** with a context/stress qualifier — still not a core compartment.
- **`is_active_in` qualifier:** This is the strongest form of location assertion (functional activity in the compartment) and is the least defensible here — it should be dropped along with the term.
- **What the evidence *does* support (unchanged):** chromatin (GO:0000785), telomeric repeat–containing region, nuclear chromosome, and the ATR–ATRIP kinase complex (GO:1990635) remain well corroborated.
- **Avoided fallback:** No "protein binding" fallback is invoked; the recommendation is specific.
- **Bottom line:** The seed action **MARK_AS_OVER_ANNOTATED is supported and, if anything, conservative.**

---

## Mechanistic Scope

The immediate molecular function of Rad3 is a **PIKK Ser/Thr protein kinase** acting as the sensor apex of the DNA replication/damage checkpoint, functioning as the Rad3–Rad26 (ATR–ATRIP) complex. Its direct action occurs on **chromatin at stalled replication forks and at telomeres**, where it phosphorylates downstream effectors (Cds1, Chk1). Direct gene-product activity (the kinase acting on chromatin/forks/telomeres) is not in dispute. What is in dispute is whether Rad3 *resides and is active in the nucleolus* — and the available primary evidence does not place it there. The nucleolar phenomena in this pathway that are real (Clp1/Flp1 release from the nucleolus; mammalian ATR-dependent rRNA shut-down) are either **downstream substrate relocalizations** or **stress-induced context-specific responses of orthologs**, not constitutive Rad3 nucleolar residence. Any nucleolar/rDNA role (as inferred from mammalian ATR) would be a **downstream, stress-inducible** activity, not the primary function.

---

## Conflicts and Alternatives

1. **Substrate–kinase conflation (most likely).** The Rad3 pathway has a bona fide nucleolar node — Clp1/Flp1 sequestration and checkpoint-dependent release (PMID:18385517, PMID:22918952). A curation step that linked "nucleolar checkpoint biology" to Rad3 rather than to its substrate would produce exactly this annotation. This alternative reinforces removal.
2. **Reference mis-attribution / typo (strongest alternative, now evidenced).** Full-text mining of PMID:18180284 found no Rad3 localization experiment and no mention of the nucleolus. The most parsimonious explanation is a mis-attributed reference or curation slip — the annotation may have been intended for a different paper, or the curator conflated Rad3 with another imaged protein. If confirmed, this favours **REMOVE**.
3. **Genuine but context-specific nucleolar biology of ATR-family kinases** (PMID:25916852, PMID:27391441). ATR is recruited to rDNA/nucleoli during nucleolar stress and Pol I inhibition, so the term is *not biologically absurd* — it argues for "non-core/context-specific" rather than "impossible," if any signal survives verification.
4. **Systematic vs. targeted disagreement.** The ORFeome screen (cytosol) and the single IDA (nucleolus) disagree; both are low-to-medium resolution for a diffuse nuclear kinase. Neither establishes the nucleolus as a preferred compartment.
5. **No paralog confusion in *S. pombe*.** Rad3 is the single-copy PIKK-ATR; Tel1 is the ATM ortholog, separately annotated. Cross-organism carry-over is also unlikely, since human ATR is itself not curated to nucleolus.

---

## Limitations and Knowledge Gaps

1. **Exact content of PMID:18180284 for Rad3.** Checked: abstract and complete main text/legends/references via PMC HTML (PMC2258774) — "nucleolus" and "rDNA" absent; Rad3 never imaged. Remaining unknown: separately hosted **supplemental figures** could not be programmatically retrieved. This matters because it decides REMOVE vs. non-core. Resolve by opening the journal PDF + supplemental files and confirming no Rad3-nucleolus panel exists.
2. **Independent *S. pombe* evidence for nucleolar Rad3.** Checked PomBase CC set and ORFeome — none corroborate the nucleolus. A second independent localization (endogenous tag, high resolution, or under replication stress) would resolve whether a minor nucleolar pool is reproducible.
3. **Functional relevance at rDNA in fission yeast.** No *S. pombe* assay ties Rad3 catalytic function to rDNA/nucleolar processes. A Rad3-dependent phenotype at rDNA (fork stalling, rDNA stability, Pol I regulation) would upgrade the term from CC-only to functionally meaningful.
4. **Negative-evidence weight of ortholog curation.** ATR lacking a nucleolus CC term is suggestive but is absence-of-evidence, not evidence-of-absence.

---

## Discriminating Tests

- **Re-read PMID:18180284** localization figures/legends (main + supplemental) to confirm whether any Rad3 image panel exists and, if so, its marker, condition and quantitation.
- **Endogenous high-resolution imaging** of Rad3-GFP/mNeonGreen (native locus) with a nucleolar marker (Gar2/Nop1/fibrillarin) and rDNA FISH, ± replication stress (HU) / rDNA fork-block, to test for a reproducible minor nucleolar pool vs. general nucleoplasmic signal.
- **rDNA-directed ChIP / CUT&RUN** of Rad3–Rad26 to test physical association with rDNA repeats.
- **Curation provenance audit:** retrieve PomBase annotation id 433558 history and original curator note to verify the intended reference and figure.
- **Functional test:** rad3Δ (or kinase-dead) effect on rDNA stability / Pol I regulation to determine whether any nucleolar presence is functional.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

- **Primary action lead:** **REMOVE** GO:0005730 (nucleolus, IDA, PMID:18180284) — or, at minimum, flag the reference as not supporting the annotation and request re-curation. The seed's **MARK_AS_OVER_ANNOTATED** is fully supported as a floor.
- **Decisive verifiable evidence:** Full text of PMC2258774 mined — "nucleolus"/"nucleolar" = 0 occurrences; "rDNA"/"ribosom-" = 0; "Rad3" = 4 occurrences, all genetic/pathway, none localization; imaged proteins = Rad22-YFP, Rhp51, Mcm4, Rad52, Crb2, phospho-H2A (Rad3 absent). *Curator: reproduce by searching the article PDF for "nucleol" and for any Rad3 image panel.*
- **Candidate supporting references / snippets to verify:**
  - PMID:16823372 (ORFeome) — systematic localization assigns rad3 to cytosol, not nucleolus.
  - PMID:17531813 — *"Cdc18 persists in a chromatin-bound complex including the checkpoint kinases Rad3 and Rad26."* (core = chromatin).
  - PMID:18385517 — *"Active Cds1p checkpoint kinase is required to release Flp1p into the nucleus"* (nucleolar biology here is a substrate event, not Rad3 residence).
  - UniProt Q13535 — human ATR curated CC lacks a nucleolus term.
  - PMID:25916852 / PMID:27391441 — ATR-family nucleolar activity is stress/context-specific (rationale for "non-core," not "impossible").
- **Suggested curator questions:** (1) Does PMID:18180284 actually contain any Rad3 localization panel (main or supplemental)? (2) If not, was the intended reference a different paper, and which? (3) Should PomBase annotation id 433558 be retracted or re-referenced?
- **Suggested experiment (only if a genuine signal must be resolved):** Endogenous Rad3-GFP + nucleolar marker (Gar2/fibrillarin) colocalization ± HU (see Discriminating Tests).

---

### Bottom line

The seed action **MARK_AS_OVER_ANNOTATED is supported**, and full-text mining of the cited reference (PMC2258774) shows the evidence is weaker still: the paper never mentions the nucleolus and never localizes Rad3, so the annotation is most likely a **mis-attributed reference / curation error and a candidate for REMOVE**. Rad3's core compartments are the ATR–ATRIP complex, chromatin/stalled forks and telomeres. A curator should confirm against the journal PDF + supplemental figures before finalizing REMOVE vs. non-core.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)