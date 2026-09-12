---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-08T14:06:17.522216'
end_time: '2026-07-08T14:23:04.893628'
duration_seconds: 1007.37
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ORYSI
  gene: B8BAB0
  gene_symbol: B8BAB0
  uniprot_accession: B8BAB0
  taxon_id: NCBITaxon:39946
  taxon_label: Oryza sativa subsp. indica
  focus_type: computational_prediction
  hypothesis_slug: prediction-pollen-maturation
  hypothesis_text: ProtNLM2 predicts that the Oryza sativa (indica) BURP domain-containing
    protein B8BAB0 functions in pollen maturation (GO:0010152); it has no curated
    GOA annotations and no direct experimental characterization (UniProt PE level
    4). Some BURP-domain family members have roles in reproductive development. Independently
    assess whether B8BAB0's domain architecture (BURP domain, signal peptide, family
    subclass) and any orthology or expression evidence support a specific role in
    pollen maturation, or whether that specific process assignment cannot be established
    from sequence alone.
  term_context: '- Term: pollen maturation (GO:0010152)'
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: ProtNLM2 predicts that the Oryza sativa (indica)\
    \ BURP domain-containing protein B8BAB0 functions\n  in pollen maturation (GO:0010152);\
    \ it has no curated GOA annotations and no direct experimental characterization\n\
    \  (UniProt PE level 4). Some BURP-domain family members have roles in reproductive\
    \ development. Independently\n  assess whether B8BAB0's domain architecture (BURP\
    \ domain, signal peptide, family subclass) and any orthology\n  or expression\
    \ evidence support a specific role in pollen maturation, or whether that specific\
    \ process\n  assignment cannot be established from sequence alone.\nfocus_type:\
    \ computational_prediction\nterm_id: GO:0010152\nterm_label: pollen maturation\n\
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
- filename: evidence_matrix_B8BAB0.csv
  path: openscientist_artifacts/evidence_matrix_B8BAB0.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix B8BAB0
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
- filename: go_decision_table_B8BAB0.csv
  path: openscientist_artifacts/go_decision_table_B8BAB0.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table B8BAB0
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ORYSI
- **Taxon:** Oryza sativa subsp. indica (NCBITaxon:39946)
- **Gene directory:** B8BAB0
- **Gene symbol:** B8BAB0
- **UniProt accession:** B8BAB0

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-pollen-maturation
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

ProtNLM2 predicts that the Oryza sativa (indica) BURP domain-containing protein B8BAB0 functions in pollen maturation (GO:0010152); it has no curated GOA annotations and no direct experimental characterization (UniProt PE level 4). Some BURP-domain family members have roles in reproductive development. Independently assess whether B8BAB0's domain architecture (BURP domain, signal peptide, family subclass) and any orthology or expression evidence support a specific role in pollen maturation, or whether that specific process assignment cannot be established from sequence alone.

## Term and Decision Context

- Term: pollen maturation (GO:0010152)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: ProtNLM2 predicts that the Oryza sativa (indica) BURP domain-containing protein B8BAB0 functions
  in pollen maturation (GO:0010152); it has no curated GOA annotations and no direct experimental characterization
  (UniProt PE level 4). Some BURP-domain family members have roles in reproductive development. Independently
  assess whether B8BAB0's domain architecture (BURP domain, signal peptide, family subclass) and any orthology
  or expression evidence support a specific role in pollen maturation, or whether that specific process
  assignment cannot be established from sequence alone.
focus_type: computational_prediction
term_id: GO:0010152
term_label: pollen maturation
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
prompt so the report can be compared against them after the run.

Do not rely on literature alone. Where the hypothesis is decidable by computation,
actually run the analysis and keep it as provenance rather than only reasoning
about it. Match the analysis to the question, for example:

- membrane topology / localization: compute a hydropathy profile and predicted
  transmembrane segments from the sequence, and locate signal peptides and
  targeting/sorting motifs (e.g. dileucine, acidic-cluster, NLS); compare against
  UniProt topology features and AlphaFold geometry.
- catalytic / binding activity: check whether the specific active-site,
  metal-binding, or motif residues are present and correctly spaced (in sequence
  and, where useful, structure) and compare to characterized family members.
- DNA-binding / regulatory: examine the binding-domain class, obligate partners,
  and known binding-motif / PWM signatures.
- family / paralog questions: use domain (Pfam/InterPro), orthology, and
  conservation comparisons to distinguish subfamilies.

Use resources you can actually access programmatically (UniProt, AlphaFold DB,
InterPro, sequence computation, public APIs). If a resource is web-only or you
cannot run a check, say so plainly instead of guessing — never fabricate a result,
and an inconclusive or "could not run" analysis is an acceptable and useful
outcome. Report all computational results conservatively and prefer recording the
underlying analysis (code, computed values, table, or plot) as provenance.

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

