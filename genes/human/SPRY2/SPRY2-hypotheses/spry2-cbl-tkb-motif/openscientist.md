---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T06:22:51.415244'
end_time: '2026-10-01T06:37:10.213770'
duration_seconds: 858.8
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SPRY2
  gene_symbol: SPRY2
  uniprot_accession: O43597
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: spry2-cbl-tkb-motif
  hypothesis_text: 'Human SPRY2 (O43597) inhibits the E3 ligase CBL because its N-terminal
    phosphotyrosine Tyr55 lies in a canonical CBL TKB-domain binding motif (e.g. N/D-x-pY-[ST]-x-x-P
    or the related R/N-x-pY-x-x-[ST] class), conserved across vertebrate SPRY2 orthologs,
    whereas SPRY4 (which does not block EGFR downregulation) lacks an equivalent motif.
    Test this with one analysis: align SPRY1, SPRY2 and SPRY4 orthologs across vertebrates
    around the conserved N-terminal tyrosine and score each paralog against the CBL
    TKB binding consensus.'
  term_context: '- Term: ubiquitin ligase inhibitor activity (GO:1990948)

    - SPRY2 also binds CIN85 via proline-arginine motifs; SPRY4 lacks these and does
    not block EGFR downregulation (PMID:15962011).'
  reference_context: '- PMID:18070883'
  source_file: genes/human/SPRY2/SPRY2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human SPRY2 (O43597) inhibits the E3 ligase CBL\
    \ because its N-terminal phosphotyrosine Tyr55\n  lies in a canonical CBL TKB-domain\
    \ binding motif (e.g. N/D-x-pY-[ST]-x-x-P or the related R/N-x-pY-x-x-[ST]\n \
    \ class), conserved across vertebrate SPRY2 orthologs, whereas SPRY4 (which does\
    \ not block EGFR downregulation)\n  lacks an equivalent motif. Test this with\
    \ one analysis: align SPRY1, SPRY2 and SPRY4 orthologs across\n  vertebrates around\
    \ the conserved N-terminal tyrosine and score each paralog against the CBL TKB\
    \ binding\n  consensus.'\nfocus_type: free_text\nterm_id: GO:1990948\nterm_label:\
    \ ubiquitin ligase inhibitor activity\ncontext:\n- SPRY2 also binds CIN85 via\
    \ proline-arginine motifs; SPRY4 lacks these and does not block EGFR downregulation\n\
    \  (PMID:15962011).\nreference_id:\n- PMID:18070883"
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
citation_count: 7
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** SPRY2
- **Gene symbol:** SPRY2
- **UniProt accession:** O43597

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** spry2-cbl-tkb-motif
- **Source file:** genes/human/SPRY2/SPRY2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human SPRY2 (O43597) inhibits the E3 ligase CBL because its N-terminal phosphotyrosine Tyr55 lies in a canonical CBL TKB-domain binding motif (e.g. N/D-x-pY-[ST]-x-x-P or the related R/N-x-pY-x-x-[ST] class), conserved across vertebrate SPRY2 orthologs, whereas SPRY4 (which does not block EGFR downregulation) lacks an equivalent motif. Test this with one analysis: align SPRY1, SPRY2 and SPRY4 orthologs across vertebrates around the conserved N-terminal tyrosine and score each paralog against the CBL TKB binding consensus.

## Term and Decision Context

- Term: ubiquitin ligase inhibitor activity (GO:1990948)
- SPRY2 also binds CIN85 via proline-arginine motifs; SPRY4 lacks these and does not block EGFR downregulation (PMID:15962011).

## Reference Context

- PMID:18070883

## Source Context YAML

