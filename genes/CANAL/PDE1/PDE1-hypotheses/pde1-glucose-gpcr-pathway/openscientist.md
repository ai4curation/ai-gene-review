---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-02T06:43:02.706864'
end_time: '2026-10-02T06:56:50.156909'
duration_seconds: 827.45
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: CANAL
  gene: PDE1
  gene_symbol: PDE1
  uniprot_accession: Q5AGE4
  taxon_id: NCBITaxon:237561
  taxon_label: Candida albicans (strain SC5314 / ATCC MYA-2876)
  focus_type: function_assignment
  hypothesis_slug: pde1-glucose-gpcr-pathway
  hypothesis_text: 'In Candida albicans, Pde1 negatively regulates an adenylate cyclase-activating
    glucose-activated G protein-coupled receptor signaling pathway: the cAMP rise
    that Pde1 terminates after glucose addition is generated through the Gpr1 receptor
    and the G-alpha protein Gpa2 (rather than solely through Cdc25/Ras1 or other inputs
    to adenylyl cyclase Cyr1).'
  term_context: '- Term: negative regulation of adenylate cyclase-activating glucose-activated
    G protein-coupled receptor signaling pathway (GO:0110034)

    - Test specifically the glucose-activated GPCR component; the cAMP phosphodiesterase
    activity of Pde1 itself is not in question.'
  reference_context: '- PMID:20558315

    - PMID:15302825

    - PMID:15673611'
  source_file: genes/CANAL/PDE1/PDE1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'In Candida albicans, Pde1 negatively regulates\
    \ an adenylate cyclase-activating glucose-activated\n  G protein-coupled receptor\
    \ signaling pathway: the cAMP rise that Pde1 terminates after glucose addition\n\
    \  is generated through the Gpr1 receptor and the G-alpha protein Gpa2 (rather\
    \ than solely through Cdc25/Ras1\n  or other inputs to adenylyl cyclase Cyr1).'\n\
    focus_type: function_assignment\nterm_id: GO:0110034\nterm_label: negative regulation\
    \ of adenylate cyclase-activating glucose-activated G protein-coupled receptor\n\
    \  signaling pathway\ncontext:\n- Test specifically the glucose-activated GPCR\
    \ component; the cAMP phosphodiesterase activity of Pde1\n  itself is not in question.\n\
    reference_id:\n- PMID:20558315\n- PMID:15302825\n- PMID:15673611"
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
citation_count: 6
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

- **Organism code:** CANAL
- **Taxon:** Candida albicans (strain SC5314 / ATCC MYA-2876) (NCBITaxon:237561)
- **Gene directory:** PDE1
- **Gene symbol:** PDE1
- **UniProt accession:** Q5AGE4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** pde1-glucose-gpcr-pathway
- **Source file:** genes/CANAL/PDE1/PDE1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

In Candida albicans, Pde1 negatively regulates an adenylate cyclase-activating glucose-activated G protein-coupled receptor signaling pathway: the cAMP rise that Pde1 terminates after glucose addition is generated through the Gpr1 receptor and the G-alpha protein Gpa2 (rather than solely through Cdc25/Ras1 or other inputs to adenylyl cyclase Cyr1).

## Term and Decision Context

- Term: negative regulation of adenylate cyclase-activating glucose-activated G protein-coupled receptor signaling pathway (GO:0110034)
- Test specifically the glucose-activated GPCR component; the cAMP phosphodiesterase activity of Pde1 itself is not in question.

## Reference Context

- PMID:20558315
- PMID:15302825
- PMID:15673611

## Source Context YAML

