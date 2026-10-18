---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T17:49:06.536478'
end_time: '2026-09-20T19:45:08.990577'
duration_seconds: 6962.45
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: 9POAL
  gene: NCGR_LOCUS1270
  gene_symbol: NCGR_LOCUS1270
  uniprot_accession: A0A811M8A5
  taxon_id: NCBITaxon:422564
  taxon_label: Miscanthus lutarioriparius
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0006000
  hypothesis_text: NCGR_LOCUS1270 of Miscanthus lutarioriparius participates in fructose
    metabolic process (GO:0006000). Establish its exact reaction and organellar role.
    Resolve whether this GO term includes metabolism of phosphorylated fructose derivatives
    by examining its definition and ontology ancestry, distinct from fructose 6-phosphate
    metabolic process GO:0006002. Separate broad-but-correct membership from a chemically
    different substrate claim.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/9POAL/NCGR_LOCUS1270/NCGR_LOCUS1270-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: NCGR_LOCUS1270 of Miscanthus lutarioriparius participates\
    \ in fructose metabolic process (GO:0006000).\n  Establish its exact reaction\
    \ and organellar role. Resolve whether this GO term includes metabolism of\n \
    \ phosphorylated fructose derivatives by examining its definition and ontology\
    \ ancestry, distinct from\n  fructose 6-phosphate metabolic process GO:0006002.\
    \ Separate broad-but-correct membership from a chemically\n  different substrate\
    \ claim.\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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

- **Organism code:** 9POAL
- **Taxon:** Miscanthus lutarioriparius (NCBITaxon:422564)
- **Gene directory:** NCGR_LOCUS1270
- **Gene symbol:** NCGR_LOCUS1270
- **UniProt accession:** A0A811M8A5

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0006000
- **Source file:** genes/9POAL/NCGR_LOCUS1270/NCGR_LOCUS1270-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

NCGR_LOCUS1270 of Miscanthus lutarioriparius participates in fructose metabolic process (GO:0006000). Establish its exact reaction and organellar role. Resolve whether this GO term includes metabolism of phosphorylated fructose derivatives by examining its definition and ontology ancestry, distinct from fructose 6-phosphate metabolic process GO:0006002. Separate broad-but-correct membership from a chemically different substrate claim.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: NCGR_LOCUS1270 of Miscanthus lutarioriparius participates in fructose metabolic process (GO:0006000).
  Establish its exact reaction and organellar role. Resolve whether this GO term includes metabolism of
  phosphorylated fructose derivatives by examining its definition and ontology ancestry, distinct from
  fructose 6-phosphate metabolic process GO:0006002. Separate broad-but-correct membership from a chemically
  different substrate claim.
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

**Target gene:** NCGR_LOCUS1270 (UniProt **A0A811M8A5**), *Miscanthus lutarioriparius* (organism code 9POAL; NCBITaxon:422564)
**Focus type:** function_assignment · **Hypothesis slug:** function-hypothesis-go-0006000
**Seed hypothesis:** NCGR_LOCUS1270 participates in **fructose metabolic process (GO:0006000)**. Establish its exact reaction and organellar role, and resolve whether GO:0006000 encompasses metabolism of phosphorylated fructose derivatives (distinct from fructose 6-phosphate metabolic process, GO:0006002).

---

## Summary

**Executive judgment: OVER-ANNOTATED — refute the GO:0006000 substrate claim; remove or demote it as a direct annotation.** NCGR_LOCUS1270 / A0A811M8A5 is a **chloroplast-stromal, thioredoxin-regulated Fructose-1,6-bisphosphatase (FBPase; EC 3.1.3.11)** — a Calvin–Benson–Bassham (CBB) cycle enzyme. Its single characterized reaction is the Mg²⁺-dependent hydrolysis of **β-D-fructose 1,6-bisphosphate + H₂O → β-D-fructose 6-phosphate + phosphate** (RHEA:11064). Both the substrate and the product are **phosphorylated fructose derivatives**; the enzyme has no described activity on free (non-phosphorylated) fructose.

