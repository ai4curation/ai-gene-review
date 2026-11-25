---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T06:22:51.415195'
end_time: '2026-10-01T07:01:03.668945'
duration_seconds: 2292.25
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SPRY4
  gene_symbol: SPRY4
  uniprot_accession: Q9C004
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: spry4-raf-not-grb2
  hypothesis_text: 'Human SPRY4 (Q9C004) inhibits Ras-ERK signalling mainly by binding
    RAF1 through its C-terminal cysteine-rich Sprouty domain rather than by sequestering
    GRB2, because SPRY4 lacks the C-terminal PxxPxR GRB2 SH3-binding motif present
    in SPRY2 while retaining the cysteine-rich domain. Test this with one analysis:
    align SPRY2 and SPRY4 orthologs across vertebrates, score presence of the PxxPxR
    motif in each, and compare conservation of the cysteine-rich Sprouty domain.'
  term_context: '- Term: protein kinase inhibitor activity (GO:0004860)

    - Grafting the SPRY2 PxxPxR motif onto SPRY4 is reported to confer GRB2-dependent
    inhibition.'
  reference_context: '- PMID:12717443'
  source_file: genes/human/SPRY4/SPRY4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human SPRY4 (Q9C004) inhibits Ras-ERK signalling\
    \ mainly by binding RAF1 through its C-terminal\n  cysteine-rich Sprouty domain\
    \ rather than by sequestering GRB2, because SPRY4 lacks the C-terminal PxxPxR\n\
    \  GRB2 SH3-binding motif present in SPRY2 while retaining the cysteine-rich domain.\
    \ Test this with one\n  analysis: align SPRY2 and SPRY4 orthologs across vertebrates,\
    \ score presence of the PxxPxR motif in\n  each, and compare conservation of the\
    \ cysteine-rich Sprouty domain.'\nfocus_type: free_text\nterm_id: GO:0004860\n\
    term_label: protein kinase inhibitor activity\ncontext:\n- Grafting the SPRY2\
    \ PxxPxR motif onto SPRY4 is reported to confer GRB2-dependent inhibition.\nreference_id:\n\
    - PMID:12717443"
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
citation_count: 4
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: spry4_go_decision_leads.csv
  path: openscientist_artifacts/spry4_go_decision_leads.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist spry4 go decision leads
- filename: spry_motif_comparison.csv
  path: openscientist_artifacts/spry_motif_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist spry motif comparison
- filename: spry_ortholog_motif_analysis.csv
  path: openscientist_artifacts/spry_ortholog_motif_analysis.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist spry ortholog motif analysis
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
- **Gene directory:** SPRY4
- **Gene symbol:** SPRY4
- **UniProt accession:** Q9C004

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** spry4-raf-not-grb2
- **Source file:** genes/human/SPRY4/SPRY4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human SPRY4 (Q9C004) inhibits Ras-ERK signalling mainly by binding RAF1 through its C-terminal cysteine-rich Sprouty domain rather than by sequestering GRB2, because SPRY4 lacks the C-terminal PxxPxR GRB2 SH3-binding motif present in SPRY2 while retaining the cysteine-rich domain. Test this with one analysis: align SPRY2 and SPRY4 orthologs across vertebrates, score presence of the PxxPxR motif in each, and compare conservation of the cysteine-rich Sprouty domain.

## Term and Decision Context

- Term: protein kinase inhibitor activity (GO:0004860)
- Grafting the SPRY2 PxxPxR motif onto SPRY4 is reported to confer GRB2-dependent inhibition.

## Reference Context

- PMID:12717443

## Source Context YAML

