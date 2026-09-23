---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T00:23:35.574709'
end_time: '2026-09-21T00:36:46.539219'
duration_seconds: 790.96
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: HST1
  gene_symbol: HST1
  uniprot_accession: P53685
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: histone-site-specificity-telomeres-and-dna-maintenance
  hypothesis_text: Saccharomyces cerevisiae Hst1 deacetylates histone H3K14 or H3K9
    in an NAD-dependent reaction, participates in native subtelomeric heterochromatin,
    localizes to telomeric regions, responds to DNA damage or negatively regulates
    recombination. Adjudicate each independently. Distinguish native Hst1 from Sir2/Hst2
    and SUM1-1 or engineered contexts, biochemical activity from major physiological
    substrate, and direct recombination control from secondary transcriptional effects.
    H4K5 preference is not exclusion of other sites. Existing general research does
    not settle target-specific versions of these claims; PMID:18990212 already supports
    context-specific H4K16 effects and PMID:27185881 conditional HMR effects, so those
    are not the unresolved questions.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/HST1/HST1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae Hst1 deacetylates histone\
    \ H3K14 or H3K9 in an NAD-dependent reaction,\n  participates in native subtelomeric\
    \ heterochromatin, localizes to telomeric regions, responds to DNA\n  damage or\
    \ negatively regulates recombination. Adjudicate each independently. Distinguish\
    \ native Hst1\n  from Sir2/Hst2 and SUM1-1 or engineered contexts, biochemical\
    \ activity from major physiological substrate,\n  and direct recombination control\
    \ from secondary transcriptional effects. H4K5 preference is not exclusion\n \
    \ of other sites. Existing general research does not settle target-specific versions\
    \ of these claims;\n  PMID:18990212 already supports context-specific H4K16 effects\
    \ and PMID:27185881 conditional HMR effects,\n  so those are not the unresolved\
    \ questions.\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 8
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: HST1_GO_decision_table.csv
  path: openscientist_artifacts/HST1_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HST1 GO decision table
- filename: HST1_GO_evidence_matrix.csv
  path: openscientist_artifacts/HST1_GO_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HST1 GO evidence matrix
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
- **Gene directory:** HST1
- **Gene symbol:** HST1
- **UniProt accession:** P53685

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** histone-site-specificity-telomeres-and-dna-maintenance
- **Source file:** genes/yeast/HST1/HST1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Hst1 deacetylates histone H3K14 or H3K9 in an NAD-dependent reaction, participates in native subtelomeric heterochromatin, localizes to telomeric regions, responds to DNA damage or negatively regulates recombination. Adjudicate each independently. Distinguish native Hst1 from Sir2/Hst2 and SUM1-1 or engineered contexts, biochemical activity from major physiological substrate, and direct recombination control from secondary transcriptional effects. H4K5 preference is not exclusion of other sites. Existing general research does not settle target-specific versions of these claims; PMID:18990212 already supports context-specific H4K16 effects and PMID:27185881 conditional HMR effects, so those are not the unresolved questions.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae Hst1 deacetylates histone H3K14 or H3K9 in an NAD-dependent reaction,
  participates in native subtelomeric heterochromatin, localizes to telomeric regions, responds to DNA
  damage or negatively regulates recombination. Adjudicate each independently. Distinguish native Hst1
  from Sir2/Hst2 and SUM1-1 or engineered contexts, biochemical activity from major physiological substrate,
  and direct recombination control from secondary transcriptional effects. H4K5 preference is not exclusion
  of other sites. Existing general research does not settle target-specific versions of these claims;
  PMID:18990212 already supports context-specific H4K16 effects and PMID:27185881 conditional HMR effects,
  so those are not the unresolved questions.
focus_type: function_assignment
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

# HST1 (P53685, *S. cerevisiae*) — Focused Hypothesis Adjudication

