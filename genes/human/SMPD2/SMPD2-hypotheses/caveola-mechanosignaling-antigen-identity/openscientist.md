---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T00:24:12.142056'
end_time: '2026-09-21T00:50:00.209169'
duration_seconds: 1548.07
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SMPD2
  gene_symbol: SMPD2
  uniprot_accession: O60906
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: caveola-mechanosignaling-antigen-identity
  hypothesis_text: 'Adjudicate human SMPD2 O60906 caveola activity GO0005901 and mechanical-stimulus
    response GO0009612 inherited/transferred from rat Smpd2 Q9ET64 (RGD619753). Actual
    live PTHR12393 target PTN002487871 descends from caveola IBD PTN000963363; the
    UniProt newer family PTHR16320 is a version difference, not a wrong target. QuickGO
    rat donor has caveola IDA and mechanical/signaling IMP12473648. Read full primary12473648
    (author-deposited ResearchGate available): rat lung perfusion/neutral-SMase assays
    and bovine endothelial Fig4 immunoblots are distinct; Methods uses preimmune and
    antiserum against bovine neutral SMase from Bernardo10713073; Discussion links
    the detected enzyme to that purified protein. Primary10713073 reports p97/46 purified
    species and peptide-specific antibodies; later16517606 clones nSMase3 using a
    peptide from a previously purified bovine neutral SMase. Trace exact peptide/antigen
    and genomic protein identity, not a title or nonspecific neutral-SMase name. Does
    the reagent correspond to SMPD2, another isoform, or unresolved/cross-reactive
    antigen? Find later target-specific caveolar/mechanosensitive evidence. Do not
    infer absence of SMPD2 function merely from rat/bovine assays, a sole donor, or
    another isoform performing a similar reaction. Do not overturn independent core
    SMase/ceramide function: full human25168245 Fig7 demonstrates endogenous SMPD2
    RNAi-dependent stress/Fas ceramide production, distinct from the mechanical/caveola
    hypothesis.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/SMPD2/SMPD2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Adjudicate human SMPD2 O60906 caveola activity\
    \ GO0005901 and mechanical-stimulus response\n  GO0009612 inherited/transferred\
    \ from rat Smpd2 Q9ET64 (RGD619753). Actual live PTHR12393 target PTN002487871\n\
    \  descends from caveola IBD PTN000963363; the UniProt newer family PTHR16320\
    \ is a version difference,\n  not a wrong target. QuickGO rat donor has caveola\
    \ IDA and mechanical/signaling IMP12473648. Read full\n  primary12473648 (author-deposited\
    \ ResearchGate available): rat lung perfusion/neutral-SMase assays and\n  bovine\
    \ endothelial Fig4 immunoblots are distinct; Methods uses preimmune and antiserum\
    \ against bovine\n  neutral SMase from Bernardo10713073; Discussion links the\
    \ detected enzyme to that purified protein.\n  Primary10713073 reports p97/46\
    \ purified species and peptide-specific antibodies; later16517606 clones\n  nSMase3\
    \ using a peptide from a previously purified bovine neutral SMase. Trace exact\
    \ peptide/antigen\n  and genomic protein identity, not a title or nonspecific\
    \ neutral-SMase name. Does the reagent correspond\n  to SMPD2, another isoform,\
    \ or unresolved/cross-reactive antigen? Find later target-specific caveolar/mechanosensitive\n\
    \  evidence. Do not infer absence of SMPD2 function merely from rat/bovine assays,\
    \ a sole donor, or another\n  isoform performing a similar reaction. Do not overturn\
    \ independent core SMase/ceramide function: full\n  human25168245 Fig7 demonstrates\
    \ endogenous SMPD2 RNAi-dependent stress/Fas ceramide production, distinct\n \
    \ from the mechanical/caveola hypothesis.'\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifacts_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: artifacts_go_decision_table.csv
  path: openscientist_artifacts/artifacts_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
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
- **Gene directory:** SMPD2
- **Gene symbol:** SMPD2
- **UniProt accession:** O60906

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** caveola-mechanosignaling-antigen-identity
- **Source file:** genes/human/SMPD2/SMPD2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Adjudicate human SMPD2 O60906 caveola activity GO0005901 and mechanical-stimulus response GO0009612 inherited/transferred from rat Smpd2 Q9ET64 (RGD619753). Actual live PTHR12393 target PTN002487871 descends from caveola IBD PTN000963363; the UniProt newer family PTHR16320 is a version difference, not a wrong target. QuickGO rat donor has caveola IDA and mechanical/signaling IMP12473648. Read full primary12473648 (author-deposited ResearchGate available): rat lung perfusion/neutral-SMase assays and bovine endothelial Fig4 immunoblots are distinct; Methods uses preimmune and antiserum against bovine neutral SMase from Bernardo10713073; Discussion links the detected enzyme to that purified protein. Primary10713073 reports p97/46 purified species and peptide-specific antibodies; later16517606 clones nSMase3 using a peptide from a previously purified bovine neutral SMase. Trace exact peptide/antigen and genomic protein identity, not a title or nonspecific neutral-SMase name. Does the reagent correspond to SMPD2, another isoform, or unresolved/cross-reactive antigen? Find later target-specific caveolar/mechanosensitive evidence. Do not infer absence of SMPD2 function merely from rat/bovine assays, a sole donor, or another isoform performing a similar reaction. Do not overturn independent core SMase/ceramide function: full human25168245 Fig7 demonstrates endogenous SMPD2 RNAi-dependent stress/Fas ceramide production, distinct from the mechanical/caveola hypothesis.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Adjudicate human SMPD2 O60906 caveola activity GO0005901 and mechanical-stimulus response
  GO0009612 inherited/transferred from rat Smpd2 Q9ET64 (RGD619753). Actual live PTHR12393 target PTN002487871
  descends from caveola IBD PTN000963363; the UniProt newer family PTHR16320 is a version difference,
  not a wrong target. QuickGO rat donor has caveola IDA and mechanical/signaling IMP12473648. Read full
  primary12473648 (author-deposited ResearchGate available): rat lung perfusion/neutral-SMase assays and
  bovine endothelial Fig4 immunoblots are distinct; Methods uses preimmune and antiserum against bovine
  neutral SMase from Bernardo10713073; Discussion links the detected enzyme to that purified protein.
  Primary10713073 reports p97/46 purified species and peptide-specific antibodies; later16517606 clones
  nSMase3 using a peptide from a previously purified bovine neutral SMase. Trace exact peptide/antigen
  and genomic protein identity, not a title or nonspecific neutral-SMase name. Does the reagent correspond
  to SMPD2, another isoform, or unresolved/cross-reactive antigen? Find later target-specific caveolar/mechanosensitive
  evidence. Do not infer absence of SMPD2 function merely from rat/bovine assays, a sole donor, or another
  isoform performing a similar reaction. Do not overturn independent core SMase/ceramide function: full
  human25168245 Fig7 demonstrates endogenous SMPD2 RNAi-dependent stress/Fas ceramide production, distinct
  from the mechanical/caveola hypothesis.'
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