The seed hypothesis poses a precise ontological question: does **GO:0006000 (fructose metabolic process)** — defined for *free* fructose, "the ketohexose arabino-2-hexulose … found free in … fruits and honey" — properly cover an enzyme that only ever touches phosphorylated fructose intermediates? Direct inspection of the GO ontology answers **no**. GO:0006000 sits on the `hexose → monosaccharide → carbohydrate` (`is_a`) branch, whereas the process terms this enzyme genuinely performs — **GO:0006002 (fructose 6-phosphate metabolic process)** and **GO:0030388 (fructose 1,6-bisphosphate metabolic process)** — sit on the separate **carbohydrate-derivative / organophosphate / phosphorus** branch (`GO:1901135 → GO:0019637 → GO:0006793`). A programmatic ancestry check confirms GO:0006000 is **not** an `is_a` ancestor of GO:0006002 or GO:0030388; their only shared ancestors are the top-level roots (GO:0008150, GO:0009987, GO:0008152).

The curation consequence is direct: the **GO:0006000 annotation is a chemically distinct, over-broad substrate claim** — most consistent with automated over-propagation (an IEA/TreeGrafter/PANTHER-family transfer that lumped "fructose" and "fructose-phosphate" processes together). It should be **removed or demoted** in favor of the terms that reflect the actual reaction: **GO:0042132 (fructose 1,6-bisphosphate 1-phosphatase activity, MF)**, **GO:0030388 / GO:0006002 (BP)**, the pathway term **GO:0019253 (reductive pentose-phosphate cycle / Calvin cycle)**, and the CC term **chloroplast / plastid stroma**. The most important caveat is that no *M. lutarioriparius*-specific enzymatic assay exists for this exact protein; the assignment rests on UniProt annotation, concordant domain models, diagnostic sequence features, and strong orthology to well-characterized plant chloroplast FBPases.

---

## Key Findings

### Finding 1 — A0A811M8A5 is a chloroplast Fructose-1,6-bisphosphatase (EC 3.1.3.11) acting only on phosphorylated substrates

The UniProt TrEMBL record for A0A811M8A5 (*M. lutarioriparius*, 411 aa) carries the recommended name **Fructose-bisphosphatase (EC 3.1.3.11)** with the catalytic activity **β-D-fructose 1,6-bisphosphate + H₂O = β-D-fructose 6-phosphate + phosphate (RHEA:11064)**. The domain architecture is unambiguous and diagnostic of the class-1 FBPase family:

| Signature type | Identifier | Meaning |
|---|---|---|
| Pfam | PF00316 + PF18913 | FBPase catalytic + FBPase_C domains |
| HAMAP | MF_01855 | FBPase class 1 |
| CDD | cd00354 | FBPase |
| PANTHER | PTHR11556:SF1 | FBPase subfamily |
| PROSITE | PS00124 | FBPase active-site signature |
| InterPro | IPR000146 | FBPase class-1 |

UniProt keywords include **Calvin cycle, Chloroplast, Plastid, Transit peptide, Disulfide bond, Magnesium**, and the subcellular location is annotated **Plastid, chloroplast** with an N-terminal chloroplast transit peptide. Critically, **both the substrate (fructose 1,6-bisphosphate) and the product (fructose 6-phosphate) are phosphorylated**; free fructose is never a substrate or product. This is the crux of the seed hypothesis — the enzyme's chemistry is confined to phosphorylated fructose derivatives.

