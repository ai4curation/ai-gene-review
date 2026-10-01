---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T18:34:41.656388'
end_time: '2026-09-20T18:52:25.877308'
duration_seconds: 1064.22
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: carD
  gene_symbol: carD
  uniprot_accession: Q9TX43
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0007189
  hypothesis_text: Dictyostelium discoideum CAR4/carD participates in adenylate cyclase-activating
    G protein-coupled receptor signaling (GO:0007189). Compare receptor-stage/paralog
    specificity and assess direct cyclase measurements versus developmental phenotypes.
    Distinguish published experiments from unpublished observations quoted in a paper.
    A GSK3-linked function does not by itself exclude cyclase activation.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DICDI/carD/carD-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Dictyostelium discoideum CAR4/carD participates\
    \ in adenylate cyclase-activating G protein-coupled\n  receptor signaling (GO:0007189).\
    \ Compare receptor-stage/paralog specificity and assess direct cyclase\n  measurements\
    \ versus developmental phenotypes. Distinguish published experiments from unpublished\
    \ observations\n  quoted in a paper. A GSK3-linked function does not by itself\
    \ exclude cyclase activation.\nfocus_type: function_assignment\ncontext: []\n\
    reference_id: []"
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
citation_count: 10
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
- filename: provenance_carD_GO0007189_evidence_matrix.csv
  path: openscientist_artifacts/provenance_carD_GO0007189_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist carD GO0007189 evidence matrix
- filename: provenance_carD_quickgo_annotations.csv
  path: openscientist_artifacts/provenance_carD_quickgo_annotations.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist carD quickgo annotations
- filename: provenance_carD_uniprot_GO_evidence.csv
  path: openscientist_artifacts/provenance_carD_uniprot_GO_evidence.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist carD uniprot GO evidence
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** DICDI
- **Taxon:** Dictyostelium discoideum (NCBITaxon:44689)
- **Gene directory:** carD
- **Gene symbol:** carD
- **UniProt accession:** Q9TX43

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0007189
- **Source file:** genes/DICDI/carD/carD-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Dictyostelium discoideum CAR4/carD participates in adenylate cyclase-activating G protein-coupled receptor signaling (GO:0007189). Compare receptor-stage/paralog specificity and assess direct cyclase measurements versus developmental phenotypes. Distinguish published experiments from unpublished observations quoted in a paper. A GSK3-linked function does not by itself exclude cyclase activation.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Dictyostelium discoideum CAR4/carD participates in adenylate cyclase-activating G protein-coupled
  receptor signaling (GO:0007189). Compare receptor-stage/paralog specificity and assess direct cyclase
  measurements versus developmental phenotypes. Distinguish published experiments from unpublished observations
  quoted in a paper. A GSK3-linked function does not by itself exclude cyclase activation.
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

# AIGR Gene Hypothesis Deep Research — *Dictyostelium discoideum* carD / cAR4 and GO:0007189

**Target gene:** carD / cAR4 (cyclic-AMP receptor 4), *Dictyostelium discoideum* (DICDI, NCBITaxon:44689)
**UniProt:** Q9TX43
**Focus:** function_assignment — does cAR4 directly participate in *adenylate cyclase-activating G protein-coupled receptor signaling pathway* (GO:0007189)?
**Hypothesis slug:** function-hypothesis-go-0007189

---

## Executive Judgment

**Verdict: Weakly supported / likely over-annotation by paralog carry-over.**

The GO:0007189 annotation on carD/cAR4 is not backed by any receptor-specific experimental evidence. Public annotation records (UniProt, EBI QuickGO) show that GO:0007189 is assigned to Q9TX43 **only** by PAINT phylogenetic inference (evidence code IBA / ECO:0000318 / GO_REF:0000033, assigned by GO_Central). It is a family-level annotation propagated across the entire *Dictyostelium* cAMP-receptor (cAR) clade rather than a statement grounded in a direct cAR4 assay.

