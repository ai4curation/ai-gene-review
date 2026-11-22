---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T18:11:28.459971'
end_time: '2026-09-20T18:37:18.476730'
duration_seconds: 1550.02
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: AGO4
  gene_symbol: AGO4
  uniprot_accession: Q9HCK5
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: mrna-destabilization-versus-slicer-loss
  hypothesis_text: Human AGO4 participates in miRNA-mediated gene silencing by mRNA
    destabilization (GO:0035279) and siRNA-mediated gene silencing by mRNA destabilization
    (GO:0090625). Adjudicate each independently. Compare the exact assay scope of
    PMID:15260970 with later experiments including PMID:18771919 and TNRC6-mediated
    decay, distinguishing natural guide-target recruitment from artificial tethering
    sufficiency. Loss of AGO4 slicer catalysis need not exclude deadenylation or other
    recruited decay pathways. Determine whether negative assertions about these broad
    processes are experimentally justified or whether the experiments only exclude
    cleavage.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/AGO4/AGO4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human AGO4 participates in miRNA-mediated gene\
    \ silencing by mRNA destabilization (GO:0035279)\n  and siRNA-mediated gene silencing\
    \ by mRNA destabilization (GO:0090625). Adjudicate each independently.\n  Compare\
    \ the exact assay scope of PMID:15260970 with later experiments including PMID:18771919\
    \ and TNRC6-mediated\n  decay, distinguishing natural guide-target recruitment\
    \ from artificial tethering sufficiency. Loss of\n  AGO4 slicer catalysis need\
    \ not exclude deadenylation or other recruited decay pathways. Determine whether\n\
    \  negative assertions about these broad processes are experimentally justified\
    \ or whether the experiments\n  only exclude cleavage.\nfocus_type: function_assignment\n\
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
citation_count: 7
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: outputs_AGO4_GO_decision_table.csv
  path: openscientist_artifacts/outputs_AGO4_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist AGO4 GO decision table
- filename: outputs_AGO4_evidence_matrix.csv
  path: openscientist_artifacts/outputs_AGO4_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist AGO4 evidence matrix
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
- **Gene directory:** AGO4
- **Gene symbol:** AGO4
- **UniProt accession:** Q9HCK5

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** mrna-destabilization-versus-slicer-loss
- **Source file:** genes/human/AGO4/AGO4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human AGO4 participates in miRNA-mediated gene silencing by mRNA destabilization (GO:0035279) and siRNA-mediated gene silencing by mRNA destabilization (GO:0090625). Adjudicate each independently. Compare the exact assay scope of PMID:15260970 with later experiments including PMID:18771919 and TNRC6-mediated decay, distinguishing natural guide-target recruitment from artificial tethering sufficiency. Loss of AGO4 slicer catalysis need not exclude deadenylation or other recruited decay pathways. Determine whether negative assertions about these broad processes are experimentally justified or whether the experiments only exclude cleavage.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human AGO4 participates in miRNA-mediated gene silencing by mRNA destabilization (GO:0035279)
  and siRNA-mediated gene silencing by mRNA destabilization (GO:0090625). Adjudicate each independently.
  Compare the exact assay scope of PMID:15260970 with later experiments including PMID:18771919 and TNRC6-mediated
  decay, distinguishing natural guide-target recruitment from artificial tethering sufficiency. Loss of
  AGO4 slicer catalysis need not exclude deadenylation or other recruited decay pathways. Determine whether
  negative assertions about these broad processes are experimentally justified or whether the experiments
  only exclude cleavage.
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

# AIGR Gene Hypothesis Deep Research — Final Report

**Target gene:** AGO4 (human) · UniProt **Q9HCK5** · NCBITaxon:9606
**Focus type:** function_assignment
**Hypothesis slug:** mrna-destabilization-versus-slicer-loss
**Source file:** `genes/human/AGO4/AGO4-ai-review.yaml`
**Terms adjudicated:** GO:0035279 (miRNA-mediated gene silencing by mRNA destabilization), GO:0090625 (siRNA-mediated gene silencing by mRNA destabilization)

---

## Summary