Primary literature confirms the biological context. Chloroplast FBPase catalyzes one of the two essentially irreversible dephosphorylation reactions of the CBB cycle and is a canonical redox-regulated target of the ferredoxin/thioredoxin system: *"Fructose-1,6-bisphosphatase (FBPase) and sedoheptulose-1,7-bisphosphatase (SBPase) are two essential activities in the Calvin-Benson-Bassham cycle that catalyze two irreversible reactions and are key for proper regulation and functioning of the cycle"* ([PMID: 36518499](https://pubmed.ncbi.nlm.nih.gov/36518499/)). The light-dependent, thioredoxin-mediated activation is documented in vivo: *"The light-dependent reduction of Calvin-Benson cycle enzymes fructose 1,6-bisphosphatase (FBPase) and sedoheptulose 1,7-bisphosphatase (SBPase) was partially impaired in the FTR-knockdown ftrb mutant"* ([PMID: 38305687](https://pubmed.ncbi.nlm.nih.gov/38305687/)).

### Finding 2 — GO:0006000 is a chemically distinct branch, NOT an ancestor of the phosphorylated-fructose process terms

This is the decisive ontological finding. Using the QuickGO ontology (relations = `is_a`):

- **GO:0006000 (fructose metabolic process)** is defined as *"chemical reactions and pathways involving fructose, the ketohexose arabino-2-hexulose … found free in … fruits and honey."* Its `is_a` ancestry runs **GO:0006000 → GO:0019318 (hexose metabolic) → GO:0005996 (monosaccharide metabolic) → GO:0005975 (carbohydrate metabolic)**.
- **GO:0006002 (fructose 6-phosphate metabolic process)** and **GO:0030388 (fructose 1,6-bisphosphate metabolic process)** run through **GO:0019637 (organophosphate metabolic) → GO:1901135 (carbohydrate DERIVATIVE metabolic) → GO:0006793 (phosphorus metabolic)**.

A programmatic ancestry check confirms: **GO:0006000 is NOT an `is_a` ancestor of GO:0006002 (False) nor of GO:0030388 (False).** The only shared ancestors between GO:0006000 and the phosphorylated-fructose terms are the top-level roots (GO:0008150 biological_process, GO:0009987 cellular process, GO:0008152 metabolic process). In GO's chemical logic, a *phosphorylated derivative* of a molecule is treated as a **distinct chemical species** from the free molecule — hence fructose-phosphate processes are deliberately filed under "carbohydrate derivative," not under "fructose."

The seed hypothesis explicitly asked whether GO:0006000 "includes metabolism of phosphorylated fructose derivatives." The ontology's own structure answers **no**: annotating this enzyme to GO:0006000 asserts involvement in *free-fructose* metabolism, which the enzyme does not perform. This resolves the two readings the seed hypothesis flagged — "broad-but-correct membership" versus "a chemically different substrate claim" — decisively in favor of the latter.

### Finding 3 — Sequence features confirm the chloroplastic, redox-regulated isoform (not the cytosolic/gluconeogenic FBPase)

Direct analysis of the 411-aa sequence pins down which FBPase isoform this is — an important discrimination because plants encode both a **cytosolic** FBPase (gluconeogenesis/sucrose synthesis; allosterically regulated by fructose-2,6-bisphosphate) and a **chloroplast-stromal** FBPase (Calvin cycle; redox-regulated by thioredoxin):

1. **Chloroplast transit peptide:** the N-terminal residues 1–50 contain **0 acidic residues (D+E = 0)** and are **40% S+A+T**, with an Ala-rich start (MAAAAAT…) — the canonical amino-acid composition of a chloroplast transit peptide.
2. **Conserved catalytic motif:** the FBPase substrate-binding/catalytic motif **FDPLDGS** is present at position 182.
3. **Diagnostic redox disulfide:** a **C227–C232 (CxxxxC, sequence CIVSVC)** cysteine pair sits in the regulatory-loop region, matching the **redox-active disulfide that distinguishes the plastidic thioredoxin-regulated FBPase** from the cytosolic isoform (which lacks this insertion loop).

UniProt independently annotates a Disulfide bond plus Calvin cycle and Plastid/chloroplast keywords, consistent with this analysis. Together these features establish that A0A811M8A5 is specifically the **stromal Calvin-cycle FBPase**, whose entire physiological role is the dephosphorylation of fructose-1,6-bisphosphate during photosynthetic carbon reduction — reinforcing that free fructose is not part of its chemistry.

---

## Mechanistic Model / Interpretation

The gene product operates in the **regeneration/reduction phase of the Calvin–Benson–Bassham cycle** inside the chloroplast stroma. In the light, reduced ferredoxin passes electrons via ferredoxin-thioredoxin reductase (FTR) to thioredoxin, which reduces the **C227–C232 regulatory disulfide**, activating the enzyme. The activated FBPase then catalyzes:

```
   β-D-fructose 1,6-bisphosphate + H2O
                 │   (chloroplast FBPase, EC 3.1.3.11, Mg2+-dependent, Trx-activated)
                 ▼
   β-D-fructose 6-phosphate + Pi
```

Both metabolites are **phosphorylated**. The product, fructose-6-phosphate, feeds back into the regenerative reactions and into starch/sucrose biosynthesis — but it is *never* dephosphorylated to free fructose by this enzyme. The step is one of the two irreversible, redox-gated control points of the cycle ([PMID: 36518499](https://pubmed.ncbi.nlm.nih.gov/36518499/)).

```
GO ancestry (is_a), simplified:

  GO:0008152 metabolic process
        │
        ├── GO:0005975 carbohydrate metabolic
        │        └── GO:0005996 monosaccharide metabolic
        │                 └── GO:0019318 hexose metabolic
        │                          └── GO:0006000 fructose metabolic   ← FREE fructose (SEED TERM)
        │
        └── GO:0006793 phosphorus metabolic
                 └── GO:0019637 organophosphate metabolic
                          └── GO:1901135 carbohydrate DERIVATIVE metabolic
                                   ├── GO:0006002 fructose 6-phosphate metabolic   ← enzyme PRODUCT
                                   └── GO:0030388 fructose 1,6-bisphosphate metabolic ← enzyme SUBSTRATE

  ⇒ GO:0006000 and GO:0006002/GO:0030388 share ONLY the root ancestors.
    GO:0006000 is NOT a parent of the terms this enzyme actually performs.
```

**Ontological mapping of the mechanism to GO terms:**

| Aspect | Correct GO term | Status vs. seed |
|---|---|---|
| Molecular function | GO:0042132 fructose 1,6-bisphosphate 1-phosphatase activity (MF) | Primary MF — retain |
| Substrate process | GO:0030388 fructose 1,6-bisphosphate metabolic process (BP) | Retain |
| Product process | GO:0006002 fructose 6-phosphate metabolic process (BP) | Retain |
| Pathway | GO:0019253 reductive pentose-phosphate cycle / Calvin cycle (BP) | Add / verify |
| Location | GO:0009507 chloroplast / plastid stroma (CC) | Retain |
| **Seed term** | **GO:0006000 fructose metabolic process (BP)** | **Chemically distinct → REMOVE / demote** |

The seed term GO:0006000 fails on chemistry (free vs. phosphorylated fructose) and fails on ontology structure (separate `is_a` branch). It is best interpreted as an **over-annotation** rather than a broad-but-true ancestor.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt A0A811M8A5 (database) | Review/database | Refutes seed substrate claim; supports FBPase identity | Enzyme reaction & localization | EC 3.1.3.11; RHEA:11064 (FBP → F6P + Pi); Plastid/chloroplast; transit peptide; disulfide; Calvin cycle | *M. lutarioriparius*, 411 aa | High for identity; TrEMBL (unreviewed), computationally annotated |
| InterPro/Pfam/HAMAP/PANTHER (database) | Computational/structural | Supports FBPase class-1 identity | Domain family robustness | PF00316+PF18913, MF_01855, cd00354, PTHR11556:SF1, PS00124, IPR000146 | Sequence-based | High; concordant family models |
| Sequence feature analysis (this study) | Computational/evolutionary | Supports plastidic (not cytosolic) isoform | Which FBPase isoform | Transit peptide (D+E=0, 40% SAT); FDPLDGS motif; C227–C232 redox loop | 411-aa protein | High for isoform; motif-based inference |
| QuickGO ontology check (this study) | Computational/database | Refutes GO:0006000 as ancestor of phospho-fructose terms | Ontology ancestry | GO:0006000 NOT `is_a` ancestor of GO:0006002/GO:0030388; separate branches | GO ontology | High; deterministic ontology query |
| [PMID: 36518499](https://pubmed.ncbi.nlm.nih.gov/36518499/) | Review/primary | Supports Calvin-cycle role & substrate | FBPase function in CBB | FBPase catalyzes an irreversible CBB-cycle reaction | Chloroplast/cyanobacteria | High for pathway role |
| [PMID: 38305687](https://pubmed.ncbi.nlm.nih.gov/38305687/) | Direct (in vivo redox) | Supports redox-regulated chloroplast FBPase | Thioredoxin regulation | Light-dependent FBPase reduction impaired in FTR-knockdown *ftrb* | Plant chloroplast | High; matches C227–C232 disulfide |
| [PMID: 34618018](https://pubmed.ncbi.nlm.nih.gov/34618018/) | Direct (redox/activity) | Qualifies (regulation) | CBB redox regulation conserved | FBP/SBPase oxidation impairs activity on TrxA depletion | *Synechocystis* | Medium; bifunctional cyanobacterial enzyme |
| [PMID: 32545358](https://pubmed.ncbi.nlm.nih.gov/32545358/) | Interaction/proteomics | Qualifies (regulation) | Trx-target interaction | FBPase identified as thioredoxin target in chloroplast interactome | *Arabidopsis* | Medium; supports regulation, not substrate |
| [PMID: 28470336](https://pubmed.ncbi.nlm.nih.gov/28470336/) | Transgenic phenotype | Qualifies (downstream) | Bisphosphatase → carbon assimilation | Chloroplast FBP/SBPase increased starch and growth | *Arabidopsis* | Downstream phenotype, not direct MF |
| [PMID: 25602028](https://pubmed.ncbi.nlm.nih.gov/25602028/) | Mutant phenotype | Competing (cytosolic isoform) | Distinguish cytosolic FBPase | Fru-2,6-P2 allosterically modulates *cytosolic* FBPase | *Arabidopsis* | Medium; highlights the isoform this gene is NOT |

---

## GO Curation Implications

**Lead requiring curator verification.** The evidence supports the following action for the **GO:0006000 (fructose metabolic process)** annotation on NCGR_LOCUS1270 / A0A811M8A5:

- **Action: REMOVE or DEMOTE (do not accept as a supported BP).** GO:0006000 is defined for *free* fructose and, by `is_a` ancestry, sits on a separate ontology branch from the phosphorylated-fructose process terms the enzyme actually performs. It is a chemically distinct substrate claim, not a broad-but-correct ancestor. The pattern (broad "fructose" process on a phospho-fructose enzyme) is characteristic of **automated over-propagation** (PANTHER/TreeGrafter family transfer).

**GO decision table (leads):**

| GO ID | Term | Aspect | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0042132 | fructose 1,6-bisphosphate 1-phosphatase activity | MF | **RETAIN** | Exact reaction (= EC 3.1.3.11, RHEA:11064); most informative MF |
| GO:0030388 | fructose 1,6-bisphosphate metabolic process | BP | **RETAIN** | Direct substrate process (organophosphate branch) |
| GO:0006002 | fructose 6-phosphate metabolic process | BP | **RETAIN** | Direct product process (organophosphate branch) |
| **GO:0006000** | **fructose metabolic process** | BP | **REMOVE / NON-CORE** | **Free-fructose branch; chemically distinct — focus of this hypothesis** |
| GO:0019253 | reductive pentose-phosphate cycle (Calvin cycle) | BP | **ADD / VERIFY** | Precise pathway for the plastidic redox-regulated isoform |
| GO:0006094 | gluconeogenesis | BP | **SCRUTINIZE / REMOVE** | Describes the cytosolic paralog; likely family carry-over |
| GO:0009507 | chloroplast | CC | **RETAIN** | Transit peptide + redox loop confirm plastid localization |
| GO:0005829 | cytosol | CC | **SCRUTINIZE / REMOVE** | Contradicts transit peptide + C227–C232 disulfide |

Do **not** fall back on "protein binding" for this gene; a specific, informative MF term (**GO:0042132**) is fully supported.

---

## Mechanistic Scope

**Immediate molecular function tested (direct):** Mg²⁺-dependent hydrolysis of the 1-phosphate from D-fructose-1,6-bisphosphate, yielding D-fructose-6-phosphate + Pi (EC 3.1.3.11 / GO:0042132), redox-activated in the light via the ferredoxin/thioredoxin system.

**What is NOT the immediate function:**
- **Metabolism of free fructose** (the seed term's implied chemistry) — no evidence; contradicted by the defined reaction. GO:0006000 would require a fructokinase, fructose transporter, or fructose-releasing hydrolase activity, none of which is supported by sequence, domain, or reaction evidence.
- **Downstream outcomes** — carbon partitioning, starch/sucrose levels, photosynthetic induction, growth/yield ([PMID: 28470336](https://pubmed.ncbi.nlm.nih.gov/28470336/), [PMID: 25602028](https://pubmed.ncbi.nlm.nih.gov/25602028/)) are pathway consequences of altered CBB flux, not the molecular function.
- **Redox regulation by thioredoxin** — a modulatory input to activity, not the catalytic function itself.

---

## Conflicts and Alternatives

1. **Isoform confusion (cytosolic vs. plastidic FBPase).** Plants have two FBPases with different regulation and location; the cytosolic isoform is allosterically controlled by fructose-2,6-bisphosphate ([PMID: 25602028](https://pubmed.ncbi.nlm.nih.gov/25602028/)). Sequence features (transit peptide, C227–C232 redox loop) place A0A811M8A5 firmly in the **plastidic** class. Notably, the GO:0006000 conclusion holds either way, since **neither** isoform metabolizes free fructose.
2. **Database carry-over / automated over-annotation.** PANTHER family PTHR11556 groups chloroplastic and cytosolic FBPases; TreeGrafter can propagate a broad BP set (including GO:0006000, gluconeogenesis, and a cytosol CC) from the family node. GO:0006000 (and possibly GO:0005829 cytosol) are likely family-level carry-over, not experimental truths.
3. **Semantic trap.** "Fructose 6-phosphate" and "fructose 1,6-bisphosphate" contain the word "fructose," which can motivate an erroneous roll-up to "fructose metabolic process." The ontology explicitly separates phosphorylated forms into the carbohydrate-derivative branch, invalidating the roll-up.
4. **Bifunctional FBP/SBPase in cyanobacteria** ([PMID: 34618018](https://pubmed.ncbi.nlm.nih.gov/34618018/)) differs from the monofunctional plant chloroplast FBPase; regulatory detail transfers, substrate conclusion is unchanged.
5. **No organism-specific assay.** Identity rests on orthology and domain models; this caps confidence for positive MF assertions at "well-supported by orthology," not "experimentally verified in *Miscanthus*."

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct enzymatic assay for A0A811M8A5 | UniProt reaction is computational (TrEMBL/ARBA/HAMAP) | Confirms substrate specificity in *this* species | Recombinant expression + phosphatase assay on FBP vs. F6P vs. free fructose |
| Localization not experimentally verified in *Miscanthus* | Transit peptide predicted from sequence; UniProt CC inferred | Confirms chloroplast-stromal role | GFP fusion / chloroplast proteomics; TargetP/ChloroP run |
| Isoform assignment inferred from motifs | C227–C232 loop, transit peptide composition | Distinguishes plastidic vs. cytosolic | Phylogenetic placement with characterized plant FBPases |
| GO:0006000 provenance not directly inspected in the review YAML | Ontology structure and chemistry assessed | Determines whether it is IEA over-propagation vs. curated | Check the annotation's evidence code and source in the gene-review record |
| Redox activation not measured for this protein | Inferred from disulfide + orthologs | Confirms Calvin-cycle regulatory identity | Thioredoxin activation assay on redox state / activity |

---

## Discriminating Tests

1. **Substrate-specificity assay (decisive):** express recombinant A0A811M8A5 and measure phosphatase activity against **fructose-1,6-bisphosphate**, **fructose-6-phosphate**, and **free fructose**. Expectation: activity only on FBP (→ F6P + Pi), none on free fructose — directly refuting GO:0006000's substrate implication.
2. **Sequence-targeting analysis** (TargetP2/ChloroP) to confirm the plastid transit peptide and rule out the cytosolic isoform → decides GO:0009507 vs. GO:0005829 and Calvin vs. gluconeogenesis BP.
3. **Redox/thioredoxin activation:** test light/thioredoxin-dependent activation and the requirement of C227/C232 (cysteine-to-serine mutants).
4. **Phylogenetic discrimination:** build a tree with characterized plant cytosolic (cyFBPase) and chloroplast (FBP1, redox-regulated) FBPases to lock the isoform call.
5. **Annotation provenance audit:** inspect the evidence code/source of the GO:0006000 assertion in the gene-review record to confirm it is an IEA/TreeGrafter transfer.

---

## Curation Leads (require curator verification)

- **Action change:** Downgrade/remove **GO:0006000** as a direct annotation for A0A811M8A5; label as over-broad IEA/TreeGrafter propagation representing a chemically distinct substrate (free fructose) the enzyme does not act on.
- **Preferred terms to keep/assert:** MF **GO:0042132** (exact reaction); BP **GO:0030388** and **GO:0006002** (substrate/product-correct); add/verify **GO:0019253** (Calvin cycle); CC **GO:0009507** (chloroplast); scrutinize/remove GO:0005829 (cytosol) and GO:0006094 (gluconeogenesis) as cytosolic-paralog carry-over.
- **Candidate references with exact snippets to verify:**
  - [PMID: 36518499](https://pubmed.ncbi.nlm.nih.gov/36518499/): *"Fructose-1,6-bisphosphatase (FBPase) and sedoheptulose-1,7-bisphosphatase (SBPase) are two essential activities in the Calvin-Benson-Bassham cycle that catalyze two irreversible reactions…"*
  - [PMID: 38305687](https://pubmed.ncbi.nlm.nih.gov/38305687/): *"The light-dependent reduction of Calvin-Benson cycle enzymes fructose 1,6-bisphosphatase (FBPase) and sedoheptulose 1,7-bisphosphatase (SBPase) was partially impaired in the FTR-knockdown ftrb mutant."*
  - [PMID: 28470336](https://pubmed.ncbi.nlm.nih.gov/28470336/): bisphosphatase activity → carbon assimilation (downstream — do NOT use for MF).
- **Suggested curator questions:** (1) Is this the chloroplastic (FBP1) or cytosolic isoform? (2) Should GO:0006000 be removed project-wide from FBPase entries as a mis-generalization? (3) Should GO:0019253 (Calvin cycle) be added for FBPase entries bearing transit peptides?
- **Suggested experiments:** recombinant FBPase substrate-specificity assay + TargetP localization to close the primary gaps.

---

## Proposed Follow-up Actions

1. **Apply the curation lead:** remove/demote GO:0006000; retain GO:0042132, GO:0030388, GO:0006002; add GO:0019253; scrutinize GO:0005829 and GO:0006094.
2. **Audit sibling FBPase entries** in the AIGR corpus for the same GO:0006000 over-propagation pattern (likely a systematic TreeGrafter artifact worth a batch fix).
3. **Run orthogonal localization prediction** (TargetP2/ChloroP) and a focused phylogeny to lock the plastidic-isoform call with reproducible provenance.
4. **Flag for experimental follow-up** the recombinant substrate-specificity assay as the single decisive test that would convert the orthology-based call into direct evidence.

---

## Provenance

- UniProt REST record `A0A811M8A5` — names, EC, catalytic activity (RHEA:11064), domain models, keywords, subcellular location, sequence.
- QuickGO ontology REST — definitions and `is_a` ancestors for GO:0006000, GO:0006002, GO:0030388, GO:0042132, GO:0019318.
- In-session logical check: GO:0006000 is NOT an `is_a` ancestor of GO:0006002 (False) or GO:0030388 (False); shared ancestors limited to the top-level roots.
- In-session sequence analysis of the 411-aa protein — transit-peptide composition, FDPLDGS catalytic motif at position 182, C227–C232 CxxxxC regulatory disulfide.
- PubMed searches on chloroplast FBPase, Calvin cycle, and thioredoxin redox regulation.

---

### Conclusion

NCGR_LOCUS1270 (A0A811M8A5) is a chloroplast-stromal, thioredoxin-regulated Fructose-1,6-bisphosphatase (EC 3.1.3.11) whose only reaction converts fructose-1,6-bisphosphate to fructose-6-phosphate — both phosphorylated species. Because GO:0006000 (fructose metabolic process) is defined for *free* fructose and lies on a separate ontology branch from the phospho-fructose process terms the enzyme actually performs, the GO:0006000 annotation is an **over-broad, chemically distinct over-annotation that should be removed or demoted**, retaining the more accurate MF/BP/CC and Calvin-cycle terms.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)