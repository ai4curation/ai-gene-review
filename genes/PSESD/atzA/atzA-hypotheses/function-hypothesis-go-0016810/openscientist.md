---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T18:28:28.374622'
end_time: '2026-10-09T18:40:42.631912'
duration_seconds: 734.26
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PSESD
  gene: atzA
  gene_symbol: atzA
  uniprot_accession: P72156
  taxon_id: NCBITaxon:47660
  taxon_label: Pseudomonas sp. ADP
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0016810
  hypothesis_text: atzA has hydrolase activity, acting on carbon-nitrogen (but not
    peptide) bonds (GO:0016810).
  term_context: '- Term: hydrolase activity, acting on carbon-nitrogen (but not peptide)
    bonds (GO:0016810)

    - Evidence type: IEA

    - Original reference: GO_REF:0000002'
  reference_context: '- GO_REF:0000002

    - PMID:8759853

    - PMID:11274097'
  source_file: genes/PSESD/atzA/atzA-ai-review.yaml
  source_selector: existing_annotations[3].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0016810\n  label: hydrolase activity, acting\
    \ on carbon-nitrogen (but not peptide) bonds\nevidence_type: IEA\noriginal_reference_id:\
    \ GO_REF:0000002"
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
citation_count: 5
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

- **Organism code:** PSESD
- **Taxon:** Pseudomonas sp. ADP (NCBITaxon:47660)
- **Gene directory:** atzA
- **Gene symbol:** atzA
- **UniProt accession:** P72156

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016810
- **Source file:** genes/PSESD/atzA/atzA-ai-review.yaml
- **Source selector:** existing_annotations[3].function_hypothesis

## Seed Hypothesis

atzA has hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds (GO:0016810).

## Term and Decision Context

- Term: hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds (GO:0016810)
- Evidence type: IEA
- Original reference: GO_REF:0000002

## Reference Context

- GO_REF:0000002
- PMID:8759853
- PMID:11274097

## Source Context YAML

