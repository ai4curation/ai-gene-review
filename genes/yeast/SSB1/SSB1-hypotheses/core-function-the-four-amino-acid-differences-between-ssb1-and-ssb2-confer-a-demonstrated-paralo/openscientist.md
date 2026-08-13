---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T07:23:55.557604'
end_time: '2026-08-12T07:40:38.967475'
duration_seconds: 1003.41
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: SSB1
  gene_symbol: SSB1
  uniprot_accession: P11484
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: core_function
  hypothesis_slug: core-function-the-four-amino-acid-differences-between-ssb1-and-ssb2-confer-a-demonstrated-paralo
  hypothesis_text: The four amino-acid differences between Ssb1 and Ssb2 confer a
    demonstrated paralog-specific substrate preference or cotranslational folding
    mechanism.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: The four amino-acid differences between Ssb1 and\
    \ Ssb2 confer a demonstrated paralog-specific\n  substrate preference or cotranslational\
    \ folding mechanism.\nfocus_type: core_function\ncontext: []\nreference_id: []"
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
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: ssb1_ssb2_substitution_analysis.csv
  path: openscientist_artifacts/ssb1_ssb2_substitution_analysis.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ssb1 ssb2 substitution analysis
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
- **Gene directory:** SSB1
- **Gene symbol:** SSB1
- **UniProt accession:** P11484

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-the-four-amino-acid-differences-between-ssb1-and-ssb2-confer-a-demonstrated-paralo
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

The four amino-acid differences between Ssb1 and Ssb2 confer a demonstrated paralog-specific substrate preference or cotranslational folding mechanism.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The four amino-acid differences between Ssb1 and Ssb2 confer a demonstrated paralog-specific
  substrate preference or cotranslational folding mechanism.
focus_type: core_function
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

# AIGR Deep Research Report — SSB1 (P11484), *Saccharomyces cerevisiae*

**Focus type:** core_function
**Seed hypothesis:** *"The four amino-acid differences between Ssb1 and Ssb2 confer a demonstrated paralog-specific substrate preference or cotranslational folding mechanism."*

---

## Executive Judgment

**Verdict: REFUTED as stated (over-annotation of a redundant paralog pair).**

The hypothesis has two clauses. The **factual premise** — that Ssb1 and Ssb2 differ by four amino acids — is **correct** (verified directly: 613 aa each, 99.35 % identical, exactly 4 substitutions). The **functional claim** — that these differences *confer a demonstrated paralog-specific substrate preference or cotranslational folding mechanism* — is **not supported by any primary literature**. Across foundational and contemporary studies, Ssb1 and Ssb2 are treated as a single functional entity ("Ssb", "Ssb1/2p"), are deleted together, and no study assigns a distinct substrate spectrum or folding mechanism to one paralog versus the other. Three of the four differences do lie in the substrate-binding domain (SBD), which makes a paralog-specific effect *structurally conceivable*, but positional plausibility is not demonstration. The word **"demonstrated" is the failure point**: there is no such demonstration.

**Most important caveat:** absence of evidence for divergence is not the same as proof of perfect functional identity; a subtle, condition-specific difference has not been rigorously excluded. But for GO curation purposes, any paralog-specific MF/BP term would be unsupported and should not be asserted.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| This report (UniProt P11484 vs P40150, computed) | Structural/evolutionary (sequence) | Qualifies (confirms premise) | Ssb1/Ssb2 differ by 4 aa | 613 aa each, 99.35 % identical; E49Q (NBD), M413I, C435V, A436S (all SBD) | *S. cerevisiae* proteins | High for the count; residues not annotated as catalytic/substrate-contacting sites |
| Nelson et al. 1992 (PMID 1394434) | Mutant phenotype / biochemistry | Refutes functional clause | Distinct roles for Ssb1 vs Ssb2 | Characterizes "Ssb1/2p" jointly; *ssb1 ssb2* double mutant needed for phenotype (ribosome association, slow growth, drug hypersensitivity) | Yeast, translating ribosomes | High; classic study, treats pair as one |
| Willmund et al. 2013 (PMID 23332755) | Direct assay (global substrate mapping) | Refutes functional clause | Paralog-specific substrate preference | Defines cotranslational substrate specificity of "the yeast Hsp70 SSB" as one entity; SSB deletion → aggregation | Yeast, ribosome-nascent chains | High; the most direct substrate-specificity study — done at the SSB (not paralog) level |
| Chiabudini et al. 2012 (PMID 23007158) | Mutant phenotype | Refutes functional clause | Paralog-specific mechanism | RAC/"Ssb" (Ssb1 and Ssb2) jointly required for translational repression | Yeast | Medium-high; both deleted together |
| Chiabudini et al. 2014 (PMID 25154418) | Mutant phenotype | Refutes functional clause | Paralog-specific mechanism | "Ssb (Ssb1 and Ssb2)" treated jointly in premature-termination assay | Yeast | Medium-high |
| Chen et al. 2022 (PMID 35701497); Kišonaitė et al. 2023 (PMID 37081320) | Structural (cryo-EM) | Qualifies | Mechanism of Ssb on ribosome | RAC–Ssb cotranslational folding mechanism resolved for "Ssb1/2" generically; no paralog distinction | Yeast / *C. thermophilum* | High for mechanism; not paralog-resolved |