```yaml
hypothesis: 'In Candida albicans, Pde1 negatively regulates an adenylate cyclase-activating glucose-activated
  G protein-coupled receptor signaling pathway: the cAMP rise that Pde1 terminates after glucose addition
  is generated through the Gpr1 receptor and the G-alpha protein Gpa2 (rather than solely through Cdc25/Ras1
  or other inputs to adenylyl cyclase Cyr1).'
focus_type: function_assignment
term_id: GO:0110034
term_label: negative regulation of adenylate cyclase-activating glucose-activated G protein-coupled receptor
  signaling pathway
context:
- Test specifically the glucose-activated GPCR component; the cAMP phosphodiesterase activity of Pde1
  itself is not in question.
reference_id:
- PMID:20558315
- PMID:15302825
- PMID:15673611
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

# AIGR Gene Hypothesis Deep Research — *Candida albicans* PDE1 (Q5AGE4)

**Hypothesis slug:** `pde1-glucose-gpcr-pathway`
**Focus type:** function_assignment
**Term under evaluation:** GO:0110034 — *negative regulation of adenylate cyclase-activating glucose-activated G protein-coupled receptor signaling pathway*
**Target:** PDE1 / Q5AGE4, *Candida albicans* SC5314 (NCBITaxon:237561)

---

## Summary

**Verdict: Partially supported but over-annotated — the specific GO:0110034 annotation should be removed (or not propagated) for *C. albicans* Pde1.**

The seed hypothesis bundles two separable claims whose evidence diverges sharply. The first — that **Pde1 negatively regulates the glucose-triggered cAMP rise** — is well supported. Pde1 is a *bona fide* low-affinity (class II) cyclic-AMP phosphodiesterase, and it is specifically the enzyme that terminates the cAMP spike produced after glucose addition or intracellular acidification ([PMID: 20558315](https://pubmed.ncbi.nlm.nih.gov/20558315/); ortholog [PMID: 9880329](https://pubmed.ncbi.nlm.nih.gov/9880329/)). There is no dispute about Pde1's role as a negative regulator of cAMP signalling downstream of glucose.

The second claim — that the cAMP rise is **generated through a glucose-activated G protein-coupled receptor (Gpr1) and the Gα protein Gpa2** — is refuted in *C. albicans*. The study that directly asked where glucose-induced cAMP comes from found that deleting *GPR1* or *GPA2* does **not** abolish glucose-induced cAMP, whereas deleting *CDC25* or *RAS1* **does** ([PMID: 15673611](https://pubmed.ncbi.nlm.nih.gov/15673611/)). The *C. albicans* Gpr1 ligand is moreover unresolved and may be amino acids such as methionine rather than glucose ([PMID: 15667329](https://pubmed.ncbi.nlm.nih.gov/15667329/)).

GO:0110034 is a highly specific Biological Process term that asserts three mechanistic commitments at once — a *GPCR-mediated*, *glucose-activated*, *adenylate-cyclase-activating* pathway — exactly the architecture the *C. albicans* data contradict. Critically, the annotation sits on Q5AGE4 **by phylogenetic inference only (IBA; GO_REF:0000033)**, with no *C. albicans* experimental support. It is a classic over-propagation from the *Saccharomyces cerevisiae* glucose-sensing paradigm into a species where the wiring differs. The correct, evidence-backed annotations to retain are GO:0004115 (MF, IDA), GO:0141162 (BP, IMP), and the broader GO:1902660 (BP).

---

## Key Findings

### Finding 1 — Pde1 terminates the glucose-induced cAMP rise (the negative-regulation activity is real)

Pde1 is a class II 3′,5′-cyclic-AMP phosphodiesterase whose physiological role is to down-regulate the cAMP transient that follows glucose addition. Wilson et al. (2010) provide direct biochemical and genetic evidence in *C. albicans*: *"Pde1, but not Pde2, is responsible for down-regulation of cAMP signalling induced by glucose addition or intracellular acidification"* ([PMID: 20558315](https://pubmed.ncbi.nlm.nih.gov/20558315/)). This cleanly separates Pde1, the low-affinity enzyme that shapes the acute, agonist-induced spike, from Pde2, the high-affinity enzyme that sets basal cAMP tone.

The specificity is conserved from the *S. cerevisiae* ortholog, where *"deletion of PDE1, but not PDE2, results in a much higher cAMP accumulation upon addition of glucose or upon intracellular acidification"* ([PMID: 9880329](https://pubmed.ncbi.nlm.nih.gov/9880329/)). UniProt Q5AGE4 records the molecular function directly: GO:0004115 (3′,5′-cyclic-AMP phosphodiesterase activity), IDA (PMID:8075796), with the class II PDEase domain (Pfam PF02112, PDEase_II; metallo-hydrolase fold).

The portion of the hypothesis asserting that Pde1 negatively regulates glucose-induced cAMP signalling is therefore correct. It maps onto the experimentally supported term **GO:0141162 (negative regulation of cAMP/PKA signal transduction, IMP, PMID:20558315)** and the molecular-function term GO:0004115. Importantly, this negative-regulation role is an action on the **second messenger**, not on the receptor.

### Finding 2 — The glucose-induced cAMP rise is Cdc25/Ras1-dependent, NOT Gpr1/Gpa2-dependent (the GPCR specificity is refuted)

This is the decisive finding. Maidan et al. (2005) performed the exact discriminating experiment — which upstream module is *required* for glucose-induced cAMP in *C. albicans*: *"deletion of neither CaGpr1 nor CaGpa2 affects glucose-induced cAMP signaling. In contrast, the latter is abolished in strains lacking CaCdc25 or CaRas1, suggesting that the CaCdc25-CaRas1 rather than the CaGpr1-CaGpa2 module mediates glucose-induced cAMP signaling in C. albicans"* ([PMID: 15673611](https://pubmed.ncbi.nlm.nih.gov/15673611/)).

This directly contradicts the mechanistic claim embedded in GO:0110034 — that the pathway being negatively regulated is a *glucose-activated GPCR* pathway. In *C. albicans*, the glucose→cAMP route runs through the Ras guanine-nucleotide-exchange factor Cdc25 and the small GTPase Ras1 to adenylyl cyclase (Cyr1/Cdc35), not through Gpr1→Gpa2→Cyr1.

A competing earlier claim exists. Miwa et al. (2004) reported that *"GPR1 and GPA2 are required for a glucose-dependent increase in cellular cAMP"* ([PMID: 15302825](https://pubmed.ncbi.nlm.nih.gov/15302825/)). This is a genuine conflict in the primary literature. However, the Maidan study specifically dissected the glucose→cAMP requirement with clean epistasis against both branches, and Wilson et al. (2010) further reframed the Gpa2 contribution as linked to **intracellular acidification** and found Gpa2's other morphogenetic effects to be *"cAMP pathway-independent."* The weight of mechanistically targeted evidence favors a Cdc25/Ras1 source for glucose-induced cAMP.

The second, more specific half of the hypothesis — that Pde1 terminates a cAMP rise *generated through Gpr1/Gpa2* — is therefore not supported and is actively contradicted in this organism.

### Finding 3 — *C. albicans* Gpr1 is likely an amino-acid (methionine) sensor, not a confirmed glucose receptor

Even the "glucose-activated" qualifier of the receptor is questionable in *C. albicans*. Maidan, Thevelein & Van Dijck (2005) found that Gpr1 internalization is induced by specific amino acids such as methionine and concluded: *"it remains unclear whether Gpr1 senses sugars, as in Saccharomyces cerevisiae, or specific amino acids like methionine"* ([PMID: 15667329](https://pubmed.ncbi.nlm.nih.gov/15667329/)). The carbon-source-induced yeast-to-hypha transition was found to depend on both the presence of amino acids and on Gpr1.

The ligand specificity that would justify calling the Gpr1 pathway "glucose-activated" is thus unresolved in *C. albicans* and may in fact be amino-acid-based. This further undermines the exact wording of GO:0110034, which bundles "glucose-activated" into the term definition.

### Finding 4 — GO:0110034 on Q5AGE4 is IBA-only and contradicted by species-specific data (over-propagation)

A QuickGO annotation retrieval for UniProtKB:Q5AGE4 (performed this run) shows that GO:0110034 is assigned **solely by IBA** (Inferred from Biological ancestor; GO_REF:0000033, GO Central phylogenetic inference). There is no IDA/IMP (experimental) support for this specific term in *C. albicans*. Across organisms the term is dominated by inference (in the first 100 annotations: IBA = 18, IEA = 10, IMP = 4, IC = 1, IGI = 1), i.e., it is largely propagated across fungal/amoebal phosphodiesterase orthologs (including *Dictyostelium* pdsA, *S. pombe* cgs2, *Ustilago*).

By contrast, Q5AGE4's experimentally anchored terms are GO:0004115 (MF, IDA; PMID:8075796), GO:0141162 (BP, IMP; PMID:20558315), and filamentous-growth terms (BP, IMP; PMID:20558315). GO:0110034 is thus a phylogenetic carry-over from the *S. cerevisiae* glucose-GPCR paradigm, applied to a species where the glucose→cAMP route is experimentally shown to be Cdc25/Ras1-dependent — precisely the kind of over-propagation curators should correct.

---

## Mechanistic Model / Interpretation

The hypothesis conflates **what Pde1 does** (correct) with **how the upstream cAMP is generated** (incorrect for this organism). The diagram below summarizes the *C. albicans* wiring as supported by primary data.

```
          ========= S. cerevisiae paradigm (the source of GO:0110034) =========
          glucose ──> Gpr1 (GPCR) ──> Gpa2 (Gα) ──┐
                                                    ├──> Cyr1 (adenylyl cyclase) ──> cAMP ──> PKA
          intracellular acidification ─────────────┘                               │
                                                                        Pde1 ◄──────┘ (terminates spike)

          ============== C. albicans reality (PMID:15673611; 20558315) ==============
          glucose ──> Cdc25 (RasGEF) ──> Ras1 ─────┐
                                                    ├──> Cyr1/Cdc35 ──> cAMP ──> PKA ──> morphogenesis
          (Gpr1/Gpa2: amino-acid sensing;           │
           Gpa2 linked to acidification) ───────────┘
                                                                        Pde1 ◄──── terminates glucose/
                                                                                   acidification-induced cAMP