```yaml
term:
  id: GO:0016810
  label: hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds
evidence_type: IEA
original_reference_id: GO_REF:0000002
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

**Gene:** atzA (atrazine chlorohydrolase) | **Organism:** *Pseudomonas* sp. ADP (NCBITaxon:47660) | **UniProt:** P72156
**Focus:** function_assignment | **Hypothesis slug:** function-hypothesis-go-0016810
**Seed hypothesis:** *atzA has hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds (GO:0016810).*
**Term under review:** GO:0016810 — hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds | **Evidence type:** IEA | **Original reference:** GO_REF:0000002

---

## Summary

**Verdict: REFUTED / OVER-ANNOTATED.** The seed hypothesis — that atzA (P72156) has "hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds" (GO:0016810) — is **not supported** by the experimental record and should be **removed** from the gene review. AtzA is an experimentally proven **atrazine chlorohydrolase** (EC 3.8.1.8) that hydrolyzes a **carbon–chlorine (C–Cl) bond**, not a carbon–nitrogen (C–N) bond. The correct, experimentally-supported molecular-function term is **GO:0018788 (atrazine chlorohydrolase activity)**, which sits in a *disjoint* sub-branch of the hydrolase ontology (the "acting on halide bonds" branch, EC 3.8) that does **not** descend from GO:0016810 (the "acting on C–N bonds" branch, EC 3.5).

The strongest evidence is mechanistic and direct. Heavy-water (H₂¹⁸O) isotope-labeling showed the hydroxyl oxygen of the hydroxyatrazine product derives from water, proving AtzA is a **chlorohydrolase (hydrolytic dechlorinase), not an oxygenase** ([PMID:8759853](https://pubmed.ncbi.nlm.nih.gov/8759853/)). A near-identical paralog study demonstrated AtzA "exclusively catalyzes dehalogenation of halo-substituted triazine ring compounds and had **no activity with melamine and ammeline**" — i.e., it lacks deaminase (C–N hydrolase) activity entirely ([PMID:11274097](https://pubmed.ncbi.nlm.nih.gov/11274097/)). AtzA is a Fe(II)-dependent metalloenzyme that proceeds via a hydrolytic mechanism ([PMID:12450410](https://pubmed.ncbi.nlm.nih.gov/12450410/)).

The GO:0016810 annotation is a **single IEA** (ECO:0000256, GO_REF:0000002) that traces to an InterPro fold/domain-superfamily mapping — specifically the IPR011059 "Metal-dependent hydrolase, composite domain superfamily" interpro2go mapping — and not to any experiment or to the enzyme's EC number. Because AtzA belongs to the amidohydrolase superfamily (a structural fold dominated by C–N-acting deaminases and amidohydrolases), a fold-based electronic pipeline mis-assigned a C–N hydrolase activity term. The EC number that IS assigned to AtzA (EC 3.8.1.8) maps, via the official ec2go mapping, to **GO:0018788**, the correct C-halide term — which already carries **two independent experimental (EXP) annotations** in live GOA. This is a textbook example of fold-based IEA over-annotation landing in the wrong, disjoint ontology branch. **Recommended curation action: remove/down-rank GO:0016810; retain GO:0018788 as the core molecular function.**

---

## Key Findings

### F001 — AtzA catalyzes C–Cl bond hydrolysis (dechlorination), not C–N bond hydrolysis

The defining reaction of AtzA is the first, committed step of atrazine catabolism: **atrazine + H₂O → hydroxyatrazine + chloride + H⁺**. This is a hydrolytic dehalogenation — water attacks the ring carbon bearing the chlorine substituent, displacing chloride and installing a hydroxyl. UniProt P72156 records this reaction with EC 3.8.1.8 and an experimentally-supported GO:0018788 (atrazine chlorohydrolase activity, EXP:UniProtKB).

The mechanism was proven directly by isotope labeling. de Souza et al. ([PMID:8759853](https://pubmed.ncbi.nlm.nih.gov/8759853/)) purified AtzA and ran the reaction in ¹⁸O-enriched water: *"The purified enzyme in H₂¹⁸O yielded [¹⁸O]hydroxyatrazine, indicating that AtzA is a chlorohydrolase and not an oxygenase."* The appearance of ¹⁸O in the product hydroxyl group establishes that the oxygen comes from solvent water (hydrolysis), not from molecular O₂ (oxygenation). This is the mechanistic crux that places AtzA firmly in the hydrolytic-dehalogenase category.

Critically, the substrate specificity of AtzA excludes C–N hydrolase (deaminase) activity. Seffernick et al. ([PMID:11274097](https://pubmed.ncbi.nlm.nih.gov/11274097/)) compared AtzA to its 98%-identical paralog melamine deaminase (TriA) and found that *"AtzA was shown to exclusively catalyze dehalogenation of halo-substituted triazine ring compounds and had no activity with melamine and ammeline."* Melamine and ammeline are deaminated (C–N bond cleavage releasing ammonia) by the paralog, but AtzA does not touch them. UniProt further states AtzA "has no deaminase activity with melamine (PubMed:22768133, PubMed:8759853)." Thus the gene product directly performs C–Cl hydrolysis and directly lacks C–N hydrolysis — the exact opposite of what GO:0016810 asserts.

### F002 — GO:0016810 is a disjoint-branch over-annotation (InterPro amidohydrolase-family IEA)

The GO ontology separates hydrolases by the bond they act upon. Using QuickGO `is_a` ancestry traversal:

- **GO:0018788** (atrazine chlorohydrolase activity) ancestry → GO:0016824 (hydrolase acting on acid halide bonds) → GO:0019120 (hydrolase acting on carbon-halide bonds) → GO:0016787 (hydrolase). **GO:0016810 is NOT an ancestor.**
- **GO:0016810** (hydrolase acting on C–N, non-peptide, bonds) ancestry → GO:0016787 (hydrolase) only.

These two terms live in **disjoint sub-branches** of the hydrolase tree — the C-halide branch (corresponding to EC 3.8) versus the C–N branch (corresponding to EC 3.5). An enzyme cannot be correctly annotated to both based on a single activity; they represent chemically distinct bond-cleavage classes. The presence of GO:0016810 on P72156 as an IEA:InterPro annotation is therefore not a more-general parent of the true function — it is a **sibling in the wrong branch**, i.e., a genuine mis-assignment rather than a harmless generalization.

The source of the error is structural homology. AtzA belongs to the **amidohydrolase superfamily** (Pfam PF01979 Amidohydro_1; InterPro IPR006680 Amidohydro-rel), a large (β/α)₈ TIM-barrel metalloenzyme fold whose members are *predominantly* C–N-acting deaminases and amidohydrolases (e.g., cytosine deaminase, adenosine deaminase, urease-related enzymes). AtzA is a rare dehalogenating member of this otherwise C–N-dominated fold. Fold-recognition IEA pipelines, keyed on the superfamily signature, therefore default to the majority function of the fold (C–N hydrolysis) and propagate GO:0016810 — overriding the known, specific dehalogenase chemistry.

### F003 — GO:0016810 traces specifically to the IPR011059 composite-domain interpro2go mapping; EC 3.8.1.8 maps to the correct term

Examining the official GO external2go mapping files (current.geneontology.org) pinpoints the exact provenance:

- **ec2go:** `EC:3.8.1.8 → GO:0018788 (atrazine chlorohydrolase activity)`. The EC number assigned to AtzA maps precisely and correctly to the C-halide molecular-function term. If the annotation pipeline had used the EC number, it would have produced the right answer.
- **interpro2go:** `IPR011059 (Metal-dependent hydrolase, composite domain superfamily) → GO:0016810`. This is the **sole source** of the seed term. The composite metal-dependent-hydrolase fold mapping carries GO:0016810 as its assigned function.
- By contrast, the more specific family signatures **IPR006680 (Amidohydrolase-related)** and **PF01979 (Amidohydro_1)** map only to the generic **GO:0016787 (hydrolase)** — a safe, correct parent that makes no bond-class claim.

The conclusion is that GO:0016810 on P72156 is a **domain-superfamily IEA driven by IPR011059**, not an EC-derived or experiment-derived annotation. It reflects the fold's majority chemistry, not AtzA's actual chemistry. The pipeline that should have governed the MF call — ec2go on EC 3.8.1.8 — points to GO:0018788.

### F004 — Live GOA confirms GO:0016810 is a single IEA while GO:0018788 carries two independent EXP annotations

The live QuickGO annotation set for P72156 contains 7 annotations, and their evidence tiers make the curation decision clear-cut:

| GO term | Label | Aspect | Evidence | Reference |
|---|---|---|---|---|
| **GO:0016810** | hydrolase activity, acting on C–N (not peptide) bonds | MF | **IEA** (ECO:0000256) | GO_REF:0000002 (InterPro) |
| **GO:0018788** | atrazine chlorohydrolase activity | MF | **EXP** (ECO:0000269) | PMID:22768133 |
| **GO:0018788** | atrazine chlorohydrolase activity | MF | **EXP** (ECO:0000269) | PMID:8759853 |
| GO:0018788 | atrazine chlorohydrolase activity | MF | IEA | — |
| GO:0016787 | hydrolase activity | MF | IEA | — |
| GO:0019381 | atrazine catabolic process | BP | IEA | — |
| GO:0005737 | cytoplasm | CC | IEA | — |

The seed term GO:0016810 rests on a **single, lowest-tier electronic annotation**. The competing, chemically-correct term GO:0018788 rests on **two independent experimental annotations** (plus an IEA). Both GO:0016810 and GO:0018788 are **non-obsolete** terms, so this is a live misclassification that a curator must correct by action — not something that will be resolved automatically by an ontology obsoletion. The generic parent GO:0016787 (hydrolase) is correctly present and can be retained as an uninformative-but-true backstop.

---

## Mechanistic Model / Interpretation

### The reaction and why it is a dehalogenation, not a deamination

```
              Cl                               OH
               |                                |
         N == C                           N == C
        /       \        + H2O            /       \       + HCl
   atrazine ring         ─────────▶   hydroxyatrazine
   (chloro-s-triazine)   AtzA, Fe(II)  (hydroxy-s-triazine)

  Bond cleaved:  C–Cl   (carbon–halide)      ← EC 3.8.1.8  → GO:0018788
  NOT cleaved:   C–N    (ring/amino)         ← EC 3.5.x    → GO:0016810  (seed term, WRONG)

  Oxygen source: H2(18)O  → [18O]hydroxyatrazine   (PMID:8759853)  = hydrolysis
