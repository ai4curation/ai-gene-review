---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:40:32.603642'
end_time: '2026-10-24T05:27:24.158619'
duration_seconds: 2811.56
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ECOLI
  gene: traB
  gene_symbol: traB
  uniprot_accession: P41067
  taxon_id: NCBITaxon:83333
  taxon_label: Escherichia coli K-12
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0016887
  hypothesis_text: traB has ATP hydrolysis activity (GO:0016887).
  term_context: '- Term: ATP hydrolysis activity (GO:0016887)

    - Evidence type: IDA

    - Original reference: PMID:20172994'
  reference_context: '- PMID:20172994'
  source_file: genes/ECOLI/traB/traB-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0016887\n  label: ATP hydrolysis activity\n\
    evidence_type: IDA\noriginal_reference_id: PMID:20172994"
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
citation_count: 2
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

- **Organism code:** ECOLI
- **Taxon:** Escherichia coli K-12 (NCBITaxon:83333)
- **Gene directory:** traB
- **Gene symbol:** traB
- **UniProt accession:** P41067

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016887
- **Source file:** genes/ECOLI/traB/traB-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

traB has ATP hydrolysis activity (GO:0016887).

## Term and Decision Context

- Term: ATP hydrolysis activity (GO:0016887)
- Evidence type: IDA
- Original reference: PMID:20172994

## Reference Context

- PMID:20172994

## Source Context YAML

