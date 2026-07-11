---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-09T12:43:48.067952'
end_time: '2026-07-09T12:55:00.276609'
duration_seconds: 672.21
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: pmp20
  gene_symbol: pmp20
  uniprot_accession: O14313
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: computational_prediction
  hypothesis_slug: prediction-peroxiredoxin-activity
  hypothesis_text: BioReason-Pro SFT predicts peroxiredoxin activity (GO:0051920),
    peroxidase activity (GO:0004601), and hydrogen peroxide catabolic process (GO:0042744)
    for the Schizosaccharomyces pombe protein pmp20 (O14313). Independently assess
    whether pmp20 retains the catalytic machinery of an active peroxiredoxin -- specifically
    the peroxidatic cysteine (Cp) in the conserved PXXX(T/S)XXC motif and the resolving
    cysteine (Cr) needed to complete the thiol catalytic cycle -- or whether it has
    lost the resolving cysteine or otherwise degenerated, which would make the peroxiredoxin/peroxidase
    predictions a pseudoenzyme over-annotation. Determine whether the predictions
    are supported or refuted.
  term_context: '- Term: peroxiredoxin activity (GO:0051920)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts peroxiredoxin activity\
    \ (GO:0051920), peroxidase activity (GO:0004601),\n  and hydrogen peroxide catabolic\
    \ process (GO:0042744) for the Schizosaccharomyces pombe protein pmp20\n  (O14313).\
    \ Independently assess whether pmp20 retains the catalytic machinery of an active\
    \ peroxiredoxin\n  -- specifically the peroxidatic cysteine (Cp) in the conserved\
    \ PXXX(T/S)XXC motif and the resolving\n  cysteine (Cr) needed to complete the\
    \ thiol catalytic cycle -- or whether it has lost the resolving cysteine\n  or\
    \ otherwise degenerated, which would make the peroxiredoxin/peroxidase predictions\
    \ a pseudoenzyme over-annotation.\n  Determine whether the predictions are supported\
    \ or refuted.\nfocus_type: computational_prediction\nterm_id: GO:0051920\nterm_label:\
    \ peroxiredoxin activity\ncontext: []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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
citation_count: 3
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
- **Gene directory:** pmp20
- **Gene symbol:** pmp20
- **UniProt accession:** O14313

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-peroxiredoxin-activity
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts peroxiredoxin activity (GO:0051920), peroxidase activity (GO:0004601), and hydrogen peroxide catabolic process (GO:0042744) for the Schizosaccharomyces pombe protein pmp20 (O14313). Independently assess whether pmp20 retains the catalytic machinery of an active peroxiredoxin -- specifically the peroxidatic cysteine (Cp) in the conserved PXXX(T/S)XXC motif and the resolving cysteine (Cr) needed to complete the thiol catalytic cycle -- or whether it has lost the resolving cysteine or otherwise degenerated, which would make the peroxiredoxin/peroxidase predictions a pseudoenzyme over-annotation. Determine whether the predictions are supported or refuted.

## Term and Decision Context

- Term: peroxiredoxin activity (GO:0051920)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts peroxiredoxin activity (GO:0051920), peroxidase activity (GO:0004601),
  and hydrogen peroxide catabolic process (GO:0042744) for the Schizosaccharomyces pombe protein pmp20
  (O14313). Independently assess whether pmp20 retains the catalytic machinery of an active peroxiredoxin
  -- specifically the peroxidatic cysteine (Cp) in the conserved PXXX(T/S)XXC motif and the resolving
  cysteine (Cr) needed to complete the thiol catalytic cycle -- or whether it has lost the resolving cysteine
  or otherwise degenerated, which would make the peroxiredoxin/peroxidase predictions a pseudoenzyme over-annotation.
  Determine whether the predictions are supported or refuted.
focus_type: computational_prediction
term_id: GO:0051920
term_label: peroxiredoxin activity
context: []
reference_id:
- doi:10.64898/2026.03.19.712954
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

## Target: *pmp20* (O14313), *Schizosaccharomyces pombe* — Peroxiredoxin Activity Prediction