**Focus:** function_assignment · slug `histone-site-specificity-telomeres-and-dna-maintenance`
**Source:** genes/yeast/HST1/HST1-ai-review.yaml (free-text hypothesis)
**Iteration:** 1 of 3

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — the compound seed hypothesis is a mix of one well-supported claim and several over-annotated / unresolved claims.**

The seed bundles five independent claims. Adjudicated separately:

| Sub-claim | Verdict |
|---|---|
| (1) NAD-dependent deacetylase activity | **Supported (direct)** |
| (1b) Specific H3K14 **or** H3K9 site as the physiological substrate | **Weakly supported / unresolved** — direct evidence is for *general* NAD-dependent HDAC activity and for **H4K5ac** as the in vivo mark; H3K9/H3K14 terms are **phylogenetic inference (IBA) only** |
| (2) Participates in **native** subtelomeric heterochromatin | **Refuted for native Hst1** — Hst1 is a *gene-specific* Sum1–Rfm1 corepressor; regional/telomeric silencing is the Sir2 function |
| (3) Localizes to telomeric regions | **Refuted/unsupported for native Hst1** (annotation is IEA only); telomere/HM localization occurs only in the engineered **SUM1‑1** gain-of-function context (at HM loci, not telomeres) |
| (4) Responds to DNA damage | **Weakly supported / mostly attributable to other sirtuins** — the DNA-damage-response term is **IBA only**; the genotoxin-sensitivity phenotype is dominated by Hst3/Hst4 (H3K56ac) |
| (5) Negatively regulates recombination | **Weakly supported / likely refuted for native rDNA recombination** — the founding *hst1Δ* study (PMID:8810037) reports **no rDNA-recombination phenotype**; an IMP annotation (GO:0045950) exists for a specific context, but direct control vs. secondary transcriptional effect is unresolved |

**Core reasoning.** Native Hst1's primary, directly-demonstrated function is **NAD⁺-dependent, Sum1–Rfm1-tethered, promoter-local histone deacetylation that gene-specifically represses** middle-sporulation genes, de novo NAD⁺-biosynthesis (*BNA*) genes, and stress genes. The seed's histone-site, telomere, subtelomeric-heterochromatin, and DNA-damage claims map almost one-to-one onto **IBA/IEA (inferred, non-experimental)** GO annotations that read as paralog carry-over from Sir2. This is the central curation signal.

