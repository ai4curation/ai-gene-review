---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T17:54:40.590907'
end_time: '2026-10-09T18:21:16.745996'
duration_seconds: 1596.16
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: XENLA
  gene: sox10
  gene_symbol: sox10
  uniprot_accession: Q8AXX8
  taxon_id: NCBITaxon:8355
  taxon_label: Xenopus laevis
  focus_type: free_text
  hypothesis_slug: nc-enhancer-inputs-scatac
  hypothesis_text: 'The neural crest specifiers sox10, snai2 and foxd3 receive direct
    regulatory input from the neural plate border factors Pax3/Pax7, Zic and TFAP2
    at neural crest-specific enhancers. Test this with one analysis: using the public
    chick neural crest ATAC-seq / single-cell ATAC data and enhancer annotations of
    Williams et al. 2019 (PMID:31639368), check whether crest-accessible enhancers
    linked to Sox10, Snai2 and FoxD3 are enriched for, or contain, PAX, ZIC and TFAP2
    binding motifs, compared to background accessible regions. Report the result even
    if inconclusive.'
  term_context: No specific term context supplied.
  reference_context: '- PMID:31639368

    - PMID:31619682'
  source_file: genes/XENLA/sox10/sox10-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'The neural crest specifiers sox10, snai2 and\
    \ foxd3 receive direct regulatory input from the\n  neural plate border factors\
    \ Pax3/Pax7, Zic and TFAP2 at neural crest-specific enhancers. Test this with\n\
    \  one analysis: using the public chick neural crest ATAC-seq / single-cell ATAC\
    \ data and enhancer annotations\n  of Williams et al. 2019 (PMID:31639368), check\
    \ whether crest-accessible enhancers linked to Sox10, Snai2\n  and FoxD3 are enriched\
    \ for, or contain, PAX, ZIC and TFAP2 binding motifs, compared to background accessible\n\
    \  regions. Report the result even if inconclusive.'\nfocus_type: free_text\n\
    context: []\nreference_id:\n- PMID:31639368\n- PMID:31619682"
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

- **Organism code:** XENLA
- **Taxon:** Xenopus laevis (NCBITaxon:8355)
- **Gene directory:** sox10
- **Gene symbol:** sox10
- **UniProt accession:** Q8AXX8

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** nc-enhancer-inputs-scatac
- **Source file:** genes/XENLA/sox10/sox10-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The neural crest specifiers sox10, snai2 and foxd3 receive direct regulatory input from the neural plate border factors Pax3/Pax7, Zic and TFAP2 at neural crest-specific enhancers. Test this with one analysis: using the public chick neural crest ATAC-seq / single-cell ATAC data and enhancer annotations of Williams et al. 2019 (PMID:31639368), check whether crest-accessible enhancers linked to Sox10, Snai2 and FoxD3 are enriched for, or contain, PAX, ZIC and TFAP2 binding motifs, compared to background accessible regions. Report the result even if inconclusive.

## Term and Decision Context

No specific term context supplied.

## Reference Context

- PMID:31639368
- PMID:31619682

## Source Context YAML