```yaml
hypothesis: 'Human SPRY2 (O43597) inhibits the E3 ligase CBL because its N-terminal phosphotyrosine Tyr55
  lies in a canonical CBL TKB-domain binding motif (e.g. N/D-x-pY-[ST]-x-x-P or the related R/N-x-pY-x-x-[ST]
  class), conserved across vertebrate SPRY2 orthologs, whereas SPRY4 (which does not block EGFR downregulation)
  lacks an equivalent motif. Test this with one analysis: align SPRY1, SPRY2 and SPRY4 orthologs across
  vertebrates around the conserved N-terminal tyrosine and score each paralog against the CBL TKB binding
  consensus.'
focus_type: free_text
term_id: GO:1990948
term_label: ubiquitin ligase inhibitor activity
context:
- SPRY2 also binds CIN85 via proline-arginine motifs; SPRY4 lacks these and does not block EGFR downregulation
  (PMID:15962011).
reference_id:
- PMID:18070883
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

# SPRY2 Tyr55 as a c-Cbl TKB-Domain Binding Motif: Hypothesis Evaluation for GO Curation

**Target gene:** Human SPRY2 (UniProt O43597) · **Term in focus:** GO:1990948 *ubiquitin ligase inhibitor activity* (MF)
**Hypothesis slug:** spry2-cbl-tkb-motif · **Focus type:** free_text / function-assignment

---

## Executive Judgment

**Verdict: Partially supported.**

The seed hypothesis has two logically separable claims, and the evidence splits them cleanly:

1. **The structural/mechanistic premise is correct and well supported.** SPRY2 Tyr55 does lie within a canonical c-Cbl TKB-domain phosphopeptide binding motif. Human/mouse SPRY2 residues 53–59 (**N-E-Y55-T-E-G-P**) score 4/4 against the established c-Cbl TKB consensus **(N/D)-x-pY-(S/T)-x-x-P**, the motif is perfectly conserved across the vertebrate SPRY2 orthologs examined, and the phospho-Tyr55–dependent interaction with the c-Cbl SH2-like/TKB domain is experimentally established by direct mutagenesis ([PMID:12815057](https://pubmed.ncbi.nlm.nih.gov/12815057/), [PMID:12593795](https://pubmed.ncbi.nlm.nih.gov/12593795/), [PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/)). This molecular activity — sequestering c-Cbl to block EGFR ubiquitination/downregulation — is precisely what GO:1990948 *ubiquitin ligase inhibitor activity* describes. This term is **not currently annotated to SPRY2**, and it would be more informative than the generic GO:0005515 *protein binding* presently supported by the same papers.

2. **The hypothesis's *discriminating* claim is over-stated and partly incorrect.** The hypothesis asserts the TKB motif is what separates SPRY2 (blocks EGFR downregulation) from SPRY4 (does not). This is not supported. The motif is **not SPRY2-specific**: SPRY1 carries an *identical* N-E-Y-T-E-G-P window (4/4), and SPRY4 does **not** "lack an equivalent motif" — it retains a degenerate 3/4 near-match (V-E-N-D-Y-I-D-N-P), keeping the D@−2, the pTyr, and the P@+4, and losing only the +1 Ser/Thr (an Ile instead). The documented molecular explanation for the SPRY2-vs-SPRY4 functional difference is the absence of **CIN85-binding proline-arginine (SH3) motifs** in SPRY4, not absence of the Cbl TKB motif ([PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/)).

**Net curation consequence:** The *function assignment* (SPRY2 directly inhibits the Cbl E3 ligase via a pTyr55 TKB motif → GO:1990948) is justified and actionable as a curation lead. The *evolutionary discriminator argument* offered as the supporting rationale is flawed and should not be the stated basis for the annotation. A curator can and should add GO:1990948 on the strength of the direct mutagenesis and interaction data — but must not reproduce the "SPRY4 lacks the motif" framing, which the sequence evidence refutes.

Most important caveat: all mechanistic support derives from a small cluster of EGFR-pathway studies in mammalian cell lines (largely overexpression contexts). The motif-scoring is a sequence/consensus match, not a solved SPRY2:Cbl co-structure.

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence & limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | [PMID:12815057](https://pubmed.ncbi.nlm.nih.gov/12815057/) | Direct assay (mutagenesis) | **Supports** | pTyr55 is required for c-Cbl TKB binding and EGFR retention | Y55F mutant loses enhanced c-Cbl binding and fails to retain EGF receptors at the cell surface; a conserved motif + Tyr55 phosphorylation drives the interaction with the SH2-like (TKB) domain of c-Cbl | Human SPRY2, mammalian cells | High for the interaction; overexpression context |
| 2 | [PMID:12593795](https://pubmed.ncbi.nlm.nih.gov/12593795/) | Interaction / mechanism | **Supports** | Conserved N-terminal pTyr recruits Cbl SH2 | Sprouty2 phosphorylation at a conserved tyrosine recruits the SH2 domain of c-Cbl, sequestering active c-Cbl and impeding EGFR ubiquitination | Mammalian EGFR signaling | High; consistent with #1 |
| 3 | [PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/) | Interaction / comparative | **Supports MF; Refutes discriminator** | What distinguishes SPRY2 from SPRY4 | SPRY2–Cbl–CIN85 ternary complex inhibits EGFR downregulation; SPRY4 **lacks CIN85-binding proline-arginine sites** (not the Cbl TKB motif) and therefore does not inhibit EGFR downregulation | Human; EGFR system | High; directly names the true discriminator |
| 4 | Sequence analysis (this work; O43597 + orthologs) | Structural/evolutionary (computational) | **Supports premise; Refutes specificity** | Does Y55 match the TKB consensus and is it SPRY2-unique? | SPRY2 = 4/4 (NEYTEGP); SPRY1 = 4/4 (identical); SPRY4 = 3/4 (NDYIDNP, loses only +1 hydroxyl). Motif conserved across 7 SPRY2 vertebrate orthologs | In silico consensus scoring | Medium-high; consensus match, not a co-structure |
| 5 | QuickGO annotation retrieval for O43597 (this work) | Review/database | **Context** | Is GO:1990948 already annotated? | GO:1990948 absent; Cbl papers back only GO:0005515 (IPI); BP counterpart GO:0031397 *negative regulation of protein ubiquitination* already present (IDA, PMID:17974561) | Database snapshot | High; reflects current annotation state |
| 6 | [PMID:18219583](https://pubmed.ncbi.nlm.nih.gov/18219583/) | Review | **Orientation** | Paralog functional divergence | Four mammalian Spry isoforms; RTK modulation is growth-factor- and cell-context-dependent | Endothelial/angiogenesis review | Review-level; orientation only |

---

## Key Findings

### Finding 1 — SPRY2 Tyr55 is a genuine, experimentally validated c-Cbl TKB-domain binding motif

The core of the hypothesis is correct. Scoring the human/mouse SPRY2 sequence window (residues 53–59, **N-E-Y55-T-E-G-P**) against the canonical c-Cbl TKB phosphopeptide consensus **(N/D)-x-pY-(S/T)-x-x-P** yields a perfect 4/4 match at the diagnostic positions: Asn at −2, the phospho-acceptor Tyr55, Thr at +1, and Pro at +4. Human and mouse SPRY2 share the identical nonapeptide (NTNEYTEGP), establishing mammalian conservation at this locus.

Crucially, this is not merely a sequence coincidence — it is backed by direct wet-lab evidence. Fong et al. ([PMID:12815057](https://pubmed.ncbi.nlm.nih.gov/12815057/)) showed by site-directed mutagenesis that *"A conserved motif on hSpry2, together with phosphorylation on tyrosine 55, is required for its enhanced interaction with the SH2-like domain of c-Cbl. A hSpry2 mutant (Y55F) that did not exhibit an enhanced binding with c-Cbl failed to retain EGF receptors on the cell surface."* The Y55F loss-of-function links the motif → Cbl binding → EGFR retention in a single causal chain. Rubin et al. ([PMID:12593795](https://pubmed.ncbi.nlm.nih.gov/12593795/)) independently confirmed that *"Sprouty2 undergoes phosphorylation at a conserved tyrosine that recruits the Src homology 2 domain of c-Cbl,"* sequestering active c-Cbl and impeding EGFR ubiquitination and downregulation.

Mechanistically, this is textbook ubiquitin-ligase inhibition: phospho-SPRY2 occupies the substrate-recognition (TKB/SH2-like) pocket of c-Cbl, acting as a competitive decoy that prevents Cbl from engaging and ubiquitinating the activated EGFR. That molecular activity maps directly onto **GO:1990948 ubiquitin ligase inhibitor activity**.

### Finding 2 — The motif is NOT SPRY2-specific; the discriminator claim fails

The hypothesis's distinguishing argument — that SPRY4 lacks the motif and this is why SPRY4 fails to block EGFR downregulation — does not survive paralog scoring.

| Paralog | Tyr | Window | TKB score | −2 | pY | +1 | +4 |
|---------|-----|--------|-----------|----|----|----|----|
| SPRY1 | Y53 | ...NE**Y**TEGP | **4/4** | N | Y | T | P |
| SPRY2 | Y55 | ...NE**Y**TEGP | **4/4** | N | Y | T | P |
| SPRY4 | Y52 | ...ND**Y**IDNP | **3/4** | D | Y | **I** | P |

SPRY1 carries an *identical* NEYTEGP core to SPRY2 (4/4), so the motif cannot by itself explain SPRY2-specific behavior. And SPRY4 does **not** "lack an equivalent motif": it retains D@−2 (an allowed Asp/Asn position), the phospho-acceptor Tyr, and P@+4, losing only the +1 Ser/Thr hydroxyl residue (an Ile instead) — a 3/4 degenerate near-match, not an absence.

The true, documented molecular basis for the SPRY2-vs-SPRY4 difference lies elsewhere. Haglund et al. ([PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/)): *"The CIN85 SH3 domains A and C bind specifically to proline-arginine motifs present in Sprouty2. Intact association between Sprouty2, Cbl and CIN85 is required for inhibition of EGFR downregulation. Moreover, Sprouty4, which lacks CIN85-binding sites, does not inhibit EGFR downregulation, providing a molecular explanation for functional differences between Sprouty isoforms."* The discriminator is the **CIN85 proline-arginine (SH3) motif**, not the Cbl TKB motif. The seed context itself acknowledges this, and the sequence analysis confirms it.

### Finding 3 — Vertebrate ortholog alignment: TKB motif conserved in SPRY2 (and SPRY1), with a conserved +1 Ile in SPRY4

Extending the scoring across vertebrate orthologs reinforces both halves of the story. All seven SPRY2 orthologs examined (human, mouse, bovine, chicken, orangutan, *Chlorocebus*, *Macaca*) share the identical window **NTNEYTEGP = 4/4** with Thr at +1. SPRY1 mammalian orthologs (human, mouse, bovine, *Cervus*) all show **GSNEYTEGP = 4/4**, an identical NEYTEGP core. SPRY4 orthologs (human, mouse, bovine) all show **VENDYIDNP = 3/4**, with a *conserved* non-hydroxyl Ile at +1.

Two conclusions follow. (i) The conservation claim in the hypothesis is genuinely supported — the TKB motif is deeply conserved across vertebrate SPRY2. (ii) But the only position that discriminates paralogs — the +1 Ser/Thr — splits **SPRY1+SPRY2 (Thr) from SPRY4 (Ile)**, not SPRY2 from everything else. The evolutionary signal is "Cbl-binding Sprouty clade (SPRY1/2) vs. SPRY4," not "SPRY2-unique."

### Finding 4 — GO:1990948 is absent from SPRY2; the Cbl interaction is captured only as generic "protein binding"

A QuickGO annotation retrieval for O43597 (100 rows) shows that the two key Cbl-binding papers ([PMID:12815057](https://pubmed.ncbi.nlm.nih.gov/12815057/), [PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/)) currently support only **GO:0005515 protein binding (IPI)**. The more specific **GO:1990948 ubiquitin ligase inhibitor activity (MF) is absent.** The existing inhibitor-related MF terms are either generic/projected (GO:0004857 enzyme inhibitor activity, IEA; GO:0140678 molecular function inhibitor activity, IEA; GO:0004860 protein kinase inhibitor activity, IBA) or refer to a different activity (GO:0030291 protein serine/threonine kinase inhibitor activity, IDA, PMID:20736167). Notably, the **BP counterpart already exists**: GO:0031397 *negative regulation of protein ubiquitination* (IDA, PMID:17974561). The presence of the BP term without its matching MF term is exactly the annotation gap GO:1990948 fills.

For completeness, the supplied reference-context PMID:18070883 currently underpins GO:0043539 (protein ser/thr kinase activator activity, IMP) and several BP terms (GO:0010628, GO:0033138, GO:0043066) — i.e., it is a cellular functional study, not the Cbl-motif analysis, and does not itself provide the motif evidence.

---

## Mechanistic Model / Interpretation

```
          EGF
           │
           ▼
      ┌─────────┐      activation       ┌──────────────┐
      │  EGFR   │ ───────────────────▶  │ phospho-EGFR │
      └─────────┘                        └──────┬───────┘
                                                 │
                        c-Cbl TKB domain recognizes EGFR pTyr
                                                 │
                                                 ▼
                                        EGFR ubiquitination
                                        → endocytosis / degradation
                                        (DOWNREGULATION)

   SPRY2 inhibition (GO:1990948 ubiquitin ligase inhibitor activity):

      SPRY2 ─(phosphorylated on Tyr55)─▶  pY55 in N-E-pY-T-E-G-P
                                               │
                   occupies c-Cbl TKB/SH2-like pocket (DECOY)
                                               │
                   + CIN85 SH3 ↔ SPRY2 Pro-Arg motifs (ternary complex)
                                               ▼
                 c-Cbl sequestered → EGFR ubiquitination BLOCKED
                 → EGFR RETAINED at surface → sustained signaling