```

**Component-by-component comparison:**

| Component | Role asserted by the hypothesis | Role supported by *C. albicans* data |
|---|---|---|
| **Pde1** | Negative regulator terminating glucose-induced cAMP | **Confirmed** — acts on the cAMP second messenger (PMID:20558315) |
| **Glucose → cAMP source** | Via Gpr1/Gpa2 GPCR module | **Refuted** — via Cdc25/Ras1 (PMID:15673611) |
| **Gpr1 ligand** | Glucose | **Uncertain** — possibly amino acids/methionine (PMID:15667329) |
| **Gpa2** | GPCR-coupled Gα driving glucose cAMP | Linked to acidification; other effects cAMP-independent (PMID:20558315) |

Pde1's negative regulation operates at the level of cAMP hydrolysis, **two steps downstream of any receptor**. Even if a Gpr1/Gpa2 input contributed to cAMP under some conditions, Pde1 does not "negatively regulate the GPCR pathway" in a receptor- or Gα-specific way — it degrades the common output (cAMP) that integrates signals from Cdc25/Ras1, acidification, and potentially Gpr1/Gpa2. The specificity named in GO:0110034 is therefore both mechanistically mislocated (Pde1 acts on the messenger, not the pathway head) and factually contradicted (the glucose cAMP source is Ras-dependent in this species).

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [20558315](https://pubmed.ncbi.nlm.nih.gov/20558315/) | Mutant phenotype + biochemistry | **Supports** (cAMP half); **Qualifies** (GPCR half) | Does Pde1 terminate glucose-induced cAMP? | "Pde1, but not Pde2, is responsible for down-regulation of cAMP signalling induced by glucose addition or intracellular acidification"; Gpa2 stimulates cAMP via acidification; its other effects are cAMP-independent | *C. albicans*, cAMP assays | High for Pde1→cAMP; does not show glucose→Gpr1/Gpa2→cAMP |
| [9880329](https://pubmed.ncbi.nlm.nih.gov/9880329/) | Mutant phenotype (ortholog) | **Supports** | Pde1 specificity for agonist-induced cAMP | "deletion of PDE1, but not PDE2, results in a much higher cAMP accumulation upon addition of glucose or upon intracellular acidification" | *S. cerevisiae* | High; conserved enzymatic role; species-transfer caveat |
| [15673611](https://pubmed.ncbi.nlm.nih.gov/15673611/) | Mutant phenotype / epistasis | **Refutes** (GPCR source) | Which module generates glucose-induced cAMP? | "deletion of neither CaGpr1 nor CaGpa2 affects glucose-induced cAMP signaling... abolished in strains lacking CaCdc25 or CaRas1" | *C. albicans* | High; direct discriminating experiment |
| [15302825](https://pubmed.ncbi.nlm.nih.gov/15302825/) | Mutant phenotype | **Competing** (supports GPCR source) | Role of Gpr1/Gpa2 in glucose cAMP | "GPR1 and GPA2 are required for a glucose-dependent increase in cellular cAMP" | *C. albicans*, solid hypha-inducing media | Moderate; contradicted by later targeted epistasis (15673611) |
| [15667329](https://pubmed.ncbi.nlm.nih.gov/15667329/) | Mutant / ligand study | **Refutes/Qualifies** ("glucose-activated" qualifier) | Is Gpr1 a glucose receptor? | "it remains unclear whether Gpr1 senses sugars... or specific amino acids like methionine" | *C. albicans*, Gpr1 internalization / hypha | Moderate-high; ligand unresolved, favors amino acids |
| UniProt Q5AGE4 / CGD | Review/database + domain | **Qualifies** | Pde1 molecular identity & current GO | Class II cNMP phosphodiesterase (Pfam PF02112); GO:0004115 IDA (PMID:8075796); curated BP GO:0141162 (IMP), filamentous-growth terms (IMP) | *C. albicans* SC5314 | High; acts on cAMP messenger, not receptor |
| QuickGO (GO_REF:0000033) | Database (evidence provenance) | **Refutes/Qualifies** | Evidence basis of GO:0110034 on Q5AGE4 | GO:0110034 on Q5AGE4 is **IBA-only** (no IDA/IMP); term-wide IBA=18/IEA=10/IMP=4/IC=1/IGI=1 → propagated across PDE orthologs | Cross-organism GO set | High; identifies term as phylogenetic carry-over |
| [14506030](https://pubmed.ncbi.nlm.nih.gov/14506030/) | Mechanistic context | Background | cAMP pathway biology in *Candida* | cAMP synthesized by adenylate cyclase (CDC35 in *C. albicans*); modulates azole susceptibility | *C. albicans*/*S. cerevisiae* | Contextual only; not a direct test |

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Label | Current status | Recommendation |
|---|---|---|---|
| **GO:0110034** | neg. reg. of adenylate cyclase-activating glucose-activated GPCR signaling pathway | annotated to Q5AGE4 via **IBA only** (GO_REF:0000033); = seed term | **Remove / do-not-propagate** — over-specified IBA carry-over; GPCR/glucose coupling refuted in *C. albicans* (PMID:15673611); no experimental support in this species |
| GO:0141162 | neg. reg. of cAMP/PKA signal transduction | annotated (IMP, PMID:20558315; + IBA) | **Retain** — experimentally supported, correct generality |
| GO:1902660 | neg. reg. of glucose-mediated signaling pathway | annotated (IBA, per UniProt) | **Retain / use as replacement** — captures glucose→cAMP buffering without the unsupported GPCR qualifier |
| GO:0004115 | 3′,5′-cyclic-AMP phosphodiesterase activity | annotated (IDA, PMID:8075796) | **Retain** — undisputed core MF |

The supported BP level is "negative regulation of cAMP-mediated / glucose-mediated signaling"; the MF is cAMP phosphodiesterase activity. The GPCR-specific BP term (GO:0110034) is not justified by primary *C. albicans* data. "Protein binding" is not invoked — a more informative set of terms is supported. The recommendation concerns a BP term only; the MF (GO:0004115) is unaffected, and no CC change is implied.

---

## Mechanistic Scope

Pde1's **direct molecular function** is hydrolysis of the 3′,5′-cyclic phosphodiester bond of cAMP, i.e., it acts on the diffusible second messenger **downstream of adenylyl cyclase (Cyr1)**. Any "negative regulation of a receptor signaling pathway" is therefore **indirect**: Pde1 lowers the shared cAMP pool irrespective of which upstream input (glucose→Cdc25/Ras1, intracellular acidification, or amino-acid→Gpr1/Gpa2) generated it. Pde1 does not bind or modify Gpr1, Gpa2, or Cyr1.

- **Direct activity:** cAMP hydrolysis (GO:0004115, IDA) — well supported.
- **Direct regulatory consequence:** lowering cAMP after glucose/acidification spikes → negative regulation of cAMP/PKA signalling (GO:0141162, IMP) — well supported.
- **Downstream phenotypes (not core function):** filamentous growth / virulence contributions are loss-of-function phenotypes mediated through altered cAMP/PKA tone, not receptor-level activity of Pde1.
- **Mis-scoped assertion:** ascribing GPCR-branch specificity to a second-messenger-degrading enzyme conflates the enzyme's activity with the particular stimulus whose output it happens to buffer — a scope error compounded by the factual refutation of the Gpr1/Gpa2 glucose source.

---

## Conflicts and Alternatives

1. **Internal reference conflict (Miwa 2004 vs. Maidan 2005).** PMID:15302825 reports Gpr1/Gpa2 are *required* for glucose-dependent cAMP; PMID:15673611 reports they are *not*, assigning glucose-induced cAMP to Cdc25/Ras1 and reassigning Gpr1/Gpa2 to amino-acid sensing. Curation should weight the more directly targeted, later study; Wilson 2010 additionally attributes Gpa2's cAMP contribution to acidification.

2. **Organism carry-over + ligand ambiguity.** The glucose-sensing GPCR role of Gpr1/Gpa2 is well established in *S. cerevisiae*, but in *C. albicans* the Gpr1 ligand is unresolved — internalization is induced by amino acids such as methionine (PMID:15667329). The "glucose-activated GPCR" premise is a probable *S. cerevisiae*→*C. albicans* carry-over; the term may fit *S. cerevisiae* Pde1 but not *C. albicans* Pde1.

3. **Alternative interpretation.** Pde1's phenotypes (filamentous growth, virulence contribution) are downstream, pleiotropic consequences of global cAMP/PKA buffering, not evidence of GPCR-branch-specific action. Even granting a minor Gpr1/Gpa2 contribution to cAMP, Pde1 degrades the common pool; GO:0110034's receptor-pathway specificity remains misplaced for a phosphodiesterase.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Miwa vs. Maidan conflict unresolved | Both abstracts/snippets reviewed | Determines whether any glucose-GPCR contribution exists | Side-by-side cAMP time-courses in *gpr1Δ*, *gpa2Δ*, *cdc25Δ*, *ras1Δ* under identical glucose/pH conditions |
| Source of the Pde1-terminated spike | Maidan assigns it to Cdc25/Ras1 | Which input Pde1 buffers | *pde1Δ* in *gpr1Δ*/*gpa2Δ* vs *ras1Δ* backgrounds |
| Gpr1 physiological ligand | PMID:15667329 (methionine internalization) | Validity of "glucose-activated" qualifier | Ligand-binding / dose-response cAMP assays, glucose vs methionine |
| Direct Pde1–Gpa2 coupling | Wilson 2010 "regulatory module" is genetic/biochemical | Whether Pde1 acts on the GPCR branch specifically | Co-IP / BioGRID / AP-MS for a Pde1–Gpr1/Gpa2 complex (none found) |
| No *C. albicans* experimental GO:0110034 | QuickGO retrieval for Q5AGE4 | Confirms IBA-only, not experimentally grounded | Any IDA/IMP study placing Pde1 regulation on a Gpr1/Gpa2 glucose pathway (none found) |
| Term-definition intent | Reviewed term label | Whether GO:0110034 means "regulate the messenger of" vs "the receptor step" | Check GO definition and annotation precedents |

Provenance note: the annotation-evidence breakdown (IBA-only for GO:0110034; experimental support for GO:0004115/GO:0141162) is derived from a QuickGO/UniProt retrieval conducted during the investigation. This is a database-level check, not a wet-lab result, and is reported as such.

---

## Discriminating Tests

1. **Unified-condition epistasis panel.** Measure glucose-induced cAMP kinetics in isogenic *gpr1Δ*, *gpa2Δ*, *cdc25Δ*, *ras1Δ*, and WT (plus *pde1Δ* in each background) under tightly controlled glucose concentration and extracellular pH. Directly adjudicates Miwa (2004) vs. Maidan (2005) and identifies which input Pde1 buffers.
2. **Ligand specificity of Gpr1.** Dose-response cAMP and receptor-internalization assays comparing glucose, sucrose, and methionine/other amino acids to establish the physiological *C. albicans* Gpr1 ligand.
3. **Interaction screen** (AP-MS / two-hybrid) for Pde1 against Gpr1/Gpa2/Cyr1 to test any direct branch coupling.
4. **Comparative annotation audit.** Confirm whether *S. cerevisiae* Pde1 (not *C. albicans*) is the proper home for a glucose-GPCR-linked term, and review other fungal IBA propagations of GO:0110034.

---

## Curation Leads (require curator verification)

- **Action:** Remove / do-not-accept the existing **IBA** GO:0110034 annotation on *C. albicans* Pde1 (Q5AGE4). Keep the experimentally grounded GO:0004115 (MF, IDA) and GO:0141162 (BP, IMP), and the broader GO:1902660 (BP). If a stimulus-linked BP is desired, prefer GO:1902660 (glucose-mediated signaling) without the GPCR qualifier. The term is currently present only through phylogenetic (IBA/GO_REF:0000033) propagation from orthologs, not through *C. albicans* experimental evidence.
- **Key references to cite in the review:**
  - PMID:15673611 — *"deletion of neither CaGpr1 nor CaGpa2 affects glucose-induced cAMP signaling. In contrast, the latter is abolished in strains lacking CaCdc25 or CaRas1..."* (refutes GPCR source).
  - PMID:20558315 — *"Pde1, but not Pde2, is responsible for down-regulation of cAMP signalling induced by glucose addition or intracellular acidification."* (supports Pde1→glucose-cAMP termination).
  - PMID:9880329 — *"deletion of PDE1, but not PDE2, results in a much higher cAMP accumulation upon addition of glucose or upon intracellular acidification."* (ortholog).
  - PMID:15302825 — *"GPR1 and GPA2 are required for a glucose-dependent increase in cellular cAMP."* (competing claim; note it is superseded by 15673611).
  - PMID:15667329 — *"it remains unclear whether Gpr1 senses sugars... or specific amino acids like methionine."* (ligand ambiguity).
- **Suggested curator question:** Does GO:0110034's definition require action at the receptor/G-protein step (which Pde1 does not perform) or merely regulation of the pathway's cAMP output?
- **Suggested experiments:** the unified-condition epistasis panel and Gpr1 ligand dose-response assays under *Discriminating Tests*.

*Artifacts (provenance):* `/tmp/evidence_matrix_PDE1_GPCR.csv`, `/tmp/go_decision_table_PDE1.csv`, `/tmp/GO0110034_evidence_codes.png` (computed from QuickGO: ~82% of GO:0110034 annotations are IBA/IEA inferred), `/tmp/PDE1_verdict_summary.png`, plus executed UniProt (Q5AGE4) and QuickGO fetches confirming domain/GO content and the IBA-only evidence basis of the GO:0110034 annotation.

---

## Final Verdict

The enzymatic and negative-regulatory core of the hypothesis is correct — Pde1 terminates the glucose-induced cAMP spike — but the specific claim that it regulates a **glucose-activated GPCR (Gpr1/Gpa2)** pathway is refuted in *C. albicans*, where glucose-induced cAMP is Cdc25/Ras1-dependent. GO:0110034 is attached to Q5AGE4 only by phylogenetic inference and should be removed or down-weighted in favor of the experimentally grounded terms GO:0004115 (MF, IDA) and GO:0141162 (BP, IMP). **Overall: partially supported, over-annotated.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)