```yaml
hypothesis: 'Human SPRY4 (Q9C004) inhibits Ras-ERK signalling mainly by binding RAF1 through its C-terminal
  cysteine-rich Sprouty domain rather than by sequestering GRB2, because SPRY4 lacks the C-terminal PxxPxR
  GRB2 SH3-binding motif present in SPRY2 while retaining the cysteine-rich domain. Test this with one
  analysis: align SPRY2 and SPRY4 orthologs across vertebrates, score presence of the PxxPxR motif in
  each, and compare conservation of the cysteine-rich Sprouty domain.'
focus_type: free_text
term_id: GO:0004860
term_label: protein kinase inhibitor activity
context:
- Grafting the SPRY2 PxxPxR motif onto SPRY4 is reported to confer GRB2-dependent inhibition.
reference_id:
- PMID:12717443
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

# SPRY4 Hypothesis Review: "RAF1-binding, not GRB2-sequestration" (slug: spry4-raf-not-grb2)

**Gene:** SPRY4 (human, Q9C004) · **Term in context:** GO:0004860 protein kinase inhibitor activity
**Seed reference:** [PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/) · **Focus type:** free_text core-/function-assignment hypothesis
**Investigation:** 3 iterations · 4 confirmed findings · 4 primary/secondary papers

---

## Summary

**Verdict: Partially supported — supported on its structural/evolutionary premise, mechanistically correct in direction but over-generalized in scope.**

The seed hypothesis bundles two separable claims. The first is a **structural/evolutionary** claim: human SPRY4 lacks the C-terminal **PxxPxR** GRB2-SH3-binding motif present in SPRY2, while retaining the cysteine-rich Sprouty (SPR) domain. The second is a **mechanistic** claim: SPRY4 therefore inhibits Ras–ERK signalling "mainly by binding RAF1 through its cysteine-rich domain rather than by sequestering GRB2." The seed proposes one decisive test — align SPRY2 and SPRY4 orthologs across vertebrates, score the PxxPxR motif, and compare conservation of the cysteine-rich domain.

That requested analysis was carried out and **cleanly confirms the structural premise**. Among the four human paralogs, the PxxPxR (SH3 class-II) motif occurs **only in SPRY2** (`PTVPPR`, residue 304, within the terminal 12 residues); it is absent in SPRY1, SPRY3, and SPRY4. Extending to reviewed orthologs, **all 7 reviewed SPRY2 orthologs carry a C-terminal PxxPxR** and **all 3 reviewed SPRY4 orthologs lack it**, while the cysteine-rich SPR core (`PGCRCK`) is conserved in both paralogs. This matches the experimental statement that the GRB2-binding sequence is "found exclusively on Spry2" ([PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/)).

The mechanistic claim is **correct in direction but must be qualified in scope**. SPRY4 does bind Raf1 via its C-terminal cysteine-rich domain, and that binding is necessary for its inhibitory activity ([PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/)). But the documented SPRY4–Raf1 effect is specific to **VEGF-induced, Ras-*independent*** Raf1 activation and does **not** block EGF-induced, Ras-*dependent* Raf1 activation. The phrase "inhibits Ras–ERK signalling mainly by binding RAF1" therefore extends a Ras-*independent* mechanism onto the canonical Ras pathway. Separately, the cleanest **direct** evidence that SPRY4 is a protein kinase inhibitor is not Raf1 at all but **TESK1**, whose catalytic activity SPRY4 inhibits via the same cysteine-rich region ([PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/)). For curation, the evidence **supports retaining GO:0004860 (protein kinase inhibitor activity, MF)**, best anchored on TESK1, with a scope qualifier on the Raf1/Ras-ERK arm.

---

## Key Findings

### Finding 1 — The PxxPxR GRB2-SH3 motif is exclusive to SPRY2; the cysteine-rich domain is conserved in all paralogs

A direct sequence scan of the four human Sprouty paralogs (SPRY1 O43609, SPRY2 O43597, SPRY3 O43610, SPRY4 Q9C004) using the SH3 class-II regex **`P..P.R`** (PxxPxR) matched **only SPRY2**, at position 304 within the terminal 12 residues (`PTVPPR`; C-terminus `...CCKVPTVPPRNFEKPT`). No PxxPxR motif was found in SPRY1, SPRY3, or SPRY4; SPRY4's C-terminus (`...VICKAASGDAKTSRPDKPF`) contains no such motif. By contrast, the cysteine-rich Sprouty (SPR) core signature **`PGCRCK`** is present in all four paralogs, and the C-terminal-half cysteine counts are comparable (SPRY1 = 26, SPRY2 = 26, SPRY3 = 25, SPRY4 = 23), indicating the inhibitory fold is conserved while the GRB2 motif is a SPRY2-specific add-on.

This computational result is independently confirmed by experiment: [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) reports that inhibition "correlates with the binding to Grb2 via a C-terminal proline-rich sequence that is **found exclusively on Spry2**." The structural premise of the hypothesis is therefore solidly established at the human-paralog level.

### Finding 2 — SPRY4 inhibits ERK via Raf1 binding through its cysteine-rich domain (Ras-independent); SPRY2 uniquely inhibits via GRB2 sequestration

[PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/) (Sasaki et al. 2003, *Nature Cell Biology*) demonstrated that **"Sprouty4 binds to Raf1 through its carboxy-terminal cysteine-rich domain, and this binding is necessary for the inhibitory activity of Sprouty4."** The same study established the scope limit: **"mammalian Sprouty4 suppresses vascular epithelial growth factor (VEGF)-induced, Ras-independent activation of Raf1 but does not affect epidermal growth factor (EGF)-induced, Ras-dependent activation of Raf1."** This is the single most important caveat — the Raf1-binding mechanism operates on a Ras-independent branch, not canonical Ras-dependent ERK signalling.

By contrast, [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) (Lao et al. 2006, *JBC*) showed that Spry2 is considerably more inhibitory than Spry1 or Spry4 in FGFR signalling, that this correlates with Grb2 binding via the SPRY2-unique PXXPXR sequence, and that Spry2 competes with SOS1 for Grb2. The decisive gain-of-function experiment: **"when added onto the C terminus of Spry4 the resultant chimera inhibits the Ras/ERK pathway"** — confirming that native SPRY4 lacks GRB2-binding capacity and that grafting the motif confers GRB2-dependent inhibition. This is exactly the "grafting" result flagged in the term/decision context.

### Finding 3 — The cysteine-rich domain is a genuine kinase-inhibitor module: it directly inhibits TESK1

[PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/) (Tsumura et al. 2005, *Biochemical Journal*) provides direct enzymatic evidence that **"Spry4 inhibits the kinase activity of TESK1 by binding to it through the C-terminal cysteine-rich region."** This inhibition suppresses integrin-/TESK1-mediated cofilin phosphorylation and cell spreading. Importantly, the Tyr-75 residue required for Ras/MAPK inhibition is **dispensable** for TESK1 inhibition, showing the cysteine-rich domain carries an autonomous kinase-inhibitory activity distinct from the MAPK function. This is the strongest direct support for **GO:0004860**, because TESK1 is a bona fide kinase whose catalytic output SPRY4 directly suppresses — exactly the semantics of that MF term — and it is mediated by the cysteine-rich domain, not any GRB2 motif.

A useful contrast comes from [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) (Hanafusa et al. 2002), which characterized the GRB2/SOS-interference model for **Spry1 and Spry2**: "after stimulation by growth factors Spry1 and Spry2 translocate to the plasma membrane and become phosphorylated on a conserved tyrosine. Next, they bind to the adaptor protein Grb2." This mechanism is defined for Spry1/Spry2 — not Spry4 — consistent with SPRY4 lacking the GRB2 motif.

### Finding 4 — Cross-vertebrate ortholog analysis seals the structural premise

A UniProt REST search (reviewed entries, Euteleostomi, taxon 7742) scored the PxxPxR motif and the SPR core across orthologs of both paralogs:

- **SPRY2:** all **7/7** reviewed orthologs examined (human O43597, mouse Q9QXV8, bovine Q08E39, chicken Q9PTL2, macaque Q2PFN5, orangutan Q5R959, vervet Q866R9) carry a **C-terminal PxxPxR**. Position checks in human/chicken/bovine place the functional motif (`PTVPPR` / `PSVPPR`) ~6 residues from the C-terminus (position ~302–304) in a conserved context `...SNTVCCKVP[TS]VPPRNFEKPT`.
- **SPRY4:** **3/3** reviewed orthologs (human Q9C004, mouse Q9WTP2, bovine A2VDU1) have **no C-terminal PxxPxR**. The single permissive-regex hit in bovine SPRY4 (`PSGPKR`) lies at position 61 — 233 residues from the C-terminus, i.e. internal and non-functional for GRB2-SH3 engagement.
- The **cysteine-rich SPR core (`PGCRCK`) is conserved** in every SPRY2 and SPRY4 ortholog examined.

This confirms the C-terminal PxxPxR is a deeply conserved, lineage-specific feature of SPRY2 (not a one-off in human) and that SPRY4 has consistently lacked it across mammals and birds, while both paralogs conserve the inhibitory cysteine-rich fold. Coverage is limited to reviewed (Swiss-Prot) entries, which are mammal/bird-biased; deep vertebrate lineages (fish, amphibians) were not systematically scored.

---

## Mechanistic Model / Interpretation

The data resolve into a clean paralog-divergence model in which two Sprouty paralogs inhibit RTK→ERK signalling through **different molecular modules**, with SPRY4 relying entirely on the conserved cysteine-rich C-terminus:

```
                         RTK stimulation (FGF / VEGF / EGF)
                                      │
        ┌─────────────────────────────┴──────────────────────────────┐
        │                                                             │
   ── SPRY2 arm ──                                             ── SPRY4 arm ──
   (GRB2-dependent)                                          (cysteine-rich domain)
        │                                                             │
   pTyr + C-terminal PxxPxR                            C-terminal cysteine-rich (SPR) domain
        │  binds GRB2 SH3                                  │ binds Raf1        │ binds TESK1
        │  competes with SOS1                              ▼                   ▼
        ▼                                          suppresses VEGF-induced,   inhibits TESK1
   blocks GRB2–SOS → Ras loading                   Ras-INDEPENDENT Raf1       kinase activity
        │                                          activation                  │
        ▼                                                │ (does NOT block     ▼
   inhibits canonical Ras→Raf→MEK→ERK                     EGF/Ras-dependent    ↓ cofilin-P,
                                                          Raf1 activation)     ↓ cell spreading