```

AtzA removes the chlorine on the s-triazine ring and installs a hydroxyl in a single hydrolytic step. The ring nitrogens and the ethyl/isopropyl amino substituents are untouched by AtzA; the subsequent amino groups are removed downstream by other enzymes (AtzB, AtzC) later in the pathway. Therefore any "C–N bond hydrolysis" chemistry in atrazine catabolism belongs to *other* genes, not atzA.

### The ontology geometry that makes the seed term wrong

```
                         GO:0016787  hydrolase activity  (TRUE, generic)
                        /                                   \
        GO:0016810 (C–N bonds)                     GO:0019120 (C–halide bonds)
        EC 3.5 branch                                |
        [SEED TERM — WRONG BRANCH]          GO:0016824 (acid halide bonds)
                                                     |
                                           GO:0018788 atrazine chlorohydrolase
                                           EC 3.8.1.8  [TRUE, 2× EXP]
```

GO:0016810 and GO:0018788 descend from GO:0016787 through **non-overlapping** intermediate terms. They are not in a parent/child relationship. An annotation to GO:0016810 is thus not a "less specific but still correct" statement — it is a **positively incorrect** claim about the chemical class of bond cleaved.

### Why the error arose (provenance chain)

```
AtzA sequence → InterPro scan → IPR011059 (metal-dependent hydrolase, composite domain superfamily)
                                      │  interpro2go
                                      ▼
                                GO:0016810   ← majority chemistry of the amidohydrolase fold (C–N deaminases)
                                             = the seed IEA, GO_REF:0000002