# SMPD2 (O60906) — Adjudication of caveola (GO:0005901) and response to mechanical stimulus (GO:0009612) annotations

**Focus:** function_assignment · hypothesis slug `caveola-mechanosignaling-antigen-identity`
**Gene:** human SMPD2 / nSMase1 (UniProt O60906) · Source: `genes/human/SMPD2/SMPD2-ai-review.yaml`

---

## Executive Judgment

**Verdict: Over-annotated (refuted for SMPD2 specifically) for the caveola + mechanical-stimulus pair; core SMase/ceramide function retained.**

The caveola (GO:0005901, CC) and response-to-mechanical-stimulus (GO:0009612, BP) annotations on human SMPD2 were propagated by PANTHER phylogenetic inference (IBA/IBD) from an experimental root on rat Smpd2 (Q9ET64, RGD:619753), which in turn rests on Czarny et al. 2003 (PMID 12473648). That paper detected a caveolar, flow/pressure-activated neutral sphingomyelinase **immunologically**, using antiserum raised against a purified bovine neutral SMase (Bernardo et al. 2000, PMID 10713073). The molecular identity of that bovine antigen was **explicitly not** any then-known SMase ("no apparent homologies … to any known protein") and was **subsequently cloned as nSMase3 / SMPD4** (Krut et al. 2006, PMID 16517606: the defining peptide "allowed us to identify … nSMase3, that shows only a little homology to nSMase1 and -2").

Therefore the caveolar/mechanosensitive activity most plausibly belongs to **SMPD4 (nSMase3)** or an unresolved cross-reactive antigen — **not SMPD2/nSMase1**. No target-specific (RNAi, knockout, tagged-protein, or MS-identified) evidence places SMPD2 itself in caveolae or as a mechanosensor was found. The annotation chain is a textbook paralog/antigen carry-over.