# B8BAB0 (Oryza sativa subsp. indica) — Evaluation of ProtNLM2 "pollen maturation (GO:0010152)" prediction

**Focus type:** computational_prediction · **Term under test:** pollen maturation (GO:0010152)
**Gene:** B8BAB0 / OsI_29064 / Gramene BGIOSGA028580 (chromosome 8) · **UniProt PE:** 4 (Predicted) · **Curated GO annotations:** none
**Japonica ortholog:** OsBURP12 / UniProt Q6ZA27 (86.7% id) = **RAP-DB Os08g0380100** (KEGG dosa:Os08g0380100) — use this locus for RiceXPro/RAP-DB expression lookup.

---

## Executive Judgment

**Verdict: REFUTED / over-annotated for the specific term GO:0010152 (pollen maturation).**

The ProtNLM2 prediction of *pollen maturation* is **not supported** by domain architecture, subfamily
placement, orthology, or structure. B8BAB0 is unambiguously a member of the **PG1β-like (polygalacturonase
non-catalytic β-subunit-like) subfamily** of BURP-domain proteins — a **secreted cell-wall / pectin-associated**
clade — and is **not** a member of the cereal anther-specific **RAFTIN / BURP-VII** clade that supplies the only
well-documented "reproductive development" precedent among BURP proteins. The prediction appears to be a
frequency/superfamily over-generalization: it borrows the "some BURP proteins act in reproduction" association
(true only for the distinct RAFTIN clade) and applies it to a protein that actually belongs to the cell-wall clade.

**Most important caveat:** I could not retrieve B8BAB0-specific pollen/anther expression data programmatically.
Sequence and structure cannot, by themselves, exclude tissue-specific expression; however, the seed hypothesis
asks whether a *specific* pollen-maturation process can be established from sequence — and it cannot. If anything,
the supportable homology leads point to **extracellular/cell-wall localization** and **pectin/cell-wall metabolism**,
not pollen maturation.

---

## Evidence Matrix

| # | Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| 1 | This work (UniProt B8BAB0; InterPro/PANTHER/Pfam) | computational / database | qualifies | What subfamily is B8BAB0? | Signal peptide 1–21; BURP domain 384–595 (Pfam PF03181); **InterPro IPR051897 "PG-associated BURP"; PANTHER PTHR31458:SF2 "Polygalacturonase 1 beta-like protein 2"** | O. sativa indica, in silico | High; independent classifiers concur |
| 2 | This work (BLOSUM62 Needleman–Wunsch) | structural/evolutionary (computational) | refutes | Is B8BAB0 RAFTIN-like or PG1β-like? | **46.5% id to tomato PG1β (Q40161, score +1250); 44.9% to AroGP3 (P93218, +1163); only 28.2% to wheat RAFTIN1A (Q70KG5, NEGATIVE score −567)** and 20–27% to other rice BURPs (negative scores) | full-length alignment | High; classic PG1β ortholog-level identity vs BURP-domain-only similarity to RAFTIN |
| 3 | PMID 1392611 (Zheng 1992) | direct characterization | refutes/qualifies | What is the PG1β β-subunit repeat & function? | β-subunit is a fruit cell-wall glycoprotein "composed almost entirely of the novel 14-aa motif **FTNYGxxGNGGxxx**"; associates with & regulates catalytic PG2 | tomato fruit | High; B8BAB0 carries this diagnostic repeat (`GFTNYGESGN`, `TFAGYGKNGN`, ~37% of protein) |
| 4 | PMID 14612572 (Wang 2003) | mutant phenotype / localization | competing | Do BURP proteins act in pollen? | **RAFTIN** (anther-specific, Ubisch-body/exine, essential for pollen) — but "occurrence of RAFTIN per se is limited to cereals," a *distinct* BURP clade | rice/wheat anther | High; establishes RAFTIN as the reproductive precedent — B8BAB0 is NOT in this clade (evidence #2) |
| 5 | PMID 24237159 (Liu 2014) | mutant phenotype | refutes | Function of the rice PG1β-like clade | **OsBURP16 (rice PG1β β-subunit)**: stress-inducible; overexpression ↓pectin, ↓cell adhesion, ↑abiotic-stress sensitivity | rice, whole plant | High; nearest functional analog of B8BAB0's clade — cell-wall/pectin, not pollen |
| 6 | PMID 26106400 (Park 2015) | mutant phenotype / localization | qualifies | Function of PG1β-like proteins | **AtPGL3** (Arabidopsis PG1β-like) localizes to **cell wall**, promotes cell enlargement; BURP domain required | Arabidopsis leaf | High; cell-wall function, not reproductive |
| 7 | PMID 11554479 (Brummell 2001) | review | qualifies | Role of PG β-subunit | β-subunit protein "plays a role in limiting pectin solubilization"; affects middle lamella / cell adhesion | tomato fruit | Medium (review); mechanistic orientation |
| 8 | PMID 12232274 (Zheng 1994) | expression / direct | qualifies | Where is PG1β expressed? | β-subunit fruit-predominant but also low levels in root, leaf, **flower**; developmentally (not ethylene) regulated | tomato | Medium; shows flower expression ≠ pollen-maturation function |
| 9 | PMID 19363683 (Ding 2009) | expression / phylogenetic | refutes/qualifies | Which rice BURP clade is flower-predominant? | 17 OsBURP genes, 7 subfamilies; **flower-predominant genes = monocot-specific "BURP VII" clade** (RAFTIN-type); most others stress-induced | rice tissues | High; B8BAB0 (PG1β-like) is a *different* subfamily from the flower-predominant one |
| 10 | This work (AlphaFold AF-B8BAB0-F1 v6) | structural (computational) | qualifies | Is the BURP domain a real fold? | BURP domain (384–595) mean pLDDT **85.4** (well-folded); repeat region 77.6; N-term/signal 63.4; overall 74.6 | in silico model | Medium-High; confirms folded BURP domain, no catalytic/pollen inference |

---

## GO Curation Implications (leads — require curator verification)

| GO aspect | Candidate term | Recommended action | Basis / evidence code |
|-----------|----------------|--------------------|------------------------|
| **BP** | **pollen maturation (GO:0010152)** — the predicted term | **DO NOT ADD / REMOVE if present.** Not supported by domain, subfamily, orthology, or structure. | Over-generalization from BURP superfamily; B8BAB0 is PG1β-like, not RAFTIN-like (#2,#4,#9) |
| **CC** | **apoplast (GO:0048046)** or **extracellular region / cell wall (GO:0005576 / GO:0005618)** | Candidate ISS lead (curator to verify) | Signal peptide + Glycoprotein keyword; PG1β/AtPGL3/GmRD22 all cell-wall/apoplast (#3,#6) |
| **BP** | **plant-type cell wall organization (GO:0009664)** or **pectin catabolic process (GO:0045490)** *(as non-catalytic partner)* | Weak ISS lead only; note β-subunit is **non-catalytic** | PG1β/OsBURP16 modulate pectin & cell adhesion (#3,#5,#7) |
| **MF** | polygalacturonase activity (GO:0004650) | **DO NOT ADD.** B8BAB0 is the *non-catalytic* β subunit; it is not a hydrolase. | #3,#5 |
| **MF** | protein binding | Avoid as a final term; the informative interaction (binding catalytic PG) is inferred from tomato only, not demonstrated for rice B8BAB0 | #3 |

**Bottom line for the curator:** the ProtNLM2 BP term should be treated as an **incorrect computational
prediction (over-annotation)** and not propagated. If any homology-based annotation is desired, the defensible
leads are **CC = cell wall/apoplast** and (weaker) **BP = cell-wall/pectin organization**, all as ISS/IEA-level
leads requiring curator verification — never as experimental evidence.

---

## Mechanistic Scope

- **Immediate/direct gene-product function (what is testable):** a **secreted (signal peptide-bearing),
  glycosylated, low-complexity-repeat BURP protein** of the PG1β β-subunit type. In the characterized paradigm
  the β-subunit is **non-catalytic** and acts as a **cell-wall structural/regulatory partner** that binds and
  modulates a catalytic polygalacturonase and limits pectin solubilization (tomato PG1; #3,#7).
- **Downstream/indirect (NOT the direct molecular function):** fruit softening, cell adhesion/expansion, and
  abiotic-stress tolerance are downstream cell-wall consequences seen for orthologs (#5,#6,#7). "Pollen
  maturation" is neither the direct activity nor an established downstream phenotype for this clade.

---

## Conflicts and Alternatives

- **Superfamily-vs-subfamily confusion (most likely source of the prediction):** BURP is a large, functionally
  diverse superfamily. The reproductive-development association is real for the **RAFTIN/BURP-VII** clade
  (#4,#9) but does **not** transfer to the PG1β-like clade that B8BAB0 occupies (#2). ProtNLM2 likely
  over-generalized at the superfamily level.
- **Architecture look-alike:** B8BAB0's signal-peptide + long tandem-repeat + C-terminal BURP layout superficially
  resembles RAFTIN, which could mislead an alignment-free predictor; but the repeat is the **PG1β β-subunit
  `FTNYGxxGNGG` motif** (#3), and quantitative alignment cleanly separates the two clades (#2).
- **Flower expression ≠ pollen maturation:** tomato PG1β is detectable at low levels in flowers (#8); such
  expression, if it existed for B8BAB0, would not by itself justify the specific process term.
- **Organism/paralog note:** B8BAB0 is the indica ortholog of japonica **OsBURP12 (Q6ZA27, 86.7% id)**; its
  paralog OsBURP14 (53.3% id) is more divergent. None of these is characterized as a pollen factor.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| B8BAB0-specific expression | UniProt, literature (PMID 19363683 family-level only); EBI Atlas & Bgee queried programmatically — no gene-level expression call returned (web-only atlases) | A curator could argue for tissue-specific pollen expression | RiceXPro / CREP / RAP-DB anther & pollen-stage RNA-seq for **japonica ortholog RAP locus Os08g0380100 (OsBURP12)** or indica BGIOSGA028580 |
| Direct in-planta function of OsBURP12 | No mutant/RNAi study found | The clade function is inferred from tomato/OsBURP16, not this gene | T-DNA/CRISPR knockout phenotyping in rice (cell-wall, fertility) |
| Interaction with a catalytic PG | Inferred from tomato PG1 only (#3) | Determines whether a "pectin/cell-wall" BP is defensible | Co-IP / pulldown of B8BAB0 with rice polygalacturonases |

---

## Discriminating Tests

1. **Tissue expression:** query anther-developmental-stage RNA-seq (RiceXPro/CREP) for BGIOSGA028580/OsBURP12.
   Pollen-maturation support would require strong, stage-specific anther/microspore expression *and* a loss-of-function
   pollen phenotype — the RAFTIN standard (#4).
2. **Reciprocal-best-hit / tree:** build a BURP-domain ML tree placing B8BAB0 among RAFTIN (BURP VII) vs PG1β-like
   references; the alignment scores here (#2) predict it falls with PG1β/OsBURP16.
3. **Knockout phenotype:** CRISPR knockout of OsBURP12; score seed set/pollen viability (RAFTIN-type) vs cell-wall/
   pectin/stress traits (OsBURP16-type). The latter is expected.

---

## Curation Leads (require curator verification)

- **Action change:** flag ProtNLM2 `pollen maturation (GO:0010152)` as **NOT SUPPORTED (over-annotation)** — do not
  add; remove/mark if present. Rationale: PG1β-like subfamily, not RAFTIN clade.
- **Candidate replacement leads (ISS/IEA, homology only):**
  - CC `apoplast (GO:0048046)` / `cell wall (GO:0005618)` — from signal peptide + PG1β/AtPGL3 localization.
  - BP `plant-type cell wall organization (GO:0009664)` — weak; note non-catalytic β-subunit role.
- **Candidate references + exact snippets to verify:**
  - PMID **1392611**: "*composed almost entirely of the novel 14-amino acid motif FTNYGxxGNGxxx*" and "*a cell wall
    protein that associates with, and apparently regulates, the catalytic PG2 polypeptides*".
  - PMID **24237159**: "*OsBURP16 belongs to the PG1β-like subfamily of BURP-family genes and encodes one putative
    PG1β subunit precursor in rice*".
  - PMID **26106400**: "*A C-terminal GFP fusion protein of AtPGL3 … localized to the cell wall*".
  - PMID **14612572**: "*occurrence RAFTIN per se is limited to cereals*" (defines the *separate* reproductive clade).
  - PMID **19363683**: "*all the genes of the BURP VII subfamily were predominantly expressed in flower organs*"
    (the flower clade is distinct from B8BAB0's PG1β-like clade).
- **Suggested curator questions:** Is there anther/pollen-stage expression for BGIOSGA028580? Any rice OsBURP12
  functional study? Is the review's prior action consistent with "no experimental support; homology → cell wall"?
- **Suggested experiments:** RNA-seq tissue profiling; CRISPR knockout fertility/cell-wall phenotyping; PG co-IP.

---

## Limitations

- No wet-lab or B8BAB0-specific expression data were accessible; conclusions rest on sequence/structure/orthology
  computation plus primary literature on orthologs. This is sufficient to judge the *sequence-based* prediction
  but does not positively assign a validated function.
- Percent identities are from a custom global BLOSUM62 alignment (provenance retained), not a curated MSA; values
  are approximate but the clade separation (positive vs negative alignment scores) is robust.

*Provenance: sequence analyses, alignments, motif detection, and AlphaFold pLDDT parsing were executed during this
investigation (Iterations 1–2) and recorded in the knowledge state; an evidence-matrix CSV accompanies this report.*


## Artifacts

- [OpenScientist evidence matrix B8BAB0](openscientist_artifacts/evidence_matrix_B8BAB0.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table B8BAB0](openscientist_artifacts/go_decision_table_B8BAB0.csv)