**Most important caveats.** (i) "H4K5 preference is not exclusion of other sites" is fair — but the burden of proof for target-specific H3K9/H3K14 native activity is unmet by primary data. (ii) PMID:18990212 (H4K16 context effects) and PMID:27185881 (conditional HMR effects) were pre-excluded as already-settled and were not re-litigated here.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| 12972620 (Bedalov 2003) | Direct assay + expression | **Supports (1)**; qualifies (1b) | NAD-dependent activity; physiological target | Hst1 is an NAD⁺ sensor; its NAD-dependent deacetylase activity **directly** represses de novo NAD⁺ biosynthesis genes | *S. cerevisiae*, in vivo + transcriptomics | High for NAD-dependence & gene-specific repression; does not localize activity to H3K9/H3K14 |
| 17242192 (Mead 2007) | Domain-swap chimeras / mutant | **Refutes (2),(3)** for native Hst1 | Gene-specific vs regional silencing | Hst1→Rfm1/Sum1 = gene-specific promoter repression; Sir2→Sir3/Sir4 = telomere/HM regional silencing; specificity set by cofactors, not enzymatic difference | *S. cerevisiae* | High; the cleanest native Hst1-vs-Sir2 separation |
| 12612074 (McCord 2003) | Interaction + mutant | Qualifies mechanism | Targeting architecture | Rfm1 tethers Hst1 to Sum1 at specific promoters | *S. cerevisiae* | High; explains promoter-local (not domain-wide) action |
| 29066473 (Jaiswal 2017) | Mutant phenotype + ChIP | Qualifies (1b) | In vivo histone substrate | Loss of Sum1–Hst1 → **increased H4K5ac** at target loci | *S. cerevisiae*, vegetative | Moderate–high; identifies H4K5 (not H3K9/H3K14) as the documented mark |
| 11316790 (Rusché & Rine 2001) | Mutant / ChIP | Qualifies (2),(3) — context-gates them | Hst1 in silencing | **SUM1‑1** relocalizes Sum1 to **HM loci** via ORC; Hst1 gives Sir-independent silencing w/ nucleosome hypoacetylation | Engineered SUM1‑1, HM loci | High; explicitly a gain-of-function, non-native context |
| 11313477 (Sutton 2001) | Mutant / genetic | Qualifies (2),(3) | Hst1 requirement in SUM1‑1 silencing | SUM1‑1 silencing at HMR requires Hst1 + its NAD⁺ activity + ORC | Engineered SUM1‑1, HMR | High; confirms context dependence |
| 26748095 (Simoneau 2016) | Genome-wide fitness + genetics | Qualifies (4) | Sirtuins & DNA-damage | Genotoxin phenotypes mainly from **Hst3/Hst4** (H3K56ac), not Hst1 | *S. cerevisiae* | High that DNA-damage role is largely non-Hst1 |
| 24710277 (Corbi 2014) | ChIP + genetics | Qualifies (5) | NDT80/meiotic control | Sum1 (not Hst1) determines NDT80 DNA occupancy; Hst1 is the enzymatic partner | *S. cerevisiae* meiosis | Moderate; recombination link is indirect/transcriptional |
| 26122277 (De Las Peñas 2015, review) | Review/database | Qualifies (2) | Local vs regional silencing | In *C. glabrata*: Hst1+Sum1–Rfm1 = **local** silencing; Sir2 = regional/telomeric | *Candida glabrata* | Orientation only; consistent cross-species division of labor |
| 8810037 (Derbyshire 1996) | Mutant phenotype (founding characterization) | **Refutes (2),(5)** for native Hst1 | rDNA recombination & regional silencing | *hst1Δ* shows **no phenotype** in rDNA recombination or regional HMLα silencing; HST1 is 71% identical to SIR2 | *S. cerevisiae*, native loss-of-function | High; original clean deletion test — argues against native recombination/regional roles |
| UniProt/GO P53685 (computed) | Database (evidence codes) | Frames all claims | Annotation provenance | H3K14/H3K9/H4K16 MF, subtelomeric-heterochromatin BP, DNA-damage BP = **IBA**; telomeric-region CC = **IEA**; only general NAD-HDAC = **IDA** | Annotation audit | Direct computed provenance (see CSV artifact) |
| HST1 vs SIR2 alignment (computed) | Structural/evolutionary | Qualifies (1b) | Enzymatic-core conservation | Catalytic core **82% identical** to Sir2; catalytic His310 conserved — near-identical enzyme, so site "choice" is set by targeting/cofactors, not intrinsic chemistry | Needleman-Wunsch, UniProt seqs | Direct computed provenance (see identity artifact) |

---

## GO Curation Implications (leads — require curator verification)

**Retain (well-supported):**
- **MF GO:0017136** *histone deacetylase activity, NAD-dependent* — IDA-backed. Keep as the primary MF.
- **CC GO:0000118 / Sum1–Rfm1–Hst1 (histone deacetylase complex), GO:0005634 nucleus** — supported by interaction data.
- **BP:** gene-specific negative regulation of transcription; **regulation of NAD⁺ biosynthesis** (well-documented, PMID:12972620); negative regulation of meiotic/sporulation genes (PMID:17242192, 12612074, 24710277).

**Scrutinize / likely too specific (paralog over-annotation):**
- **MF GO:0032041 (H3K14) and GO:0046969 (H3K9)** — **IBA only**. Recommend *do not assert as native experimental MF*; the direct evidence supports only the general NAD-HDAC term, and the one documented in vivo mark is **H4K5ac**. Lead: generalize to GO:0017136, or, if a residue-specific term is desired, the best-evidenced candidate is an H4K5-directed activity (still indirect). GO:0046970 (H4K16) likewise IBA — not native-supported.