**Most important caveats:** (1) I could not read the full text of PMID 12473648 to independently confirm the seed's claim that its Methods used the Bernardo antiserum and its Discussion links the enzyme to that purified protein — this rests on the seed and on the abstract-level chain, which is nonetheless internally consistent and corroborated by Krut 2006. (2) "Over-annotated" means *mis-attributed to this gene*, not that caveolar nSMase mechanotransduction is unreal — it is real, but the gene identity is the issue. (3) The seed's separate instruction stands: do **not** overturn SMPD2's independent core ceramide-generating function (PMID 25168245), which is molecularly target-specific and out of scope here.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| 12473648 (Czarny 2003) | Direct assay + localization | Qualifies (source of claim) | Is there a caveolar, mechanoactivated neutral SMase? | Flow/pressure transiently activate a caveola-enriched neutral (not acid) SMase → ceramide → ERK1/2; enzyme detected immunologically, **gene identity not molecularly established** | Rat lung endothelium in situ; cell-free luminal membranes | Robust for the *phenomenon*; does NOT identify the gene as Smpd2 |
| 15142848 (Czarny & Schnitzer 2004) | Direct assay (pharmacology) | Qualifies | Follow-up mechanotransduction pharmacology | Scyphostatin blocks, C2/C6-ceramide mimics mechanosignaling | Rat lung, bovine aorta EC, cell-free | Scyphostatin inhibits *all* Mg²⁺ nSMases (nSMase2/3/bovine) — not isoform-specific; cannot assign to SMPD2 |
| 10713073 (Bernardo 2000) | Direct assay (protein purification) | Refutes SMPD2 identity | What is the purified bovine nSMase antigen? | p46/p97 species; tryptic peptides "showed **no apparent homologies … to any known protein**"; peptide antibodies used downstream | Bovine brain | The antigen was neither nSMase1(SMPD2) nor nSMase2(SMPD3), both already cloned by 2000 |
| 16517606 (Krut 2006) | Structural/evolutionary + cloning | Refutes SMPD2 identity (competing = SMPD4) | Which gene does the bovine peptide correspond to? | Peptide from the purified bovine nSMase identified **nSMase3 (SMPD4)**, "only a little homology to nSMase1 and -2"; ER/Golgi, C-tail-anchored, TNF-responsive | Human cDNA; yeast expression | Directly reassigns the reagent lineage to SMPD4, a distinct paralog |
| 25168245 (Yabu 2015) | Mutant/RNAi + phosphosite | Supports (independent core, out of scope) | Does SMPD2 itself generate ceramide? | JNK phosphorylates nSMase1/SMPD2 at Ser-270; stress/anti-Fas activate it; **SMPD2 RNAi lowers ceramide** | Zebrafish ZE + human Jurkat T | Target-specific; establishes core function, unrelated to caveola/mechano |
| Computational (this run) | Computational | Supports refutation | Are nSMase1/2/3 distinct enough that a peptide couldn't be confused? | Global-alignment pairwise identity ~22% (aligned) among SMPD2/SMPD3/SMPD4 | UniProt O60906/Q9NY59/Q9NXE4 | Crude NW scoring; directionally confirms high divergence / "little homology" |

---

## GO Curation Implications (leads — require curator verification)

- **GO:0005901 (caveola, CC) on SMPD2** — *Lead: REMOVE or strongly qualify.* The only experimental support (via IBA/IBD from rat Smpd2 IDA) traces to an antibody now known to target nSMase3/SMPD4. SMPD2's own reported localization is ER/nuclear-membrane–associated, not caveolar. If IBA-derived, the correct fix is at the **experimental source annotation** on rat Smpd2 (PMID 12473648), which should be re-evaluated; correcting it will re-propagate to human.
- **GO:0009612 (response to mechanical stimulus, BP) on SMPD2** — *Lead: REMOVE or strongly qualify.* Same provenance flaw; mechanosensor role belongs to the caveolar enzyme reagent = SMPD4/nSMase3 lineage, not SMPD2.
- **Do NOT touch** SMPD2's core MF/BP terms for **sphingomyelin phosphodiesterase activity / ceramide biosynthesis / apoptotic signaling** — supported by target-specific evidence (PMID 25168245). Avoid a blanket "remove all non-core" that would collateralize the valid function.
- **PANTHER note:** The seed argues PTHR12393 vs PTHR16320 is a family-version difference, not a wrong phylogenetic target. Agreed — the annotation is not defeated by the family-version mismatch. It is defeated by the **flawed experimental root** feeding the IBD/IBA. Curators should treat the PANTHER path as legitimate but the propagated evidence as compromised.

---