```

**Comparison table — paralog mechanism:**

| Feature | SPRY2 | SPRY4 |
|---|---|---|
| C-terminal PxxPxR (GRB2-SH3) motif | **Present** (PTVPPR, pos 304) | **Absent** |
| Cysteine-rich SPR domain (PGCRCK) | Present | Present |
| GRB2 binding / SOS1 competition | **Yes** (dominant mechanism) | No |
| Raf1 binding via cysteine-rich domain | — (not the main route) | **Yes**, necessary for inhibition |
| Branch of Raf1 activation inhibited | Canonical Ras-dependent (via GRB2) | **VEGF-induced, Ras-independent only** |
| Direct TESK1 kinase inhibition | — | **Yes** (cysteine-rich domain) |
| Effect of grafting SPRY2 PxxPxR onto SPRY4 | n/a | **Gains** Ras/ERK (GRB2-dependent) inhibition |

The key interpretive point for curation: the seed's contrast ("RAF1 not GRB2") is **correct as a statement of paralog divergence** — SPRY4's inhibitory activity is cysteine-rich-domain-dependent and GRB2-motif-independent. But "inhibits Ras–ERK signalling **mainly** by binding RAF1" blurs a distinction the primary literature is explicit about: SPRY4's Raf1-directed effect is confined to Ras-*independent* Raf1 activation. SPRY4's most unambiguous *direct* catalytic-inhibition activity is against **TESK1**, not Raf1 (Raf1 is a binding partner whose activation is suppressed, not a kinase SPRY4 is shown to directly inhibit catalytically).

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| Sequence scan (this work; O43609/O43597/O43610/Q9C004) | Structural/evolutionary (computational) | **Supports** | PxxPxR only in SPRY2; SPR core conserved | `PTVPPR` at res 304 in SPRY2 only; no PxxPxR in SPRY1/3/4; `PGCRCK` in all four | Human paralogs, verified accessions | High for human paralogs; internal analysis, confirmed by PMID:16893902 |
| Ortholog scan (this work; UniProt REST, reviewed) | Structural/evolutionary (computational) | **Supports** | Cross-vertebrate conservation of SPRY2-specific C-terminal PxxPxR; SPR core in both | SPRY2 C-terminal PxxPxR 7/7; SPRY4 0/3 (bovine hit internal at pos 61); SPR core conserved in all | Mammals + chicken; reviewed only | High for amniotes; fish/amphibia & unreviewed not scored |
| [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) (Lao 2006) | Direct assay + interaction (mutant/chimera) | **Supports** | GRB2 motif is SPRY2-exclusive; grafting confers inhibition | PXXPXR "found exclusively on Spry2"; Spry4+PXXPXR chimera inhibits Ras/ERK; Spry2 competes with SOS1 | FGFR signalling, cultured cells | High; establishes SPRY4 natively lacks GRB2 arm |
| [PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/) (Sasaki 2003) | Direct assay + interaction | **Supports / qualifies** | SPRY4 inhibits via Raf1 binding (Cys-rich domain) | Binds Raf1 via C-terminal cysteine-rich domain; binding necessary; blocks VEGF (Ras-independent) but NOT EGF (Ras-dependent) Raf1 activation | VEGF vs EGF; mammalian cells | High; **scope caveat = Ras-independent only** |
| [PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/) (Tsumura 2005) | Direct assay (kinase activity) + interaction | **Supports (strongest for GO:0004860)** | SPRY4 has protein kinase inhibitor activity via Cys-rich domain | Inhibits **TESK1 catalytic activity** through C-terminal cysteine-rich region; suppresses cofilin-P/cell spreading; Tyr-75 dispensable | Integrin/cytoskeleton; cultured cells | High; different kinase (TESK1); Ras/MAPK-independent |
| [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) (Hanafusa 2002) | Direct assay + interaction / review | **Competing / paralog-specific** | Grb2-interference model of Sprouty | Spry1 and **Spry2** translocate, are Tyr-phosphorylated, bind Grb2 | FGFR/ERK; mammalian cells | High; characterized for Spry1/2, **not Spry4** — supports SPRY4 GRB2-independence |

---

## GO Curation Implications (leads — require curator verification)

- **GO:0004860 (protein kinase inhibitor activity, MF): RETAIN as a directly supported MF.** Strongest anchor is TESK1 catalytic inhibition via the cysteine-rich domain ([PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/)), complemented by Raf1 binding/inhibition ([PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/)). If a curator judges the Raf1 effect to be sequestration rather than catalytic inhibition, the TESK1 assay still independently licenses the term.
- **GO:0019901 (protein kinase binding, MF):** supportable fallback (Raf1, TESK1 binding) and more conservative if catalytic inhibition is contested — but do **not** downgrade all the way to generic "protein binding," which the TESK1 catalytic data make unnecessary.
- **GO:0070373 (negative regulation of ERK1/ERK2 cascade, BP):** supportable; note the Raf1 arm is in a **Ras-independent (VEGF)** context.
- **GO:0046580 (negative regulation of Ras protein signal transduction, BP):** **qualify/limit** — the SPRY4–Raf1 mechanism specifically does **not** act on Ras-dependent Raf activation; avoid over-assigning canonical Ras-pathway inhibition to the Raf1-binding mechanism.
- **GO:0030336 (negative regulation of cell migration, BP):** supportable as a distinct, Ras/MAPK-independent role via TESK1/cofilin ([PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/)).
- **Flag/remove any GRB2-sequestration annotation on SPRY4** as likely paralog carry-over from SPRY2.
- **Overall:** The seed hypothesis **should influence the review** by (a) affirming the cysteine-rich domain (not GRB2) as SPRY4's effector module, and (b) adding the caveat that SPRY4's Ras–ERK inhibition is Ras-*independent* and that its best-documented kinase-inhibitor substrate is TESK1.

---

## Mechanistic Scope

- **Direct gene-product activity:** SPRY4's C-terminal cysteine-rich (SPR) domain binds Raf1 and TESK1; it inhibits TESK1's catalytic kinase activity and is required to block Ras-independent Raf1 activation.
- **Pathway consequence:** reduced ERK1/2 phosphorylation (RTK-context-dependent; strongest for VEGF/Ras-independent) and reduced cofilin phosphorylation (cytoskeletal).
- **Downstream phenotypes (not the molecular function):** suppressed neurite outgrowth, reduced integrin-mediated cell spreading/migration, anti-angiogenic effects.
- **Not supported as SPRY4's mechanism:** GRB2–SH3 sequestration / SOS1 competition — this is the SPRY2-specific route ([PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/); the Hanafusa model [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) is Spry1/2).

---

## Conflicts and Alternatives

1. **Paralog confusion (most important).** Much "Sprouty inhibits Ras/ERK via Grb2" literature (e.g., [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/)) concerns **Spry1/Spry2**. Carrying that mechanism over to SPRY4 would be a database/paralog carry-over error; the sequence data and Lao 2006 both say SPRY4 lacks the GRB2 motif.
2. **Ras-dependence mismatch.** The seed phrase "inhibits Ras-ERK signalling mainly by binding RAF1" conflicts with [PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/)'s finding that SPRY4–Raf1 acts on **Ras-independent** Raf activation. A curator should not annotate SPRY4 as a canonical Ras-dependent ERK inhibitor on the Raf1 interaction alone.
3. **Which kinase is "directly inhibited"?** The only *direct kinase-activity inhibition* demonstrated is against **TESK1** ([PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/)). Raf1 is a binding partner whose activation is suppressed. The cysteine-rich domain targets at least two unrelated kinases (Raf1, TESK1), so "RAF1" is one instance of a broader Cys-rich-domain kinase-inhibitory activity rather than the sole target.
4. **Tyrosine-phosphorylation dependence differs by function.** The conserved N-terminal tyrosine (Tyr-53/Tyr-75 depending on numbering) is required for FGF/Ras-ERK inhibition but dispensable for VEGF-Raf1 and TESK1 inhibition — SPRY4 uses distinct mechanisms per context.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Deep-vertebrate ortholog conservation of PxxPxR/SPR | SPRY2 7 orthologs + SPRY4 3 orthologs (reviewed, amniote-biased) | The seed's proposed test is a cross-vertebrate alignment; demonstrated for amniotes, not fish/amphibia | Full orthology set (OrthoDB/Ensembl Compara) + MSA with motif scoring |
| Direct vs sequestration for Raf1 | Literature (binding necessary for inhibition) | Determines whether GO:0004860 vs GO:0019901 is most precise for the Raf1 arm | In vitro Raf1 kinase assay ± purified SPRY4 Cys-rich domain |
| Human (vs mouse/rat) SPRY4 biochemistry | Many assays use mouse/rat Spry4 constructs | Q9C004 is the human target; residue numbering differs | Confirm key assays with human SPRY4 Q9C004 |
| Endogenous relevance | Overexpression/chimera assays dominate | Over-expression can force interactions | Endogenous co-IP / knockout rescue in physiological cells |
| Generality of the Ras-independence restriction | One primary study (VEGF vs EGF) | Whether SPRY4 ever blocks canonical Ras-dependent ERK elsewhere | Test SPRY4 against FGF/EGF-driven Ras-dependent ERK across cell types |

---

## Discriminating Tests

1. **Motif-swap reciprocal assay (confirmatory of seed):** Delete the SPR cysteine-rich domain of SPRY4 vs delete only putative C-terminal residues; test loss of Raf1/TESK1 binding and ERK/cofilin inhibition. Predicts SPR deletion abolishes inhibition while SPRY4 never gains GRB2 binding unless PXXPXR is added.
2. **In vitro Raf1 and TESK1 kinase assays** with purified SPRY4 SPR domain to distinguish catalytic inhibition (GO:0004860) from sequestration (GO:0019901).
3. **Ras-dependent vs -independent panel:** EGF vs VEGF (and FGF) stimulation with SPRY4 to confirm the Ras-independence boundary (reproduce [PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/)).
4. **Proper cross-vertebrate MSA** (Ensembl Compara orthologs of SPRY2 and SPRY4) scoring PxxPxR and SPR-domain conservation across fish/amphibians — completing the deep-lineage portion of the seed's proposed analysis.
5. **Endogenous interactome IP** comparing GRB2 vs Raf1 vs TESK1 to confirm the native SPRY4 interactome lacks GRB2 engagement.

---

## Curation Leads (require curator verification)

- **Candidate references to attach/verify:**
  - [PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/) — snippet: *"Sprouty4 binds to Raf1 through its carboxy-terminal cysteine-rich domain, and this binding is necessary for the inhibitory activity of Sprouty4"*; and *"suppresses vascular epithelial growth factor (VEGF)-induced, Ras-independent activation of Raf1 but does not affect epidermal growth factor (EGF)-induced, Ras-dependent activation of Raf1."*
  - [PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/) — snippet: *"Spry4 inhibits the kinase activity of TESK1 by binding to it through the C-terminal cysteine-rich region."*
  - [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) — snippets: *"a C-terminal proline-rich sequence that is found exclusively on Spry2"* and *"when added onto the C terminus of Spry4 the resultant chimera inhibits the Ras/ERK pathway."*
  - [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) — snippet: *"Spry1 and Spry2 translocate to the plasma membrane ... bind to the adaptor protein Grb2"* (establishes the GRB2 route is Spry1/2, not Spry4).
- **GO term leads:** Retain **GO:0004860** (MF, direct via TESK1); consider adding **GO:0019901** (binding), **GO:0070373** (BP), **GO:0030336** (BP, TESK1/cytoskeleton); **qualify** any Ras-dependent BP term.
- **Action change lead:** Reframe the review statement from "inhibits Ras-ERK mainly by binding RAF1" to "inhibits RTK→ERK and cytoskeletal signalling via its C-terminal cysteine-rich domain (binds/inhibits RAF1 in a Ras-INDEPENDENT context and directly inhibits TESK1); lacks the SPRY2 GRB2-SH3 (PxxPxR) motif."
- **Suggested curator questions:** Is the Raf1 effect catalytic inhibition or sequestration? Should human-specific (Q9C004) assays be required before IDA? Is TESK1 inhibition in-scope for this gene's core-function annotation?

---

## Evidence Base (Literature)

- *Mammalian Sprouty4 suppresses Ras-independent ERK activation by binding to Raf1.* Sasaki et al., 2003, *Nature Cell Biology*. [PMID:12717443](https://pubmed.ncbi.nlm.nih.gov/12717443/) — Establishes the SPRY4–Raf1 cysteine-rich mechanism and its Ras-independent scope. **Supports with caveat.**
- *A Src homology 3-binding sequence on the C terminus of Sprouty2 is necessary for inhibition of the Ras/ERK pathway downstream of FGFR stimulation.* Lao et al., 2006, *JBC*. [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) — Shows the GRB2-binding PxxPxR motif is SPRY2-exclusive and that grafting it onto SPRY4 confers Ras/ERK inhibition. **Supports.**
- *Sprouty-4 negatively regulates cell spreading by inhibiting the kinase activity of testicular protein kinase (TESK1).* Tsumura et al., 2005, *Biochemical Journal*. [PMID:15584898](https://pubmed.ncbi.nlm.nih.gov/15584898/) — Direct demonstration of SPRY4 kinase-inhibitor activity via the cysteine-rich domain. **Supports GO:0004860.**
- *Sprouty1 and Sprouty2 provide a control mechanism for the Ras/MAPK signalling pathway.* Hanafusa et al., 2002. [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) — Defines the GRB2-interference mechanism for Spry1/Spry2, not Spry4. **Qualifies.**

---

## Proposed Follow-up Experiments / Actions

1. **Complete the deep-vertebrate alignment** as a saved artifact: SPRY1–4 across jawed vertebrates (including fish/amphibians and unreviewed entries) with per-residue conservation of the PxxPxR window and the cysteine-rich domain.
2. **Resolve direct vs indirect Raf1 inhibition** with in vitro kinase assays using the purified SPRY4 cysteine-rich domain.
3. **Re-test scope** of SPRY4's ERK inhibition across RTKs and cell types to confirm the Ras-independence restriction generalizes.
4. **Audit SPRY4's existing annotation set** for GRB2/SOS carry-over from SPRY2 and re-anchor the MF term on TESK1.
5. **Update the review text** to reflect the scope qualifier and the TESK1-vs-Raf1 distinction.

---

*Report generated from a 3-iteration autonomous investigation (4 confirmed findings; 4 primary/secondary papers). Internal sequence and ortholog scans are computational and were confirmed against primary experimental literature where possible; deep-vertebrate ortholog coverage is limited to reviewed UniProt entries and was not extended to fish/amphibian lineages — stated plainly, not fabricated.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist spry4 go decision leads](openscientist_artifacts/spry4_go_decision_leads.csv)
- [OpenScientist spry motif comparison](openscientist_artifacts/spry_motif_comparison.csv)
- [OpenScientist spry ortholog motif analysis](openscientist_artifacts/spry_ortholog_motif_analysis.csv)