**Make context-specific / non-core:**
- **BP GO:0031509 subtelomeric heterochromatin formation** (IBA) and **CC GO:0000781 telomeric region** (IEA) — recommend **remove or down-weight** for native Hst1; these are Sir2 functions. If retained, gate to the SUM1‑1 engineered context.
- **BP GO:0030466 silent mating-type heterochromatin** (IMP) — retain **only with a SUM1‑1 / gain-of-function qualifier**; it is not native targeting.

**Treat as unresolved / needs primary check:**
- **BP GO:0006974 DNA damage response** (IBA) — recommend non-core; phenotype dominated by Hst3/Hst4.
- **BP GO:0045950 negative regulation of mitotic recombination** (IMP) — flag for curator: the founding *hst1Δ* study (PMID:8810037) found **no rDNA-recombination phenotype**, so verify the exact locus/context behind the IMP annotation and whether it reflects direct control vs. secondary transcriptional silencing; recommend treating as **non-core** pending that check.

> Avoiding "protein binding": the recommended informative MF is **NAD-dependent histone/protein-lysine deacetylase activity (GO:0017136)**, not a generic binding term.

---

## Mechanistic Scope

**Direct gene-product activity:** NAD⁺-dependent deacetylation of promoter-proximal nucleosomal histones (in vivo mark: H4K5ac) at loci bound by the DNA-binding protein Sum1, to which Hst1 is tethered by Rfm1. This is a **local, sequence-directed** activity — not domain-wide heterochromatin nucleation/spreading.

**Downstream / inferred (not the immediate function):** transcriptional repression outputs (middle-sporulation genes; *BNA* NAD-biosynthesis genes; oxidative-stress genes), and any recombination or meiotic-progression phenotypes that follow from that repression. Telomeric/heterochromatic and DNA-damage "functions" are either paralog-inferred (Sir2/Hst3/Hst4) or gain-of-function (SUM1‑1) manifestations.

---

## Conflicts and Alternatives

- **Paralog confusion (central issue):** Sir2 (telomere/HM regional silencing, H4K16), Hst3/Hst4 (H3K56ac, genotoxin sensitivity). The seed's telomere/subtelomeric/DNA-damage/site-specificity claims track Sir2/Hst3/Hst4 biology, propagated to Hst1 via IBA.
- **Engineered vs native:** SUM1‑1 silencing (PMID:11316790, 11313477) is at HM loci and is a dominant gain-of-function; it should not be read as native telomere localization.
- **Organism differences:** *C. glabrata* Hst1 does *local* silencing while Sir2 does regional (PMID:26122277) — consistent with the *S. cerevisiae* division of labor, arguing against a native regional/subtelomeric role for Hst1.
- **Enzymatic promiscuity vs physiology:** Hst1's catalytic core is **82% identical to Sir2** (computed; catalytic His310 conserved), so an in-vitro Sir2-family core can deacetylate multiple acetyl-lysines. Per PMID:17242192 the divergence is in cofactor/targeting, not enzyme chemistry — hence homology (IBA) transfer of Sir2's H3K9/H3K14/H4K16 activities is plausible in vitro but does **not** establish those as the *major physiological substrate* of native Hst1 (documented in vivo mark: H4K5ac).

---

## Knowledge Gaps

1. **Native histone site-specificity.** Checked: no primary assay pinning native Hst1 to H3K9/H3K14; only general NAD-HDAC (IDA) + in vivo H4K5ac (PMID:29066473). Matters because the seed's site claim is exactly what curators must accept/reject. Resolve with: recombinant Sum1–Rfm1–Hst1 on defined acetyl-histone peptides/nucleosomes, plus locus-specific ChIP of H3K9ac/H3K14ac/H4K5ac in *hst1Δ*.
2. **Direct vs secondary recombination control.** Checked: IMP annotation exists but mechanism unclear. Matters for GO:0045950. Resolve with: recombination assays in *hst1Δ* separating transcriptional-repression loss from a direct chromatin effect (e.g., rDNA/marker recombination with target-gene rescue).
3. **Native telomere occupancy.** Checked: annotation IEA/IBA only; native Sum1 binds specific promoters, not telomeres. Resolve with: genome-wide Hst1 ChIP-seq in wild-type cells to test for any native subtelomeric enrichment.