*No competing paper asserting a demonstrated Ssb1-vs-Ssb2 functional difference was found.*

---

## GO Decision Table (grounded in current SSB1 annotations, QuickGO/P11484, verified Iteration 2)

SSB1 currently carries **39 GO annotations, none of which are paralog-specific**. Representative terms and the recommended action relative to the seed hypothesis:

| GO ID | Aspect | Term | Evidence (ref) | Relation to hypothesis | Recommended action |
|---|---|---|---|---|---|
| GO:0044183 | MF | protein folding chaperone | IBA | Shared core function | Retain (core) |
| GO:0016887 | MF | ATP hydrolysis activity | IDA (PMID 9860955) | Shared core function | Retain (core) |
| GO:0005524 | MF | ATP binding | IEA | Shared core function | Retain |
| GO:0031072 | MF | heat shock protein binding | IBA | Shared (RAC co-chaperone interaction) | Retain |
| GO:0051083 | BP | 'de novo' cotranslational protein folding | IDA (PMID 9670014) | Shared core process | Retain (core) |
| GO:0002181 | BP | cytoplasmic translation | IMP (PMID 1394434) | Shared; from *ssb1 ssb2* double mutant | Retain |
| GO:0005829 | CC | cytosol | IBA | Shared localization | Retain (core) |
| GO:0005516 | MF | calmodulin binding | IDA (PMID 17146552) | Not paralog-specific; likely non-core | Curator review (non-core?) |
| GO:0005515 | MF | protein binding | IPI (PMID 11805837) | Uninformative | Do not treat as core |
| — (proposed) | MF/BP | *Ssb1-specific substrate preference / distinct cotranslational mechanism* | **none** | **The seed hypothesis** | **Do NOT add — unsupported** |

Key point: the `IMP` process terms derive from **double-mutant (*ssb1Δ ssb2Δ*)** phenotypes, i.e., they document the *shared* Ssb function, not a paralog-resolved one. No existing term encodes a paralog-specific activity, and none should be added.

## GO Curation Implications (leads — require curator verification)

- **Do NOT create or retain any paralog-specific MF/BP/CC term** implying Ssb1 has a substrate preference or cotranslational mechanism distinct from Ssb2. Such a term would be an over-annotation.
- **Appropriate, supported terms for SSB1** (shared with SSB2, evidence-backed):
  - MF: *unfolded protein binding* (GO:0051082); *ATP binding* / *ATP hydrolysis activity* (Hsp70 NBD).
  - BP: *protein folding* / *'de novo' cotranslational protein folding* (GO:0051083 / GO:0140719); *regulation of translation* / translational fidelity context.
  - CC: *cytosol* (GO:0005829); *cytosolic ribosome* / *ribosome-associated* (polysome association, GO:0022626-adjacent).
- **Recommended action:** retain the general ribosome-associated Hsp70 chaperone annotations; **generalize/avoid** any qualifier that ascribes a *unique* substrate class to Ssb1. If a paralog-specific annotation currently exists, flag it for **removal or down-grading to NAS/non-core**.
- Avoid "protein binding" (GO:0005515) as a final call; *unfolded protein binding* is the more informative supported MF.

---

## Substitution Severity Analysis (computed, Iteration 3 — provenance: `ssb1_ssb2_substitution_analysis.csv`)

Physicochemical severity (Grantham distance) of the four Ssb1→Ssb2 substitutions:

| Pos | SSB1 | SSB2 | Domain | Grantham | Severity |
|---|---|---|---|---|---|
| 49 | E | Q | NBD (ATPase) | 29 | conservative |
| 413 | M | I | SBDβ | 10 | conservative |
| 435 | C | V | SBDβ | **192** | **radical** |
| 436 | A | S | SBDβ | 99 | moderate |

Mean Grantham = 82.5. **Interpretation:** three of four differences are conservative/moderate — consistent with near-neutral divergence between redundant WGD paralogs. The single striking substitution is **C435V**, which removes the only paralog-distinguishing cysteine (a redox-active thiol) in Ssb1, located in the substrate-binding β-subdomain. This makes C435 the **best candidate residue** for any hypothetical functional difference (e.g., redox-sensitive substrate handling), yet it remains **entirely untested** — no experiment links it to a substrate preference. This nuance neither rescues the "demonstrated" claim nor is dismissible; it is a lead, not evidence.