Correct path (not used for the MF bond-class call):
AtzA → EC 3.8.1.8 → ec2go → GO:0018788 (correct C-halide term)
```

The amidohydrolase superfamily fold is a generalist scaffold that supports many different hydrolytic reactions; most of its characterized members are deaminases/amidohydrolases acting on C–N bonds. A fold-level mapping therefore encodes the *modal* activity of the superfamily, which does not match AtzA's specialized, experimentally established dehalogenase activity.

---

## Evidence Base

### Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:8759853](https://pubmed.ncbi.nlm.nih.gov/8759853/) (de Souza et al.) | Direct assay (¹⁸O isotope labeling); enzyme purification | **Refutes** seed; supports GO:0018788 | Is AtzA a hydrolytic dechlorinase or an oxygenase? | "The purified enzyme in H₂¹⁸O yielded [¹⁸O]hydroxyatrazine, indicating that AtzA is a chlorohydrolase and not an oxygenase." | Purified AtzA, *Pseudomonas* sp. ADP, in vitro | High. Definitive mechanism; basis for one of the two EXP GO:0018788 annotations. |
| [PMID:11274097](https://pubmed.ncbi.nlm.nih.gov/11274097/) (Seffernick et al.) | Direct assay; comparative substrate specificity | **Refutes** seed (C–N activity) | Does AtzA have deaminase (C–N hydrolase) activity? | "AtzA was shown to exclusively catalyze dehalogenation of halo-substituted triazine ring compounds and had no activity with melamine and ammeline." | AtzA vs 98%-identical melamine deaminase (TriA), in vitro | High. Direct demonstration that AtzA lacks C–N (deaminase) activity. |
| [PMID:12450410](https://pubmed.ncbi.nlm.nih.gov/12450410/) (Seffernick et al.) | Direct assay; metal reconstitution | **Supports** hydrolytic mechanism / GO:0018788 | Is AtzA a metal-dependent hydrolase? | "AtzA is a functional metalloenzyme... the first report of a metal-dependent dechlorinating enzyme that proceeds via a hydrolytic mechanism"; native metal Fe(II), 1:1 stoichiometry. | Purified AtzA, chelator/metal reconstitution, in vitro | High. Confirms hydrolytic dehalogenation; amidohydrolase-superfamily metalloenzyme. |
| UniProt P72156 (ec2go, interpro2go, GOA) | Database / computational provenance | **Qualifies** — pins the error source | What generates GO:0016810 vs GO:0018788? | EC 3.8.1.8 → GO:0018788 (ec2go, correct); IPR011059 → GO:0016810 (interpro2go, sole seed source). | Public mapping files, current.geneontology.org | High for provenance tracing; database-level evidence. |
| QuickGO live annotations (P72156) | Database | **Refutes** (tier asymmetry) | How strong is each competing annotation? | GO:0016810 = single IEA/GO_REF:0000002; GO:0018788 = 2× EXP (PMID:22768133, PMID:8759853). | Live GOA | High. Both terms non-obsolete → live misclassification. |
| [PMID:12680937](https://pubmed.ncbi.nlm.nih.gov/12680937/) (Arthrobacter AD1) | Review/comparative (orientation) | Context | Is atzA conserved / what is its role? | atzA "isolated from strain AD1 differed from that found in the *Pseudomonas* sp. ADP by only one nucleotide"; encodes atrazine chlorohydrolase; highly conserved. | Arthrobacter sp. AD1, 16S + gene sequencing | Moderate. Orientation-level; reinforces chlorohydrolase identity and conservation. |

### Narrative of the literature

The primary mechanistic literature is unusually clean for a bacterial catabolic enzyme. **de Souza et al. 1996** ([PMID:8759853](https://pubmed.ncbi.nlm.nih.gov/8759853/)) cloned, sequenced, purified, and characterized AtzA, and used the H₂¹⁸O labeling experiment to nail the chlorohydrolase (hydrolytic) mechanism. This paper is itself one of the two experimental references underpinning the correct GO:0018788 annotation in GOA. **Seffernick et al. 2001** ([PMID:11274097](https://pubmed.ncbi.nlm.nih.gov/11274097/)) provides the decisive negative evidence against the seed term: by contrasting AtzA with its 98%-identical paralog melamine deaminase, they show that a handful of amino-acid substitutions flips the enzyme between dehalogenation (AtzA, C–Cl) and deamination (melamine deaminase, C–N), and that AtzA has *no* deaminase activity. This both refutes the C–N hypothesis and illustrates exactly why fold-based annotation is dangerous here — near-identical sequences in this superfamily can have different bond-class chemistries. **Seffernick et al. 2002** ([PMID:12450410](https://pubmed.ncbi.nlm.nih.gov/12450410/)) confirms AtzA is an Fe(II) metalloenzyme operating by a hydrolytic mechanism within the amidohydrolase superfamily, consolidating the mechanistic picture. **PMID:12680937** (Arthrobacter AD1) is orientation-level but reinforces that atzA is a highly conserved atrazine chlorohydrolase across hosts.

No primary study reports any C–N-bond hydrolase (deaminase/amidohydrolase) activity for AtzA; the only support for GO:0016810 is the electronic fold mapping.

---

## GO Curation Implications

**Likely curation action (lead — requires curator verification): REMOVE (or down-rank) GO:0016810 from P72156.**

- **Aspect:** Molecular Function.
- **Term GO:0016810 (hydrolase acting on C–N, non-peptide, bonds):** Should be **removed**, not generalized. It is not a true (less-specific) parent of AtzA's activity; it is a sibling term in the disjoint C–N branch (EC 3.5), whereas AtzA's activity is in the C-halide branch (EC 3.8). Retaining it would assert an incorrect bond-class chemistry. Its sole support is a single IPR011059-driven IEA (GO_REF:0000002).
- **Term GO:0018788 (atrazine chlorohydrolase activity):** Should be **retained** as the core molecular function. It is EC-correct (EC 3.8.1.8 via ec2go) and carries two independent EXP annotations (PMID:22768133, PMID:8759853).
- **Term GO:0016787 (hydrolase activity):** May be **retained** as a correct, uninformative generic parent (it is the shared ancestor of both branches and makes no false bond-class claim).
- **BP GO:0019381 (atrazine catabolic process)** and **CC GO:0005737 (cytoplasm):** Not in scope of this hypothesis; both are reasonable and can be left as-is pending separate review.

This is **not** a case where "protein binding" or any binding term is the fallback — a specific, experimentally supported, EC-correct MF term (GO:0018788) is available and should be the headline annotation.

### GO decision table

| Term | Action | Confidence | Basis |
|---|---|---|---|
| GO:0016810 (C–N hydrolase) | **Remove / NOT** | High | Single IEA; disjoint wrong branch; experimentally excluded C–N activity |
| GO:0018788 (atrazine chlorohydrolase) | **Retain (core MF)** | High | 2× EXP; EC 3.8.1.8 ec2go match |
| GO:0016787 (hydrolase) | Retain (generic) | Medium | True shared parent; uninformative |

---

## Mechanistic Scope

The immediate molecular function under test is a **single-step hydrolytic bond cleavage**: AtzA uses an active-site Fe(II) and a water molecule to displace chloride from the s-triazine ring carbon of atrazine, producing hydroxyatrazine. This is a direct, catalytic, gene-product-intrinsic activity measured on purified enzyme in vitro (PMID:8759853, PMID:12450410).

The seed term GO:0016810 asserts a *different* immediate molecular function — hydrolysis of a carbon–nitrogen bond (e.g., deamination, amide hydrolysis). That activity is **directly excluded** for AtzA by substrate-specificity assays (no activity on melamine/ammeline; PMID:11274097). It is important to separate:

- **Direct gene-product activity:** C–Cl hydrolysis (dechlorination) — GO:0018788. ✅
- **Downstream pathway chemistry:** Later C–N cleavages (deaminations, ring-N hydrolyses) in the atrazine → cyanuric acid → CO₂ + NH₃ pathway are carried out by **other enzymes** (AtzB hydroxyatrazine ethylaminohydrolase, AtzC N-isopropylammelide isopropylaminohydrolase, etc.), **not** by AtzA. Attributing a C–N hydrolase term to AtzA conflates AtzA with these downstream pathway members.
- **Not a loss-of-function inference:** The refutation here rests on positive biochemical assays of purified enzyme, not on phenotype inference.

Thus the seed hypothesis fails at the level of the gene product's *primary and only* catalytic activity.

---

## Conflicts and Alternatives

1. **Paralog confusion (the central alternative).** AtzA is 98% identical to melamine deaminase (TriA), which *does* hydrolyze C–N bonds (deamination). A naive sequence- or fold-based pipeline could easily conflate the two. The primary literature explicitly resolves this: AtzA dehalogenates and does **not** deaminate (PMID:11274097). The seed term looks like exactly the kind of error this paralog pair is famous for generating.

2. **Fold/superfamily majority-function bias.** The amidohydrolase superfamily is dominated by C–N-acting enzymes. IPR011059 (composite metal-dependent hydrolase domain) maps to GO:0016810, so any member — including the rare dehalogenase AtzA — inherits the C–N term electronically. This is frequency/majority bias in fold2GO mappings, not evidence about AtzA.

3. **Database carry-over / provenance chain error.** The MF bond-class call should flow from EC 3.8.1.8 (→ GO:0018788) but instead flowed from IPR011059 (→ GO:0016810). The correct mapping exists and is applied (GO:0018788 is present); the incorrect one was not filtered out.

4. **Organism considerations.** atzA is near-identical across hosts (one-nucleotide difference between *Pseudomonas* sp. ADP and *Arthrobacter* AD1; PMID:12680937), so there is no organism-specific isoform that would rescue a C–N activity interpretation. The function is conserved as a chlorohydrolase.

No credible primary evidence supports the C–N hypothesis; all conflicts resolve against the seed term.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Exact pipeline version behind GO_REF:0000002 | Confirmed GO_REF:0000002 = InterPro2GO electronic pipeline; traced term to IPR011059 via interpro2go | Confirms the annotation is fold-based, not EC- or experiment-based, strengthening the "remove" lead | Direct inspection of the GOA submission batch / InterPro release that generated the annotation |
| Whether GO:0016810 is additionally propagated by any non-IEA path | QuickGO live set shows GO:0016810 as a single IEA only | If it were also curated/EXP, removal would be contestable; it is not | Confirmed — single IEA; no action-blocking evidence |
| Structural confirmation of active-site geometry | Relied on biochemical metal/mechanism data (PMID:12450410) and superfamily assignment; no crystal structure analyzed here | A structure would further cement the C-halide active-site chemistry vs a deaminase-type site | AtzA crystal structure / AlphaFold active-site comparison to known deaminases vs dehalogenases |
| PMID:22768133 content | Cited via UniProt/GOA as a second EXP support for GO:0018788 and "no deaminase activity with melamine"; abstract not independently retrieved in this run | It is one of the two EXP anchors for the correct term | Retrieve and verify PMID:22768133 abstract directly |

These gaps are provenance/confirmatory in nature; none of them provide any support for the seed C–N hypothesis.

---

## Discriminating Tests

Although the case is already resolved by existing primary literature, the following would most efficiently distinguish the C–Cl (true) from the C–N (seed) interpretation if independent confirmation were desired:

1. **Isotope-labeling re-confirmation (decisive, already done):** H₂¹⁸O assay → ¹⁸O incorporation into hydroxyatrazine confirms hydrolytic dechlorination (PMID:8759853). A deaminase would release ¹⁵N-labeled ammonia from the amino group instead.
2. **Substrate-panel specificity assay (decisive, already done):** Test AtzA on melamine/ammeline (C–N deaminase substrates) vs chloro-s-triazines (C–Cl substrates). AtzA is active only on halo-substituted substrates (PMID:11274097). Quantify chloride release (halide-selective electrode) vs ammonia release (Nessler/glutamate-dehydrogenase coupled assay) to directly read out bond class.
3. **Active-site structural comparison:** Solve/align AtzA structure (or high-confidence model) against amidohydrolase-superfamily deaminases (C–N) and dehalogenases (C–Cl); map metal coordination and substrate-positioning residues to the appropriate reaction class.
4. **Site-directed paralog swap:** The small set of residues that interconvert AtzA (dehalogenase) and melamine deaminase define the bond-class determinant; mutating them should toggle chloride-release vs ammonia-release activity, directly linking sequence to bond class.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Primary lead — action change:**
- **Action:** Remove (or mark NOT/down-rank) **GO:0016810** (IEA, GO_REF:0000002) on P72156. Rationale: disjoint-branch over-annotation from IPR011059 fold mapping; experimentally contradicted C–N activity.
- **Retain:** **GO:0018788** (atrazine chlorohydrolase activity) as the core MF — EC-correct (EC 3.8.1.8) and 2× EXP.
- **Retain (optional):** **GO:0016787** (hydrolase activity) as a true generic parent.

**Candidate references with exact snippets to verify:**
- [PMID:8759853](https://pubmed.ncbi.nlm.nih.gov/8759853/): *"The purified enzyme in H₂¹⁸O yielded [¹⁸O]hydroxyatrazine, indicating that AtzA is a chlorohydrolase and not an oxygenase."* → proves hydrolytic dechlorination (supports GO:0018788, refutes GO:0016810).
- [PMID:11274097](https://pubmed.ncbi.nlm.nih.gov/11274097/): *"AtzA was shown to exclusively catalyze dehalogenation of halo-substituted triazine ring compounds and had no activity with melamine and ammeline."* → proves absence of C–N (deaminase) activity (refutes GO:0016810).
- [PMID:12450410](https://pubmed.ncbi.nlm.nih.gov/12450410/): AtzA is "the first report... of a metal-dependent dechlorinating enzyme that proceeds via a hydrolytic mechanism" → supports hydrolytic C–Cl mechanism.

**Candidate replacement/relationship notes:**
- GO:0016810 and GO:0018788 are disjoint under GO:0016787 (not parent/child). Do not "generalize" GO:0018788 to GO:0016810; they are chemically distinct bond classes (EC 3.8 vs EC 3.5).

**Suggested questions for the curator:**
- Should the IPR011059 → GO:0016810 interpro2go mapping be flagged upstream, given it misannotates dehalogenase members of the amidohydrolase superfamily?
- Should a NOT-qualifier annotation (NOT GO:0016810) be added given explicit experimental evidence of absence of C–N activity, or is simple removal preferred by GOA policy?

**Suggested experiments:** See Discriminating Tests (isotope labeling and chloride-vs-ammonia release panels are the most direct and already partially in the literature).

---

## Conclusion

The seed hypothesis is **refuted**. AtzA (P72156) is an atrazine chlorohydrolase that hydrolyzes a carbon–chlorine bond (EC 3.8.1.8, GO:0018788), proven by H₂¹⁸O isotope labeling (PMID:8759853) and metal-reconstitution mechanism studies (PMID:12450410), and it explicitly lacks carbon–nitrogen (deaminase) activity (PMID:11274097). The GO:0016810 annotation is a single wrong-branch IEA arising from the IPR011059 amidohydrolase-superfamily fold mapping (GO_REF:0000002), inconsistent with both the enzyme's EC number (which correctly maps to GO:0018788) and its experimental record. **Recommended curation lead: remove GO:0016810; retain the doubly-EXP-supported GO:0018788 as the gene product's core molecular function.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)