**Focus type:** computational_prediction
**Hypothesis slug:** prediction-peroxiredoxin-activity
**Terms under evaluation:** peroxiredoxin activity (GO:0051920), peroxidase activity (GO:0004601), hydrogen peroxide catabolic process (GO:0042744)

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — the pseudoenzyme/"lost resolving cysteine" alternative is REFUTED, but direct catalytic activity in *S. pombe* remains unproven.**

The BioReason-Pro SFT prediction that pmp20 is a peroxiredoxin/peroxidase is grounded in real, intact catalytic machinery — not a degenerate over-annotation. The seed hypothesis raised a specific, testable structural concern: that pmp20 might have lost the resolving cysteine (Cr) or otherwise degenerated its active site, which would make the peroxiredoxin predictions a pseudoenzyme artifact. That specific concern is **incorrect on its premise**. pmp20 is a **1-Cys peroxiredoxin** — a legitimate, well-characterized structural subclass of the peroxiredoxin family (PMP20/PRDX6 type) that normally has no resolving cysteine at all. The absence of a second cysteine is therefore not degeneration; it is the expected, catalytically competent architecture. Structural analysis confirms that the peroxidatic active site is fully intact and correctly assembled.

However, the prediction cannot be scored as fully "supported" because the single direct enzymatic assay performed on *S. pombe* PMP20 failed to detect thioredoxin-dependent peroxidase activity, and the authors instead proposed a molecular chaperone role ([PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/)). Family-level evidence (orthologs in *Hansenula polymorpha*, human, and mouse) strongly supports antioxidant/peroxiredoxin function, but 1-Cys peroxiredoxins typically use physiological reductants other than thioredoxin (e.g., glutathione, ascorbate, or protein partners), so a negative thioredoxin assay does not by itself rule out peroxidase activity. The net result for a curator: the molecular machinery justifies retaining GO:0051920 and GO:0042744 as **conservation/family-supported leads**, but the species-specific claim of *thioredoxin* peroxidase activity (GO:0008379) is not supported and should be generalized or dropped for this organism.

The most important caveat is the tension between **structural competence** (strongly in favor of peroxidase function) and **the one direct functional assay** (which was negative for the thioredoxin-coupled reaction). This is a classic 1-Cys peroxiredoxin situation where the correct reductant/partner matters, and it is exactly the kind of nuance a curator should preserve rather than flatten into a single yes/no annotation.

---

## Key Findings

### Finding 1 — pmp20 retains an intact peroxidatic cysteine motif but is a 1-Cys peroxiredoxin (no resolving Cys)

UniProt O14313 encodes a 156-amino-acid protein containing **exactly one cysteine, Cys43**, which UniProt annotates as the active-site residue forming a "Cysteine sulfenic acid (–SOH) intermediate." This is the diagnostic signature of the peroxidatic cysteine (Cp) of a peroxiredoxin: during catalysis, Cp attacks the peroxide substrate and is oxidized to a sulfenic acid intermediate.

Critically, Cys43 sits within an **intact peroxiredoxin peroxidatic motif**: the local sequence P36-G-A-F-T40-P-P-C43 matches the canonical **P-x-x-x-(T/S)-x-x-C** signature exactly. Position 1 is proline (P36), position 5 is the conserved threonine (T40), and position 8 is the peroxidatic cysteine (C43). All three invariant anchor residues of the motif are satisfied.

Because the entire 156-residue sequence contains **no second cysteine anywhere**, there is **no resolving cysteine (Cr)**. This is the defining feature of the **1-Cys peroxiredoxin** subclass. In 2-Cys peroxiredoxins, Cr forms a disulfide with the oxidized Cp to complete the catalytic cycle; in 1-Cys peroxiredoxins, that role is filled instead by an external low-molecular-weight thiol or a protein partner. The seed hypothesis framed the absence of a resolving cysteine as possible "degeneration" indicative of a pseudoenzyme — but for the PMP20/PRDX6 family, the lack of Cr is the **normal, catalytically legitimate architecture**, not a loss.

Domain and family classifications corroborate the assignment: InterPro places pmp20 in the **PRX5-like** superfamily (IPR037944) with a thioredoxin-like fold, and PANTHER assigns it to **PTHR10430 PEROXIREDOXIN:SF39 (PMP20)**. Both are canonical peroxiredoxin family memberships, not degenerate outliers.

### Finding 2 — The PMP20 family is a genuine antioxidant peroxiredoxin, but *S. pombe* pmp20 showed no thioredoxin-dependent peroxidase activity in vitro