## Mechanistic Scope

- **Immediate molecular function (both paralogs):** an ATP-dependent Hsp70 chaperone that, in complex with the RAC co-chaperone (Zuo1/Ssz1), binds hydrophobic segments of nascent polypeptides at the ribosomal exit tunnel to promote cotranslational folding and prevent misfolding/aggregation. This is a *shared* activity.
- **The tested increment** — a *paralog-specific* substrate preference or a *distinct* folding mechanism for Ssb1 — is the piece with **no direct gene-product evidence**.
- **Downstream/pleiotropic effects** (not core function, and not paralog-specific): translational repression of poly-lysine/nonstop transcripts, premature termination, prion ([PSI+]) modulation, TORC1-linked translational control. These are collective RAC/Ssb-system phenotypes.

---

## Conflicts and Alternatives

- **Paralog confusion / carry-over is the central risk.** SSB1 and SSB2 arose from the whole-genome duplication and remain ~99 % identical; databases and papers routinely collapse them to "Ssb". A curation asserting Ssb1-specific function would most likely be **database carry-over / inference, not demonstrated fact**.
- **Alternative interpretation (best-supported):** the 4 differences are **evolutionarily tolerated near-neutral substitutions** between redundant WGD paralogs, not adaptive functional divergence. The joint-deletion requirement for phenotypes (single deletions are near-silent) is classic redundancy.
- **Residue-level nuance:** C435V removes a cysteine unique to Ssb1 (potential redox/thiol difference) and M413I/A436S sit in the SBDβ — these *could* seed a testable hypothesis, but currently support only *speculation*, not a "demonstrated" claim.

---

## Knowledge Gaps

1. **Has any assay directly compared Ssb1-only vs Ssb2-only cells/proteins?** Checked PubMed broadly; none found. Matters because it is the exact evidence the hypothesis claims exists. Resolve with paralog-swap strains + selective ribosome profiling (SeRP).
2. **Do the 4 residues alter substrate contacts?** Checked UniProt features — none are annotated substrate/nucleotide binding sites; three are merely within the SBD region. Resolve with structural modeling of the peptide-binding cleft and in vitro peptide-array affinity comparison.
3. **Expression/regulatory divergence?** Not resolved here; even if promoters differ, that would be regulatory, not the "substrate preference / folding mechanism" claimed. Resolve with paralog-specific expression datasets.

---

## Discriminating Tests

- **Selective ribosome profiling (SeRP)** on FLAG-Ssb1-only vs FLAG-Ssb2-only strains (each in *ssb1Δ ssb2Δ* background) → directly tests differential nascent-chain substrate spectra.
- **Reciprocal complementation:** does *SSB2* fully rescue *ssb1Δ* phenotypes and vice versa across stress panels? Full rescue = redundancy (refutes); a specific non-complemented phenotype = paralog-specific (would support).
- **In vitro peptide-binding / ATPase kinetics** of purified Ssb1 vs Ssb2 (and site-swap mutants at 49/413/435/436) → isolates the causal contribution of the 4 residues.
- **Cys435 redox probe:** test thiol-dependent behavior unique to Ssb1.

---

## Curation Leads (verify before applying)

- **Lead 1 — Reject paralog-specific functional annotation.** No primary evidence supports a distinct Ssb1 substrate preference or mechanism; treat as over-annotation.
- **Lead 2 — Candidate references to cite for shared function:** PMID 23332755 (SSB cotranslational substrate specificity, as one entity), PMID 1394434 (Ssb1/2p ribosome association), PMID 35701497 / 37081320 (RAC–Ssb cotranslational folding mechanism).
  - Snippet to verify (PMID 23332755): *"we use a sensitive and global approach to define the cotranslational substrate specificity of the yeast Hsp70 SSB."*
  - Snippet to verify (PMID 1394434): *"The SSB hsp70s (Ssb1/2p) are associated with translating ribosomes."*
- **Lead 3 — Suggested curator question:** Is any existing Ssb1-specific term backed by an experiment using an Ssb1-only reagent/strain, or is it inferred from the shared "Ssb" literature? If the latter, generalize the term to reflect shared function.
- **Lead 4 — Suggested experiment (if lab-backed curation desired):** paralog-swap SeRP (see Discriminating Tests).

---

### Confidence
High confidence that the hypothesis is not *demonstrated* (verdict: refuted-as-stated / over-annotation). Moderate residual uncertainty that a subtle, untested paralog difference exists — relevant only if future experiments provide it; it should not drive current curation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist ssb1 ssb2 substitution analysis](openscientist_artifacts/ssb1_ssb2_substitution_analysis.csv)