```yaml
term:
  id: GO:0016887
  label: ATP hydrolysis activity
evidence_type: IDA
original_reference_id: PMID:20172994
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

# AIGR Deep Research Report: ATP Hydrolysis Activity (GO:0016887) on F-plasmid TraB (P41067)

**Gene:** traB (ECOLI) · **UniProt:** P41067 (TRAB1_ECOLI) · **Organism:** *Escherichia coli* K-12 (NCBITaxon:83333)
**Focus type:** function_assignment · **Seed hypothesis:** *traB has ATP hydrolysis activity (GO:0016887)*
**Term under review:** GO:0016887 (ATP hydrolysis activity), evidence IDA, original reference [PMID:20172994](https://pubmed.ncbi.nlm.nih.gov/20172994/)

---

## Summary

**The GO:0016887 "ATP hydrolysis activity" annotation on P41067 is REFUTED as an over-annotation caused by a TraB name collision.** The seed hypothesis — that the F-plasmid conjugation protein TraB (P41067) directly catalyzes ATP hydrolysis — is not supported by any direct evidence pertaining to this protein. Instead, the annotation traces to a conflation of two unrelated conjugation proteins that happen to share the colloquial name "TraB."

P41067 (TRAB1_ECOLI, 475 aa) is the *F-plasmid* TraB, a member of the **VirB10/TraB/TrbI family** (Pfam PF03743 "TrbI", InterPro IPR005498). This family is the non-catalytic, envelope-spanning **structural scaffold** of the type IV secretion system (T4SS). Its UniProt-curated function is "Involved in F pilus assembly," and its sequence contains **no Walker-A / P-loop motif** (GxxxxGK[S/T]) — the diagnostic signature required for ATP hydrolysis. By contrast, the IDA reference [PMID:20172994](https://pubmed.ncbi.nlm.nih.gov/20172994/) is explicitly titled *"Biochemical dissection of the ATPase TraB, the VirB4 homologue of the Escherichia coli pKM101 conjugation machinery."* That paper assayed a **different protein**: the ~866-aa **VirB4-family** TraB of plasmid pKM101 (UniProt Q46698), a bona-fide P-loop ATPase with a canonical Walker-A motif (GMSGEGKT, ~residue 498).

The two "TraB" proteins differ in essentially every discriminating feature — length (475 vs 866 aa), domain family (VirB10 scaffold vs VirB4 ATPase), presence of nucleotide-binding motifs (absent vs present), and documented biochemical role (structural vs catalytic). Independent primary evidence ([PMID:11722740](https://pubmed.ncbi.nlm.nih.gov/11722740/)) confirms that the F-plasmid TraB is an inner-membrane structural component of the envelope-spanning TraV–TraK–TraB complex, with no catalytic activity demonstrated. The only GO:0016887 annotation on P41067 is a single IDA:CACAO community-curation entry, the typical vector for name-collision propagation. **Recommended curation action: remove GO:0016887 from P41067 (optionally re-home the evidence to Q46698), pending curator verification.**

---

## Executive Judgment

**Verdict: REFUTED (over-annotation via name collision).**

The ATP-hydrolysis evidence is real, but it belongs to the pKM101 VirB4-TraB (Q46698), **not** to the F-plasmid VirB10-TraB (P41067). The refutation rests on four convergent, orthogonal lines of evidence:

1. **The IDA reference assayed a different protein.** PMID:20172994 characterizes the VirB4 homologue TraB of pKM101 (~866 aa), explicitly named as "the ATPase TraB."
2. **Domain family is non-catalytic.** P41067 is VirB10/TraB/TrbI (PF03743, IPR005498) — a structural T4SS scaffold family, not a VirB4/VirB11/VirD4 ATPase family.
3. **No catalytic apparatus.** P41067 lacks a Walker-A / P-loop motif; ATP hydrolysis is mechanistically impossible without a nucleotide-binding fold.
4. **Positive alternative function.** PMID:11722740 shows P41067 is an inner-membrane structural component of the TraV–TraK–TraB complex — the canonical VirB10 scaffold role.

**Most important caveat:** This is a high-confidence refutation of the *attribution*. Confirmation of the exact UniProt accession assayed in PMID:20172994 (inferred to be Q46698) from the paper's full-text methods would fully close the loop before the IDA is re-homed.

---

## Key Findings

### Finding 1 — The GO:0016887 IDA on P41067 is a TraB name-collision mis-annotation

P41067 (TRAB1_ECOLI, 475 aa) is the F-plasmid "Protein TraB." Its UniProt-curated molecular function is *"Involved in F pilus assembly,"* and its domain architecture places it unambiguously in a **structural**, not catalytic, protein family: Pfam **PF03743 (TrbI)** and InterPro **IPR005498** ("Type IV secretion system VirB10/TraB/TrbI family"). The VirB10/TraB/TrbI family forms the inner-membrane, envelope-spanning scaffold of the T4SS core complex. It is energized by — but does not itself perform — ATP hydrolysis.

Critically, **P41067's sequence contains no Walker-A (P-loop) motif** (GxxxxGK[S/T]), the diagnostic nucleotide-binding signature of ATPases. A protein lacking a P-loop cannot be assumed to hydrolyze ATP, and VirB10-family members are canonically non-catalytic.

The only GO:0016887 annotation on P41067 is a single **IDA:CACAO** community-curation entry. Its cited primary reference, [PMID:20172994](https://pubmed.ncbi.nlm.nih.gov/20172994/) (Durand, Oomen & Waksman, 2010), explicitly characterizes *"the ATPase TraB, the VirB4 homologue of the E. coli pKM101 conjugation machinery."* That protein is in the **VirB4 family** (not VirB10), is **~866 aa** (not 475 aa), and corresponds to **UniProt Q46698** (Q46698_ECOLX) — not P41067. Every discriminating feature indicates the ATP-hydrolysis evidence describes the **pKM101 VirB4-TraB**, not the **F-plasmid VirB10-TraB P41067**. The two proteins share only the colloquial label "TraB," a conjugation-gene name reused across independent plasmid transfer systems. Notably, in the F system the VirB4 ATPase role is filled by a differently named protein (TraC), while "TraB" denotes the VirB10 scaffold — the inverse of the pKM101 nomenclature, which is precisely how the cross-assignment error occurred.

### Finding 2 — F-plasmid TraB (P41067) is an inner-membrane structural scaffold, not an ATPase

Independent primary literature corroborates the structural (non-catalytic) role of P41067. [PMID:11722740](https://pubmed.ncbi.nlm.nih.gov/11722740/) (Harris, Hombs & Silverman, 2001) used yeast two-hybrid interaction mapping and membrane fractionation to show that F-plasmid TraB is an **inner-membrane protein** that assembles with **TraK (periplasm)** and **TraV (outer-membrane lipoprotein)** into an **envelope-spanning TraV–TraK–TraB complex.** The authors state directly that *"TraV, TraK and TraB form a complex in Escherichia coli that spans the cell envelope from the outer membrane (TraV) through the periplasm (TraK) to the inner membrane (TraB)."*

TraB fractionates with the inner membrane, and the assembled complex bridges outer membrane → periplasm → inner membrane. This is precisely the **canonical VirB10-family structural/scaffolding role**, consistent with P41067's Pfam PF03743 / InterPro IPR005498 assignment. No catalytic or ATP-hydrolysis activity is demonstrated or implied for TraB in this work.

Combined with the **absence of any P-loop/Walker-A motif** in P41067 (475 aa) versus the genuine VirB4-TraB ATPase of pKM101 (Q46698; ~866 aa; P-loop NTPase with Walker-A motif GMSGEGKT near residue 498 — the protein actually assayed in PMID:20172994), this independently confirms that the GO:0016887 IDA on P41067 is a mis-assignment. Two orthogonal lines of evidence — domain-family/sequence analysis and direct biochemical/cell-biological characterization — converge on the same conclusion.

---

## Mechanistic Model / Interpretation

### The two "TraB" proteins

The core of this review is distinguishing two proteins that share a name but nothing else functionally important:

| Feature | **F-plasmid TraB (P41067)** — *annotated* | **pKM101 TraB (Q46698)** — *assayed in IDA ref* |
|---|---|---|
| UniProt | P41067 (TRAB1_ECOLI) | Q46698 (Q46698_ECOLX) |
| Length | 475 aa | ~866 aa |
| Family | VirB10 / TraB / TrbI | VirB4 |
| Pfam | PF03743 (TrbI) | PF03135 (CagE/TrbE/VirB4) |
| InterPro | IPR005498 (VirB10/TraB/TrbI, **structural**) | IPR027417 (P-loop NTPase) + IPR004346 (VirB4_CagE) |
| Walker-A (P-loop) | **Absent** | **Present** (GMSGEGKT, ~res 498) |
| Function | Inner-membrane **structural scaffold** | **ATPase** (energizer of T4SS) |
| Curated role | F pilus assembly; TraV–TraK–TraB complex | ATP hydrolysis driving conjugation |
| Primary evidence | PMID:11722740 (structure/localization) | PMID:20172994 (biochemical ATPase assay) |

### Where each protein sits in the conjugation machine

```
            F-plasmid T4SS (schematic)                 ATP energizer (separate protein family)

   OUTER MEMBRANE   ── TraV (OM lipoprotein) ──┐
                                               │        VirB4-type ATPase
   PERIPLASM        ── TraK (periplasm) ───────┤  <---  (e.g. pKM101 TraB / Q46698)
                                               │        P-loop NTPase; binds + hydrolyzes ATP
   INNER MEMBRANE   ── TraB (P41067) ──────────┘        → GO:0016887 belongs HERE
                      VirB10-family scaffold
                      NON-catalytic; no Walker-A
                      → GO:0016887 does NOT belong here