## Mechanistic Scope

- **Immediate function under test:** subcellular *localization to caveolae* (CC) and participation in a plasma-membrane *mechanotransduction* response (BP) by the SMPD2 gene product.
- **Direct gene-product activity actually attributable to SMPD2:** Mg²⁺-dependent neutral sphingomyelinase → ceramide, activated downstream of JNK/stress (PMID 25168245). ER/Golgi/nuclear-membrane associated in the general literature.
- **Downstream/other-gene phenomena mis-attributed:** caveolar sphingomyelin hydrolysis → ceramide → Src/ERK mechanosignaling is a genuine endothelial pathway, but the enzyme is the bovine/nSMase3(SMPD4) lineage, i.e., a *different gene product* performing a similar reaction. Attribution to SMPD2 is inference from a non-isoform-specific reagent, not direct SMPD2 evidence.

---

## Conflicts and Alternatives

1. **Paralog confusion (primary alternative):** the reagent lineage is nSMase3/SMPD4 (Krut 2006). Competing assignment: GO:0005901/GO:0009612 should sit on **SMPD4**, if anywhere, pending isoform-specific validation.
2. **Unresolved / cross-reactive antigen:** Bernardo peptides matched "no known protein"; polyclonal antiserum against a p46/p97 pair could cross-react. The caveolar enzyme could be a mixture or a non-SMPD antigen.
3. **Organism/tissue specificity:** rat lung / bovine aorta endothelium; caveola-rich EC context does not generalize to SMPD2's ER-associated distribution in other cells.
4. **Non-specific pharmacology:** scyphostatin (PMID 15142848) inhibits all Mg²⁺ nSMases, so it cannot discriminate SMPD2 from SMPD3/SMPD4.
5. **Database carry-over:** rat Smpd2 IDA/IMP → PANTHER IBD/IBA → human SMPD2 IBA is a single-donor propagation lacking independent, target-specific confirmation.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Did PMID 12473648 Methods/Discussion actually use the Bernardo antiserum and tie the caveolar enzyme to that purified protein? | Abstracts of 12473648/15142848 (no antibody named in abstract); seed asserts full-text usage | Confirms the reagent→antigen link that drives the whole judgment | Read full text of PMID 12473648 (author-deposited copy) and confirm antibody source and Western identity |
| Is the rat Smpd2 caveola IDA / mechanical IMP in RGD/QuickGO literally sourced to PMID 12473648? | Seed states QuickGO donor Q9ET64 caveola IDA + mechanical IMP (PMID 12473648) | Determines whether fixing the source annotation corrects human IBA | Inspect QuickGO/RGD annotation provenance for Q9ET64 |
| Is there any SMPD2-specific caveolar/mechanosensitive evidence (post-2006)? | PubMed searches returned none tying SMPD2 to caveola/mechanotransduction | Absence would firm up the removal lead | Targeted search + review of SMPD2 KO/tagged-localization studies |
| Exact SMPD4/nSMase3 caveolar/mechano evidence | Krut 2006 shows ER/Golgi, TNF-responsive; caveola not directly shown for SMPD4 | Decides whether the terms should *move* to SMPD4 vs. be dropped entirely | Isoform-specific localization/mechano assays for SMPD4 |

---

## Discriminating Tests

1. **Isoform-specific knockdown/knockout + flow assay:** SMPD2 vs SMPD3 vs SMPD4 siRNA/CRISPR in endothelial cells, then measure flow/pressure-induced neutral-SMase activity and ceramide. Prediction: loss of SMPD4 (not SMPD2) abolishes caveolar mechanoactivation.
2. **Tagged-protein colocalization with caveolin-1** for each isoform under identical conditions; test caveolar residency of SMPD2 directly.
3. **Antibody validation:** confirm the Bernardo/Czarny antiserum reactivity against recombinant SMPD2, SMPD3, SMPD4 (Western) — establishes which isoform(s) it detects.
4. **Reanalysis of caveolar proteomics** (e.g., luminal EC membrane MS) for SMPD2 vs SMPD4 peptides.

---

## Curation Leads (require curator verification)