The seed hypothesis asks whether human AGO4 should be annotated to **GO:0035279** and **GO:0090625** (miRNA/siRNA-mediated gene silencing *by mRNA destabilization*), and — critically — whether any *negative* assertion against these processes is experimentally justified or whether it merely reflects the exclusion of endonucleolytic cleavage. The investigation returns a clear, curation-actionable answer: **the hypothesis is partially supported, and any strong negative on these two terms sourced to [PMID:15260970](https://pubmed.ncbi.nlm.nih.gov/15260970/) (Meister 2004) is over-strong.** The seed's core logic is correct — *loss of AGO4 slicer catalysis does not exclude deadenylation-dependent mRNA destabilization.*

The pivotal reference used to strip AGO4 of decay activity assayed **only endonucleolytic RISC cleavage**. It concluded that "endonuclease activity is exclusively associated with Ago2," but it never measured deadenylation, decapping, or general mRNA turnover, and the same paper shows AGO4 *does* load miRNAs into functional microRNPs. Later work establishes that AGO4 retains the *capacity* to trigger decay: when tethered, all four human Ago proteins — including AGO4 — recapitulate the two-step (Pan2–Pan3 then Ccr4–Caf1) deadenylation that drives miRNA-mediated decay ([PMID:19838187](https://pubmed.ncbi.nlm.nih.gov/19838187/)), and the non-nucleolytic Agos (AGO1/3/4) direct translational repression ([PMID:18771919](https://pubmed.ncbi.nlm.nih.gov/18771919/)).

Two caveats govern the curation decision. First, the positive AGO4 evidence is **capacity/sufficiency from artificial tethering**, not a demonstrated natural miRNA-guide→endogenous-target decay event attributable specifically to AGO4. Second, the two GO terms are **internally inconsistent**: their names say "destabilization" (the deadenylation branch) but their definition text describes endonucleolytic **cleavage**. This ambiguity — not the biology — is the deciding factor. The defensible negative for AGO4 is at the **molecular-function/slicer level** ("no endonuclease/cleavage"); the two destabilization BP terms should be treated as **non-core/uncertain**, with the already-curated **GO:0006402** (mRNA catabolic process, IDA) and **GO:0035278** (translation inhibition, IDA) as the better-supported homes.

---

## Executive Judgment

**Verdict: Partially supported — the negative assertion is over-strong and should be re-scoped to the slicer molecular function.**

The chain of reasoning:

1. **The keystone reference excludes cleavage only.** [PMID:15260970](https://pubmed.ncbi.nlm.nih.gov/15260970/) (Meister et al., *Mol Cell* 2004) purified FLAG/HA-tagged AGO1–4 microRNPs and assayed endonucleolytic target cleavage plus an siRNA-knockdown reporter. It found cleavage is AGO2-exclusive but is **silent on deadenylation/decay**, while explicitly showing AGO4 loads miRNAs. A broad BP negative sourced to this paper is not experimentally justified.

2. **Slicer loss ≠ decay loss.** [PMID:19838187](https://pubmed.ncbi.nlm.nih.gov/19838187/) shows all four human Ago proteins, including AGO4, recapitulate biphasic deadenylation when tethered — a mechanism of mRNA destabilization that does not require slicing. AGO4 is *sufficient* to recruit the decay machinery.

3. **But the positive is capacity-only.** Tethering demonstrates sufficiency, not natural guide-directed recruitment; paralogs differ quantitatively ([PMID:18771919](https://pubmed.ncbi.nlm.nih.gov/18771919/)). Combined with the ontology-internal cleavage-vs-deadenylation ambiguity, the two destabilization terms cannot carry a confident positive *or* a confident negative for AGO4.

**Most important caveats:** (a) AGO4 positive evidence is sufficiency-level, not demonstrated on endogenous targets; (b) GO:0035279/GO:0090625 definitions describe cleavage while their names/synonyms describe deadenylation, so the "right" answer depends on how the term is read; (c) AGO4 is typically the lowest-abundance, least-active paralog, so strong AGO4-specific positive claims risk paralog over-annotation from AGO2.

**Bottom line for the curator:** Do not carry a blanket NOT-annotation on GO:0035279/GO:0090625 sourced to a slicer-only paper. Place the defensible negative at the **MF level (no slicer/endonuclease activity)**; retain the well-supported **GO:0006402** and **GO:0035278**; treat the two destabilization terms as **non-core/uncertain**.

---

## Key Findings

### Finding 1 — The Meister 2004 assay excludes only slicer cleavage, not mRNA destabilization

[PMID:15260970](https://pubmed.ncbi.nlm.nih.gov/15260970/) (Meister et al., *Mol Cell* 2004) purified FLAG/HA-tagged AGO1–AGO4 microRNPs from human cell lines and assayed two things only: **endonuclease (RISC target-cleavage) activity** and siRNA knockdown with a positive-readout reporter. The central result is that *"endonuclease activity is exclusively associated with Ago2"* and that *"exogenously introduced siRNAs also associate with Ago2 for guiding target RNA cleavage."*

Critically, the **same paper** demonstrates AGO4 is a competent miRNA-loading effector: *"miRNAs are incorporated indiscriminately of their sequence into Ago1 through Ago4 containing microRNPs."* This shows AGO4 forms functional miRNPs — it binds guides and can, in principle, recruit downstream effectors — even though it cannot cleave.

The assay measured **target cleavage only**; it did not measure deadenylation, decapping, or bulk decay. The reference is therefore **silent** on whether AGO4 participates in deadenylation-dependent mRNA destabilization. Using it to justify a broad negative against GO:0035279/GO:0090625 conflates "no cleavage" with "no decay" — an unjustified inferential leap.

### Finding 2 — AGO4 has intrinsic capacity to trigger deadenylation-dependent decay, and non-nucleolytic Agos direct repression

[PMID:19838187](https://pubmed.ncbi.nlm.nih.gov/19838187/) (Chen, Zheng, Xia & Shyu, *Nat Struct Mol Biol* 2009) used transcriptional pulsing with RNA tethering and found *"when tethered to mRNAs, all four human Ago proteins and TNRC6C are each able to recapitulate the two deadenylation steps"* (Pan2–Pan3, then Ccr4–Caf1, followed by Dcp1–Dcp2 decapping). Because AGO4 is one of the four, this directly demonstrates that AGO4 can intrinsically recruit the deadenylation/decay machinery **independent of slicer catalysis.**

Complementing this, [PMID:18771919](https://pubmed.ncbi.nlm.nih.gov/18771919/) (Wu, Fan & Belasco, *Curr Biol* 2008) shows the non-nucleolytic Ago proteins (AGO1/3/4) contribute to on-target silencing through translational repression, noting that *"the four Ago proteins with which siRNAs associate in humans differ significantly in their capacity to direct translational repression."*

**Interpretation and caveat:** these establish **sufficiency** — AGO4 *can* trigger decay/repression when artificially recruited — but not **necessity** or natural guide-directed recruitment to endogenous targets. Tethering bypasses guide:target recognition, and paralogs differ quantitatively. This is precisely why the destabilization terms should be non-core rather than confidently asserted.

### Finding 3 — The two GO destabilization terms are internally inconsistent, and AGO4 is annotated to sibling terms, not the destabilization terms

QuickGO definitions (retrieved 2026) expose an ontology-internal problem:

- **GO:0035279** ("miRNA-mediated gene silencing by mRNA destabilization") has a **definition text describing endonucleolytic cleavage** ("miRNAs direct the cleavage of target mRNAs … near-perfect complementarity … Many plant miRNAs"), yet its **synonyms** include *"gene silencing by mRNA cleavage"* **and** *"miRNA-mediated gene silencing by mRNA deadenylation"* / *"deadenylation involved in gene silencing by miRNA."*
- **GO:0090625** is analogously defined by siRNA-directed **cleavage** while named "by mRNA destabilization."
- Both are the named sibling of **GO:0035278** ("miRNA-mediated gene silencing by inhibition of translation").

This is curation-critical: read through the cleavage-flavored definition, an AGO4 NOT could seem justified (AGO4 can't cleave); read through the deadenylation synonyms, AGO4 arguably *qualifies* (AGO4 can deadenylate when tethered). The term is not clean enough to carry a confident positive or negative for AGO4.

**Current UniProt annotation set for Q9HCK5:**

| GO ID | Term | Aspect | Evidence |
|---|---|---|---|
| GO:0035278 | miRNA silencing by inhibition of translation | BP | IDA |
| GO:0006402 | mRNA catabolic process | BP | IDA |
| GO:0035198 | miRNA binding | MF | IDA |
| GO:0016442 | RISC complex | CC | IDA |
| GO:0035194 | post-transcriptional gene silencing by RNA | BP | IBA |
| GO:0035279 | miRNA silencing **by mRNA destabilization** | BP | **absent** |
| GO:0090625 | siRNA silencing **by mRNA destabilization** | BP | **absent** |

AGO4 is **not** annotated to the destabilization terms; it is annotated to their siblings (translation inhibition and general mRNA catabolic process) — consistent with treating the destabilization terms as non-core.

### Finding 4 — UniProt already scopes AGO4's negative to the endonuclease/cleavage molecular function

The UniProt Q9HCK5 FUNCTION comment reads: *"Required for RNA-mediated gene silencing (RNAi). Binds to short RNAs such as microRNAs (miRNAs) and represses the translation of mRNAs which are complementary to them. **Lacks endonuclease activity and does not appear to cleave target mRNAs.**"*

The **only** explicit negative curators recorded is at the **molecular-function/cleavage level**. There is **no** curated negative about deadenylation or destabilization. No catalytic active-site residues are feature-annotated for AGO4 (only PDB-derived secondary-structure features are present), consistent with catalytic degeneration of the PIWI slicer site. This independent, expert-curated scoping reinforces the central recommendation: **the negative belongs at the slicer MF, not on the destabilization BP terms.**

---

## Mechanistic Model / Interpretation

The confusion in the seed hypothesis is a conflation of two mechanistically separable silencing routes that both fall under "mRNA destabilization":

```
                     AGO4-loaded miRNP (guide bound; PMID:15260970 confirms loading)
                                    │
                    ┌───────────────┴────────────────┐
                    ▼                                 ▼
        (A) ENDONUCLEOLYTIC CLEAVAGE        (B) DEADENYLATION-DEPENDENT DECAY
            "slicer" / RISC activity            via TNRC6 → CCR4-NOT / PAN2-3
                    │                                 │
        Requires intact PIWI catalytic       Requires guide/target binding +
        tetrad (DEDH)                        effector (TNRC6) recruitment
                    │                                 │
        AGO4: ABSENT                         AGO4: CAPABLE (when tethered)
        (PMID:15260970; UniProt "lacks       (PMID:19838187 — all 4 Agos
         endonuclease activity")             recapitulate 2 deadenylation steps)
                    │                                 │
                    ▼                                 ▼
        Justified NOT at slicer MF          NOT justified as a broad negative;
        (endonuclease/cleavage MF)          sufficiency shown, natural-target
                                            decay NOT demonstrated → NON-CORE
```

**Route (A)** — endonucleolytic cleavage — is genuinely absent in AGO4. This is what PMID:15260970 tested and what UniProt codifies; a NOT restricted to the endonuclease/slicer MF is defensible.

**Route (B)** — deadenylation/decay via TNRC6 → CCR4-NOT — does **not** require slicer catalysis. Tethering shows AGO4 is *capable* of triggering it. The destabilization terms semantically span both routes because of their inconsistent definition/synonym structure. AGO4 is negative for the cleavage flavor and *capacity-positive* (but not physiologically demonstrated) for the deadenylation flavor. This mixed status is exactly why the terms should be **non-core/uncertain**.

The **well-supported** homes for AGO4's silencing activity are the sibling terms already held by IDA: **GO:0035278** and **GO:0006402**. These capture AGO4's demonstrated repression/decay contribution without overcommitting to the mechanistically ambiguous destabilization terms.

---

## Evidence Base

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID:15260970](https://pubmed.ncbi.nlm.nih.gov/15260970/) (Meister 2004) | Direct assay — RISC endonuclease + reporter | Qualifies; refutes **cleavage** only | Do AGO1–4 slice? Do they bind miRNAs? | "Endonuclease activity is exclusively associated with Ago2"; "miRNAs are incorporated indiscriminately … into Ago1 through Ago4 containing microRNPs" | Human cell lines; FLAG/HA-AGO IP + cleavage reporter | High for excluding AGO4 slicing; **silent on deadenylation/decay** |
| [PMID:19838187](https://pubmed.ncbi.nlm.nih.gov/19838187/) (Chen & Shyu 2009) | Direct assay — tethering + transcriptional pulsing | **Supports (capacity)** | Can Agos trigger deadenylation without slicing? | "When tethered to mRNAs, all four human Ago proteins and TNRC6C are each able to recapitulate the two deadenylation steps" | Mammalian cells; λN/BoxB tethering | High that AGO4 is **sufficient**; tethering ≠ natural recruitment |
| [PMID:18771919](https://pubmed.ncbi.nlm.nih.gov/18771919/) (Wu, Fan & Belasco 2008) | Direct assay — on-target siRNA reporters | Supports / qualifies | Do non-nucleolytic Agos silence beyond cleavage? | AGO1/3/4 direct translational repression; "the four Ago proteins … differ significantly in their capacity" | Human cells | Moderate; quantitative paralog differences weaken AGO4-specific strength |
| UniProt Q9HCK5 FUNCTION | Review / database | Qualifies (scopes the negative) | Where do curators place AGO4's negative? | "Lacks endonuclease activity and does not appear to cleave target mRNAs"; represses translation | Curated, human | Database-level; confirms negative is at cleavage MF, not decay BP |
| QuickGO GO:0035279 / GO:0090625 | Review / database | Competing / qualifies | Are the destabilization terms clean? | Definitions describe cleavage; synonyms include deadenylation → internally inconsistent | Ontology | Structural ambiguity makes confident positive or negative unsafe |
| [PMID:29040713](https://pubmed.ncbi.nlm.nih.gov/29040713/) (AGO3 slicer) | Structural / biochemical | Context | Do non-AGO2 paralogs retain catalysis? | AGO3 slices guide-dependently; AGO4 remains slicer-independent | Recombinant human Agos | Confirms AGO4 stays in the slicer-independent class |
| [PMID:22863743](https://pubmed.ncbi.nlm.nih.gov/22863743/) (Ago4-KO mouse) | Mutant phenotype | Context | Does AGO4 have specialized in vivo roles? | AGO4 controls meiotic entry and MSCI; nuclear localization in spermatocytes | Mouse germline | Organism/context-specific; not a decay-vs-cleavage discriminator |

Additional orienting literature: [PMID:21984184](https://pubmed.ncbi.nlm.nih.gov/21984184/) (GW182/TNRC6 recruits CCR4–NOT via W-motifs — mechanistic basis for the Ago→TNRC6→deadenylation route AGO4 can engage) and [PMID:33122430](https://pubmed.ncbi.nlm.nih.gov/33122430/) (AGO2/AGO3 activated by different guide lengths — cautions against blanket "non-AGO2 = inactive" statements).

---

## GO Curation Implications

Adjudicating **each term independently** (both resolve the same way):

- **GO:0035279 (miRNA silencing by mRNA destabilization) — BP.** *Lead:* do not assert a strong NOT based on PMID:15260970; treat as **non-core / uncertain**. A positive is supportable only at **capacity level** (tethering, PMID:19838187) and would require an ISS/IC or IBA-by-redundancy justification with an explicit note — never IDA-on-natural-target.
- **GO:0090625 (siRNA silencing by mRNA destabilization) — BP.** *Lead:* same. Extra wrinkle: canonical siRNA on-target "destabilization" *is* endonucleolytic cleavage, which is AGO2-specific; AGO4 lacks slicing. AGO4's contribution is the **decay branch**, again capacity-level.
- **GO:0006402 (mRNA catabolic process) — BP — RETAIN.** Already IDA; a more defensible home for AGO4's decay involvement than the destabilization terms.
- **GO:0035278 (miRNA silencing by inhibition of translation) — BP — RETAIN.** Sibling term, already IDA; consistent with Wu/Belasco.
- **Slicer / endoribonuclease-mediated cleavage — MF — negative JUSTIFIED.** PMID:15260970 + UniProt directly support that AGO4 lacks slicer activity. If a NOT is desired, place it here (MF), not on the broad BP destabilization terms.

Avoid "protein binding" as a recommendation — the informative content is the **RISC/TNRC6→CCR4–NOT decay axis** and the **slicer-negative MF**, both captured above.

**GO decision summary:**

| Term | Aspect | Current status | Recommended action | Rationale |
|---|---|---|---|---|
| Endonuclease/slicer cleavage | MF | Implicit negative | **Retain NOT here** | PMID:15260970 + UniProt directly support |
| GO:0035279 | BP | Absent | **No strong positive; no broad NOT** | Term ambiguous; only capacity shown |
| GO:0090625 | BP | Absent | **Same as above** | Term ambiguous; only capacity shown |
| GO:0035278 | BP | IDA | **Retain** | Directly supported |
| GO:0006402 | BP | IDA | **Retain** | Best-supported decay home |
| GO:0035198 | MF | IDA | **Retain** | Core function (avoid "protein binding") |
| GO:0016442 | CC | IDA | **Retain** | Core localization |

---

## Mechanistic Scope

- **Immediate molecular activity being tested:** AGO4 as the small-RNA–binding core of RISC, with two separable outputs — (i) endonucleolytic target cleavage (slicer MF), which AGO4 lacks; (ii) recruitment of TNRC6/GW182 → CCR4–NOT (Ccr4–Caf1) and Pan2–Pan3 deadenylases → decapping/decay, for which AGO4 is *sufficient* when tethered.
- **Direct gene-product activity:** miRNA/RNA binding (GO:0035198, IDA), RISC complex membership (GO:0016442, IDA), and (by tethering) recruitment of the deadenylation machinery.
- **Downstream / inferred (not a direct MF of AGO4):** actual half-life reduction of endogenous targets under natural guide-directed recruitment; meiotic/germline phenotypes (mouse *Ago4⁻/⁻*, PMID:22863743 — a loss-of-function developmental phenotype, not evidence of the destabilization MF); any organismal silencing outcome.

The key discipline: **loss of cleavage (a direct activity) has been over-generalized to loss of destabilization (a broader pathway outcome).** These are separable, and the evidence separates them.

---

## Conflicts and Alternatives

1. **GO ontology inconsistency (primary conflict).** The term *definition* (cleavage, "many plant miRNAs") conflicts with the term *name/synonyms* (deadenylation). A curator reading the definition literally could justify the negative; reading the name could not. This is a database/ontology artifact, not a biological disagreement.
2. **Tethering sufficiency ≠ natural recruitment.** PMID:19838187 uses artificial tethering; it proves capacity, not that endogenous AGO4-loaded miRNAs destabilize natural targets. This is exactly the distinction the seed asked to preserve.
3. **Paralog quantitative differences.** PMID:18771919 stresses the four Agos "differ significantly." AGO4 is typically the lowest-abundance, least-active paralog; strong AGO4-specific positive claims risk paralog over-annotation carried from AGO2.
4. **siRNA-specific caveat.** For siRNA "on-target" silencing, the destabilization-by-cleavage route is AGO2's; assigning GO:0090625 (if read as cleavage) to AGO4 would be paralog over-annotation.
5. **Paralog catalytic re-evaluation.** AGO3 was later shown to slice guide-dependently ([PMID:29040713](https://pubmed.ncbi.nlm.nih.gov/29040713/)). This does not rehabilitate AGO4 as a slicer, but it cautions against blanket "non-AGO2 = inactive" statements — favoring conservative, mechanism-specific scoping.
6. **Database concordance.** UniProt curators already scope the negative to cleavage MF and place AGO4's positive role in translational repression, independently supporting re-scoping any NOT to the slicer MF.

---

## Limitations and Knowledge Gaps

This report is literature/annotation-based (no gene-specific dataset was supplied). Public resources used: NCBI abstracts, EBI QuickGO term definitions/synonyms, and UniProt Q9HCK5 annotations. Positive AGO4 evidence is capacity/sufficiency-level; no primary study demonstrating endogenous AGO4-guided natural-target destabilization was located.

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No demonstration of **endogenous AGO4-guide → natural-target deadenylation/decay** | Meister (cleavage only), Chen/Shyu (tethering), Wu/Belasco (reporters) | Distinguishes IDA-worthy natural process from capacity/sufficiency | AGO4-selective (AGO2-null) cells + AGO4-eCLIP + target half-life/poly(A) profiling |
| **Term meaning** intended by the ontology | QuickGO definition + synonyms | Determines whether the negative is defensible | GO editorial clarification / mapping to the deadenylation branch |
| AGO4 **catalytic residues** (tetrad retained but inactive?) | UniProt features: no catalytic active-site annotated | Supports the MF-level negative mechanistically | PIWI DEDH tetrad alignment vs AGO2; direct AGO4 slicer assay (as for AGO3) |
| AGO4 **abundance/context** in tested systems | Wu/Belasco note cell-type-dependent Ago distribution | Affects whether AGO4 contributes meaningfully in vivo | Quantitative proteomics of RISC composition per tissue |

---

## Discriminating Tests

1. **AGO4-only rescue in an AGO-null background** (AGO1/2/3 knockout or AGO2-null) with a natural miRNA target reporter: measure poly(A) shortening and decay vs. translation block → separates destabilization from translational repression for AGO4 specifically.
2. **AGO4 eCLIP + transcriptome decay** (SLAM-seq/BRIC-seq half-life) in cells where AGO4 is the dominant loaded Argonaute → tests natural guide-target recruitment leading to decay.
3. **TNRC6-interaction-deficient AGO4 mutant** (disrupt the PIWI Trp-binding pockets analogous to AGO2 F470/F505) in tethering and natural-target assays → tests TNRC6/CCR4–NOT dependence of AGO4 destabilization.
4. **Direct AGO4 slicer assay** with guide-length variants (as for AGO3, PMID:29040713) → confirms/refutes the MF-level negative.
5. **Ontology adjudication** — file a GO clarification request to disambiguate GO:0035279/GO:0090625 (cleavage vs. deadenylation) before committing any positive/negative annotation.

---

## Proposed Follow-up Actions (Curation Leads — require curator verification)

- **Action change:** Replace/avoid any blanket NOT-annotation on **GO:0035279** and **GO:0090625** citing **PMID:15260970**; that reference supports only a **slicer/cleavage (MF)** negative. Re-scope the negative to MF.
- **Candidate references + exact snippets to verify:**
  - PMID:15260970 — *"endonuclease activity is exclusively associated with Ago2"* (supports MF-negative); *"miRNAs are incorporated indiscriminately of their sequence into Ago1 through Ago4 containing microRNPs"* (AGO4 loads guides).
  - PMID:19838187 — *"When tethered to mRNAs, all four human Ago proteins and TNRC6C are each able to recapitulate the two deadenylation steps."* (AGO4 decay capacity).
  - PMID:18771919 — *"the four Ago proteins with which siRNAs associate in humans differ significantly in their capacity to direct translational repression."* (non-nucleolytic Agos silence; paralog differences).
- **Candidate GO handling:** Retain **GO:0006402 (mRNA catabolic process, IDA)** and **GO:0035278 (IDA)**; treat **GO:0035279/GO:0090625** as **non-core/uncertain**, annotating only with a capacity/redundancy caveat (ISS/IC or IBA), never as IDA on a natural target. Keep **GO:0035198** and **GO:0016442**; avoid falling back to "protein binding."
- **Suggested curator questions:** (1) Is the intended meaning of GO:0035279/0090625 the cleavage branch or the deadenylation branch? (2) Should AGO4's tethering-based decay capacity be captured by GO:0006402 rather than the destabilization terms? (3) Is a NOT-annotation intended at MF (slicer) rather than BP?
- **Suggested experiments:** the five discriminating tests above.

---

*Prepared for AI Gene Review curator adjudication. All annotation recommendations are leads requiring curator verification. Positive AGO4 destabilization evidence is capacity/sufficiency-level; the defensible negative is at the slicer molecular function only.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist AGO4 GO decision table](openscientist_artifacts/outputs_AGO4_GO_decision_table.csv)
- [OpenScientist AGO4 evidence matrix](openscientist_artifacts/outputs_AGO4_evidence_matrix.csv)