The experimental basis for "cAMP receptor activates adenylyl cyclase" in this organism comes from the **aggregation-stage receptors cAR1 and cAR3**, characterized in car1⁻/gα2⁻ cells (Pupillo et al. 1992, [PMID: 1333842](https://pubmed.ncbi.nlm.nih.gov/1333842/)) and in constitutive-expression/chimera studies of cAR1/cAR2/cAR3 (Kim et al. 1998, [PMID: 9578623](https://pubmed.ncbi.nlm.nih.gov/9578623/)). **cAR4 was not included in any of these direct adenylyl-cyclase assays.** The single statement in the literature asserting that cAR4 itself can activate adenylyl cyclase is explicitly flagged as an **unpublished observation** ("A.R. Kimmel, unpubl.") inside the discussion of Ginsburg & Kimmel 1997 ([PMID: 9284050](https://pubmed.ncbi.nlm.nih.gov/9284050/)) — it is not a reported experiment.

The **experimentally characterized** function of cAR4 is late-development axial patterning (prestalk/prespore cell-fate decisions) through G-protein-coupled signaling that is *antagonistic* to the cAR1/cAR3→ZAK1→GSK3 arm, consistent with cAR4's curated MF annotation as a protein tyrosine phosphatase activator (GO:0008160, TAS). The seed hypothesis correctly notes that a GSK3-linked function does not by itself exclude cyclase activation — and indeed it does not — but the absence of any direct cAR4 cyclase measurement, combined with cAR4's post-relay expression window, means the cyclase-activation claim remains unproven for this specific receptor. **Recommended curation stance: treat GO:0007189 as non-core, family-level IBA; do not upgrade to an experimental evidence code without a direct cAR4 cyclase reconstitution assay.**

---

## Key Findings

### F001 — GO:0007189 on carD/cAR4 is a family-level IBA annotation, not receptor-specific experimental evidence

Inspection of the UniProt Q9TX43 GO cross-references shows that GO:0007189 (*adenylate cyclase-activating G protein-coupled receptor signaling pathway*) is assigned with evidence code **IBA:GO_Central** — Inferred from Biological aspect of Ancestor, produced by the PANTHER/PAINT phylogenetic pipeline. This is a propagated, ancestor-based inference, not a curated experimental annotation for cAR4.

By contrast, the receptor's directly supported annotations carry experimental or curator-reviewed evidence codes: cAMP binding (GO:0030552, **IDA**), cAMP receptor activity (GO:0001646, ISS), protein tyrosine phosphatase activator activity (GO:0008160, **TAS**), and multiple **IMP** developmental biological-process terms (cell differentiation, culmination, positive/negative regulation of gene expression). Crucially, there is **no IDA/IMP/IGI-level experimental support for adenylate cyclase activation by cAR4**. The strongest, most specific evidence on this protein points to cAMP binding and to developmental patterning — not to cyclase activation.

### F002 — Experimentally characterized cAR4 function is late-development patterning via GSK3 antagonism, not cAMP relay / adenylate cyclase activation

The founding characterization of the gene (Louis, Ginsburg & Kimmel 1994, [PMID: 7958880](https://pubmed.ncbi.nlm.nih.gov/7958880/)) established that CAR4 mRNA first appears at tip elongation and accumulates through culmination, with maximal expression in the pseudoplasmodium anterior. car4-null cells progress **normally through early development (aggregation)** but show anteroposterior patterning defects: reduced prestalk gene expression, with prespore markers overexpressed and mislocalized into zones normally restricted to prestalk cells.

Ginsburg & Kimmel 1997 ([PMID: 9284050](https://pubmed.ncbi.nlm.nih.gov/9284050/)) showed that cAR4 signaling is **antagonistic** to the positive intracellular signals of cAR1 and/or cAR3, and that these CAR-mediated pathways converge on the serine/threonine kinase GSK3. Kim, Liu & Kimmel 1999 ([PMID: 10571182](https://pubmed.ncbi.nlm.nih.gov/10571182/)) and the Weeks 2000 review ([PMID: 11121784](https://pubmed.ncbi.nlm.nih.gov/11121784/)) established that cAR3 *activates* GSK3 via the tyrosine kinase ZAK1, while cAR4 acts oppositely (linked to a protein tyrosine phosphatase, consistent with UniProt GO:0008160, TAS). **None** of these primary papers report a direct adenylyl-cyclase-activation assay for cAR4; the entire evidence base is developmental/gene-expression phenotype plus GSK3-pathway coupling.

### F003 — cAMP receptor subtypes can mediate adenylyl cyclase activation at different agonist concentrations, but cAR4 itself was not assayed

Kim, Borleis & Devreotes 1998 ([PMID: 9578623](https://pubmed.ncbi.nlm.nih.gov/9578623/)) constitutively expressed cAR1, cAR2 and cAR3 (plus chimeric and mutant receptors) and showed that all can mediate identical aggregation-stage responses — including activation of adenylyl cyclase — differing only in the cAMP concentration range they sense (matching their intrinsic affinities). This is the strongest "common responses" argument for extending cyclase activation across the receptor family. However, the receptors directly tested were **cAR1, cAR2 and cAR3**; **cAR4 (carD) was NOT included** in the adenylyl-cyclase-activation experiments. The "common function" evidence therefore reaches a low-affinity paralog (cAR2) but does *not* directly touch cAR4.

### F004 — The claim that cAR4 activates adenylate cyclase rests on an UNPUBLISHED observation

The full text of Ginsburg & Kimmel 1997 (Genes & Development; PMC316452, [PMID: 9284050](https://pubmed.ncbi.nlm.nih.gov/9284050/)) states verbatim:

> "Although their dose-dependent responses to cAMP may differ, all of the CARs may be capable of adenylyl cyclase activation (Pupillo et al. 1992; A.R. Kimmel, unpubl.) and, hence, PKA activation."

The same paper cautions: *"it is difficult to predict definitively which specific intracellular responses are affected by the loss of CAR4, a low-affinity receptor."* The **published** citation embedded there — Pupillo, Insall, Pitt & Devreotes 1992 ([PMID: 1333842](https://pubmed.ncbi.nlm.nih.gov/1333842/)) — used car1⁻ and gα2⁻ aggregation-competent cells to show that "cAR1 and another cAMP receptor are linked to activation of adenylyl cyclase." At the aggregation stage, that "other" receptor is cAR3; cAR4, expressed only later at tip/culmination, was **not tested**. Thus the extension of adenylyl-cyclase-activation to cAR4 is explicitly attributed in the source to an **unpublished observation (A.R. Kimmel, unpubl.)**, while the peer-reviewed experiment concerns cAR1/cAR3. This is exactly the "published experiment vs. unpublished observation quoted in a paper" distinction the seed hypothesis asked us to make — and it resolves against a published cAR4 experiment.

### F005 — QuickGO confirms GO:0007189 is a PAINT phylogenetic annotation; the informative parent term already exists

The EBI QuickGO annotation API for Q9TX43 (23 annotations) returns GO:0007189 with evidence **IBA / ECO:0000318 / GO_REF:0000033, assigned by GO_Central** — the standard PAINT phylogenetic-inference reference, not an experimental annotation. The more specific, experimentally anchored annotations are GO:0030552 cAMP binding (IDA, [PMID: 2722797](https://pubmed.ncbi.nlm.nih.gov/2722797/)), GO:0008160 protein tyrosine phosphatase activator activity (TAS, [PMID: 12408804](https://pubmed.ncbi.nlm.nih.gov/12408804/)), and four IMP developmental BP terms all from [PMID: 7958880](https://pubmed.ncbi.nlm.nih.gov/7958880/). Importantly, the **parent process term GO:0007186** (*G protein-coupled receptor signaling pathway*) is already present on carD as IEA (GO_REF:0000002, InterPro2GO). This matters for curation: the informative, well-supported generalization (cAR4 is a GPCR that signals) is already captured, so the more specific cyclase-activating child term GO:0007189 adds a claim that outruns the evidence.

---

## Mechanistic Model / Interpretation

### Two functionally distinct arms of cAR signaling

The *Dictyostelium* cAR family comprises four sequentially expressed 7-transmembrane cAMP receptors (cAR1–cAR4). They fall into two functional regimes relevant to this hypothesis:

```
          AGGREGATION STAGE (early)                  LATE / SLUG-CULMINATION STAGE
          high-affinity cAR1, cAR3                    low-affinity cAR4 (carD)
                    |                                            |
        cAMP relay / chemotaxis                     axial (A–P) patterning
                    |                                            |
     +--------------+--------------+                +------------+------------+
     |                             |                |                         |
  Adenylyl cyclase (ACA)      ZAK1 -> GSK3      antagonizes GSK3         prestalk ON /
  activation                  ACTIVATION        (PTP activator,          prespore OFF
  (Pupillo 1992, cAR1/cAR3)   (Kim 1999)        GO:0008160 TAS)          (Louis 1994 IMP)
     |                                                 |
  GO:0007189                                   opposite sign to cAR1/cAR3
  (DIRECT evidence: cAR1/cAR3)                 (Ginsburg & Kimmel 1997)
     |
  cAR4: extended ONLY by "A.R. Kimmel, unpubl." + IBA
```

The experimentally demonstrated adenylyl-cyclase activation (GO:0007189) is anchored in the **early, high-affinity receptors** operating during the cAMP relay that drives aggregation. cAR4 operates in a **different developmental window** (tip elongation → culmination), is a **low-affinity** receptor, and its documented intracellular coupling is *antagonistic* to the cAR1/cAR3→ZAK1→GSK3 axis — cAR4 behaves as a GSK3 antagonist and protein-tyrosine-phosphatase activator, functionally opposite to the cyclase-relay receptors.

### Why the annotation looks like carry-over

Because all four cARs share a 7-TM GPCR architecture and cAMP-binding function, a phylogenetic pipeline (PAINT/PANTHER) will propagate an ancestor's cyclase-activation annotation to every descendant, including cAR4. This is a textbook mechanism for **paralog over-annotation**: an experimentally verified activity of one or two paralogs (cAR1/cAR3) is inherited by all clade members regardless of stage-, affinity-, or effector-specificity. The literature itself hedges on this exact point ("all of the CARs *may* be capable of adenylyl cyclase activation … A.R. Kimmel, unpubl.").

### Reconciling with the seed hypothesis

The seed hypothesis is careful and correct on two counts: (1) a GSK3-linked function does not logically exclude cyclase activation, and (2) unpublished observations quoted in a paper must be distinguished from published experiments. Applying both principles: the GSK3-antagonist role does not disprove cyclase activation, but the *only* affirmative statement for cyclase activation by cAR4 is precisely the kind of unpublished observation the hypothesis flags. There is therefore no positive published evidence to confirm, and the default should be conservative.

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt Q9TX43 (record) | Review/database | Qualifies | Is GO:0007189 on cAR4 experimental? | GO:0007189 assigned **IBA:GO_Central** (phylogenetic); cAMP binding (IDA), PTP activator (TAS), developmental BP (IMP) are the experimental terms | Database record | High for provenance; database-level |
| QuickGO API, Q9TX43 (GO_REF:0000033) | Review/database | Qualifies | Evidence class of GO:0007189 | Confirms PAINT phylogenetic inference (IBA/ECO:0000318); parent GO:0007186 already present as IEA | Database record | High; orientation only |
| [PMID: 7958880](https://pubmed.ncbi.nlm.nih.gov/7958880/) (Louis 1994) | Mutant phenotype / expression | Competing (assigns different core role) | cAR4 loss-of-function phenotype | car4-null: normal early development; late A–P patterning defects, reduced prestalk, expanded prespore; cAR4 mRNA at tip→culmination | *D. discoideum* pseudoplasmodia | High for developmental role; no cyclase assay |
| [PMID: 9284050](https://pubmed.ncbi.nlm.nih.gov/9284050/) (Ginsburg & Kimmel 1997) | Mutant phenotype + explicit unpublished note | Refutes published cyclase evidence / Competing | Does cAR4 activate adenylyl cyclase? | cAR4 antagonizes cAR1/cAR3, converges on GSK3; cyclase extension explicitly "A.R. Kimmel, **unpubl.**" | *D. discoideum* | High; cyclase claim is unpublished, not tested |
| [PMID: 1333842](https://pubmed.ncbi.nlm.nih.gov/1333842/) (Pupillo 1992) | Direct assay | Supports family, NOT cAR4 | Which cARs are linked to ACA? | cAR1 + "another" (cAR3, aggregation stage) linked to ACA; requires Gα2 | car1⁻/gα2⁻ aggregation-stage cells | High for cAR1/cAR3; cAR4 not tested |
| [PMID: 9578623](https://pubmed.ncbi.nlm.nih.gov/9578623/) (Kim 1998) | Direct assay | Supports family, NOT cAR4 | Do cAR subtypes share cyclase activation? | cAR1/cAR2/cAR3 all mediate ACA activation at different [cAMP]; C-termini interchangeable | Constitutive expression in car1⁻/car3⁻ | High for cAR1/2/3; **cAR4 excluded** |
| [PMID: 10571182](https://pubmed.ncbi.nlm.nih.gov/10571182/) (Kim 1999) | Direct assay / genetic | Competing (defines opposite arm) | How is GSK3 regulated by cARs? | ZAK1 (downstream of cAR3) phosphorylates & activates GSK3 in vitro; zak1-null defective | *D. discoideum* | High; positions cAR4 as antagonist |
| [PMID: 11121784](https://pubmed.ncbi.nlm.nih.gov/11121784/) (Weeks 2000) | Review | Qualifies | cAR3→ZAK1→GSK3 architecture | Extracellular cAMP stimulates GSK3 via cAR3/ZAK1; cAR4 antagonistic | Review | Moderate; review-level |
| [PMID: 8811185](https://pubmed.ncbi.nlm.nih.gov/8811185/) (review) | Review | Qualifies | cAR family couples to ACA/GC | cAR family acts on heterotrimeric G protein to stimulate adenylyl & guanylyl cyclases | Review | Moderate; family-level, not cAR4-specific |
| [PMID: 7496377](https://pubmed.ncbi.nlm.nih.gov/7496377/) (review) | Review | Qualifies | Distinct cAR subtype phenotypes | Four cAR subtypes with temporally/spatially distinct expression and distinct null phenotypes | Review | Moderate; supports subtype specialization |

---

## GO Curation Implications

**Lead (requires curator verification):** Treat GO:0007189 (*adenylate cyclase-activating G protein-coupled receptor signaling pathway*) on carD/cAR4 as a **non-core, family-level phylogenetic (IBA) annotation** rather than a receptor-specific experimental fact.

- **Evidence class:** BP-level, phylogenetically inferred (IBA / ECO:0000318 / GO_REF:0000033). No direct cAR4 assay behind it.
- **Retain / remove / generalize / make more specific?**
  - **Do not upgrade** to any experimental evidence code (IDA/IMP/IGI/TAS) — no direct cAR4 cyclase measurement exists; the only supporting statement is an unpublished observation quoted in [PMID: 9284050](https://pubmed.ncbi.nlm.nih.gov/9284050/).
  - **The informative parent already exists:** GO:0007186 (*G protein-coupled receptor signaling pathway*) is already annotated (IEA). This captures the well-supported generalization without over-committing to cyclase activation.
  - **Preferred stance:** either (a) retain GO:0007189 strictly as IBA with a curator note that it is family carry-over unverified for cAR4, or (b) if project policy removes IBA terms that conflict with a receptor's documented antagonistic/non-relay role, replace it with the parent GO:0007186 and rely on the experimentally grounded terms.
- **Best-supported, most informative terms to keep:** GO:0030552 cAMP binding (IDA); GO:0001646 cAMP receptor activity (ISS); GO:0008160 protein tyrosine phosphatase activator activity (TAS); and the IMP developmental BP terms from [PMID: 7958880](https://pubmed.ncbi.nlm.nih.gov/7958880/). These represent cAR4's demonstrated core function far better than GO:0007189.

We explicitly avoid recommending "protein binding" as a final term; cAMP binding (GO:0030552) and cAMP receptor activity (GO:0001646) are more informative and experimentally/ISS-supported.

---

## Mechanistic Scope

**Immediate molecular function being tested:** whether cAR4, upon binding extracellular cAMP, couples through a heterotrimeric G protein to **activate adenylyl cyclase** (raising intracellular cAMP) — the molecular meaning of GO:0007189.

**Direct gene-product activity that IS supported:** cAMP binding (GO:0030552, IDA); GPCR-type signal transduction (GO:0007186, IEA); and — inferred from mutant phenotypes and pathway epistasis — a coupling that **activates a protein tyrosine phosphatase** (GO:0008160, TAS), thereby **antagonizing the ZAK1→GSK3 axis**.

**Downstream phenotypes / pathway consequences (NOT the immediate MF):** anteroposterior axis formation, prestalk vs. prespore cell-fate specification, prestalk gene expression, prespore-marker restriction, culmination, and fruiting-body patterning. These are the *outcomes* of cAR4 signaling documented in car4-null mutants — developmental phenotypes, not a demonstration of cyclase activation.

The critical scope distinction: **cyclase activation is a proposed proximal biochemical activity never directly measured for cAR4**, whereas the patterning defects are loss-of-function *phenotypes* several steps removed from any specific effector. Attributing GO:0007189 to cAR4 conflates a family-level proximal activity with cAR4's documented developmental role.

---

## Conflicts and Alternatives

1. **Paralog confusion / carry-over (primary alternative):** The cyclase-activation evidence belongs to cAR1 and cAR3 (Pupillo 1992, [PMID: 1333842](https://pubmed.ncbi.nlm.nih.gov/1333842/); Kim 1998, [PMID: 9578623](https://pubmed.ncbi.nlm.nih.gov/9578623/)). PAINT propagates it to cAR4 by ancestry — the most parsimonious explanation for the GO:0007189 annotation on carD.

2. **Stage / affinity mismatch:** cAR1/cAR3 operate during aggregation-stage cAMP relay; cAR4 is a low-affinity receptor expressed only later (tip→culmination). The relay-associated cyclase activation is a property of the early receptors' context, which cAR4 does not obviously share.

3. **Functional opposition:** cAR4's documented intracellular coupling is *antagonistic* to cAR1/cAR3 (Ginsburg & Kimmel 1997, [PMID: 9284050](https://pubmed.ncbi.nlm.nih.gov/9284050/)), acting as a GSK3 antagonist / PTP activator — functionally opposite to the "activating" receptors, weakening a simple "all cARs do the same thing" argument.

4. **Unpublished vs. published evidence:** The only affirmative cAR4 cyclase statement is "A.R. Kimmel, unpubl." — not usable as published experimental support; the authors themselves hedge ("*may* be capable").

5. **Not excluded, merely unproven:** The seed's caution is valid — none of this *disproves* that cAR4 could activate cyclase if directly assayed. The alternative interpretations show why the current annotation over-reaches, not that cyclase activation is impossible.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct cAR4 cyclase assay | Primary papers (1992, 1994, 1997, 1998, 1999) — none assays cAR4 for ACA activation | Without it, GO:0007189 on cAR4 is inference only | cAMP-stimulated ACA activity assay with cAR4 as sole/primary receptor at its native stage |
| Content of "A.R. Kimmel, unpubl." | Full text of PMID:9284050 read; observation is unpublished | Curators must not treat it as a published experiment | Locate any later Kimmel-lab publication/dataset reporting the assay |
| cAR4 affinity/effector coupling | Literature: low affinity, antagonistic role | Determines whether cAR4's G-protein coupling can activate ACA at all | Reconstitution / G-protein coupling assays with defined Gα partners |
| cAR4 C-terminus divergence | Kim 1998 showed cAR1/2/3 C-termini interchangeable; cAR4 not tested | C-terminal divergence could alter effector coupling | Chimera swap of cAR4 C-terminus into cAR1 backbone with ACA readout |
| Current PAINT tree / annotation status | UniProt + QuickGO checked (both IBA/GO_REF:0000033) | Annotation may be revised in newer releases | Re-check GO_Central PAINT family tree and any NOT-qualifier annotations |

---

## Discriminating Tests / Proposed Follow-up Experiments

1. **Direct adenylyl-cyclase activation assay for cAR4** — the decisive experiment. Express cAR4 in a car1⁻/car3⁻ background (as in Kim 1998) or at its native late stage, stimulate with cAMP across the receptor's affinity range, and measure ACA activation kinetics. A positive result would justify an experimental GO:0007189; a negative result would support removing/qualifying it.

2. **C-terminal chimera swap** — replace the cAR1 C-terminus with cAR4's and test whether ACA activation persists, isolating whether cAR4-specific sequence features preclude cyclase coupling.

3. **G-protein coupling profile** — identify which Gα cAR4 couples to and whether that Gα is ACA-competent (cAR1/cAR3 require Gα2, per Pupillo 1992).

4. **Stage-resolved cAMP measurement** in car4-null vs. wild-type at tip/culmination to test whether cAR4 loss alters intracellular cAMP (a phenotype-level proxy for cyclase involvement).

5. **Literature / dataset audit** for any post-1997 publication reporting the "unpublished" cAR4 cyclase observation, to settle the published-vs-unpublished question definitively.

---

## Curation Leads (require curator verification)

**Candidate action change:**
- **Downgrade / annotate as non-core:** flag GO:0007189 on carD as family-level IBA carry-over; do not present it as receptor-specific function. Options: (a) retain as IBA with curator note; (b) generalize to the already-present parent GO:0007186. **Do not** attach an experimental evidence code.

**Candidate references and exact snippets to verify:**
- [PMID: 9284050](https://pubmed.ncbi.nlm.nih.gov/9284050/) — verify verbatim: *"all of the CARs may be capable of adenylyl cyclase activation (Pupillo et al. 1992; A.R. Kimmel, unpubl.)"* and *"it is difficult to predict definitively which specific intracellular responses are affected by the loss of CAR4, a low-affinity receptor."*
- [PMID: 1333842](https://pubmed.ncbi.nlm.nih.gov/1333842/) — verify that the assayed receptors are cAR1 and "another" (cAR3), in car1⁻/gα2⁻ aggregation-stage cells; cAR4 not present.
- [PMID: 9578623](https://pubmed.ncbi.nlm.nih.gov/9578623/) — verify only cAR1/cAR2/cAR3 assayed for ACA activation; cAR4 excluded.
- [PMID: 7958880](https://pubmed.ncbi.nlm.nih.gov/7958880/) — verify cAR4 expression window (tip→culmination) and car4-null patterning phenotype (source of the IMP BP terms).

**Candidate GO terms to prefer (retain / emphasize):**
- GO:0030552 cAMP binding (IDA) — retain
- GO:0001646 cAMP receptor activity (ISS) — retain
- GO:0008160 protein tyrosine phosphatase activator activity (TAS, PMID:12408804) — retain; best captures cAR4's distinctive coupling
- GO:0007186 G protein-coupled receptor signaling pathway (IEA) — retain as the informative parent
- Developmental IMP BP terms (cell differentiation, culmination, +/- regulation of gene expression; PMID:7958880) — retain

**Suggested curator questions:**
- Should family-level IBA terms that conflict with a paralog's experimentally documented (antagonistic, non-relay) role be retained, qualified, or removed under project policy?
- Is there any post-1997 publication converting the "A.R. Kimmel, unpubl." cyclase observation into a citable experiment?

**Suggested experiment (for the record):** a direct cAMP-stimulated adenylyl-cyclase assay with cAR4 as the operative receptor at its native developmental stage — the single result that would move GO:0007189 from inference to experimental support (or refute it).

---

## Summary Statement

GO:0007189 on carD/cAR4 is **weakly supported and best treated as a family-level phylogenetic (IBA) carry-over**. The direct adenylyl-cyclase evidence belongs to cAR1/cAR3 at the aggregation stage; cAR4 was never assayed, is expressed later as a low-affinity receptor, and its documented role (late axial patterning via GSK3 antagonism / PTP activation) is functionally distinct. The lone affirmative cyclase statement for cAR4 is an explicitly unpublished observation. Curators should keep the experimentally grounded MF/BP terms, rely on the already-present GPCR-signaling parent, and refrain from upgrading GO:0007189 absent a direct cAR4 cyclase assay.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist carD GO0007189 evidence matrix](openscientist_artifacts/provenance_carD_GO0007189_evidence_matrix.csv)
- [OpenScientist carD quickgo annotations](openscientist_artifacts/provenance_carD_quickgo_annotations.csv)
- [OpenScientist carD uniprot GO evidence](openscientist_artifacts/provenance_carD_uniprot_GO_evidence.csv)