- **Action change:** Flag GO:0005901 and GO:0009612 on SMPD2 for **removal / NOT-qualification**, with the fix ideally applied to the rat Smpd2 experimental source so IBA re-propagation self-corrects.
- **Candidate references to verify (exact snippets):**
  - PMID 16517606 — "a peptide sequence derived from a previously purified bovine neutral sphingomyelinase (nSMase) allowed us to identify a cDNA encoding a novel human sphingomyelinase, nSMase3, that shows only a little homology to nSMase1 and -2." → reassigns reagent to SMPD4.
  - PMID 10713073 — "Amino acid sequencing of tryptic peptides showed no apparent homologies of bovine N-SMase to any known protein." → antigen ≠ SMPD2/SMPD3.
  - PMID 12473648 — "primarily in caveolae enriched in sphingomyelin and neutral sphingomyelinase" → origin of caveola/mechano claim, reagent-based.
  - PMID 25168245 — "phosphorylation of nSMase1 (… SMPD2) by … JNK … stimulates ceramide generation and apoptosis" → retain core function.
- **Candidate term relocation (optional):** consider whether caveola/mechanotransduction terms belong on **SMPD4/nSMase3** — but only pending direct isoform-specific evidence; do not auto-transfer.
- **Suggested curator questions:** Is the human SMPD2 IBA the only support for these two terms? Does the rat source annotation cite PMID 12473648? Is there any post-2006 SMPD2-specific caveolar/mechano paper?
- **Suggested experiments:** the discriminating tests above (isoform-resolved knockdown + flow ceramide assay; antibody cross-reactivity panel).

---

---

## Iteration 2 addendum — verification attempts & database checks

- **Full text of PMID 12473648 is not machine-accessible.** JBC and ScienceDirect returned HTTP 403; Europe PMC reports the article as not open access (no PMCID / full-text XML). I therefore **could not independently confirm** the seed's specific claim that its Methods used preimmune serum + antiserum against the Bernardo bovine nSMase and that the Discussion links the detected enzyme to that purified protein. This remains the key knowledge gap. However, WebSearch of the article confirmed it is antibody/immunoblot-based and does **not** molecularly assign the enzyme to a specific SMPD gene, which is consistent with the abstract-level provenance chain.
- **No SMPD2-specific caveolar/mechanotransduction paper found.** Targeted PubMed queries ("SMPD2 nSMase1 caveolae … mechanotransduction/shear stress") returned zero hits — supporting the absence of independent, target-specific caveolar/mechanosensor evidence for SMPD2.
- **UniProt curated database check (computed this run):** gene-name mapping confirmed as distinct genes — O60906=**SMPD2**/nSMase1, Q9NY59=**SMPD3**/nSMase2, Q9NXE4=**SMPD4**/nSMase3. UniProt curated subcellular location for **SMPD2 = "Cell membrane"** (no caveola listed); SMPD3 = Golgi/Cell membrane; SMPD4 = ER/Golgi/nuclear envelope/sarcolemma. So even the reference proteome record does not place SMPD2 in caveolae.
- **Artifacts saved:** `artifacts/evidence_matrix.csv`, `artifacts/go_decision_table.csv` (computed provenance tables).

### Iteration 3 note — antibody-specificity chain tightened
Secondary sourcing of Bernardo et al. 2000 (PMID 10713073) clarifies that its **peptide-specific polyclonal antibody was raised against a p97-derived peptide** and **stained a 97-kDa protein in bovine aortic endothelial cell lysates**; the 46-kDa species is a breakdown product, and the antigen is a single protein. This is decisive for two reasons: (1) the p97 species is precisely the sequence that Krut et al. 2006 (PMID 16517606) used to clone **nSMase3/SMPD4**; and (2) the antibody was validated in **bovine aortic endothelial cells**, the same endothelial system used in the Czarny/Schnitzer mechanotransduction work. Thus, to the extent the caveolar mechano-nSMase was identified immunologically with this reagent lineage, it points to **SMPD4/nSMase3**, not SMPD2. The only residual gap is direct confirmation, from the inaccessible PMID 12473648 full text, that this exact antiserum (vs. a generic activity assay) was the identifying reagent in that paper.

### Provenance / methods note
Literature retrieved via PubMed (abstracts quoted verbatim). Pairwise identity of human SMPD2/SMPD3/SMPD4 (UniProt O60906/Q9NY59/Q9NXE4) computed in-run by a simple Needleman–Wunsch global alignment; the crude match-only scoring inflates the "% over shorter" figure, so only the aligned-identity (~22%) is interpreted, and solely to corroborate the published "little homology" statement. Full text of PMID 12473648 was not machine-readable in this run; the reagent→antigen link is inferred from the abstract-level chain plus the seed, and is flagged as a knowledge gap.


## Artifacts

- [OpenScientist evidence matrix](openscientist_artifacts/artifacts_evidence_matrix.csv)
- [OpenScientist go decision table](openscientist_artifacts/artifacts_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)