```

The F-plasmid TraB (P41067) is the **VirB10-family channel/scaffold** component that physically couples the outer-membrane and periplasmic subassemblies to the inner membrane. In T4SS architecture the ATP-hydrolyzing engines are the **VirB4, VirB11, and VirD4** family NTPases — distinct proteins bearing P-loop motifs. The energy-providing ATPase role and the structural scaffold role are performed by **different proteins**. The IDA annotation conflated the two because the pKM101 VirB4 homologue is also named "TraB."

### Why the mis-annotation is mechanistically implausible

ATP hydrolysis requires a nucleotide-binding fold — minimally a Walker-A/P-loop (GxxxxGK[S/T]) and usually a Walker-B motif. P41067 has neither. VirB10-family proteins are not NTPases; they respond to ATP binding/hydrolysis by *other* T4SS components (conformational "energy sensing") but do not catalyze the reaction themselves. Assigning a direct catalytic MF term to a scaffold protein lacking the catalytic apparatus is biochemically unsupportable.

---

## Evidence Base

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | [PMID:20172994](https://pubmed.ncbi.nlm.nih.gov/20172994/) (Durand 2010) | Direct assay (IDA) | **Competing / mis-attributed** | TraB hydrolyzes ATP | Soluble **pKM101 TraB** (VirB4 homolog, ~866 aa) is the characterized ATPase | *E. coli* pKM101 T4SS; purified protein in vitro | High for the VirB4-TraB; but that protein is 866 aa, Q46698 — NOT P41067 |
| 2 | UniProt P41067 (TRAB1_ECOLI) | Review/database | **Refutes** | P41067 is an ATPase | Curated function = *"Involved in F pilus assembly"*; no catalytic/EC annotation | F plasmid, *E. coli* K-12 | High; curated record |
| 3 | Pfam PF03743 / InterPro IPR005498 | Structural/evolutionary | **Refutes** | P41067 belongs to an ATPase family | Assigned to **VirB10/TraB/TrbI**, a structural T4SS core family | T4SS, multiple organisms | High; domain assignment |
| 4 | Sequence motif scan | Computational | **Refutes** | P41067 has a nucleotide-binding motif | **No Walker-A (GxxxxGK[S/T]) motif** in the 475-aa sequence | Direct scan of P41067 | Medium-high; absence of canonical P-loop is strong |
| 5 | UniProt search (pKM101 TraB) | Computational/database | **Qualifies** | Which TraB the paper studied | pKM101/VirB4 "TraB" = **Q46698_ECOLX, 866 aa**, distinct accession | T4SS ATPase | High; length and family match VirB4 |
| 6 | [PMID:11722740](https://pubmed.ncbi.nlm.nih.gov/11722740/) (Harris 2001) | Interaction + localization | **Refutes (positive alt.)** | What P41067 does | F TraB is an **inner-membrane** protein forming the **envelope-spanning TraV–TraK–TraB complex** — a scaffold; no catalytic activity | *E. coli*, F plasmid; Y2H + fractionation | High; primary structural evidence |
| 7 | GO annotation provenance | Database | **Qualifies** | Reliability of the IDA | Sole GO:0016887 support is **IDA:CACAO** (community annotation), a known error source | — | Supports mis-annotation interpretation |

**Literature detail:**

- *[PMID:20172994](https://pubmed.ncbi.nlm.nih.gov/20172994/) — Biochemical dissection of the ATPase TraB, the VirB4 homologue of the Escherichia coli pKM101 conjugation machinery* (Durand, Oomen & Waksman, 2010). The original IDA reference. It characterizes the **pKM101 VirB4-TraB ATPase (Q46698)** — a different protein from P41067. This establishes the name-collision mis-attribution: the real ATP-hydrolysis evidence belongs to a VirB4 homologue, not to the F-plasmid VirB10-family TraB.

- *[PMID:11722740](https://pubmed.ncbi.nlm.nih.gov/11722740/) — Evidence that F-plasmid proteins TraV, TraK and TraB assemble into an envelope-spanning structure in Escherichia coli* (Harris, Hombs & Silverman, 2001). Primary evidence that **F-plasmid TraB (P41067)** is an inner-membrane **structural scaffold** in the TraV–TraK–TraB complex — consistent with the VirB10 family and inconsistent with intrinsic ATPase activity.

---

## GO Curation Implications

**Likely curation action (lead requiring curator verification):**

- **Remove GO:0016887 (ATP hydrolysis activity, MF) from P41067.** The IDA evidence does not describe this protein; it describes the pKM101 VirB4 homologue (Q46698). The annotation is an over-annotation produced by a name collision.
- **Optionally re-home the GO:0016887 IDA to UniProt Q46698** (the pKM101 VirB4-TraB), where PMID:20172994 provides direct biochemical support. This requires curator confirmation of the exact accession assayed.

**On retaining vs removing / generalizing:**

- The term should **not be retained** on P41067 — it is not merely too broad or too specific; it attributes the wrong molecular activity entirely.
- No more general ATPase term is warranted, because P41067 lacks the catalytic apparatus for any ATP-hydrolysis function.

**More informative terms that ARE supported for P41067 (candidate replacements / additions):**

- **CC:** inner (plasma) membrane localization (supported by PMID:11722740 fractionation); component of a conjugative T4SS / pilus-assembly complex.
- **BP:** conjugation / pilus assembly (supported by UniProt curated function "Involved in F pilus assembly" and the TraV–TraK–TraB complex role).
- **MF/CC:** structural constituent of a type IV secretion / conjugative transfer complex. (Prefer a specific T4SS-structural term over the uninformative "protein binding.")

These structural/BP terms, not GO:0016887, represent P41067's primary function.

---

## Mechanistic Scope

**Immediate molecular function being tested:** direct catalysis of ATP → ADP + Pi (ATP hydrolysis activity, GO:0016887) by the P41067 gene product.

**Direct gene-product activity (P41067):** inner-membrane structural scaffolding within the F-plasmid conjugation (T4SS) apparatus; assembly into the envelope-spanning TraV–TraK–TraB complex; contribution to F pilus biogenesis. These are structural and complex-formation activities — **not** catalytic.

**Separated downstream/contextual effects (not direct MF of P41067):** conjugative DNA transfer and pilus elaboration are **pathway-level consequences** of the assembled machine, powered by *separate* VirB4/VirB11/VirD4-type ATPases. The ATP-hydrolysis step is a property of those energizer proteins. Attributing GO:0016887 to P41067 confuses a system-level energetic requirement (the machine consumes ATP) with the specific enzyme that performs the reaction.

---

## Conflicts and Alternatives

- **Paralog / name confusion (primary issue):** "TraB" is reused across independent conjugation systems. The F-plasmid TraB (VirB10 family, P41067) and the pKM101 TraB (VirB4 family, Q46698) are **non-orthologous** proteins sharing a name. In F the VirB4 ATPase is named TraC; in pKM101 it is named TraB — the inverse nomenclature that drove the error.
- **Organism/plasmid-specific differences:** both are in *E. coli*, but on different plasmids (F vs pKM101). The organism match (ECOLI) likely facilitated the erroneous cross-assignment.
- **In vitro-only activity vs wrong protein:** the issue is not that the assay was in vitro — it is that the assay was on a *different protein*. The biochemistry in PMID:20172994 is valid; the accession linkage is wrong.
- **Database carry-over:** the single IDA:CACAO source suggests a community-curation entry keyed on gene symbol ("TraB") + organism rather than exact accession — a classic name-collision vector.
- **No competing evidence for P41067 ATPase:** no primary study was found demonstrating intrinsic ATP hydrolysis by the F-plasmid TraB. The absence of a P-loop motif makes any such claim mechanistically unlikely.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Exact accession assayed in PMID:20172994 | Title/abstract establish VirB4 homolog, pKM101; inferred Q46698 from UniProt | Re-homing the IDA requires the precise accession for the pKM101 TraB construct | Read the full methods/materials of PMID:20172994 for the exact construct/accession |
| Provenance of the CACAO IDA entry | Identified as sole GO:0016887 source on P41067 | Confirms whether the error originated in community curation keyed on gene symbol | Inspect the GO annotation record / CACAO submission linking PMID:20172994 to P41067 |
| Direct experimental test of P41067 ATPase | No primary study found; motif absent | A definitive negative would fully close the case | Purify P41067; malachite-green/coupled ATPase assay (expected: no activity) |
| Walker-A scan reproducibility | Motif reported absent in P41067; present in Q46698 | The sequence argument underpins the refutation | Re-run an explicit P-loop regex / HMMER P-loop NTPase scan on both sequences as saved provenance |
| Structural confirmation | Family assignment via Pfam/InterPro | A structure/AlphaFold model would visually confirm scaffold vs NTPase fold | Compare AlphaFold models of P41067 (VirB10 fold) vs Q46698 (RecA-like NTPase fold) |

**Methodological note:** The sequence/motif and domain-family statements rest on database annotations (UniProt, Pfam, InterPro) and a Walker-A regex scan summarized in the investigation. Where a specific computational scan (e.g., HMMER P-loop detection) would strengthen provenance, it is listed above as a follow-up to run and save as an executable artifact; it should not be presented as a re-read of the PMID:20172994 methods.

---

## Discriminating Tests

1. **Accession verification (fastest, highest value):** confirm from the PMID:20172994 full text that the assayed "TraB" is the pKM101 VirB4 homologue (Q46698), not P41067. This single check settles the curation decision.
2. **Explicit P-loop/Walker-A HMMER scan:** run the P-loop_NTPase Pfam profile against P41067 and Q46698; expect a hit only for Q46698. Save code + output as provenance.
3. **Sequence length and alignment:** pairwise-align P41067 (475 aa) and the pKM101 TraB (~866 aa); length and low identity confirm non-orthology.
4. **Domain-architecture comparison:** confirm P41067 → PF03743 (TrbI/VirB10) and the pKM101 TraB → VirB4 P-loop NTPase family via InterProScan.
5. **AlphaFold fold comparison:** model both; P41067 should adopt the VirB10 scaffold fold (periplasmic β-barrel + TM), the pKM101 TraB a RecA-like NTPase fold.
6. **Direct biochemistry (definitive negative):** purify P41067 and assay for ATP hydrolysis (malachite green). Predicted: no detectable activity, in contrast to Q46698.

---

## Proposed Follow-up Actions (Curation Leads — verify before acting)

**Candidate action change:**
- **Primary lead:** remove GO:0016887 (ATP hydrolysis activity) from P41067. Rationale: name-collision mis-attribution; evidence belongs to the pKM101 VirB4-TraB (Q46698).
- **Secondary lead:** re-home the GO:0016887 IDA (PMID:20172994) to Q46698 after confirming the assayed accession.

**Candidate references with exact snippets to verify:**
- [PMID:20172994](https://pubmed.ncbi.nlm.nih.gov/20172994/): *"Biochemical dissection of the ATPase TraB, the VirB4 homologue of the Escherichia coli pKM101 conjugation machinery."* — verify this describes the pKM101 VirB4-TraB (different from P41067).
- [PMID:11722740](https://pubmed.ncbi.nlm.nih.gov/11722740/): *"TraV, TraK and TraB form a complex in Escherichia coli that spans the cell envelope from the outer membrane (TraV) through the periplasm (TraK) to the inner membrane (TraB)."* — verify F-plasmid TraB (P41067) is an inner-membrane structural component.

**Candidate replacement / additional GO terms for P41067 (leads):**
- CC: inner (plasma) membrane; component of a conjugative T4SS / pilus-assembly complex.
- BP: conjugation / pilus assembly (aligns with UniProt "Involved in F pilus assembly").
- MF/CC: structural constituent of a type IV secretion / conjugative transfer complex (prefer over generic "protein binding").

**Suggested curator questions:**
- Does the GO annotation record for GO:0016887 on P41067 cite PMID:20172994 via a gene-symbol match rather than an accession match?
- Is the pKM101 TraB accession in PMID:20172994 Q46698, and does it already carry GO:0016887?
- Is the F-plasmid TraB (P41067) ever directly shown to bind or hydrolyze ATP in any primary source? (None found here.)

**Suggested experiments:**
- In vitro ATPase assay on purified P41067 (expected negative).
- Side-by-side P-loop HMMER scan and AlphaFold fold comparison of P41067 vs Q46698.

---

## Positive-Control Contrast Table (computed provenance)

| Property | P41067 (F TraB — seed target) | Q46698 (pKM101 TraB — protein in PMID:20172994) |
|----------|-------------------------------|--------------------------------------------------|
| UniProt ID | TRAB1_ECOLI | Q46698_ECOLX |
| Length | 475 aa | 866 aa |
| Pfam | PF03743 (TrbI) | PF03135 (CagE/TrbE/VirB4) |
| InterPro | IPR005498 (VirB10/TraB/TrbI, **structural**) | IPR027417 (**P-loop NTPase**) + IPR004346 (**VirB4_CagE**) |
| Walker-A (GxxxxGK[S/T]) | **none** | **res. 498: GMSGEGKT** (canonical P-loop) |
| Curated function | "Involved in F pilus assembly" | VirB4 ATPase; ATP hydrolysis shown in PMID:20172994 |

The target entry P41067 lacks any P-loop/NTPase signature, while the entry bearing the genuine ATP-hydrolysis evidence (Q46698) is a bona-fide VirB4 P-loop ATPase. This categorical difference confirms the GO:0016887 IDA on P41067 is a name-collision mis-annotation.

---

## Conclusion

The GO:0016887 "ATP hydrolysis activity" annotation on P41067 is **refuted as an over-annotation** driven by a TraB name collision. P41067 is the F-plasmid TraB — a 475-aa VirB10/TraB/TrbI-family (Pfam PF03743) inner-membrane **structural scaffold** with **no Walker-A motif** and a curated role in **F pilus assembly** (confirmed as an inner-membrane component of the TraV–TraK–TraB complex, PMID:11722740). The IDA reference PMID:20172994 instead assayed a different protein — the ~866-aa VirB4-homolog TraB of pKM101 (UniProt Q46698). Because the ATP-hydrolysis evidence belongs to the VirB4-TraB, **GO:0016887 should be removed from P41067** (and optionally re-homed to Q46698), pending curator verification.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)