Family-level functional evidence is consistent and strong:

- In the methylotrophic yeast *Hansenula polymorpha*, deletion of the peroxisomal peroxiredoxin (pmp20Δ) produces a methanol-dependent growth defect, elevated reactive oxygen species, lipid peroxidation, loss of peroxisome membrane integrity, and necrotic cell death ([PMID: 18694816](https://pubmed.ncbi.nlm.nih.gov/18694816/)). This is a direct loss-of-function demonstration that a PMP20-family peroxiredoxin protects against oxidative damage.
- Human and murine PMP20 orthologs "exhibit antioxidant activity in vitro" and share high sequence similarity to thiol-specific antioxidant proteins ([PMID: 10514471](https://pubmed.ncbi.nlm.nih.gov/10514471/)).

However, the **species-specific** evidence for *S. pombe* introduces an important qualification. In a direct comparative study of fission yeast peroxiredoxin isozymes and glutathione peroxidase, recombinant *S. pombe* PMP20 showed **no thioredoxin-dependent peroxidase activity**, in contrast to the TPx, BCP, and GPx enzymes that were assayed in parallel. The authors explicitly stated that "peroxidase activity was not observed for PMP20 (peroxisomal membrane protein 20)" and proposed that "the fission yeast PMP20 without thioredoxin-dependent peroxidase activity may act as a molecular chaperone" ([PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/)).

Two interpretations are compatible with this negative result, and a curator should hold both:

1. **Wrong reductant.** 1-Cys peroxiredoxins characteristically do *not* use thioredoxin as their recycling partner; they typically depend on glutathione, ascorbate, or specific protein partners. A negative thioredoxin-coupled assay is therefore weak evidence against peroxidase activity per se — it may simply reflect the wrong electron donor in the in vitro reconstitution.
2. **Genuinely divergent function.** Alternatively, *S. pombe* pmp20 may have shifted toward a chaperone-dominant role, as the authors suggest, even while retaining the structural active site.

The evidence does not currently discriminate cleanly between these, which is precisely why the prediction lands at "partially supported."

### Finding 3 — AlphaFold model shows a fully assembled peroxiredoxin catalytic tetrad (Pro36–Thr40–Cys43–Arg122)

The high-confidence AlphaFold model **AF-O14313-F1-v6** (overall mean pLDDT 95.4; active-site residues pLDDT 93.9–97.9) directly refutes the "degenerate active site" premise of the seed hypothesis. Measured geometry of the modeled active site shows the conserved catalytic residues correctly positioned around the peroxidatic cysteine:

| Interaction | Measured distance | Interpretation |
|---|---|---|
| Cys43(SG) – Thr40(OG1) | 3.00 Å | Hydrogen-bonding distance; Thr correctly poised to stabilize the Cp thiolate/transition state |
| Cys43(SG) – Arg122(guanidinium CZ) | 3.86 Å | Conserved catalytic Arg correctly positioned to lower Cp pKa and stabilize the sulfenate |
| Pro36 | Present, high confidence | Completes the canonical Pro–Thr–Cys–Arg tetrad |

The **Pro36–Thr40–Cys43–Arg122 catalytic tetrad** — the universally conserved active-site constellation of functional peroxiredoxins — is therefore fully assembled at high modeling confidence. There is no second cysteine anywhere in the structure, confirming the 1-Cys architecture at the structural level and matching the sequence analysis. Structurally, pmp20 is an **active-site-competent peroxiredoxin**, not a degenerate pseudoenzyme.

---

## Mechanistic Model / Interpretation

The three findings converge on a coherent picture. pmp20 is a **structurally intact 1-Cys peroxiredoxin** whose catalytic machinery is fully present, but whose recycling chemistry in *S. pombe* is unresolved.

```
        PEROXIREDOXIN CATALYTIC CYCLE (1-Cys type)

   ROOH (H2O2 / lipid peroxide)
        |
        v
   Cp-SH  --(peroxidatic Cys43 attacks peroxide)-->  Cp-SOH  + ROH
   (thiolate                                          (sulfenic acid
    stabilized by                                      intermediate;
    Thr40 + Arg122)                                    UniProt-annotated)
        ^                                                  |
        |                                                  v
        |                              Resolution step requires an EXTERNAL reductant
        |                              (1-Cys Prx has NO resolving Cys of its own)
        |                                                  |
        +---- reduced by: glutathione / ascorbate / -------+
              protein partner  (NOT thioredoxin in vitro — PMID 20356456)

   Catalytic tetrad (AlphaFold AF-O14313-F1-v6, pLDDT ~95):
       Pro36 --- Thr40 (3.0 Å to Cp) --- Cys43(Cp) --- Arg122 (3.9 Å to Cp)
       ALL PRESENT AND CORRECTLY POSITIONED
```

**What the machinery tells us (strongly supported):** The peroxidatic half-reaction — the step that actually defines "peroxidase/peroxiredoxin activity" — has an intact, correctly geometried active site. Sequence (P-x-x-x-T-x-x-C motif), family classification (PRX5-like, PANTHER PMP20), and structure (assembled Pro/Thr/Cys/Arg tetrad) all agree. The seed's pseudoenzyme hypothesis is refuted.

**What remains uncertain (the resolution half-reaction):** The absence of a resolving cysteine is normal for this subclass, but it means the enzyme depends on an external reductant. The only direct *S. pombe* assay used thioredoxin and was negative — an expected outcome if pmp20 is a glutathione- or ascorbate-dependent 1-Cys enzyme, but also consistent with a functional shift toward chaperone activity. The negative thioredoxin result should therefore **not** be read as "no peroxidase activity," only as "no *thioredoxin-dependent* peroxidase activity."

The correct mechanistic scope for curation is: pmp20's **immediate molecular function** is thiol-based peroxide reduction via a sulfenic-acid intermediate on Cys43. Downstream/pleiotropic consequences at the family level (peroxisome membrane protection, prevention of lipid peroxidation and necrotic death in orthologs) are real but should not be conflated with the direct MF term.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt O14313 (database record) | Structural/evolutionary; database | Refutes pseudoenzyme; supports Prx MF | Does pmp20 retain the Cp motif and a resolving Cys? | Single Cys (C43) in intact P36-x-x-x-T40-x-x-C43 motif; annotated Cys-sulfenic-acid intermediate; 1-Cys architecture (no Cr) | *S. pombe*, sequence-level | High for sequence facts; annotation is inference-based |
| InterPro IPR037944 / PANTHER PTHR10430:SF39 (database) | Computational/family | Supports Prx family membership | Is pmp20 a bona fide peroxiredoxin family member? | PRX5-like, thioredoxin-like fold; PANTHER PMP20 subfamily | *S. pombe* | High for classification; does not prove activity |
| AlphaFold AF-O14313-F1-v6 (structural model) | Structural (predicted) | Refutes degenerate active site | Is the catalytic tetrad assembled? | Pro36–Thr40–Cys43–Arg122 tetrad intact; Cp–Thr 3.0 Å, Cp–Arg 3.9 Å; pLDDT ~95 | *S. pombe*, in silico | High model confidence; predicted not experimental structure |
| [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/) | Direct in vitro assay | Qualifies / partially refutes | Does *S. pombe* PMP20 have Trx-dependent peroxidase activity? | No thioredoxin-dependent peroxidase activity observed; proposed chaperone role | *S. pombe* recombinant protein | High for the negative Trx result; wrong reductant is a strong confound for 1-Cys Prx |
| [PMID: 18694816](https://pubmed.ncbi.nlm.nih.gov/18694816/) | Mutant phenotype (loss-of-function) | Supports (family level) | Does a PMP20-family Prx protect against oxidative damage? | pmp20Δ → ROS, lipid peroxidation, membrane leakage, necrotic death | *Hansenula polymorpha* | High for ortholog; not *S. pombe*; phenotype is downstream of MF |
| [PMID: 10514471](https://pubmed.ncbi.nlm.nih.gov/10514471/) | Direct assay (ortholog) | Supports (family level) | Do PMP20 orthologs have antioxidant activity? | Human/murine PMP20 show antioxidant activity in vitro; similar to thiol-specific antioxidants | Human, mouse | Moderate-high for orthologs; species transfer inference |

---

## GO Curation Implications

**Lead requiring curator verification.** The molecular and structural evidence justifies treating the peroxiredoxin function as real but not fully experimentally nailed down in *S. pombe*.

| GO term | Aspect | Recommended action (lead) | Rationale |
|---|---|---|---|
| GO:0051920 peroxiredoxin activity | MF | **Retain as conservation/family-supported lead** (evidence code ISS/IBA-type reasoning) | Intact Cp motif + assembled catalytic tetrad + family membership strongly support the MF; direct *S. pombe* kinetics not demonstrated |
| GO:0004601 peroxidase activity | MF | **Retain as the broader parent lead** | Supported by same structural/family evidence; more general and safer than the thioredoxin-specific child |
| GO:0042744 hydrogen peroxide catabolic process | BP | **Retain as family-supported lead** | Consistent with peroxiredoxin MF and ortholog oxidative-stress phenotypes |
| GO:0008379 thioredoxin peroxidase activity | MF | **Do NOT assign / generalize** for *S. pombe* | Directly contradicted by the one in vitro assay ([PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/)); 1-Cys Prx generally are not thioredoxin-coupled |
| Chaperone activity (e.g., unfolded protein binding / chaperone) | MF | **Flag as a competing/complementary lead** | Proposed by [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/); needs curator judgement on whether experimentally established |

The evidence supports an **MF** (peroxiredoxin/peroxidase) and an associated **BP** (H2O2 catabolism), with the peroxisomal **CC** context suggested by family membership (PMP20 = peroxisomal membrane protein 20). "Protein binding" is not an appropriate final term here; the informative MF is peroxiredoxin/peroxidase activity. The key curator decision is whether to attach these as computationally/conservation-supported (ISS/IBA) rather than experimentally supported (IDA), given the absence of a positive direct assay in this species.

---

## Mechanistic Scope

- **Direct gene-product activity (what is being tested):** Thiol-based reduction of peroxide substrate via nucleophilic attack by the peroxidatic Cys43, forming a Cys-sulfenic-acid intermediate stabilized by Thr40 and Arg122. This is the immediate molecular function.
- **Resolution chemistry:** As a 1-Cys peroxiredoxin, pmp20 lacks an internal resolving cysteine and must be recycled by an external reductant (glutathione/ascorbate/protein partner), not by an intramolecular disulfide.
- **Downstream / not to be conflated with MF:** Peroxisome membrane integrity, protection from lipid peroxidation, prevention of necrotic death (ortholog phenotypes) — these are pathway-level consequences of the antioxidant function, valuable as BP context but not direct MF evidence.
- **Competing direct function:** Possible molecular chaperone activity, proposed on the basis of the absent thioredoxin-dependent peroxidase activity in *S. pombe*.

---

## Conflicts and Alternatives

1. **Structural competence vs. negative functional assay.** The dominant conflict: sequence + AlphaFold say "fully competent active site," while the one direct *S. pombe* assay says "no thioredoxin-dependent peroxidase activity." The most parsimonious reconciliation is that the assay used the wrong reductant for a 1-Cys enzyme, not that the enzyme is inactive.
2. **Chaperone reassignment.** [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/) proposes a molecular chaperone role. This is a genuine alternative primary function that a curator should weigh; peroxiredoxins are known to moonlight as chaperones, so the two are not mutually exclusive.
3. **Ortholog/paralog transfer risk.** The strongest positive functional data come from *H. polymorpha*, human, and mouse orthologs, not *S. pombe* itself. Cross-species function transfer is reasonable for a conserved family but is inference, not direct evidence.
4. **"Lost resolving cysteine = pseudoenzyme" is a category error.** The seed hypothesis implicitly treats a missing Cr as pathological. For the PMP20/PRDX6 1-Cys subclass this is the normal architecture, so the pseudoenzyme framing does not apply.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No positive direct peroxidase assay in *S. pombe* | Literature; found only a negative thioredoxin-coupled assay | Determines whether MF should be IDA vs ISS/IBA | Peroxide-reduction assay with glutathione/ascorbate or candidate protein reductants |
| Physiological reductant unknown | Sequence shows 1-Cys architecture (needs external reductant) | 1-Cys Prx recycling partner defines its true activity | Reconstitution with GSH/glutaredoxin, ascorbate, and protein-partner screens |
| Chaperone vs peroxidase primacy unresolved | [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/) proposes chaperone | Affects which MF is "core" | Side-by-side chaperone and peroxidase assays; in vivo H2O2 sensitivity of pmp20Δ |
| Subcellular localization not independently verified here | Family name implies peroxisomal (PMP20) | CC term assignment | GFP localization / peroxisome fractionation in *S. pombe* |
| AlphaFold is a model, not experimental structure | pLDDT ~95 gives high confidence | Geometry-based active-site claims rest on a prediction | Experimental crystal/cryo-EM structure |

---

## Discriminating Tests

1. **Reductant-swap peroxidase assay.** Repeat the peroxide-reduction assay using **glutathione (± glutaredoxin) and ascorbate** as reductants rather than thioredoxin. A positive result would convert the annotation from a conservation lead to a direct (IDA) peroxiredoxin annotation and explain the negative thioredoxin result.
2. **Cys43-to-Ser active-site mutant.** Test whether C43S abolishes any detected peroxidase (and/or chaperone) activity — establishes that the annotated Cp is the catalytic residue.
3. **In vivo oxidative-stress phenotyping.** Compare *S. pombe* wild-type vs pmp20Δ (and C43S knock-in) under H2O2 and organic-peroxide challenge; scored ROS, lipid peroxidation, and viability — mirrors the informative *H. polymorpha* experiment.
4. **Chaperone activity assay.** Aggregation-prevention (e.g., citrate synthase/insulin turbidity) to test the chaperone hypothesis directly and determine whether it is redox-state dependent.
5. **Localization confirmation.** Fluorescent tagging / peroxisome co-localization to justify a peroxisomal CC term.

---

## Curation Leads

**All items below are leads requiring curator verification.**

**Candidate references with exact snippets to verify:**
- [PMID: 20356456](https://pubmed.ncbi.nlm.nih.gov/20356456/) — verify snippet: *"peroxidase activity was not observed for PMP20 (peroxisomal membrane protein 20)"* and *"The fission yeast PMP20 without thioredoxin-dependent peroxidase activity may act as a molecular chaperone."* → supports NOT assigning GO:0008379 and flags a competing chaperone MF.
- [PMID: 18694816](https://pubmed.ncbi.nlm.nih.gov/18694816/) — verify snippet: *"absence of the peroxisomal peroxiredoxin leads to loss of peroxisome membrane integrity and necrotic cell death"* → family-level antioxidant/peroxidase support (ortholog).
- [PMID: 10514471](https://pubmed.ncbi.nlm.nih.gov/10514471/) — verify PMP20 orthologs *"exhibit antioxidant activity in vitro"* → family-level support.

**Candidate GO actions:**
- Retain **GO:0051920 peroxiredoxin activity** and **GO:0004601 peroxidase activity** as conservation/family-supported (ISS/IBA) leads, not IDA.
- Retain **GO:0042744 hydrogen peroxide catabolic process** as a supporting BP lead.
- Do **not** assign **GO:0008379 thioredoxin peroxidase activity** for *S. pombe*; generalize to the parent peroxidase term.
- Consider a peroxisomal **CC** term consistent with PMP20 family identity (verify by localization).
- Consider flagging a **chaperone** MF as an alternative/complementary function pending direct evidence.

**Suggested curator questions:**
- Is there any positive peroxidase assay for *S. pombe* pmp20 with a non-thioredoxin reductant?
- Should the record carry both a peroxiredoxin MF (conservation-based) and a chaperone MF (experiment-based proposal)?

**Suggested experiments:** the five discriminating tests above, prioritizing the glutathione/ascorbate-coupled peroxidase assay and the C43S mutant.

---

## Bottom Line

pmp20 is a structurally intact **1-Cys peroxiredoxin** with a complete, correctly assembled Pro36–Thr40–Cys43–Arg122 catalytic tetrad. The seed's "lost resolving cysteine / pseudoenzyme over-annotation" hypothesis is **refuted** — the missing resolving cysteine is the normal architecture of this subclass, not degeneration. The BioReason-Pro peroxiredoxin/peroxidase/H2O2-catabolism predictions are therefore **partially supported**: justified as conservation/family-based leads (retain GO:0051920, GO:0004601, GO:0042744), but not upgraded to direct-experimental confidence because the only direct *S. pombe* assay found no thioredoxin-dependent peroxidase activity (GO:0008379 should be generalized/dropped for this organism), and a competing chaperone role remains on the table.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)