```yaml
hypothesis: 'The neural crest specifiers sox10, snai2 and foxd3 receive direct regulatory input from the
  neural plate border factors Pax3/Pax7, Zic and TFAP2 at neural crest-specific enhancers. Test this with
  one analysis: using the public chick neural crest ATAC-seq / single-cell ATAC data and enhancer annotations
  of Williams et al. 2019 (PMID:31639368), check whether crest-accessible enhancers linked to Sox10, Snai2
  and FoxD3 are enriched for, or contain, PAX, ZIC and TFAP2 binding motifs, compared to background accessible
  regions. Report the result even if inconclusive.'
focus_type: free_text
context: []
reference_id:
- PMID:31639368
- PMID:31619682
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

# AIGR Deep Research Report — sox10 (XENLA, Q8AXX8)

**Hypothesis slug:** nc-enhancer-inputs-scatac
**Seed hypothesis:** The neural crest specifiers sox10, snai2 and foxd3 receive direct regulatory input from the neural plate border (NPB) factors Pax3/Pax7, Zic and TFAP2 at neural crest–specific enhancers. Test by checking whether crest-accessible enhancers linked to Sox10, Snai2 and FoxD3 in the Williams et al. 2019 chick NC ATAC/scATAC dataset (PMID:31639368) are enriched for PAX, ZIC and TFAP2 motifs vs. background.

---

## Executive Judgment

**Verdict: Partially supported — supported for snai2 and foxd3 (the hypothesis holds strongly for these two specifiers, including in *Xenopus*); qualified/indirect for the actual review gene sox10.**

Using the full text of the hypothesis's own dataset (Williams et al. 2019, PMC6838682), organism-matched *Xenopus* functional genomics (Plouhinec et al. 2014), and the primary enhancer-dissection literature, the picture is:

- **Organism-matched key result (Xenopus, Plouhinec 2014, PMID:24360906):** Pax3+Zic1 are *direct* upstream regulators of **Snail1/2 (snai2), Foxd3, Twist1 and Tfap2b** — but **Sox10 is NOT among the identified direct Pax3/Zic1 targets**. This both supports the hypothesis for snai2/foxd3 and narrows it for sox10 in the review's own organism.

And at the motif/enhancer level:

- **TFAP2 — supported.** TFAP2 motifs are a pivotal, enriched component of the canonical NC cis-regulatory signature at NC-specific enhancers (which include the Sox10 super-enhancer and Snai2/FoxD3-class elements).
- **PAX — supported as a motif class, but ambiguous as to Pax3/Pax7.** A PAX motif (reported as "Pax3") is among the motifs controlling the canonical-NC enhancer cluster (k-Cl3), but the de-novo PAX motif enriched in the broader program maps to **Pax2** (a border/neural PAX), and PAX-domain motifs cannot cleanly distinguish Pax3/Pax7 from Pax2.
- **ZIC — qualified/weak.** The Zic motif appears, but Williams 2019 assigns it to the subgroup **shared with the neural-lineage cluster (k-Cl1)**, i.e. it is not restricted to or dominant at the canonical NC specifier enhancers.
- **For Sox10 *specifically* (the target gene), the "direct input" claim is not supported.** The experimentally validated Sox10 NC enhancer (Sox10E2) is directly bound by **Sox9, Ets1 and cMyb** (Betancur 2010), not by Pax3/7, Zic or TFAP2. NPB factors feed into Sox10 **indirectly**, chiefly via Sox9/FoxD3.
- **The strongest *direct* NPB→specifier enhancer evidence is for FoxD3, not Sox10:** Pax7 binds FoxD3 NC1 and Zic1 directly binds FoxD3 NC2 (Simões-Costa 2012).

**Most important caveat for curation:** this hypothesis is about *upstream regulatory input to* sox10, not about the molecular function of the Sox10 gene product. It is GRN context and does **not** by itself justify adding or changing a molecular-function or cellular-component GO term on sox10.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:31639368 (Williams 2019; the hypothesis dataset) | De novo motif enrichment of scATAC enhancer clusters; Capture-C; CRISPR KO | Supports (TFAP2, PAX) / Qualifies (ZIC) | Are Sox10/Snai2/FoxD3-linked crest enhancers enriched for PAX/ZIC/TFAP2 motifs vs background? | Canonical-NC enhancer cluster (k-Cl3) controlled by **Sox9, Pax3, Sox8** motifs; canonical-NC signature = "pivotal role of **TFAP2s, Sox10, and Fox factors**"; **Zic** motif listed in the subgroup **shared with the neural cluster k-Cl1** (ATF, Maf, RAR, Zic, Zfp, GATA). Enriched de-novo PAX in the neural program = **Pax2**. | Chick premigratory/migrating cranial NC, in vivo | PAX & TFAP2 present/enriched; PAX motif cannot separate Pax3/7 from Pax2; ZIC not NC-specific |
| PMID:20139305 (Betancur 2010, Sox10E2) | ChIP + DNA pull-down + gel-shift + binding-site mutagenesis | Qualifies / competes | Does Sox10's validated NC enhancer receive *direct* input from Pax3/7, Zic, TFAP2? | **Sox10E2 direct inputs = Sox9, Ets1, cMyb**; site mutation / regulator knockdown abolishes activity. Pax3/Zic/TFAP2 are **not** the direct Sox10E2 inputs. | Chick cranial NC, in vivo | High; NPB factors act on Sox10 indirectly (via Sox9) |
| PMID:23284303 (Simões-Costa 2012, FoxD3 NC1/NC2) | ChIP + mutagenesis + morpholino KD | Supports (PAX, ZIC) | Do border factors Pax7/Zic1 directly bind NC-specifier enhancers? | FoxD3 **NC1 bound by Pax7 + Msx1/2 + Ets1**; **NC2 directly bound by Zic1**. | Chick cranial & vagal/trunk NC, in vivo | Direct NPB input confirmed, **but for FoxD3, not Sox10** |
| PMID:31619682 (Hockman 2019, lamprey) | ATAC-seq + cross-species enhancer reporter | Supports (conservation) | Are SoxE/Tfap2 NC enhancers ancient/conserved? | Validated enhancers of **Tfap2B** and **SoxE1** (Sox10 ortholog); SoxE1 enhancer activity deeply conserved to jawed vertebrates. | Sea lamprey vs jawed vertebrates | Supports conserved SoxE/TFAP2 cis-regulation; says nothing about direct Pax/Zic input |
| **PMID:24360906 (Plouhinec 2014; organism-matched)** | GOF + translation-blockade direct-target screen; transcriptome of neural border | **Supports (snai2, foxd3) / narrows (sox10)** | Do Pax3+Zic1 directly activate the NC specifiers in *Xenopus*? | "Pax3 and Zic1 are direct upstream regulators of neural crest specifiers **Snail1/2, Foxd3, Twist1, and Tfap2b**"; **Sox10 not identified as a direct target**; Pax3 autoregulates. | ***Xenopus laevis*** neural border, in vivo | High; same organism as the review gene. Tfap2b is itself a Pax3/Zic1 target (feedforward) |
| PMID:12885557 (Honoré 2003) | Morpholino loss-of-function | Context | Where does Sox10 sit in the Xenopus NC hierarchy? | Sox10 is expressed from earliest NC specification; its knockdown reduces **Slug (snai2) and FoxD3** — Sox10 acts early and feeds forward onto other specifiers. | *Xenopus laevis*, in vivo | Shows Sox10 is an early specifier/feedforward node, not a terminal Pax3/Zic1 output |

*(Provenance: evidence matrix also saved as `/tmp/evidence_matrix.csv`; motif passages extracted programmatically from EuropePMC full text PMC6838682.)*

### Per-gene verdict (seed hypothesis = direct NPB-factor input at NC enhancers)

| Gene | NPB input (Pax3/7, Zic, TFAP2) | Verdict | Key evidence |
|---|---|---|---|
| **sox10 (TARGET)** | Pax3/7: indirect (via Sox9); Zic: possible only at earliest neural-type enh-99; TFAP2: feedforward input | **Narrowed — not direct** | Sox10E2 direct inputs = Sox9/Ets1/cMyb (PMID:20139305); Sox10 absent from Xenopus Pax3/Zic1 direct targets (PMID:24360906); Sox10 super-enhancer dominated by canonical Sox9/TFAP2/Fox code, earliest element enh-99 in neural k-Cl1 cluster (PMID:31639368) |
| snai2 / Snail1-2 | Pax3+Zic1 direct (Xenopus) | **Supported** | PMID:24360906; NC-specific Snai2 enhancers PMID:31639368 |
| foxd3 | Pax7 direct (NC1), Zic1 direct (NC2) | **Supported** | PMID:23284303 (ChIP+mutagenesis); PMID:24360906 |
| tfap2b | Is *itself* a direct Pax3/Zic1 target | Supported but **feedforward** | PMID:24360906 + PMID:31639368 (TFAP2 also an enriched enhancer-input motif) |

### GO decision table (review gene sox10, Q8AXX8) — leads, require curator verification

| GO item | Current status | Recommended action | Rationale |
|---|---|---|---|
| sox10 "regulated by Pax3/Zic/TFAP2" | none proposed | **No new term** | Non-core: describes *regulators*, not Sox10 gene-product function |
| GO:0003700 / GO:0000978 / GO:0000981 DNA-binding TF activity (MF) | existing ISS/IBA/IEA | **Retain** | Core Sox10 function; unaffected by hypothesis |
| GO:0014029 neural crest formation (BP) | existing IMP (PMID:12812785) | **Retain** | Sox10 role; supported by Xenopus LOF (PMID:12885557) |
| GO:0001755 NC cell migration (BP) | existing IBA/IEA | **Retain** | Core Sox10 role |
| GO:0005634 nucleus (CC) | existing | **Retain** | Site of Sox10 TF action |

*(Provenance: `/tmp/per_gene_verdict.csv`, `/tmp/go_decision_table.csv`; Sox10 super-enhancer composition extracted from PMC6838682: constituent enhancers mostly k-Cl3 canonical-NC, earliest enh-99 in neural k-Cl1; cranial 10E2 interacts with the Sox10 promoter.)*

---

## GO Curation Implications (leads — require curator verification)

**Grounding against the actual XENLA sox10 (Q8AXX8) annotation set (QuickGO, 32 annotations):** existing terms describe the gene product's own activity and the processes it drives — MF GO:0000978/GO:0000981/GO:0003700 (RNA Pol II cis-regulatory DNA-binding TF activity), GO:0003677 (DNA binding), GO:0019899 (enzyme binding, IPI PMID:16256735); BP GO:0014029 (neural crest formation, IMP PMID:12812785), GO:0001755 (NC cell migration), GO:0030318 (melanocyte differentiation, IMP), GO:0007422 (PNS development), GO:0045893/GO:0000122 (pos/neg regulation of transcription); CC GO:0005634 (nucleus), GO:0005737 (cytoplasm). **None encodes "regulated by Pax3/Zic/TFAP2," and none should** — GO annotates the gene product's function, not the identity of its upstream transcriptional regulators.

1. **Do not convert this hypothesis into a new MF/CC/BP annotation on sox10.** It concerns *who regulates sox10*, which is a property of the regulators (Pax3/Pax7/Zic1/Tfap2a/b), not of the Sox10 gene product. The existing sox10 MF (DNA-binding TF activity) and BP (neural crest formation/migration) terms already capture its role and should be **retained** as-is; this hypothesis neither adds nor subtracts from them.
2. **Treat the regulatory-input statement as non-core / contextual** for the sox10 review. If it is to be captured at all, it belongs as a BP "regulation of" annotation **on the upstream factors** (e.g., Pax7/Zic1 → *positive regulation of transcription; neural crest cell fate commitment*), with sox10 as the regulated target — not as a function of sox10.
3. **If any directional cis-regulatory statement about sox10 is curated, anchor it to Sox9/Ets1/cMyb (Sox10E2; PMID:20139305), not to Pax3/7/Zic/TFAP2.** The latter are indirect for sox10.
4. Avoid "protein binding" as an endpoint; the informative relationships here are specific TF→enhancer regulatory inputs, which are better captured as BP regulation terms on the regulators.

---

## Mechanistic Scope

- **Immediate molecular event tested:** sequence-specific TF occupancy of NC-specific enhancers (PAX/ZIC/TFAP2 motif usage) that activate NC-specifier transcription.
- **Direct vs downstream:**
  - *Direct on FoxD3:* Pax7 (NC1), Zic1 (NC2) — validated binding.
  - *Direct on Sox10:* Sox9, Ets1, cMyb (Sox10E2) — PAX/ZIC/TFAP2 are **not** the direct Sox10 enhancer inputs.
  - *Direct on Snai2 (snai2/Slug):* Pax3+Zic1 are direct upstream activators in Xenopus (Plouhinec 2014, translation-blockade direct-target assay); Williams 2019 also identifies NC-specific accessible enhancers near Snai2. Hypothesis supported for snai2.
  - *Downstream / pleiotropic (not this annotation):* craniofacial skeleton, PNS, melanocyte and enteric phenotypes are developmental outcomes of sox10, not the regulatory-input event.

---

## Conflicts and Alternatives

- **Sox9 vs the NPB factors.** The dominant direct input to the Sox10 enhancer is Sox9 (a SoxE paralog), which itself integrates Pax3/Zic signals. This is the main interpretation that *competes* with the literal seed hypothesis for sox10: Pax3/7/Zic act **through** Sox9/FoxD3 rather than directly on Sox10.
- **PAX motif identity.** De-novo PAX motifs cannot distinguish Pax3/Pax7 from Pax2; Williams 2019 explicitly enriches **Pax2** in the neural program. A motif-only enrichment therefore cannot confirm *Pax3/Pax7* input specifically.
- **ZIC placement.** Zic co-localizes with neural/shared (k-Cl1) elements, so a naïve "ZIC enriched at NC enhancers" claim risks capturing a neuroepithelial rather than a bona-fide NC signal.
- **Feedforward/autoregulation.** The canonical NC code is dominated by Sox10/TFAP2/Fox feedforward loops; much "enhancer input" is NC-specifier self-reinforcement, not NPB input.
- **Organism-matched direct-target data reinforce the narrowing.** In *Xenopus* (Plouhinec 2014, PMID:24360906), the Pax3/Zic1 *direct* targets are Snail1/2, Foxd3, Twist1 and Tfap2b — **Sox10 is absent from the direct-target list**. So in the review's own organism, sox10 is not a demonstrated direct Pax3/Zic1 output, while snai2 and foxd3 are. This is concordant, not conflicting, across chick and frog.
- **TFAP2 is both input and output.** Tfap2b is a *direct Pax3/Zic1 target* (Plouhinec 2014) yet TFAP2 motifs are *enriched inputs* at canonical NC enhancers (Williams 2019) — i.e. TFAP2 sits in a feedforward loop. A "TFAP2 provides input" statement is true but must not be read as TFAP2 being upstream-most.
- **Hierarchy caveat for Sox10.** Honoré 2003 (PMID:12885557) shows Xenopus Sox10 knockdown reduces Slug/FoxD3, so Sox10 is an early specifier that feeds forward onto the other two "specifiers" in the hypothesis — they are partly its *downstream* targets, not co-equal parallel outputs of the border code.

---

## Knowledge Gaps

1. **Direct Pax3/Pax7 or Zic binding at a *Sox10* enhancer in any species.** Checked Betancur 2010 (Sox10E2) and Williams 2019 — not demonstrated; Sox10E2 inputs are Sox9/Ets1/cMyb. Resolving this needs ChIP/footprinting + site-mutagenesis at Sox10 CREs showing PAX/ZIC dependence.
2. **Whether the enriched PAX motif at canonical-NC enhancers is Pax3/7 vs Pax2.** Motif ambiguity; resolve with factor-specific ChIP-seq/CUT&RUN footprints.
3. **Snai2 enhancer gene-specific validation** in the chick dataset (direct Pax3/Zic/TFAP2 occupancy at Snai2 CREs). Checked Williams 2019: NC-specific Snai2 enhancers identified, but per-site TF binding not individually dissected in the cited refs.
4. **X. laevis–specific cis-regulation of sox10.** None of the supplied references test Xenopus sox10 enhancers directly.

---

## Discriminating Tests

1. **Factor-specific CUT&RUN/ChIP-seq for Pax3, Pax7, Zic1, Tfap2a** in premigratory NC, intersected with the Sox10/Snai2/FoxD3 enhancer coordinates — distinguishes true Pax3/7 occupancy from Pax2 and places Zic at NC vs neural elements.
2. **Enhancer reporter + binding-site mutagenesis** of Sox10 CREs (Sox10E2 and the Sox10 super-enhancer sub-elements) for PAX/ZIC/TFAP2 sites — tests *direct* dependence vs Sox9-mediated indirect input.
3. **Epistasis / perturbation:** Pax3/Zic1 knockdown with rescue by Sox9 — tests whether Pax3/Zic act on Sox10 only through Sox9.
4. **Re-run the motif-enrichment on Williams 2019 target-gene-assigned enhancer sets** (Capture-C–linked to Sox10, Snai2, FoxD3) specifically, reporting PAX/ZIC/TFAP2 enrichment vs the 99,583-peak background used in the paper — the exact analysis the seed proposes, which the full-text summary indicates would yield strong TFAP2/PAX and weak/neural ZIC signals.

---

## Curation Leads (require curator verification)

- **Candidate references to attach to the sox10 GRN context (not as sox10 MF/CC):**
  - PMID:20139305 — snippet to verify: *"Deep characterization of Sox10E2 reveals Sox9, Ets1, and cMyb as direct inputs mediating enhancer activity."* Use to document that sox10's direct enhancer inputs are Sox9/Ets1/cMyb.
  - PMID:23284303 — snippets: *"Pax7 and Msx1/2 cooperate with the neural crest specifier gene, Ets1, to bind to the cranial NC1 regulatory element"* and *"the neural plate border gene, Zic1, which directly binds to the NC2 enhancer."* Use on FoxD3, not sox10.
  - PMID:31639368 — motif/combinatorial code (TFAP2s/Sox10/Fox canonical signature; Zic shared with neural cluster).
  - PMID:31619682 — conserved SoxE1/Tfap2B NC enhancers.
  - **PMID:24360906 (organism-matched, Xenopus)** — snippet to verify: *"the neural border specifiers Pax3 and Zic1 are direct upstream regulators of neural crest specifiers Snail1/2, Foxd3, Twist1, and Tfap2b."* Use to support the hypothesis for **snai2 and foxd3** and to document that **sox10 is not a listed direct Pax3/Zic1 target**.
  - PMID:12885557 (Honoré 2003) — Xenopus Sox10 is required early and its loss reduces Slug/FoxD3 (hierarchy context).
- **Candidate action:** Record the seed hypothesis as **contextual/non-core** for the sox10 review. Do **not** add an MF or CC term from it. Any directional regulation term belongs on the regulators (Pax3/Pax7/Zic1/Tfap2a → regulation of sox10), as a lead.
- **Suggested curator question:** Is the intent to annotate sox10's *function* or to document its *upstream regulators*? If the former, this hypothesis is out of scope; if the latter, annotate the regulators and keep sox10 as the target.
- **Suggested experiment (if local bioinformatics is to adjudicate):** reproduce the Williams 2019 motif enrichment restricted to Capture-C-linked Sox10/Snai2/FoxD3 enhancers vs the paper's background peak set.

---

## Notes on Reproducibility / Access

- Primary motif-enrichment numbers were read from the Williams 2019 full text (EuropePMC PMC6838682); the raw scATAC BED/enhancer-coordinate files were **not** re-processed here (dataset not provided locally, and the environment's code sandbox has no outbound large-file download). This is stated plainly rather than fabricated. The qualitative enrichment pattern (TFAP2/PAX strong at canonical NC enhancers; ZIC neural/shared; Sox9/Ets at Sox10) is taken directly from the authors' reported de-novo motif analysis and the enhancer-dissection papers.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)