```

**Two distinct molecular modules, one phenotype.**

| Module | Partner | Motif on SPRY2 | Present in SPRY4? | Role in blocking EGFR downregulation |
|--------|---------|----------------|-------------------|--------------------------------------|
| A — Cbl engagement | c-Cbl TKB/SH2-like | pTyr55 in N-E-Y-T-E-G-P (4/4) | Partial (3/4, +1 Ile) | Necessary; competitive decoy for Cbl substrate pocket |
| B — CIN85 engagement | CIN85 SH3 (A & C) | Proline-arginine (SH3-ligand) | **Absent** | Necessary; stabilizes ternary complex |

The hypothesis correctly identifies **Module A** as a real ubiquitin-ligase-inhibitory activity, and this is the basis for the MF annotation. But it mis-assigns the *paralog discriminator* to Module A, when the literature places it in **Module B** (CIN85). Both modules are required for the full EGFR-downregulation-blocking phenotype; the TKB motif alone is shared with SPRY1 and only degraded (not deleted) in SPRY4.

The cleanest reading for curation: SPRY2 has *ubiquitin ligase inhibitor activity* directed at c-Cbl, exerted through a pTyr55 TKB-motif decoy mechanism, and this activity is captured by GO:1990948. The *specificity* of the physiological outcome among paralogs is an additional layer (CIN85 motifs) that is a separate annotation story and not a prerequisite for assigning the MF term.

---

## Evidence Base

- ***Tyrosine phosphorylation of Sprouty2 enhances its interaction with c-Cbl and is crucial for its function.*** [PMID:12815057](https://pubmed.ncbi.nlm.nih.gov/12815057/) — The anchor paper. Direct Y55F mutagenesis establishes pTyr55 as required for c-Cbl TKB binding and EGFR retention. Supports the MF assignment.
- ***Sprouty fine-tunes EGF signaling through interlinked positive and negative feedback loops.*** [PMID:12593795](https://pubmed.ncbi.nlm.nih.gov/12593795/) — Independent confirmation that a conserved N-terminal pTyr recruits the c-Cbl SH2 domain and impedes EGFR ubiquitination. Supports the decoy mechanism.
- ***Sprouty2 acts at the Cbl/CIN85 interface to inhibit epidermal growth factor receptor downregulation.*** [PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/) — Supports the MF (ternary complex inhibits EGFR downregulation) but *refutes the discriminator claim*: SPRY4 fails because it lacks CIN85 Pro-Arg sites, not the Cbl TKB motif.
- ***Sprouty proteins, masterminds of receptor tyrosine kinase signaling.*** [PMID:18219583](https://pubmed.ncbi.nlm.nih.gov/18219583/) — Review; orientation on paralog divergence and context dependence. Not primary evidence.
- QuickGO/O43597 annotation snapshot (database-level) — documents that GO:1990948 is currently missing and the BP counterpart GO:0031397 is present.

---

## Conflicts and Alternatives

1. **Paralog-specificity conflict (central).** The hypothesis frames the TKB motif as SPRY2-distinguishing; sequence scoring shows SPRY1 is identical (4/4) and SPRY4 is a 3/4 near-match. The motif marks the Cbl-binding Sprouty clade, not SPRY2 alone. Directly refuted by Findings 2/3.
2. **Wrong discriminator.** [PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/) attributes the SPRY2-vs-SPRY4 difference to CIN85 Pro-Arg motifs. A curator should not cite "SPRY4 lacks the Cbl TKB motif" as rationale.
3. **Consensus match ≠ structure.** The 4/4 score is against a published consensus, not a solved SPRY2:c-Cbl co-crystal. The exact register and +1 preference of the Cbl TKB pocket for SPRY2 is inferred.
4. **Overexpression/context dependence.** The mechanistic data come from EGFR-pathway cell-line studies; Spry isoform behavior is explicitly growth-factor- and cell-context-dependent ([PMID:18219583](https://pubmed.ncbi.nlm.nih.gov/18219583/)). The inhibitory activity may not generalize across all RTKs or tissues.
5. **Reference-context mismatch.** Supplied PMID:18070883 underpins kinase-activator and BP annotations, not the Cbl-motif analysis; it is not independent support for the MF term.

---

## GO Curation Implications

**Lead (requires curator verification): ADD GO:1990948 *ubiquitin ligase inhibitor activity* (MF) to SPRY2 (O43597).**

- **Evidence class:** Direct assay (IDA/IMP) supportable by [PMID:12815057](https://pubmed.ncbi.nlm.nih.gov/12815057/) (Y55F mutant abolishes Cbl binding and EGFR retention) with corroboration from [PMID:12593795](https://pubmed.ncbi.nlm.nih.gov/12593795/) and [PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/).
- **Why more specific than current:** These papers currently back only GO:0005515 *protein binding* (IPI). GO:1990948 captures the actual molecular activity (inhibition of the c-Cbl E3 ligase) and is strictly more informative. Per curation guidance, avoid leaving "protein binding" as the final term when a more informative MF is supported.
- **Consistency check:** The BP counterpart GO:0031397 *negative regulation of protein ubiquitination* (IDA, PMID:17974561) is already annotated — adding the MF term closes a coherent MF/BP pair.
- **Qualifier/target note:** If the GO framework supports it, annotate with the physical target (c-Cbl / CBL, UniProt P22681) to record that the inhibited ligase is specifically c-Cbl.

**Do NOT** record the rationale as "SPRY2-unique motif absent in SPRY4." The sequence evidence refutes paralog specificity of the TKB motif; the paralog difference is a CIN85-motif story.

### GO decision table

| GO term | Aspect | Current state | Recommended action | Basis |
|---------|--------|---------------|--------------------|-------|
| GO:1990948 ubiquitin ligase inhibitor activity | MF | Absent | **Add** (curator-verify) | PMID:12815057, 12593795, 15962011 |
| GO:0005515 protein binding | MF | Present (IPI, Cbl papers) | Retain but supersede with GO:1990948 as the informative term | — |
| GO:0031397 neg. reg. protein ubiquitination | BP | Present (IDA) | Retain (BP counterpart) | PMID:17974561 |
| "SPRY4 lacks TKB motif" rationale | — | Proposed | **Reject as rationale** | Sequence scoring: SPRY4 = 3/4; SPRY1 = 4/4 |

---

## Mechanistic Scope

**Immediate molecular activity being tested:** competitive inhibition of the c-Cbl RING E3 ubiquitin ligase by phospho-SPRY2, via occupation of the Cbl TKB/SH2-like substrate-recognition pocket by pTyr55. This is a direct gene-product molecular function (GO:1990948).

**Separable downstream layers (not the MF term itself):**
- *Pathway consequence:* reduced EGFR ubiquitination → impaired receptor endocytosis/degradation (GO:0031397 BP).
- *Signaling outcome:* EGFR retention at the cell surface → sustained/modulated RTK–MAPK signaling.
- *Phenotype/developmental:* Sprouty family negative-feedback modulation of growth-factor responses (context-dependent; review-level).

The MF assignment rests on the first layer only, which is directly evidenced. The paralog-discriminator claim belongs to the downstream-outcome layer and is governed by CIN85 motifs, not the TKB motif.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| No co-structure | Consensus scoring only (4/4) | Confirms motif register and the +1 preference of the Cbl TKB pocket for SPRY2 | SPRY2 phosphopeptide:c-Cbl TKB co-crystal or cryo-EM; AlphaFold-Multimer with PAE at the interface |
| Does SPRY1 actually inhibit Cbl comparably? | SPRY1 scores identical 4/4 | If SPRY1 binds Cbl equally, it strengthens "clade" not "SPRY2-unique" reading and may warrant a SPRY1 annotation too | Direct SPRY1–Cbl binding + EGFR-downregulation assays |
| SPRY4 3/4 — does it bind Cbl weakly? | Scored 3/4 (loses +1 hydroxyl) | Determines whether SPRY4's failure is purely CIN85-driven or also weaker Cbl engagement | Quantitative SPRY4 pY52–Cbl TKB affinity measurement |
| Generality beyond EGFR/cell lines | Evidence from overexpression EGFR systems | MF may be RTK/context-specific | Endogenous-level and multi-RTK validation |
| Reference PMID:18070883 content | Confirmed it backs kinase-activator/BP terms | It is not motif evidence; curators should not treat it as such | n/a (documented) |

---

## Discriminating Tests

1. **SPRY1 vs SPRY2 vs SPRY4 head-to-head Cbl TKB binding (ITC/SPR with synthetic pY phosphopeptides):** directly tests whether the +1 Thr→Ile (SPRY4) and the shared NEYTEGP (SPRY1/2) predict binding affinity. Expectation under this report: SPRY1 ≈ SPRY2 > SPRY4.
2. **Domain-swap functional assay:** transplant the CIN85 Pro-Arg motifs into SPRY4 and test rescue of EGFR-downregulation blockade — isolates Module B (CIN85) from Module A (TKB) as the discriminator.
3. **SPRY2 +1 mutant (T56I) EGFR assay:** convert SPRY2's +1 Thr to the SPRY4-like Ile; if EGFR blockade persists, the +1 residue is not the functional discriminator.
4. **Structural confirmation:** AlphaFold-Multimer (SPRY2 pY55 peptide + c-Cbl TKB) and/or co-crystal to confirm the binding register claimed by consensus scoring.
5. **Endogenous co-IP across cell types** to confirm the MF beyond overexpression artifacts.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**Candidate annotation update (lead — verify before committing):**
- Add **GO:1990948 ubiquitin ligase inhibitor activity** (MF) to O43597.
- Evidence code: IMP/IDA from [PMID:12815057](https://pubmed.ncbi.nlm.nih.gov/12815057/) (Y55F mutant); supporting [PMID:12593795](https://pubmed.ncbi.nlm.nih.gov/12593795/), [PMID:15962011](https://pubmed.ncbi.nlm.nih.gov/15962011/).
- Where supported, annotate the target as c-Cbl (CBL, P22681).
- Supersede the Cbl-paper GO:0005515 *protein binding* annotations with the more informative MF term.

**Candidate reference snippets to verify (exact quotes from stored abstracts):**
- PMID:12815057 — *"A conserved motif on hSpry2, together with phosphorylation on tyrosine 55, is required for its enhanced interaction with the SH2-like domain of c-Cbl. A hSpry2 mutant (Y55F) ... failed to retain EGF receptors on the cell surface."*
- PMID:15962011 — *"Sprouty4, which lacks CIN85-binding sites, does not inhibit EGFR downregulation, providing a molecular explanation for functional differences between Sprouty isoforms."*

**Suggested questions for the curator:**
- Should SPRY1 receive the same MF annotation given its identical TKB motif and documented Cbl engagement?
- Should the review text be corrected to attribute the SPRY2-vs-SPRY4 difference to CIN85 motifs (Module B), not to the TKB motif (Module A)?

**Rationale wording to AVOID:** "SPRY4 lacks the Cbl TKB motif." Replace with: "SPRY4 retains a degenerate TKB near-match but lacks CIN85-binding proline-arginine motifs, which is the documented molecular basis for its failure to block EGFR downregulation."

---

## Conclusion

The hypothesis is **partially supported**. Its structural and mechanistic core is correct and directly evidenced, and it correctly motivates adding GO:1990948 *ubiquitin ligase inhibitor activity* — a term currently missing from SPRY2 and more informative than the generic *protein binding* now carried on the same papers. However, its distinguishing argument (that the Cbl TKB motif is SPRY2-specific and explains the SPRY2-vs-SPRY4 difference) is refuted by sequence scoring (SPRY1 identical 4/4; SPRY4 a 3/4 near-match) and by the primary literature, which attributes that difference to CIN85-binding proline-arginine motifs. Curators should act on the function assignment while discarding the flawed paralog-discriminator rationale.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)