---

## Discriminating Tests

- **Nucleosome deacetylation assay** of purified Sum1–Rfm1–Hst1 across H3K9ac/H3K14ac/H4K5ac/H4K16ac — distinguishes in-vitro promiscuity from a preferred physiological site.
- **Hst1 ChIP-seq (WT vs SUM1‑1)** — directly tests native telomeric/subtelomeric localization vs promoter-specific binding, and isolates the SUM1‑1 gain-of-function.
- **Residue-resolved ChIP of acetyl marks in *hst1Δ*** — tests which histone-site acetylation rises when Hst1 is lost (expected: H4K5ac at Sum1 targets).
- **Epistasis for recombination** (*hst1Δ* ± restored target-gene expression) — separates direct recombination control from transcriptional consequence.

---

## Curation Leads (require curator verification)

- **Reference leads (verify snippets):**
  - PMID:17242192 — "Hst1 interacts with Rfm1 and Sum1 to repress the transcription of specific middle-sporulation genes. Sir2 interacts with Sir3 and Sir4 to silence genes contained within the silent-mating-type loci and telomere chromosomal regions." → supports gene-specific (not telomeric) native role.
  - PMID:12972620 — "The NAD(+)-dependent deacetylase activity of Hst1p represses de novo NAD(+) biosynthesis genes ... suggesting a direct effect." → primary NAD-dependent, gene-specific function.
  - PMID:29066473 — "increased H4K5ac at these loci" → documented in vivo histone mark.
  - PMID:11316790 / 11313477 — SUM1‑1 gain-of-function context for HM-locus silencing.
- **Candidate GO actions:** keep GO:0017136 (MF, primary) + NAD-biosynthesis/transcription-repression BP + Sum1–Rfm1–Hst1 CC; down-weight/remove IBA site terms (GO:0032041/GO:0046969/GO:0046970), telomere/subtelomeric terms (GO:0000781/GO:0031509), and DNA-damage term (GO:0006974) as non-core; add SUM1‑1/engineered qualifier to GO:0030466; flag GO:0045950 for direct-vs-secondary verification.
- **Suggested question to curator:** Is any residue-specific MF (H3K9/H3K14) intended to reflect native physiology or Sir2-family homology? If homology-only, prefer the general NAD-HDAC term.
- **Suggested experiments:** the four Discriminating Tests above.

**Artifacts:** `HST1_GO_evidence_matrix.csv` (computed GO/evidence-code audit for P53685); `HST1_vs_SIR2_identity.txt` (computed Needleman-Wunsch identity: 82% catalytic-core identity to Sir2, His310 conserved).

**Iteration 2 update:** Added founding-paper loss-of-function evidence (PMID:8810037: *hst1Δ* has no rDNA-recombination or regional HMLα-silencing phenotype), which strengthens the refutation of the native recombination and heterochromatin sub-claims, and added a computed HST1-vs-SIR2 catalytic-core alignment supporting the "targeting-not-enzyme" basis of Hst1/Sir2 divergence.

**Iteration 3 update:** Targeted search for a primary in-vitro Hst1 histone-site assay returned none, reinforcing that H3K9/H3K14 site-specificity for native Hst1 rests on homology inference rather than direct biochemistry. Consolidated a per-term GO decision table (`HST1_GO_decision_table.csv`) with recommended actions.


## Artifacts

- [OpenScientist HST1 GO decision table](openscientist_artifacts/HST1_GO_decision_table.csv)
- [OpenScientist HST1 GO evidence matrix](openscientist_artifacts/HST1_GO_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)